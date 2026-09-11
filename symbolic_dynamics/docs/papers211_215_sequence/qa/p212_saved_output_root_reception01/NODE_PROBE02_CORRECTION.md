# Root builtin-probe value-kind correction

The second actual builtin-only probe parsed successfully but failed while
fingerprinting Node's exposed native-source registry: 448939/session 29360,
completion d60fcb/exit 1. No semantic receiver was loaded. Source
node_preload02.js and its full actual failure remain unchanged.

A separate actual read-only kind census (c54d3c/exit 0) found exactly 359
string entries and one `configs` entry whose value is undefined. Forward
node_preload03.js keeps every entry and explicitly records its type. Only
`configs` may have type undefined; no missing source is silently omitted or
claimed to be source text. The binary itself remains separately pinned.
The exact same whole typed registry must match before/after a later run.
