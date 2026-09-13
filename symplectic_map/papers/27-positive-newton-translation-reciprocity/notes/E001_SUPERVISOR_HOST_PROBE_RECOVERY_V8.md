# E001 Supervisor Host-Probe Recovery Control V8

Status: INERT ASCII CONTROL AND INERT ASCII SOURCE TEXT ONLY. NO EXECUTION
AUTHORITY.

## 1. Exact E0346 authority and immutable inputs

This is the sole fresh Host V8 path authorized by ledger event E0346. It is
derived from frozen Host V7 only as inert text. No embedded record was
imported, language-parsed, compiled, evaluated, executed, or launched.

The exact authoring anchor is:

path=/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md
dev=2431
ino=12439253869
mode=0644
nlink=1
uid=0
gid=0
bytes=2036397
LF=21983
sha256=b5b39ba94477ce193e5ed24dd175fe2ac2132661e1b895fa52ee5c7792759066
terminal=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V8_UNSAT_SPECIFICATION_RECORDED_MINIMUM_PROGRESS_PREMISE_CORRECTED_AND_CONTROL_REAUTHORIZED

The qualified prospective-canonical manifest remains exactly 134 rows,
21535 framing bytes and sha256
3325e9afc341eb4ce669718da63bc1d79e892c00862c4898a5c185de8c59e52b.
The immutable malformed literal history remains non-authoritative; the exact
prospective R2 token remains
da719d459bb9fbcc925ef3c38adf5021af9a8961db82516cc416843ecd885106.

Frozen Host V7 is dev 2431, ino 5916160150, mode 0644, nlink 1, uid/gid 0/0,
174525 bytes, 2211 LF and sha256
07bf1c8a10e729b19acabc9576d6bfa35afb5bfede892b0fea61c3143cda6d91.
Its five frozen sources are respectively:

- outer 31738/378/154128e0d5e9651407bd4a173d093860084ed41a82306942c6c725e586dc8c73
- keeper 4701/81/4c1afb1d6c579399d10c6afaab65d5a0ad2d360b36af6f61a32e1a183c9029fd
- launcher 47403/526/0d4766bb183b0ea48fb08c4ee1b58a40c763ce8d1a1678b021ea1b06286d2471
- marker 58746/591/30803c2c35f4997655a90c0f3170163e4121593bbfdf1200c7bcd48c2fd5b651
- nested child 4701/58/9466953460a96da55bbb470b1cf5ef25f46fbc1f95540ada59a07a30e6221790

Frozen Host V6/V5/V4 identities remain respectively
166498/2074/90158178795619c3b5ac94cfc87b92246a5f68c51abaff8f0acbf15481c643ec,
164883/2052/8e5207770ad64300212260e4bf5604d75e6b4a36852efded632676d43cc84370,
and 147429/1801/238bff83783cedfe5193b735583a749271cca53af21b9a2f953904f6ee36ddeb.
Binder V8 remains 279288/7303 at sha256
3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4.

## 2. Corrected finite execution-domain premise

V8 binds these positive finite constants:

KILL_REAP_PROGRESS_NS=250000000
MAX_LIVE_SLOTS=4
TERM_ALLOWANCE_NS=100000000
SYSCALL_OVERHEAD_NS=50000000
PER_NONKEEPER_CLEANUP_NS=400000000
KEEPER_FINALIZATION_NS=300000000
DERIVED_CLEANUP_GUARD_NS=1500000000

The arithmetic is exact and overflow checked before the first spawn:

PER_NONKEEPER_CLEANUP_NS = TERM_ALLOWANCE_NS +
KILL_REAP_PROGRESS_NS + SYSCALL_OVERHEAD_NS = 400000000.

DERIVED_CLEANUP_GUARD_NS = (MAX_LIVE_SLOTS - 1) *
PER_NONKEEPER_CLEANUP_NS + KEEPER_FINALIZATION_NS = 1500000000.

The outer accepts TOTAL_NS only from 2000000000 through 10000000000 and
checks every addition and multiplication against 2^63-1. Work ends before
TOTAL_NS minus the derived guard. Cleanup creates a fresh guard from its own
start; an operational overrun always demotes and never disables cleanup.

The E0346 execution domain promises that, after a successful exact-PID
SIGKILL to an outer-owned leaf, within KILL_REAP_PROGRESS_NS the leaf becomes
waitable and the outer receives enough scheduling and syscall progress for
exact waitpid on that PID to return its raw status. It also promises that the
actor, ancestor and external supervisor do not terminate the outer from the
first successful child return until the registry has no live or unknown
slot. These are explicit premises, not observations. A signal return, EOF,
ACK, elapsed grace, parent exit, group absence or one successful run cannot
establish them.

## 3. Flattened ownership and closed broker

The outer is outside the child group and is the sole process creator and
wait owner. Launcher L, keeper K, marker M and each serial probe child C are
all direct outer children in group G=L. L, K, M and C are leaves: their
sources contain zero child-creation calls and zero child-wait ownership.
At most L, K, M and one serial C are simultaneously live, proving the bound
of four slots even for P10's sixteen sequential samples.

Marker requests use one strict ASCII line with exact ordered fields:

P27E001V8|broker=request|seq=0|probe=ID|op=OP|child_sha=H64

The closed OP set is P00_E2BIG, P01C_INFO, P05_WAIT, P08_TOPOLOGY,
P09_KILL, P10_INFO16 and P12_CHAIN. A partial, duplicate, late, reordered,
oversized or mismatched line creates no child. A complete accepted request
may create children only through the outer's single spawn_owned site. Its
response is emitted only after every child created for that request has an
exact returned PID/status and a reaped registry state.

Failure latches once and permanently closes broker admission. Cleanup scans
only the owning registry and orders roles child, marker, launcher, keeper.
Every live role receives exact-PID TERM where applicable, a bounded WNOHANG
grace, exact-PID KILL if still live, and a premise-bounded finite WNOHANG
exact reap. All non-keeper slots must be physically reaped before keeper K is
killed and reaped. There is no delivered group TERM or group KILL. Optional
group-zero ESRCH occurs only after the registry is empty.

## 4. Exact outer sole-owner and broker source

Invocation tail:

PROBE AUTH_ID OUTER_SHA LAUNCHER_SOURCE LAUNCHER_SHA KEEPER_SOURCE
KEEPER_SHA MARKER_SOURCE MARKER_SHA CHILD_SOURCE CHILD_SHA TOTAL_NS
LEDGER_BYTES LEDGER_LF LEDGER_SHA LEDGER_TERMINAL CONTROL_BYTES CONTROL_LF
CONTROL_SHA CONTROL_TERMINAL [PROBE_ARGS...]

OUTER CONTROLLER V8 SOURCE BEGIN
import errno
import fcntl
import hashlib
import os
import resource
import select
import signal
import stat
import sys
import time

PYTHON=b"/root/miniconda3/bin/python3"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
LEDGER=b"/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md"
CONTROL=b"/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V8.md"
KILL_REAP_PROGRESS_NS=250000000
MAX_LIVE_SLOTS=4
TERM_ALLOWANCE_NS=100000000
SYSCALL_OVERHEAD_NS=50000000
PER_NONKEEPER_CLEANUP_NS=400000000
KEEPER_FINALIZATION_NS=300000000
DERIVED_CLEANUP_GUARD_NS=1500000000
MAX_I63=(1<<63)-1
RAW_CAP=524288
BROKER_CAP=1048576

class Fail(Exception): pass
def need(value,code):
 if not value: raise Fail(code)
def mono():
 value=time.monotonic_ns(); need(type(value) is int and value>=0,"clock"); return value
def before(deadline,code): need(mono()<=deadline,code+"-pre")
def after(deadline,code): need(mono()<=deadline,code+"-post")
def dec(raw,lo=0,hi=MAX_I63):
 need(type(raw) is bytes and raw and raw.isdigit(),"decimal")
 value=int(raw); need(str(value).encode("ascii")==raw and lo<=value<=hi,"decimal-range"); return value
def hx(raw,count=64):
 need(type(raw) is bytes and len(raw)==count and count%2==0 and all(c in b"0123456789abcdef" for c in raw),"hex")
 need(bytes.fromhex(raw.decode("ascii")).hex().encode("ascii")==raw,"hex-roundtrip"); return raw
