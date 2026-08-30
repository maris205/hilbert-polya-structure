# Proof spike: transpose self-commutator collapse

**Status:** `KILLED AFTER HOSTILE GATE / CORRECTED ARCHIVE ONLY`.
The initial depth census confused the image with the kernel; the formulas
below incorporate the correction.  The literal map also repeats the earlier
P117--P121 candidate B2B-08, already killed as theorem-thin.  It may not
receive a paper number.  **External status:** `HOLD_EXTERNAL`.

## 1. The universal two-step identity

Let \(R\) be an associative algebra equipped with an involution
\(x\mapsto x^*\), and define

\[
                    \Delta(x)=xx^*-x^*x.
\]

Both \(xx^*\) and \(x^*x\) are self-adjoint, hence
\(\Delta(x)^*=\Delta(x)\).  Every self-adjoint element \(h\) satisfies
\(\Delta(h)=hh-hh=0\).  Therefore

\[
                         \boxed{\Delta^2=0}
\]

on every involutive associative algebra, in every characteristic.  Thus zero
is the unique periodic point and every orbit has depth at most two.  This
identity is elementary and receives no novelty credit by itself; its role is
to expose the exact finite-field fibre problem.

## 2. Complete graph on \(M_2(\mathbb F_q)\)

Take the transpose involution and write

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
u=b-c,\quad v=b+c,\quad w=a-d.
\]

A direct multiplication gives

\[
\Delta(A)=
\begin{pmatrix}
uv&-uw\\-uw&-uv
\end{pmatrix}.                                           \tag{1}
\]

### Odd characteristic

When \(q\) is odd, \((a,b,c,d)\mapsto(u,v,w,a+d)\) is invertible.  Formula
(1) shows that the image is the full two-dimensional space of symmetric
trace-zero matrices.  For a nonzero target \((x,y)=(uv,-uw)\), necessarily
\(u\ne0\); there are \(q-1\) choices of \(u\), then unique \(v,w\), and
\(q\) choices of \(a+d\).  Hence every nonzero image point has \(q(q-1)\)
preimages.  Above zero, either \(u=0\) and \((v,w)\) is arbitrary, or
\(u\ne0\) and \(v=w=0\).  Multiplying by the free trace coordinate gives

\[
 |\operatorname{im}\Delta|=q^2,qquad
 |\Delta^{-1}(0)|=q(q^2+q-1),qquad
 |\Delta^{-1}(B)|=q(q-1)\quad(B\ne0).                    \tag{2}
\]

The zero fibre is the kernel of the set map.  Since the image is a proper
subset of that kernel, the exact depth census is

\[
 (L_0,L_1,L_2)=
 (1,q^3+q^2-q-1,q^4-q^3-q^2+q).                          \tag{3}
\]

### Characteristic two

Now \(u=v=b+c\) and \(w=a+d\), so

\[
\Delta(A)=\begin{pmatrix}u^2&uw\\uw&u^2\end{pmatrix}.   \tag{4}
\]

Frobenius is bijective on every finite field.  The zero image has \(u=0\);
for each \(u\ne0\), the off-diagonal entry \(uw\) ranges freely.  Thus

\[
 |\operatorname{im}\Delta|=1+q(q-1)=q^2-q+1.             \tag{5}
\]

The linear map from the four matrix entries to \((u,w)\) has fibres of size
\(q^2\).  The zero target permits all \(q\) values of \(w\), whereas a
nonzero target determines \((u,w)\).  Consequently

\[
 |\Delta^{-1}(0)|=q^3,qquad
 |\Delta^{-1}(B)|=q^2\quad(B\ne0),                       \tag{6}
\]

and the kernel-based depth census is

\[
       (L_0,L_1,L_2)=(1,q^3-1,q^4-q^3).                  \tag{7}
\]

Equations (2)--(7), together with the strict inclusion of the image in the
kernel, split the vertices into zero; nonzero image points; kernel points
outside the image; and points outside the kernel.  The latter two classes
have indegree zero, while the first two have the displayed fibre sizes.

## 3. Controls and claim ceiling

The independent verifier enumerates all \(2\times2\) matrices over
\(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,
\mathbb F_8,\mathbb F_9\), checks literal matrix multiplication, every second
iterate, the full fibre multiset, and (2)--(7).  It also exhausts
\(M_3(\mathbb F_2)\) and \(M_3(\mathbb F_3)\) for the universal identity.

Ordinary commutators, self-commutators, involutions, symmetric matrices,
quadratic fibres, and the observation that a self-adjoint input maps to zero
are zero-credit background.  The candidate residual is deliberately narrow:
the characteristic-sensitive complete functional graph (2)--(7), placed
inside the universal involutive-algebra collapse.  A bounded exact-map search
found no direct source for these finite-field fibre formulas; that non-hit is
not a novelty certificate.

**Final internal verdict:** `CORRECTED BUT KILLED / ARCHIVE ONLY`.
