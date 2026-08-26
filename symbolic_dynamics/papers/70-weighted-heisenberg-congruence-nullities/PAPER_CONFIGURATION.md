# Paper configuration

- **Internal identifier:** P70
- **Working title:** Weighted Three-Term Shifts on Finite Heisenberg Quotients
- **Article type:** short theoretical paper
- **Language:** English manuscript; separate Chinese abstract supplied
- **Authorship:** anonymous internal draft
- **Venue posture:** journal-neutral `amsart`, 11 pt, A4, short-note target 6--9 pages
- **Freeze date:** 2026-08-25 UTC
- **Official review status:** GPT-5.4/xhigh Rounds 1--2 complete; mathematical
  `PASS AS STATED` and package `PASS`; neither official review supplied a
  numeric score
- **Release status:** **HOLD -- Stage 2.5 specialist exact-statement source
  audit remains required**

## Theorem contract

Let `Gamma` be the discrete Heisenberg group and let `N_ell` be the normal
kernel of reduction modulo an odd prime `ell`.  For a prime `p != ell` and
nonzero `alpha,beta,gamma in F_p`, the paper proves the exact dimension of the
`N_ell`-fixed space of the linear group shift cut out by

```text
alpha*x_g + beta*x_(ga) + gamma*x_(gb) = 0.
```

The answer is the sum of two arithmetically different terms:

1. a cyclotomic torsion-intersection degree from the one-dimensional
   representations; and
2. a uniform `ell(ell-1)` jump on the Fermat locus
   `alpha^ell+beta^ell+gamma^ell=0` from the nonlinear representations.

The specialization `(alpha,beta,gamma)=(1,1,1)` recovers the Stage-1
characteristic-three jump but is not the full paper.

## Mandatory firewalls

- The exact element `1+a+b` and the principal Heisenberg-action framework are
  prior work and are cited as such.
- The finite-field shift is not conflated with the compact connected integer
  principal action.
- The proof freezes the right-convolution convention and checks how a switch
  to the dual convention permutes blocks without changing nullity.
- `p=ell` is excluded because Maschke semisimplicity fails.
- Finite matrices are regression evidence, not proof premises.
- A bounded source search is not a priority certificate; no “first” claim is
  authorized.
- The official convention/proof audit is closed. This does not close the
  separate worldwide exact-source/priority gate.
