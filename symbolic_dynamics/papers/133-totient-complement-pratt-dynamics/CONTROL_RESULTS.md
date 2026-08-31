# Control results

## Fresh independent verifier

Run on 2026-08-31 UTC from the repository root:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

Result: `cmp` status `0`.

```text
TOTAL_STATES=226
TOTAL_TARGETS=226
TOTAL_ASSERTIONS=4774
EXACT_ARITHMETIC=python_integers
FLOATING_POINT=none
SAMPLING=none
STATUS=PASS
```

| lane | vertices | sources | height | states | recurrent | cycles | max tail | image | max fibre | assertions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| singleton | 1 | 1 | 0 | 2 | 2 | 1 | 0 | 2 | 1 | 33 |
| chain5 | 5 | 1 | 4 | 32 | 2 | 1 | 3 | 8 | 10 | 655 |
| mixed6 | 6 | 2 | 4 | 64 | 4 | 2 | 4 | 17 | 8 | 1,419 |
| disconnected7 | 7 | 4 | 3 | 128 | 16 | 8 | 2 | 25 | 8 | 2,667 |

## What is checked

- literal integer gcd/totient update versus the support map at every state;
- complemented AND--NOT coordinates;
- source-depth computation and the nonsharp `h+1` entry bound;
- both phases of the explicit decoder and equality with the literal
  recurrent set;
- consecutive-coordinate exclusion and the two-step erasure identity;
- every target's literal fibre versus the inclusion--exclusion formula,
  including zero fibres;
- fibre nonnegativity and total mass.

Finite enumeration is a falsifier only.  It does not prove the
all-parameter theorem or support novelty/priority.

## Pinned hashes

```text
841ed6f77091e0d0e6721c24dc334891f8bc3b54701717153da49ecbb391262a  code/verify.py
1c90aea14a3c45d084ec9cd6d86e951d3508494d94fa04afa6bd6ec12692b99d  code/verification_output.txt
3f62efbd5a23a5a0a811e92f4f975ba643cd4262b958c6c6ab0804920f602835  main.tex
3311a309139704fb8712bb152895ce5dec7e0ddbe087d44e4a20504976b83e2d  references.bib
bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b  main_round0_original.pdf
```

External status: `HOLD_EXTERNAL`.
