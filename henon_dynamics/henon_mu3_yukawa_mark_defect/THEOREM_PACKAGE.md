# HCS-C65 theorem package

Status: **PREFREEZE_IMPLEMENTED / PAPER_COMPILED / NOT_RELEASED**.

Let (z_1,z_2,z_3) be the C63 integer character-kernel basis and let (m)
be the C64 16-type mark map.  Put

[
L_o=m\langle z_1,z_3\rangle,\qquad L_a=m\langle z_1,z_2,z_3\rangle,
\qquad U(L)=(\mathbb QL)\cap\mathbb Z^{16}.
]

The displayed C63 kernel basis is saturated (the gcd of its (3\times3)
maximal minors is 1).  The exact determinantal-divisor computations give

[
\operatorname{SNF}(L_o)=(2,8),\qquad
\operatorname{SNF}(L_a)=(2,2,8),
]

and hence

[
U(L_o)/L_o\cong\mathbb Z/2\oplus\mathbb Z/8,
\qquad
U(L_a)/L_a\cong\mathbb Z/2\oplus\mathbb Z/2\oplus\mathbb Z/8.
]

Writing (u_1=m(z_1)/8), (u_2=m(z_2)/2), and (u_3=m(z_3)/2), these
three vectors form a saturated basis of (U(L_a)), while (u_1,u_3) form
a saturated basis of (U(L_o)).  Therefore

[
U(L_a)/(L_a+U(L_o))\cong\mathbb Z/2,
]

with generator the class of (u_2=m(z_2)/2=-m(R_4)/2).  This is the precise
meaning of the one-class jump; it avoids an ill-defined quotient of finite
groups of different ranks.

Scope is restricted to the C63/C64 16-type submodule and
`NO_BAD_EULER_OR_ROOT_NUMBER`.
