# Paper 13 closed-world exact audit package

This directory contains the pre-execution implementation for the single
candidate `henon_primitive_cycle_cover_v1`.  It is a bounded exact-arithmetic
falsifier/certificate package under external source-proof authority.  It does
not create a theorem verdict and it is not an official result.

The two scientific roots are deliberately separate:

- Track Q uses cyclic-equation quotient reduction, standard monomials,
  Reynolds averaging, and direct derivative-matrix multiplication.
- Track R uses a separately implemented sparse coefficient ring, Sylvester
  elimination with fraction-free determinants, Fitting matrices, and
  top-exterior records.

The tracks import no project helper.  They share only the JSON files in
`candidate_v1/shared`, which contain definitions and types but no expected
scientific value, source/review path, acceptance vector, or algorithm.  Each
track owns an input-only private fixture.  Scientific children are launched
with `python -I -S -B`, receive a hash-bound capability through file descriptor
3, and install an audit hook that denies source/review/ledger paths, the other
track, network/process/loader capabilities, and writes outside private
staging.

## Safe pre-execution sequence

From `papers/13-henon-primitive-cycle-cover`, with caches disabled:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B -m pytest -p no:cacheprovider code/tests \
  --junitxml=preexecution/junit.xml
PYTHONDONTWRITEBYTECODE=1 python -B code/scripts/run_safe_preflight.py
PYTHONDONTWRITEBYTECODE=1 python -B code/scripts/freeze_code_manifest.py
```

This sequence runs source/AST controls, mutation-sensitive endpoint tests,
one-shot lifecycle tests in temporary directories, and real isolated
capability probes.  The probes do not load either scientific engine and do not
call `run_science`.  They also exercise descriptor-3 reuse/restoration and
bounded persistent child diagnostics.  The sequence must leave the observed
registered-audit count at zero and create no runtime claim, terminal, staging,
or result.

After those three preexecution artifacts are frozen, a fresh reviewer who did
not author this tree must inspect and bind them.  This implementation is
complete but inert pending that independent deployment record.  Development
does not create a deployment disposition, durable claim, registered run,
official result, figure, or manuscript.

## One-shot boundary

The sole registered entry is `scripts/run_registered_once.py`.  If and only if
the runtime tree is absent, it freshly revalidates the bound source/review,
JUnit, preflight, code manifest/tree, deployment record, ledger, definitions,
and both track bindings; creates the durable claim; and immediately hands the
claim to the single parent R100 transaction with sequential isolated Q and R
children.  Its per-track child cap is the frozen exact value 30 seconds and is
not a command-line tuning parameter.

The transaction seals Q to
`runtime/candidate_v1/staging/track_q/envelope.json`, releases the Q launch
handle, then opens R and seals it separately.  R has no read capability for Q
staging.  Full inbound bindings are rehashed after each track, and both staged
envelopes are re-read before adjudication.  After payload, raw result, result
manifest, and the exact preterminal runtime tree have all passed validation,
the lifecycle invokes a mandatory one-shot inbound guard.  That guard rehashes
the durable claim, source and review, code manifest and current code tree,
JUnit, preflight, deployment review, ledger, definitions, and both tracks'
runner, engine, and fixture files against the original prelaunch snapshot.
Only its exact bound receipt permits the lifecycle's immediately following
terminal commit; a missing, stale, unset, repeated, or mutated guard is a
terminal failure.  For any claim-postdating exception,
the lifecycle attempts and commits exactly one exclusive terminal when storage
durability permits, including bounded child stdout/stderr diagnostics.  A
persistent terminal directory-barrier failure is surfaced as
`CommittedTerminalDurabilityError` and never triggers a retry.  An existing
claim or terminal always forbids another attempt.  No retry loop, third engine,
fallback fixture, neighboring pair, parameter scan, or post-result repair
exists.  Safe tests exercise this orchestration with synthetic ledger-derived
records only; they never invoke the registered entry or `run_science`.
