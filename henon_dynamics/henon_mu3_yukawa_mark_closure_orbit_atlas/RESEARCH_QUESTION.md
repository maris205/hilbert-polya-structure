# C76 research question

For the sixteen frozen C75 labels in

\[
Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2,
\]

what is the exact orbit atlas of finite label supports under the effective
label symmetry, and which supports are irredundant for generating a prescribed
closure?

The question has five exact parts:

1. Quotient the C75 lifted symmetry by its ambient C6 action kernel and
   record a faithful permutation presentation on the sixteen labels.
2. Enumerate the induced orbits on all `2^16 = 65536` supports, including the
   orbit-size spectrum and the count at each support cardinality.
3. Compute the generated subgroup `Phi(A)` for every support and tabulate the
   closure atlas over all twenty subgroups of `Q`.
4. Identify supports that are single-deletion minimal for their generated
   closure, and then restrict to minimal supports whose closure is all of `Q`.
5. Verify that the effective label action, rather than the non-faithful
   ambient lattice action, is the object used for support orbits.

For a support `A`, define

\[
\Phi(A)=\left\langle x_i:S_i\in A\right\rangle\leq Q,
\qquad \Phi(\varnothing)=\{0\}.
\]

The C76 closure-minimal convention is: `A` is minimal iff `A` is empty or
every single-label deletion changes `Phi(A)`.  Full-core minimality adds the
condition `Phi(A)=Q`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
