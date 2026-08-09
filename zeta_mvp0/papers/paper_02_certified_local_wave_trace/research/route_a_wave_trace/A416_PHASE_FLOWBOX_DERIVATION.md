# A4.16 phase-anchor and local flow-box derivation package

Date: 2026-08-09 (UTC)  
Programme: Route A / `R401-VAL`  
Status: **COHERENT AFTER REFRAMING / EXTRA ASSUMPTION**

## Target

The accepted A4.15 result proves uniqueness of a reduced return root in the
fixed positive-turning chart.  It does not, by itself, prove uniqueness of a
geometric periodic orbit modulo time translation.  A4.16 isolates and closes
the smallest missing bridge that can legitimately make that upgrade.

For fixed \(\epsilon\in[0,0.101]\), let \(\Phi_\epsilon^t\) be the Hamilton
flow on

\[
 \Sigma_\epsilon=\{z:K_\epsilon(z)=1\},
 \qquad I_{\rm near}=[0.64,0.69],
\]

and define

\[
 r_-^2(z)=(\omega_-Q_-)^2+P_-^2.
\]

The time-translation-invariant candidate class is

\[
 \mathscr C_\epsilon^{\rm tube}
 =\left\{(z,T):
 \begin{array}{l}
 z\in\Sigma_\epsilon,\ T\in I_{\rm near},\
 \Phi_\epsilon^Tz=z,\\[2pt]
 \displaystyle\sup_{0\le t\le T}
 r_-(\Phi_\epsilon^t z)<0.06
 \end{array}\right\}.
\]

Time translation acts by

\[
 s\cdot(z,T)=(\Phi_\epsilon^s z,T).
\]

The proposed A4.16 conclusion is the explicitly local statement

\[
 \boxed{
 \mathscr C_\epsilon^{\rm tube}/\mathbb R
 =\{[(z_\epsilon,T_\epsilon)]\},
 }
\]

where \((z_\epsilon,T_\epsilon)\) is the A4.12--A4.15 fast branch.  The
quantifier over candidates includes the full-period tube condition.  A4.16
does not claim that every periodic orbit on the complete energy shell belongs
to this class.

## Status

The mathematical reduction below is complete.  The new interval statements
are not yet theorem-authoritative.  They require a prospectively frozen
state-space proof tree, a validated full-trajectory enclosure for the known
branch, and an independent proof-object replay.  Until those gates pass,
A4.16 is a derivation and experiment target rather than an accepted
computer-assisted theorem.

## Invariant object

The invariant object is the quotient

\[
 \mathscr C_\epsilon^{\rm tube}/\mathbb R,
\]

not a preferred initial point on a periodic orbit.  The positive fast
turning section is only a phase anchor used to select one representative of
each quotient class.

Let

\[
 D_{\rm loc}=[-0.02,0.02]\times[0.12,0.17]
              \times[-0.08,0.08]
\]

in coordinates \((Q_-,Q_+,P_-)\), and set

\[
 \mathcal S_\epsilon^{\rm loc}
 =\{(Q_-,Q_+,P_-,0)\in\Sigma_\epsilon:
     (Q_-,Q_+,P_-)\in D_{\rm loc}\}.
\]

The corresponding reduced root box is

\[
 B_{\rm loc}=D_{\rm loc}\times I_{\rm near}.
\]

## Assumptions and inherited results

1. The normalized Hamiltonian and algebraic normal coordinates are exactly
   those frozen by `R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md`.
2. A4.12 supplies one continuous primitive fast branch in protected local
   boxes over all 51 parameter slabs.
3. A4.15 proves, for every slab and every parameter in that slab,

   \[
   Z(F_\epsilon)\cap B_{\rm loc}=\{x_\epsilon\}.
   \]

4. A candidate to which A4.16 applies remains in \(r_-<0.06\) for its
   complete period.  This is part of the definition of
   \(\mathscr C_\epsilon^{\rm tube}\), not a consequence of its value at one
   phase.
5. A new validated calculation must prove that the accepted branch itself
   remains in the stricter tube \(r_-<0.04\) for its complete period.

