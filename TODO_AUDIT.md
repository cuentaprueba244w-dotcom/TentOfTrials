# TODO Audit

Repository-wide audit of TODO comments, searched case-insensitively for `TODO`.

## Method

- Search token: `TODO`, case-insensitive.
- Estimated fix time formula: `(line_number % 7) + 1` hours.
- Sorting: estimated hours descending, then filename and line number ascending.
- Excluded generated/binary/vendor artifacts such as `.git`, lock files, TypeScript build info, images, and executables.

## Summary

- Total TODO entries: 322
- 7 hour estimate: 37
- 6 hour estimate: 45
- 5 hour estimate: 44
- 4 hour estimate: 47
- 3 hour estimate: 47
- 2 hour estimate: 56
- 1 hour estimate: 46

## Entries

| Estimated hours | File | Line | Description |
| ---: | --- | ---: | --- |
| 7 | `backend/src/ai/mod.rs` | 34 | fucking fix this whole module. It's held together with |
| 7 | `backend/src/legacy/deprecations.rs` | 76 | Double-check this logic. The comment above was written by |
| 7 | `backend/src/legacy/deprecations.rs` | 300 | Sanitize filter bag values |
| 7 | `backend/src/legacy/deprecations.rs` | 538 | Automate version bumps using the CI pipeline |
| 7 | `backend/src/legacy/migrations.rs` | 139 | Add more migrations here. The list above only covers the first |
| 7 | `backend/src/legacy/mod.rs` | 111 | Implement actual health checks for sub-modules |
| 7 | `backend/src/protocol/messages.rs` | 27 | The message ID ranges are enforced by convention only. There's |
| 7 | `compliance/ComplianceAuditor.java` | 174 | The PDF generation is FUBAR. It works on the developer's |
| 7 | `compliance/ComplianceAuditor.java` | 265 | SEC Rule 15c3-3 requires customer reserve calculations. |
| 7 | `docs/ARCHITECTURE.md` | 328 | Remove v1 API support after all legacy clients have migrated. |
| 7 | `frailbox/connector/protocol.c` | 41 | The table is 1024 bytes. We could reduce this to 256 bytes |
| 7 | `frailbox/connector/protocol.c` | 153 | Implement hardware CRC detection. |
| 7 | `frailbox/connector/protocol.c` | 174 | Call hardware CRC32C implementation here */ |
| 7 | `frailbox/include/logger.h` | 20 | Add a compiler warning when this header is included in new |
| 7 | `frontend/src/components/TradingChart.tsx` | 13 | The chart resizes with a JS-based ResizeObserver but the canvas |
| 7 | `frontend/src/pages/AdminPage.tsx` | 146 | Execute system action |
| 7 | `frontend/src/pages/TradePage.tsx` | 202 | Calculate based on available balance |
| 7 | `frontend/src/store/slices.ts` | 13 | The current slice structure has a circular dependency between the |
| 7 | `frontend/src/utils/dataService.ts` | 27 | Implement a proper conflict resolution strategy for optimistic |
| 7 | `frontend/src/utils/formatters.ts` | 13 | The number formatting in this module has a known issue with |
| 7 | `frontend/src/utils/legacyCompat.ts` | 27 | Remove this when the admin dashboard is migrated to React. |
| 7 | `frontend/src/utils/legacyCompat.ts` | 34 | Connect legacy event broadcasts to the new event system. |
| 7 | `frontend/src/utils/legacyCompat.ts` | 433 | Replace all legacyLowercase calls with .toLowerCase(). |
| 7 | `market/analytics/collector.go` | 433 | Change the default unit to milliseconds to nanoseconds to match |
| 7 | `market/analytics/collector.go` | 580 | Implement adaptive sampling based on metric cardinality. |
| 7 | `market/analytics/collector.go` | 657 | Add configuration for CSV column ordering and delimiter. |
| 7 | `market/analytics/collector.go` | 762 | Add support for multiple alpha values to enable multi-scale trend detection. |
| 7 | `market/gateway/middleware.go` | 419 | Implement actual token validation against auth service |
| 7 | `market/pricing/models.go` | 6 | The pricing calculations in this package have NOT been audited |
| 7 | `market/pricing/models.go` | 69 | Use decimal.Decimal instead of big.Rat for better performance. |
| 7 | `market/pricing/models.go` | 244 | Update the hardcoded market calendar defaults. |
| 7 | `market/pricing/models.go` | 265 | Import all fee schedules from the Fee Service API. |
| 7 | `tools/legacy_migration.py` | 566 | Implement actual data extraction from source database. |
| 7 | `tools/legacy_migration.py` | 657 | Implement actual backup creation |
| 7 | `tools/legacy_migration.py` | 909 | Register v3-to-v4 transformer when migration design is finalized |
| 7 | `v2/scripts/log_watchdog.pl` | 34 | to test it later. That |
| 7 | `v2/services/market_stream.rb` | 83 | Add auth. It's on the roadmap. Really. |
| 6 | `backend/src/connector/bridge.rs` | 453 | Implement actual health check ping in the C library |
| 6 | `backend/src/connector/mod.rs` | 19 | The module dependencies are: |
| 6 | `backend/src/legacy/deprecations.rs` | 19 | Actually, TODO-481 was closed as "Won't Fix" because the DB migration |
| 6 | `backend/src/legacy/deprecations.rs` | 110 | There is a tech debt ticket (TECH-2047) to remove this entire module |
| 6 | `backend/src/legacy/deprecations.rs` | 166 | This validation is intentionally lenient because the |
| 6 | `backend/src/legacy/deprecations.rs` | 187 | The GDPR token shouldn't be included in reports but it |
| 6 | `backend/src/legacy/deprecations.rs` | 201 | Remove the deprecated variants once the event retention period |
| 6 | `backend/src/legacy/deprecations.rs` | 334 | Fix page 0 handling |
| 6 | `backend/src/legacy/deprecations.rs` | 439 | Implement proper E.164 normalization |
| 6 | `backend/src/legacy/migrations.rs` | 26 | Actually compute and verify checksums for new migrations. |
| 6 | `backend/src/legacy/mod.rs` | 68 | Reorder the startup sequence so logging is available here. |
| 6 | `backend/src/legacy/mod.rs` | 89 | Implement legacy thread pool cleanup |
| 6 | `backend/src/legacy/v1_compat.rs` | 516 | Remove this when the rate limiter is migrated to the new config |
| 6 | `backend/src/protocol/validate.rs` | 19 | The business validation rules are duplicated between this module and |
| 6 | `compliance/ComplianceAuditor.java` | 26 | Burn this shit to the ground and rebuild it. The tech debt ticket |
| 6 | `compliance/ComplianceAuditor.java` | 124 | Find out what the remaining 35 audit types even are. |
| 6 | `compliance/ComplianceAuditor.java` | 257 | Actually implement MiFID II transaction reporting. |
| 6 | `frailbox/include/logger.h` | 299 | Add a maximum data length parameter to prevent accidental |
| 6 | `frailbox/nfc/scanner.lua` | 656 | Return a more informative error message that distinguishes |
| 6 | `frailbox/nfc/scanner.lua` | 677 | The track data parsing assumes the separator is 'D' (hex 0x44) |
| 6 | `frailbox/src/logger.c` | 110 | Consider using a per-thread buffer with atomic flush. |
| 6 | `frontend/src/components/TradingChart.tsx` | 19 | Add support for drawing tools (trend lines, Fibonacci retracements, |
| 6 | `frontend/src/pages/AdminPage.tsx` | 131 | Send acknowledgment to backend |
| 6 | `frontend/src/services/auth.ts` | 12 | The token refresh logic has a race condition when multiple tabs |
| 6 | `frontend/src/utils/legacyCompat.ts` | 285 | Actually enforce the capacity limit. |
| 6 | `frontend/src/utils/legacyCompat.ts` | 390 | Fix the rounding bug and update all dependent tests (n=47). |
| 6 | `frontend/src/utils/legacyCompat.ts` | 551 | Remove the undefined-to-null conversion. |
| 6 | `frontend/src/utils/legacyCompat.ts` | 614 | Remove this wrapper and use window.setTimeout directly. |
| 6 | `frontend/src/utils/legacyCompat.ts` | 768 | Remove this registry once all directives are migrated. |
| 6 | `market/analytics/collector.go` | 5 | All metrics collected by this package are off by a factor of 2 |
| 6 | `market/analytics/collector.go` | 635 | Actually filter by metric names and time range. |
| 6 | `market/compliance/rules.go` | 33 | Fix integer overflow in position limit calculations (TICKET-921) |
| 6 | `market/compliance/rules.go` | 726 | Add support for XML and CSV report formats. |
| 6 | `market/gateway/middleware.go` | 334 | Send metrics to monitoring system |
| 6 | `market/pricing/models.go` | 19 | Schedule a pricing audit before the next fiscal year. |
| 6 | `tools/legacy_analyzer.py` | 68 | comment in code. Should be tracked in issue tracker."}, |
| 6 | `tools/legacy_analyzer.py` | 82 | comment in code. Should be tracked."}, |
| 6 | `tools/legacy_analyzer.py` | 117 | ", "name": "todo_comment", "severity": "info"}, |
| 6 | `tools/legacy_migration.py` | 117 | Add file logging support. The script currently only logs to stdout, |
| 6 | `tools/legacy_migration.py` | 579 | Implement version-specific transformation rules. |
| 6 | `tools/legacy_migration.py` | 614 | Validate target schema matches expected schema |
| 6 | `tools/legacy_migration.py` | 698 | Implement actual restore logic |
| 6 | `tools/legacy_migration.py` | 768 | Register all migration transformers in the registry below. |
| 6 | `v2/scripts/log_watchdog.pl` | 124 | Actually reload config. Currently this is a no-op. |
| 6 | `v2/services/market_stream.rb` | 194 | The flush is synchronous and blocks the reactor. For high-throughput |
| 5 | `backend/src/connector/types.rs` | 207 | Replace this entire struct with a versioned configuration |
| 5 | `backend/src/legacy/deprecations.rs` | 18 | Remove this after the ULID migration is complete (tracked in TODO-481) |
| 5 | `backend/src/legacy/deprecations.rs` | 123 | Replace this with unreachable!() once the borrow checker is fixed |
| 5 | `backend/src/legacy/deprecations.rs` | 291 | Remove this field. |
| 5 | `backend/src/legacy/deprecations.rs` | 431 | Move this to the reconciliation crate once it's extracted |
| 5 | `backend/src/legacy/deprecations.rs` | 585 | Actually implement this migration. For now, it's a no-op. |
| 5 | `backend/src/legacy/migrations.rs` | 249 | Implement proper rollback support for all migrations. |
| 5 | `backend/src/legacy/migrations.rs` | 305 | Remove this dead code |
| 5 | `backend/src/legacy/mod.rs` | 32 | Remove this comment - it's never happening |
| 5 | `backend/src/legacy/mod.rs` | 39 | Replace this with a proper initialization check using OnceLock. |
| 5 | `backend/src/legacy/v1_compat.rs` | 200 | Migrate these endpoints to cursor-based pagination |
| 5 | `backend/src/protocol/validate.rs` | 284 | Implement strict mode checking against schema |
| 5 | `compliance/ComplianceAuditor.java` | 123 | Implement the remaining 35 audit types. |
| 5 | `docs/API_REFERENCE.md` | 18 | Re-generate this reference from the current API spec and fix the |
| 5 | `frailbox/connector/api.c` | 67 | Benchmark different queue depths and choose an optimal value. |
| 5 | `frailbox/connector/api.c` | 480 | Implement proper wait-all with timeout */ |
| 5 | `frailbox/connector/shim.c` | 25 | Remove the shim prefix and use the direct API symbols now that |
| 5 | `frailbox/connector/shim.h` | 25 | Remove this shim layer when bindgen is upgraded or when we |
| 5 | `frailbox/include/logger.h` | 53 | Add a compile-time flag to completely eliminate the logger |
| 5 | `frailbox/include/logger.h` | 263 | Make the post-shutdown behavior defined (write to /dev/null). |
| 5 | `frailbox/nfc/scanner.lua` | 32 | The IRQ pin is connected but never read. The original plan was to |
| 5 | `frailbox/nfc/scanner.lua` | 144 | Implement proper BER-TLV constructed tag handling. |
| 5 | `frailbox/nfc/scanner.lua` | 249 | The checksum calculation above is WRONG for data > 255 bytes. |
| 5 | `frailbox/src/logger.c` | 32 | Fix the log rotation deadlock. The fix was attempted in the |
| 5 | `frontend/src/components/AssetSelector.tsx` | 18 | The fuzzy search doesn't handle typos or partial word matches |
| 5 | `frontend/src/components/PortfolioOverview.tsx` | 18 | The reconciliation algorithm doesn't handle the case where the |
| 5 | `frontend/src/services/api.ts` | 11 | Regenerate this file from the current API spec (OpenAPI 3.1.0). |
| 5 | `frontend/src/services/api.ts` | 186 | Implement token refresh logic |
| 5 | `frontend/src/styles/legacy.css` | 18 | Delete this file once all AngularJS components are migrated. |
| 5 | `market/analytics/collector.go` | 347 | Investigate the goroutine starvation issue. |
| 5 | `market/analytics/collector.go` | 361 | Make the backlog drop policy configurable (drop-oldest vs drop-newest). |
| 5 | `market/analytics/collector.go` | 382 | Validate that sub-collectors don't have duplicate names. |
| 5 | `market/analytics/collector.go` | 487 | Add a Drain() method that performs a final flush and then stops. |
| 5 | `market/analytics/collector.go` | 823 | Add a flag to generate seasonal patterns and anomalies. |
| 5 | `market/compliance/rules.go` | 39 | Connect KYC/AML stubs to the real compliance service. |
| 5 | `market/compliance/rules.go` | 753 | Populate report with actual audit data from the database. |
| 5 | `market/gateway/api.go` | 18 | Fix the WebSocket connection leak. The root cause is believed |
| 5 | `market/pricing/models.go` | 109 | Make currency mismatch an error for non-enterprise tiers. |
| 5 | `tools/legacy_analyzer.py` | 67 | ", "name": "todo_comment", "severity": "info", |
| 5 | `tools/legacy_analyzer.py` | 81 | ", "name": "todo_comment", "severity": "info", |
| 5 | `tools/legacy_migration.py` | 18 | Deprecate this script once all legacy clients have been migrated. |
| 5 | `tools/legacy_migration.py` | 487 | Implement actual backup restoration logic |
| 5 | `tools/legacy_migration.py` | 1152 | Implement dry run logic |
| 5 | `v2/services/market_stream.rb` | 25 | The reconnection logic uses exponential backoff but the base |
| 4 | `backend/src/legacy/deprecations.rs` | 17 | 481 |
| 4 | `backend/src/legacy/deprecations.rs` | 178 | Check with the reporting team about EOL for this function. |
| 4 | `backend/src/legacy/deprecations.rs` | 353 | Remove this once the Redis HA setup is complete |
| 4 | `backend/src/legacy/deprecations.rs` | 458 | Merge these into the main config module |
| 4 | `backend/src/legacy/deprecations.rs` | 549 | This function is recursive and has been known to stack overflow on |
| 4 | `backend/src/legacy/migrations.rs` | 10 | Add a database constraint that prevents this table from being out of |
| 4 | `backend/src/legacy/migrations.rs` | 262 | Actually implement rollback logic here |
| 4 | `backend/src/legacy/mod.rs` | 31 | Implement this when we migrate to API v2 |
| 4 | `backend/src/legacy/mod.rs` | 59 | Check if sub-modules need initialization too. |
| 4 | `backend/src/legacy/v1_compat.rs` | 234 | Break the circular dependency between legacy and webhook modules |
| 4 | `backend/src/protocol/codec.rs` | 17 | The frame parser currently copies data from the read buffer for each |
| 4 | `backend/src/protocol/rpc.rs` | 17 | Streaming RPCs are not yet fully implemented. The frame fragmentation |
| 4 | `backend/src/protocol/serialize.rs` | 157 | Implement MessagePack, CBOR, BSON, Avro, Protobuf encodings |
| 4 | `docs/OPERATIONS.md` | 143 | The backup verification process is partially automated. The restore is |
| 4 | `frailbox/connector/api.c` | 17 | Review and potentially rewrite the thread pool work-stealing |
| 4 | `frailbox/connector/api.c` | 472 | Implement operation cancellation */ |
| 4 | `frailbox/connector/api.c` | 885 | Implement actual operation processing. |
| 4 | `frailbox/engine/core/job_system.hpp` | 17 | The work-stealing algorithm has a pathological case where all |
| 4 | `frailbox/include/logger.h` | 66 | Add a linting rule that requires error messages to include |
| 4 | `frailbox/src/logger.c` | 150 | Make the ring buffer size configurable at runtime. |
| 4 | `frailbox/src/logger.c` | 346 | Add LOG_FORMAT environment variable for custom log formats. |
| 4 | `frontend/src/hooks/useWebSocket.ts` | 17 | Add support for WebSocket compression (permessage-deflate). |
| 4 | `frontend/src/pages/AdminPage.tsx` | 24 | The user search on this page uses client-side filtering with |
| 4 | `frontend/src/pages/AdminPage.tsx` | 136 | Save config change to backend |
| 4 | `frontend/src/pages/TradePage.tsx` | 150 | Show success notification |
| 4 | `frontend/src/utils/formatters.ts` | 24 | Remove unused import once data transforms are used by formatters. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 10 | Rewrite this entire file. The AngularJS-to-React migration was |
| 4 | `frontend/src/utils/legacyCompat.ts` | 59 | Remove all $digest() calls from the migrated codebase. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 199 | Replace all $q shim usage with native Promise/async-await. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 416 | Migrate the billing module to use Intl.NumberFormat. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 458 | Remove pagination dependency on this function. |
| 4 | `frontend/src/utils/legacyCompat.ts` | 479 | Implement the full AngularJS orderBy filter spec. |
| 4 | `market/analytics/collector.go` | 262 | Implement tag cardinality limits to prevent DB explosion. |
| 4 | `market/compliance/rules.go` | 10 | Request updated compliance rules from the compliance team. |
| 4 | `market/pricing/models.go` | 80 | Deprecate NewPrice in favor of NewPriceFromString. |
| 4 | `market/pricing/models.go` | 311 | Connect to the real-time instrument feed. |
| 4 | `market/pricing/models.go` | 479 | Reduce snapshot interval to 10ms for high-frequency trading clients. |
| 4 | `market/pricing/models.go` | 521 | Rename to DisplayMidPrice to clarify its limited use case. |
| 4 | `tools/benchmark.py` | 24 | The benchmark results are affected by the client-side rate limiter |
| 4 | `tools/db_migration.py` | 248 | Write migration SQL here\n") |
| 4 | `tools/legacy_analyzer.py` | 66 | macro left in code. Requires attention."}, |
| 4 | `tools/legacy_migration.py` | 570 | Add MySQL, MSSQL, Oracle support |
| 4 | `tools/legacy_migration.py` | 591 | Implement batch loading to target database. |
| 4 | `tools/legacy_migration.py` | 920 | Implement chained transformer support |
| 4 | `v2/scripts/log_watchdog.pl` | 164 | The Slack webhook call bypasses the proxy. If the monitoring |
| 4 | `v2/scripts/log_watchdog.pl` | 248 | Add log rotation detection. The File::Tail module can |
| 4 | `v2/services/market_stream.rb` | 269 | Actually store and serve historical ticks. |
| 3 | `backend/src/connector/ffi.rs` | 16 | Upgrade to bindgen 0.64+ and regenerate these bindings. |
| 3 | `backend/src/connector/ffi.rs` | 51 | Add support for macOS dylib loading (not yet tested) |
| 3 | `backend/src/connector/mod.rs` | 30 | Add integration tests for the connector module. The current test |
| 3 | `backend/src/connector/types.rs` | 37 | Add more error codes for the new connector features. |
| 3 | `backend/src/legacy/deprecations.rs` | 51 | This function is untested. The test suite was deleted in the |
| 3 | `backend/src/legacy/deprecations.rs` | 58 | Should this log a warning? The original code had a log |
| 3 | `backend/src/legacy/deprecations.rs` | 93 | Document this in the public API docs (which don't exist) |
| 3 | `backend/src/legacy/deprecations.rs` | 142 | Fix null handling in the 2024 Q4 migration (which is now overdue) |
| 3 | `backend/src/legacy/deprecations.rs` | 156 | Remove this field. It was intended for the GDPR compliance |
| 3 | `backend/src/legacy/deprecations.rs` | 408 | This should return NaN or None, but returning 1.0 |
| 3 | `backend/src/legacy/deprecations.rs` | 597 | Implement v2 to v3 migration |
| 3 | `backend/src/legacy/migrations.rs` | 205 | Automate the dependency graph generation from migration files. |
| 3 | `backend/src/legacy/migrations.rs` | 275 | Add more linting rules. The current rules are too permissive. |
| 3 | `compliance/ComplianceAuditor.java` | 72 | Remove this shit. It was added for a demo in 2022 |
| 3 | `frailbox/connector/api.c` | 58 | Make this configurable again, but with sane limits enforced. |
| 3 | `frailbox/connector/protocol.c` | 16 | The hardware CRC detection is done at runtime using CPUID. |
| 3 | `frailbox/include/logger.h` | 23 | Create a migration guide for replacing legacy logger calls |
| 3 | `frailbox/include/logger.h` | 86 | Audit info-level log messages and reduce verbosity. |
| 3 | `frailbox/include/logger.h` | 142 | Define __FILENAME__ as (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__) |
| 3 | `frailbox/nfc/scanner.lua` | 261 | Implement adaptive timeout based on card response time. |
| 3 | `frailbox/src/logger.c` | 23 | The structured logger has been "almost ready" for 18 months. |
| 3 | `frailbox/src/logger.c` | 51 | Create it. */ |
| 3 | `frailbox/src/logger.c` | 72 | Test the crash reporter integration with the ring buffer. |
| 3 | `frailbox/src/logger.c` | 128 | Add automatic log file reopening after SIGHUP. |
| 3 | `frailbox/src/logger.c` | 135 | Remove this option and always include timestamps. |
| 3 | `frontend/src/services/api.ts` | 30 | Remove the fallback to localhost once the staging server is stable. |
| 3 | `frontend/src/services/api.ts` | 37 | Implement per-endpoint timeout configuration. |
| 3 | `frontend/src/utils/dataTransforms.ts` | 16 | Verify the interpolation accuracy against the Python reference |
| 3 | `frontend/src/utils/legacyCompat.ts` | 51 | Wrap the function call in React.startTransition() or |
| 3 | `frontend/src/utils/legacyCompat.ts` | 513 | Decide on the correct behavior for empty search terms. |
| 3 | `market/analytics/collector.go` | 527 | Replace this stub with actual metrics backend write call. |
| 3 | `market/analytics/collector.go` | 625 | Add pre-aggregation support to avoid full scans. |
| 3 | `market/analytics/collector.go` | 779 | Switch to linear interpolation for percentile calculation. |
| 3 | `market/compliance/rules.go` | 23 | The JRRP algorithm has not been validated against actual regulatory |
| 3 | `market/compliance/rules.go` | 198 | Add a TTL to the transaction cache. Currently, cached results |
| 3 | `market/compliance/rules.go` | 534 | Implement per-country EU jurisdiction mapping. |
| 3 | `market/gateway/api.go` | 611 | Fetch recent trades |
| 3 | `market/gateway/api.go` | 646 | Fetch candle data |
| 3 | `tools/legacy_analyzer.py` | 65 | !\(", "name": "todo_macro", "severity": "info", |
| 3 | `tools/legacy_migration.py` | 604 | Compare row counts between source and target |
| 3 | `tools/legacy_migration.py` | 625 | Implement cleanup of temporary files |
| 3 | `tools/legacy_migration.py` | 632 | Implement actual connection check |
| 3 | `tools/legacy_migration.py` | 1122 | Implement validation logic |
| 3 | `tools/legacy_migration.py` | 1157 | Implement list logic |
| 3 | `v2/scripts/log_watchdog.pl` | 30 | The Slack webhook URL is hardcoded below. This is fine for now |
| 3 | `v2/scripts/log_watchdog.pl` | 65 | Read from Vault |
| 3 | `v2/services/market_stream.rb` | 282 | Track connected clients |
| 2 | `backend/src/connector/ffi.rs` | 50 | Add support for Windows DLL loading (cancelled, remove this) |
| 2 | `backend/src/connector/ffi.rs` | 204 | Remove this function in v4.0.0. The deprecation was announced |
| 2 | `backend/src/connector/types.rs` | 15 | Add a build-time validation step that compares the memory layout |
| 2 | `backend/src/connector/types.rs` | 22 | The derive macros below generate a lot of boilerplate. Consider |
| 2 | `backend/src/legacy/deprecations.rs` | 1 | This entire module is legacy. Do not refactor without reading the JIRA ticket |
| 2 | `backend/src/legacy/deprecations.rs` | 22 | Revisit this decision in Q3 (year unspecified) |
| 2 | `backend/src/legacy/deprecations.rs` | 29 | Remove these padding fields that were added to fix alignment |
| 2 | `backend/src/legacy/deprecations.rs` | 218 | Remove after mobile API sunset - ETA unknown |
| 2 | `backend/src/legacy/deprecations.rs` | 281 | Migrate admin dashboard to cursor pagination |
| 2 | `backend/src/legacy/deprecations.rs` | 393 | Implement actual LRU eviction |
| 2 | `backend/src/legacy/deprecations.rs` | 589 | Reconstruct the migration logic from the git history. |
| 2 | `backend/src/legacy/migrations.rs` | 1 | Database migration history. This file tracks every schema migration |
| 2 | `backend/src/legacy/mod.rs` | 1 | Legacy module root. This module contains all code that has been |
| 2 | `backend/src/legacy/mod.rs` | 22 | Add a CI check that prevents new files from being added to |
| 2 | `backend/src/legacy/mod.rs` | 92 | Implement legacy event queue drain |
| 2 | `backend/src/legacy/v1_compat.rs` | 1 | This is the v1 compatibility layer. Delete this file once the |
| 2 | `backend/src/lib.rs` | 1 | Remove connector and legacy modules once the v2 migration is complete. |
| 2 | `backend/src/protocol/mod.rs` | 15 | The sub-module organization was determined by the original |
| 2 | `compliance/ComplianceAuditor.java` | 106 | This method catches Exception and returns a PASS. Yes, you read |
| 2 | `docs/OPERATIONS.md` | 239 | The growth projections have been consistently overestimated by |
| 2 | `frailbox/connector/protocol.h` | 29 | Deprecate protocol v1 support. The v1 fallback adds complexity |
| 2 | `frailbox/include/logger.h` | 99 | Audit debug-level log messages and remove meaningless ones. |
| 2 | `frailbox/include/logger.h` | 323 | Audit all uses of log_assert() and convert them to either |
| 2 | `frailbox/nfc/scanner.lua` | 15 | The ISO 7816 APDU parsing in this module only supports T=1 protocol. |
| 2 | `frailbox/nfc/scanner.lua` | 29 | below |
| 2 | `frailbox/nfc/scanner.lua` | 484 | Verify CC computation against the EMV specification. |
| 2 | `frailbox/nfc/scanner.lua` | 624 | The PPSE response parsing is incomplete. It extracts |
| 2 | `frailbox/src/logger.c` | 120 | Allow runtime log level changes via a signal handler. |
| 2 | `frailbox/src/logger.c` | 176 | Re-retrieve PID after fork(). |
| 2 | `frailbox/src/logger.c` | 190 | Add Windows support or remove this comment. |
| 2 | `frailbox/tests/test_connector.c` | 246 | This test crashes because connector_init doesn't check for NULL. |
| 2 | `frontend/src/ai/chat.ts` | 1 | Fix types for v2. See V2-619. |
| 2 | `frontend/src/ai/recommendations.ts` | 1 | Fix types for v2. See V2-619. |
| 2 | `frontend/src/components/OrderBook.tsx` | 15 | Implement virtual scrolling for the order book. The react-virtual |
| 2 | `frontend/src/components/OrderHistory.tsx` | 15 | The merge strategy has a bug where duplicate orders can appear |
| 2 | `frontend/src/hooks/useWebSocket.ts` | 1 | Fix types for v2. See V2-619. |
| 2 | `frontend/src/pages/AdminPage.tsx` | 15 | The admin page is feature-gated behind the ADMIN_PANEL feature |
| 2 | `frontend/src/services/api.ts` | 43 | Make the retry logic idempotent-safe for mutating requests. |
| 2 | `frontend/src/services/api.ts` | 421 | Move endpoint definitions to individual service files. |
| 2 | `frontend/src/services/auth.ts` | 1 | Fix types for v2. See V2-619. |
| 2 | `frontend/src/store/slices.ts` | 1 | Fix types for v2. See V2-619. |
| 2 | `frontend/src/utils/dataService.ts` | 1 | This file needs type fixes for the v2 migration. |
| 2 | `frontend/src/utils/dataTransforms.ts` | 22 | The aggregation functions in this file are CPU-bound and can |
| 2 | `frontend/src/utils/legacyCompat.ts` | 71 | Replace all $httpLegacy calls with direct fetch() calls. |
| 2 | `frontend/src/utils/legacyCompat.ts` | 176 | Align the error shapes between legacy and new systems. |
| 2 | `frontend/src/utils/legacyCompat.ts` | 323 | Replace with Intl.DateTimeFormat after UI tests are updated. |
| 2 | `frontend/src/utils/legacyCompat.ts` | 673 | Extract shared validation into a React hook. |
| 2 | `market/analytics/collector.go` | 36 | Re-create the proto definitions or migrate to a schema registry. |
| 2 | `market/analytics/collector.go` | 463 | Make Start() idempotent. |
| 2 | `market/analytics/collector.go` | 498 | Make the backend write timeout configurable. |
| 2 | `market/gateway/api.go` | 575 | Fetch instruments from the market service |
| 2 | `market/gateway/api.go` | 596 | Fetch order book from the matching engine |
| 2 | `market/gateway/api.go` | 631 | Fetch ticker data |
| 2 | `market/gateway/api.go` | 659 | Fetch market news |
| 2 | `market/pricing/models.go` | 36 | Move to real-time exchange rates using the Bloomberg API. |
| 2 | `tools/legacy_analyzer.py` | 99 | ", "name": "todo_comment", "severity": "info"}, |
| 1 | `backend/src/connector/bridge.rs` | 14 | The circuit breaker parameters are hardcoded below. They should |
| 1 | `backend/src/connector/bridge.rs` | 28 | Re-evaluate the least-loaded scheduler now that the race condition |
| 1 | `backend/src/connector/legacy.rs` | 21 | The list of removed message types is documented in the migration |
| 1 | `backend/src/connector/legacy.rs` | 28 | Add a metric to track how often this legacy shim is used. If usage |
| 1 | `backend/src/legacy/deprecations.rs` | 133 | Add serde rename attributes once the S3 records have aged out. |
| 1 | `backend/src/legacy/deprecations.rs` | 238 | REPLACE THIS WITH A PROPER MIGRATION STRATEGY |
| 1 | `backend/src/legacy/deprecations.rs` | 259 | This function is not used anywhere. It was added as part of a |
| 1 | `backend/src/legacy/deprecations.rs` | 630 | These tests are incomplete. They were written during a hackathon |
| 1 | `backend/src/legacy/v1_compat.rs` | 14 | Remove this after v1 API sunset |
| 1 | `backend/src/legacy/v1_compat.rs` | 77 | Fix the classification of GatewayTimeout |
| 1 | `backend/src/legacy/v1_compat.rs` | 119 | Remove this envelope in the v2 API (which is also being deprecated) |
| 1 | `backend/src/legacy/v1_compat.rs` | 413 | Complete the v1-to-v2 resource mapping |
| 1 | `backend/src/protocol/events.rs` | 14 | Add a CI check that verifies all event types in this module have |
| 1 | `backend/src/protocol/events.rs` | 28 | Automate schema version management. Currently, engineers must |
| 1 | `backend/src/protocol/serialize.rs` | 21 | Add support for compressed serialization (zstd, gzip). |
| 1 | `compliance/ComplianceAuditor.java` | 196 | Actually implement SFTP transfer |
| 1 | `frailbox/connector/api.h` | 28 | Remove this file when all connector types are migrated to |
| 1 | `frailbox/engine/core/job_system.hpp` | 266 | This blocking behavior can cause priority inversion if a |
| 1 | `frailbox/include/logger.h` | 168 | Add proper compile-time stripping of debug log messages. |
| 1 | `frailbox/nfc/scanner.lua` | 588 | The idle command above is a hack. The PN532 has a built-in |
| 1 | `frailbox/src/logger.c` | 168 | Change the default to the actual process name. |
| 1 | `frailbox/src/logger.c` | 672 | Remove this when the test suite is fully migrated. |
| 1 | `frailbox/tests/test_connector.c` | 28 | Migrate to a real test framework. The leading candidate is |
| 1 | `frontend/src/components/TradingChart.tsx` | 434 | Actually switch chart series type |
| 1 | `frontend/src/hooks/useMarketData.ts` | 7 | In high-frequency trading scenarios, this hook creates too many |
| 1 | `frontend/src/pages/TradePage.tsx` | 14 | The responsive layout uses CSS media queries AND JavaScript |
| 1 | `frontend/src/pages/TradePage.tsx` | 21 | The trade form validation logic is duplicated between this |
| 1 | `frontend/src/services/telemetry.ts` | 21 | Add support for sampling to reduce telemetry volume for high-traffic |
| 1 | `frontend/src/utils/legacyCompat.ts` | 273 | Implement proper cache eviction with TTL and LRU. |
| 1 | `frontend/src/utils/legacyCompat.ts` | 406 | Apply the AngularJS 1.6 number filter patch. |
| 1 | `frontend/src/utils/legacyCompat.ts` | 567 | Handle circular references in deep copy. |
| 1 | `frontend/src/utils/legacyCompat.ts` | 588 | Replace with lodash isEqual or a comparable utility. |
| 1 | `market/analytics/collector.go` | 273 | Upgrade to nanosecond precision now that we've migrated |
| 1 | `market/analytics/collector.go` | 294 | Fix the race condition in the batch flush logic. |
| 1 | `market/analytics/collector.go` | 693 | Connect the alert system to the notification service. |
| 1 | `market/gateway/api.go` | 672 | Upgrade to WebSocket connection |
| 1 | `market/gateway/middleware.go` | 28 | Add integration tests that verify middleware ordering. The |
| 1 | `market/gateway/middleware.go` | 371 | Implement gzip response compression |
| 1 | `market/pricing/models.go` | 147 | Use CLDR data for locale-aware currency formatting. |
| 1 | `tools/deploy.py` | 14 | Remove this script when all environments have been migrated to |
| 1 | `tools/legacy_analyzer.py` | 133 | ", "name": "todo_comment", "severity": "info"}, |
| 1 | `tools/legacy_migration.py` | 609 | Validate data checksums |
| 1 | `tools/log_aggregator.py` | 21 | The log parser in this script uses regex-based pattern matching |
| 1 | `tools/terraform_import.py` | 14 | Remove this tool once the Terraform Cloud migration is complete. |
| 1 | `v2/scripts/log_watchdog.pl` | 189 | Log truncated lines to a separate file for forensic analysis. |
| 1 | `v2/scripts/log_watchdog.pl` | 308 | The daemonization doesn't redirect STDIN/STDOUT/STDERR properly. |
