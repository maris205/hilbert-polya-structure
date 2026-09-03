# Round 10 Stage 4′ correction-execution authority — attempt 1 incident

- Workflow date: `2026-09-04 UTC`
- Attempt time: `2026-09-03T21:40:49Z`
- Scope: authorization-record and input-freeze construction only.
- Result: fail-closed before any authorization record, receipt, freeze, manuscript, bibliography, result, Route, or initial-system write.

The builder compared `File.binread` (`ASCII-8BIT`) directly with a UTF-8 Ruby
literal. The byte sequences were identical, and the author-event SHA-256 was
`111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812`, but Ruby's
encoding-aware equality returned false. The comparison was corrected to use an
explicit binary literal. No authority input, user instruction, or scientific
content was altered.
