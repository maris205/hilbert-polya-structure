"""Original minimal native subprocess receipt, confined to reviewer output."""
import hashlib,json,os,pathlib,subprocess,sys,time
D=pathlib.Path(__file__).resolve().parent
name=sys.argv[1]
out=D/'execution'/name
out.mkdir(parents=True,exist_ok=False)
cmd=sys.argv[2:]
def put(n,v):
 (out/n).write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
safe={'PATH','LANG','LC_ALL','LC_CTYPE','TZ','LD_LIBRARY_PATH','LIBRARY_PATH','OMP_NUM_THREADS','MKL_NUM_THREADS','PYTHONHASHSEED','PYTHONPATH','PYTHONDONTWRITEBYTECODE','PYTHONOPTIMIZE'}
put('ATTEMPT.json',{'argv':cmd,'cwd':str(pathlib.Path.cwd()),'environment':{k:v for k,v in os.environ.items() if k in safe},'omitted_launcher_environment_keys':sorted(set(os.environ)-safe),'environment_scope':'Relevant launcher settings only; complete explicit child scientific/build environment is in capsule CONTEXT and command ATTEMPT records. Sensitive platform fields omitted.','start_ns':time.time_ns(),'scope':'A artifact launcher, not scientific code'})
with (out/'stdout').open('xb') as a,(out/'stderr').open('xb') as b:
 p=subprocess.run(cmd,stdout=a,stderr=b,check=False)
receipt={'native_returncode':p.returncode,'end_ns':time.time_ns(),'stdout_sha256':hashlib.sha256((out/'stdout').read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((out/'stderr').read_bytes()).hexdigest()}
put('RESULT.json',receipt)
print(json.dumps({'output':str(out),'result':receipt},sort_keys=True))
raise SystemExit(p.returncode)
