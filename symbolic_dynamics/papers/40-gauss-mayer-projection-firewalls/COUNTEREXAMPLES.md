# Exact witnesses and sharp scope countermodels

Status: `POST_CANONICAL_DEPENDENT_RENDERING`
Candidate: `SD-C42`
Source lock: `2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041`
Control result: `d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f`
Prototype result: `2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995`

All matrices use `A(a)=[[a,1],[1,0]]` and left-to-right stored digit order.
Pair words are quotiented by cyclic pair rotation only.  These are contract
falsifiers and scope controls; no priority or minimality claim is attached to
them.

## In-contract exact witnesses

### C1: order-discriminant boundary

For `w=((1,1))`,

\[
M(w)=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad
t=3,\quad \det M=1,\quad \Delta_{\mathbb Z[M]}=5.
\]

This is the unique trace boundary where `(t-2)(t+2)` can be a rational prime.
It prevents the false statement that the order discriminant is never prime.

### C2: composite species in the full ledger

For `w=((1,2))`,

\[
M(w)=\begin{pmatrix}3&1\\2&1\end{pmatrix},\quad t=4,\quad \Delta=12.
\]

The full untwisted pair determinant therefore contains a composite trace
species.  It cannot equal a trace-prime selected product.

### C3: trace-4 reversal collision

The distinct pair necklaces `((1,2))` and `((2,1))` have matrices

\[
\begin{pmatrix}3&1\\2&1\end{pmatrix},\qquad
\begin{pmatrix}3&2\\1&1\end{pmatrix}.
\]

Both have determinant one, trace `4`, order discriminant `12`, norm label,
and roof in common.  They are digit reversals, but reversal is metadata and
is not part of the object quotient.  They are also the two `rho` phases of a
single `sigma`-period-two orbit, which confirms rather than removes their
distinctness in the pair ledger.

### C4: trace-6 non-reversal collision

The pair necklaces `((1,4))` and `((2,2))` have matrices

\[
\begin{pmatrix}5&1\\4&1\end{pmatrix},\qquad
\begin{pmatrix}5&2\\2&1\end{pmatrix}.
\]

They are not digit reversals, yet both have determinant one, trace `6`, and
order discriminant `32`.  The second word is pair-primitive even though its
flattened digit word is `sigma`-imprimitive.

### C5: trace-10 cross-length non-reversal collision

The pair words `((2,4))` and `((1,1),(1,2))` have matrices

\[
\begin{pmatrix}9&2\\4&1\end{pmatrix},\qquad
\begin{pmatrix}8&3\\5&2\end{pmatrix}.
\]

They are primitive, not digit reversals, and have pair lengths one and two.
Both have determinant one, trace `10`, and order discriminant `96`.  This
example is retained because it is cross-pair-length, not because it is
minimal.

### C6: raw operator-order discriminator

For the non-palindromic stored word `(1,2,2,3,1,4)`, `z=1/4`, and `s=1`,
globally reversing the raw `L_s^6` dummy indices gives

\[
\Phi_w(z)=\frac{442}{623},\qquad
G_{w,1}(z)=\frac{16}{388129}.
\]

Using the stored digits directly as raw nested indices gives the wrong
`146/697` and `16/485809`.  Trace alone does not expose this order error, so
the direct nested branch and weight are both required fixtures.

## Out-of-contract sharpness controls

### X1: odd determinant-minus-one boundary

The one-digit word `(3)` gives matrix `[[3,1],[1,0]]`, determinant `-1`,
trace `3`, and characteristic discriminant `13`.  It is outside the even-word
`SL_2(Z)` theorem domain.  Treating it as an in-domain pair word is rejected.

### X2: prime-indexed direct sum

The diagonal finite operator with basis values `2,3,5` has determinant
polynomial

\[
(1-2u)(1-3u)(1-5u)=1-10u+31u^2-30u^3.
\]

It is a positive countermodel to universal “no prime operator” language.  It
does not share the Gauss pair source object, marker, roof, or Mayer space, so
it provides no in-contract ownership.

### X3: one-field roof and marker mutations

Changing the derivative roof while keeping all other baseline fields fixed
changes exactly `clock`; changing `u`-per-digit to another marker changes
exactly `marker`.  These controls show that a roof or marker repair is a new
contract, not a harmless relabeling.  A mutation changing both fields is
rejected as nonexclusive.

### X4: selected scalar subproduct

Filtering the exact inventory `{3,4}` by primality gives `{3}` and removes
`{4}`.  This is a valid scalar selection, but the frozen schema declares no
projector owning it.  A string that calls the subproduct an “owner” is
rejected.

### X5: finite directed cycle

The three-cycle permutation matrix

\[
C=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}
\]

has `det(I-uC)=1-u^3`.  It is a positive finite determinant/primitive-cycle
model and therefore prevents a universal no-determinant conclusion.  It is
not the Mayer operator and earns no Route-A rung for SD-C42.

## Executable closure

The canonical control evaluates C1--C6 and X1--X5 as exact predicates.  Its
mutations change matrices, reversal and length classifications, parity,
determinant polynomials, field exclusivity, and declared-owner status.  The
independent evaluator recomputes the underlying records rather than trusting
the producer booleans.  The canonical prototype separately reproduces all
three collision classes, the odd boundary, the splitting law, and C6.  All
declared checks pass; the finite census supplies verification only, not the
universal theorem or witness novelty.
