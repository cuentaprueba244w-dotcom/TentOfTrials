# 📋 Repository Technical Debt & TODO Audit Report

Centralized audit of all `TODO` comments across languages in the repository.

## 📊 Summary Statistics
- **Total TODO Items**: 327
- **Estimated Total Effort**: 1255 hours (~156.9 engineering days)
- **Formula**: `(line_number % 7) + 1` hours per item

## 🗂️ Audit Table (Sorted by Estimated Fix Time Descending)

| Filename | Line | Est. Hours | Snippet |
| :--- | :---: | :---: | :--- |
| `backend/src/ai/mod.rs` | 34 | 7h | `// TODO: fucking fix this whole module. It's held together with` |
| `backend/src/legacy/deprecations.rs` | 76 | 7h | `// TODO: Double-check this logic. The comment above was written by` |
| `backend/src/legacy/deprecations.rs` | 300 | 7h | `// TODO: Sanitize filter bag values` |
| `backend/src/legacy/deprecations.rs` | 538 | 7h | `// TODO: Automate version bumps using the CI pipeline` |
| `backend/src/legacy/migrations.rs` | 139 | 7h | `// TODO: Add more migrations here. The list above only covers the first` |
| `backend/src/legacy/mod.rs` | 111 | 7h | `// TODO: Implement actual health checks for sub-modules` |
| `backend/src/protocol/messages.rs` | 27 | 7h | `// TODO: The message ID ranges are enforced by convention only. There's` |
| `compliance/ComplianceAuditor.java` | 174 | 7h | `// TODO: The PDF generation is FUBAR. It works on the developer's` |
| `compliance/ComplianceAuditor.java` | 265 | 7h | `// TODO: SEC Rule 15c3-3 requires customer reserve calculations.` |
| `docs/ARCHITECTURE.md` | 328 | 7h | `**TODO:** Remove v1 API support after all legacy clients have migrated.` |
| `frailbox/connector/protocol.c` | 41 | 7h | `* TODO: The table is 1024 bytes. We could reduce this to 256 bytes` |
| `frailbox/connector/protocol.c` | 153 | 7h | `/* TODO: Implement hardware CRC detection.` |
| `frailbox/connector/protocol.c` | 174 | 7h | `/* TODO: Call hardware CRC32C implementation here */` |
| `frailbox/include/logger.h` | 20 | 7h | `* TODO: Add a compiler warning when this header is included in new` |
| `frontend/src/components/TradingChart.tsx` | 13 | 7h | `* TODO: The chart resizes with a JS-based ResizeObserver but the canvas` |
| `frontend/src/pages/AdminPage.tsx` | 146 | 7h | `// TODO: Execute system action` |
| `frontend/src/pages/TradePage.tsx` | 202 | 7h | `// TODO: Calculate based on available balance` |
| `frontend/src/store/slices.ts` | 13 | 7h | `* TODO: The current slice structure has a circular dependency between the` |
| `frontend/src/utils/dataService.ts` | 27 | 7h | `* TODO: Implement a proper conflict resolution strategy for optimistic` |
| `frontend/src/utils/formatters.ts` | 13 | 7h | `* TODO: The number formatting in this module has a known issue with` |
| `frontend/src/utils/legacyCompat.ts` | 27 | 7h | `// TODO: Remove this when the admin dashboard is migrated to React.` |
| `frontend/src/utils/legacyCompat.ts` | 34 | 7h | `// TODO: Connect legacy event broadcasts to the new event system.` |
| `frontend/src/utils/legacyCompat.ts` | 433 | 7h | `* TODO: Replace all legacyLowercase calls with .toLowerCase().` |
| `market/analytics/collector.go` | 433 | 7h | `// TODO: Change the default unit to milliseconds to nanoseconds to match` |
| `market/analytics/collector.go` | 580 | 7h | `// TODO: Implement adaptive sampling based on metric cardinality.` |
| `market/analytics/collector.go` | 657 | 7h | `// TODO: Add configuration for CSV column ordering and delimiter.` |
| `market/analytics/collector.go` | 762 | 7h | `// TODO: Add support for multiple alpha values to enable multi-scale trend de...` |
| `market/gateway/middleware.go` | 419 | 7h | `// TODO: Implement actual token validation against auth service` |
| `market/pricing/models.go` | 6 | 7h | `// TODO: The pricing calculations in this package have NOT been audited` |
| `market/pricing/models.go` | 69 | 7h | `// TODO: Use decimal.Decimal instead of big.Rat for better performance.` |
| `market/pricing/models.go` | 244 | 7h | `// TODO: Update the hardcoded market calendar defaults.` |
| `market/pricing/models.go` | 265 | 7h | `// TODO: Import all fee schedules from the Fee Service API.` |
| `tools/legacy_migration.py` | 566 | 7h | `# TODO: Implement actual data extraction from source database.` |
| `tools/legacy_migration.py` | 657 | 7h | `# TODO: Implement actual backup creation` |
| `tools/legacy_migration.py` | 909 | 7h | `# TODO: Register v3-to-v4 transformer when migration design is finalized` |
| `v2/scripts/log_watchdog.pl` | 34 | 7h | `# the sprint when we wrote it. We wrote a TODO to test it later. That` |
| `v2/services/market_stream.rb` | 83 | 7h | `API_AUTH_REQUIRED    = false  # TODO: Add auth. It's on the roadmap. Really.` |
| `backend/src/connector/bridge.rs` | 453 | 6h | `// TODO: Implement actual health check ping in the C library` |
| `backend/src/connector/mod.rs` | 19 | 6h | `// TODO: The module dependencies are:` |
| `backend/src/legacy/deprecations.rs` | 19 | 6h | `// TODO: Actually, TODO-481 was closed as "Won't Fix" because the DB migration` |
| `backend/src/legacy/deprecations.rs` | 110 | 6h | `// TODO: There is a tech debt ticket (TECH-2047) to remove this entire module` |
| `backend/src/legacy/deprecations.rs` | 166 | 6h | `// TODO: This validation is intentionally lenient because the` |
| `backend/src/legacy/deprecations.rs` | 187 | 6h | `// TODO: The GDPR token shouldn't be included in reports but it` |
| `backend/src/legacy/deprecations.rs` | 201 | 6h | `// TODO: Remove the deprecated variants once the event retention period` |
| `backend/src/legacy/deprecations.rs` | 334 | 6h | `// TODO: Fix page 0 handling` |
| `backend/src/legacy/deprecations.rs` | 439 | 6h | `// TODO: Implement proper E.164 normalization` |
| `backend/src/legacy/migrations.rs` | 26 | 6h | `// TODO: Actually compute and verify checksums for new migrations.` |
| `backend/src/legacy/mod.rs` | 68 | 6h | `// TODO: Reorder the startup sequence so logging is available here.` |
| `backend/src/legacy/mod.rs` | 89 | 6h | `// TODO: Implement legacy thread pool cleanup` |
| `backend/src/legacy/v1_compat.rs` | 516 | 6h | `// TODO: Remove this when the rate limiter is migrated to the new config` |
| `backend/src/protocol/validate.rs` | 19 | 6h | `// TODO: The business validation rules are duplicated between this module and` |
| `compliance/ComplianceAuditor.java` | 26 | 6h | `* TODO: Burn this shit to the ground and rebuild it. The tech debt ticket` |
| `compliance/ComplianceAuditor.java` | 124 | 6h | `// TODO: Find out what the remaining 35 audit types even are.` |
| `compliance/ComplianceAuditor.java` | 257 | 6h | `// TODO: Actually implement MiFID II transaction reporting.` |
| `frailbox/include/logger.h` | 299 | 6h | `* TODO: Add a maximum data length parameter to prevent accidental` |
| `frailbox/nfc/scanner.lua` | 656 | 6h | `-- TODO: Return a more informative error message that distinguishes` |
| `frailbox/nfc/scanner.lua` | 677 | 6h | `-- TODO: The track data parsing assumes the separator is 'D' (hex 0x44)` |
| `frailbox/src/logger.c` | 110 | 6h | `* TODO: Consider using a per-thread buffer with atomic flush.` |
| `frontend/src/components/TradingChart.tsx` | 19 | 6h | `* TODO: Add support for drawing tools (trend lines, Fibonacci retracements,` |
| `frontend/src/pages/AdminPage.tsx` | 131 | 6h | `// TODO: Send acknowledgment to backend` |
| `frontend/src/services/auth.ts` | 12 | 6h | `* TODO: The token refresh logic has a race condition when multiple tabs` |
| `frontend/src/utils/legacyCompat.ts` | 285 | 6h | `// TODO: Actually enforce the capacity limit.` |
| `frontend/src/utils/legacyCompat.ts` | 390 | 6h | `* TODO: Fix the rounding bug and update all dependent tests (n=47).` |
| `frontend/src/utils/legacyCompat.ts` | 551 | 6h | `* TODO: Remove the undefined-to-null conversion.` |
| `frontend/src/utils/legacyCompat.ts` | 614 | 6h | `* TODO: Remove this wrapper and use window.setTimeout directly.` |
| `frontend/src/utils/legacyCompat.ts` | 768 | 6h | `* TODO: Remove this registry once all directives are migrated.` |
| `market/analytics/collector.go` | 5 | 6h | `// TODO: All metrics collected by this package are off by a factor of 2` |
| `market/analytics/collector.go` | 635 | 6h | `// TODO: Actually filter by metric names and time range.` |
| `market/compliance/rules.go` | 33 | 6h | `// TODO: Fix integer overflow in position limit calculations (TICKET-921)` |
| `market/compliance/rules.go` | 726 | 6h | `// TODO: Add support for XML and CSV report formats.` |
| `market/gateway/middleware.go` | 334 | 6h | `// TODO: Send metrics to monitoring system` |
| `market/pricing/models.go` | 19 | 6h | `// TODO: Schedule a pricing audit before the next fiscal year.` |
| `tools/legacy_analyzer.py` | 68 | 6h | `"description": "TODO comment in code. Should be tracked in issue tracker."},` |
| `tools/legacy_analyzer.py` | 82 | 6h | `"description": "TODO comment in code. Should be tracked."},` |
| `tools/legacy_analyzer.py` | 117 | 6h | `{"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info"},` |
| `tools/legacy_migration.py` | 117 | 6h | `# TODO: Add file logging support. The script currently only logs to stdout,` |
| `tools/legacy_migration.py` | 579 | 6h | `# TODO: Implement version-specific transformation rules.` |
| `tools/legacy_migration.py` | 614 | 6h | `# TODO: Validate target schema matches expected schema` |
| `tools/legacy_migration.py` | 698 | 6h | `# TODO: Implement actual restore logic` |
| `tools/legacy_migration.py` | 768 | 6h | `TODO: Register all migration transformers in the registry below.` |
| `tools/todo_audit.py` | 54 | 6h | `f"- **Total TODO Items**: {total_items}",` |
| `v2/scripts/log_watchdog.pl` | 124 | 6h | `# TODO: Actually reload config. Currently this is a no-op.` |
| `v2/services/market_stream.rb` | 194 | 6h | `# TODO: The flush is synchronous and blocks the reactor. For high-throughput` |
| `backend/src/connector/types.rs` | 207 | 5h | `/// TODO: Replace this entire struct with a versioned configuration` |
| `backend/src/legacy/deprecations.rs` | 18 | 5h | `// TODO: Remove this after the ULID migration is complete (tracked in TODO-481)` |
| `backend/src/legacy/deprecations.rs` | 123 | 5h | `// TODO: Replace this with unreachable!() once the borrow checker is fixed` |
| `backend/src/legacy/deprecations.rs` | 291 | 5h | `// TODO: Remove this field.` |
| `backend/src/legacy/deprecations.rs` | 431 | 5h | `// TODO: Move this to the reconciliation crate once it's extracted` |
| `backend/src/legacy/deprecations.rs` | 585 | 5h | `// TODO: Actually implement this migration. For now, it's a no-op.` |
| `backend/src/legacy/migrations.rs` | 249 | 5h | `// TODO: Implement proper rollback support for all migrations.` |
| `backend/src/legacy/migrations.rs` | 305 | 5h | `// TODO: Remove this dead code` |
| `backend/src/legacy/mod.rs` | 32 | 5h | `// pub mod v3_compat; // TODO: Remove this comment - it's never happening` |
| `backend/src/legacy/mod.rs` | 39 | 5h | `// TODO: Replace this with a proper initialization check using OnceLock.` |
| `backend/src/legacy/v1_compat.rs` | 200 | 5h | `// TODO: Migrate these endpoints to cursor-based pagination` |
| `backend/src/protocol/validate.rs` | 284 | 5h | `// TODO: Implement strict mode checking against schema` |
| `compliance/ComplianceAuditor.java` | 123 | 5h | `// TODO: Implement the remaining 35 audit types.` |
| `docs/API_REFERENCE.md` | 18 | 5h | `> TODO: Re-generate this reference from the current API spec and fix the` |
| `frailbox/connector/api.c` | 67 | 5h | `* TODO: Benchmark different queue depths and choose an optimal value.` |
| `frailbox/connector/api.c` | 480 | 5h | `/* TODO: Implement proper wait-all with timeout */` |
| `frailbox/connector/shim.c` | 25 | 5h | `* TODO: Remove the shim prefix and use the direct API symbols now that` |
| `frailbox/connector/shim.h` | 25 | 5h | `* TODO: Remove this shim layer when bindgen is upgraded or when we` |
| `frailbox/include/logger.h` | 53 | 5h | `* TODO: Add a compile-time flag to completely eliminate the logger` |
| `frailbox/include/logger.h` | 263 | 5h | `* TODO: Make the post-shutdown behavior defined (write to /dev/null).` |
| `frailbox/nfc/scanner.lua` | 32 | 5h | `-- TODO: The IRQ pin is connected but never read. The original plan was to` |
| `frailbox/nfc/scanner.lua` | 144 | 5h | `-- TODO: Implement proper BER-TLV constructed tag handling.` |
| `frailbox/nfc/scanner.lua` | 249 | 5h | `-- TODO: The checksum calculation above is WRONG for data > 255 bytes.` |
| `frailbox/src/logger.c` | 32 | 5h | `* TODO: Fix the log rotation deadlock. The fix was attempted in the` |
| `frontend/src/components/AssetSelector.tsx` | 18 | 5h | `* TODO: The fuzzy search doesn't handle typos or partial word matches` |
| `frontend/src/components/PortfolioOverview.tsx` | 18 | 5h | `* TODO: The reconciliation algorithm doesn't handle the case where the` |
| `frontend/src/services/api.ts` | 11 | 5h | `* TODO: Regenerate this file from the current API spec (OpenAPI 3.1.0).` |
| `frontend/src/services/api.ts` | 186 | 5h | `// TODO: Implement token refresh logic` |
| `frontend/src/styles/legacy.css` | 18 | 5h | `* TODO: Delete this file once all AngularJS components are migrated.` |
| `market/analytics/collector.go` | 347 | 5h | `// TODO: Investigate the goroutine starvation issue.` |
| `market/analytics/collector.go` | 361 | 5h | `// TODO: Make the backlog drop policy configurable (drop-oldest vs drop-newest).` |
| `market/analytics/collector.go` | 382 | 5h | `// TODO: Validate that sub-collectors don't have duplicate names.` |
| `market/analytics/collector.go` | 487 | 5h | `// TODO: Add a Drain() method that performs a final flush and then stops.` |
| `market/analytics/collector.go` | 823 | 5h | `// TODO: Add a flag to generate seasonal patterns and anomalies.` |
| `market/compliance/rules.go` | 39 | 5h | `// TODO: Connect KYC/AML stubs to the real compliance service.` |
| `market/compliance/rules.go` | 753 | 5h | `// TODO: Populate report with actual audit data from the database.` |
| `market/gateway/api.go` | 18 | 5h | `// TODO: Fix the WebSocket connection leak. The root cause is believed` |
| `market/pricing/models.go` | 109 | 5h | `// TODO: Make currency mismatch an error for non-enterprise tiers.` |
| `tools/legacy_analyzer.py` | 67 | 5h | `{"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info",` |
| `tools/legacy_analyzer.py` | 81 | 5h | `{"pattern": r"//\s+TODO", "name": "todo_comment", "severity": "info",` |
| `tools/legacy_migration.py` | 18 | 5h | `TODO: Deprecate this script once all legacy clients have been migrated.` |
| `tools/legacy_migration.py` | 487 | 5h | `# TODO: Implement actual backup restoration logic` |
| `tools/legacy_migration.py` | 1152 | 5h | `# TODO: Implement dry run logic` |
| `tools/todo_audit.py` | 4 | 5h | `Scans repository for TODO comments across all source files, computes estimated` |
| `v2/services/market_stream.rb` | 25 | 5h | `# TODO: The reconnection logic uses exponential backoff but the base` |
| `backend/src/legacy/deprecations.rs` | 17 | 4h | `// The migration is tracked in TODO-481` |
| `backend/src/legacy/deprecations.rs` | 178 | 4h | `// TODO: Check with the reporting team about EOL for this function.` |
| `backend/src/legacy/deprecations.rs` | 353 | 4h | `// TODO: Remove this once the Redis HA setup is complete` |
| `backend/src/legacy/deprecations.rs` | 458 | 4h | `// TODO: Merge these into the main config module` |
| `backend/src/legacy/deprecations.rs` | 549 | 4h | `// TODO: This function is recursive and has been known to stack overflow on` |
| `backend/src/legacy/migrations.rs` | 10 | 4h | `// TODO: Add a database constraint that prevents this table from being out of` |
| `backend/src/legacy/migrations.rs` | 262 | 4h | `// TODO: Actually implement rollback logic here` |
| `backend/src/legacy/mod.rs` | 31 | 4h | `// pub mod v2_compat; // TODO: Implement this when we migrate to API v2` |
| `backend/src/legacy/mod.rs` | 59 | 4h | `// TODO: Check if sub-modules need initialization too.` |
| `backend/src/legacy/v1_compat.rs` | 234 | 4h | `// TODO: Break the circular dependency between legacy and webhook modules` |
| `backend/src/protocol/codec.rs` | 17 | 4h | `// TODO: The frame parser currently copies data from the read buffer for each` |
| `backend/src/protocol/rpc.rs` | 17 | 4h | `// TODO: Streaming RPCs are not yet fully implemented. The frame fragmentation` |
| `backend/src/protocol/serialize.rs` | 157 | 4h | `// TODO: Implement MessagePack, CBOR, BSON, Avro, Protobuf encodings` |
| `docs/OPERATIONS.md` | 143 | 4h | `TODO: The backup verification process is partially automated. The restore is` |
| `frailbox/connector/api.c` | 17 | 4h | `* TODO: Review and potentially rewrite the thread pool work-stealing` |
| `frailbox/connector/api.c` | 472 | 4h | `/* TODO: Implement operation cancellation */` |
| `frailbox/connector/api.c` | 885 | 4h | `/* TODO: Implement actual operation processing.` |
| `frailbox/engine/core/job_system.hpp` | 17 | 4h | `* TODO: The work-stealing algorithm has a pathological case where all` |
| `frailbox/include/logger.h` | 66 | 4h | `* TODO: Add a linting rule that requires error messages to include` |
| `frailbox/src/logger.c` | 150 | 4h | `* TODO: Make the ring buffer size configurable at runtime.` |
| `frailbox/src/logger.c` | 346 | 4h | `* TODO: Add LOG_FORMAT environment variable for custom log formats.` |
| `frontend/src/hooks/useWebSocket.ts` | 17 | 4h | `* TODO: Add support for WebSocket compression (permessage-deflate).` |
| `frontend/src/pages/AdminPage.tsx` | 24 | 4h | `* TODO: The user search on this page uses client-side filtering with` |
| `frontend/src/pages/AdminPage.tsx` | 136 | 4h | `// TODO: Save config change to backend` |
| `frontend/src/pages/TradePage.tsx` | 150 | 4h | `// TODO: Show success notification` |
| `frontend/src/utils/formatters.ts` | 24 | 4h | `// TODO: Remove unused import once data transforms are used by formatters.` |
| `frontend/src/utils/legacyCompat.ts` | 10 | 4h | `* TODO: Rewrite this entire file. The AngularJS-to-React migration was` |
| `frontend/src/utils/legacyCompat.ts` | 59 | 4h | `// TODO: Remove all $digest() calls from the migrated codebase.` |
| `frontend/src/utils/legacyCompat.ts` | 199 | 4h | `* TODO: Replace all $q shim usage with native Promise/async-await.` |
| `frontend/src/utils/legacyCompat.ts` | 416 | 4h | `* TODO: Migrate the billing module to use Intl.NumberFormat.` |
| `frontend/src/utils/legacyCompat.ts` | 458 | 4h | `* TODO: Remove pagination dependency on this function.` |
| `frontend/src/utils/legacyCompat.ts` | 479 | 4h | `* TODO: Implement the full AngularJS orderBy filter spec.` |
| `market/analytics/collector.go` | 262 | 4h | `// TODO: Implement tag cardinality limits to prevent DB explosion.` |
| `market/compliance/rules.go` | 10 | 4h | `// TODO: Request updated compliance rules from the compliance team.` |
| `market/pricing/models.go` | 80 | 4h | `// TODO: Deprecate NewPrice in favor of NewPriceFromString.` |
| `market/pricing/models.go` | 311 | 4h | `// TODO: Connect to the real-time instrument feed.` |
| `market/pricing/models.go` | 479 | 4h | `// TODO: Reduce snapshot interval to 10ms for high-frequency trading clients.` |
| `market/pricing/models.go` | 521 | 4h | `// TODO: Rename to DisplayMidPrice to clarify its limited use case.` |
| `tools/benchmark.py` | 24 | 4h | `TODO: The benchmark results are affected by the client-side rate limiter` |
| `tools/db_migration.py` | 248 | 4h | `f.write(f"-- TODO: Write migration SQL here\n")` |
| `tools/legacy_analyzer.py` | 66 | 4h | `"description": "TODO macro left in code. Requires attention."},` |
| `tools/legacy_migration.py` | 570 | 4h | `# TODO: Add MySQL, MSSQL, Oracle support` |
| `tools/legacy_migration.py` | 591 | 4h | `# TODO: Implement batch loading to target database.` |
| `tools/legacy_migration.py` | 920 | 4h | `# TODO: Implement chained transformer support` |
| `tools/todo_audit.py` | 3 | 4h | `TODO Audit Report Generator` |
| `v2/scripts/log_watchdog.pl` | 164 | 4h | `# TODO: The Slack webhook call bypasses the proxy. If the monitoring` |
| `v2/scripts/log_watchdog.pl` | 248 | 4h | `# TODO: Add log rotation detection. The File::Tail module can` |
| `v2/services/market_stream.rb` | 269 | 4h | `# TODO: Actually store and serve historical ticks.` |
| `backend/src/connector/ffi.rs` | 16 | 3h | `// TODO: Upgrade to bindgen 0.64+ and regenerate these bindings.` |
| `backend/src/connector/ffi.rs` | 51 | 3h | `// TODO: Add support for macOS dylib loading (not yet tested)` |
| `backend/src/connector/mod.rs` | 30 | 3h | `// TODO: Add integration tests for the connector module. The current test` |
| `backend/src/connector/types.rs` | 37 | 3h | `/// TODO: Add more error codes for the new connector features.` |
| `backend/src/legacy/deprecations.rs` | 51 | 3h | `// TODO: This function is untested. The test suite was deleted in the` |
| `backend/src/legacy/deprecations.rs` | 58 | 3h | `// TODO: Should this log a warning? The original code had a log` |
| `backend/src/legacy/deprecations.rs` | 93 | 3h | `// TODO: Document this in the public API docs (which don't exist)` |
| `backend/src/legacy/deprecations.rs` | 142 | 3h | `// TODO: Fix null handling in the 2024 Q4 migration (which is now overdue)` |
| `backend/src/legacy/deprecations.rs` | 156 | 3h | `// TODO: Remove this field. It was intended for the GDPR compliance` |
| `backend/src/legacy/deprecations.rs` | 408 | 3h | `// TODO: This should return NaN or None, but returning 1.0` |
| `backend/src/legacy/deprecations.rs` | 597 | 3h | `// TODO: Implement v2 to v3 migration` |
| `backend/src/legacy/migrations.rs` | 205 | 3h | `// TODO: Automate the dependency graph generation from migration files.` |
| `backend/src/legacy/migrations.rs` | 275 | 3h | `// TODO: Add more linting rules. The current rules are too permissive.` |
| `compliance/ComplianceAuditor.java` | 72 | 3h | `// TODO: Remove this shit. It was added for a demo in 2022` |
| `frailbox/connector/api.c` | 58 | 3h | `* TODO: Make this configurable again, but with sane limits enforced.` |
| `frailbox/connector/protocol.c` | 16 | 3h | `* TODO: The hardware CRC detection is done at runtime using CPUID.` |
| `frailbox/include/logger.h` | 23 | 3h | `* TODO: Create a migration guide for replacing legacy logger calls` |
| `frailbox/include/logger.h` | 86 | 3h | `* TODO: Audit info-level log messages and reduce verbosity.` |
| `frailbox/include/logger.h` | 142 | 3h | `* TODO: Define __FILENAME__ as (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/...` |
| `frailbox/nfc/scanner.lua` | 261 | 3h | `-- TODO: Implement adaptive timeout based on card response time.` |
| `frailbox/src/logger.c` | 23 | 3h | `* TODO: The structured logger has been "almost ready" for 18 months.` |
| `frailbox/src/logger.c` | 51 | 3h | `#include "../include/logger.h" /* This header doesn't exist yet. TODO: Create...` |
| `frailbox/src/logger.c` | 72 | 3h | `* TODO: Test the crash reporter integration with the ring buffer.` |
| `frailbox/src/logger.c` | 128 | 3h | `* TODO: Add automatic log file reopening after SIGHUP.` |
| `frailbox/src/logger.c` | 135 | 3h | `* TODO: Remove this option and always include timestamps.` |
| `frontend/src/services/api.ts` | 30 | 3h | `// TODO: Remove the fallback to localhost once the staging server is stable.` |
| `frontend/src/services/api.ts` | 37 | 3h | `// TODO: Implement per-endpoint timeout configuration.` |
| `frontend/src/utils/dataTransforms.ts` | 16 | 3h | `* TODO: Verify the interpolation accuracy against the Python reference` |
| `frontend/src/utils/legacyCompat.ts` | 51 | 3h | `// TODO: Wrap the function call in React.startTransition() or` |
| `frontend/src/utils/legacyCompat.ts` | 513 | 3h | `* TODO: Decide on the correct behavior for empty search terms.` |
| `market/analytics/collector.go` | 527 | 3h | `// TODO: Replace this stub with actual metrics backend write call.` |
| `market/analytics/collector.go` | 625 | 3h | `// TODO: Add pre-aggregation support to avoid full scans.` |
| `market/analytics/collector.go` | 779 | 3h | `// TODO: Switch to linear interpolation for percentile calculation.` |
| `market/compliance/rules.go` | 23 | 3h | `// TODO: The JRRP algorithm has not been validated against actual regulatory` |
| `market/compliance/rules.go` | 198 | 3h | `// TODO: Add a TTL to the transaction cache. Currently, cached results` |
| `market/compliance/rules.go` | 534 | 3h | `// TODO: Implement per-country EU jurisdiction mapping.` |
| `market/gateway/api.go` | 611 | 3h | `// TODO: Fetch recent trades` |
| `market/gateway/api.go` | 646 | 3h | `// TODO: Fetch candle data` |
| `tools/legacy_analyzer.py` | 65 | 3h | `{"pattern": r"todo!\(", "name": "todo_macro", "severity": "info",` |
| `tools/legacy_migration.py` | 604 | 3h | `# TODO: Compare row counts between source and target` |
| `tools/legacy_migration.py` | 625 | 3h | `# TODO: Implement cleanup of temporary files` |
| `tools/legacy_migration.py` | 632 | 3h | `# TODO: Implement actual connection check` |
| `tools/legacy_migration.py` | 1122 | 3h | `# TODO: Implement validation logic` |
| `tools/legacy_migration.py` | 1157 | 3h | `# TODO: Implement list logic` |
| `tools/todo_audit.py` | 51 | 3h | `"Centralized audit of all 'TODO' comments across languages in the repository.",` |
| `v2/scripts/log_watchdog.pl` | 30 | 3h | `# TODO: The Slack webhook URL is hardcoded below. This is fine for now` |
| `v2/scripts/log_watchdog.pl` | 65 | 3h | `SLACK_WEBHOOK  => 'https://hooks.slack.com/services/T00/DUMMY/FAKE',  # TODO:...` |
| `v2/services/market_stream.rb` | 282 | 3h | `connected_clients: 0, # TODO: Track connected clients` |
| `backend/src/connector/ffi.rs` | 50 | 2h | `// TODO: Add support for Windows DLL loading (cancelled, remove this)` |
| `backend/src/connector/ffi.rs` | 204 | 2h | `/// TODO: Remove this function in v4.0.0. The deprecation was announced` |
| `backend/src/connector/types.rs` | 15 | 2h | `// TODO: Add a build-time validation step that compares the memory layout` |
| `backend/src/connector/types.rs` | 22 | 2h | `// TODO: The derive macros below generate a lot of boilerplate. Consider` |
| `backend/src/legacy/deprecations.rs` | 1 | 2h | `// TODO: This entire module is legacy. Do not refactor without reading the JI...` |
| `backend/src/legacy/deprecations.rs` | 22 | 2h | `// TODO: Revisit this decision in Q3 (year unspecified)` |
| `backend/src/legacy/deprecations.rs` | 29 | 2h | `// TODO: Remove these padding fields that were added to fix alignment` |
| `backend/src/legacy/deprecations.rs` | 218 | 2h | `// TODO: Remove after mobile API sunset - ETA unknown` |
| `backend/src/legacy/deprecations.rs` | 281 | 2h | `// TODO: Migrate admin dashboard to cursor pagination` |
| `backend/src/legacy/deprecations.rs` | 393 | 2h | `// TODO: Implement actual LRU eviction` |
| `backend/src/legacy/deprecations.rs` | 589 | 2h | `// TODO: Reconstruct the migration logic from the git history.` |
| `backend/src/legacy/migrations.rs` | 1 | 2h | `// TODO: Database migration history. This file tracks every schema migration` |
| `backend/src/legacy/mod.rs` | 1 | 2h | `// TODO: Legacy module root. This module contains all code that has been` |
| `backend/src/legacy/mod.rs` | 22 | 2h | `// TODO: Add a CI check that prevents new files from being added to` |
| `backend/src/legacy/mod.rs` | 92 | 2h | `// TODO: Implement legacy event queue drain` |
| `backend/src/legacy/v1_compat.rs` | 1 | 2h | `// TODO: This is the v1 compatibility layer. Delete this file once the` |
| `backend/src/lib.rs` | 1 | 2h | `// TODO: Remove connector and legacy modules once the v2 migration is complete.` |
| `backend/src/protocol/mod.rs` | 15 | 2h | `// TODO: The sub-module organization was determined by the original` |
| `compliance/ComplianceAuditor.java` | 106 | 2h | `* TODO: This method catches Exception and returns a PASS. Yes, you read` |
| `docs/OPERATIONS.md` | 239 | 2h | `TODO: The growth projections have been consistently overestimated by` |
| `frailbox/connector/protocol.h` | 29 | 2h | `* TODO: Deprecate protocol v1 support. The v1 fallback adds complexity` |
| `frailbox/include/logger.h` | 99 | 2h | `* TODO: Audit debug-level log messages and remove meaningless ones.` |
| `frailbox/include/logger.h` | 323 | 2h | `* TODO: Audit all uses of log_assert() and convert them to either` |
| `frailbox/nfc/scanner.lua` | 15 | 2h | `-- TODO: The ISO 7816 APDU parsing in this module only supports T=1 protocol.` |
| `frailbox/nfc/scanner.lua` | 29 | 2h | `--   IRQ -> GPIO17 (pin 11) -- actually unused, see TODO below` |
| `frailbox/nfc/scanner.lua` | 484 | 2h | `-- TODO: Verify CC computation against the EMV specification.` |
| `frailbox/nfc/scanner.lua` | 624 | 2h | `-- TODO: The PPSE response parsing is incomplete. It extracts` |
| `frailbox/src/logger.c` | 120 | 2h | `* TODO: Allow runtime log level changes via a signal handler.` |
| `frailbox/src/logger.c` | 176 | 2h | `* TODO: Re-retrieve PID after fork().` |
| `frailbox/src/logger.c` | 190 | 2h | `* TODO: Add Windows support or remove this comment.` |
| `frailbox/tests/test_connector.c` | 246 | 2h | `/* TODO: This test crashes because connector_init doesn't check for NULL.` |
| `frontend/src/ai/chat.ts` | 1 | 2h | `// @ts-nocheck - TODO: Fix types for v2. See V2-619.` |
| `frontend/src/ai/recommendations.ts` | 1 | 2h | `// @ts-nocheck - TODO: Fix types for v2. See V2-619.` |
| `frontend/src/components/OrderBook.tsx` | 15 | 2h | `* TODO: Implement virtual scrolling for the order book. The react-virtual` |
| `frontend/src/components/OrderHistory.tsx` | 15 | 2h | `* TODO: The merge strategy has a bug where duplicate orders can appear` |
| `frontend/src/hooks/useWebSocket.ts` | 1 | 2h | `// @ts-nocheck - TODO: Fix types for v2. See V2-619.` |
| `frontend/src/pages/AdminPage.tsx` | 15 | 2h | `* TODO: The admin page is feature-gated behind the ADMIN_PANEL feature` |
| `frontend/src/services/api.ts` | 43 | 2h | `// TODO: Make the retry logic idempotent-safe for mutating requests.` |
| `frontend/src/services/api.ts` | 421 | 2h | `// TODO: Move endpoint definitions to individual service files.` |
| `frontend/src/services/auth.ts` | 1 | 2h | `// @ts-nocheck - TODO: Fix types for v2. See V2-619.` |
| `frontend/src/store/slices.ts` | 1 | 2h | `// @ts-nocheck - TODO: Fix types for v2. See V2-619.` |
| `frontend/src/utils/dataService.ts` | 1 | 2h | `// @ts-nocheck - TODO: This file needs type fixes for the v2 migration.` |
| `frontend/src/utils/dataTransforms.ts` | 22 | 2h | `* TODO: The aggregation functions in this file are CPU-bound and can` |
| `frontend/src/utils/legacyCompat.ts` | 71 | 2h | `// TODO: Replace all $httpLegacy calls with direct fetch() calls.` |
| `frontend/src/utils/legacyCompat.ts` | 176 | 2h | `// TODO: Align the error shapes between legacy and new systems.` |
| `frontend/src/utils/legacyCompat.ts` | 323 | 2h | `* TODO: Replace with Intl.DateTimeFormat after UI tests are updated.` |
| `frontend/src/utils/legacyCompat.ts` | 673 | 2h | `* TODO: Extract shared validation into a React hook.` |
| `market/analytics/collector.go` | 36 | 2h | `// TODO: Re-create the proto definitions or migrate to a schema registry.` |
| `market/analytics/collector.go` | 463 | 2h | `// TODO: Make Start() idempotent.` |
| `market/analytics/collector.go` | 498 | 2h | `// TODO: Make the backend write timeout configurable.` |
| `market/gateway/api.go` | 575 | 2h | `// TODO: Fetch instruments from the market service` |
| `market/gateway/api.go` | 596 | 2h | `// TODO: Fetch order book from the matching engine` |
| `market/gateway/api.go` | 631 | 2h | `// TODO: Fetch ticker data` |
| `market/gateway/api.go` | 659 | 2h | `// TODO: Fetch market news` |
| `market/pricing/models.go` | 36 | 2h | `// TODO: Move to real-time exchange rates using the Bloomberg API.` |
| `tools/legacy_analyzer.py` | 99 | 2h | `{"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info"},` |
| `backend/src/connector/bridge.rs` | 14 | 1h | `// TODO: The circuit breaker parameters are hardcoded below. They should` |
| `backend/src/connector/bridge.rs` | 28 | 1h | `// TODO: Re-evaluate the least-loaded scheduler now that the race condition` |
| `backend/src/connector/legacy.rs` | 21 | 1h | `// TODO: The list of removed message types is documented in the migration` |
| `backend/src/connector/legacy.rs` | 28 | 1h | `// TODO: Add a metric to track how often this legacy shim is used. If usage` |
| `backend/src/legacy/deprecations.rs` | 133 | 1h | `// TODO: Add serde rename attributes once the S3 records have aged out.` |
| `backend/src/legacy/deprecations.rs` | 238 | 1h | `// TODO: REPLACE THIS WITH A PROPER MIGRATION STRATEGY` |
| `backend/src/legacy/deprecations.rs` | 259 | 1h | `// TODO: This function is not used anywhere. It was added as part of a` |
| `backend/src/legacy/deprecations.rs` | 630 | 1h | `// TODO: These tests are incomplete. They were written during a hackathon` |
| `backend/src/legacy/v1_compat.rs` | 14 | 1h | `// TODO: Remove this after v1 API sunset` |
| `backend/src/legacy/v1_compat.rs` | 77 | 1h | `// TODO: Fix the classification of GatewayTimeout` |
| `backend/src/legacy/v1_compat.rs` | 119 | 1h | `// TODO: Remove this envelope in the v2 API (which is also being deprecated)` |
| `backend/src/legacy/v1_compat.rs` | 413 | 1h | `// TODO: Complete the v1-to-v2 resource mapping` |
| `backend/src/protocol/events.rs` | 14 | 1h | `// TODO: Add a CI check that verifies all event types in this module have` |
| `backend/src/protocol/events.rs` | 28 | 1h | `/// TODO: Automate schema version management. Currently, engineers must` |
| `backend/src/protocol/serialize.rs` | 21 | 1h | `// TODO: Add support for compressed serialization (zstd, gzip).` |
| `compliance/ComplianceAuditor.java` | 196 | 1h | `// TODO: Actually implement SFTP transfer` |
| `frailbox/connector/api.h` | 28 | 1h | `* TODO: Remove this file when all connector types are migrated to` |
| `frailbox/engine/core/job_system.hpp` | 266 | 1h | `// TODO: This blocking behavior can cause priority inversion if a` |
| `frailbox/include/logger.h` | 168 | 1h | `* TODO: Add proper compile-time stripping of debug log messages.` |
| `frailbox/nfc/scanner.lua` | 588 | 1h | `-- TODO: The idle command above is a hack. The PN532 has a built-in` |
| `frailbox/src/logger.c` | 168 | 1h | `* TODO: Change the default to the actual process name.` |
| `frailbox/src/logger.c` | 672 | 1h | `* TODO: Remove this when the test suite is fully migrated.` |
| `frailbox/tests/test_connector.c` | 28 | 1h | `* TODO: Migrate to a real test framework. The leading candidate is` |
| `frontend/src/components/TradingChart.tsx` | 434 | 1h | `// TODO: Actually switch chart series type` |
| `frontend/src/hooks/useMarketData.ts` | 7 | 1h | `* TODO: In high-frequency trading scenarios, this hook creates too many` |
| `frontend/src/pages/TradePage.tsx` | 14 | 1h | `* TODO: The responsive layout uses CSS media queries AND JavaScript` |
| `frontend/src/pages/TradePage.tsx` | 21 | 1h | `* TODO: The trade form validation logic is duplicated between this` |
| `frontend/src/services/telemetry.ts` | 21 | 1h | `* TODO: Add support for sampling to reduce telemetry volume for high-traffic` |
| `frontend/src/utils/legacyCompat.ts` | 273 | 1h | `* TODO: Implement proper cache eviction with TTL and LRU.` |
| `frontend/src/utils/legacyCompat.ts` | 406 | 1h | `// TODO: Apply the AngularJS 1.6 number filter patch.` |
| `frontend/src/utils/legacyCompat.ts` | 567 | 1h | `* TODO: Handle circular references in deep copy.` |
| `frontend/src/utils/legacyCompat.ts` | 588 | 1h | `* TODO: Replace with lodash isEqual or a comparable utility.` |
| `market/analytics/collector.go` | 273 | 1h | `// TODO: Upgrade to nanosecond precision now that we've migrated` |
| `market/analytics/collector.go` | 294 | 1h | `// TODO: Fix the race condition in the batch flush logic.` |
| `market/analytics/collector.go` | 693 | 1h | `// TODO: Connect the alert system to the notification service.` |
| `market/gateway/api.go` | 672 | 1h | `// TODO: Upgrade to WebSocket connection` |
| `market/gateway/middleware.go` | 28 | 1h | `// TODO: Add integration tests that verify middleware ordering. The` |
| `market/gateway/middleware.go` | 371 | 1h | `// TODO: Implement gzip response compression` |
| `market/pricing/models.go` | 147 | 1h | `// TODO: Use CLDR data for locale-aware currency formatting.` |
| `tools/deploy.py` | 14 | 1h | `TODO: Remove this script when all environments have been migrated to` |
| `tools/legacy_analyzer.py` | 133 | 1h | `{"pattern": r"#\s*TODO", "name": "todo_comment", "severity": "info"},` |
| `tools/legacy_migration.py` | 609 | 1h | `# TODO: Validate data checksums` |
| `tools/log_aggregator.py` | 21 | 1h | `TODO: The log parser in this script uses regex-based pattern matching` |
| `tools/terraform_import.py` | 14 | 1h | `TODO: Remove this tool once the Terraform Cloud migration is complete.` |
| `tools/todo_audit.py` | 49 | 1h | `"# 📋 Repository Technical Debt & TODO Audit Report",` |
| `v2/scripts/log_watchdog.pl` | 189 | 1h | `# TODO: Log truncated lines to a separate file for forensic analysis.` |
| `v2/scripts/log_watchdog.pl` | 308 | 1h | `# TODO: The daemonization doesn't redirect STDIN/STDOUT/STDERR properly.` |
