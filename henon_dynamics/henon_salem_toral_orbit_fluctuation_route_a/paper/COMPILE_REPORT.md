# Compilation protocol and receipt location

The release runner compiles all three revisions in two fresh directories apiece, each with two settled LuaLaTeX passes. Fixed epoch1788566400. The generated compile_round0/1/2.txt retain raw settled logs; release refuses warning, overfull, underfull, missing-character and undefined-reference patterns. main.pdf is the round2 byte-identical copy. Font/text/raster and double-build receipts are stored in the reconstructed manifest. Actual final-page inspection is required before release; see review/FINAL_INTEGRITY.md.
