# Paper improvement log

## Round progression

| Round | Categorical review verdict | Substantive theorem addition |
|---|---|---|
| 0 | PASS_WITH_REQUIRED_EXTENSION | all-level intersection, degree, exact finite image, and restriction maps |
| 1 | PASS_WITH_REQUIRED_EXTENSION | complete fixed-root spectrum, impossible multiplicities, Chebotarev densities, and limit |
| 2 | READY_FOR_DETERMINISTIC_RELEASE_GATES | inverse-limit image, all-iterate dictionary, exact evidence, finite Koopman boundary, collision and Route-A closure |

Round 1 is not a repackaging of Round 0, and Round 2 is not a split fragment
of Round 1.  Each adds a new theorem layer and compiles from its own source.

## Review provenance

The reviews in `review/` are role-separated internal reviews produced in
the same Codex session.  They are neither scored nor presented as
independent human or cross-model reports.  Their purpose is to preserve
specific objections and corresponding changes.  Mechanical conclusions
are independently recomputed by executable lanes.

## Main corrections made

1. Exposed the nonsquare and fourth-power branches of Capelli's criterion.
2. Replaced finite-image guessing by the degree/cardinality proof.
3. Explained the missing four-root stratum through the conductor-eight
   character rather than an empty experimental bin.
4. Separated exact density from finite prime frequencies.
5. Assigned universal finite-permutation ownership to HCS-C12A.
6. Locked the target-analytic and Route-B nonclaims in prose, YAML, JSON,
   mutation tests, and the release gate.
7. Applied the strict v0.2 distinction between an exact fixed-root law and
   a complete arithmetic primitive-orbit layer; downgraded A1 to `A1_WEAK`
   and the overall status to `ROUTE_A_EXPLORATORY` without changing a
   mathematical theorem.
8. Added analytic basepoint-3 and exact full-affine-parent controls, plus an
   exact decomposition of 25 odd composites into five prime-power
   `Frob_p^r` repetitions and twenty mixed labels without a single-prime
   owner, while explicitly denying A0 credit to empirical density.
9. Added independently written English/Chinese abstracts with 5--7
   language-matched keywords and strict round-leak/CJK embedding gates.
10. Tightened A4 from an unearned stronger label to `A4_FORMAL_HINT`:
    finite basis-permutation unitarity is proved, while common time reversal,
    nontrivial phase/weight preservation, and a global Hamiltonian are not.
