# Intake-side failures and limitations

All changes described here affect only this new independent intake directory.
No scout packet, source record, input pin or historical mapping was edited.

1. An exploratory read guessed the nonexistent path
   `docs/papers211_215_sequence/scouting/ARTIFACT_CONTRACT.md`. The actual
   command was `sed -n '1,240p'` on that exact path with output budget 12000.
   Native chunk `79dfb7`, exit 2, wall time 0.05179785 seconds,
   original_token_count 26, output exactly:

   ```text
   sed: can't read docs/papers211_215_sequence/scouting/ARTIFACT_CONTRACT.md: No such file or directory
   ```

   This guessed read supplied no contract evidence. The required skill,
   workflow and real batch contract had already been fully read in the
   preceding work segment; the workflow was then located by its real path.

2. Exploratory combined displays `a45837` and `15eb1c` were too large for
   their displayed budgets. `78d427` also mistakenly enumerated string
   indexes with Object.keys on a child web return and was tool-truncated.
   Those displays are navigation only, not complete artifact checks or
   source reading. They were not archived here as invented complete returns.
   The actual frozen raw JSON bytes were subsequently fully read by the
   checker; its complete native data report replaces neither old returns
   nor source-access failures. Whole-file hashes and every record's exact
   complete returned-string/native-output digest are in CHECK_NATIVE.json.

3. CHECK01_FAILED.cjs and CHECK01_FAILED_NATIVE.json preserve the first
   independent checker source and its genuine exit-1 native result. The
   checker transcribed the fresh12 seal with one `b` where the previously
   observed original seal has `d`, at the substring `f966b033` versus
   `f966d033`. The exact original seal assertion was restored only in the
   new checker. This was an intake transcription defect, not an author
   package failure; no original manifest was changed.

4. The corrected second run exited 0 internally but its pretty-printed
   72,245-token report exceeded the 60,000-token return budget.
   CHECK02_TRUNCATED_NATIVE.json preserves that actual incomplete return.
   It is not a complete passing evidence record. The current checker emits
   compact JSON and the next actual run requested 100,000 output tokens;
   CHECK_NATIVE.json contains the complete parseable output, not a
   reconstructed report. The closing run additionally compares exact raw
   original pin stdout bytes, without trim/normalization. This strengthens
   the check without changing any archive data or historical assertion.

The task-message per-scout attribution was corrected with root before the
check, as described in PLAN.md. Two task-message hash literals had one extra
trailing character; the exact 64-character original pins and original
MAPPING entries, rather than those mistyped messages, bind the adapters.
These corrections do not authorize a central count change by this agent.
