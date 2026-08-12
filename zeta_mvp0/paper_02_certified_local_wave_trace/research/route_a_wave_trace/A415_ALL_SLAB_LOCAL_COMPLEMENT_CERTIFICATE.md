# A4.15 All-Slab Local-Complement Certificate

Protocol: `R401-VAL-L2-A1`  
Archive generation: `a658e754000ea29aa0f2289aa03f45b565e216c96584fb3de6d494f9c27c95e0`  
Independent replay: 158,782 checks with zero failures.

## Certified mathematical statement

Let

\[
B_{\mathrm{loc}}=[-0.02,0.02]\times[0.12,0.17]\times[-0.08,0.08]\times[0.64,0.69]
\]

in the frozen reduced coordinates `q_slow, q_fast, p_slow, period`. For every
frozen slab \(E_j\), \(j=0,\ldots,50\), every \(\epsilon\in E_j\), and the
corresponding protected L1 box \(P_j\), the certified complement calculation
gives

\[
Z(F_\epsilon)\cap\bigl(B_{\mathrm{loc}}\setminus\operatorname{int}P_j\bigr)
=\varnothing.
\]

Combined only with the previously accepted L1 existence-and-uniqueness
certificate inside \(P_j\), this yields

\[
Z(F_\epsilon)\cap B_{\mathrm{loc}}=\{x_j(\epsilon)\}.
\]

This conclusion is pointwise in \(\epsilon\) and confined to the frozen local
\(P_+=0\) reduced chart.

## Certified evidence

- The canonical matrix contains 51 slabs at 128-bit precision and the same 51
  slabs at 256-bit precision, for 102 completed trees.
- The archive contains 52,790 evaluated nodes: 3,368 energy exclusions, 23,435
  return exclusions, and 25,987 internal split nodes.
- All 26,803 terminal leaves are certified exclusions; the remaining frontier
  is empty.
- The independent exact-rational replay performed 158,782 checks and reported
  zero failures.
- No blocking classification, root candidate, invalid result, timeout, depth
  exhaustion, node-budget exhaustion, or precision-domain disagreement
  remains.

| Provenance edge | SHA-256 |
|---|---|
| Main freeze | `c64d7b3cb7d6cfef403edfe35b7459ba5291608104aea4653ae8c0feec710cf2` |
| Machine freeze | `b9291716b859da9651a2549832581cf85b1852b725bcf285539dea47eb7cbef4` |
| Sealed run configuration | `f2d3eef4a76f18246c15789e32fe597266e3fe855c5e9a8bd2b5c3e67dfdf70d` |
| Aggregate summary | `769f06671d23a16be4b8a4cedead3d25370423d0fee2484342c83a0fef61ecfe` |
| Aggregate manifest | `c2e06c4cb7abdac56c157f334c9949441de97bfad84fedee893992d87bf253b2` |
| Independent checker | `a3663435de931c30769038deffbc7cc05fe6f6613c5da638c77301396695c707` |
| Postcheck object | `54a2aa4efbf27d4018c5b1ad313a2fc32f2423e9529e9a7b2fbe6890ffa2450a` |
| Ordered tree-manifest root | `240c81a09d4ffd327fb1f3ba660d6df32c8bb300a3bf62f1481d0c9d3e37605c` |

## Acceptance declaration

Status: PASS_LOCAL_COMPLEMENT_ALL_SLABS
milestone_status = PASS_LOCAL_COMPLEMENT_ALL_SLABS
theorem_status = PASS_LOCAL_COMPLEMENT_ALL_SLABS
final_status = null
Claim boundary: local P_+=0 reduced-chart result only; no energy-shell/global, trace-formula, Hilbert-Polya, zeta-zero, or RH promotion

## Scope limitations

This certificate does not provide a phase or flow-box cover of a complete
periodic orbit, uniqueness on a full energy shell or in global phase space,
continuation outside the 51 frozen slabs, a primitive-period theorem,
exclusion of every shorter return, an event-projected determinant bound, or a
new quantitative trace-domain margin. It supplies no trace formula,
arithmetic-prime theorem, Hilbert--Polya operator, Riemann-zero reconstruction,
proof of RH, or implication toward RH.
