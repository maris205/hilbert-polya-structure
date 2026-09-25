# Document verification — ASFS-SCOUT-20260919-PSR01

Date: 2026-09-19. These are document-integrity checks, not proof certificates.
No numerical scientific calculation or independent orbit enumeration ran.

## Historical preservation

The 18 pre-notice SHA-256 values in [source-audit.md](source-audit.md) were
checked against the complete original byte remainder of each touched old
record. Every check passed. Only the dated notice prefix is new in those
18 files; no underlying frozen definition or historical paragraph was changed.

Reproduce from the arithmetic_symplectic_flow working directory:

```python
from pathlib import Path
import hashlib, re
root = Path.cwd()
audit = root / 'papers/266-prime-source-return-rescreen/evidence/source-audit.md'
entries = re.findall(
    r'^\| ((?:0(?:78|79|80|81|82)|240)-[^|]+?) \| ([0-9a-f]{64}) \|$',
    audit.read_text(), re.M)
assert len(entries) == 18
for rel, expected in entries:
    raw = (root / 'papers' / rel).read_bytes()
    assert raw.startswith(b'<!-- PSR01 CORRECTION NOTICE START -->\n')
    old = raw.split(b'<!-- PSR01 CORRECTION NOTICE END -->\n\n', 1)[1]
    assert hashlib.sha256(old).hexdigest() == expected, rel
print('PASS: 18 historical byte remainders unchanged')
```

The original successful check also printed all 18 exact paths. This check
does not establish that unrelated repository changes predate the current
turn; no broad worktree reset or normalization was performed.

## Links, status and whitespace

Check local Markdown targets in the new package and all 18 correction
records, plus the new266 link in each registry. Exclude external HTTP(S)
links and fragment-only links from filesystem existence checks; primary
source accessibility was separately verified in source-audit.md. Check
the common scope ID/status in the new paper, card, ledger, package summary
and both registry entries, and each corrected candidate's ID/status in
its card/paper/ledger/summary. No automated test decides mathematical truth.

The changed-path `git diff --check` completed with exit0 and no output.
No staging, commit, push, broad rewrite or removal was performed.

Recorded results: 27 Markdown files checked (9 new-package files plus the
18 notice-bearing historical records), 102 local links including the two
new registry entries, zero missing targets. All6 scope ID/status checks
and all12 corrected-owner ID/status checks passed. These are scoped checks,
not a claim to have validated every link in the long historical registries.

## Independent review

The [review](independent-review.md) records a separate initial derivation
from raw definitions and the primary theorem, then synthesis/final-draft
checking. Its final hashes bind the reviewed inputs. It is model review,
not external peer review. The correction's substantive input did not change
after the mathematical audit; final readback covers metadata and notices.
