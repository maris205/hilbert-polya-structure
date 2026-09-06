# P208 actual author execution evidence

Status: AUTHOR_EXECUTION_PASS, not independent manuscript review.
All production remained on the predeclared complete n=3,...,10 carriers.

## Actual commands and full stdout

Executed from this paper directory using the reviewed recorder:

```
python3 -I -B record_author.py initial initial_01
python3 -I -B record_author.py pair pair_01
```

Each of the three actual source-only producers passed 62,101 assertions
on all 2,055 states. The initial producer wrote CANONICAL.json exclusively
from its complete stdout. Each of the subsequent two producers compared
against that canonical using actual /usr/bin/cmp; a third raw cmp compared
the two fresh outputs. All three pair comparison exits were zero, with
empty stdout/stderr. This is raw byte equality, not normalized JSON equality.

- [Initial receipt](qa_author/initial_01/RECEIPT.json)
- [Fresh pair receipt](qa_author/pair_01/RECEIPT.json)
- [Full canonical output](CANONICAL.json), 4,974,397 bytes
- [Pre-execution scope](VERIFICATION_SCOPE.md)

Verifier SHA-256: 12653e9025931fa9424bf06aef7c7f40ffb9a47f95df6bf5dd5b5a50ca57578b.
Canonical SHA-256: d4667d1b9be183993f48a49a5fda51f5a519cb29a473d2dbd680caa33c8ab395.

The canonical contains every tree/labelled diagonal set, next state,
entrance, complete decoded predecessor set, K next state and K entrance,
along with whole-carrier summaries and the full sharp-witness orbit.
The original author code is preserved in provenance/ and is not described
as an independent representation. The candidate gate implementation is
neither imported nor copied.

## Actual input and runtime closure

Each source-only directory initially and finally contained exactly its
copied verify.py. Complete current paper-source/documentary inputs were
physically snapshotted outside the run directories and hashed before/after.
The only allowed initial-production addition was CANONICAL.json; the fresh
pair changed no captured input. Receipt status explicitly requires the
expected producer count, positive parsed assertion counts, unchanged copied
source and inputs, successful child exits and no validation exception.

Actual interpreter: /root/miniconda3/bin/python3.12, Python 3.12.3,
Anaconda build, GCC 11.2.0. Probes record optimize=0, isolated=1,
dont_write_bytecode=true, safe_path=true, no_user_site=1, no_site=0.
PYTHONHASHSEED=0 is present in the recorded controlled environment, but
-I sets ignore_environment=1 and hash_randomization=1; no disabled-randomization
claim is made. The producer's sorted/ordered output is deterministic under
the actual isolated runtime. Every file-backed module loaded by the
same-import runtime probe, including startup modules, has an actual origin
and SHA-256. Before/after raw runtime probe outputs compare equal.

Interpreter, recorder, comparator, dynamic resolver and resolved shared
library bytes were unchanged. Complete ldd output is retained; ASLR addresses
are not compared as stable bytes, but resolved-library hashes are. This
records the actual runtime, not a hermetic or historical OS reconstruction.

All initial and pair producer/probe/comparator commands exited zero; no
numerical failed attempt occurred in this paper-local production. Original
scouting/gate failures remain untouched in their own packages. Source pins
are pre-execution, not retroactive pre-first-read pins. The later summary
reports and fixed author manifest are documentary outputs explicitly
excluded by the recorder, not hidden scientific input changes.

The all-parameter theorems are established by the written proof. These
finite checks neither prove arbitrary n nor replace the required A/B reviews
or root's independent fresh replay pair.
