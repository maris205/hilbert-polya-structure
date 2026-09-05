# Reproduction

Run from this package directory using the versions in requirements.txt.
LuaLaTeX, Poppler pdfinfo/pdffonts/pdftotext/pdftoppm, TeX Gyre Pagella,
TeX Gyre Pagella Math and Droid Sans Fallback are required for the PDFs.

```sh
python -B code/c390_lyness_producer.py
python -B code/c390_lyness_checker.py
python -B code/c390_lyness_sympy_crosscheck.py
python -B code/c390_lyness_replay.py
python -B code/c390_lyness_mutation.py
python -B -m unittest discover -s tests
python -B code/c390_release_manifest.py --build-pdfs
python -B code/c390_release_manifest.py --write
python -B code/c390_release_manifest.py
```

Producer and checker share no implementation import. The checker performs
exact scalar-recurrence and dual-derivative reconstruction. Symbolic and
quadrature checks are separate controls. The replay compares two fresh
directory runs with committed evidence bytes.

The release validates strict YAML raw and semantic/type hashes in both
write and nonwrite modes, rejects symlink/control-byte payloads, runs all
lanes and optimized-mode refusal, double-builds each substantive PDF in
fresh directories, and audits fonts, text and raster output. The three
settled raw TeX logs are retained as paper/compile_round[012].txt.
The manifest excludes itself and records exact physical membership,
hashes, evidence, three PDFs and reproducible lane receipts. Full-page
human-style image inspection is recorded separately, not inferred from
successful rasterization.
