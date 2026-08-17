# Typed object, marker, operator, and determinant contract

## Type ledger

| Type | Definition | Owned data | Explicitly not owned |
|---|---|---|---|
| `KnaufRootedWord` | a finite binary word `w` with a distinguished first letter | `M_w`, first column, `h(w)`, word depth | cyclic orbit, primitive class |
| `KnaufStableState` | colimit class under `w -> w0` | stable value `h([w])`; full multiplicity ledger | right append action, necklace rotation |
| `BinaryNecklace` | cyclic-rotation class of a nonempty word | word period and powers, once defined | `h`, because `h(01)!=h(10)` |
| `FareyTraceWord` | matrix word weighted by `tr(M_w)` or a matrix eigenvalue | cyclic trace and matrix-power data | the frozen rooted `h` partition trace |
| `LiouvilleStateObservable` | `lambda(h(w))` | arithmetic value attached after `h` | source-derived symbolic cocycle |
| `StateInventoryDiagonal` | diagonal operator indexed by stable states | a trace and ordinary marked determinant | graph step, primitive return map |
| `DynamicalTransferOperator` | operator whose powers enumerate returns on a declared phase space | only if separately constructed | no such operator is source-owned by `SD-C06` |

No arrow between two rows inherits the source type automatically.

## Marker ledger

| Marker | Meaning | Legal use | Illegal identification |
|---|---|---|---|
| `k` | finite spin-chain depth | index `W_k` and `Z_k(s)` | primitive period or repetition count |
| `s` | inverse-temperature/Dirichlet variable | weight `h(w)^(-s)` | orbit marker |
| `u` | free power marker for the diagonal inventory operator | `det(I-uQ_s)` and its trace-log | original graph step or spin depth |
| `r` | formal temporal repetition of a putative primitive word | test `w -> w^r` | finite-depth extension `w -> w0` |

## Finite operator

On `H_k=C^{W_k}` define the diagonal operator

\[
 Q_{k,s}e_w=h(w)^{-s}e_w.
\]

Then `Tr Q_{k,s}=Z_k(s)`.  This is a finite state-inventory identity.  The
operator is not the binary refinement, not a transfer operator, and not a
periodic return operator.

## Limiting state-inventory operator

Let `S_K=colim(W_k,w->w0)`.  The source multiplicity theorem gives

\[
 \#\{x\in S_K:h(x)=n\}=\varphi(n).
\]

For `Re(s)>2`, define on `H_K=ell^2(S_K)`

\[
 Q_se_x=h(x)^{-s}e_x.
\]

It is trace class because

\[
 \|Q_s\|_1=\sum_x |h(x)^{-s}|
 =\sum_{n\ge1}\varphi(n)n^{-\Re s}<\infty.
\]

Consequently

\[
 \operatorname{Tr}Q_s=\frac{\zeta(s-1)}{\zeta(s)}.
\]

This gives a valid operator realization of the **partition trace only**.  It
does not upgrade A4: `Q_s` depends on the spectral parameter `s`, is generally
not self-adjoint for complex `s`, and does not supply a fixed Hilbert--Polya
operator or same-clock primitive return dynamics.

## Owned determinant

The diagonal object owns

\[
 \Delta_K(s,u)=\det(I-uQ_s)
 =\prod_{x\in S_K}(1-u h(x)^{-s})
 =\prod_{n\ge1}(1-u n^{-s})^{\varphi(n)}.
\]

For `Re(s)>2` it is an ordinary trace-class Fredholm determinant, entire in
`u`.  On `|u|<1`, where the principal trace-log expansion is unambiguous,

\[
 -\log\Delta_K(s,u)
 =\sum_{r\ge1}\frac{u^r}{r}\operatorname{Tr}(Q_s^r)
 =\sum_{r\ge1}\frac{u^r}{r}
   \frac{\zeta(rs-1)}{\zeta(rs)}.
\]

The coefficient of `u` is the source partition function.  Higher coefficients
are independently forced by the diagonal inventory.  Since the `n=1` state
contributes `(1-u)`, `Delta_K(s,1)=0`; in particular the source quotient is
not recovered by setting `u=1`.

This determinant is a prior-art consistency control, not the proposed new
result and not an A2 primitive-orbit determinant.

## Proposed terminal codes

```text
GO_SOURCE_PARTITION_TRACE_IDENTITY
STOP_DIRECT_LIMIT_RIGHT_ACTION_NON_DESCENT
STOP_ROOTED_CLOCK_CYCLIC_DESCENT
STOP_ROOTED_CLOCK_TEMPORAL_POWERS
STOP_LIOUVILLE_ORBIT_CHARACTER
STOP_INVENTORY_TRACE_PRIMITIVE_DETERMINANT_IDENTIFICATION
ROUTE_A_REJECTED
```

