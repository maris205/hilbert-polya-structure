# Build protocol — P134

From this directory, run the required four stages:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Round-zero QA additionally requires:

1. a fresh raw-stdout byte comparison of `code/verify.py` with
   `code/verification_output.txt`;
2. a settled-log audit for errors, undefined citations/references, bad boxes,
   and rerun requests;
3. page count, A4 media box, extractable text, anonymous metadata, and fully
   embedded/subsetted fonts;
4. rasterization and visual inspection of every page;
5. preservation of the compiled PDF as `main_round0_original.pdf`.

Mechanical build success does not alter `HOLD_EXTERNAL`.  Final round-zero
counts and hashes are recorded after compilation below.

## Round-zero result

Completed on 2026-08-31 UTC.

- The fresh paper-local verifier executed 1,694,506 exact assertions and its
  raw stdout matched `code/verification_output.txt` byte for byte (`cmp=0`).
- The required `pdflatex`--`bibtex`--`pdflatex`--`pdflatex` sequence exited
  successfully.  The same four stages in an isolated temporary directory
  containing only `main.tex` and `references.bib` produced a byte-identical
  PDF.
- `main.pdf` and `main_round0_original.pdf` are byte-identical, 5-page A4
  files of 322,388 bytes.  Both have SHA-256
  `958d05206b1b5a50456bddf9533d65c757b407a54728d79f3308da5f5e74c829`.
- The settled log has no errors, undefined citations/references, bad boxes,
  or rerun requests.  All 24 reported font rows are embedded, subsetted, and
  Unicode-capable; document title, author, subject, and keyword metadata are
  blank.
- Extracted text and rasterized inspection of all five pages found no missing
  glyphs, clipping, overlap, malformed display, or unintended blank page.

The round-zero artifact remains anonymous and `HOLD_EXTERNAL`.

## Round-one result

Completed on 2026-08-31 UTC after implementing both Review-A exposition
repairs.

- The fresh paper-local verifier executed 1,694,506 exact assertions and its
  raw stdout again matched `code/verification_output.txt` byte for byte
  (`cmp=0`).
- The four required build stages, repeated in the isolated directory
  `/tmp/p134r1iso.vgNPT7`, produced a byte-identical PDF and a clean settled
  log.
- `main.tex` has SHA-256
  `f14a1e2a10f51acf800fb922b073a0a8b227f1b9f5b2196535b5ba380f0ac4a3`.
- `main.pdf` and `main_round1.pdf` are byte-identical five-page A4 files of
  323,084 bytes with SHA-256
  `d1c1ed8fe7667bb192c6c00e59259e1a80403c5a18e52735be99e907c7662525`.
- All 24 reported font rows are embedded, subsetted, and Unicode-capable;
  identifying metadata is blank.  The repaired mismatch argument and the
  `n=2` empty-product boundary were visually inspected and are clean.
- `main_round0_original.pdf` remains unchanged with SHA-256
  `958d05206b1b5a50456bddf9533d65c757b407a54728d79f3308da5f5e74c829`.

The round-one artifact remains anonymous and `HOLD_EXTERNAL`.

## Round-two result

Completed on 2026-09-01 UTC after implementing both Review-B documentary
repairs.

- The unchanged 1,694,506-assertion verifier again matched its canonical
  stdout byte for byte (`cmp=0`).
- The current source has SHA-256
  `4fac43a74db22838e1595975c73972360cc3aa54e79530feaa3a22e5bc3153b6`.
- The repository build and the isolated four-stage build in
  `/tmp/p134r2iso.9edN6H` produced byte-identical PDFs.  The settled logs have
  no error, warning, undefined citation/reference, bad box, or rerun request.
- `main.pdf` and `main_round2.pdf` are byte-identical five-page A4 files of
  323,103 bytes with SHA-256
  `7d69a1e9338e9421ef31ac3e265a35317e0d11c836f1a652a76a69c36b923962`.
- All 24 reported font rows remain embedded, subsetted, and Unicode-capable;
  the PDF is unencrypted, form-free, JavaScript-free, and anonymous.
- `main_round1.pdf` remains unchanged at SHA-256
  `d1c1ed8fe7667bb192c6c00e59259e1a80403c5a18e52735be99e907c7662525`,
  and the immutable Round-0 PDF remains unchanged.

The distinct Round-2 bytes arise solely from the corrected in-proof paragraph
pointer.  External status remains `HOLD_EXTERNAL`.
