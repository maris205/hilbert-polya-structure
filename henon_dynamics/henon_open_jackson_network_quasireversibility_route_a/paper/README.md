# Paper build

paper/main.tex is a single deterministic LuaLaTeX source. The macro
\(\backslash\)CRevisionRound selects one of three substantively increasing
versions:

- 0: product-form/global-balance closure;
- 1: reversed-network closure;
- 2: necessity, external-departure, boundaries, evidence, and Route-A closure.

The release gate compiles each round twice in separate temporary directories
with SOURCE_DATE_EPOCH=1788393600, FORCE_SOURCE_DATE=1, and TZ=UTC. The checked
paper/main.pdf must be byte-identical to paper/main_round2.pdf.
