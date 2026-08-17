# Paper 41 figure specification — SD-C43

All three figures are mutable writer-owned pure TikZ. They contain no raster
artwork, empirical count, provisional result, target-zero datum, or
integration-owned artifact. Color, shape, border, label, and line style
jointly encode meaning so that no conclusion depends on color alone.

## Figure 1 — rooted state and failed quotient arrows

File: `figures/rooted_state_non_descent.tex`.

- Left: `KnaufRootedWord`, with `M_w`, `h(w)`, and depth `k`.
- Center: the trailing-zero colimit `KnaufStableState`, reached by a solid
  arrow labeled `w ~ w0`; `h` is shown as owned by this quotient.
- Upper witness: `epsilon ~ 0`.
- A barred right-append arrow displays `h(1)=2` versus `h(01)=3` and says
  `append 1 does not descend`.
- Lower branch: a dashed cyclic-quotient attempt to `BinaryNecklace`, barred
  by `h(01)=3 != 2=h(10)`.
- A small scope badge says `full matrices or chosen roots = changed state`.

Caption requirement: the same invariant that certifies the trailing-zero
class distinguishes the two would-be append-one images. Cyclic rotation is a
second, separately failed quotient. The artwork rules out only the canonical
maps under the frozen `h` contract.

## Figure 2 — clock and scalar-phase witness map

File: `figures/clock_phase_non_descent.tex`.

- Top-left clock panel: cyclic rotations `01` and `10`, labeled by `3` and
  `2`.
- Top-right repetition panel: primitive word `1` with `h=2`, arrow `square`,
  repeated word `11` with `h=3`, and the failed target `4`.
- Bottom-left phase panel: cyclic rotations `001` and `010`, labeled by
  Liouville signs `+1` and `-1`.
- Bottom-right phase-power panel: `lambda(h(1))=-1`, whose square is `+1`,
  versus `lambda(h(11))=-1`.
- A positive-control strip shows `tr(M_{uv})=tr(M_{vu})` and matrix
  eigenvalue powers as valid changed clocks, not in-place repairs.

Caption requirement: exact finite witnesses defeat universal cyclic and
power identities for the frozen label and literal scalar observable. The
positive controls prevent the conclusion from being misread as a claim that
matrix models cannot carry cyclic or temporal data.

## Figure 3 — state-inventory determinant ownership

File: `figures/inventory_ownership.tex`.

- Left: finite rooted layers and the trailing-zero colimit with multiplicity
  `#{x:h(x)=n}=phi(n)`.
- Center: diagonal operator `Q_s e_x=h(x)^(-s)e_x` on the stable-state
  inventory, with domain `Re(s)>2`.
- Upper right: owned trace
  `Tr Q_s=zeta(s-1)/zeta(s)`.
- Lower right: owned marked determinant
  `Delta_K(s,u)=product_n(1-u n^(-s))^(phi(n))` and local trace-log
  boundary `|u|<1`.
- A barred arrow from the determinant to `binary primitive returns` says
  `u counts diagonal powers; no return map`.
- A boundary badge states `Delta_K(s,1)=0` because the `n=1` state contributes
  `1-u`.

Caption requirement: the diagonal determinant is mathematically valid but
belongs to state inventory. Its first trace-log coefficient is the partition
function; this does not identify the source quotient with a primitive-return
determinant or a fixed Hilbert--Polya operator.

## Shared visual language

- `formalblue`: frozen source object or exact identity;
- `deepgreen`: retained positive ownership statement;
- `warningamber`: changed type, domain, or scope boundary;
- `stopred`: failed descent or barred credit transfer;
- `governancepurple`: chronology and Route boundary;
- `softgray`: neutral metadata.

Solid arrows are declared maps. Dashed arrows are attempted quotients or
changed-model comparisons. A double slash across an arrow is a failed
descent. Dotted borders denote external or changed-model data.

## Quality gates

- pure vector TikZ with no title inside the artwork;
- legible at full text width and in grayscale;
- no arrow hides a node endpoint or crosses a mathematical label;
- captions remain self-contained;
- every object, marker, and operator type matches the immutable contract;
- no experiment, numerical target comparison, or writer-created result;
- no wording implies prospective selection, universal no-go, or novelty for
  the source quotient or diagonal trace principle.
