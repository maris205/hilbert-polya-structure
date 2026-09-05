# P199 Round1 freeze

2026-09-05UTC. Review A by batch197_lzk_gate accepted no change. Root read
the complete report, proof reconstruction, source/owner audit, build/visual
record, replay receipt and delta. All16root-relative input pins and the
topmanifest were verified; all14QAentries also passed from their proper
qa/working directory. An earlier QAcheck used the parent directory and
reported missing relative paths only; no bytes changed to repair it.

Root freshly ran verify_word_orbits.py under pipefail and cmp against
CANONICAL.txt: exit0,1926465assertions, SHA256
b302b308a27c506b0a5d030a8f59612cc6a9afe2f57f9b5938172b64a3e30851.
An initial command used the nonexistent generic filename and failed before
running any code; the corrected command above is the successful replay.

Round1 copies the unchanged accepted Round0 bytes. The reviewer had already
reproduced the exact four-page PDF from sources and viewed all pages; this
copy is not another build or an invented textual revision.

| Item | SHA256 |
|---|---|
| main.tex | 33e5e27fe6c9cedef8490bc33628ce06dcef0416784ed4e2671c341cdbc80beb |
| references.bib | bea6c3a80631bd0a2450813d8b981214c852e0681cb4a33cdb7d2730a4b2bb28 |
| code/verify.py | d5eb32ce04fa9aef9acedda5a5f0bef5bcab4d3beb28e74cbb8a90ea265c0bb3 |
| code/CANONICAL.txt | 0b9a1f131984c427db95d8443470a280129b4863b4f92e817e484f99fc13c0ff |
| main_round1.pdf | b6ba18a10e83281c1dd491b47cf5d8513ab9914933c659411c8d5c24b72478a0 |

Frozen source/code are in frozen_round1/. Open AfindingsC0/M0/m0. Distinct
Review B, terminal cold builds and root all-final-page QA remain required.
OWNER_AMBER / HOLD_EXTERNAL; no batch completion implied.