The fourth item is essential because \(r_-\) is not conserved by the
nonlinear flow.

## Notation and exact model

Let \(a=51/50\),

\[
 c=2(\sqrt{1+a}-1),
\]

and let \(O=(e_-\ e_+)\) be the exact algebraic orthogonal matrix from the
frozen normal-coordinate construction.  Write \(q=OQ\), \(p=OP\), and

\[
 W_\epsilon(q)=
 \begin{pmatrix}
 -cq_1-q_2-a\epsilon q_1^2\\
 q_1
 \end{pmatrix},
 \qquad R=|W_\epsilon(q)|^2.
\]

Then

\[
 K_\epsilon(Q,P)
 =\frac{P_-^2+P_+^2}{2}
 +2\pi^2R\,\operatorname{exprel}(\pi\epsilon^2R),
\]

where \(\operatorname{exprel}(s)=(e^s-1)/s\), continuously extended at
zero.  The normal frequencies are

\[
 \omega_\pm=2\pi\sqrt{\lambda_\pm}.
\]

All interval implementations must reconstruct these constants outward from
the algebraic definitions.  Rounded stored eigenvectors are not inputs.

## Derivation strategy

The original frozen theorem-domain protocol requested a dyadic ODE phase
tree.  For the present local tube, a smaller invariant certificate is
available:

1. prove that the fast polar radius never vanishes on
   \(K_\epsilon=1, r_-\le0.06\);
2. prove strict positive fast angular velocity on the same constrained
   state domain;
3. prove that one period accumulates less than \(4\pi\) of fast angle;
4. infer winding number one and hence exactly one positive fast turning
   crossing;
5. prove statically that this crossing lands in \(D_{\rm loc}\);
6. invoke A4.15 at the anchored crossing;
7. separately certify that the distinguished branch belongs to the tube.

This replaces a time-parameterized phase search by a constrained
state-space interval proof.  It is a prospective protocol refinement and
cannot silently overwrite the older frozen gate.

## Derivation map

\[
\begin{array}{c}
 K_\epsilon=1,\ r_-<0.06,\ T\in[0.64,0.69]\\
 \Downarrow\\
 \rho_+^2=\omega_+^2Q_+^2+P_+^2>0,
 \quad 0<\dot\vartheta_+\le18\\
 \Downarrow\\
 0<\Delta\vartheta_+<18(0.69)<4\pi\\
 \Downarrow\\
 \operatorname{wind}_+=1\\
 \Downarrow\\
 \exists!\ s\in[0,T):\ P_+(s)=0,\ Q_+(s)>0\\
 \Downarrow\\
 (Q_-(s),Q_+(s),P_-(s),T)\in B_{\rm loc}\\
 \Downarrow\quad\text{A4.15}\\
 (\Phi_\epsilon^s z,T)=(z_\epsilon,T_\epsilon)\\
 \Downarrow\\
 [(z,T)]=[(z_\epsilon,T_\epsilon)].
\end{array}
\]

## Main derivation

### 1. Fast-angle identity

On the fast plane away from the origin define a lifted angle by

\[
 \vartheta_+=\operatorname{atan2}(-P_+,\omega_+Q_+).
\]

Hamilton's equations give \(\dot Q_+=P_+\) and
\(\dot P_+=-\partial_{Q_+}K_\epsilon\).  Differentiating `atan2` yields

\[
\begin{aligned}
 \dot\vartheta_+
 &=\frac{(\omega_+Q_+)(-\dot P_+)
          -(-P_+)(\omega_+\dot Q_+)}
         {\omega_+^2Q_+^2+P_+^2}\\
 &=\boxed{
 \omega_+
 \frac{P_+^2+Q_+\partial_{Q_+}K_\epsilon}
      {\omega_+^2Q_+^2+P_+^2}}.
\end{aligned}
\]

Set

\[
 D_+=\omega_+^2Q_+^2+P_+^2,
 \qquad
 N_+=P_+^2+Q_+\partial_{Q_+}K_\epsilon.
\]

The new static proof tree must certify, on every point satisfying
\(K_\epsilon=1\) and \(r_-\le0.06\),

