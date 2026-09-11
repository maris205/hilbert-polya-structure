# P214 Review A artifact reception contract

PENDING ACTUAL BUILD. Acceptance requires all of the following from the new
`reviews/p214_a/build01` tree; this file is a contract, not a receipt.

- Build controller and all four passes exit zero; raw streams and commands are
  complete, and source/runtime keys are identical before and after.
- Cold source inventory is exactly the nine pinned files, all regular nonlinks,
  with no reused PDF or generated product before pass 1.
- Ordered FLS events reconcile every consumed input with the cold source set
  and the separately bound runtime manifest; unknown inputs are a stop.
- AUX/BBL/BLG/LOG/PDF and every pass snapshot are retained. References and
  citations resolve; diagnostics contain no error, undefined reference,
  missing glyph, overfull or underfull warning.
- PDF metadata, complete extracted text, font table and all page PNGs are
  retained. Every font is embedded and the abstract text actually contains
  `polynomial map`.
- The receiver compares every artifact as whole raw bytes, checks exact tree
  membership and writes a nonself manifest without overwriting failed or old
  evidence.

Only after this DATA reception and actual page inspection may the same A
reviewer issue the final verdict. HOLD_EXTERNAL.
