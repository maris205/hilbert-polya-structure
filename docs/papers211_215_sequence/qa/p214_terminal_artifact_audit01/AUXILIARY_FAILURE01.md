# Unavailable jq helper

2026-09-11 UTC. A final-QA convenience command attempted to print the two
already existing `FINDINGS_FINAL.json` files with `jq`. The host returned
`jq: command not found` twice. The same command's two strict final-input pin
checks passed, but the command as a whole is not credited. A subsequent Node
JSON.parse read both complete JSON bodies and confirmed empty current findings
and 0/0/0 censuses. No build, artifact or source changed.

