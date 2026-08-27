# C203 compile report

LuaLaTeX 1.14.0 was run with `SOURCE_DATE_EPOCH=1787788800` and
`FORCE_SOURCE_DATE=1`.  Rounds 0/1/2 contain 2/3/3 pages and have distinct
SHA-256 values:

```text
a4a6a5c213cf2e9f99f74438432ccb845be5dbb09fea47e4d18f20cd8aa7d598
b1d751811e4126e17077d1b8cbd2c4befe9a42aa170387c24361bcd803aeedb3
395643b221b94c5af0345243e93ad18b30d69872acadd81d3830371be4ab9689
```

`main.pdf` is 161,320 bytes, has three A4 pages, and is byte-identical to
round 2.  Two additional builds from distinct fresh temporary directories
reproduced the final SHA byte for byte.  Every font is embedded; extracted text
contains the bilingual abstract, pseudoforest formulas, scope literal and AI
disclosure.  Both fresh logs are free of warnings, bad boxes, undefined
references and missing characters.  All three final pages were inspected at
120 dpi; matrices, long formulas, Chinese glyphs, margins and breaks are intact.
