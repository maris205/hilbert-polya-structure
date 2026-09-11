# P197 Round1 freeze

2026-09-05 UTC. Review A was completed by batch197_lzk_gate, a process
distinct from the author. Root read its full review, proof reconstruction,
source/owner audit, build/visual record, replay receipt and no-change delta.
All18root-relative input pins and the10-entry nonself review manifest pass.
Root freshly ran its verifier twice: the first full stdout was inspected,
and the second was piped under pipefail to cmp against CANONICAL.txt,
returning zero. Each run contains4,814,623assertions. Canonical SHA256:
56cf9e85128085117465b1c365f70a223ced365d37b5f2726364832fa748970b.

Decision: ACCEPTED_NO_CHANGE. Critical0, Major0, Minor0 open in Review A.
The Review A source-only cold build independently reproduced the original
PDF. Round1 is an exact copy, not a claim of a new revision or another
cold-build experiment. Frozen source/code bytes are in frozen_round1/.

| Input | SHA256 |
|---|---|
| main.tex | 3958fd63a7a7487bceb9720fb140426651d27fb51bab79dc03a30286eb4deda0 |
| references.bib | 56fff92afda7b377cab2a340e5b41cb245c147e965d6e691102a2e25ae15937b |
| code/verify.py | 2dde93e3e8c8b4c85f23ceb476d1cddd63a8f477c5c11d2cb59ee4f6e16b1e27 |
| code/CANONICAL.txt | 54d09ba740900f49fdd045c9aae3b3fbe4f0cf2bc6cbbee3fe92f7f98a77d5d1 |
| main_round1.pdf | 42cb9e1e7cd10858a7ecf98faf2d8ced79faeb31211f608fd20f4b75a01b792a |

Review B, terminal two-cold-build QA, root all-final-page viewing and final
package manifests remain required. OWNER_AMBER / HOLD_EXTERNAL.
