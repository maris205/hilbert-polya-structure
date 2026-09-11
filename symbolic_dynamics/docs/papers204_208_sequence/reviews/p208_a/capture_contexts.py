"""Pin each named historical original before A's substantive history read."""
from pathlib import Path
import hashlib,json,time
ROOT=Path('/root/autodl-tmp/symbolic_dynamics')
OUT=ROOT/'docs/papers204_208_sequence/reviews/p208_a'
GATE=ROOT/'docs/papers204_208_sequence/scouting/OFS_GATE'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
paths=[GATE/'SOURCE_AND_PROOF.md',GATE/'HISTORY_PINS.sha256',GATE/'INPUT_PINS.sha256']
for name in ('HISTORY_PINS.sha256','INPUT_PINS.sha256'):
    for line in (GATE/name).read_text().splitlines():
        _,rel=line.split('  ',1);paths.append(ROOT/rel)
origins=ROOT/'docs/papers204_208_sequence/qa/p208_round0_input_inspection_v2/historical_workspace_origins'
paths += [p for p in origins.rglob('*') if p.is_file()]
paths += [ROOT/'docs/papers204_208_sequence/FINAL_THEOREM_CONTRACTS.md']
payload={str(p.relative_to(ROOT)):sha(p) for p in sorted(set(paths))}
(OUT/'HISTORY_CONTEXT_PINS.sha256').write_text(''.join(f'{h}  {p}\n' for p,h in payload.items()))
(OUT/'HISTORY_PIN_RECEIPT.json').write_text(json.dumps(dict(time_ns=time.time_ns(),count=len(payload),
    chronology='Captured after frozen manuscript/author code read, before substantive nonfrozen history/candidate-source read. Candidate manifest listings were already read.',
    recorder_sha256=sha(Path(__file__)),pins_sha256=sha(OUT/'HISTORY_CONTEXT_PINS.sha256')),indent=2)+'\n')
print('PINNED',len(payload))
