# C199 compile report

LuaLaTeX 1.14.0 was run with `SOURCE_DATE_EPOCH=1787788800` and
`FORCE_SOURCE_DATE=1`.  Rounds 0/1/2 contain 2/3/3 pages and have distinct
SHA-256 values:

```text
3bc9b83fc659a465483cc412e77bff57399ce038540ec1bed0c134a3e1b77e56
94fb7f535d690df53551bf0a35d52e62d54953f0935cb6a4de9641ef95ee2f28
4c17171ef2e6b48aeb2dacac7cc37c422cb92bac07d645698e8d28c63198575b
```

`main.pdf` is 168,785 bytes, has three A4 pages, and is byte-identical to
round 2.  Two additional builds from distinct fresh temporary directories
reproduced the final SHA byte for byte.  `pdffonts` reports every font embedded;
`pdftotext` extracts the bilingual abstract, theorem, scope literal and AI-use
disclosure.  Both fresh logs contain no warning, bad-box, undefined-reference
or missing-character sentinel.  All three rendered final pages were inspected
at 120 dpi: equations, Chinese glyphs, margins and page breaks are intact.
