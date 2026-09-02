# P156 — weak-excedance extraction

Status: **ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL**.

For `pi in S_n`, P156 retains the letters at weak-excedance positions
`pi_i >= i` and standardizes them.  The frozen paper package proves:

1. `sigma in W(S_n)` iff `n >= |sigma|+d(sigma)`, with explicit right
   sections at every admissible rank;
2. a Ferrers-board completion formula for every target fibre;
3. identity-only recurrence and strict rank drop; and
4. a canonical locally minimum inverse ray with resource update
   `(m,d)->(m+d,m)` and exact Fibonacci matrix powers.

“Locally minimum” means one-step minimum rank only.  The false pointwise
maximum-drop clock, the unproved global maximum clock, and global minimum rank
among all iterated preimages are explicitly excluded.

## Reproduce the exact control

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p156.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p156.py > /tmp/p156_replay.txt
cmp -s /tmp/p156_replay.txt verification_output.txt
```

The frozen run executes 3,689,489 exact assertions.  It includes 409,113
literal states through rank nine, 6,985 every-target fibre cells, 316,646
`n<m` boundary cells, all 46,233 same-rank cells, and six
right-inverse levels for all 46,225 nonidentity targets through rank eight.
It also reproduces the rank-11 counterexample delimiting the withdrawn clock.

## Rebuild

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` preserves the author freeze at SHA-256
`ee5cedd089d9d837839f9fc715aae9530e19fc4f414dfcbef77ad0adfafa256c`.
`main_round1.pdf` preserves the Review-A repair freeze.  The current
`main.pdf` and canonical `main_round2.pdf` are byte-identical, 4 A4 pages and
336,311 bytes, at SHA-256
`7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979`;
Round 1 has the same PDF bytes because Review B required only a ledger
correction.  Hostile Review A's two Minor findings and Hostile Review B's one
Minor finding are closed in `IMPROVEMENT_LOG.md`.  The mathematical source,
verifier, transcript, and PDF are unchanged in Round 2.  External posting,
circulation, contact, submission, and release remain unauthorized.
