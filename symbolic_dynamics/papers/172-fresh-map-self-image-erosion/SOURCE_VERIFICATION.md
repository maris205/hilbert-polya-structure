# Source verification and owner subtraction — P172

**External state:** `HOLD_EXTERNAL`  
**Interpretation:** a direct source removes credit; a query miss adds none.

## Verified primary controls

| Source | Verified record | What is assigned zero credit |
|---|---|---|
| Zubkov and Serov, *Limit theorem for the size of an image of subset under compositions of random mappings*, 2017, DOI `10.4213/dm1403` | Math-Net/publisher DOI metadata and Crossref BibTeX | the ordinary random-image size process and its asymptotics |
| Flajolet and Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989 proceedings, DOI `10.1007/3-540-46885-4_34` | Springer DOI/Crossref record | the random-mapping carrier and standard mapping statistics |
| Hoffman, Jenkins, and Roughgarden, *On a Game in Directed Graphs*, *Information Processing Letters* 83(1), 13--16 (2002), DOI `10.1016/S0020-0190(01)00309-X` | Elsevier/ScienceDirect record, IBM Research record, and author-hosted manuscript | successive-elimination and leader-election vocabulary in which selected endpoints are removed |
| Charalambides, *On Weighted Stirling and Other Related Numbers and Some Combinatorial Applications*, *The Fibonacci Quarterly* 22(4), 296--309 (1984), DOI `10.1080/00150517.1984.12429864` | journal volume index, primary journal PDF, and DOI/Crossref BibTeX | specified-cell occupancy and required-box inclusion--exclusion |
| O'Neill, *Three Distributions in the Extended Occupancy Problem*, *Methodology and Computing in Applied Probability* 25, article 84 (2023), DOI `10.1007/s11009-023-10053-y` | Springer version of record and DOI/Crossref BibTeX | the extended-occupancy mass function, noncentral-Stirling formulation, and its generic transition/spectral treatment |
| Fitzsimmons and Pitman, *Kac's moment formula and the Feynman--Kac formula for additive functionals of a Markov process*, *Stochastic Processes and their Applications* 79(1), 117--134 (1999), DOI `10.1016/S0304-4149(98)00081-7` | Elsevier/ScienceDirect metadata and DOI/Crossref BibTeX | generic marked-kernel/Feynman--Kac product machinery |

Classical Stirling surjection counts, finite triangular Markov chains,
Jordan normal form, and generic hitting-time identities are also background.
They are reproved only where needed for a self-contained literal result.

## Exact occupancy subtraction

For a current set of size `a>=1`, regard its `a` labels as specified cells and
the other `n-a` labels as fall-through outcomes.  In O'Neill's notation the
whole unmarked size row is exactly

```text
Q_ab = Occ(b | a balls, a bins, theta=a/n)
     = n^(-a) (a)_b S_nc(a,b;n-a).
```

Equivalently, the fixed-target required-box count is

```text
N_ab = sum_{j=0}^b (-1)^j binom(b,j) (n-a+b-j)^a.
```

Accordingly the ordinary row law, this inclusion--exclusion, its
noncentral-Stirling rewrite, and generic occupancy spectral algebra receive
zero contribution credit.  The empty row is separately `Q_00=1`; it is not
forced into O'Neill's parameterization, which assumes positive bin count and
`theta>0`.  O'Neill's process evolves by adding balls to a
fixed occupancy experiment; it does not supply P172's state-dependent
iteration `A <- A intersect f(A)`, every-labelled-target history lift, or
terminal Jordan collision.  The retained marked axis is the literal
fixed-endpoint/total-image refinement `H_n(a,b;k)` and its coefficientwise
history lift, not the standard polynomial-kernel multiplication itself.

The Hoffman--Jenkins--Roughgarden game is a structural neighbour, not a
literal owner of the stated chain.  In one of its simultaneous rounds, every
active vertex selects an outgoing target and selected targets are eliminated;
the survivors therefore have zero indegree.  P172 instead retains active
labels hit by at least one source, hence positive-indegree labels, and samples
each new map from the active source into the fixed ambient set `[n]` rather
than using the induced current graph.  This distinction is recorded to
prevent a terminology-dependent owner-search blind spot, not to claim
novelty.

## Internal firewall

| paper | shared shell assigned zero credit | nontransferable P172 residue |
|---|---|---|
| P158, cut-intersection collapse | nested random intersection, labelled endpoints, absorption | graph-cut masks and cut-history fibres do not give specified-bin image occupancy |
| P162, random-translation intersection | `A intersect random-transform(A)`, stabilizer recovery, absorption | invertible group translations and coset/stabilizer geometry do not give a noninvertible endomap image fibre |
| P170, random-permutation fixed-point sieve | subset erosion, size quotient, marked histories | permutation fixed sets and cycle marks do not give the total image-size refinement |
| P173, random quotient-leakage erosion | fresh ambient maps, nesting, small quotient, every-target lift, triangular spectra, Jordan recursion, absorption | quotient-kernel injectivity and a complementary-dimension Jordan ladder do not give P172's specified-box/Stirling fibre or its single terminal `J_2` |

Thus nesting, quotient construction, symmetry recovery, triangular
eigenvalue reading, Jordan-recursion tactics, and absorption recursions all
earn zero separation credit.  P171 is also a literal noncollision: it uses
Boolean Gram feedback and ordered clique-cover fibres, not a resampled
endomap.

The only retained conjunction is the state-dependent self-image erosion,
the labelled endpoint/total-image refinement and its coefficientwise lift,
and the forced terminal `J_2`.  A source stating that conjunction or a proof
transfer from an occupied system is an immediate kill switch.  The current
search result is `BOUNDED_LITERAL_OWNER_NON_HIT`, not a novelty or
freedom-to-operate certificate.
