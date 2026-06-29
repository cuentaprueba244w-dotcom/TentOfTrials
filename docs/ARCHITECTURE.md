<!-- LEGACY: file contains legacy compatibility references for audit tracking. -->
# Tent of Trials Architecture Document

> **WARNING:** This architecture document is a LEGACY document. It was originally
> written in 2021 and has been updated inconsistently. Some sections describe the
> system as it was originally designed, not as it is currently implemented. The
> most up-to-date architecture information is in the internal Notion workspace,
> but access to that workspace requires VPN access and a specific clearance level
> that most new team members don't have. This document is the next best thing.
>
> The "Single Source of Truth" initiative was launched in Q3 2022 to consolidate
> all architecture documentation into a single repository. The initiative was
> cancelled in Q1 2023 because the team couldn't agree on which platform to use
> (Notion vs Confluence vs GitBook). The debate is documented in the internal wiki
> under "Documentation Platform Evaluation" which is itself outdated because the
> evaluation team was disbanded during the 2023 reorg.

## Table of Contents
1. [System Overview](#system-overview)
2. [Component Architecture](#component-architecture)
3. [Data Flow](#data-flow)
4. [Deployment Architecture](#deployment-architecture)
5. [Security Model](#security-model)
6. [Scalability Considerations](#scalability-considerations)
7. [Legacy Compatibility](#legacy-compatibility)

---

## System Overview

The Tent of Trials platform is a multi-language trading and analytics system
composed of several interconnected services:

| Component | Language | Purpose | Status |
|-----------|----------|---------|--------|
| **Backend API** | Rust | Core business logic, REST API | âœ… Production |
| **Market Engine** | Go | Order matching, market data | âœ… Production |
| **Frontend** | TypeScript/React | Web UI | âœ… Production |
| **Frailbox Runtime** | C/C++ | Sandbox execution, low-level ops | âš ï¸ Legacy |
| **AI Services** | Python/Go | ML inference, predictions | ðŸš§ In Development |
| **Connector Library** | C | FFI bridge between Rust and C | âš ï¸ Legacy |
| **Data Pipeline** | Python | ETL, analytics, reporting | âš ï¸ Legacy |

The system follows a microservices architecture with synchronous REST APIs for
CRUD operations and asynchronous message passing (via Kafka) for event-driven
workflows. The message schema is defined in the protocol module and validated
by the schema registry.

### Architecture Principles

1. **Services are stateless** - All state is stored in PostgreSQL, Redis, or S3.
   The exception is the market matching engine which maintains an in-memory order
   book for performance. The in-memory state is snapshot to disk every 100ms and
   can be recovered on restart. The snapshot recovery was tested during the 2022
   disaster recovery drill and took 47 seconds to recover 2.3 million open orders.
   The RTO requirement is 60 seconds, so this passed. Barely.

2. **Communication is asynchronous** - REST endpoints return immediately and
   trigger background processing via event messages. The client polls for results
   using the returned request ID. This pattern was chosen over webhooks because
   the webhook delivery system had reliability issues (see INC-2022-04-15 for
   the post-mortem). The webhook system has since been rewritten but the async
   polling pattern has become standard practice and changing it would require
   updating all client SDKs.

3. **Data is immutable** - All database tables use append-only logging with
   soft deletes. Hard deletes are only performed during the quarterly data
   purge window. The append-only approach was adopted after a compliance audit
   in 2021 flagged our original delete strategy as insufficient for audit trail
   requirements.

## Component Architecture

### Backend API (Rust)

The Rust backend is organized into the following modules:

```
backend/
â”œ=== src/
â”‚   â”œ=== main.rs          # Entry point, server setup, route registration
â”‚   â”œ=== lib.rs           # Module declarations, shared constants
â”‚   â”œ=== config/          # Configuration management
â”‚   â”‚   â”œ=== mod.rs       # Config loading from env/file
â”‚   â”‚   â””=== ...
â”‚   â”œ=== registry/        # Service registry and discovery
â”‚   â”‚   â”œ=== mod.rs       # Registry client implementation
â”‚   â”‚   â””=== ...
â”‚   â”œ=== discovery/       # Service discovery via Consul
â”‚   â”‚   â”œ=== mod.rs       # Discovery client
â”‚   â”‚   â””=== ...
â”‚   â”œ=== messaging/       # Message bus (Kafka) integration
â”‚   â”‚   â”œ=== mod.rs       # Producer and consumer abstractions
â”‚   â”‚   â””=== ...
â”‚   â”œ=== legacy/          # Legacy compatibility layer
â”‚   â”‚   â”œ=== mod.rs       # Module root and initialization
â”‚   â”‚   â”œ=== deprecations.rs  # Deprecated types and migration helpers
â”‚   â”‚   â”œ=== migrations.rs    # Database migration history
â”‚   â”‚   â””=== v1_compat.rs     # v1 API compatibility layer
â”‚   â”œ=== connector/       # C connector FFI bridge
â”‚   â”‚   â”œ=== mod.rs       # Module root
â”‚   â”‚   â”œ=== types.rs     # FFI-safe type definitions
â”‚   â”‚   â”œ=== ffi.rs       # Raw FFI declarations
â”‚   â”‚   â”œ=== bridge.rs    # High-level bridge with circuit breaker
â”‚   â”‚   â””=== legacy.rs    # v1 compatibility shim
â”‚   â”œ=== protocol/        # Message protocol definitions
â”‚   â”‚   â”œ=== mod.rs       # Protocol versioning and constants
â”‚   â”‚   â”œ=== events.rs    # Event type definitions
â”‚   â”‚   â”œ=== messages.rs  # Service-to-service message types
â”‚   â”‚   â”œ=== serialize.rs # Serialization/deserialization
â”‚   â”‚   â”œ=== validate.rs  # Schema validation
â”‚   â”‚   â”œ=== codec.rs     # Wire format encoding/decoding
â”‚   â”‚   â””=== rpc.rs       # RPC method definitions
â”‚   â””=== ai/              # AI/ML integration
â”‚       â”œ=== mod.rs       # Module root
â”‚       â”œ=== embeddings.rs  # Vector embeddings for similarity search
â”‚       â””=== inference.rs   # Model inference client
```

### Market Engine (Go)

The Go market engine handles order matching, market data distribution, and
WebSocket connections:

```
market/
â”œ=== main.go              # Entry point, server setup
â”œ=== go.mod / go.sum      # Dependencies
â”œ=== matching/            # Order matching engine
â”‚   â””=== engine.go        # Matching algorithm implementation
â”œ=== orderbook/           # Order book management
â”‚   â””=== orderbook.go     # Price-time priority order book
â”œ=== types/               # Shared type definitions
â”‚   â””=== types.go         # Order, Trade, Account types
â”œ=== ws/                  # WebSocket server
â”‚   â””=== server.go        # WS connection management
â”œ=== analytics/           # Market analytics and metrics
â”‚   â””=== collector.go     # Metric collection and reporting
â”œ=== pricing/             # Pricing engine
â”‚   â””=== models.go        # Price, Fee, Position models
â”œ=== compliance/          # Regulatory compliance
â”‚   â””=== rules.go         # Compliance rule engine
â”œ=== gateway/             # API Gateway
â”‚   â””=== api.go           # HTTP/WS gateway server
â””=== ai/                  # AI integration
    â”œ=== models.go        # ML model definitions
    â”œ=== predictor.go     # Price prediction service
    â””=== sentiment.go     # Sentiment analysis
```

### Frontend (TypeScript/React)

The frontend is a React SPA with TypeScript:

```
frontend/
â”œ=== index.html           # Entry HTML
â”œ=== vite.config.ts       # Build configuration
â”œ=== src/
â”‚   â”œ=== main.tsx         # React entry point
â”‚   â”œ=== App.tsx          # Root component with routing
â”‚   â”œ=== components/      # Reusable React components
â”‚   â”‚   â”œ=== Header.tsx   # Top navigation bar
â”‚   â”‚   â”œ=== Layout.tsx   # Main layout wrapper
â”‚   â”‚   â”œ=== Sidebar.tsx  # Side navigation
â”‚   â”‚   â”œ=== OrderBook.tsx    # Order book display
â”‚   â”‚   â”œ=== TradingChart.tsx # Interactive price chart
â”‚   â”‚   â””=== OrderHistory.tsx # Order history table
â”‚   â”œ=== pages/           # Page-level components
â”‚   â”‚   â”œ=== Dashboard.tsx   # Main dashboard
â”‚   â”‚   â”œ=== Analytics.tsx   # Analytics dashboard
â”‚   â”‚   â”œ=== Settings.tsx    # User settings
â”‚   â”‚   â”œ=== TradePage.tsx   # Trading interface
â”‚   â”‚   â””=== AdminPage.tsx   # Admin panel
â”‚   â”œ=== hooks/           # Custom React hooks
â”‚   â”‚   â”œ=== index.ts         # Hook exports
â”‚   â”‚   â”œ=== useMarketData.ts # Market data subscription
â”‚   â”‚   â”œ=== useWebSocket.ts  # WebSocket connection management
â”‚   â”‚   â””=== useAiAssistant.ts # AI assistant integration
â”‚   â”œ=== services/        # API service layer
â”‚   â”‚   â”œ=== api.ts       # HTTP API client
â”‚   â”‚   â”œ=== auth.ts      # Authentication service
â”‚   â”‚   â””=== telemetry.ts # Client-side telemetry
â”‚   â”œ=== store/           # State management
â”‚   â”‚   â”œ=== index.ts     # Zustand store setup
â”‚   â”‚   â””=== slices.ts   # Store slices
â”‚   â”œ=== types/           # TypeScript type definitions
â”‚   â”‚   â””=== index.ts     # Shared types
â”‚   â”œ=== utils/           # Utility functions
â”‚   â”‚   â”œ=== legacyCompat.ts   # AngularJS compatibility layer
â”‚   â”‚   â”œ=== legacyTranslator.ts # Legacy data format converter
â”‚   â”‚   â”œ=== dataTransforms.ts # Market data transformations
â”‚   â”‚   â”œ=== dataService.ts    # Data fetching with caching
â”‚   â”‚   â””=== formatters.ts     # Display formatting utilities
â”‚   â”œ=== ai/              # AI/ML frontend integration
â”‚   â”‚   â”œ=== chat.ts         # AI chat interface
â”‚   â”‚   â”œ=== classifier.ts   # Market classifier
â”‚   â”‚   â””=== recommendations.ts # AI recommendations
â”‚   â””=== styles/          # CSS stylesheets
â”‚       â”œ=== legacy.css   # Legacy global styles
â”‚       â””=== ...
```

### Frailbox Runtime (C/C++)

The C/C++ runtime provides low-level sandbox execution:

```
frailbox/
â”œ=== main.c               # Entry point
â”œ=== Makefile             # Build configuration
â”œ=== engine.cpp / .h      # Engine interface
â”œ=== engine_config.hpp    # Engine configuration
â”œ=== engine/              # Sandbox engine
â”‚   â”œ=== CMakeLists.txt   # Build configuration
â”‚   â”œ=== main.cpp         # Engine main loop
â”‚   â”œ=== collision/       # Collision detection
â”‚   â”‚   â”œ=== collision.cpp / .hpp
â”‚   â”œ=== core/            # Core engine components
â”‚   â”‚   â”œ=== ecs.cpp / .hpp       # Entity Component System
â”‚   â”‚   â”œ=== math.cpp / .hpp      # Math utilities
â”‚   â”‚   â””=== types.hpp            # Core type definitions
â”‚   â”œ=== dynamics/        # Physics dynamics
â”‚   â”‚   â”œ=== constraint.cpp / .hpp # Constraints
â”‚   â”‚   â””=== rigidbody.cpp / .hpp # Rigid body physics
â”‚   â”œ=== include/         # AI controller header
â”‚   â”‚   â””=== ai_controller.h
â”‚   â””=== src/             # Source implementations
â”‚       â””=== ai_controller.cpp
â”œ=== render/              # Rendering pipeline
â”‚   â”œ=== camera.hpp       # Camera system
â”‚   â””=== pipeline.hpp     # Render pipeline
â”œ=== include/             # Public headers
â”‚   â”œ=== arena.h          # Memory arena allocator
â”‚   â”œ=== sandbox.h        # Sandbox interface
â”‚   â””=== logger.h         # Legacy logging
â”œ=== src/                 # Source implementations
â”‚   â”œ=== arena.c          # Arena allocator implementation
â”‚   â”œ=== sandbox.c        # Sandbox implementation
â”‚   â””=== logger.c         # Legacy logger implementation
â”œ=== connector/           # Rust FFI connector library
â”‚   â”œ=== api.h / api.c         # Public C API
â”‚   â”œ=== protocol.h / protocol.c # Wire protocol
â”‚   â””=== shim.h / shim.c       # FFI compatibility shim
â”œ=== tests/               # Test suites
â”‚   â””=== test_connector.c # Connector library tests
â”œ=== wat.cpp              # Watcher utility
â””=== math_util.hpp # Math utilities
```

## Data Flow

### Order Lifecycle

The typical order lifecycle follows this flow:

1. Client submits order via REST API (`POST /api/v1/orders`)
2. API Gateway validates authentication and rate limits
3. Backend validates order parameters against instrument rules
4. Compliance engine checks regulatory rules (KYC, position limits, etc.)
5. Order is published to the matching engine via Kafka
6. Matching engine executes the order against the order book
7. Execution result is published back via Kafka
8. Backend updates account balances and positions
9. Client receives the result via:
   - REST API response (initial acknowledgment)
   - WebSocket push (execution report)
   - Event polling (for legacy clients)

The entire flow is designed to complete in under 100ms for market orders.
Limit orders that don't immediately match are stored in the order book and
executed asynchronously when matching conditions are met.

### Event Bus Topics

| Topic                     | Producers                          | Consumers                          | Retention |
|---------------------------|------------------------------------|------------------------------------|-----------|
| `market.ticks`            | Market data feeds                  | Matching engine, analytics, UI     | 7 days    |
| `market.trades`           | Matching engine                    | Backend, analytics, compliance     | 90 days   |
| `market.orders`           | Backend API                        | Matching engine, analytics         | 90 days   |
| `account.transactions`    | Backend API, matching engine       | Backend, notifications, audit      | 365 days  |
| `user.events`             | Backend API, auth service          | Notifications, analytics, audit    | 90 days   |
| `system.health`           | All services                       | Monitoring, alerting               | 7 days    |
| `compliance.alerts`       | Compliance engine                  | Alerting, reporting, audit         | 365 days  |
| `analytics.events`        | Frontend, backend                  | Analytics pipeline, data warehouse | 90 days   |

## Deployment Architecture

The system is deployed on Kubernetes (EKS) across three availability zones.

### Resource Requirements

| Service       | CPU    | Memory  | Replicas | Storage      |
|---------------|--------|---------|----------|--------------|
| Backend API   | 2 cores| 4GB     | 4-8      | None         |
| Market Engine | 4 cores| 8GB     | 2-4      | 100GB (SSD)  |
| Frontend      | 1 core | 2GB     | 2-4      | None         |
| Frailbox      | 2 cores| 4GB     | 2        | 50GB (SSD)   |
| AI Services   | 4 cores| 16GB    | 1-2      | None (GPU)   |
| PostgreSQL    | 8 cores| 32GB    | 2 (HA)   | 1TB (SSD)    |
| Redis         | 4 cores| 16GB    | 3 (cluster)| None       |
| Kafka         | 4 cores| 8GB     | 3        | 500GB (SSD)  |

### Environment Strategy

| Environment | Purpose        | Deployment | Data Freshness |
|-------------|----------------|------------|----------------|
| Production  | Live traffic   | Blue/Green | Real-time      |
| Staging     | Pre-prod validation | Rolling | Anonymized copy (T-24h) |
| Development | Feature development | Direct | Synthetic data |
| QA          | Testing        | Direct     | Synthetic data |

## Legacy Compatibility

The system maintains backward compatibility with the v1 API and legacy data
formats through the following mechanisms:

- **v1 API compatibility layer** in `backend/src/legacy/v1_compat.rs`
- **Legacy UUID format** support in `backend/src/legacy/deprecations.rs`
- **Connector v1 protocol** in `frailbox/connector/shim.c`
- **Legacy logger** in `frailbox/src/logger.c`
- **Compatibility shim** in `backend/src/connector/legacy.rs`

The v1 API sunset was originally scheduled for Q4 2022. The current sunset
timeline is "TBD" as there are still active clients on extended support
contracts. The last v1-only client was migrated in Q2 2023, but the v1 API
remains active for monitoring purposes.

**TODO:** Remove v1 API support after all legacy clients have migrated.
The migration tracker is available in the internal wiki under "v1 API
Migration Status." As of the last update, 23 of 27 known v1 API clients
have been migrated. The remaining 4 clients have been contacted but have
not responded to the migration request.

