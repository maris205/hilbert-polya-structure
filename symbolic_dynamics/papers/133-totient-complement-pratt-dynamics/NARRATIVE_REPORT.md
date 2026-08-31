# Narrative report

## Core story

Fix a nonempty finite prime set `P`, let `n` be its product, and iterate

```text
F_n(d)=gcd(n,(n/d)phi(d)),   d|n.
```

Squarefree support turns this arithmetic map into a signed Boolean system on
the induced Pratt divisibility DAG.  That reduction alone is elementary and
receives no contribution credit.  The residual short-note result is the
conjunction of three exact outputs for the literal arithmetic map: an
explicit decoder of every recurrent state from source phases, a uniform
entry bound in terms of longest directed path, and a one-step fibre formula
for every target divisor.

## Proof spine

1. If `S` is the prime support of `d`, then a prime `p` divides
   `(n/d)phi(d)` exactly when `p` is absent from `S` or some `q in S`
   satisfies `p|(q-1)`.  This proves the statewise support conjugacy.
2. In complemented coordinates the rule is
   `y'_p=(1-y_p) product_(q->p)y_q`.  Sources toggle.  Once parent phase pairs
   are known, the unique child phase pair is obtained by swapping the two
   parent conjunctions.  Hence `s` source phase bits give exactly `2^s`
   recurrent states and `2^(s-1)` exact two-cycles.
3. For a nonsource, consecutive parent conjunctions cannot both be one.  The
   resulting two-step identity erases the coordinate's initial value.
   Induction on source distance gives recurrence from time `h+1`.  This is a
   safe bound; no sharpness statement is made.
4. For a target support `B`, target zeros force specified source bits to one
   and all their parents to zero.  Inclusion--exclusion over the remaining
   bad target-one events gives the fibre over every `B`, whether or not `B`
   is in the image.

## Evidence and limitations

The paper-local verifier uses exact Python integers only.  It compares the
literal gcd/totient map, Boolean rule, phase decoder, tail bound, and all
target fibres on four explicit prime sets, including a singleton.  These
finite checks can refute a formula but cannot prove the all-parameter
theorems or establish novelty.

Prime-chain geometry and Pratt height are owned background, as is the general
AND--NOT/signed-Boolean framework.  A bounded search did not locate the exact
literal map or the combined decoder/bound/fibre package.  That non-hit is not
priority evidence, so external release remains on hold.

