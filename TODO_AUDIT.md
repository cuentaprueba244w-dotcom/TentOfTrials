# TODO Audit Report

Comprehensive listing of all TODO comments found in the repository.
Search is case-insensitive for TODO.

**Total TODOs found:** 334
**Estimate formula:** `(line_number % 7) + 1` hours
**Sort order:** Estimated hours descending

## Summary by Language

| Language | Count |
|----------|-------|
| Rust | 92 |
| TypeScript | 62 |
| Python | 59 |
| Go | 53 |
| C | 27 |
| C/C++ | 14 |
| Lua | 11 |
| Java | 9 |
| Ruby | 5 |
| C++ | 2 |

## Summary by Estimated Fix Time

| Estimated Hours | Count |
|-----------------|-------|
| 7h | 36 |
| 6h | 49 |
| 5h | 47 |
| 4h | 45 |
| 3h | 51 |
| 2h | 59 |
| 1h | 47 |

## Detailed TODO Listing

| # | Filename | Line | Description | Est. Hours |
|---|----------|------|-------------|------------|
| 1 | `backend/src/ai/mod.rs` | 34 | fucking fix this whole module. It's held together with | 7h |
| 2 | `backend/src/legacy/deprecations.rs` | 76 | Double-check this logic. The comment above was written by | 7h |
| 3 | `backend/src/legacy/deprecations.rs` | 300 | Sanitize filter bag values | 7h |
| 4 | `backend/src/legacy/deprecations.rs` | 538 | Automate version bumps using the CI pipeline | 7h |
| 5 | `backend/src/legacy/migrations.rs` | 139 | Add more migrations here. The list above only covers the first | 7h |
| 6 | `backend/src/legacy/mod.rs` | 111 | Implement actual health checks for sub-modules | 7h |
| 7 | `backend/src/protocol/messages.rs` | 27 | The message ID ranges are enforced by convention only. There's | 7h |
| 8 | `compliance/ComplianceAuditor.java` | 174 | The PDF generation is FUBAR. It works on the developer's | 7h |
| 9 | `compliance/ComplianceAuditor.java` | 265 | SEC Rule 15c3-3 requires customer reserve calculations. | 7h |
| 10 | `frailbox/connector/protocol.c` | 41 | The table is 1024 bytes. We could reduce this to 256 bytes | 7h |
| 11 | `frailbox/connector/protocol.c` | 153 | Implement hardware CRC detection. | 7h |
| 12 | `frailbox/connector/protocol.c` | 174 | Call hardware CRC32C implementation here | 7h |
| 13 | `frailbox/include/logger.h` | 20 | Add a compiler warning when this header is included in new | 7h |
| 14 | `frontend/src/components/TradingChart.tsx` | 13 | The chart resizes with a JS-based ResizeObserver but the canvas | 7h |
| 15 | `frontend/src/pages/AdminPage.tsx` | 146 | Execute system action | 7h |
| 16 | `frontend/src/pages/TradePage.tsx` | 202 | Calculate based on available balance | 7h |
| 17 | `frontend/src/store/slices.ts` | 13 | The current slice structure has a circular dependency between the | 7h |
| 18 | `frontend/src/utils/dataService.ts` | 27 | Implement a proper conflict resolution strategy for optimistic | 7h |
| 19 | `frontend/src/utils/formatters.ts` | 13 | The number formatting in this module has a known issue with | 7h |
| 20 | `frontend/src/utils/legacyCompat.ts` | 27 | Remove this when the admin dashboard is migrated to React. | 7h |
| 21 | `frontend/src/utils/legacyCompat.ts` | 34 | Connect legacy event broadcasts to the new event system. | 7h |
| 22 | `frontend/src/utils/legacyCompat.ts` | 433 | Replace all legacyLowercase calls with .toLowerCase(). | 7h |
| 23 | `generate_todo_audit.py` | 48 | (no description) | 7h |
| 24 | `market/analytics/collector.go` | 433 | Change the default unit to milliseconds to nanoseconds to match | 7h |
| 25 | `market/analytics/collector.go` | 580 | Implement adaptive sampling based on metric cardinality. | 7h |
| 26 | `market/analytics/collector.go` | 657 | Add configuration for CSV column ordering and delimiter. | 7h |
| 27 | `market/analytics/collector.go` | 762 | Add support for multiple alpha values to enable multi-scale trend detection. | 7h |
| 28 | `market/gateway/middleware.go` | 419 | Implement actual token validation against auth service | 7h |
| 29 | `market/pricing/models.go` | 6 | The pricing calculations in this package have NOT been audited | 7h |
| 30 | `market/pricing/models.go` | 69 | Use decimal.Decimal instead of big.Rat for better performance. | 7h |
| 31 | `market/pricing/models.go` | 244 | Update the hardcoded market calendar defaults. | 7h |
| 32 | `market/pricing/models.go` | 265 | Import all fee schedules from the Fee Service API. | 7h |
| 33 | `tools/legacy_migration.py` | 566 | Implement actual data extraction from source database. | 7h |
| 34 | `tools/legacy_migration.py` | 657 | Implement actual backup creation | 7h |
| 35 | `tools/legacy_migration.py` | 909 | Register v3-to-v4 transformer when migration design is finalized | 7h |
| 36 | `v2/services/market_stream.rb` | 83 | Add auth. It's on the roadmap. Really. | 7h |
| 37 | `backend/src/connector/bridge.rs` | 453 | Implement actual health check ping in the C library | 6h |
| 38 | `backend/src/connector/mod.rs` | 19 | The module dependencies are: | 6h |
| 39 | `backend/src/legacy/deprecations.rs` | 19 | Actually, TODO-481 was closed as "Won't Fix" because the DB migration | 6h |
| 40 | `backend/src/legacy/deprecations.rs` | 110 | There is a tech debt ticket (TECH-2047) to remove this entire module | 6h |
| 41 | `backend/src/legacy/deprecations.rs` | 166 | This validation is intentionally lenient because the | 6h |
| 42 | `backend/src/legacy/deprecations.rs` | 187 | The GDPR token shouldn't be included in reports but it | 6h |
| 43 | `backend/src/legacy/deprecations.rs` | 201 | Remove the deprecated variants once the event retention period | 6h |
| 44 | `backend/src/legacy/deprecations.rs` | 334 | Fix page 0 handling | 6h |
| 45 | `backend/src/legacy/deprecations.rs` | 439 | Implement proper E.164 normalization | 6h |
| 46 | `backend/src/legacy/migrations.rs` | 26 | Actually compute and verify checksums for new migrations. | 6h |
| 47 | `backend/src/legacy/mod.rs` | 68 | Reorder the startup sequence so logging is available here. | 6h |
| 48 | `backend/src/legacy/mod.rs` | 89 | Implement legacy thread pool cleanup | 6h |
| 49 | `backend/src/legacy/v1_compat.rs` | 516 | Remove this when the rate limiter is migrated to the new config | 6h |
| 50 | `backend/src/protocol/validate.rs` | 19 | The business validation rules are duplicated between this module and | 6h |
| 51 | `compliance/ComplianceAuditor.java` | 26 | Burn this shit to the ground and rebuild it. The tech debt ticket | 6h |
| 52 | `compliance/ComplianceAuditor.java` | 124 | Find out what the remaining 35 audit types even are. | 6h |
| 53 | `compliance/ComplianceAuditor.java` | 257 | Actually implement MiFID II transaction reporting. | 6h |
| 54 | `frailbox/include/logger.h` | 299 | Add a maximum data length parameter to prevent accidental | 6h |
| 55 | `frailbox/nfc/scanner.lua` | 656 | Return a more informative error message that distinguishes | 6h |
| 56 | `frailbox/nfc/scanner.lua` | 677 | The track data parsing assumes the separator is 'D' (hex 0x44) | 6h |
| 57 | `frailbox/src/logger.c` | 110 | Consider using a per-thread buffer with atomic flush. | 6h |
| 58 | `frontend/src/components/TradingChart.tsx` | 19 | Add support for drawing tools (trend lines, Fibonacci retracements, | 6h |
| 59 | `frontend/src/pages/AdminPage.tsx` | 131 | Send acknowledgment to backend | 6h |
| 60 | `frontend/src/services/auth.ts` | 12 | The token refresh logic has a race condition when multiple tabs | 6h |
| 61 | `frontend/src/utils/legacyCompat.ts` | 285 | Actually enforce the capacity limit. | 6h |
| 62 | `frontend/src/utils/legacyCompat.ts` | 390 | Fix the rounding bug and update all dependent tests (n=47). | 6h |
| 63 | `frontend/src/utils/legacyCompat.ts` | 551 | Remove the undefined-to-null conversion. | 6h |
| 64 | `frontend/src/utils/legacyCompat.ts` | 614 | Remove this wrapper and use window.setTimeout directly. | 6h |
| 65 | `frontend/src/utils/legacyCompat.ts` | 768 | Remove this registry once all directives are migrated. | 6h |
| 66 | `generate_todo_audit.py` | 47 | ', line, re.IGNORECASE): | 6h |
| 67 | `generate_todo_audit.py` | 75 | _AUDIT.md content.""" | 6h |
| 68 | `generate_todo_audit.py` | 82 | s found:** {len(todos)}") | 6h |
| 69 | `generate_todo_audit.py` | 89 | s: | 6h |
| 70 | `generate_todo_audit.py` | 103 | s: | 6h |
| 71 | `market/analytics/collector.go` | 5 | All metrics collected by this package are off by a factor of 2 | 6h |
| 72 | `market/analytics/collector.go` | 635 | Actually filter by metric names and time range. | 6h |
| 73 | `market/compliance/rules.go` | 33 | Fix integer overflow in position limit calculations (TICKET-921) | 6h |
| 74 | `market/compliance/rules.go` | 726 | Add support for XML and CSV report formats. | 6h |
| 75 | `market/gateway/middleware.go` | 334 | Send metrics to monitoring system | 6h |
| 76 | `market/pricing/models.go` | 19 | Schedule a pricing audit before the next fiscal year. | 6h |
| 77 | `tools/legacy_analyzer.py` | 68 | comment in code. Should be tracked in issue tracker."}, | 6h |
| 78 | `tools/legacy_analyzer.py` | 82 | comment in code. Should be tracked."}, | 6h |
| 79 | `tools/legacy_analyzer.py` | 117 | ", "name": "todo_comment", "severity": "info"}, | 6h |
| 80 | `tools/legacy_migration.py` | 117 | Add file logging support. The script currently only logs to stdout, | 6h |
| 81 | `tools/legacy_migration.py` | 579 | Implement version-specific transformation rules. | 6h |
| 82 | `tools/legacy_migration.py` | 614 | Validate target schema matches expected schema | 6h |
| 83 | `tools/legacy_migration.py` | 698 | Implement actual restore logic | 6h |
| 84 | `tools/legacy_migration.py` | 768 | Register all migration transformers in the registry below. | 6h |
| 85 | `v2/services/market_stream.rb` | 194 | The flush is synchronous and blocks the reactor. For high-throughput | 6h |
| 86 | `backend/src/connector/types.rs` | 207 | Replace this entire struct with a versioned configuration | 5h |
| 87 | `backend/src/legacy/deprecations.rs` | 18 | Remove this after the ULID migration is complete (tracked in TODO-481) | 5h |
| 88 | `backend/src/legacy/deprecations.rs` | 123 | Replace this with unreachable!() once the borrow checker is fixed | 5h |
| 89 | `backend/src/legacy/deprecations.rs` | 291 | Remove this field. | 5h |
| 90 | `backend/src/legacy/deprecations.rs` | 431 | Move this to the reconciliation crate once it's extracted | 5h |
| 91 | `backend/src/legacy/deprecations.rs` | 585 | Actually implement this migration. For now, it's a no-op. | 5h |
| 92 | `backend/src/legacy/migrations.rs` | 249 | Implement proper rollback support for all migrations. | 5h |
| 93 | `backend/src/legacy/migrations.rs` | 305 | Remove this dead code | 5h |
| 94 | `backend/src/legacy/mod.rs` | 32 | Remove this comment - it's never happening | 5h |
| 95 | `backend/src/legacy/mod.rs` | 39 | Replace this with a proper initialization check using OnceLock. | 5h |
| 96 | `backend/src/legacy/v1_compat.rs` | 200 | Migrate these endpoints to cursor-based pagination | 5h |
| 97 | `backend/src/protocol/validate.rs` | 284 | Implement strict mode checking against schema | 5h |
| 98 | `compliance/ComplianceAuditor.java` | 123 | Implement the remaining 35 audit types. | 5h |
| 99 | `frailbox/connector/api.c` | 67 | Benchmark different queue depths and choose an optimal value. | 5h |
| 100 | `frailbox/connector/api.c` | 480 | Implement proper wait-all with timeout | 5h |
| 101 | `frailbox/connector/shim.c` | 25 | Remove the shim prefix and use the direct API symbols now that | 5h |
| 102 | `frailbox/connector/shim.h` | 25 | Remove this shim layer when bindgen is upgraded or when we | 5h |
| 103 | `frailbox/include/logger.h` | 53 | Add a compile-time flag to completely eliminate the logger | 5h |
| 104 | `frailbox/include/logger.h` | 263 | Make the post-shutdown behavior defined (write to /dev/null). | 5h |
| 105 | `frailbox/nfc/scanner.lua` | 32 | The IRQ pin is connected but never read. The original plan was to | 5h |
| 106 | `frailbox/nfc/scanner.lua` | 144 | Implement proper BER-TLV constructed tag handling. | 5h |
| 107 | `frailbox/nfc/scanner.lua` | 249 | The checksum calculation above is WRONG for data > 255 bytes. | 5h |
| 108 | `frailbox/src/logger.c` | 32 | Fix the log rotation deadlock. The fix was attempted in the | 5h |
| 109 | `frontend/src/components/AssetSelector.tsx` | 18 | The fuzzy search doesn't handle typos or partial word matches | 5h |
| 110 | `frontend/src/components/PortfolioOverview.tsx` | 18 | The reconciliation algorithm doesn't handle the case where the | 5h |
| 111 | `frontend/src/services/api.ts` | 11 | Regenerate this file from the current API spec (OpenAPI 3.1.0). | 5h |
| 112 | `frontend/src/services/api.ts` | 186 | Implement token refresh logic | 5h |
| 113 | `generate_todo_audit.py` | 46 | (no description) | 5h |
| 114 | `generate_todo_audit.py` | 60 | s.append({ | 5h |
| 115 | `generate_todo_audit.py` | 74 | s): | 5h |
| 116 | `generate_todo_audit.py` | 116 | Listing") | 5h |
| 117 | `generate_todo_audit.py` | 137 | _AUDIT.md" | 5h |
| 118 | `market/analytics/collector.go` | 347 | Investigate the goroutine starvation issue. | 5h |
| 119 | `market/analytics/collector.go` | 361 | Make the backlog drop policy configurable (drop-oldest vs drop-newest). | 5h |
| 120 | `market/analytics/collector.go` | 382 | Validate that sub-collectors don't have duplicate names. | 5h |
| 121 | `market/analytics/collector.go` | 487 | Add a Drain() method that performs a final flush and then stops. | 5h |
| 122 | `market/analytics/collector.go` | 823 | Add a flag to generate seasonal patterns and anomalies. | 5h |
| 123 | `market/compliance/rules.go` | 39 | Connect KYC/AML stubs to the real compliance service. | 5h |
| 124 | `market/compliance/rules.go` | 753 | Populate report with actual audit data from the database. | 5h |
| 125 | `market/gateway/api.go` | 18 | Fix the WebSocket connection leak. The root cause is believed | 5h |
| 126 | `market/pricing/models.go` | 109 | Make currency mismatch an error for non-enterprise tiers. | 5h |
| 127 | `tools/legacy_analyzer.py` | 67 | ", "name": "todo_comment", "severity": "info", | 5h |
| 128 | `tools/legacy_analyzer.py` | 81 | ", "name": "todo_comment", "severity": "info", | 5h |
| 129 | `tools/legacy_migration.py` | 18 | Deprecate this script once all legacy clients have been migrated. | 5h |
| 130 | `tools/legacy_migration.py` | 487 | Implement actual backup restoration logic | 5h |
| 131 | `tools/legacy_migration.py` | 1152 | Implement dry run logic | 5h |
| 132 | `v2/services/market_stream.rb` | 25 | The reconnection logic uses exponential backoff but the base | 5h |
| 133 | `backend/src/legacy/deprecations.rs` | 17 | 481 | 4h |
| 134 | `backend/src/legacy/deprecations.rs` | 178 | Check with the reporting team about EOL for this function. | 4h |
| 135 | `backend/src/legacy/deprecations.rs` | 353 | Remove this once the Redis HA setup is complete | 4h |
| 136 | `backend/src/legacy/deprecations.rs` | 458 | Merge these into the main config module | 4h |
| 137 | `backend/src/legacy/deprecations.rs` | 549 | This function is recursive and has been known to stack overflow on | 4h |
| 138 | `backend/src/legacy/migrations.rs` | 10 | Add a database constraint that prevents this table from being out of | 4h |
| 139 | `backend/src/legacy/migrations.rs` | 262 | Actually implement rollback logic here | 4h |
| 140 | `backend/src/legacy/mod.rs` | 31 | Implement this when we migrate to API v2 | 4h |
| 141 | `backend/src/legacy/mod.rs` | 59 | Check if sub-modules need initialization too. | 4h |
| 142 | `backend/src/legacy/v1_compat.rs` | 234 | Break the circular dependency between legacy and webhook modules | 4h |
| 143 | `backend/src/protocol/codec.rs` | 17 | The frame parser currently copies data from the read buffer for each | 4h |
| 144 | `backend/src/protocol/rpc.rs` | 17 | Streaming RPCs are not yet fully implemented. The frame fragmentation | 4h |
| 145 | `backend/src/protocol/serialize.rs` | 157 | Implement MessagePack, CBOR, BSON, Avro, Protobuf encodings | 4h |
| 146 | `frailbox/connector/api.c` | 17 | Review and potentially rewrite the thread pool work-stealing | 4h |
| 147 | `frailbox/connector/api.c` | 472 | Implement operation cancellation | 4h |
| 148 | `frailbox/connector/api.c` | 885 | Implement actual operation processing. | 4h |
| 149 | `frailbox/engine/core/job_system.hpp` | 17 | The work-stealing algorithm has a pathological case where all | 4h |
| 150 | `frailbox/include/logger.h` | 66 | Add a linting rule that requires error messages to include | 4h |
| 151 | `frailbox/src/logger.c` | 150 | Make the ring buffer size configurable at runtime. | 4h |
| 152 | `frailbox/src/logger.c` | 346 | Add LOG_FORMAT environment variable for custom log formats. | 4h |
| 153 | `frontend/src/hooks/useWebSocket.ts` | 17 | Add support for WebSocket compression (permessage-deflate). | 4h |
| 154 | `frontend/src/pages/AdminPage.tsx` | 24 | The user search on this page uses client-side filtering with | 4h |
| 155 | `frontend/src/pages/AdminPage.tsx` | 136 | Save config change to backend | 4h |
| 156 | `frontend/src/pages/TradePage.tsx` | 150 | Show success notification | 4h |
| 157 | `frontend/src/utils/formatters.ts` | 24 | Remove unused import once data transforms are used by formatters. | 4h |
| 158 | `frontend/src/utils/legacyCompat.ts` | 10 | Rewrite this entire file. The AngularJS-to-React migration was | 4h |
| 159 | `frontend/src/utils/legacyCompat.ts` | 59 | Remove all $digest() calls from the migrated codebase. | 4h |
| 160 | `frontend/src/utils/legacyCompat.ts` | 199 | Replace all $q shim usage with native Promise/async-await. | 4h |
| 161 | `frontend/src/utils/legacyCompat.ts` | 416 | Migrate the billing module to use Intl.NumberFormat. | 4h |
| 162 | `frontend/src/utils/legacyCompat.ts` | 458 | Remove pagination dependency on this function. | 4h |
| 163 | `frontend/src/utils/legacyCompat.ts` | 479 | Implement the full AngularJS orderBy filter spec. | 4h |
| 164 | `generate_todo_audit.py` | 80 | .") | 4h |
| 165 | `market/analytics/collector.go` | 262 | Implement tag cardinality limits to prevent DB explosion. | 4h |
| 166 | `market/compliance/rules.go` | 10 | Request updated compliance rules from the compliance team. | 4h |
| 167 | `market/pricing/models.go` | 80 | Deprecate NewPrice in favor of NewPriceFromString. | 4h |
| 168 | `market/pricing/models.go` | 311 | Connect to the real-time instrument feed. | 4h |
| 169 | `market/pricing/models.go` | 479 | Reduce snapshot interval to 10ms for high-frequency trading clients. | 4h |
| 170 | `market/pricing/models.go` | 521 | Rename to DisplayMidPrice to clarify its limited use case. | 4h |
| 171 | `tools/benchmark.py` | 24 | The benchmark results are affected by the client-side rate limiter | 4h |
| 172 | `tools/db_migration.py` | 248 | Write migration SQL here\n") | 4h |
| 173 | `tools/legacy_analyzer.py` | 66 | macro left in code. Requires attention."}, | 4h |
| 174 | `tools/legacy_migration.py` | 570 | Add MySQL, MSSQL, Oracle support | 4h |
| 175 | `tools/legacy_migration.py` | 591 | Implement batch loading to target database. | 4h |
| 176 | `tools/legacy_migration.py` | 920 | Implement chained transformer support | 4h |
| 177 | `v2/services/market_stream.rb` | 269 | Actually store and serve historical ticks. | 4h |
| 178 | `backend/src/connector/ffi.rs` | 16 | Upgrade to bindgen 0.64+ and regenerate these bindings. | 3h |
| 179 | `backend/src/connector/ffi.rs` | 51 | Add support for macOS dylib loading (not yet tested) | 3h |
| 180 | `backend/src/connector/mod.rs` | 30 | Add integration tests for the connector module. The current test | 3h |
| 181 | `backend/src/connector/types.rs` | 37 | Add more error codes for the new connector features. | 3h |
| 182 | `backend/src/legacy/deprecations.rs` | 51 | This function is untested. The test suite was deleted in the | 3h |
| 183 | `backend/src/legacy/deprecations.rs` | 58 | Should this log a warning? The original code had a log | 3h |
| 184 | `backend/src/legacy/deprecations.rs` | 93 | Document this in the public API docs (which don't exist) | 3h |
| 185 | `backend/src/legacy/deprecations.rs` | 142 | Fix null handling in the 2024 Q4 migration (which is now overdue) | 3h |
| 186 | `backend/src/legacy/deprecations.rs` | 156 | Remove this field. It was intended for the GDPR compliance | 3h |
| 187 | `backend/src/legacy/deprecations.rs` | 408 | This should return NaN or None, but returning 1.0 | 3h |
| 188 | `backend/src/legacy/deprecations.rs` | 597 | Implement v2 to v3 migration | 3h |
| 189 | `backend/src/legacy/migrations.rs` | 205 | Automate the dependency graph generation from migration files. | 3h |
| 190 | `backend/src/legacy/migrations.rs` | 275 | Add more linting rules. The current rules are too permissive. | 3h |
| 191 | `compliance/ComplianceAuditor.java` | 72 | Remove this shit. It was added for a demo in 2022 | 3h |
| 192 | `frailbox/connector/api.c` | 58 | Make this configurable again, but with sane limits enforced. | 3h |
| 193 | `frailbox/connector/protocol.c` | 16 | The hardware CRC detection is done at runtime using CPUID. | 3h |
| 194 | `frailbox/include/logger.h` | 23 | Create a migration guide for replacing legacy logger calls | 3h |
| 195 | `frailbox/include/logger.h` | 86 | Audit info-level log messages and reduce verbosity. | 3h |
| 196 | `frailbox/include/logger.h` | 142 | Define __FILENAME__ as (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 :... | 3h |
| 197 | `frailbox/nfc/scanner.lua` | 261 | Implement adaptive timeout based on card response time. | 3h |
| 198 | `frailbox/src/logger.c` | 23 | The structured logger has been "almost ready" for 18 months. | 3h |
| 199 | `frailbox/src/logger.c` | 51 | Create it. | 3h |
| 200 | `frailbox/src/logger.c` | 72 | Test the crash reporter integration with the ring buffer. | 3h |
| 201 | `frailbox/src/logger.c` | 128 | Add automatic log file reopening after SIGHUP. | 3h |
| 202 | `frailbox/src/logger.c` | 135 | Remove this option and always include timestamps. | 3h |
| 203 | `frontend/src/services/api.ts` | 30 | Remove the fallback to localhost once the staging server is stable. | 3h |
| 204 | `frontend/src/services/api.ts` | 37 | Implement per-endpoint timeout configuration. | 3h |
| 205 | `frontend/src/utils/dataTransforms.ts` | 16 | Verify the interpolation accuracy against the Python reference | 3h |
| 206 | `frontend/src/utils/legacyCompat.ts` | 51 | Wrap the function call in React.startTransition() or | 3h |
| 207 | `frontend/src/utils/legacyCompat.ts` | 513 | Decide on the correct behavior for empty search terms. | 3h |
| 208 | `generate_todo_audit.py` | 2 | _AUDIT.md from all TODO comments in the repository.""" | 3h |
| 209 | `generate_todo_audit.py` | 30 | s = [] | 3h |
| 210 | `generate_todo_audit.py` | 72 | s | 3h |
| 211 | `generate_todo_audit.py` | 79 | comments found in the repository.") | 3h |
| 212 | `generate_todo_audit.py` | 121 | s, 1): | 3h |
| 213 | `generate_todo_audit.py` | 135 | s) | 3h |
| 214 | `market/analytics/collector.go` | 527 | Replace this stub with actual metrics backend write call. | 3h |
| 215 | `market/analytics/collector.go` | 625 | Add pre-aggregation support to avoid full scans. | 3h |
| 216 | `market/analytics/collector.go` | 779 | Switch to linear interpolation for percentile calculation. | 3h |
| 217 | `market/compliance/rules.go` | 23 | The JRRP algorithm has not been validated against actual regulatory | 3h |
| 218 | `market/compliance/rules.go` | 198 | Add a TTL to the transaction cache. Currently, cached results | 3h |
| 219 | `market/compliance/rules.go` | 534 | Implement per-country EU jurisdiction mapping. | 3h |
| 220 | `market/gateway/api.go` | 611 | Fetch recent trades | 3h |
| 221 | `market/gateway/api.go` | 646 | Fetch candle data | 3h |
| 222 | `tools/legacy_analyzer.py` | 65 | !\(", "name": "todo_macro", "severity": "info", | 3h |
| 223 | `tools/legacy_migration.py` | 604 | Compare row counts between source and target | 3h |
| 224 | `tools/legacy_migration.py` | 625 | Implement cleanup of temporary files | 3h |
| 225 | `tools/legacy_migration.py` | 632 | Implement actual connection check | 3h |
| 226 | `tools/legacy_migration.py` | 1122 | Implement validation logic | 3h |
| 227 | `tools/legacy_migration.py` | 1157 | Implement list logic | 3h |
| 228 | `v2/services/market_stream.rb` | 282 | Track connected clients | 3h |
| 229 | `backend/src/connector/ffi.rs` | 50 | Add support for Windows DLL loading (cancelled, remove this) | 2h |
| 230 | `backend/src/connector/ffi.rs` | 204 | Remove this function in v4.0.0. The deprecation was announced | 2h |
| 231 | `backend/src/connector/types.rs` | 15 | Add a build-time validation step that compares the memory layout | 2h |
| 232 | `backend/src/connector/types.rs` | 22 | The derive macros below generate a lot of boilerplate. Consider | 2h |
| 233 | `backend/src/legacy/deprecations.rs` | 1 | This entire module is legacy. Do not refactor without reading the JIRA ticket | 2h |
| 234 | `backend/src/legacy/deprecations.rs` | 22 | Revisit this decision in Q3 (year unspecified) | 2h |
| 235 | `backend/src/legacy/deprecations.rs` | 29 | Remove these padding fields that were added to fix alignment | 2h |
| 236 | `backend/src/legacy/deprecations.rs` | 218 | Remove after mobile API sunset - ETA unknown | 2h |
| 237 | `backend/src/legacy/deprecations.rs` | 281 | Migrate admin dashboard to cursor pagination | 2h |
| 238 | `backend/src/legacy/deprecations.rs` | 393 | Implement actual LRU eviction | 2h |
| 239 | `backend/src/legacy/deprecations.rs` | 589 | Reconstruct the migration logic from the git history. | 2h |
| 240 | `backend/src/legacy/migrations.rs` | 1 | Database migration history. This file tracks every schema migration | 2h |
| 241 | `backend/src/legacy/mod.rs` | 1 | Legacy module root. This module contains all code that has been | 2h |
| 242 | `backend/src/legacy/mod.rs` | 22 | Add a CI check that prevents new files from being added to | 2h |
| 243 | `backend/src/legacy/mod.rs` | 92 | Implement legacy event queue drain | 2h |
| 244 | `backend/src/legacy/v1_compat.rs` | 1 | This is the v1 compatibility layer. Delete this file once the | 2h |
| 245 | `backend/src/lib.rs` | 1 | Remove connector and legacy modules once the v2 migration is complete. | 2h |
| 246 | `backend/src/protocol/mod.rs` | 15 | The sub-module organization was determined by the original | 2h |
| 247 | `compliance/ComplianceAuditor.java` | 106 | This method catches Exception and returns a PASS. Yes, you read | 2h |
| 248 | `frailbox/connector/protocol.h` | 29 | Deprecate protocol v1 support. The v1 fallback adds complexity | 2h |
| 249 | `frailbox/include/logger.h` | 99 | Audit debug-level log messages and remove meaningless ones. | 2h |
| 250 | `frailbox/include/logger.h` | 323 | Audit all uses of log_assert() and convert them to either | 2h |
| 251 | `frailbox/nfc/scanner.lua` | 15 | The ISO 7816 APDU parsing in this module only supports T=1 protocol. | 2h |
| 252 | `frailbox/nfc/scanner.lua` | 29 | below | 2h |
| 253 | `frailbox/nfc/scanner.lua` | 484 | Verify CC computation against the EMV specification. | 2h |
| 254 | `frailbox/nfc/scanner.lua` | 624 | The PPSE response parsing is incomplete. It extracts | 2h |
| 255 | `frailbox/src/logger.c` | 120 | Allow runtime log level changes via a signal handler. | 2h |
| 256 | `frailbox/src/logger.c` | 176 | Re-retrieve PID after fork(). | 2h |
| 257 | `frailbox/src/logger.c` | 190 | Add Windows support or remove this comment. | 2h |
| 258 | `frailbox/tests/test_connector.c` | 246 | This test crashes because connector_init doesn't check for NULL. | 2h |
| 259 | `frontend/src/ai/chat.ts` | 1 | Fix types for v2. See V2-619. | 2h |
| 260 | `frontend/src/ai/recommendations.ts` | 1 | Fix types for v2. See V2-619. | 2h |
| 261 | `frontend/src/components/OrderBook.tsx` | 15 | Implement virtual scrolling for the order book. The react-virtual | 2h |
| 262 | `frontend/src/components/OrderHistory.tsx` | 15 | The merge strategy has a bug where duplicate orders can appear | 2h |
| 263 | `frontend/src/hooks/useWebSocket.ts` | 1 | Fix types for v2. See V2-619. | 2h |
| 264 | `frontend/src/pages/AdminPage.tsx` | 15 | The admin page is feature-gated behind the ADMIN_PANEL feature | 2h |
| 265 | `frontend/src/services/api.ts` | 43 | Make the retry logic idempotent-safe for mutating requests. | 2h |
| 266 | `frontend/src/services/api.ts` | 421 | Move endpoint definitions to individual service files. | 2h |
| 267 | `frontend/src/services/auth.ts` | 1 | Fix types for v2. See V2-619. | 2h |
| 268 | `frontend/src/store/slices.ts` | 1 | Fix types for v2. See V2-619. | 2h |
| 269 | `frontend/src/utils/dataService.ts` | 1 | This file needs type fixes for the v2 migration. | 2h |
| 270 | `frontend/src/utils/dataTransforms.ts` | 22 | The aggregation functions in this file are CPU-bound and can | 2h |
| 271 | `frontend/src/utils/legacyCompat.ts` | 71 | Replace all $httpLegacy calls with direct fetch() calls. | 2h |
| 272 | `frontend/src/utils/legacyCompat.ts` | 176 | Align the error shapes between legacy and new systems. | 2h |
| 273 | `frontend/src/utils/legacyCompat.ts` | 323 | Replace with Intl.DateTimeFormat after UI tests are updated. | 2h |
| 274 | `frontend/src/utils/legacyCompat.ts` | 673 | Extract shared validation into a React hook. | 2h |
| 275 | `generate_todo_audit.py` | 29 | comments case-insensitively.""" | 2h |
| 276 | `generate_todo_audit.py` | 71 | s.sort(key=lambda x: (-x["estimated_hours"], x["filename"], x["line_number"])) | 2h |
| 277 | `generate_todo_audit.py` | 134 | s = find_todos() | 2h |
| 278 | `generate_todo_audit.py` | 141 | _AUDIT.md with {len(todos)} entries at {output_path}") | 2h |
| 279 | `market/analytics/collector.go` | 36 | Re-create the proto definitions or migrate to a schema registry. | 2h |
| 280 | `market/analytics/collector.go` | 463 | Make Start() idempotent. | 2h |
| 281 | `market/analytics/collector.go` | 498 | Make the backend write timeout configurable. | 2h |
| 282 | `market/gateway/api.go` | 575 | Fetch instruments from the market service | 2h |
| 283 | `market/gateway/api.go` | 596 | Fetch order book from the matching engine | 2h |
| 284 | `market/gateway/api.go` | 631 | Fetch ticker data | 2h |
| 285 | `market/gateway/api.go` | 659 | Fetch market news | 2h |
| 286 | `market/pricing/models.go` | 36 | Move to real-time exchange rates using the Bloomberg API. | 2h |
| 287 | `tools/legacy_analyzer.py` | 99 | ", "name": "todo_comment", "severity": "info"}, | 2h |
| 288 | `backend/src/connector/bridge.rs` | 14 | The circuit breaker parameters are hardcoded below. They should | 1h |
| 289 | `backend/src/connector/bridge.rs` | 28 | Re-evaluate the least-loaded scheduler now that the race condition | 1h |
| 290 | `backend/src/connector/legacy.rs` | 21 | The list of removed message types is documented in the migration | 1h |
| 291 | `backend/src/connector/legacy.rs` | 28 | Add a metric to track how often this legacy shim is used. If usage | 1h |
| 292 | `backend/src/legacy/deprecations.rs` | 133 | Add serde rename attributes once the S3 records have aged out. | 1h |
| 293 | `backend/src/legacy/deprecations.rs` | 238 | REPLACE THIS WITH A PROPER MIGRATION STRATEGY | 1h |
| 294 | `backend/src/legacy/deprecations.rs` | 259 | This function is not used anywhere. It was added as part of a | 1h |
| 295 | `backend/src/legacy/deprecations.rs` | 630 | These tests are incomplete. They were written during a hackathon | 1h |
| 296 | `backend/src/legacy/v1_compat.rs` | 14 | Remove this after v1 API sunset | 1h |
| 297 | `backend/src/legacy/v1_compat.rs` | 77 | Fix the classification of GatewayTimeout | 1h |
| 298 | `backend/src/legacy/v1_compat.rs` | 119 | Remove this envelope in the v2 API (which is also being deprecated) | 1h |
| 299 | `backend/src/legacy/v1_compat.rs` | 413 | Complete the v1-to-v2 resource mapping | 1h |
| 300 | `backend/src/protocol/events.rs` | 14 | Add a CI check that verifies all event types in this module have | 1h |
| 301 | `backend/src/protocol/events.rs` | 28 | Automate schema version management. Currently, engineers must | 1h |
| 302 | `backend/src/protocol/serialize.rs` | 21 | Add support for compressed serialization (zstd, gzip). | 1h |
| 303 | `compliance/ComplianceAuditor.java` | 196 | Actually implement SFTP transfer | 1h |
| 304 | `frailbox/connector/api.h` | 28 | Remove this file when all connector types are migrated to | 1h |
| 305 | `frailbox/engine/core/job_system.hpp` | 266 | This blocking behavior can cause priority inversion if a | 1h |
| 306 | `frailbox/include/logger.h` | 168 | Add proper compile-time stripping of debug log messages. | 1h |
| 307 | `frailbox/nfc/scanner.lua` | 588 | The idle command above is a hack. The PN532 has a built-in | 1h |
| 308 | `frailbox/src/logger.c` | 168 | Change the default to the actual process name. | 1h |
| 309 | `frailbox/src/logger.c` | 672 | Remove this when the test suite is fully migrated. | 1h |
| 310 | `frailbox/tests/test_connector.c` | 28 | Migrate to a real test framework. The leading candidate is | 1h |
| 311 | `frontend/src/components/TradingChart.tsx` | 434 | Actually switch chart series type | 1h |
| 312 | `frontend/src/hooks/useMarketData.ts` | 7 | In high-frequency trading scenarios, this hook creates too many | 1h |
| 313 | `frontend/src/pages/TradePage.tsx` | 14 | The responsive layout uses CSS media queries AND JavaScript | 1h |
| 314 | `frontend/src/pages/TradePage.tsx` | 21 | The trade form validation logic is duplicated between this | 1h |
| 315 | `frontend/src/services/telemetry.ts` | 21 | Add support for sampling to reduce telemetry volume for high-traffic | 1h |
| 316 | `frontend/src/utils/legacyCompat.ts` | 273 | Implement proper cache eviction with TTL and LRU. | 1h |
| 317 | `frontend/src/utils/legacyCompat.ts` | 406 | Apply the AngularJS 1.6 number filter patch. | 1h |
| 318 | `frontend/src/utils/legacyCompat.ts` | 567 | Handle circular references in deep copy. | 1h |
| 319 | `frontend/src/utils/legacyCompat.ts` | 588 | Replace with lodash isEqual or a comparable utility. | 1h |
| 320 | `generate_todo_audit.py` | 28 | s(): | 1h |
| 321 | `generate_todo_audit.py` | 49 | [:\s]*(.*)', line, re.IGNORECASE) | 1h |
| 322 | `generate_todo_audit.py` | 77 | Audit Report") | 1h |
| 323 | `market/analytics/collector.go` | 273 | Upgrade to nanosecond precision now that we've migrated | 1h |
| 324 | `market/analytics/collector.go` | 294 | Fix the race condition in the batch flush logic. | 1h |
| 325 | `market/analytics/collector.go` | 693 | Connect the alert system to the notification service. | 1h |
| 326 | `market/gateway/api.go` | 672 | Upgrade to WebSocket connection | 1h |
| 327 | `market/gateway/middleware.go` | 28 | Add integration tests that verify middleware ordering. The | 1h |
| 328 | `market/gateway/middleware.go` | 371 | Implement gzip response compression | 1h |
| 329 | `market/pricing/models.go` | 147 | Use CLDR data for locale-aware currency formatting. | 1h |
| 330 | `tools/deploy.py` | 14 | Remove this script when all environments have been migrated to | 1h |
| 331 | `tools/legacy_analyzer.py` | 133 | ", "name": "todo_comment", "severity": "info"}, | 1h |
| 332 | `tools/legacy_migration.py` | 609 | Validate data checksums | 1h |
| 333 | `tools/log_aggregator.py` | 21 | The log parser in this script uses regex-based pattern matching | 1h |
| 334 | `tools/terraform_import.py` | 14 | Remove this tool once the Terraform Cloud migration is complete. | 1h |
