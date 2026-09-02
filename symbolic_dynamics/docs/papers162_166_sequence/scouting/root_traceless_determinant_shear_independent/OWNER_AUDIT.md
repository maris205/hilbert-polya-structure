# Traceless determinant shear — public owner audit

**Gate result:** `KILL_CONJUGATE_TO_CLASSICAL_ARTIN_SCHREIER_LINEAR_MAP`  
**Search date:** 2026-09-03  
**Lifecycle:** `HOLD_EXTERNAL`

The search was bounded and used public primary/publisher records.  A non-hit
for the exact matrix notation is not novelty evidence.  In this case the kill
does not depend on finding the literal string in print: an explicit bijection
reduces the whole map to an owned linearized-polynomial functional graph.

## 1. Literal-map searches

Queries included:

```text
"A + det(A) I" matrix finite field characteristic 2 dynamics
"traceless determinant" "x^2+x" finite field matrix
"determinant shear" finite field
traceless matrix determinant Artin-Schreier characteristic two
functional graph Artin-Schreier map x^2+x finite fields
functional graph linearized polynomial finite field
linear map finite field primary decomposition preperiod cycle
```

No public result defining this exact matrix wrapper was located.  That
bounded literal non-hit is immaterial because

```text
H([[a,b],[c,a]])=(b,c,a^2+bc)
```

is a bijection and conjugates the proposed map to
`(b,c,e)->(b,c,e^2+e)`.

## 2. Directly controlling owner literature

### General finite-field linear functional graphs

Daniel Panario and Lucas Reis, *The functional graph of linear maps over
finite fields and applications*, Designs, Codes and Cryptography 87 (2019),
437--453,
[DOI 10.1007/s10623-018-0547-5](https://doi.org/10.1007/s10623-018-0547-5),
studies functional graphs induced by linearized polynomials and extracts
cycle/preperiod information from the associated polynomial/module data.
This is the direct methodological owner for reducing a finite-field linear
map to cyclic/primary polynomial factors.

Joachim von zur Gathen, Michael Giesbrecht, and Konstantin Ziegler,
*Composition collisions and projective polynomials*, and the broader
linearized-polynomial algebra are not needed for the kill.  A directly
inspected modern primary reference is Baofeng Wu and Zhuojun Liu,
*Linearized polynomials over finite fields revisited*,
[arXiv:1211.5475](https://arxiv.org/abs/1211.5475), which records the
finite-field linear-transformation interpretation and composition algebra of
linearized polynomials.  The present `D(x)=x^2+x` is one of the elementary
members of that class.

Stephen D. Cohen and Dirk Hachenberger, *The dynamics of linearized
polynomials*, Proceedings of the Edinburgh Mathematical Society 43 (2000),
113--128,
[DOI 10.1017/S0013091500020733](https://doi.org/10.1017/S0013091500020733),
is further primary evidence that iteration and periods of linearized
polynomials are an established dynamical subject.  Its carrier question is
not identical to the present element map, so it is supporting neighborhood
evidence rather than the sole kill source.

Lucas Reis, *Nilpotent linearized polynomials over finite fields and
applications*, Finite Fields and Their Applications 50 (2018), 279--292,
[DOI 10.1016/j.ffa.2017.12.005](https://doi.org/10.1016/j.ffa.2017.12.005),
develops nilpotent/invertible linearized-polynomial structure and cycle
interfaces.  Again, the gate does not need a claim that this paper states the
specific `D` formula verbatim; primary decomposition already transfers the
entire proposed contract.

## 3. Mandatory zero-credit boundary

The task explicitly assigns zero credit to generic Frobenius and
Artin--Schreier facts.  The following are therefore all owned inputs:

- `F(x)=x^2` is the Frobenius automorphism of `F_{2^m}`;
- `D=F+I` is an `F_2`-linearized polynomial;
- `im D=ker Tr` and `ker D=F_2`;
- normal-basis/cyclic-module representation of Frobenius;
- primary decomposition into nilpotent and invertible parts;
- image and kernel cardinalities of powers of a finite linear map;
- fixed-point counts from polynomial gcds;
- cycle counts from Möbius inversion;
- copying a functional graph by two passive coordinates.

Once the full conjugacy is known, every claimed forward/inverse statistic is
on this list or is a one-line specialization of it.

## 4. Residual test after subtraction

| proposed axis | after full conjugacy and subtraction |
|---|---|
| determinant semiconjugacy | understates the bijective coordinate change; no residual |
| matrix iterate `A+R_t(D)det(A)I` | coordinate translation of the scalar linear iterate |
| tail `s=2^{v_2(m)}` | zero-primary exponent of `(z+1)^m+1` |
| recurrent and depth counts | `q^2` times the standard nilpotent/invertible decomposition |
| all-time images and uniform fibres | `q^2` passive copies of `im D^t` and `ker D^t` |
| trace criterion at time one | standard `im(x^2+x)=ker Tr` |
| fixed and exact-period counts | cyclic-module gcd plus Möbius inversion |
| recurrent-target exact ancestry | uniform power-kernel size |

No second matrix-sensitive theorem axis remains.  The determinant coordinate
does not lose information about `a`, so the proposed nonlinear wrapper does
not create a pullback problem, a nonuniform fibre, or a new target invariant.

## 5. Owner adjudication

The literal matrix notation is owner-thin, but the functional system is
owner-dense after conjugacy.  Under the gate's explicit rule that generic
Frobenius/Artin--Schreier structure receives zero credit, the correct result
is a value/ownership kill:

```text
KILL_CONJUGATE_TO_CLASSICAL_ARTIN_SCHREIER_LINEAR_MAP
```

This does not assert that a prior paper uses the name “traceless determinant
shear.”  It asserts the stronger mathematical fact that the named system is
isomorphic to a standard linearized-polynomial system and has no residual
conjunction after mandatory subtraction.
