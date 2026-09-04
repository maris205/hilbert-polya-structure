# Reproducibility

Requirements are Python 3, PyYAML, SymPy, LuaLaTeX with TeX Gyre fonts, Poppler (`pdfinfo`, `pdffonts`, `pdftotext`, `pdftoppm`), and standard Unix utilities. No network, training data, random seed, or floating-point tolerance is used by the canonical producer/checker.

Run the commands in `README.md` from this package directory. The producer serializes sorted UTF-8 JSON with exact rational numerator/denominator pairs. The checker imports no producer code and reconstructs all formulas. Replay regenerates evidence in an isolated directory and requires byte equality. Mutation repairs section and payload hashes before asking the checker to reject semantic corruption.

The release script compiles each of rounds 0, 1, and 2 twice in fresh temporary directories with `SOURCE_DATE_EPOCH=1788480000`, requires byte equality, scans settled logs, checks font embedding and extractable text, rasterizes every page, runs every computational lane, closes the payload ledger, and writes a self-excluded manifest.
