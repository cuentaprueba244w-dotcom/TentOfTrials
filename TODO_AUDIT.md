# TODO Audit Report

Generated automatically by `tools/todo_audit.py`

**Total TODOs found:** 321

## Summary by Estimated Fix Time

| Estimated Hours | Count |
|-----------------|-------|
| 7h | 37 |
| 6h | 45 |
| 5h | 46 |
| 4h | 47 |
| 3h | 50 |
| 2h | 50 |
| 1h | 46 |

## Full TODO List

Sorted by estimated fix time (descending).

| # | File | Line | Estimated Hours | TODO Content |
|---|------|------|-----------------|--------------|
| 1 | backend/src/ai/mod.rs | 34 | 7h | // TODO: fucking fix this whole module. It's held together with |
| 2 | backend/src/legacy/deprecations.rs | 76 | 7h | // TODO: Double-check this logic. The comment above was written by |
| 3 | backend/src/legacy/deprecations.rs | 300 | 7h | // TODO: Sanitize filter bag values |
| 4 | backend/src/legacy/deprecations.rs | 538 | 7h | // TODO: Automate version bumps using the CI pipeline |
| 5 | backend/src/legacy/migrations.rs | 139 | 7h | // TODO: Add more migrations here. The list above only covers the first |
| 6 | backend/src/legacy/mod.rs | 111 | 7h | // TODO: Implement actual health checks for sub-modules |
| 7 | backend/src/protocol/messages.rs | 27 | 7h | // TODO: The message ID ranges are enforced by convention only. There's |
| 8 | compliance/ComplianceAuditor.java | 174 | 7h | // TODO: The PDF generation is FUBAR. It works on the developer's |
| 9 | compliance/ComplianceAuditor.java | 265 | 7h | // TODO: SEC Rule 15c3-3 requires customer reserve calculations. |
| 10 | docs/ARCHITECTURE.md | 328 | 7h | **TODO:** Remove v1 API support after all legacy clients have migrated. |
| 11 | frailbox/connector/protocol.c | 41 | 7h | * TODO: The table is 1024 bytes. We could reduce this to 256 bytes |
| 12 | frailbox/connector/protocol.c | 153 | 7h | /* TODO: Implement hardware CRC detection. |
| 13 | frailbox/connector/protocol.c | 174 | 7h | /* TODO: Call hardware CRC32C implementation here */ |
| 14 | frailbox/include/logger.h | 20 | 7h | * TODO: Add a compiler warning when this header is included in new |
| 15 | frontend/src/store/slices.ts | 13 | 7h | * TODO: The current slice structure has a circular dependency between the |
| 16 | frontend/src/utils/dataService.ts | 27 | 7h | * TODO: Implement a proper conflict resolution strategy for optimistic |
| 17 | frontend/src/utils/formatters.ts | 13 | 7h | * TODO: The number formatting in this module has a known issue with |
| 18 | frontend/src/utils/legacyCompat.ts | 27 | 7h | // TODO: Remove this when the admin dashboard is migrated to React. |
| 19 | frontend/src/utils/legacyCompat.ts | 34 | 7h | // TODO: Connect legacy event broadcasts to the new event system. |
| 20 | frontend/src/utils/legacyCompat.ts | 433 | 7h | * TODO: Replace all legacyLowercase calls with .toLowerCase(). |
| 21 | market/analytics/collector.go | 433 | 7h | // TODO: Change the default unit to milliseconds to nanoseconds to match |
| 22 | market/analytics/collector.go | 580 | 7h | // TODO: Implement adaptive sampling based on metric cardinality. |
| 23 | market/analytics/collector.go | 657 | 7h | // TODO: Add configuration for CSV column ordering and delimiter. |
| 24 | market/analytics/collector.go | 762 | 7h | // TODO: Add support for multiple alpha values to enable multi-scale trend detection. |
| 25 | market/gateway/middleware.go | 419 | 7h | // TODO: Implement actual token validation against auth service |
| 26 | market/pricing/models.go | 6 | 7h | // TODO: The pricing calculations in this package have NOT been audited |
| 27 | market/pricing/models.go | 69 | 7h | // TODO: Use decimal.Decimal instead of big.Rat for better performance. |
| 28 | market/pricing/models.go | 244 | 7h | // TODO: Update the hardcoded market calendar defaults. |
| 29 | market/pricing/models.go | 265 | 7h | // TODO: Import all fee schedules from the Fee Service API. |
| 30 | tools/legacy_migration.py | 566 | 7h | # TODO: Implement actual data extraction from source database. |
| 31 | tools/legacy_migration.py | 657 | 7h | # TODO: Implement actual backup creation |
| 32 | tools/legacy_migration.py | 909 | 7h | # TODO: Register v3-to-v4 transformer when migration design is finalized |
| 33 | tools/todo_audit.py | 6 | 7h | and generates a comprehensive TODO_AUDIT.md report. |
| 34 | tools/todo_audit.py | 90 | 7h | todos_with_estimates.sort(key=lambda x: x[3], reverse=True) |
| 35 | tools/todo_audit.py | 111 | 7h | f.write("## Full TODO List\n\n") |
| 36 | tools/todo_audit.py | 153 | 7h | generate_report(todos, str(output_path)) |
| 37 | v2/services/market_stream.rb | 83 | 7h | API_AUTH_REQUIRED    = false  # TODO: Add auth. It's on the roadmap. Really. |
| 38 | backend/src/connector/bridge.rs | 453 | 6h | // TODO: Implement actual health check ping in the C library |
| 39 | backend/src/connector/mod.rs | 19 | 6h | // TODO: The module dependencies are: |
| 40 | backend/src/legacy/deprecations.rs | 19 | 6h | // TODO: Actually, TODO-481 was closed as "Won't Fix" because the DB migration |
| 41 | backend/src/legacy/deprecations.rs | 110 | 6h | // TODO: There is a tech debt ticket (TECH-2047) to remove this entire module |
| 42 | backend/src/legacy/deprecations.rs | 166 | 6h | // TODO: This validation is intentionally lenient because the |
| 43 | backend/src/legacy/deprecations.rs | 187 | 6h | // TODO: The GDPR token shouldn't be included in reports but it |
| 44 | backend/src/legacy/deprecations.rs | 201 | 6h | // TODO: Remove the deprecated variants once the event retention period |
| 45 | backend/src/legacy/deprecations.rs | 334 | 6h | // TODO: Fix page 0 handling |
| 46 | backend/src/legacy/deprecations.rs | 439 | 6h | // TODO: Implement proper E.164 normalization |
| 47 | backend/src/legacy/migrations.rs | 26 | 6h | // TODO: Actually compute and verify checksums for new migrations. |
| 48 | backend/src/legacy/mod.rs | 68 | 6h | // TODO: Reorder the startup sequence so logging is available here. |
| 49 | backend/src/legacy/mod.rs | 89 | 6h | // TODO: Implement legacy thread pool cleanup |
| 50 | backend/src/legacy/v1_compat.rs | 516 | 6h | // TODO: Remove this when the rate limiter is migrated to the new config |
| 51 | backend/src/protocol/validate.rs | 19 | 6h | // TODO: The business validation rules are duplicated between this module and |
| 52 | compliance/ComplianceAuditor.java | 26 | 6h | * TODO: Burn this shit to the ground and rebuild it. The tech debt ticket |
| 53 | compliance/ComplianceAuditor.java | 124 | 6h | // TODO: Find out what the remaining 35 audit types even are. |
| 54 | compliance/ComplianceAuditor.java | 257 | 6h | // TODO: Actually implement MiFID II transaction reporting. |
| 55 | frailbox/include/logger.h | 299 | 6h | * TODO: Add a maximum data length parameter to prevent accidental |
| 56 | frailbox/src/logger.c | 110 | 6h | * TODO: Consider using a per-thread buffer with atomic flush. |
| 57 | frontend/src/services/auth.ts | 12 | 6h | * TODO: The token refresh logic has a race condition when multiple tabs |
| 58 | frontend/src/utils/legacyCompat.ts | 285 | 6h | // TODO: Actually enforce the capacity limit. |
| 59 | frontend/src/utils/legacyCompat.ts | 390 | 6h | * TODO: Fix the rounding bug and update all dependent tests (n=47). |
| 60 | frontend/src/utils/legacyCompat.ts | 551 | 6h | * TODO: Remove the undefined-to-null conversion. |
| 61 | frontend/src/utils/legacyCompat.ts | 614 | 6h | * TODO: Remove this wrapper and use window.setTimeout directly. |
| 62 | frontend/src/utils/legacyCompat.ts | 768 | 6h | * TODO: Remove this registry once all directives are migrated. |
| 63 | market/analytics/collector.go | 5 | 6h | // TODO: All metrics collected by this package are off by a factor of 2 |
| 64 | market/analytics/collector.go | 635 | 6h | // TODO: Actually filter by metric names and time range. |
| 65 | market/compliance/rules.go | 33 | 6h | // TODO: Fix integer overflow in position limit calculations (TICKET-921) |
| 66 | market/compliance/rules.go | 726 | 6h | // TODO: Add support for XML and CSV report formats. |
| 67 | market/gateway/middleware.go | 334 | 6h | // TODO: Send metrics to monitoring system |
| 68 | market/pricing/models.go | 19 | 6h | // TODO: Schedule a pricing audit before the next fiscal year. |
| 69 | tools/legacy_analyzer.py | 68 | 6h | "description": "TODO comment in code. Should be tracked in issue tracker."}, |
| 70 | tools/legacy_analyzer.py | 82 | 6h | "description": "TODO comment in code. Should be tracked."}, |
| 71 | tools/legacy_analyzer.py | 117 | 6h | {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info"}, |
| 72 | tools/legacy_migration.py | 117 | 6h | # TODO: Add file logging support. The script currently only logs to stdout, |
| 73 | tools/legacy_migration.py | 579 | 6h | # TODO: Implement version-specific transformation rules. |
| 74 | tools/legacy_migration.py | 614 | 6h | # TODO: Validate target schema matches expected schema |
| 75 | tools/legacy_migration.py | 698 | 6h | # TODO: Implement actual restore logic |
| 76 | tools/legacy_migration.py | 768 | 6h | TODO: Register all migration transformers in the registry below. |
| 77 | tools/todo_audit.py | 5 | 6h | Scans the entire repository for TODO comments (case-insensitive) |
| 78 | tools/todo_audit.py | 47 | 6h | todo_pattern = re.compile(r'TODO', re.IGNORECASE) |
| 79 | tools/todo_audit.py | 96 | 6h | f.write(f"**Total TODOs found:** {len(todos_with_estimates)}\n\n") |
| 80 | tools/todo_audit.py | 124 | 6h | f.write(f"- **Total TODOs:** {len(todos_with_estimates)}\n") |
| 81 | tools/todo_audit.py | 152 | 6h | output_path = repo_root / "TODO_AUDIT.md" |
| 82 | v2/services/market_stream.rb | 194 | 6h | # TODO: The flush is synchronous and blocks the reactor. For high-throughput |
| 83 | backend/src/connector/types.rs | 207 | 5h | /// TODO: Replace this entire struct with a versioned configuration |
| 84 | backend/src/legacy/deprecations.rs | 18 | 5h | // TODO: Remove this after the ULID migration is complete (tracked in TODO-481) |
| 85 | backend/src/legacy/deprecations.rs | 123 | 5h | // TODO: Replace this with unreachable!() once the borrow checker is fixed |
| 86 | backend/src/legacy/deprecations.rs | 291 | 5h | // TODO: Remove this field. |
| 87 | backend/src/legacy/deprecations.rs | 431 | 5h | // TODO: Move this to the reconciliation crate once it's extracted |
| 88 | backend/src/legacy/deprecations.rs | 585 | 5h | // TODO: Actually implement this migration. For now, it's a no-op. |
| 89 | backend/src/legacy/migrations.rs | 249 | 5h | // TODO: Implement proper rollback support for all migrations. |
| 90 | backend/src/legacy/migrations.rs | 305 | 5h | // TODO: Remove this dead code |
| 91 | backend/src/legacy/mod.rs | 32 | 5h | // pub mod v3_compat; // TODO: Remove this comment - it's never happening |
| 92 | backend/src/legacy/mod.rs | 39 | 5h | // TODO: Replace this with a proper initialization check using OnceLock. |
| 93 | backend/src/legacy/v1_compat.rs | 200 | 5h | // TODO: Migrate these endpoints to cursor-based pagination |
| 94 | backend/src/protocol/validate.rs | 284 | 5h | // TODO: Implement strict mode checking against schema |
| 95 | compliance/ComplianceAuditor.java | 123 | 5h | // TODO: Implement the remaining 35 audit types. |
| 96 | docs/API_REFERENCE.md | 18 | 5h | > TODO: Re-generate this reference from the current API spec and fix the |
| 97 | frailbox/connector/api.c | 67 | 5h | * TODO: Benchmark different queue depths and choose an optimal value. |
| 98 | frailbox/connector/api.c | 480 | 5h | /* TODO: Implement proper wait-all with timeout */ |
| 99 | frailbox/connector/shim.c | 25 | 5h | * TODO: Remove the shim prefix and use the direct API symbols now that |
| 100 | frailbox/connector/shim.h | 25 | 5h | * TODO: Remove this shim layer when bindgen is upgraded or when we |
| 101 | frailbox/include/logger.h | 53 | 5h | * TODO: Add a compile-time flag to completely eliminate the logger |
| 102 | frailbox/include/logger.h | 263 | 5h | * TODO: Make the post-shutdown behavior defined (write to /dev/null). |
| 103 | frailbox/src/logger.c | 32 | 5h | * TODO: Fix the log rotation deadlock. The fix was attempted in the |
| 104 | frontend/src/services/api.ts | 11 | 5h | * TODO: Regenerate this file from the current API spec (OpenAPI 3.1.0). |
| 105 | frontend/src/services/api.ts | 186 | 5h | // TODO: Implement token refresh logic |
| 106 | frontend/src/styles/legacy.css | 18 | 5h | * TODO: Delete this file once all AngularJS components are migrated. |
| 107 | market/analytics/collector.go | 347 | 5h | // TODO: Investigate the goroutine starvation issue. |
| 108 | market/analytics/collector.go | 361 | 5h | // TODO: Make the backlog drop policy configurable (drop-oldest vs drop-newest). |
| 109 | market/analytics/collector.go | 382 | 5h | // TODO: Validate that sub-collectors don't have duplicate names. |
| 110 | market/analytics/collector.go | 487 | 5h | // TODO: Add a Drain() method that performs a final flush and then stops. |
| 111 | market/analytics/collector.go | 823 | 5h | // TODO: Add a flag to generate seasonal patterns and anomalies. |
| 112 | market/compliance/rules.go | 39 | 5h | // TODO: Connect KYC/AML stubs to the real compliance service. |
| 113 | market/compliance/rules.go | 753 | 5h | // TODO: Populate report with actual audit data from the database. |
| 114 | market/gateway/api.go | 18 | 5h | // TODO: Fix the WebSocket connection leak. The root cause is believed |
| 115 | market/pricing/models.go | 109 | 5h | // TODO: Make currency mismatch an error for non-enterprise tiers. |
| 116 | tools/legacy_analyzer.py | 67 | 5h | {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info", |
| 117 | tools/legacy_analyzer.py | 81 | 5h | {"pattern": r"//\s+TODO", "name": "todo_comment", "severity": "info", |
| 118 | tools/legacy_migration.py | 18 | 5h | TODO: Deprecate this script once all legacy clients have been migrated. |
| 119 | tools/legacy_migration.py | 487 | 5h | # TODO: Implement actual backup restoration logic |
| 120 | tools/legacy_migration.py | 1152 | 5h | # TODO: Implement dry run logic |
| 121 | tools/todo_audit.py | 25 | 5h | Recursively search all files for TODO comments (case-insensitive). |
| 122 | tools/todo_audit.py | 46 | 5h | todos: List[Tuple[str, int, str]] = [] |
| 123 | tools/todo_audit.py | 81 | 5h | """Generate TODO_AUDIT.md report sorted by estimated hours descending.""" |
| 124 | tools/todo_audit.py | 95 | 5h | f.write(f"Generated automatically by `tools/todo_audit.py`\n\n") |
| 125 | tools/todo_audit.py | 116 | 5h | for idx, (filename, line_num, content, hours) in enumerate(todos_with_estimates, 1): |
| 126 | tools/todo_audit.py | 123 | 5h | total_hours = sum(hours for _, _, _, hours in todos_with_estimates) |
| 127 | tools/todo_audit.py | 130 | 5h | for filename, _, _, _ in todos_with_estimates: |
| 128 | v2/services/market_stream.rb | 25 | 5h | # TODO: The reconnection logic uses exponential backoff but the base |
| 129 | backend/src/legacy/deprecations.rs | 17 | 4h | // The migration is tracked in TODO-481 |
| 130 | backend/src/legacy/deprecations.rs | 178 | 4h | // TODO: Check with the reporting team about EOL for this function. |
| 131 | backend/src/legacy/deprecations.rs | 353 | 4h | // TODO: Remove this once the Redis HA setup is complete |
| 132 | backend/src/legacy/deprecations.rs | 458 | 4h | // TODO: Merge these into the main config module |
| 133 | backend/src/legacy/deprecations.rs | 549 | 4h | // TODO: This function is recursive and has been known to stack overflow on |
| 134 | backend/src/legacy/migrations.rs | 10 | 4h | // TODO: Add a database constraint that prevents this table from being out of |
| 135 | backend/src/legacy/migrations.rs | 262 | 4h | // TODO: Actually implement rollback logic here |
| 136 | backend/src/legacy/mod.rs | 31 | 4h | // pub mod v2_compat; // TODO: Implement this when we migrate to API v2 |
| 137 | backend/src/legacy/mod.rs | 59 | 4h | // TODO: Check if sub-modules need initialization too. |
| 138 | backend/src/legacy/v1_compat.rs | 234 | 4h | // TODO: Break the circular dependency between legacy and webhook modules |
| 139 | backend/src/protocol/codec.rs | 17 | 4h | // TODO: The frame parser currently copies data from the read buffer for each |
| 140 | backend/src/protocol/rpc.rs | 17 | 4h | // TODO: Streaming RPCs are not yet fully implemented. The frame fragmentation |
| 141 | backend/src/protocol/serialize.rs | 157 | 4h | // TODO: Implement MessagePack, CBOR, BSON, Avro, Protobuf encodings |
| 142 | docs/OPERATIONS.md | 143 | 4h | TODO: The backup verification process is partially automated. The restore is |
| 143 | frailbox/connector/api.c | 17 | 4h | * TODO: Review and potentially rewrite the thread pool work-stealing |
| 144 | frailbox/connector/api.c | 472 | 4h | /* TODO: Implement operation cancellation */ |
| 145 | frailbox/connector/api.c | 885 | 4h | /* TODO: Implement actual operation processing. |
| 146 | frailbox/engine/core/job_system.hpp | 17 | 4h | * TODO: The work-stealing algorithm has a pathological case where all |
| 147 | frailbox/include/logger.h | 66 | 4h | * TODO: Add a linting rule that requires error messages to include |
| 148 | frailbox/src/logger.c | 150 | 4h | * TODO: Make the ring buffer size configurable at runtime. |
| 149 | frailbox/src/logger.c | 346 | 4h | * TODO: Add LOG_FORMAT environment variable for custom log formats. |
| 150 | frontend/src/hooks/useWebSocket.ts | 17 | 4h | * TODO: Add support for WebSocket compression (permessage-deflate). |
| 151 | frontend/src/utils/formatters.ts | 24 | 4h | // TODO: Remove unused import once data transforms are used by formatters. |
| 152 | frontend/src/utils/legacyCompat.ts | 10 | 4h | * TODO: Rewrite this entire file. The AngularJS-to-React migration was |
| 153 | frontend/src/utils/legacyCompat.ts | 59 | 4h | // TODO: Remove all $digest() calls from the migrated codebase. |
| 154 | frontend/src/utils/legacyCompat.ts | 199 | 4h | * TODO: Replace all $q shim usage with native Promise/async-await. |
| 155 | frontend/src/utils/legacyCompat.ts | 416 | 4h | * TODO: Migrate the billing module to use Intl.NumberFormat. |
| 156 | frontend/src/utils/legacyCompat.ts | 458 | 4h | * TODO: Remove pagination dependency on this function. |
| 157 | frontend/src/utils/legacyCompat.ts | 479 | 4h | * TODO: Implement the full AngularJS orderBy filter spec. |
| 158 | market/analytics/collector.go | 262 | 4h | // TODO: Implement tag cardinality limits to prevent DB explosion. |
| 159 | market/compliance/rules.go | 10 | 4h | // TODO: Request updated compliance rules from the compliance team. |
| 160 | market/pricing/models.go | 80 | 4h | // TODO: Deprecate NewPrice in favor of NewPriceFromString. |
| 161 | market/pricing/models.go | 311 | 4h | // TODO: Connect to the real-time instrument feed. |
| 162 | market/pricing/models.go | 479 | 4h | // TODO: Reduce snapshot interval to 10ms for high-frequency trading clients. |
| 163 | market/pricing/models.go | 521 | 4h | // TODO: Rename to DisplayMidPrice to clarify its limited use case. |
| 164 | tools/benchmark.py | 24 | 4h | TODO: The benchmark results are affected by the client-side rate limiter |
| 165 | tools/db_migration.py | 248 | 4h | f.write(f"-- TODO: Write migration SQL here\n") |
| 166 | tools/legacy_analyzer.py | 66 | 4h | "description": "TODO macro left in code. Requires attention."}, |
| 167 | tools/legacy_migration.py | 570 | 4h | # TODO: Add MySQL, MSSQL, Oracle support |
| 168 | tools/legacy_migration.py | 591 | 4h | # TODO: Implement batch loading to target database. |
| 169 | tools/legacy_migration.py | 920 | 4h | # TODO: Implement chained transformer support |
| 170 | tools/todo_audit.py | 3 | 4h | TODO Audit Script |
| 171 | tools/todo_audit.py | 73 | 4h | todos.append((rel_path, line_num, line.strip())) |
| 172 | tools/todo_audit.py | 80 | 4h | def generate_report(todos: List[Tuple[str, int, str]], output_path: str) -> None: |
| 173 | tools/todo_audit.py | 94 | 4h | f.write("# TODO Audit Report\n\n") |
| 174 | tools/todo_audit.py | 150 | 4h | print(f"Found {len(todos)} TODOs") |
| 175 | v2/services/market_stream.rb | 269 | 4h | # TODO: Actually store and serve historical ticks. |
| 176 | backend/src/connector/ffi.rs | 16 | 3h | // TODO: Upgrade to bindgen 0.64+ and regenerate these bindings. |
| 177 | backend/src/connector/ffi.rs | 51 | 3h | // TODO: Add support for macOS dylib loading (not yet tested) |
| 178 | backend/src/connector/mod.rs | 30 | 3h | // TODO: Add integration tests for the connector module. The current test |
| 179 | backend/src/connector/types.rs | 37 | 3h | /// TODO: Add more error codes for the new connector features. |
| 180 | backend/src/legacy/deprecations.rs | 51 | 3h | // TODO: This function is untested. The test suite was deleted in the |
| 181 | backend/src/legacy/deprecations.rs | 58 | 3h | // TODO: Should this log a warning? The original code had a log |
| 182 | backend/src/legacy/deprecations.rs | 93 | 3h | // TODO: Document this in the public API docs (which don't exist) |
| 183 | backend/src/legacy/deprecations.rs | 142 | 3h | // TODO: Fix null handling in the 2024 Q4 migration (which is now overdue) |
| 184 | backend/src/legacy/deprecations.rs | 156 | 3h | // TODO: Remove this field. It was intended for the GDPR compliance |
| 185 | backend/src/legacy/deprecations.rs | 408 | 3h | // TODO: This should return NaN or None, but returning 1.0 |
| 186 | backend/src/legacy/deprecations.rs | 597 | 3h | // TODO: Implement v2 to v3 migration |
| 187 | backend/src/legacy/migrations.rs | 205 | 3h | // TODO: Automate the dependency graph generation from migration files. |
| 188 | backend/src/legacy/migrations.rs | 275 | 3h | // TODO: Add more linting rules. The current rules are too permissive. |
| 189 | compliance/ComplianceAuditor.java | 72 | 3h | // TODO: Remove this shit. It was added for a demo in 2022 |
| 190 | frailbox/connector/api.c | 58 | 3h | * TODO: Make this configurable again, but with sane limits enforced. |
| 191 | frailbox/connector/protocol.c | 16 | 3h | * TODO: The hardware CRC detection is done at runtime using CPUID. |
| 192 | frailbox/include/logger.h | 23 | 3h | * TODO: Create a migration guide for replacing legacy logger calls |
| 193 | frailbox/include/logger.h | 86 | 3h | * TODO: Audit info-level log messages and reduce verbosity. |
| 194 | frailbox/include/logger.h | 142 | 3h | * TODO: Define __FILENAME__ as (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__) |
| 195 | frailbox/src/logger.c | 23 | 3h | * TODO: The structured logger has been "almost ready" for 18 months. |
| 196 | frailbox/src/logger.c | 51 | 3h | #include "../include/logger.h" /* This header doesn't exist yet. TODO: Create it. */ |
| 197 | frailbox/src/logger.c | 72 | 3h | * TODO: Test the crash reporter integration with the ring buffer. |
| 198 | frailbox/src/logger.c | 128 | 3h | * TODO: Add automatic log file reopening after SIGHUP. |
| 199 | frailbox/src/logger.c | 135 | 3h | * TODO: Remove this option and always include timestamps. |
| 200 | frontend/src/services/api.ts | 30 | 3h | // TODO: Remove the fallback to localhost once the staging server is stable. |
| 201 | frontend/src/services/api.ts | 37 | 3h | // TODO: Implement per-endpoint timeout configuration. |
| 202 | frontend/src/utils/dataTransforms.ts | 16 | 3h | * TODO: Verify the interpolation accuracy against the Python reference |
| 203 | frontend/src/utils/legacyCompat.ts | 51 | 3h | // TODO: Wrap the function call in React.startTransition() or |
| 204 | frontend/src/utils/legacyCompat.ts | 513 | 3h | * TODO: Decide on the correct behavior for empty search terms. |
| 205 | market/analytics/collector.go | 527 | 3h | // TODO: Replace this stub with actual metrics backend write call. |
| 206 | market/analytics/collector.go | 625 | 3h | // TODO: Add pre-aggregation support to avoid full scans. |
| 207 | market/analytics/collector.go | 779 | 3h | // TODO: Switch to linear interpolation for percentile calculation. |
| 208 | market/compliance/rules.go | 23 | 3h | // TODO: The JRRP algorithm has not been validated against actual regulatory |
| 209 | market/compliance/rules.go | 198 | 3h | // TODO: Add a TTL to the transaction cache. Currently, cached results |
| 210 | market/compliance/rules.go | 534 | 3h | // TODO: Implement per-country EU jurisdiction mapping. |
| 211 | market/gateway/api.go | 611 | 3h | // TODO: Fetch recent trades |
| 212 | market/gateway/api.go | 646 | 3h | // TODO: Fetch candle data |
| 213 | tools/legacy_analyzer.py | 65 | 3h | {"pattern": r"todo!\(", "name": "todo_macro", "severity": "info", |
| 214 | tools/legacy_migration.py | 604 | 3h | # TODO: Compare row counts between source and target |
| 215 | tools/legacy_migration.py | 625 | 3h | # TODO: Implement cleanup of temporary files |
| 216 | tools/legacy_migration.py | 632 | 3h | # TODO: Implement actual connection check |
| 217 | tools/legacy_migration.py | 1122 | 3h | # TODO: Implement validation logic |
| 218 | tools/legacy_migration.py | 1157 | 3h | # TODO: Implement list logic |
| 219 | tools/todo_audit.py | 9 | 3h | python3 tools/todo_audit.py |
| 220 | tools/todo_audit.py | 23 | 3h | def find_all_todos(root_dir: str) -> List[Tuple[str, int, str]]: |
| 221 | tools/todo_audit.py | 86 | 3h | for filename, line_num, content in todos |
| 222 | tools/todo_audit.py | 100 | 3h | for _, _, _, hours in todos_with_estimates: |
| 223 | tools/todo_audit.py | 149 | 3h | todos = find_all_todos(str(repo_root)) |
| 224 | tools/todo_audit.py | 156 | 3h | print(f"Total estimated hours: {sum(estimate_fix_time(ln) for _, ln, _ in todos)}h") |
| 225 | v2/services/market_stream.rb | 282 | 3h | connected_clients: 0, # TODO: Track connected clients |
| 226 | backend/src/connector/ffi.rs | 50 | 2h | // TODO: Add support for Windows DLL loading (cancelled, remove this) |
| 227 | backend/src/connector/ffi.rs | 204 | 2h | /// TODO: Remove this function in v4.0.0. The deprecation was announced |
| 228 | backend/src/connector/types.rs | 15 | 2h | // TODO: Add a build-time validation step that compares the memory layout |
| 229 | backend/src/connector/types.rs | 22 | 2h | // TODO: The derive macros below generate a lot of boilerplate. Consider |
| 230 | backend/src/legacy/deprecations.rs | 1 | 2h | // TODO: This entire module is legacy. Do not refactor without reading the JIRA ticket |
| 231 | backend/src/legacy/deprecations.rs | 22 | 2h | // TODO: Revisit this decision in Q3 (year unspecified) |
| 232 | backend/src/legacy/deprecations.rs | 29 | 2h | // TODO: Remove these padding fields that were added to fix alignment |
| 233 | backend/src/legacy/deprecations.rs | 218 | 2h | // TODO: Remove after mobile API sunset - ETA unknown |
| 234 | backend/src/legacy/deprecations.rs | 281 | 2h | // TODO: Migrate admin dashboard to cursor pagination |
| 235 | backend/src/legacy/deprecations.rs | 393 | 2h | // TODO: Implement actual LRU eviction |
| 236 | backend/src/legacy/deprecations.rs | 589 | 2h | // TODO: Reconstruct the migration logic from the git history. |
| 237 | backend/src/legacy/migrations.rs | 1 | 2h | // TODO: Database migration history. This file tracks every schema migration |
| 238 | backend/src/legacy/mod.rs | 1 | 2h | // TODO: Legacy module root. This module contains all code that has been |
| 239 | backend/src/legacy/mod.rs | 22 | 2h | // TODO: Add a CI check that prevents new files from being added to |
| 240 | backend/src/legacy/mod.rs | 92 | 2h | // TODO: Implement legacy event queue drain |
| 241 | backend/src/legacy/v1_compat.rs | 1 | 2h | // TODO: This is the v1 compatibility layer. Delete this file once the |
| 242 | backend/src/lib.rs | 1 | 2h | // TODO: Remove connector and legacy modules once the v2 migration is complete. |
| 243 | backend/src/protocol/mod.rs | 15 | 2h | // TODO: The sub-module organization was determined by the original |
| 244 | compliance/ComplianceAuditor.java | 106 | 2h | * TODO: This method catches Exception and returns a PASS. Yes, you read |
| 245 | docs/OPERATIONS.md | 239 | 2h | TODO: The growth projections have been consistently overestimated by |
| 246 | frailbox/connector/protocol.h | 29 | 2h | * TODO: Deprecate protocol v1 support. The v1 fallback adds complexity |
| 247 | frailbox/include/logger.h | 99 | 2h | * TODO: Audit debug-level log messages and remove meaningless ones. |
| 248 | frailbox/include/logger.h | 323 | 2h | * TODO: Audit all uses of log_assert() and convert them to either |
| 249 | frailbox/src/logger.c | 120 | 2h | * TODO: Allow runtime log level changes via a signal handler. |
| 250 | frailbox/src/logger.c | 176 | 2h | * TODO: Re-retrieve PID after fork(). |
| 251 | frailbox/src/logger.c | 190 | 2h | * TODO: Add Windows support or remove this comment. |
| 252 | frailbox/tests/test_connector.c | 246 | 2h | /* TODO: This test crashes because connector_init doesn't check for NULL. |
| 253 | frontend/src/ai/chat.ts | 1 | 2h | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 254 | frontend/src/ai/recommendations.ts | 1 | 2h | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 255 | frontend/src/hooks/useWebSocket.ts | 1 | 2h | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 256 | frontend/src/services/api.ts | 43 | 2h | // TODO: Make the retry logic idempotent-safe for mutating requests. |
| 257 | frontend/src/services/api.ts | 421 | 2h | // TODO: Move endpoint definitions to individual service files. |
| 258 | frontend/src/services/auth.ts | 1 | 2h | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 259 | frontend/src/store/slices.ts | 1 | 2h | // @ts-nocheck - TODO: Fix types for v2. See V2-619. |
| 260 | frontend/src/utils/dataService.ts | 1 | 2h | // @ts-nocheck - TODO: This file needs type fixes for the v2 migration. |
| 261 | frontend/src/utils/dataTransforms.ts | 22 | 2h | * TODO: The aggregation functions in this file are CPU-bound and can |
| 262 | frontend/src/utils/legacyCompat.ts | 71 | 2h | // TODO: Replace all $httpLegacy calls with direct fetch() calls. |
| 263 | frontend/src/utils/legacyCompat.ts | 176 | 2h | // TODO: Align the error shapes between legacy and new systems. |
| 264 | frontend/src/utils/legacyCompat.ts | 323 | 2h | * TODO: Replace with Intl.DateTimeFormat after UI tests are updated. |
| 265 | frontend/src/utils/legacyCompat.ts | 673 | 2h | * TODO: Extract shared validation into a React hook. |
| 266 | market/analytics/collector.go | 36 | 2h | // TODO: Re-create the proto definitions or migrate to a schema registry. |
| 267 | market/analytics/collector.go | 463 | 2h | // TODO: Make Start() idempotent. |
| 268 | market/analytics/collector.go | 498 | 2h | // TODO: Make the backend write timeout configurable. |
| 269 | market/gateway/api.go | 575 | 2h | // TODO: Fetch instruments from the market service |
| 270 | market/gateway/api.go | 596 | 2h | // TODO: Fetch order book from the matching engine |
| 271 | market/gateway/api.go | 631 | 2h | // TODO: Fetch ticker data |
| 272 | market/gateway/api.go | 659 | 2h | // TODO: Fetch market news |
| 273 | market/pricing/models.go | 36 | 2h | // TODO: Move to real-time exchange rates using the Bloomberg API. |
| 274 | tools/legacy_analyzer.py | 99 | 2h | {"pattern": r"//\s*TODO", "name": "todo_comment", "severity": "info"}, |
| 275 | tools/todo_audit.py | 113 | 2h | f.write("\| # \| File \| Line \| Estimated Hours \| TODO Content \|\n") |
| 276 | backend/src/connector/bridge.rs | 14 | 1h | // TODO: The circuit breaker parameters are hardcoded below. They should |
| 277 | backend/src/connector/bridge.rs | 28 | 1h | // TODO: Re-evaluate the least-loaded scheduler now that the race condition |
| 278 | backend/src/connector/legacy.rs | 21 | 1h | // TODO: The list of removed message types is documented in the migration |
| 279 | backend/src/connector/legacy.rs | 28 | 1h | // TODO: Add a metric to track how often this legacy shim is used. If usage |
| 280 | backend/src/legacy/deprecations.rs | 133 | 1h | // TODO: Add serde rename attributes once the S3 records have aged out. |
| 281 | backend/src/legacy/deprecations.rs | 238 | 1h | // TODO: REPLACE THIS WITH A PROPER MIGRATION STRATEGY |
| 282 | backend/src/legacy/deprecations.rs | 259 | 1h | // TODO: This function is not used anywhere. It was added as part of a |
| 283 | backend/src/legacy/deprecations.rs | 630 | 1h | // TODO: These tests are incomplete. They were written during a hackathon |
| 284 | backend/src/legacy/v1_compat.rs | 14 | 1h | // TODO: Remove this after v1 API sunset |
| 285 | backend/src/legacy/v1_compat.rs | 77 | 1h | // TODO: Fix the classification of GatewayTimeout |
| 286 | backend/src/legacy/v1_compat.rs | 119 | 1h | // TODO: Remove this envelope in the v2 API (which is also being deprecated) |
| 287 | backend/src/legacy/v1_compat.rs | 413 | 1h | // TODO: Complete the v1-to-v2 resource mapping |
| 288 | backend/src/protocol/events.rs | 14 | 1h | // TODO: Add a CI check that verifies all event types in this module have |
| 289 | backend/src/protocol/events.rs | 28 | 1h | /// TODO: Automate schema version management. Currently, engineers must |
| 290 | backend/src/protocol/serialize.rs | 21 | 1h | // TODO: Add support for compressed serialization (zstd, gzip). |
| 291 | compliance/ComplianceAuditor.java | 196 | 1h | // TODO: Actually implement SFTP transfer |
| 292 | frailbox/connector/api.h | 28 | 1h | * TODO: Remove this file when all connector types are migrated to |
| 293 | frailbox/engine/core/job_system.hpp | 266 | 1h | // TODO: This blocking behavior can cause priority inversion if a |
| 294 | frailbox/include/logger.h | 168 | 1h | * TODO: Add proper compile-time stripping of debug log messages. |
| 295 | frailbox/src/logger.c | 168 | 1h | * TODO: Change the default to the actual process name. |
| 296 | frailbox/src/logger.c | 672 | 1h | * TODO: Remove this when the test suite is fully migrated. |
| 297 | frailbox/tests/test_connector.c | 28 | 1h | * TODO: Migrate to a real test framework. The leading candidate is |
| 298 | frontend/src/hooks/useMarketData.ts | 7 | 1h | * TODO: In high-frequency trading scenarios, this hook creates too many |
| 299 | frontend/src/services/telemetry.ts | 21 | 1h | * TODO: Add support for sampling to reduce telemetry volume for high-traffic |
| 300 | frontend/src/utils/legacyCompat.ts | 273 | 1h | * TODO: Implement proper cache eviction with TTL and LRU. |
| 301 | frontend/src/utils/legacyCompat.ts | 406 | 1h | // TODO: Apply the AngularJS 1.6 number filter patch. |
| 302 | frontend/src/utils/legacyCompat.ts | 567 | 1h | * TODO: Handle circular references in deep copy. |
| 303 | frontend/src/utils/legacyCompat.ts | 588 | 1h | * TODO: Replace with lodash isEqual or a comparable utility. |
| 304 | market/analytics/collector.go | 273 | 1h | // TODO: Upgrade to nanosecond precision now that we've migrated |
| 305 | market/analytics/collector.go | 294 | 1h | // TODO: Fix the race condition in the batch flush logic. |
| 306 | market/analytics/collector.go | 693 | 1h | // TODO: Connect the alert system to the notification service. |
| 307 | market/gateway/api.go | 672 | 1h | // TODO: Upgrade to WebSocket connection |
| 308 | market/gateway/middleware.go | 28 | 1h | // TODO: Add integration tests that verify middleware ordering. The |
| 309 | market/gateway/middleware.go | 371 | 1h | // TODO: Implement gzip response compression |
| 310 | market/pricing/models.go | 147 | 1h | // TODO: Use CLDR data for locale-aware currency formatting. |
| 311 | tools/deploy.py | 14 | 1h | TODO: Remove this script when all environments have been migrated to |
| 312 | tools/legacy_analyzer.py | 133 | 1h | {"pattern": r"#\s*TODO", "name": "todo_comment", "severity": "info"}, |
| 313 | tools/legacy_migration.py | 609 | 1h | # TODO: Validate data checksums |
| 314 | tools/log_aggregator.py | 21 | 1h | TODO: The log parser in this script uses regex-based pattern matching |
| 315 | tools/terraform_import.py | 14 | 1h | TODO: Remove this tool once the Terraform Cloud migration is complete. |
| 316 | tools/todo_audit.py | 70 | 1h | if todo_pattern.search(line): |
| 317 | tools/todo_audit.py | 77 | 1h | return todos |
| 318 | tools/todo_audit.py | 84 | 1h | todos_with_estimates = [ |
| 319 | tools/todo_audit.py | 126 | 1h | f.write(f"- **Average per TODO:** {total_hours / len(todos_with_estimates):.1f}h\n") |
| 320 | tools/todo_audit.py | 133 | 1h | f.write("\n## TODOs by File\n\n") |
| 321 | tools/todo_audit.py | 147 | 1h | print("Searching for TODO comments (case-insensitive)...") |

## Statistics

- **Total TODOs:** 321
- **Total estimated hours:** 1243h
- **Average per TODO:** 3.9h

## TODOs by File

| File | Count |
|------|-------|
| backend/src/legacy/deprecations.rs | 38 |
| tools/todo_audit.py | 34 |
| frontend/src/utils/legacyCompat.ts | 24 |
| market/analytics/collector.go | 21 |
| tools/legacy_migration.py | 20 |
| frailbox/src/logger.c | 14 |
| market/pricing/models.go | 12 |
| frailbox/include/logger.h | 11 |
| backend/src/legacy/mod.rs | 10 |
| backend/src/legacy/migrations.rs | 9 |
| compliance/ComplianceAuditor.java | 9 |
| tools/legacy_analyzer.py | 9 |
| backend/src/legacy/v1_compat.rs | 8 |
| market/compliance/rules.go | 8 |
| market/gateway/api.go | 8 |
| frailbox/connector/api.c | 6 |
| frontend/src/services/api.ts | 6 |
| v2/services/market_stream.rb | 5 |
| frailbox/connector/protocol.c | 4 |
| market/gateway/middleware.go | 4 |
| backend/src/connector/types.rs | 4 |
| backend/src/connector/ffi.rs | 4 |
| backend/src/connector/bridge.rs | 3 |
| frontend/src/store/slices.ts | 2 |
| frontend/src/utils/dataService.ts | 2 |
| frontend/src/utils/formatters.ts | 2 |
| backend/src/connector/mod.rs | 2 |
| backend/src/protocol/validate.rs | 2 |
| frontend/src/services/auth.ts | 2 |
| backend/src/protocol/serialize.rs | 2 |
| docs/OPERATIONS.md | 2 |
| frailbox/engine/core/job_system.hpp | 2 |
| frontend/src/hooks/useWebSocket.ts | 2 |
| frontend/src/utils/dataTransforms.ts | 2 |
| frailbox/tests/test_connector.c | 2 |
| backend/src/connector/legacy.rs | 2 |
| backend/src/protocol/events.rs | 2 |
| backend/src/ai/mod.rs | 1 |
| backend/src/protocol/messages.rs | 1 |
| docs/ARCHITECTURE.md | 1 |
| docs/API_REFERENCE.md | 1 |
| frailbox/connector/shim.c | 1 |
| frailbox/connector/shim.h | 1 |
| frontend/src/styles/legacy.css | 1 |
| backend/src/protocol/codec.rs | 1 |
| backend/src/protocol/rpc.rs | 1 |
| tools/benchmark.py | 1 |
| tools/db_migration.py | 1 |
| backend/src/lib.rs | 1 |
| backend/src/protocol/mod.rs | 1 |
| frailbox/connector/protocol.h | 1 |
| frontend/src/ai/chat.ts | 1 |
| frontend/src/ai/recommendations.ts | 1 |
| frailbox/connector/api.h | 1 |
| frontend/src/hooks/useMarketData.ts | 1 |
| frontend/src/services/telemetry.ts | 1 |
| tools/deploy.py | 1 |
| tools/log_aggregator.py | 1 |
| tools/terraform_import.py | 1 |
