import hashlib,json,pathlib
R=pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
D=R/'docs/papers204_208_sequence/reviews/p210_a'
F=R/'papers/210-weakly-increasing-run-aggregation/frozen_round0'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
expected='e8446cd17b1a283c74f9a6b4ced413b9e30810396c3d30f936ac2986ce790e26'
assert sha(F/'SHA256SUMS')==expected
rows=[]
for line in (F/'SHA256SUMS').read_text().splitlines():
 h,name=line.split('  ',1);p=F/name
 assert sha(p)==h,(name,h,sha(p));rows.append(p)
assert len(rows)==493
assert set(rows)==set(p for p in F.rglob('*') if p.is_file() and p.name!='SHA256SUMS')|set(p for p in F.rglob('SHA256SUMS') if p!=F/'SHA256SUMS')
rows.append(F/'SHA256SUMS')
(D/'INPUT_PINS.sha256').write_text(''.join(sha(p)+'  '+str(p.relative_to(R))+'\n' for p in sorted(rows)))
print(json.dumps({'status':'PASS','frozen_payloads':493,'input_pins':len(rows),'freeze_seal':expected,'semantic_author_checker_read':False},sort_keys=True))
