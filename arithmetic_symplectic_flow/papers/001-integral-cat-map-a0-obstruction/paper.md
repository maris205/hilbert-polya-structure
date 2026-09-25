# Integral cat-map suspension: a scoped obstruction to A0

**Paper ID:** `001-integral-cat-map-a0-obstruction`  
**Candidate ID:** `ASFS-20260913-CAT01`  
**Date / status:** `2026-09-13; NEGATIVE`  
**Route state:** `A0 scoped FAIL; A1/A2 NOT EVALUATED; formal Route A UNASSIGNED; Route B NOT INVOKED`

## Abstract

We freeze the suspension over \(F([v])=[Av]\) on \((\mathbb T^2,dx\wedge dy)\), where \(A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\) and \(\tau\equiv1\). Its proposed arithmetic source is the integral lattice action and congruence reductions. The object is coherent, but the allowed data contain neither a prime-selection rule nor a derivation of logarithmic time. Label, roof-scale, ownership, and `PROVES_TOO_MUCH` controls show that apparent prime correspondence is analyst-supplied. This is a scoped A0 failure, not a no-go theorem for other candidates. No A1/A2, zero-match, or Route-B work is performed.

## 1. Candidate identity and same-object ledger

The exact object and owners are frozen in [candidate-card.md](candidate-card.md). No symbolic clock, orbit catalogue, determinant, or operator from another object is used. The three-dimensional suspension is not claimed Hamiltonian.

| Item | Frozen definition / owner | Status |
| --- | --- | --- |
| Base | \((\mathbb T^2,dx\wedge dy)\), \(F([v])=[Av]\) | `FROZEN` |
| Clock / flow | \(\tau\equiv1\), \(M_\tau\), \(\varphi^u\) | `FROZEN` |
| Arithmetic proposal | integral lattice and reductions modulo \(N\) | `AUDITED` |
| Coding / orbit ledger | none used | `NOT EVALUATED` |
| Transfer object | none used | `NOT CONSTRUCTED` |
| Future quantum owner | none | `DEFERRED` |

## 2. Question and claim boundary

Can the integral/congruence structure of this roofed suspension produce \(p\leftrightarrow\gamma_p\) and \(T_{\gamma_p}\approx\log p\), without importing primes, their weights, or logarithms? The strongest supported answer is **no for this frozen proposal**. Integrality yields algebraic/congruence data, but no internally distinguished prime-indexed orbit family or logarithmic clock. No claim is made about every integral symplectic map.

## 3. Inputs and method

The sole inputs are the displayed matrix, torus, form, Haar measure, and constant roof. Iterates \(A^n\) are integral and reductions modulo every \(N\ge2\) are defined on \((\mathbb Z/N\mathbb Z)^2\). The lock excludes prime lists, \(\log p\), von Mangoldt weights, zero data, and fitted parameter choices. We make an exact dependency audit: does a rule built only from the allowed data (i) name primes, (ii) distinguish a prime-labelled orbit from an arbitrary labelled orbit, and (iii) generate a logarithmic clock? A mechanism fails when association appears only after an external label or arbitrary enumeration is inserted.

The direct identity \(A^TJA=(\det A)J=J\) proves the symplectic base check, and \(\inf\tau=1\) proves the required non-Zeno clock. Neither fact establishes arithmetic relevance.

## 4. Results

One may study reductions at prime moduli, but choosing those moduli already imports a prime selector. Letting \(N\) range over all integers does not make primes intrinsic to the dynamics. For a base orbit that later closes after \(n\) returns, the frozen roof gives elapsed time exactly \(n\); neither \(A\) nor \(\tau\) contains a rule yielding \(\log p\). Declaring \(n=\lfloor\log p\rfloor\), or selecting an orbit after consulting \(p\), violates the allowed-data lock. Thus the proposed source fails A0.

## 5. Controls and adverse findings

| Control | Test | Finding |
| --- | --- | --- |
| Arithmetic labels | Shuffle labels, use composites only, or density-matched integers. | The dynamics creates no labels and cannot distinguish primes. |
| Roof scale | Replace \(\tau=1\) by \(\tau=c>0\) with the same base. | Times become \(cn\); no internal logarithmic normalization is selected. |
| Ownership | Try a symbolic clock or borrowed determinant. | It changes the owner and is inadmissible. |
| `PROVES_TOO_MUCH` | Pair prescribed data with arbitrary orbit enumeration. | The same external pairing works for nonprime data, exposing the absent mechanism. |

This is structural rather than statistical: no finite cutoff or precision choice could repair it without changing the candidate.

## 6. Gate assessment

| Gate | Evidence | Status | Next obligation |
| --- | --- | --- | --- |
| A0 | Dependency audit and controls | `SCOPED FAIL` | Stop; a new source requires new P0. |
| A1 | Not reached in A0 → A1 order | `NOT EVALUATED` | No orbit result is implied. |
| A2 | No analytic object constructed | `NOT EVALUATED` | Do not borrow a determinant. |
| Formal Route A | No formal evaluation | `UNASSIGNED` | Not inferred from this audit. |
| Route B | No entry condition or authorization | `NOT INVOKED` | Deferred. |

## 7. Conclusion and decision

`ASFS-20260913-CAT01` is a coherent suspension over a concrete symplectic map, but its proposed arithmetic source fails A0. The same-object ledger stayed intact: nothing was borrowed to compensate for the failure. The candidate is **stopped**. The next authorized choice is to retain it as a negative control or fork a new P0 candidate whose endogenous arithmetic source, clock, and orbit-selection rule are all fixed before an A0 claim.

## Reproducibility / evidence index

See [evidence/README.md](evidence/README.md), [candidate-card.md](candidate-card.md), and [claim-ledger.md](claim-ledger.md). There are no computations to rerun.
