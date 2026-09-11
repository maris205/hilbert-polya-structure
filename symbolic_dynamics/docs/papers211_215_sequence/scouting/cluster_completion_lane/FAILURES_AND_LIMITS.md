# Preserved failures and exact read limits

- `BROWSER_PRIMARY_OPEN.json` is the actual initial tool return. It contains
  an arXiv HTML HTTP 406 failure and a successful cached/extracted initial
  Kent PDF view through displayed line 192. It is a tool response, not local
  original PDF bytes or a claim of whole-paper reading.
- `BROWSER_PRIMARY_FIND_FAILURE.json` is the actual tool return for two
  failed equation searches; its internal-error/no-match messages do not
  establish that the equations are absent from the source.
- Subsequent browser opening at line 300 and by the earlier cached reference
  at line 470 both returned timeout-fetch errors. The latter exact response
  is retained as `BROWSER_PRIMARY_BODY_FAILURE.json`; the former is described
  here from the actual tool return, not represented as a separately preserved
  raw-native receipt.
- Native PDF acquisition failed with **HTTP 401**, curl return code 22,
  and `size_download=0`; headers and both raw streams are retained. The
  extraction step was explicitly skipped. An intermediate commentary said
  HTTP 502 before the header was read; that statement was incorrect and
  was corrected immediately after inspecting the native receipt.
- A preflight `rg --files` against the then nonexistent lane directory
  exited 2; after the failed acquisition, `rg` and `sed` against nonexistent
  `raw/08_primary_text.stdout` also exited 2. Those diagnostic tool returns
  were observed, but their raw terminal streams were not separately saved
  to the package. No missing extraction file is treated as a read source.
- The nine commands in `NATIVE_RECEIPT.json` are the collector's commands,
  not a claim to account for every surrounding diagnostic/browser call.
  There were zero scientific runs and zero attempted scientific runs.
- Old implementation, canonical outputs and selected original prose were
  read narrowly. Byte pinning is not full semantic reading. Source metadata
  and introductory context do not prove the source's unaccessed equations.
- All deductions and artifact checks in this packet are by the author
  scout; no self-authored acceptance or independent-review claim is made.
