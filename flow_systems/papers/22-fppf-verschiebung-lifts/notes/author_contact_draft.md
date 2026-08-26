# UNSENT author-contact draft

> **Status: UNSENT.** This is an internal drafting artifact only. No external
> contact has been authorized or made. Verify the final manuscript, author
> names, and attachment set before any future use.

**Draft date:** 2026-08-24  
**Proposed subject:** Question on Corollary 4.6 and Verschiebung lifting in
arXiv:2508.05329v1

Dear Professor Deninger,

We have been studying your paper *Rational Witt vectors and associated
sheaves*, in particular the Verschiebung lifting question on p. 25. We believe
that the following finite-free descent calculation may indicate an issue with
the sectionwise statement of Corollary 4.6 as it appears in v1.

Let

```text
A = F_2[x],              B = F_2[s],              x |-> s^2.
```

The section `1-xT^2` in `W_rat(A)` restricts over `B` to

```text
omega(2(s)) = (1-sT)^2 = 1-s^2 T^2.
```

Proposition 4.5, together with the Dedekind-domain refinement argument,
gives the relevant injectivity over the domain `B`, so
`2(s)^sharp` is the only possible local preimage. If a global preimage over
`A` existed, its two restrictions to

```text
B tensor_A B = F_2[s_1,s_2]/(s_1^2-s_2^2)
```

would agree. Pulling this equality back along

```text
s_1 |-> epsilon,         s_2 |-> 0
```

to `F_2[epsilon]/(epsilon^2)` would force `2(epsilon)^sharp=0`. This seems to
contradict precisely the nonzero kernel class established in Example 4.4.
Consequently, `1-xT^2` appears to have no global preimage in
`underline Z(A)^sharp`.

Our reading is that Proposition 4.3 supplies an epimorphism of sheaves, hence
local lifts, whereas the proof of Corollary 4.6 uses surjectivity on the
section group over `Spec A`. Proposition 4.5, together with the
Dedekind-domain refinement, supplies injectivity and therefore uniqueness of
the local lift, but it does not make that lift descend.
The same calculation also obstructs an additive lift of `V_2`: such a lift,
applied to `(x)^sharp`, would provide the missing global preimage. We have an
analogous argument for every index `N>1`, although the case `N=2` already
isolates the sectionwise issue.

Could you please let us know whether we have misunderstood the finite-flat
topology or the convention for sections, or whether Corollary 4.6 should be
read differently? Before circulating any manuscript, we wanted to check this
point with you. We would be glad to send a short detailed note containing the
all-index argument.

With best regards,

`[Author name(s)]`
