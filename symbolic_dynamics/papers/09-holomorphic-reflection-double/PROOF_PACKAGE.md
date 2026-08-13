# SD-C11 Proof Package

## Frozen object

Let `T_s^+` and `T_s^-` be two copies of the recurrent positive-cone
tensor-prime transfer, with disjoint directed-positive cocycle alphabets. On
the two-channel extension set

```text
C_s = [[0,T_s^+],[T_(1-s)^-,0]].
```

The trace is the channel matrix trace, the atom trace, and the two canonical
group traces. Reflection swaps the channels and canonically exchanges the
alphabets.

## Theorem chain

1. **Common ideal strip.** `C_s` belongs to noncommutative `L^q` exactly when
   `1/q < Re(s) < 1-1/q`. The first nonempty integer strip is `q=3`.

2. **Exact reflection.** After the fixed alphabet exchange,
   `J C_s J = C_(1-s)`. Hence every trace-series regularized determinant is
   invariant under `s <-> 1-s` wherever it is defined.

3. **All-order positive-cone sterility.** A cross-edge word is a nonempty
   positive word in at least one free factor and has zero canonical trace.
   The only visible closed words are alternating pure loops, so

   ```text
   Phi_2(C_s^(2r)) = 2 sum_p p^(-r),
   Phi_2(C_s^(2r+1)) = 0.
   ```

4. **Regularized determinant collapse.** The quadratic term diverges because
   `sum_p 1/p` diverges. On the common `L^3` strip,

   ```text
   det_3(I-z C_s) = product_p (1-z^2/p) exp(z^2/p),
   ```

   and is independent of `s`.

5. **Finite-channel rigidity.** In every finite bipartite reflected channel
   grammar whose identity-visible closed words are pure in one atom, each
   visible word has equal `s` and `1-s` counts. Its critical-line frequency
   is therefore zero. Constant signs, phases, finite supertraces, and virtual
   channel differences cannot restore motion.

6. **Two-step escape dichotomy.** Identifying a reflected label with an
   inverse makes a two-step word visible. Its weight is

   ```text
   p^(-s) q^(-(1-s))
     = (pq)^(-1/2) exp[-it log(p/q)].
   ```

   It is pure and stationary when `p=q`; it moves only when `p!=q`, in which
   case it is a forbidden mixed-atom ledger term.

## Boundary of proof

The rigidity result covers finite-channel, monomial endpoint-roof transfers
with bipartite reflection balance. It does not cover infinite-memory renewal
potentials, infinite channel limits, or nonmonomial source-derived roofs.
It proves neither analytic continuation nor a completed divisor, and it
does not produce a fixed self-adjoint operator.

## Route decision

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FAIL)

ROUTE_A_EXPLORATORY
GO_REFLECTION_RIGIDITY_THEOREM
STOP_VERTICAL_DIVISOR
STOP_FINITE_CHANNEL_ESCAPES
ROUTE_B_LOCKED
```
