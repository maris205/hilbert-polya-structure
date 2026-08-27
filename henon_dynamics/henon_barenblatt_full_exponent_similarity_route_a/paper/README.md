# Paper artifacts

- `main_round0_original.pdf`: profile classification and normalization core;
- `main_round1.pdf`: adds moments, sharp boundaries, pressure, rescaling, and
  conditional dissipation;
- `main_round2.pdf`: adds executable closure, Route-A evaluation, sources,
  disclosures, and claim firewall;
- `main.pdf`: byte-identical copy of round 2;
- `main.tex`: conditional source for all three revisions.

All PDFs are built by LuaLaTeX with
`SOURCE_DATE_EPOCH=1787788800`.  The final release requires two independent
fresh-directory builds with the same SHA-256, embedded subset fonts,
extractable text, a clean log, and visual inspection of every page.