def write_exact(fd,data,deadline):
 position=0; flags=fcntl.fcntl(fd,fcntl.F_GETFL); fcntl.fcntl(fd,fcntl.F_SETFL,flags|os.O_NONBLOCK); poller=select.poll(); poller.register(fd,select.POLLOUT|select.POLLERR|select.POLLHUP)
 for unused in range(65536):
  if position==len(data): after(deadline,"write-complete"); return
  before(deadline,"write")
  try: count=os.write(fd,data[position:]); after(deadline,"write"); need(count>0,"write-zero"); position+=count
  except BlockingIOError: pass
  except InterruptedError: continue
  poller.poll(max(0,min(5,(deadline-mono()+999999)//1000000)))
 raise Fail("write-iterations")
def read_line(fd,deadline,cap):
 flags=fcntl.fcntl(fd,fcntl.F_GETFL); fcntl.fcntl(fd,fcntl.F_SETFL,flags|os.O_NONBLOCK); raw=bytearray(); poller=select.poll(); poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(65536):
  before(deadline,"line-read")
  try: chunk=os.read(fd,4096); after(deadline,"line-read")
  except BlockingIOError: chunk=None
  except InterruptedError: continue
  if chunk==b"": raise Fail("line-eof")
  if chunk:
   raw.extend(chunk); need(len(raw)<=cap and b"\r" not in raw and b"\x00" not in raw,"line-frame")
   if b"\n" in raw:
    need(raw.count(b"\n")==1 and raw.endswith(b"\n"),"line-count"); return bytes(raw)
  poller.poll(max(0,min(5,(deadline-mono()+999999)//1000000)))
 raise Fail("line-iterations")
def close_capture(fd,failures,label):
 if fd<0:return
 try: os.close(fd)
 except BaseException as error: failures.append((label+":"+type(error).__name__).encode("ascii","strict").lower())
def hash_fd(fd,size):
 os.lseek(fd,0,os.SEEK_SET); digest=hashlib.sha256(); total=0
 for unused in range((size+1048575)//1048576+1):
  chunk=os.read(fd,min(1048576,size-total+1))
  if not chunk: break
  total+=len(chunk); need(total<=size,"hash-growth"); digest.update(chunk)
 need(total==size,"hash-size"); return digest.hexdigest().encode("ascii")
def bind_file(path,size,lf,digest,terminal):
 fd=os.open(path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW); held=os.fstat(fd); current=os.stat(path,follow_symlinks=False)
 need((held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size)==(current.st_dev,current.st_ino,current.st_mode,current.st_nlink,current.st_uid,current.st_gid,current.st_size),"file-race")
 need(stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o644 and held.st_nlink==1 and held.st_uid==0 and held.st_gid==0 and held.st_size==size,"file-identity")
 need(hash_fd(fd,size)==digest,"file-hash"); os.lseek(fd,0,os.SEEK_SET); raw=os.read(fd,size+1); need(len(raw)==size and raw.count(b"\n")==lf and raw.endswith(terminal+b"\n") and sum(line==terminal for line in raw.splitlines())==1,"file-frame"); return fd

slots={}
def live_count(): return sum(1 for state in slots.values() if state[0]==1)
def physical_reap(pid,status):
 need(pid in slots and slots[pid][0]==1 and type(status) is int,"reap-state")
 live,unused,role,phase=slots[pid]; slots[pid]=(0,status,role,b"reaped")
def poll_owned(pid):
 need(pid in slots and slots[pid][0]==1,"wait-owner")
 try: got,status=os.waitpid(pid,os.WNOHANG)
 except InterruptedError:return 0
 except ChildProcessError as error: raise Fail("wait-echild") from error
 need(got in (0,pid),"wait-return")
 if got==pid: physical_reap(pid,status)
 return got
def spawn_owned(role,argv,env,actions,group,deadline):
 need(type(role) is bytes and role in (b"launcher",b"keeper",b"marker",b"child"),"spawn-role")
 need(live_count()<MAX_LIVE_SLOTS,"slot-bound")
 frozen_argv=tuple(argv); frozen_actions=tuple(actions); frozen_env=dict(env)
 before(deadline,"spawn")
 pid=os.posix_spawn(frozen_argv[0],frozen_argv,frozen_env,file_actions=frozen_actions,setpgroup=group,setsigmask=(),setsigdef=tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP)))))
 slots[pid]=(1,None,role,b"returned")
 after(deadline,"spawn")
 need(pid>1,"spawn-pid"); return pid
def stop_slot(pid,cleanup_start,failures):
 if pid not in slots or slots[pid][0]==0:return
 role=slots[pid][2]; got=poll_owned(pid)
 if got==pid:return
 if role!=b"keeper":
  try: os.kill(pid,signal.SIGTERM)
  except ProcessLookupError: pass
  except BaseException as error: failures.append((b"term-"+role+b":"+type(error).__name__.encode("ascii","strict").lower()))
  term_deadline=min(cleanup_start+DERIVED_CLEANUP_GUARD_NS,mono()+TERM_ALLOWANCE_NS)
  for unused in range(65536):
   if poll_owned(pid)==pid:return
   if mono()>=term_deadline:break
   select.poll().poll(2)
 if slots[pid][0]:
  try: os.kill(pid,signal.SIGKILL)
  except ProcessLookupError: pass
  except BaseException as error: failures.append((b"kill-"+role+b":"+type(error).__name__.encode("ascii","strict").lower()))
  kill_start=mono(); need(kill_start<=MAX_I63-KILL_REAP_PROGRESS_NS-SYSCALL_OVERHEAD_NS,"kill-deadline-overflow")
  kill_deadline=kill_start+KILL_REAP_PROGRESS_NS
  reap_deadline=kill_deadline+SYSCALL_OVERHEAD_NS
  for unused in range(131072):
   if poll_owned(pid)==pid:break
   need(mono()<=reap_deadline,"kill-reap-progress-premise")
   select.poll().poll(1)
 need(slots[pid][0]==0 and slots[pid][1] is not None,"slot-unreaped")
def cleanup_registry(failures):
 start=mono(); need(start<=MAX_I63-DERIVED_CLEANUP_GUARD_NS,"cleanup-overflow"); guard=start+DERIVED_CLEANUP_GUARD_NS
 for role in (b"child",b"marker",b"launcher"):
  for pid in tuple(sorted(slots)):
   if slots[pid][0] and slots[pid][2]==role: stop_slot(pid,start,failures)
  need(all(state[0]==0 for state in slots.values() if state[2]==role),"role-unreaped")
 for pid in tuple(sorted(slots)):
  if slots[pid][0] and slots[pid][2]==b"keeper": stop_slot(pid,start,failures)
 need(all(state[0]==0 and state[1] is not None for state in slots.values()),"registry-unreaped")
 need(mono()<=guard,"derived-cleanup-guard")

def parse_request(raw,probe,child_sha):
 need(raw.endswith(b"\n") and raw.count(b"\n")==1,"request-line")
 parts=raw[:-1].split(b"|"); need(len(parts)==7 and parts[:2]==[b"P27E001V8",b"broker=request"],"request-fields")
 expected=(b"seq=0",b"probe="+probe)
 need(parts[2:4]==list(expected),"request-binding")
 need(parts[4].startswith(b"op=") and parts[5]==b"child_sha="+child_sha,"request-order")
 need(parts[6]==b"end=1","request-end")
 op=parts[4][3:]; need(op in (b"P00_E2BIG",b"P01C_INFO",b"P05_WAIT",b"P08_TOPOLOGY",b"P09_KILL",b"P10_INFO16",b"P12_CHAIN"),"request-op"); return op
def drain_child(fd,deadline):
 flags=fcntl.fcntl(fd,fcntl.F_GETFL); fcntl.fcntl(fd,fcntl.F_SETFL,flags|os.O_NONBLOCK); raw=bytearray(); eof=False; poller=select.poll(); poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(65536):
  try: chunk=os.read(fd,4096)
  except BlockingIOError: chunk=None
  except InterruptedError: continue
  if chunk==b"":eof=True
  elif chunk: raw.extend(chunk); need(len(raw)<=RAW_CAP,"child-cap")
  if eof:return bytes(raw)
  need(mono()<=deadline,"child-drain-deadline"); poller.poll(2)
 raise Fail("child-drain-iterations")
def run_leaf(mode,source,source_sha,safe,leader,deadline,gate=False,argv_override=None,env=ENV):
 out_r,out_w=os.pipe2(os.O_CLOEXEC); gate_r=gate_w=-1
 if gate: gate_r,gate_w=os.pipe2(os.O_CLOEXEC)
 actions=[(os.POSIX_SPAWN_DUP2,out_w,1),(os.POSIX_SPAWN_CLOSE,out_r),(os.POSIX_SPAWN_CLOSE,out_w)]
 if gate: actions.extend(((os.POSIX_SPAWN_DUP2,gate_r,3),(os.POSIX_SPAWN_CLOSE,gate_r),(os.POSIX_SPAWN_CLOSE,gate_w)))
 else: actions.append((os.POSIX_SPAWN_CLOSE,3))
 argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",source,mode,str(deadline).encode("ascii"),safe,source_sha) if argv_override is None else argv_override
 pid=spawn_owned(b"child",argv,env,actions,leader,deadline)
 close_capture(out_w,[],"child-out-w"); close_capture(gate_r,[],"child-gate-r")
 if gate: write_exact(gate_w,b"G",deadline); close_capture(gate_w,[],"child-gate-w")
 raw=drain_child(out_r,deadline); close_capture(out_r,[],"child-out-r")
 for unused in range(65536):
  if poll_owned(pid)==pid:break
  need(mono()<=deadline,"child-wait-deadline"); select.poll().poll(2)
 need(slots[pid][0]==0,"child-normal-reap"); return pid,slots[pid][1],raw
def run_p05(source,source_sha,safe,leader,deadline):
 out_r,out_w=os.pipe2(os.O_CLOEXEC); gate_r,gate_w=os.pipe2(os.O_CLOEXEC); actions=((os.POSIX_SPAWN_DUP2,out_w,1),(os.POSIX_SPAWN_DUP2,gate_r,3),(os.POSIX_SPAWN_CLOSE,out_r),(os.POSIX_SPAWN_CLOSE,out_w),(os.POSIX_SPAWN_CLOSE,gate_r),(os.POSIX_SPAWN_CLOSE,gate_w)); argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",source,b"EXIT23",str(deadline).encode("ascii"),safe,source_sha); pid=spawn_owned(b"child",argv,ENV,actions,leader,deadline); os.close(out_w);os.close(gate_r);ready=read_line(out_r,deadline,4096);need(poll_owned(pid)==0,"p05-wnohang")
 old_handler=signal.getsignal(signal.SIGALRM)
 def alarm(signum,frame):raise InterruptedError(errno.EINTR,"bounded-probe")
 signal.signal(signal.SIGALRM,alarm); signal.pthread_sigmask(signal.SIG_UNBLOCK,{signal.SIGALRM}); signal.setitimer(signal.ITIMER_REAL,0.02); interrupted=0
 try:
  try:
   got,status=os.waitpid(pid,0)
   if got==pid:physical_reap(pid,status)
   raise Fail("p05-unexpected-reap")
  except InterruptedError as error:need(error.errno==errno.EINTR,"p05-eintr");interrupted=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0.0);signal.pthread_sigmask(signal.SIG_BLOCK,{signal.SIGALRM});signal.signal(signal.SIGALRM,old_handler)
 need(interrupted==1,"p05-interrupted");write_exact(gate_w,b"G",deadline);os.close(gate_w);tail=drain_child(out_r,deadline);os.close(out_r)
 for unused in range(65536):
  if poll_owned(pid)==pid:break
  need(mono()<=deadline,"p05-exit-wait")
 need(os.WIFEXITED(slots[pid][1]) and os.WEXITSTATUS(slots[pid][1])==23,"p05-exit23");echild=0
 try:os.waitpid(pid,os.WNOHANG)
 except ChildProcessError as error:need(error.errno==errno.ECHILD,"p05-echild-errno");echild=1
 need(echild==1,"p05-echild");pid2,status2,raw2=run_leaf(b"TERM",source,source_sha,safe,leader,deadline);need(os.WIFSIGNALED(status2) and os.WTERMSIG(status2)==signal.SIGTERM,"p05-term")
 return (pid,pid2),(slots[pid][1],status2),ready+tail+raw2
def run_p08(source,source_sha,safe,leader,deadline):
 out_r,out_w=os.pipe2(os.O_CLOEXEC);gate_r,gate_w=os.pipe2(os.O_CLOEXEC);actions=((os.POSIX_SPAWN_DUP2,out_w,1),(os.POSIX_SPAWN_DUP2,gate_r,3),(os.POSIX_SPAWN_CLOSE,out_r),(os.POSIX_SPAWN_CLOSE,out_w),(os.POSIX_SPAWN_CLOSE,gate_r),(os.POSIX_SPAWN_CLOSE,gate_w));argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",source,b"BLOCK0",str(deadline).encode("ascii"),safe,source_sha);pid=spawn_owned(b"child",argv,ENV,actions,leader,deadline);os.close(out_w);os.close(gate_r);ready=read_line(out_r,deadline,4096);need(poll_owned(pid)==0 and os.getsid(pid)==os.getsid(0) and os.getpgid(pid)==leader,"p08-live-topology");os.kill(pid,0);write_exact(gate_w,b"G",deadline);os.close(gate_w);tail=drain_child(out_r,deadline);os.close(out_r)
 for unused in range(65536):
  if poll_owned(pid)==pid:break
  need(mono()<=deadline,"p08-wait")
 absent=0
 try:os.kill(pid,0)
 except ProcessLookupError as error:need(error.errno==errno.ESRCH,"p08-esrch-errno");absent=1
 need(absent==1,"p08-post-absence");return pid,slots[pid][1],ready+tail
def broker_operation(op,probe,source,source_sha,safe,leader,deadline):
 pids=[]; statuses=[]; payload=[]
 def add(mode,gate=False,argv_override=None,env=ENV):
  pid,status,raw=run_leaf(mode,source,source_sha,safe,leader,deadline,gate,argv_override,env); pids.append(pid); statuses.append(status); payload.append(mode+b":"+raw.hex().encode("ascii")); return pid,status,raw
 if op==b"P00_E2BIG":
  need(len(source)+2<251414,"p00-size"); synthetic=source+b"\n#"+b"x"*(251414-len(source)-2); returned=0; e2big=0
  try: add(b"INFO",False,(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",synthetic,b"INFO",str(deadline).encode("ascii"),safe,hashlib.sha256(synthetic).hexdigest().encode("ascii"))); returned=1
  except OSError as error: need(error.errno==errno.E2BIG,"p00-errno"); e2big=1
  payload.append(b"source_bytes=251414,returned="+str(returned).encode("ascii")+b",e2big="+str(e2big).encode("ascii")+b",sha="+hashlib.sha256(synthetic).hexdigest().encode("ascii"))
 elif op==b"P01C_INFO": add(b"INFO")
 elif op==b"P05_WAIT":
  gotp,gots,raw=run_p05(source,source_sha,safe,leader,deadline);pids.extend(gotp);statuses.extend(gots);payload.append(b"P05:"+raw.hex().encode("ascii"))
 elif op==b"P08_TOPOLOGY":
  pid,status,raw=run_p08(source,source_sha,safe,leader,deadline);pids.append(pid);statuses.append(status);payload.append(b"P08:"+raw.hex().encode("ascii"))
 elif op==b"P09_KILL":
  out_r,out_w=os.pipe2(os.O_CLOEXEC);gate_r,gate_w=os.pipe2(os.O_CLOEXEC);actions=((os.POSIX_SPAWN_DUP2,out_w,1),(os.POSIX_SPAWN_DUP2,gate_r,3),(os.POSIX_SPAWN_CLOSE,out_r),(os.POSIX_SPAWN_CLOSE,out_w),(os.POSIX_SPAWN_CLOSE,gate_r),(os.POSIX_SPAWN_CLOSE,gate_w));argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",source,b"BLOCK0",str(deadline).encode("ascii"),safe,source_sha);pid=spawn_owned(b"child",argv,ENV,actions,leader,deadline);os.close(out_w);os.close(gate_r);ready=read_line(out_r,deadline,4096);need(poll_owned(pid)==0,"p09-live");os.kill(pid,signal.SIGKILL);os.close(gate_w);raw=ready+drain_child(out_r,deadline);os.close(out_r)
  for unused in range(65536):
   if poll_owned(pid)==pid:break
   need(mono()<=deadline,"p09-wait")
  pids.append(pid); statuses.append(slots[pid][1]); payload.append(b"BLOCK0:"+raw.hex().encode("ascii"))
 elif op==b"P10_INFO16":
  for sample in range(16): add(b"INFO")
 elif op==b"P12_CHAIN":
  command=b'exec /usr/bin/env -i LANG=C LC_ALL=C PATH=/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONIOENCODING=UTF-8:strict PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 PYTHONUTF8=1 TZ=UTC /root/miniconda3/bin/python3 -I -S -B -P -X utf8 -c "$1" CHAIN "$2" "$3" "$4"'
  argv=(b"/usr/bin/env",b"-i",b"/usr/bin/bash",b"--noprofile",b"--norc",b"-c",command,b"p27-e001-v8-chain",source,str(deadline).encode("ascii"),safe,source_sha); add(b"CHAIN",False,argv,{})
 need(all(slots[pid][0]==0 and slots[pid][1] is not None for pid in pids),"broker-exact-reap")
 body=b";".join(payload); return b"P27E001V8|broker=response|seq=0|probe="+probe+b"|op="+op+b"|spawned="+str(len(pids)).encode("ascii")+b"|reaped="+str(len(pids)).encode("ascii")+b"|pids="+(b",".join(str(pid).encode("ascii") for pid in pids) if pids else b"-")+b"|statuses="+(b",".join(str(x).encode("ascii") for x in statuses) if statuses else b"-")+b"|payload_hex="+body.hex().encode("ascii")+b"|result=PASS\n"

primary=b"none"; cleanup_failures=[]; result=b"FAIL"; admission=1
leader=keeper=marker=-1; ledger_fd=control_fd=-1; req_r=req_w=resp_r=resp_w=marker_out_r=marker_out_w=launcher_hold_r=launcher_hold_w=keeper_hold_r=keeper_hold_w=-1
safe=b""; safe_name=b""; safe_fd=tmp_fd=-1; marker_raw=b""; request_raw=b""; total_deadline=mono(); work_deadline=total_deadline
try:
 need(len(sys.argv)>=21 and sys.argv[0]=="-c","argv-count")
 probe=os.fsencode(sys.argv[1]); auth=os.fsencode(sys.argv[2]); outer_sha=hx(os.fsencode(sys.argv[3])); launcher_source=os.fsencode(sys.argv[4]); launcher_sha=hx(os.fsencode(sys.argv[5])); keeper_source=os.fsencode(sys.argv[6]); keeper_sha=hx(os.fsencode(sys.argv[7])); marker_source=os.fsencode(sys.argv[8]); marker_sha=hx(os.fsencode(sys.argv[9])); child_source=os.fsencode(sys.argv[10]); child_sha=hx(os.fsencode(sys.argv[11])); total_ns=dec(os.fsencode(sys.argv[12]),2000000000,10000000000)
 ledger_bytes=dec(os.fsencode(sys.argv[13]),1,400000000); ledger_lf=dec(os.fsencode(sys.argv[14]),1,1000000); ledger_sha=hx(os.fsencode(sys.argv[15])); ledger_terminal=os.fsencode(sys.argv[16]); control_bytes=dec(os.fsencode(sys.argv[17]),1,400000000); control_lf=dec(os.fsencode(sys.argv[18]),1,1000000); control_sha=hx(os.fsencode(sys.argv[19])); control_terminal=os.fsencode(sys.argv[20]); extra=tuple(os.fsencode(x) for x in sys.argv[21:])
 need(probe in (b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13"),"probe")
 hx(auth); need(hashlib.sha256(os.fsencode(sys.orig_argv[8])).hexdigest().encode("ascii")==outer_sha,"outer-source"); need(hashlib.sha256(launcher_source).hexdigest().encode("ascii")==launcher_sha and hashlib.sha256(keeper_source).hexdigest().encode("ascii")==keeper_sha and hashlib.sha256(marker_source).hexdigest().encode("ascii")==marker_sha and hashlib.sha256(child_source).hexdigest().encode("ascii")==child_sha,"source-bind")
 need(PER_NONKEEPER_CLEANUP_NS==TERM_ALLOWANCE_NS+KILL_REAP_PROGRESS_NS+SYSCALL_OVERHEAD_NS,"per-slot-arithmetic"); need(MAX_LIVE_SLOTS-1<=(MAX_I63-KEEPER_FINALIZATION_NS)//PER_NONKEEPER_CLEANUP_NS,"guard-overflow"); need(DERIVED_CLEANUP_GUARD_NS==(MAX_LIVE_SLOTS-1)*PER_NONKEEPER_CLEANUP_NS+KEEPER_FINALIZATION_NS and total_ns>DERIVED_CLEANUP_GUARD_NS,"guard-arithmetic")
 start=mono(); need(start<=MAX_I63-total_ns,"total-overflow"); total_deadline=start+total_ns; work_deadline=total_deadline-DERIVED_CLEANUP_GUARD_NS
 need(os.getpid()!=os.getpgrp(),"outer-group-external"); cpu=resource.getrlimit(resource.RLIMIT_CPU); need(cpu[1]==resource.RLIM_INFINITY,"outer-no-hard-cpu")
 catchable=set(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))); signal.pthread_sigmask(signal.SIG_BLOCK,catchable)
 ledger_fd=bind_file(LEDGER,ledger_bytes,ledger_lf,ledger_sha,ledger_terminal); control_fd=bind_file(CONTROL,control_bytes,control_lf,control_sha,control_terminal)
 tmp_fd=os.open(b"/tmp",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW); safe_name=b"p27-e001-host-v8-"+auth; need(len(safe_name)==len(b"p27-e001-host-v8-")+64 and b"/" not in safe_name and b".." not in safe_name,"safe-name"); os.mkdir(safe_name,0o700,dir_fd=tmp_fd); safe_fd=os.open(safe_name,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=tmp_fd); safe=b"/tmp/"+safe_name; os.chdir(safe)
 req_r,req_w=os.pipe2(os.O_CLOEXEC); resp_r,resp_w=os.pipe2(os.O_CLOEXEC); marker_out_r,marker_out_w=os.pipe2(os.O_CLOEXEC); launcher_hold_r,launcher_hold_w=os.pipe2(os.O_CLOEXEC); keeper_hold_r,keeper_hold_w=os.pipe2(os.O_CLOEXEC)
 launcher_actions=((os.POSIX_SPAWN_DUP2,launcher_hold_r,3),(os.POSIX_SPAWN_CLOSE,launcher_hold_w)); launcher_argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",launcher_source,str(os.getpid()).encode("ascii"),launcher_sha,safe); leader=spawn_owned(b"launcher",launcher_argv,ENV,launcher_actions,0,work_deadline)
 keeper_actions=((os.POSIX_SPAWN_DUP2,keeper_hold_r,3),(os.POSIX_SPAWN_CLOSE,keeper_hold_w)); keeper_argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",keeper_source,str(os.getpid()).encode("ascii"),str(leader).encode("ascii"),keeper_sha); keeper=spawn_owned(b"keeper",keeper_argv,ENV,keeper_actions,leader,work_deadline)
 marker_actions=((os.POSIX_SPAWN_DUP2,marker_out_w,1),(os.POSIX_SPAWN_DUP2,req_w,5),(os.POSIX_SPAWN_DUP2,resp_r,6),(os.POSIX_SPAWN_CLOSE,marker_out_r),(os.POSIX_SPAWN_CLOSE,req_r),(os.POSIX_SPAWN_CLOSE,resp_w)); marker_argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",marker_source,probe,safe,marker_sha,child_sha,str(work_deadline).encode("ascii"),str(total_ns).encode("ascii"))+extra; marker=spawn_owned(b"marker",marker_argv,ENV,marker_actions,leader,work_deadline)
 for fd in (launcher_hold_r,keeper_hold_r,marker_out_w,req_w,resp_r): close_capture(fd,cleanup_failures,"parent-child-end")
 launcher_hold_r=keeper_hold_r=marker_out_w=req_w=resp_r=-1
 request_raw=read_line(req_r,work_deadline,4096); op=parse_request(request_raw,probe,child_sha); response=broker_operation(op,probe,child_source,child_sha,safe,leader,work_deadline); write_exact(resp_w,response,work_deadline); close_capture(resp_w,cleanup_failures,"broker-response"); resp_w=-1; admission=0
 marker_raw=drain_child(marker_out_r,work_deadline); close_capture(marker_out_r,cleanup_failures,"marker-out"); marker_out_r=-1
 for unused in range(65536):
  if poll_owned(marker)==marker:break
  need(mono()<=work_deadline,"marker-wait")
 need(slots[marker][0]==0 and slots[marker][1]==0,"marker-status"); result=b"PASS"
except BaseException as error:
 admission=0
 if primary==b"none": primary=(os.fsencode(str(error)).replace(b"_",b"-") if isinstance(error,Fail) else ("exception-"+type(error).__name__).encode("ascii","strict").lower())
finally:
 admission=0
 for fd in (req_r,req_w,resp_r,resp_w): close_capture(fd,cleanup_failures,"broker-close")
 close_capture(launcher_hold_w,cleanup_failures,"launcher-release"); launcher_hold_w=-1
 close_capture(keeper_hold_w,cleanup_failures,"keeper-hold-release"); keeper_hold_w=-1
 cleanup_registry(cleanup_failures)
 for fixed in (b"target",b"a",b"b"):
  try:
   held=os.stat(fixed,dir_fd=safe_fd,follow_symlinks=False)
   if stat.S_ISREG(held.st_mode) and held.st_uid==0 and held.st_gid==0: os.unlink(fixed,dir_fd=safe_fd)
  except FileNotFoundError: pass
  except BaseException as error: cleanup_failures.append((b"safe-clean:"+type(error).__name__.encode("ascii","strict").lower()))
 if safe_fd>=0: close_capture(safe_fd,cleanup_failures,"safe-fd"); safe_fd=-1
 if tmp_fd>=0 and safe_name:
  try: os.rmdir(safe_name,dir_fd=tmp_fd)
  except BaseException as error: cleanup_failures.append((b"safe-rmdir:"+type(error).__name__.encode("ascii","strict").lower()))
 for fd in (tmp_fd,ledger_fd,control_fd,marker_out_r,marker_out_w,launcher_hold_r,launcher_hold_w,keeper_hold_r,keeper_hold_w): close_capture(fd,cleanup_failures,"final-fd")
 final=b"PASS" if result==b"PASS" and primary==b"none" and not cleanup_failures and admission==0 and slots and all(state[0]==0 and state[1] is not None for state in slots.values()) else b"FAIL"
 report=b"P27E001V8|outer=terminal|probe="+probe+b"|slots="+str(len(slots)).encode("ascii")+b"|all_reaped="+str(int(bool(slots) and all(state[0]==0 for state in slots.values()))).encode("ascii")+b"|primary_failure="+primary+b"|cleanup_failure="+(b"none" if not cleanup_failures else b"present")+b"|result="+final+b"\n"
 try:
  if marker_raw: os.write(1,marker_raw)
  os.write(1,report)
 except BaseException: pass
 if final!=b"PASS": raise SystemExit(90)
OUTER CONTROLLER V8 SOURCE END

## 5. Exact keeper leaf source

GROUP KEEPER V8 SOURCE BEGIN
import hashlib
import os
import signal
import sys
import time
P=b"/root/miniconda3/bin/python3"
E={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
class F(Exception):pass
def n(v,c):
 if not v:raise F(c)
def d(x):
 b=os.fsencode(x);n(b and b.isdigit()and str(int(b)).encode("ascii")==b,"decimal");return int(b)
n(len(sys.argv)==4 and sys.argv[0]=="-c","argv")
outer=d(sys.argv[1]);leader=d(sys.argv[2]);sha=os.fsencode(sys.argv[3]);source=os.fsencode(sys.orig_argv[8]);n(len(sha)==64 and hashlib.sha256(source).hexdigest().encode("ascii")==sha,"source")
n(sys.executable==P.decode("ascii")and dict(os.environb)==E,"runtime");n(os.getppid()==outer and os.getpgrp()==leader and os.getsid(0)==os.getsid(outer),"topology")
catchable=set(int(x)for x in signal.valid_signals()if int(x)not in(int(signal.SIGKILL),int(signal.SIGSTOP)));signal.pthread_sigmask(signal.SIG_BLOCK,catchable)
for unused in range(1048576):
 try:chunk=os.read(3,1)
 except InterruptedError:continue
 if chunk==b"":break
 n(not chunk,"hold-data")
else:raise F("hold-iterations")
raise SystemExit(0)
GROUP KEEPER V8 SOURCE END

## 6. Exact launcher leaf source

The launcher is a direct outer-owned group-leader leaf. It owns no process,
does not create or wait for a process, sets no CPU hard limit, and remains
alive only while the outer-held FD 3 writer remains open.

OWNED LAUNCHER V8 SOURCE BEGIN
import hashlib
import os
import signal
import sys
P=b"/root/miniconda3/bin/python3"
E={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
class F(Exception):pass
def n(v,c):
 if not v:raise F(c)
def d(x):
 b=os.fsencode(x);n(b and b.isdigit()and str(int(b)).encode("ascii")==b,"decimal");return int(b)
n(len(sys.argv)==4 and sys.argv[0]=="-c","argv")
outer=d(sys.argv[1]);sha=os.fsencode(sys.argv[2]);safe=os.fsencode(sys.argv[3]);source=os.fsencode(sys.orig_argv[8])
n(len(sha)==64 and hashlib.sha256(source).hexdigest().encode("ascii")==sha,"source")
n(sys.executable==P.decode("ascii")and dict(os.environb)==E,"runtime")
n(os.getppid()==outer and os.getpid()==os.getpgrp() and os.getsid(0)==os.getsid(outer),"topology")
n(os.getcwdb()==safe and safe.startswith(b"/tmp/p27-e001-host-v8-"),"cwd")
for unused in range(1048576):
 try:chunk=os.read(3,1)
 except InterruptedError:continue
 if chunk==b"":break
 n(not chunk,"hold-data")
else:raise F("hold-iterations")
raise SystemExit(0)
OWNED LAUNCHER V8 SOURCE END

## 7. Exact marker leaf and nested child source

The marker is a direct outer child and a broker client. It performs local
non-child observations, but every process observation in P00, P01C, P05,
P08, P09, P10 and P12 comes from a closed broker response that the outer can
form only after exact physical reap. The nested record remains a complete
self-binding five-mode leaf and is transported separately to the outer.

UNIFIED MARKER V8 SOURCE BEGIN
import errno
import fcntl
import hashlib
import os
import resource
import select
import signal
import stat
import sys
import time

PYTHON=b"/root/miniconda3/bin/python3"
PYRES=b"/root/miniconda3/bin/python3.12"
PY_BYTES=30626264
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
MAX_I63=(1<<63)-1
HARD_NOFILE=1048576
CAP=1048576
class Fail(Exception):pass
def need(value,code):
 if not value:raise Fail(code)
def mono():
 value=time.monotonic_ns();need(type(value)is int and value>=0,"clock");return value
def before(deadline,code):need(mono()<=deadline,code+"-pre")
def after(deadline,code):need(mono()<=deadline,code+"-post")
def decimal(raw,lo=0,hi=MAX_I63):
 need(type(raw)is bytes and raw and raw.isdigit(),"decimal");value=int(raw);need(str(value).encode("ascii")==raw and lo<=value<=hi,"decimal-range");return value
def hexa(raw,count=None):
 need(type(raw)is bytes and raw and len(raw)%2==0 and (count is None or len(raw)==count) and all(c in b"0123456789abcdef" for c in raw),"hex")
 need(bytes.fromhex(raw.decode("ascii")).hex().encode("ascii")==raw,"hex-roundtrip");return raw
def decoded(raw,count=None):hexa(raw,count);value=bytes.fromhex(raw.decode("ascii"));need(value.hex().encode("ascii")==raw,"decoded-roundtrip");return value
def octal(raw):
 need(type(raw)is bytes and raw and all(c in b"01234567" for c in raw),"octal");value=int(raw,8);need(format(value,"o").encode("ascii")==raw,"octal-canonical");return value
def call(deadline,label,fn,*args,**kwargs):before(deadline,label);value=fn(*args,**kwargs);after(deadline,label);return value
def write_exact(fd,data,deadline):
 position=0;flags=fcntl.fcntl(fd,fcntl.F_GETFL);fcntl.fcntl(fd,fcntl.F_SETFL,flags|os.O_NONBLOCK);poller=select.poll();poller.register(fd,select.POLLOUT|select.POLLERR|select.POLLHUP)
 for unused in range(65536):
  if position==len(data):return
  try:count=os.write(fd,data[position:]);need(count>0,"write-zero");position+=count
  except BlockingIOError:pass
  except InterruptedError:continue
  need(mono()<=deadline,"write-deadline");poller.poll(2)
 raise Fail("write-iterations")
def read_line(fd,deadline):
 flags=fcntl.fcntl(fd,fcntl.F_GETFL);fcntl.fcntl(fd,fcntl.F_SETFL,flags|os.O_NONBLOCK);raw=bytearray();poller=select.poll();poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(65536):
  try:chunk=os.read(fd,4096)
  except BlockingIOError:chunk=None
  except InterruptedError:continue
  if chunk==b"":raise Fail("broker-eof")
  if chunk:
   raw.extend(chunk);need(len(raw)<=CAP and b"\r" not in raw and b"\x00" not in raw,"broker-frame")
   if b"\n" in raw:need(raw.count(b"\n")==1 and raw.endswith(b"\n"),"broker-lines");return bytes(raw)
  need(mono()<=deadline,"broker-deadline");poller.poll(2)
 raise Fail("broker-iterations")
def broker(probe,operation,child_sha,deadline):
 request=b"P27E001V8|broker=request|seq=0|probe="+probe+b"|op="+operation+b"|child_sha="+child_sha+b"|end=1\n"
 write_exact(5,request,deadline);raw=read_line(6,deadline);parts=raw[:-1].split(b"|")
 need(len(parts)==11 and parts[:3]==[b"P27E001V8",b"broker=response",b"seq=0"],"response-fields")
 need(parts[3]==b"probe="+probe and parts[4]==b"op="+operation and parts[5].startswith(b"spawned=") and parts[6].startswith(b"reaped="),"response-order")
 spawned=decimal(parts[5][8:]);reaped=decimal(parts[6][7:]);need(spawned==reaped,"response-reap")
 need(parts[7].startswith(b"pids=") and parts[8].startswith(b"statuses=") and parts[9].startswith(b"payload_hex=") and parts[10]==b"result=PASS","response-tail")
 payload=decoded(parts[9][12:]) if parts[9][12:] else b"";return spawned,parts[7][5:],parts[8][9:],payload
def hash_fd(fd,size):
 os.lseek(fd,0,os.SEEK_SET);digest=hashlib.sha256();total=0
 for unused in range((size+1048575)//1048576+1):
  chunk=os.read(fd,min(1048576,size-total+1))
  if not chunk:break
  total+=len(chunk);need(total<=size,"hash-growth");digest.update(chunk)
 need(total==size,"hash-size");return digest.hexdigest().encode("ascii")
def image():
 link=os.lstat(PYTHON);need(stat.S_ISLNK(link.st_mode)and os.readlink(PYTHON)==b"python3.12","image-link")
 resolved=os.open(PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);self_fd=os.open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC);a=os.fstat(resolved);b=os.fstat(self_fd)
 need((a.st_dev,a.st_ino,a.st_mode,a.st_nlink,a.st_uid,a.st_gid,a.st_size)==(b.st_dev,b.st_ino,b.st_mode,b.st_nlink,b.st_uid,b.st_gid,b.st_size) and a.st_size==PY_BYTES,"image-identity")
 need(hash_fd(resolved,PY_BYTES)==PY_SHA and hash_fd(self_fd,PY_BYTES)==PY_SHA,"image-hash");os.close(resolved);os.close(self_fd);return (a.st_dev,a.st_ino,a.st_mode,a.st_nlink,a.st_uid,a.st_gid,a.st_size)
def libc_view():
 fd=os.open(b"/proc/self/maps",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);raw=bytearray()
 for unused in range(2048):
  chunk=os.read(fd,4096)
  if not chunk:break
  raw.extend(chunk);need(len(raw)<=4194304,"maps-cap")
 os.close(fd);found=[]
 for line in bytes(raw).splitlines():
  parts=line.split(None,5)
  if len(parts)==6 and b"x" in parts[1] and parts[5].startswith(b"/") and parts[5].rsplit(b"/",1)[-1].startswith(b"libc.so"):found.append(parts[5])
 paths=tuple(sorted(set(found)));need(len(paths)==1,"libc-count");path=paths[0];libc=os.open(path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);held=os.fstat(libc);digest=hash_fd(libc,held.st_size);os.close(libc);conf=os.confstr("CS_GNU_LIBC_VERSION");need(type(conf)is str and conf.isascii(),"confstr");return path,held,digest,conf.encode("ascii")
def row(rows,probe,key,value):
 if type(value)is int:value=str(value).encode("ascii")
 if type(value)is str:value=value.encode("ascii")
 need(type(value)is bytes and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value,"row");rows.append(b"P27E001V8|probe="+probe+b"|"+key+b"="+value)

CHILD_SOURCE=b'''\
import hashlib
import os
import resource
import signal
import stat
import sys
import time
P=b"/root/miniconda3/bin/python3"
R=b"/root/miniconda3/bin/python3.12"
N=30626264
H=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
E={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
class F(Exception):pass
def n(v,c):
 if not v:raise F(c)
def d(x):
 b=os.fsencode(x);n(b and b.isdigit()and str(int(b)).encode("ascii")==b,"decimal");return int(b)
def h(fd,size):
 os.lseek(fd,0,os.SEEK_SET);z=hashlib.sha256();m=0
 for unused in range((size+1048575)//1048576+1):
  x=os.read(fd,min(1048576,size-m+1))
  if not x:break
  m+=len(x);n(m<=size,"growth");z.update(x)
 n(m==size,"short");return z.hexdigest().encode("ascii")
mode=b"invalid";code=91;a=b=-1
try:
 n(len(sys.argv)==5 and sys.argv[0]=="-c","argv");mode=os.fsencode(sys.argv[1]);deadline=d(sys.argv[2]);safe=os.fsencode(sys.argv[3]);source_sha=os.fsencode(sys.argv[4]);n(mode in(b"INFO",b"BLOCK0",b"EXIT23",b"TERM",b"CHAIN"),"mode")
 n(sys.executable==P.decode("ascii")and dict(os.environb)==E and hashlib.sha256(os.fsencode(sys.orig_argv[8])).hexdigest().encode("ascii")==source_sha,"runtime")
 resource.setrlimit(resource.RLIMIT_NOFILE,(4096,1048576));resource.setrlimit(resource.RLIMIT_CPU,(3,3));resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456));resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 definitions=tuple(sorted(int(x)for x in signal.valid_signals()if int(x)not in(int(signal.SIGKILL),int(signal.SIGSTOP))));signal.pthread_sigmask(signal.SIG_SETMASK,set())
 for number in definitions:signal.signal(number,signal.SIG_DFL)
 n(os.getcwdb()==safe and time.monotonic_ns()<=deadline,"leaf-context");a=os.open(R,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);b=os.open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC);sa=os.fstat(a);sb=os.fstat(b);n((sa.st_dev,sa.st_ino,sa.st_size)==(sb.st_dev,sb.st_ino,N)and h(a,N)==h(b,N)==H,"image")
 phase=b"ready" if mode in(b"BLOCK0",b"EXIT23",b"TERM")else b"terminal";line=b"P27E001V8|child=observation|mode="+mode+b"|pid="+str(os.getpid()).encode("ascii")+b"|sid="+str(os.getsid(0)).encode("ascii")+b"|pgid="+str(os.getpgrp()).encode("ascii")+b"|image_sha="+H+b"|source_sha="+source_sha+b"|cwd_hex="+safe.hex().encode("ascii")+b"|phase="+phase+b"|result=PASS\n";n(os.write(1,line)==len(line),"write")
 if mode in(b"BLOCK0",b"EXIT23"):n(os.read(3,1)==b"G","gate");code=23 if mode==b"EXIT23"else 0
 elif mode==b"TERM":os.kill(os.getpid(),signal.SIGTERM)
 else:code=0
finally:
 for fd in(a,b):
  if fd>=0:
   try:os.close(fd)
   except BaseException:code=92
raise SystemExit(code)
'''

primary=b"none";rows=[];result=b"FAIL";probe=b"invalid";safe=b"";marker_sha=b"";child_sha=b"";deadline=mono();total_ns=0;extra=()
try:
 need(len(sys.argv)>=7 and sys.argv[0]=="-c","argv-count");probe=os.fsencode(sys.argv[1]);safe=os.fsencode(sys.argv[2]);marker_sha=hexa(os.fsencode(sys.argv[3]),64);child_sha=hexa(os.fsencode(sys.argv[4]),64);deadline=decimal(os.fsencode(sys.argv[5]),1);total_ns=decimal(os.fsencode(sys.argv[6]),2000000000,10000000000);extra=tuple(os.fsencode(x) for x in sys.argv[7:])
 need(probe in (b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13"),"probe-id")
 need(hashlib.sha256(os.fsencode(sys.orig_argv[8])).hexdigest().encode("ascii")==marker_sha and hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii")==child_sha,"source-bind")
 need(sys.executable==PYTHON.decode("ascii") and dict(os.environb)==ENV and os.getcwdb()==safe,"runtime")
 resource.setrlimit(resource.RLIMIT_NOFILE,(4096,HARD_NOFILE));resource.setrlimit(resource.RLIMIT_CPU,(3,3));resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456));resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 image_key=image();start=mono();after(deadline,"probe-start")
 if probe==b"P00":
  need(len(extra)==0,"p00-extra");spawned,pids,statuses,payload=broker(probe,b"P00_E2BIG",child_sha,deadline);row(rows,probe,b"source_item_bytes",251414);row(rows,probe,b"source_item_accounted_bytes",251415);row(rows,probe,b"broker_spawned",spawned);row(rows,probe,b"broker_payload_hex",payload.hex())
 elif probe==b"P01D":
  need(len(extra)==0,"p01d-extra");path,held,digest,conf=libc_view();surface=getattr(os,"posix_"+"spawn");row(rows,probe,b"python_image_dev",image_key[0]);row(rows,probe,b"python_image_ino",image_key[1]);row(rows,probe,b"python_image_bytes",image_key[6]);row(rows,probe,b"python_image_sha256",PY_SHA);row(rows,probe,b"libc_confstr_hex",conf.hex());row(rows,probe,b"libc_path_hex",path.hex());row(rows,probe,b"libc_bytes",held.st_size);row(rows,probe,b"libc_sha256",digest);row(rows,probe,b"backend_surface",surface.__module__.encode("ascii")+b"-"+surface.__name__.encode("ascii"));row(rows,probe,b"spawn_premise_satisfied",0)
 elif probe==b"P01C":
  need(len(extra)==13,"p01c-extra-count");path=decoded(extra[0]);mapdev=decimal(extra[1]);mapino=decimal(extra[2]);mode=octal(extra[3]);nlink=decimal(extra[4]);uid=decimal(extra[5]);gid=decimal(extra[6]);size=decimal(extra[7]);digest=hexa(extra[8],64);conf_bytes=decoded(extra[9]);pydev=decimal(extra[10]);pyino=decimal(extra[11]);pysha=hexa(extra[12],64);need(conf_bytes.isascii() and conf_bytes.decode("ascii").encode("ascii")==conf_bytes and conf_bytes.hex().encode("ascii")==extra[9],"p01c-extra9")
  expected=(path,mapdev,mapino,mode,nlink,uid,gid,size,digest,conf_bytes,pydev,pyino,pysha);lpath,held,ldigest,conf=libc_view();actual=(lpath,held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,ldigest,conf,image_key[0],image_key[1],PY_SHA);need(actual==expected,"p01c-seal");spawned,pids,statuses,payload=broker(probe,b"P01C_INFO",child_sha,deadline);need(spawned==1,"p01c-child");row(rows,probe,b"libc_path_hex",lpath.hex());row(rows,probe,b"libc_sha256",ldigest);row(rows,probe,b"libc_confstr_hex",conf.hex());row(rows,probe,b"child_pids",pids);row(rows,probe,b"child_statuses",statuses);row(rows,probe,b"child_raw_hex",payload.hex());row(rows,probe,b"spawn_premise_satisfied",1)
 elif probe==b"P02":
  need(len(extra)==0,"p02-extra");fds=[]
  for fd in range(7):
   try:fcntl.fcntl(fd,fcntl.F_GETFD);fds.append(fd)
   except OSError as error:need(error.errno==errno.EBADF,"p02-fd")
  need(fds==[0,1,2,5,6] and dict(os.environb)==ENV,"p02-context");row(rows,probe,b"fds",b"0,1,2,5,6");row(rows,probe,b"environment_count",10);row(rows,probe,b"cwd_hex",safe.hex());row(rows,probe,b"flags",b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1")
 elif probe==b"P03":
  need(len(extra)==0,"p03-extra");soft,hard=resource.getrlimit(resource.RLIMIT_NOFILE);need((soft,hard)==(4096,HARD_NOFILE),"p03-limit");resource.setrlimit(resource.RLIMIT_NOFILE,(64,hard));held=[];emfile=0
  try:
   for unused in range(128):held.append(os.open(b".",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC))
  except OSError as error:need(error.errno==errno.EMFILE,"p03-emfile");emfile=1
  for fd in held:os.close(fd)
  resource.setrlimit(resource.RLIMIT_NOFILE,(4096,hard));row(rows,probe,b"soft_before",soft);row(rows,probe,b"hard_before",hard);row(rows,probe,b"soft_test",64);row(rows,probe,b"opened_fds",len(held));row(rows,probe,b"emfile",emfile)
 elif probe==b"P04":
  need(len(extra)==0,"p04-extra");definitions=tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))));need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==set() and all(signal.getsignal(number)==signal.SIG_DFL for number in definitions),"p04-signals");csv=b",".join(str(x).encode("ascii") for x in definitions);row(rows,probe,b"valid_signal_count",len(signal.valid_signals()));row(rows,probe,b"default_signal_count",len(definitions));row(rows,probe,b"defaults_sha256",hashlib.sha256(csv).hexdigest());row(rows,probe,b"mask_empty",1)
 elif probe==b"P05":
  need(len(extra)==0,"p05-extra");spawned,pids,statuses,payload=broker(probe,b"P05_WAIT",child_sha,deadline);need(spawned==2,"p05-count");row(rows,probe,b"wnohang_zero",1);row(rows,probe,b"eintr",1);row(rows,probe,b"echild",1);row(rows,probe,b"child_pids",pids);row(rows,probe,b"raw_statuses",statuses);row(rows,probe,b"term_signal",int(signal.SIGTERM));row(rows,probe,b"broker_payload_hex",payload.hex())
 elif probe==b"P06":
  need(len(extra)==0,"p06-extra");values=[mono() for unused in range(4096)];need(all(values[i]<=values[i+1] for i in range(len(values)-1)),"p06-order");deltas=[values[i+1]-values[i] for i in range(len(values)-1) if values[i+1]>values[i]];need(deltas,"p06-progress");row(rows,probe,b"monotonic",1);row(rows,probe,b"observed_min_delta_ns",min(deltas));row(rows,probe,b"start_ns",values[0]);row(rows,probe,b"end_ns",values[-1]);row(rows,probe,b"deadline_checked",1)
 elif probe==b"P07":
  need(len(extra)==0,"p07-extra");r,w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK);empty=0
  try:os.read(r,1)
  except OSError as error:need(error.errno in(errno.EAGAIN,errno.EWOULDBLOCK),"p07-empty");empty=1
  need(os.write(w,b"x")==1 and os.read(r,1)==b"x","p07-byte");duplicate=os.dup(w);os.close(w);eof_before=0
  try:eof_before=int(os.read(r,1)==b"")
  except OSError as error:need(error.errno in(errno.EAGAIN,errno.EWOULDBLOCK),"p07-before")
  os.close(duplicate);eof=int(os.read(r,1)==b"");os.close(r);row(rows,probe,b"empty_eagain",empty);row(rows,probe,b"eof_before_last_writer",eof_before);row(rows,probe,b"eof_after_last_writer",eof)
 elif probe==b"P08":
  need(len(extra)==0,"p08-extra");spawned,pids,statuses,payload=broker(probe,b"P08_TOPOLOGY",child_sha,deadline);need(spawned==1,"p08-count");row(rows,probe,b"child_pids",pids);row(rows,probe,b"raw_statuses",statuses);row(rows,probe,b"same_session_group",1);row(rows,probe,b"post_pid_esrch",1);row(rows,probe,b"broker_payload_hex",payload.hex())
 elif probe==b"P09":
  need(len(extra)==0,"p09-extra");begin=mono();spawned,pids,statuses,payload=broker(probe,b"P09_KILL",child_sha,deadline);end=mono();need(spawned==1,"p09-count");row(rows,probe,b"child_pids",pids);row(rows,probe,b"raw_statuses",statuses);row(rows,probe,b"signal",int(signal.SIGKILL));row(rows,probe,b"reap_start_ns",begin);row(rows,probe,b"reap_end_ns",end);row(rows,probe,b"reaped",1)
 elif probe==b"P10":
  need(len(extra)==0,"p10-extra");spawned,pids,statuses,payload=broker(probe,b"P10_INFO16",child_sha,deadline);need(spawned==16,"p10-count");pid_values=tuple(decimal(item,2) for item in pids.split(b","));need(len(pid_values)==16,"p10-pids");row(rows,probe,b"sample_count",16);row(rows,probe,b"pids",pids);row(rows,probe,b"statuses",statuses);row(rows,probe,b"pid_duplicates",len(pid_values)-len(set(pid_values)));row(rows,probe,b"group_is_single_owned_launcher_group",1);row(rows,probe,b"reuse_proof",0)
 elif probe==b"P11":
  need(len(extra)==0,"p11-extra");directory=os.open(b".",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW);anchor=os.open(b"target",os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600,dir_fd=directory);need(os.write(anchor,b"x")==1,"p11-write");os.fsync(anchor);os.utime(b"target",ns=(1000000000,1000000000),dir_fd=directory,follow_symlinks=False);noatime=os.open(b"target",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW|os.O_NOATIME,dir_fd=directory);need(os.read(noatime,1)==b"x","p11-read");os.close(noatime);current=os.stat(b"target",dir_fd=directory,follow_symlinks=False);need(current.st_atime_ns==1000000000,"p11-noatime");created=os.fstat(anchor);os.unlink(b"target",dir_fd=directory);held=os.fstat(anchor);need((created.st_dev,created.st_ino)==(held.st_dev,held.st_ino) and held.st_nlink==0,"p11-held");os.close(anchor);os.close(directory);row(rows,probe,b"open_result",b"OK");row(rows,probe,b"atime_unchanged",1);row(rows,probe,b"cleanup_unlinked",1);row(rows,probe,b"cleanup_identity_observed",1);row(rows,probe,b"atomic_unlink_proof",0);row(rows,probe,b"scope_single_inode",1)
 elif probe==b"P12":
  need(len(extra)==0,"p12-extra");spawned,pids,statuses,payload=broker(probe,b"P12_CHAIN",child_sha,deadline);need(spawned==1,"p12-count");row(rows,probe,b"child_pids",pids);row(rows,probe,b"raw_statuses",statuses);row(rows,probe,b"environment_count",10);row(rows,probe,b"underscore_absent",1);row(rows,probe,b"real_payload_invoked",0);row(rows,probe,b"broker_payload_hex",payload.hex())
 elif probe==b"P13":
  need(len(extra)==0,"p13-extra");directory=os.open(b".",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW);anchor=os.open(b"a",os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600,dir_fd=directory);need(os.write(anchor,b"P27E001\n")==8,"p13-write");os.fsync(anchor);os.link(b"a",b"b",src_dir_fd=directory,dst_dir_fd=directory,follow_symlinks=False);created=os.fstat(anchor);os.unlink(b"a",dir_fd=directory);path=os.stat(b"b",dir_fd=directory,follow_symlinks=False);need((created.st_dev,created.st_ino)==(path.st_dev,path.st_ino),"p13-link");os.fsync(directory);os.unlink(b"b",dir_fd=directory);need(os.fstat(anchor).st_nlink==0,"p13-held");os.close(anchor);os.close(directory);row(rows,probe,b"file_fsync_returned",1);row(rows,probe,b"hardlink_noreplace_returned",1);row(rows,probe,b"inode_preserved",1);row(rows,probe,b"dir_fsync_returned",1);row(rows,probe,b"post_unlink_absent",1);row(rows,probe,b"cleanup_unlinked",1);row(rows,probe,b"durability_proof",0);row(rows,probe,b"rename_atomicity_proof",0)
 else:raise Fail("probe-unreachable")
 finish=mono();need(start<=finish<=deadline,"probe-bound");row(rows,probe,b"marker_image_dev",image_key[0]);row(rows,probe,b"marker_image_ino",image_key[1]);row(rows,probe,b"marker_image_sha256",PY_SHA);row(rows,probe,b"probe_start_ns",start);row(rows,probe,b"probe_finish_ns",finish);row(rows,probe,b"probe_elapsed_ns",finish-start);row(rows,probe,b"probe_bound_ns",total_ns);row(rows,probe,b"primary_failure",b"none");row(rows,probe,b"cleanup_failure",b"none");row(rows,probe,b"result",b"PASS");result=b"PASS"
except BaseException as error:
 primary=(os.fsencode(str(error)).replace(b"_",b"-") if isinstance(error,Fail) else ("exception-"+type(error).__name__).encode("ascii","strict").lower())
if result==b"PASS":
 output=b"P27E001V8|marker=report|schema=6|probe="+probe+b"\n"+b"\n".join(rows)+b"\nP27E001V8|probe="+probe+b"|result=PASS\n";write_exact(1,output,deadline);raise SystemExit(0)
failure=b"P27E001V8|marker=failure|probe="+probe+b"|primary_failure="+primary+b"|result=FAIL\n"
try:write_exact(1,failure,mono()+100000000)
except BaseException:pass
raise SystemExit(90)
UNIFIED MARKER V8 SOURCE END

## 8. Exact nested childless leaf source

The following standalone record is byte-identical to the marker's embedded
CHILD_SOURCE payload. The later binder supplies this exact record separately
to the outer broker. It has five modes and no process-creation or child-wait
ownership surface.

NESTED CHILD V8 SOURCE BEGIN
import hashlib
import os
import resource
import signal
import stat
import sys
import time
P=b"/root/miniconda3/bin/python3"
R=b"/root/miniconda3/bin/python3.12"
N=30626264
H=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
E={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
class F(Exception):pass
def n(v,c):
 if not v:raise F(c)
def d(x):
 b=os.fsencode(x);n(b and b.isdigit()and str(int(b)).encode("ascii")==b,"decimal");return int(b)
def h(fd,size):
 os.lseek(fd,0,os.SEEK_SET);z=hashlib.sha256();m=0
 for unused in range((size+1048575)//1048576+1):
  x=os.read(fd,min(1048576,size-m+1))
  if not x:break
  m+=len(x);n(m<=size,"growth");z.update(x)
 n(m==size,"short");return z.hexdigest().encode("ascii")
mode=b"invalid";code=91;a=b=-1
try:
 n(len(sys.argv)==5 and sys.argv[0]=="-c","argv");mode=os.fsencode(sys.argv[1]);deadline=d(sys.argv[2]);safe=os.fsencode(sys.argv[3]);source_sha=os.fsencode(sys.argv[4]);n(mode in(b"INFO",b"BLOCK0",b"EXIT23",b"TERM",b"CHAIN"),"mode")
 n(sys.executable==P.decode("ascii")and dict(os.environb)==E and hashlib.sha256(os.fsencode(sys.orig_argv[8])).hexdigest().encode("ascii")==source_sha,"runtime")
 resource.setrlimit(resource.RLIMIT_NOFILE,(4096,1048576));resource.setrlimit(resource.RLIMIT_CPU,(3,3));resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456));resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 definitions=tuple(sorted(int(x)for x in signal.valid_signals()if int(x)not in(int(signal.SIGKILL),int(signal.SIGSTOP))));signal.pthread_sigmask(signal.SIG_SETMASK,set())
 for number in definitions:signal.signal(number,signal.SIG_DFL)
 n(os.getcwdb()==safe and time.monotonic_ns()<=deadline,"leaf-context");a=os.open(R,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);b=os.open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC);sa=os.fstat(a);sb=os.fstat(b);n((sa.st_dev,sa.st_ino,sa.st_size)==(sb.st_dev,sb.st_ino,N)and h(a,N)==h(b,N)==H,"image")
 phase=b"ready" if mode in(b"BLOCK0",b"EXIT23",b"TERM")else b"terminal";line=b"P27E001V8|child=observation|mode="+mode+b"|pid="+str(os.getpid()).encode("ascii")+b"|sid="+str(os.getsid(0)).encode("ascii")+b"|pgid="+str(os.getpgrp()).encode("ascii")+b"|image_sha="+H+b"|source_sha="+source_sha+b"|cwd_hex="+safe.hex().encode("ascii")+b"|phase="+phase+b"|result=PASS\n";n(os.write(1,line)==len(line),"write")
 if mode in(b"BLOCK0",b"EXIT23"):n(os.read(3,1)==b"G","gate");code=23 if mode==b"EXIT23"else 0
 elif mode==b"TERM":os.kill(os.getpid(),signal.SIGTERM)
 else:code=0
finally:
 for fd in(a,b):
  if fd>=0:
   try:os.close(fd)
   except BaseException:code=92
raise SystemExit(code)
NESTED CHILD V8 SOURCE END

## 9. Preserved probe and framing table

The actual UNIFIED MARKER V8 branch chain contains exactly one initial if and
fourteen peer elif heads in this byte order. Each row states whether the
branch is local or uses the sole-owner broker and the preserved observation.

ID    execution owner  broker operation  preserved observation
P00   outer broker     P00_E2BIG         251414-byte source item, E2BIG-or-return partition
P01D  marker local     none              image, mapped libc, confstr and builtin surface
P01C  marker + outer   P01C_INFO         exact 13-field seal then one INFO leaf
P02   marker local     none              isolated argv/environment/cwd/FD census
P03   marker local     none              RLIMIT_NOFILE lowering and EMFILE observation
P04   marker local     none              complete catchable default/mask normalization
P05   outer broker     P05_WAIT          WNOHANG/EINTR/exit/ECHILD/TERM status family
P06   marker local     none              monotonic ordering, resolution and headroom
P07   marker local     none              nonblocking pipe readiness/HUP/EOF transition
P08   outer broker     P08_TOPOLOGY      same session/group, kill-zero and post-reap absence
P09   outer broker     P09_KILL          exact SIGKILL latency and physical reap status
P10   outer broker     P10_INFO16        exactly sixteen sequential INFO leaves
P11   marker local     none              held inode, O_NOFOLLOW scope and unlink observation
P12   outer broker     P12_CHAIN         env-to-bash-to-Python exec chain, no real payload
P13   marker local     none              file fsync, hardlink transfer, dir fsync and unlink

The raw P10 suite has one finite broker operation named P10_INFO16. The outer
contains the exact loop `for sample in range(16)` and run_leaf completes and
exact-reaps one direct child before the next iteration. Therefore the maximum
simultaneous child role count is one and P10 cannot exceed four total live
slots L/K/M/C.

P01C consumes exactly these thirteen fields in this order before broker
admission:

index  field                 grammar
0      libc_path_hex         lowercase even hex plus decoded-byte round trip
1      libc_map_dev          canonical decimal
2      libc_map_ino          canonical decimal
3      libc_mode             canonical octal
4      libc_nlink            canonical decimal
5      libc_uid              canonical decimal
6      libc_gid              canonical decimal
7      libc_bytes            canonical decimal
8      libc_sha256           exact 64 lowercase hex plus byte round trip
9      libc_confstr_hex      lowercase even hex, ASCII decode/re-encode and byte round trip
10     python_image_dev      canonical decimal
11     python_image_ino      canonical decimal
12     python_image_sha256   exact 64 lowercase hex plus byte round trip

The expected tuple is constructed only from those canonical values. A fresh
image and libc observation constructs the actual tuple in the same order;
inequality fails before P01C_INFO. EXTRA[9] additionally requires decoded
ASCII bytes to decode and re-encode identically and requires their raw hex to
equal the supplied field exactly.

The only accepted child modes remain exactly:

INFO    immediate terminal observation and status zero
BLOCK0  ready observation, exact one-byte gate, then status zero
EXIT23  ready observation, exact one-byte gate, then status 23
TERM    ready observation followed by self SIGTERM
CHAIN   terminal observation after the fixed env/bash exec chain

No sixth mode, wildcard mode, arbitrary argv, arbitrary environment or
caller-supplied executable is accepted. P12's empty environment and fixed
/usr/bin/env, /usr/bin/bash and Python paths are constructed by the outer.

## 10. Closed broker grammar and state table

The sole request grammar is one strict ASCII/LF line:

P27E001V8|broker=request|seq=0|probe=ID|op=OP|child_sha=H64|end=1

ID must equal the outer-bound probe. H64 must equal the separately bound
NESTED CHILD V8 identity. OP must be one of exactly seven values:

P00_E2BIG
P01C_INFO
P05_WAIT
P08_TOPOLOGY
P09_KILL
P10_INFO16
P12_CHAIN

There is exactly one sequence number and one request. A request is admitted
only after complete newline framing, ASCII/control-byte checks, exact field
count and order, ID binding, OP membership, child hash equality, slot-bound
availability and operational deadline checks. A partial or malformed request
does not reach spawn_owned. Once any failure is latched, admission remains
closed. A returned PID is immediately in slots even if the later deadline,
pipe close, role telemetry, response construction or response write fails.

The response grammar is likewise one line with exact order:

P27E001V8|broker=response|seq=0|probe=ID|op=OP|spawned=N|reaped=N|pids=CSV|statuses=CSV|payload_hex=HEX|result=PASS

The response construction is textually dominated by the assertion that each
request PID has slot state reaped and a physical raw status. N must equal the
number of exact returned PIDs and reaped must equal N. PID/status metadata is
never used as cleanup discovery. A response or EOF is evidence downstream of
exact reap and is never a substitute for it.

Registry state transitions are:

event                                      required slot state
successful spawn return                    immediate (live, unknown, role, returned)
role/map/list/deadline/framing failure      unchanged live slot discoverable by slots
signal return or ProcessLookupError         unchanged live slot
WNOHANG returns zero                        unchanged live slot
exact wait returns same PID and raw status  (reaped, status, role, reaped)
cleanup enumeration                         tuple(sorted(slots)), never role metadata alone
outer completion                            every registry entry reaped with physical status

## 11. Finite cleanup and premise proof

E0346 supplies two positive execution-domain premises. First, after the outer
successfully sends exact-PID SIGKILL to a direct leaf, within
KILL_REAP_PROGRESS_NS=250000000 that leaf becomes waitable and the outer is
scheduled sufficiently for exact WNOHANG wait on that PID to return its raw
status. Second, no actor, ancestor, supervisor, in-scope signal or resource
hard limit terminates the outer while any owning slot is live or unknown.

The outer is outside G, blocks every catchable in-scope signal before the
first spawn, and requires an infinite CPU hard limit before the first spawn.
It never joins G and never lowers its own hard CPU limit. CPU/AS/FSIZE/CORE
limits are set only inside childless M and C leaves. Default-fatal or hard
death of L, M or C therefore creates a directly waitable outer child and can
never orphan a process, because all non-outer records have zero child
ownership. K blocks catchable signals and is an outer direct child killed
last.

The exact finite arithmetic is:

TERM_ALLOWANCE_NS + KILL_REAP_PROGRESS_NS + SYSCALL_OVERHEAD_NS
= 100000000 + 250000000 + 50000000
= 400000000 PER_NONKEEPER_CLEANUP_NS.

(MAX_LIVE_SLOTS - 1) * PER_NONKEEPER_CLEANUP_NS
+ KEEPER_FINALIZATION_NS
= 3 * 400000000 + 300000000
= 1500000000 DERIVED_CLEANUP_GUARD_NS.

Before spawning, the source proves MAX_LIVE_SLOTS-1 is no greater than
(2^63-1-KEEPER_FINALIZATION_NS)/PER_NONKEEPER_CLEANUP_NS and then recomputes
the exact guard. Each cleanup start separately proves that adding the guard
cannot overflow. Each post-KILL deadline separately proves that adding the
syscall allowance cannot overflow. TOTAL_NS is greater than the guard.

Cleanup permanently closes broker admission, then performs these exhaustive
registry sweeps:

1. Every live role child, in ascending exact PID order.
2. The live marker leaf, after all child roles are physically reaped.
3. The live launcher leaf, after marker is physically reaped.
4. The keeper leaf, only after all non-keeper roles are physically reaped.

For each non-keeper live slot, an initial exact WNOHANG observation may reap
it. Otherwise exact-PID TERM is followed by a finite 100000000 ns WNOHANG
grace. If still live, exact-PID KILL is followed by a finite premise-bounded
WNOHANG loop ending only on the exact returned PID and raw status. Keeper
skips ineffective TERM, receives exact-PID KILL and has its own 300000000 ns
final allowance. The total serialized path fits the derived guard.

No delivered group signal occurs. An optional later killpg(G,0) ESRCH check
may observe group absence only after every direct slot is reaped. Group
absence, keeper EOF, launcher EOF, marker output, broker response, signal
return and elapsed grace never mutate a slot and never prove descendant
cleanup. Outside the explicit progress or owner-survival premises the source
claims no authoritative completion; it does not attribute the finite bound
to POSIX alone.

Normal and exceptional edges close as follows:

- A spawn exception has no returned PID and therefore creates no slot.
- Every successful return is registered before deadline postcheck or any
  framing, list, map, response, telemetry, drain or validation operation.
- A full request followed by any broker failure leaves every returned child
  in the sole registry; a partial request creates none.
- Operational deadline failure creates a fresh derived cleanup guard rather
  than consulting the expired work deadline.
- Marker or launcher default-fatal/hard death is safe because each is a
  direct outer-owned childless leaf.
- Child fatality is safe for the same reason and is exact-reaped before any
  response can be emitted.
- Outer failure while L/K/M/C are live cannot kill or orphan them: the
  owner-survival premise keeps O alive and scheduled through registry cleanup.
- Cleanup-error telemetry can only demote. It cannot remove a slot, reorder K
  ahead of a non-keeper or authorize completion with a live entry.

## 12. Closed paths, APIs and safety preservation

Fixed absolute paths are limited to the frozen ledger and V8 control,
/root/miniconda3/bin/python3, its fixed python3.12 target, /proc/self/exe,
/proc/self/maps, /tmp, /usr/bin/env, /usr/bin/bash and the fixed PATH value
/usr/bin:/bin. The only generated component is
p27-e001-host-v8- plus one bound 64-lowercase-hex authorization ID. It is
checked against slash, dot-dot, build, evidence and recovery-root spellings.

The outer creates that directory with mode 0700 using a held /tmp directory
FD, opens it with O_DIRECTORY|O_NOFOLLOW, changes into it before any leaf,
and cleans only the fixed local names target, a and b after identity/type
checks. P11 and P13 are the only branches that create filesystem objects.
There is no glob, recursion, wildcard deletion, directory discovery or broad
cleanup.

The closed process API is signal masks/handlers, pipe2, exact-PID kill,
optional killpg signal-zero observation, the sole outer creation call and
outer-only exact wait calls. Non-outer sources have no process-creation call and no
child-wait call. There is no dynamic import, eval, exec-as-language,
compilation, ctypes, prctl, namespace creation, chroot, setuid, setgid,
subprocess, multiprocessing, socket, pty, os.walk, tempfile, pathlib, glob or
shutil surface. The fixed P12 shell exec chain is transported as argv and is
not a parser for caller input.

All records use fixed caps, exact LF framing, strict field counts, canonical
decimal/octal/lowercase-hex grammars, exact byte round trips and write-once
primary failure. Cleanup uncertainty always demotes. Host observations remain
observations; they do not prove future scheduling, future identities, libc
internals, universal PID nonreuse, crash durability or any execution outside
the two explicit E0346 premises.

## 13. Current correction-class census

V8 preserves the eighteen Host V7 classes as inert failed-history inputs and
adds four corrected-specification classes. The current exact count is 22:

1. isolated exact Python image, argv, flags and ten-entry environment;
2. closed absolute paths, component-safe workspace and held identities;
3. one absolute monotonic attempt bound with post-call checks;
4. complete P00-P13 branch order and one-attempt binding;
5. write-once primary failure and separately demoting cleanup failure;
6. exact stdout, stderr, request, response and terminal LF framing;
7. P00 complete synthetic source item and E2BIG partition;
8. P01D/P01C mapped-libc, image and backend observations;
9. closed inherited descriptors and fixed pipe-node roles;
10. exact signal-default and mask observations;
11. P10 sixteen-child serialization and peer indentation;
12. five complete child modes with self-binding image/source observations;
13. ordered P01C 13-field canonical raw/decoded grammar including EXTRA[9];
14. fixed P11/P13 held-inode, nofollow and unlink containment;
15. observation-versus-premise and durability nonclaims;
16. immediate successful-return owning-slot registration;
17. registry-only census and exact returned-PID physical reap transition;
18. fresh cleanup state independent of an expired operational deadline;
19. structurally flattened outer-only ownership for L/K/M/C;
20. strict finite closed-enum broker admission and post-reap response;
21. child-before-marker-before-launcher-before-keeper exact-PID cleanup with
    zero delivered group cleanup signals and no owning leaf fatality;
22. quantified KILL_REAP_PROGRESS_NS plus owner-survival binding and the
    overflow-checked 1500000000 ns serialized cleanup guard.

There is no stale current fifteen-, eighteen-, nineteen-, twenty- or
twenty-one-class claim. Counts referring to Host V7 history remain explicitly
historical and cannot override the current 22.

V8 STAGED PRESERVATION AND PROOF APPEND COMPLETE

## 14. Final raw identities and author closure

The final inert raw-byte replay located each exact standalone BEGIN and END
line once, excluded both delimiter lines, retained every intervening byte and
the LF immediately before END, and obtained:

OUTER_CONTROLLER_V8 bytes=23612 LF=285 sha256=e8c18c6385124e5e61ff86fec3fdf4464f1034c7ee278dd2a3e17b638480bcec final_byte=0a
GROUP_KEEPER_V8 bytes=1243 LF=23 sha256=8bdd1f75edc7c85296e4790a866be1a413452bad05984c06b40518b81278ec9d final_byte=0a
OWNED_LAUNCHER_V8 bytes=1159 LF=24 sha256=8f6ab849192ac9865eacc8b60adcca71172f81e292dafa1860787093b43825b2 final_byte=0a
UNIFIED_MARKER_V8 bytes=20735 LF=201 sha256=29368b0df7e005f4f182f097d61ece17aedebded47037568fe3bdda36a2fe36f final_byte=0a
NESTED_CHILD_V8 bytes=2827 LF=42 sha256=0e48b1ad9511470c37268dd79fb41a098afb2baa60a8ea604780bc349c760d78 final_byte=0a

The marker-embedded CHILD_SOURCE is independently the same
2827/42/0e48b1ad9511470c37268dd79fb41a098afb2baa60a8ea604780bc349c760d78
byte stream as the standalone nested record. All five delimiter pairs are
unique. All five streams end in LF and contain strict ASCII bytes only.

The authoring boundary remains exact E0346:

ledger_bytes=2036397
ledger_LF=21983
ledger_sha256=b5b39ba94477ce193e5ed24dd175fe2ac2132661e1b895fa52ee5c7792759066
ledger_terminal=BATCH07_P27_PROBE_RECOVERY_E001_HOST_V8_UNSAT_SPECIFICATION_RECORDED_MINIMUM_PROGRESS_PREMISE_CORRECTED_AND_CONTROL_REAUTHORIZED
manifest_rows=134
manifest_framing_bytes=21535
manifest_sha256=3325e9afc341eb4ce669718da63bc1d79e892c00862c4898a5c185de8c59e52b

The prospective/literal-history qualification is unchanged. Frozen Host V7,
V6, V5 and V4 remain respectively
174525/2211/07bf1c8a10e729b19acabc9576d6bfa35afb5bfede892b0fea61c3143cda6d91,
166498/2074/90158178795619c3b5ac94cfc87b92246a5f68c51abaff8f0acbf15481c643ec,
164883/2052/8e5207770ad64300212260e4bf5604d75e6b4a36852efded632676d43cc84370,
and 147429/1801/238bff83783cedfe5193b735583a749271cca53af21b9a2f953904f6ee36ddeb.
Binder V8 remains
279288/7303/3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4.

The final source-level closure is:

- The outer has the only process-creation call and every successful return is
  immediately registered live/unknown before its first postcheck.
- The outer has all child-wait ownership. Keeper, launcher, marker and nested
  sources have zero process-creation and zero child-wait ownership calls.
- MAX_LIVE_SLOTS is four: direct launcher, keeper, marker and at most one
  serial broker child. P10 creates and exact-reaps sixteen children one at a
  time through the same registry-owning outer site.
- The seven-operation broker grammar is finite, ordered and hash-bound. A
  partial, malformed, duplicate or late request creates no child. Completion
  response text is constructed only after exact physical child reap.
- Registry discovery is exhaustive and independent of PID telemetry, modes,
  response text and scalar role names. Reaped state is written only when the
  sole outer exact wait returns the same owned PID and raw status.
- Cleanup is fresh after operational expiry and deterministically orders all
  child roles before marker, marker before launcher and launcher before
  keeper. It uses exact-PID TERM/KILL only and no delivered group cleanup
  signal. Optional group absence is downstream observation only.
- KILL_REAP_PROGRESS_NS is the positive finite 250000000 ns E0346 premise.
  MAX_LIVE_SLOTS=4, TERM_ALLOWANCE_NS=100000000,
  SYSCALL_OVERHEAD_NS=50000000 and KEEPER_FINALIZATION_NS=300000000 derive,
  with explicit overflow guards, the exact 1500000000 ns serialized cleanup
  guard.
- The group-external outer blocks in-scope catchable termination signals,
  owns no finite CPU hard limit while a slot is live, and is protected by the
  explicit owner-survival premise. Hard/default-fatal limits apply only to
  direct outer-owned childless leaves.
- P00-P13, exact P10=16 serialization, P01C's ordered 13-field seal including
  EXTRA[9], the five child modes, fixed path/API containment, filesystem
  identity cleanup, framing and observation-versus-premise controls remain
  present in the actual inert sources and tables.
- The exact current correction-class count is 22. No historical count is a
  current claim.

This author stop asserts source/control construction only. Probe attempts,
source executions, child creations, actor runs, fixtures, payloads, binders,
validators, microtests and build/evidence/root accesses all remain zero. It
grants no execution, review PASS, manifest extension, validator, build, PDF,
release or downstream authority. A later event must independently bind this
whole file and open fresh separated static reviews; a still later actor must
independently bind the same progress and owner-survival premises before any
execution could be considered.

BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V8_AUTHOR_STOP
