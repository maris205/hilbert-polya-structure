# Independent Stage-2 audit handoff

## Frozen scope

Audit only `/tmp/p50_toeplitz_stage2` against the immutable Stage-1 input
`/tmp/p49_53_phase1`.  Do not edit either directory.  Do not create a Git
repository, README, mirror, manuscript, figure, seal, authority record, or
publication artifact.  The package author must communicate the SHA-256 of
`SHA256SUMS.txt` out of band after declaring `STOP/frozen`; compare that
value before reading the proof.

The expected Stage-1 manifest SHA-256 is

```text
7fd51d53d077e3d7e0af905eda6bf2d15ee9aa64d6459bf3dcfa1dc282d97ec8.
```

## Gate 1: byte, file-set, and mode integrity

Run, without permitting Python bytecode:

```text
cd /tmp/p50_toeplitz_stage2
sha256sum SHA256SUMS.txt
sha256sum -c SHA256SUMS.txt
PYTHONDONTWRITEBYTECODE=1 python3 verify_manifest.py
cd /tmp/p49_53_phase1
sha256sum SHA256SUMS.txt
sha256sum -c SHA256SUMS.txt
```

`verify_manifest.py` must report `PASS`, the exact manifest digest supplied
out of band, and 13 listed package files.  Stop immediately on an added,
missing, changed, symlinked, nonregular, cache, bytecode, or mode-mismatched
entry.

## Gate 2: theorem-contract audit before evidence

Read `THEOREM_CONTRACT.md`, then check these restrictions literally.

- `p` ranges over every integer at least 3.
- For composite `p`, `nu_p` is called a divisibility exponent, never a
  `p`-adic valuation.
- Directives have exact support, least period at least 2, and unequal cyclic
  neighbors.
- Factor maps are continuous, onto, shift commuting, same-base, and pointed
  at the displayed Toeplitz points.
- Cross-base and nonpointed maps are nonclaims.
- Graph counts refer to fixed-source target classes modulo pointed
  conjugacy, not labeled maps.

Any silent weakening of a hypothesis or widening of a conclusion is a
contract failure.

## Gate 3: proof audit independent of the computations

Read `PROOF_PACKAGE.md` without using the JSON evidence to fill a gap.  In
particular verify each of the following.

1. `(p-1)k+1` is nonzero for every integer coordinate.
2. The exact hole is `r_N+p^N Z`, and the argument excludes **every** point
   of that class from `Per_{p^N}`, not only its preferred representative.
3. Essentiality follows from the least period of the one-hole skeleton;
   aperiodicity follows simultaneously for all `N`.
4. The one-hole recursion has no residual ordinary integer.
5. In the prime constructive lower bound, every
   `1<=q<p^(N+1)` is handled at `r_{nu_p(q)}`, and the modular inverse is used
   only because `p` is prime.
6. In the composite lane, `q=ell*p^N` preserves every position of `B_N` for
   every `t in Z`, including the unique exponent-`N` position.
7. The high-center identity remains valid for composite `p` without
   pretending that `j/p^e` is a unit modulo `p`.
8. Curtis--Hedlund--Lyndon supplies an arbitrary finite radius; high-center
   windows remove the contextual dependence; directive periodicity extends
   the large-index relation to all phases; pointed orbit density extends
   equality from the basepoint to the whole source subshift.
9. Exact target support forces the letter map to be surjective and also
   makes it unique.
10. Kernel partitions are admissible exactly when every block is independent
    in the cyclic adjacency graph; quotient words are reduced to least
    period; refinement has the stated arrow direction.
11. The graphical Stirling and chromatic formulas count the promised
    equivalence classes and no broader objects.

The factor theorem must stand even if every finite local-rule result is
deleted.

## Gate 4: independent implementation reproduction

Use an auditor-controlled temporary output directory so that the frozen
package is not rewritten.  From the package directory, run a command of the
form

```text
audit_output=$(mktemp -d /tmp/p50_toeplitz_audit.XXXXXX)
PYTHONDONTWRITEBYTECODE=1 python3 run_stage2.py \
  --stage1 /tmp/p49_53_phase1 \
  --output "$audit_output"
cmp evidence/input_hashes.json "$audit_output/evidence/input_hashes.json"
cmp evidence/canonical_evidence.json "$audit_output/evidence/canonical_evidence.json"
cmp evidence/test_results.json "$audit_output/evidence/test_results.json"
```

Remove the auditor-owned temporary directory only under the auditor's own
cleanup policy.  The expected result is nine passing assertion groups and
the following anchor counts:

```text
point comparisons                         68,288
skeleton cases / residue classes          32 / 28,764
high-center identities                    1,920
prime smaller periods rejected            3,918
composite direct / nested comparisons      998,025 / 99,519
directives / partition checks              44 / 477
admissible partitions                      112
chromatic evaluations                      308
bounded local cases                        972
consistent / quotient cases                132 / 132
false positives / false negatives          0 / 0
typed negative controls                    4
```

The frozen evidence hashes are

```text
620c53d713d91c74ac1519d7bce259b0728c043d383e5b13adff8cc44dd14bc0  input_hashes.json
b6e7f69ca360680c21bf3d772d79ceeb543f1cb8a82d236a647206df8781c74b  canonical_evidence.json
99ee0fb200903772944ec05897af21ae4126bedd1df08fab6cae4bdf46772963  test_results.json
```

Check that the two modules do not import one another and that their core
evaluators really use affine divisibility versus nested hole filling.

## Gate 5: independent nearest-owner search

Start with the primary-source quantifiers in `SOURCE_LOCK.md`, especially:

- DKL (1995), Theorem 1, for same-period over-zero aligned `t`-symbol maps;
- Hosseini--Yassawi, Section 2.2.1 and Theorem 1.1, for constructive period
  structures and the pure-power divisibility obstruction;
- Sell--Sieron for updated separated-hole/factor context;
- simple-Toeplitz, finite-rank/S-adic, substitution-factor, and Toeplitz
  automorphism neighbors listed there.

Search full text for the conjunction of explicit affine family, same-base
pointed maps, arbitrary-radius collapse to a unique letter quotient, and
the independent-set partition poset.  An exact owner is an
`EXACT_COLLISION`; stop rather than redescribe it as incremental novelty.
Absence from a bounded search permits only the same bounded wording, never
an absolute priority sentence.

## Audit decision rules

- A proof counterexample, quantifier gap, stale hash, nondeterministic
  reproduction, or source collision is a blocker and must be reported with
  an exact witness.
- A finite search miss is not a proof counterexample unless the purported
  rule is actually valid on the full subshift.
- A broader cross-base or nonpointed example is not a counterexample to the
  frozen theorem, but any package sentence claiming to cover it is a scope
  defect.
- Passing all gates means only that a later authority may decide the next
  step.  It does not itself authorize a paper or public write.

Package handoff status:

```text
HOLD_FOR_INDEPENDENT_STAGE2_AUDIT
```