\[
 D_+>0,\qquad N_+>0,
 \qquad \omega_+N_+/D_+<18.
\]

The fixed rational ceiling 18 is deliberately stronger than needed, since

\[
 18\cdot0.69=12.42<4\pi.
\]

### 2. Winding and the unique positive crossing

For a periodic candidate in the tube, \(D_+>0\) makes the fast-plane loop
avoid the origin.  Its lifted angle therefore satisfies

\[
 \vartheta_+(T)-\vartheta_+(0)=2\pi m,
 \qquad m\in\mathbb Z.
\]

Strict positivity of \(\dot\vartheta_+\) gives \(m>0\), while the rate and
period ceilings give

\[
 2\pi m<18(0.69)<4\pi.
\]

Hence \(m=1\).  A strictly increasing lift gaining exactly \(2\pi\) crosses
the congruence class \(0\pmod{2\pi}\) exactly once in the half-open interval
\([0,T)\).  At that phase,

\[
 P_+=0,\qquad Q_+>0.
\]

Moreover, there \(N_+=Q_+\partial_{Q_+}K_\epsilon>0\), so

\[
 \partial_{Q_+}K_\epsilon>0,
 \qquad \dot P_+=-\partial_{Q_+}K_\epsilon<0.
\]

Thus the crossing is oriented and transverse.  Winding one also excludes a
proper multiple traversal in the declared period window.

### 3. Landing in the accepted reduced chart

The slow-radius bound immediately gives

\[
 |P_-|<0.06<0.08,
 \qquad
 |Q_-|<\frac{0.06}{\omega_-}
 <0.015<0.02.
\]

The remaining landing gate is the constrained interval statement

\[
 \left.
 \begin{array}{c}
 K_\epsilon=1,\quad r_-\le0.06,\\
 P_+=0,\quad Q_+>0
 \end{array}
 \right\}
 \Longrightarrow
 0.12<Q_+<0.17.
\]

No separate numerical slope threshold is needed here.  On a surviving
positive section point, the already certified angle numerator gives
\(Q_+K_{Q_+}>0\), hence \(K_{Q_+}>0\).  The proof object may report a
quantitative lower margin as telemetry, but that value is not a smoke gate.

### 4. Reduction to the A4.15 root theorem

