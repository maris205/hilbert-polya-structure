# Compilation report

All three revision artifacts were built in two independent temporary trees,
with two LuaLaTeX passes per tree, `TZ=UTC`, and
`SOURCE_DATE_EPOCH=1788048000`.  The two trees produced identical bytes for
each revision; build sidecars remained outside this package.  The release PDF
is byte-identical to `main_round2.pdf`.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `6e3f1423d454fb157c214b59028f2d72eb6573bdbd23c972e2e35872aca35c8b` | 3 |
| `main_round1.pdf` | `663226cd6c71cf435be9a9d91bd1904515f2c408691e4c5d07242a35554a5af2` | 3 |
| `main_round2.pdf` | `cbb4fd060c5ec8b25a1567b5afa83b339759926a0f8180a04525763a4d71f8e2` | 3 |
| `main.pdf` | `cbb4fd060c5ec8b25a1567b5afa83b339759926a0f8180a04525763a4d71f8e2` | 3 |

The settled second pass has no undefined references, overfull boxes, or fatal
warnings.  Fonts are embedded/subset and extracted text is checked for the
square recurrence, (2a/\rho), Markov-renewal/Palm, and Route-A boundary.  No
LaTeX sidecars are included in the release.
