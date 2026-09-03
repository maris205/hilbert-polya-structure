# P178 narrative report — state-selected finite differences

**Round:** Round 2 dual-review freeze  
**Format:** anonymous AMS short theory note  
**Scientific status:** `OWNER_THIN`  
**External lifecycle:** `HOLD_EXTERNAL`

## One-sentence thesis

When a function on \(\mathbb F_p\) chooses its own finite-difference
direction through its current value at zero, the resulting nonlinear map has
a sharp \(p\)-step clock, a complete every-time/every-target fibre atlas,
closed depth shells, and an exact transition Jordan inventory.

## Literal object

For the full \(p\)-dimensional function space

\[
\mathcal V_p=\{f:\mathbb F_p\to\mathbb F_p\},
\]

define

\[
T_p(f)(x)=f(x+f(0))-f(x).
\]

The update is not a fixed difference operator: after each epoch the new
state selects the next direction again. A zero selected direction sends the
state to zero, while a nonzero direction advances one layer in the cyclic
augmentation flag.

## Technical story

Let \(N=\tau_1-I\) and \(J^t=N^t\mathcal V_p\). The binomial functions
\(e_j(x)=\binom{x}{j}\) form a basis with \(Ne_j=e_{j-1}\), so
\(\dim J^t=p-t\). For every nonzero \(a\),

\[
\tau_a-I=N\,U_a(N),\qquad U_a(0)=a\ne0,
\]

and \(U_a(N)\) is a unit. Thus every nonzero direction maps \(J^i\) onto
\(J^{i+1}\) with the constant functions as its one-dimensional kernel.

The crucial inverse step adds the anchor \(f(0)=a\). Evaluation at zero is
nonzero on the constant kernel, so it selects exactly one lift. A nonzero
time-\(t\) target therefore has one source for each word in
\((\mathbb F_p^\times)^t\). This yields \((p-1)^t\) sources, while mass
balance gives the exceptional zero fibre. The same cumulative zero fibres
give all depth shells.

Finally, the deterministic transition operator splits into its rank-one
fixed projection and a nilpotent complement. Its nilpotent rank sequence is
\(p^{p-t}-1\); second differences determine every zero-Jordan block.

## Frozen theorem spine

1. \(\operatorname{im}T_p^t=J^t\) and
   \(|\operatorname{im}T_p^t|=p^{p-t}\) for \(0\le t\le p\).
2. For \(1\le t\le p\), every nonzero \(g\in J^t\) has
   \((p-1)^t\) time-\(t\) preimages, the zero fibre has
   \(p^p-(p^{p-t}-1)(p-1)^t\) elements, and all other fibres vanish.
3. The graph is a single rooted component of sharp height \(p\), with
   \[
   A_0=1,\qquad
   A_d=(p-1)^{d-1}(p^{p-d}+p-2).
   \]
4. The complex transition operator has characteristic polynomial
   \((\lambda-1)\lambda^{p^p-1}\), with
   \[
   m_s=(p-1)^2p^{p-s-1}\ (s<p),\qquad m_p=p-1
   \]
   zero-Jordan blocks of size \(s\).

## Contribution and owner boundary

The paper assigns zero contribution credit to fixed finite-difference
operators, augmentation-ideal powers and nilpotence, affine kernel-coset
counts, linear finite dynamical systems, and the generic conversion from
power ranks to Jordan block multiplicities. Internally, A05 already tested a
fixed cyclic difference and P164 already used a nonlinear front followed by
a fixed cyclic-difference tail.

The retained residual is the repeated state selection, the observable
nonzero direction word, and the anchor that makes each reverse integration
unique. A bounded literal search did not find this exact conjunction, but
that nonhit is not a novelty, priority, or freedom-to-operate claim.

## Evidence and limitation

The standalone verifier exhausts all states, all targets, and every time for
\(p=2,3,5\). A separately organized matrix certificate checks the
augmentation flag and anchored-map ranks through \(p=19\). Its settled
transcript contains 44,689 exact assertions. Computation is falsification
pressure only; the all-prime result rests on the proof.

The theorem is restricted to prime fields. No extension-field analogue is
claimed, because a single scalar value \(f(0)\in\mathbb F_{p^e}\) need not
generate the additive translation group.