Let \((z,T)\in\mathscr C_\epsilon^{\rm tube}\), and translate it to its
unique positive crossing \(z'=\Phi_\epsilon^s z\).  The landing result gives

\[
 (Q_-(z'),Q_+(z'),P_-(z'),T)\in B_{\rm loc}.
\]

Periodicity gives the reduced return equations

\[
 F_\epsilon(Q_-(z'),Q_+(z'),P_-(z'),T)=0.
\]

A4.15 says that the only such root is \(x_\epsilon\).  Hence
\((z',T)=(z_\epsilon,T_\epsilon)\).  Uniqueness of the Hamiltonian initial
value problem then implies that the two complete trajectories agree, and

\[
 [(z,T)]=[(z_\epsilon,T_\epsilon)].
\]

### 5. Analytic flow-box consequences

At a certified positive crossing, let \(h(z)=P_+\).  Since

\[
 dh(X_{K_\epsilon})=-\partial_{Q_+}K_\epsilon<0,
\]

the energy shell is regular there, the section is transverse, and the local
flow-box map \((s,\xi)\mapsto\Phi_\epsilon^s(\xi)\) is a local
diffeomorphism.  The event time is a unique local \(C^1\) function with

\[
 D\tau(z)=
 -\frac{dh_{\Phi^\tau z}D_z\Phi^\tau(z)}
        {dh_{\Phi^\tau z}X_{K_\epsilon}(\Phi^\tau z)}.
\]

On the section, the energy constraint solves locally for \(Q_+\) as a
function of \((Q_-,P_-)\), with embedding derivative

\[
 D\iota=
 \begin{pmatrix}
 1&0\\
 -K_{Q_-}/K_{Q_+}&-K_{P_-}/K_{Q_+}\\
 0&1\\
 0&0
 \end{pmatrix}.
\]

These are analytic consequences of transversality.  A local flow-box theorem
alone does not supply the whole-circuit phase coverage; that role is played
by the winding certificate above.

## Validated outer-domain obligations

The state-space proof may not assume a convenient finite box without proving
that it contains the constrained shell.  The proposed implementation must
certify the following chain with directed rounding:

1. \(r_-\le0.06\) and \(\omega_->4\) imply
   \(|Q_-|<0.015\), \(|P_-|\le0.06\).
2. Nonnegative potential and \(K=1\) imply
   \(|P_+|\le\sqrt2<1.415\).
3. Write \(W=Aq-a\epsilon q_1^2e_1\), where
   \(A^TA=O\operatorname{diag}(\lambda_-,\lambda_+)O^T\) and \(W_2=q_1\).
   Since \(\operatorname{exprel}(s)\ge1\) for \(s\ge0\), the energy shell
   gives \(|W|\le1/(\sqrt2\pi)\) and \(|q_1|\le|W|\).  Therefore

   \[
   \sqrt{\lambda_+}|Q_+|
   \le |Aq|
   \le |W|+a\epsilon |q_1|^2
   \le \frac1{\sqrt2\pi}
      +\frac{a\epsilon}{2\pi^2}
   <0.18\sqrt{\lambda_+}.
   \]

   Thus \(|Q_+|<0.18\) follows directly from one outward algebraic gate; no
   assumed outer shell or numerical compactness argument is needed.

Only after these three gates pass may the angle tree use the compact root
domain

\[
 [0,0.101]\times[-0.015,0.015]\times[-0.18,0.18]
 \times[-0.06,0.06]\times[-1.415,1.415].
\]

## Remarks and interpretation

- The static angle certificate is stronger and smaller than a dense time
  scan: it controls every point of every admissible tube-contained orbit at
  once.
- Exactly one positive crossing is stronger than the orbit-uniqueness proof
  strictly needs; one crossing in \(B_{\rm loc}\) would suffice.
- Preliminary nonrigorous scouts found angular rates near 9.3--9.7, well
  below the frozen ceiling 18, and branch slow radii near 0.011, well below
  0.04.  These values guide the protocol but carry no theorem authority.
- An inline 128-bit Arb prototype closed a state-space tree without unresolved
  leaves.  Because that prototype was not archived, independently checked,
  or prospectively frozen, it is evidence of feasibility only.

## Boundaries and non-claims

A successful A4.16 certificate would prove uniqueness modulo time
translation only among periodic candidates whose complete trajectories stay
inside \(r_-<0.06\), together with membership of the accepted branch in the
stricter \(r_-<0.04\) tube.  It would not prove:

- that every orbit on the complete energy shell enters or remains in this
  tube;
- the global return-exclusion cover for \(r_-\ge0.05\) or far periods;
- uniqueness in global phase space;
- the independent event-projected determinant or Taylor residual;
- a quantitative trace radius \(\delta_{\rm tr}\) or the programme threshold
  \(P_0\);
- a trace formula, prime-orbit identity, Hilbert--Polya operator, zeta-zero
  reconstruction, RH, or any implication toward RH.

## Open risks

1. **Outer-box leakage.**  The proof is invalid unless the singular-value
   inequality giving \(|Q_+|<0.18\), together with the slow and momentum
   bounds, is an explicit outward-rounded proof object.
2. **Constraint overreach.**  A box intersecting both \(K=1,r_-\le0.06\)
   may be discarded only by a rigorous energy or tube separation, never by
   midpoint sampling.
3. **Angular wrapping.**  Direct interval division can become too wide near
   small fast radius; unresolved boxes must split or fail, not be accepted by
   a Boolean summary.
4. **Branch trajectory wrapping.**  The existing pure-Arb Taylor integrator
   is too wide on whole root boxes.  The intended branch proof uses the pinned
   CAPD multiprecision Lohner `SolutionCurve` and a complete dyadic phase
   cover.
5. **Endpoint double counting.**  Crossings are counted on \([0,T)\), not on
   both endpoints of \([0,T]\).
6. **Protocol authority.**  The static winding route is a prospective
   amendment.  It must pass independent review and freeze before any
   all-slab theorem run can license A4.16.
