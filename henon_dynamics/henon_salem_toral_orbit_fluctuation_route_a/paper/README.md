# Manuscript

main.tex defaults to round2. The three driver files select the substantive revisions described in PAPER_IMPROVEMENT_LOG.md. main.pdf must equal main_round2.pdf byte-for-byte. All final proofs are in the actual manuscript. Deterministic builds use LuaLaTeX twice in each of two fresh directories, with raw settled logs retained. Release additionally checks font embedding, Chinese abstracts, six keywords per language, extracted text and page rasterization. Actual human-interface page opening is recorded separately; raster existence alone is not called visual review.
