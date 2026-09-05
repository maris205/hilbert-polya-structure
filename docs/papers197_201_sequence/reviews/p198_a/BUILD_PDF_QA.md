# P198 rejected-review build record

The cold_build/ directory was populated with only frozen main.tex and
references.bib, then pdflatex-recorder, BibTeX and two further pdflatex
passes were run under SOURCE_DATE_EPOCH1704067200, FORCE_SOURCE_DATE1,
TZUTC and LC_ALLC. All returned zero and cmp reproduced the exact frozen
PDF575d7382ed14715591a86e4f42599b3b5d131f859e498b68e564bc351acb14dd.
Poppler reports4A4pages,321432bytes, blank identifying metadata, no
encryption/forms/JavaScript. All listed fonts have embedded/subset/Unicode
flags yes. The mathematical reading used complete source text.

This reviewer did not perform terminal all-page visual QA after the fatal
admission reduction. The author's existing all-page review remains author
QA, not independently credited here. No final QA or publishability is claimed.
