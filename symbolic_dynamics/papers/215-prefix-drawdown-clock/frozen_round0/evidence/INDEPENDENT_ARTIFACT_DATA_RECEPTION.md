# P215 current02 independent artifact DATA accepted

2026-09-11 UTC. Root consumed the single V2 grant through the exclusive
wrapper. The checker exited zero, captured 69505 stdout bytes at SHA256
73731e38a7954a2b3b0a198bdfd3b5f7e3475bf16028075dfd065fa263c185d4,
and emitted zero stderr bytes.

The complete independent report returns ACCEPT_INITIAL_ARTIFACT_DATA with
1767 checks and zero findings. It receives exactly 160 artifact files /
3319238 bytes, 13 directories, 227 selected resources, eight sources, eight
snapshots, six pages, 16 embedded Type1 font rows and 19 raw bridge pairs.
Its complete pass1/pass2/pass3 FLS classifications contain respectively
241/248/248 events; all selected-runtime inputs are in the prospective
227-row manifest and all source/generated roles close.

The preserved V1 path error and run01 four-TFM HOLD remain failures, not DATA.
After V2, a root summary command incorrectly used Node require on the raw JSON
and failed before parsing; a corrected JSON.parse read of the unchanged
69505-byte report returned the accepted summary above. Neither command reran
the checker or changed any artifact.

Together with root's separate 216-check artifact receiver and exact current02
page-identity reception, this closes initial artifact DATA. It does not by
itself adopt the PDF, edit lifecycle prose, freeze Round0 or start Review A.
OWNER_AMBER / HOLD_EXTERNAL.
