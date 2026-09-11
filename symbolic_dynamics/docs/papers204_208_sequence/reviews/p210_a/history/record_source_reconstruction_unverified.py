"""UNVERIFIED RECONSTRUCTION of original launcher source; DO NOT EXECUTE.

Original pre-execution source hash is unavailable, so this recreation is not
authenticated original evidence. Remaining text follows the original patch.
"""
import hashlib,json,os,pathlib,subprocess,sys,time
D=pathlib.Path(__file__).resolve().parent
name=sys.argv[1]
out=D/'execution'/name
out.mkdir(parents=True,exist_ok=False)
cmd=sys.argv[2:]
def put(n,v):
 (out/n).write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
put('ATTEMPT.json',{'argv':cmd,'cwd':str(pathlib.Path.cwd()),'environment':dict(os.environ),'start_ns':time.time_ns(),'scope':'A artifact launcher, not scientific code'})
with (out/'stdout').open('xb') as a,(out/'stderr').open('xb') as b:
 p=subprocess.run(cmd,stdout=a,stderr=b,check=False)
receipt={'native_returncode':p.returncode,'end_ns':time.time_ns(),'stdout_sha256':hashlib.sha256((out/'stdout').read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((out/'stderr').read_bytes()).hexdigest()}
put('RESULT.json',receipt)
print(json.dumps({'output':str(out),'result':receipt},sort_keys=True))
raise SystemExit(p.returncode)
