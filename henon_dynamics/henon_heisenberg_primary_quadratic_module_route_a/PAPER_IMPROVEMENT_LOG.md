# C156 paper improvement log

No external or cross-model reviewer was used or claimed.  The two rounds below
are genuine internal theorem, scope, and presentation audits without numerical
scores.

## Pre-manuscript derivation audit

The first derivation treated the canonical correction `q_B` as though it were
the actual iterate cocycle.  Exact checks at `n=2,6,8,12` showed that this
changes zero counts.  The repaired theorem and evidence retain
`q_n=q_(A^n)+ell_n` with the integer linear drift explicitly recorded.  Signed
polynomial coefficients use a non-modular serializer; only rotation residues
are reduced modulo one.

## Round 0 to round 1

The baseline PDF stated the exponent denominator but compressed the parity
argument into one sentence and did not display the rotation polarization.
During expansion, an initial auxiliary formula used the wrong second mixed
term.  A separate symbolic derivation fixed it to

```text
beta([m],[u])=v_1*u_2-u_1*v_2+m_1*u_2.
```

**Fix:** expose the integer numerator `N`, its complete reduction modulo two,
the period-three Fibonacci/Lucas cases, and the corrected polarization.
SymPy now derives both cocycle and rotation polarizations; the checker also
tests a nontrivial per-iterate sentinel and every cross-primary pair.

## Round 1 to round 2

The second review found three presentation gaps: the odd-primary argument did
not explain the `p=2` edge, the exact table hid how local products look, and
the manuscript lacked the academic-paper declarations and bilingual abstract.

**Fix:** explain how the all-iterate exponent theorem removes the possible
extra factor two, add the `n=12,14` local products, write independently phrased
English and Chinese abstracts with six keywords each, and add compact data,
ethics, contribution, conflict, funding, and AI-use declarations.  The CJK
addition changed the engine to LuaLaTeX.  Manual CJK line breaks and removal of
font-incompatible microtype settings eliminated missing-glyph, layout, and
font-slot warnings.

## Final audit

The final package passes producer, full independent checker, SymPy, byte
replay, repaired-hash mutation, fixed-epoch double-build, embedded-font, clean
log, extracted-text, visual, scope, and manifest-closure checks.  The term
primary remains explicitly group-theoretic and is never promoted to an
arithmetic local or Euler factorization.
