"""Read-only discovery of post-observation changes within A-owned output paths."""
import gzip,hashlib,json,pathlib
D=pathlib.Path(__file__).resolve().parent
with gzip.open(D/'AUDIT_READS.json.gz','rt') as f:data=json.load(f)
rows=[]
for path,row in data.items():
 p=pathlib.Path(path)
 if p.is_relative_to(D):
  h=hashlib.sha256(p.read_bytes()).hexdigest()
  if h!=row['sha256']:rows.append({'path':str(p.relative_to(D)),'observed_sha256':row['sha256'],'current_sha256':h})
print(json.dumps({'role':'actual documentary read-ledger observations versus later owned-file state, not scientific input changes','changes':rows},sort_keys=True,indent=2))
