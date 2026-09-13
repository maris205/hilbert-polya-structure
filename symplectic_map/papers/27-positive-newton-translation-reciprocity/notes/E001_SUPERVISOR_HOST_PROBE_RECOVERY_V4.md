# E001 Supervisor Host-Probe Recovery Control V4

Status: INERT ASCII CONTROL AND INERT ASCII SOURCE TEXT ONLY. NO EXECUTION
AUTHORITY.

## 1. Authority and immutable history

This is the single fresh host-probe V4 path authorized by E0337. Host-probe
V1, V2, and V3 remain immutable failed history. This file does not edit,
replace, reinterpret, execute, import, parse, compile, or evaluate any old
control or any source record. Authoring created no process, pipe, directory,
fixture, report, evidence, or result. It opened no build, evidence, recovery
root, payload, validator, binder, or marker-program path. Source execution
count and probe attempt count are both zero.

The exact E0337 authoring anchor is:

```text
path=/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md
dev=2431
ino=12439253869
mode=0644
nlink=1
uid=0
gid=0
bytes=1928853
LF=21224
sha256=6c733439a5295fd4a563036bdfdb3ad045129f869a226cf90395cbb638767aec
terminal=BATCH07_P27_PROBE_RECOVERY_E001_ACTOR_V3_STATIC_PASS_AND_DERIVATION_HOST_V3_FAILURE_RECORDED_AND_V4_CONTROLS_AUTHORIZED
```

The frozen failed V3 identity is:

```text
path=papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V3.md
dev=2431
ino=5915986573
mode=0644
nlink=1
uid=0
gid=0
bytes=112237
LF=1759
sha256=c1d8569fde501b068bef75a65b18e13479e9343f3d4422475287ad9ccac77ddf
terminal=BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V3_AUTHOR_STOP
```

No author stop grants execution. A later ledger event must independently bind
this entire file, all exact source identities, one exact probe, one fresh
64-lowercase-hex authorization ID, and one attempt. There is no retry,
fallback, repair, parser widening, alternate executable, or second sample.

## 2. Frozen production premise and executable premise

The production premise remains the frozen V8 control only:

```text
path=papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_BINDER_RECOVERY_V8.md
dev=2431
ino=5917339790
mode=0644
nlink=1
uid=0
gid=0
bytes=279288
LF=7303
sha256=3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4
terminal=BATCH07_P27_E001_SUPERVISOR_BINDER_RECOVERY_V8_AUTHOR_STOP
normalized_source_bytes=251414
normalized_source_LF=6839
normalized_source_sha256=34449280b51dae17eeb5eb841296e99d25512867185525fec39dc73a39dfc076
normalized_source_final_byte=41
normalized_source_apostrophe_dollar_backtick=0,0,0
```

No source record below opens or embeds V8. P00 constructs a same-length
synthetic Python source from the frozen self-binding child stub and inert
comment padding. The exact interpreter premise is:

```text
spelling=/root/miniconda3/bin/python3
literal_symlink_target=python3.12
resolved_path=/root/miniconda3/bin/python3.12
resolved_bytes=30626264
resolved_sha256=9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101
watchdog_flags=-I -S -B -P -X utf8 -c
```

Every Python layer uses the exact ten-key environment below. No inherited
entry is accepted.

```text
LANG=C
LC_ALL=C
PATH=/usr/bin:/bin
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
PYTHONIOENCODING=UTF-8:strict
PYTHONNOUSERSITE=1
PYTHONSAFEPATH=1
PYTHONUTF8=1
TZ=UTC
```

## 3. Ownership and deadline construction

V4 freezes three source records: OUTER CONTROLLER V4, OWNED LAUNCHER V4, and
UNIFIED MARKER V4. The outer controller performs no repository, procfs,
executable-image, pathname-identity, mountinfo, inventory, or cleanup read.
It owns exactly one direct launcher session/group and gives that launcher an
absolute monotonic total deadline. The owned launcher is therefore the exact
separately owned helper for every potentially blocking source, image, procfs,
and filesystem phase. If any such syscall does not return, the outer
controller's nonblocking poll/WNOHANG state machine reaches TERM/KILL and the
attempt cannot PASS. A returned helper result is accepted only after a fresh
`now <= deadline` check.

The launcher verifies its own image and the still-live outer image. The
marker verifies its own image. Every nested Python child runs one frozen
self-binding child stub before it can emit an accepted observation. Thus no
accepted branch borrows another process's image proof. P00 pads that same
stub to exactly 251414 source bytes; it is not an all-comment child.

The caller supplies `TOTAL_NS` from 2000000000 through 10000000000. The outer
reserves the last 500000000 ns for cleanup and reporting. All probe work,
launcher cleanup, terminal identity checks, rmdir, final parsing, and report
acceptance must complete with nonnegative elapsed time no greater than the
same total bound.

## 4. Exact outer-controller source

The exact invocation tail is:

```text
PROBE AUTH_ID LAUNCHER_SOURCE LAUNCHER_SHA256 MARKER_SOURCE MARKER_SHA256
TOTAL_NS LEDGER_BYTES LEDGER_LF LEDGER_SHA256 LEDGER_TERMINAL CONTROL_BYTES
CONTROL_LF CONTROL_SHA256 CONTROL_TERMINAL [PROBE_ARGS...]
```

```text
OUTER CONTROLLER V4 SOURCE BEGIN
import errno
import fcntl
import hashlib
import os
import resource
import select
import signal
import sys
import time

PYTHON=b"/root/miniconda3/bin/python3"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
RAW_CAP=524288
TELE_CAP=262144
RESERVE_NS=500000000
HARD_NOFILE=1048576

class Fail(Exception): pass

def need(v,code):
 if not v: raise Fail(code)

def mono():
 v=time.monotonic_ns(); need(type(v) is int and v>=0,"clock-value"); return v

def before(deadline,code):
 n=mono(); need(n<=deadline,code+"-pre"); return n

def after(deadline,code):
 n=mono(); need(n<=deadline,code+"-post"); return n

def canonical_decimal(raw,minimum=0,maximum=(1<<63)-1):
 need(type(raw) is bytes and raw and all(48<=c<=57 for c in raw),"decimal-grammar")
 value=int(raw); need(str(value).encode("ascii")==raw and minimum<=value<=maximum,"decimal-canonical"); return value

def canonical_hex(raw,count):
 need(type(raw) is bytes and len(raw)==count and all(c in b"0123456789abcdef" for c in raw),"hex-canonical"); return raw

def set_nonblock(fd,deadline):
 before(deadline,"fcntl-get"); flags=fcntl.fcntl(fd,fcntl.F_GETFL); after(deadline,"fcntl-get")
 before(deadline,"fcntl-set"); fcntl.fcntl(fd,fcntl.F_SETFL,flags|os.O_NONBLOCK); after(deadline,"fcntl-set")

def close_capture(fd,deadline,failures,label):
 if fd<0: return
 try:
  before(deadline,label+"-close"); os.close(fd); after(deadline,label+"-close")
 except BaseException as e:
  failures.append((label+":"+type(e).__name__).encode("ascii","strict"))

def write_exact(fd,data,deadline):
 set_nonblock(fd,deadline); poller=select.poll(); poller.register(fd,select.POLLOUT|select.POLLERR|select.POLLHUP); pos=0
 for unused in range(8192):
  if pos==len(data): after(deadline,"write-complete"); return
  before(deadline,"write")
  try:
   count=os.write(fd,data[pos:]); after(deadline,"write"); need(count>0,"write-zero"); pos+=count
  except BlockingIOError: pass
  except InterruptedError: continue
  before(deadline,"write-poll"); poller.poll(max(0,min(10,(deadline-mono()+999999)//1000000))); after(deadline,"write-poll")
 raise Fail("write-iterations")

def drain(fd,buf,cap,deadline,label):
 eof=False
 for unused in range(256):
  before(deadline,label+"-read")
  try: chunk=os.read(fd,4096)
  except BlockingIOError: after(deadline,label+"-read"); break
  except InterruptedError: after(deadline,label+"-read"); continue
  after(deadline,label+"-read")
  if not chunk: eof=True; break
  buf.extend(chunk); need(len(buf)<=cap,label+"-cap")
 return eof

def physical_reap(slots,pid,status):
 slots[pid]=(0,status)

def fd_census(limit,deadline):
 got=[]
 for fd in range(limit):
  before(deadline,"fd-census")
  try: fcntl.fcntl(fd,fcntl.F_GETFD); after(deadline,"fd-census")
  except OSError as e:
   after(deadline,"fd-census")
   if e.errno==errno.EBADF: continue
   raise
  got.append(fd)
 return tuple(got)

def wait_owned(slots,pid,deadline):
 need(pid in slots and slots[pid][0]==1,"wait-ownership")
 before(deadline,"waitpid")
 try: got,status=os.waitpid(pid,os.WNOHANG)
 except InterruptedError: after(deadline,"waitpid"); return 0
 except ChildProcessError as e: raise Fail("wait-echild") from e
 if got==pid: physical_reap(slots,pid,status)
 after(deadline,"waitpid")
 need(got in (0,pid),"wait-return"); return got

def parse_record(line,kind,fields):
 need(type(line) is bytes and line and b"\r" not in line and b"\x00" not in line,"record-frame")
 try: line.decode("ascii")
 except UnicodeDecodeError as e: raise Fail("record-ascii") from e
 parts=line.split(b"|"); need(len(parts)==2+len(fields),"record-field-count")
 need(parts[0]==b"P27E001V4" and parts[1]==kind,"record-prefix")
 out={}
 for item,(key,grammar) in zip(parts[2:],fields):
  prefix=key+b"="; need(item.startswith(prefix) and item.count(b"=")==1,"record-order")
  value=item[len(prefix):]; need(value,"record-empty")
  if grammar==b"d": canonical_decimal(value)
  elif grammar==b"p": canonical_decimal(value,2)
  elif grammar==b"h64": canonical_hex(value,64)
  elif grammar==b"auth": canonical_hex(value,64)
  elif grammar==b"flag": need(value in (b"0",b"1"),"record-flag")
  elif grammar==b"result": need(value in (b"PASS",b"FAIL"),"record-result")
  elif grammar==b"token": need(all(c in b"abcdefghijklmnopqrstuvwxyz0123456789_-" for c in value),"record-token")
  else: raise Fail("record-grammar")
  out[key]=value
 return out

WORKER_FIELDS=((b"probe",b"token"),(b"auth_id",b"auth"),(b"outer_pid",b"p"),(b"launcher_pid",b"p"),(b"marker_pid",b"d"),(b"marker_raw_status",b"d"),(b"marker_reaped",b"flag"),(b"nested_spawned",b"d"),(b"nested_reaped",b"d"),(b"marker_stdout_bytes",b"d"),(b"marker_stdout_sha256",b"h64"),(b"marker_stderr_bytes",b"d"),(b"marker_stderr_sha256",b"h64"),(b"nested_telemetry_bytes",b"d"),(b"nested_telemetry_sha256",b"h64"),(b"primary_failure",b"token"),(b"cleanup_failure",b"token"),(b"total_cleanup_pass",b"flag"),(b"probe_start_ns",b"d"),(b"probe_finish_ns",b"d"),(b"probe_elapsed_ns",b"d"),(b"probe_bound_ns",b"d"),(b"result",b"result"))
OWNERSHIP_FIELDS=((b"probe",b"token"),(b"launcher_pid",b"p"),(b"launcher_sid",b"p"),(b"launcher_pgid",b"p"),(b"marker_pid",b"p"))
SPAWN_FIELDS=((b"pid",b"p"),(b"mode",b"token"))
REAP_FIELDS=((b"pid",b"p"),(b"mode",b"token"),(b"raw_status",b"d"))
RAW_FIELDS=((b"pid",b"p"),(b"seq",b"d"),(b"bytes",b"d"),(b"sha256",b"h64"),(b"hex",b"token"))

def parse_telemetry(raw,probe,pid,marker_pid,spawned,expected_bytes,expected_sha):
 need(raw.endswith(b"\n") and b"\r" not in raw and b"\x00" not in raw,"telemetry-frame")
 lines=raw.split(b"\n"); need(lines[-1]==b"" and len(lines)>=2 and all(lines[:-1]),"telemetry-lines")
 ownership=parse_record(lines[0],b"launcher=ownership",OWNERSHIP_FIELDS)
 need(ownership[b"probe"]==probe and canonical_decimal(ownership[b"launcher_pid"],2)==pid and canonical_decimal(ownership[b"launcher_sid"],2)==pid and canonical_decimal(ownership[b"launcher_pgid"],2)==pid and canonical_decimal(ownership[b"marker_pid"],2)==marker_pid,"telemetry-ownership")
 nested=b"\n".join(lines[1:-1])+(b"\n" if len(lines)>2 else b"")
 need(len(nested)==expected_bytes and hashlib.sha256(nested).hexdigest().encode("ascii")==expected_sha,"telemetry-nested-identity")
 current=None; count=0
 for line in lines[1:-1]:
  if line.startswith(b"P27E001V4|child=spawn|"):
   need(current is None or current[3]==1,"telemetry-overlap"); item=parse_record(line,b"child=spawn",SPAWN_FIELDS); need(item[b"mode"] in (b"INFO",b"BLOCK0",b"EXIT23",b"TERM",b"CHAIN"),"telemetry-mode"); current=[item[b"pid"],item[b"mode"],0,0]
  elif line.startswith(b"P27E001V4|child=reap|"):
   need(current is not None and current[3]==0,"telemetry-orphan-reap"); item=parse_record(line,b"child=reap",REAP_FIELDS); need((item[b"pid"],item[b"mode"])==(current[0],current[1]),"telemetry-reap-match"); current[3]=1; count+=1
  elif line.startswith(b"P27E001V4|child=raw|"):
   need(current is not None,"telemetry-orphan-raw"); item=parse_record(line,b"child=raw",RAW_FIELDS); need(item[b"pid"]==current[0] and canonical_decimal(item[b"seq"])==current[2],"telemetry-raw-sequence"); raw=bytes.fromhex(item[b"hex"].decode("ascii")); need(raw and raw.hex().encode("ascii")==item[b"hex"] and len(raw)==canonical_decimal(item[b"bytes"]) and hashlib.sha256(raw).hexdigest().encode("ascii")==item[b"sha256"],"telemetry-raw-content"); current[2]+=1
  else: raise Fail("telemetry-record-kind")
 need((current is None and spawned==0) or (current is not None and current[3]==1),"telemetry-final-child"); need(count==spawned,"telemetry-count")

def parse_worker(raw,probe,auth,pid,stderr_raw,telemetry_raw,total_ns):
 need(raw.endswith(b"\n") and b"\r" not in raw and b"\x00" not in raw,"worker-frame")
 lines=raw.split(b"\n"); need(lines[-1]==b"" and len(lines)>=3 and all(lines[:-1]),"worker-lines")
 terminal_prefix=b"P27E001V4|worker=terminal|"
 need(lines[-2].startswith(terminal_prefix),"worker-final-line")
 need(sum(1 for line in lines[:-1] if line.startswith(terminal_prefix))==1,"worker-terminal-standalone-count")
 values=parse_record(lines[-2],b"worker=terminal",WORKER_FIELDS)
 marker_raw=b"\n".join(lines[:-2])+b"\n"
 need(values[b"probe"]==probe and values[b"auth_id"]==auth,"worker-binding")
 need(canonical_decimal(values[b"outer_pid"],2)==os.getpid() and canonical_decimal(values[b"launcher_pid"],2)==pid,"worker-topology")
 need(canonical_decimal(values[b"marker_stdout_bytes"])==len(marker_raw) and values[b"marker_stdout_sha256"]==hashlib.sha256(marker_raw).hexdigest().encode("ascii"),"worker-marker-stdout")
 need(canonical_decimal(values[b"marker_stderr_bytes"])==len(stderr_raw) and values[b"marker_stderr_sha256"]==hashlib.sha256(stderr_raw).hexdigest().encode("ascii"),"worker-marker-stderr")
 start=canonical_decimal(values[b"probe_start_ns"]); finish=canonical_decimal(values[b"probe_finish_ns"]); elapsed=canonical_decimal(values[b"probe_elapsed_ns"]); bound=canonical_decimal(values[b"probe_bound_ns"])
 need(start<=finish and elapsed==finish-start and elapsed<=bound<=total_ns,"worker-elapsed")
 need(values[b"marker_reaped"]==b"1" and values[b"marker_raw_status"]==b"0","worker-marker-status")
 need(values[b"nested_spawned"]==values[b"nested_reaped"],"worker-nested-reap")
 need(values[b"primary_failure"]==b"none" and values[b"cleanup_failure"]==b"none" and values[b"total_cleanup_pass"]==b"1" and values[b"result"]==b"PASS","worker-pass")
 parse_telemetry(telemetry_raw,probe,pid,canonical_decimal(values[b"marker_pid"],2),canonical_decimal(values[b"nested_spawned"]),canonical_decimal(values[b"nested_telemetry_bytes"]),values[b"nested_telemetry_sha256"])
 return values

primary=b"none"; cleanup_failures=[]; result=b"FAIL"; timed=0
leader=-1; slots={}; term_sent=0; kill_sent=0; group_absent=0
in_r=in_w=out_r=out_w=err_r=err_w=tele_r=tele_w=-1
stdout_raw=bytearray(); stderr_raw=bytearray(); telemetry_raw=bytearray(); out_eof=err_eof=tele_eof=False
attempt_start=mono(); attempt_finish=attempt_start; total_deadline=attempt_start; work_deadline=attempt_start
probe=b"invalid"; auth=b"0"*64; outer_source=b""; launcher_source=b""; marker_source=b""; total_ns=0

try:
 need(len(sys.argv)>=16 and sys.argv[0]=="-c","argv-count")
 probe=os.fsencode(sys.argv[1]); auth=os.fsencode(sys.argv[2]); launcher_source=os.fsencode(sys.argv[3]); launcher_sha=os.fsencode(sys.argv[4]); marker_source=os.fsencode(sys.argv[5]); marker_sha=os.fsencode(sys.argv[6])
 total_raw=os.fsencode(sys.argv[7]); ledger_bytes_raw=os.fsencode(sys.argv[8]); ledger_lf_raw=os.fsencode(sys.argv[9]); ledger_sha=os.fsencode(sys.argv[10]); ledger_terminal=os.fsencode(sys.argv[11]); control_bytes_raw=os.fsencode(sys.argv[12]); control_lf_raw=os.fsencode(sys.argv[13]); control_sha=os.fsencode(sys.argv[14]); control_terminal=os.fsencode(sys.argv[15]); extra=tuple(os.fsencode(x) for x in sys.argv[16:])
 need(probe in (b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13"),"probe-id")
 canonical_hex(auth,64); total_ns=canonical_decimal(total_raw,2000000000,10000000000)
 ledger_bytes=canonical_decimal(ledger_bytes_raw,1,400000000); ledger_lf=canonical_decimal(ledger_lf_raw,1,1000000); canonical_hex(ledger_sha,64)
 control_bytes=canonical_decimal(control_bytes_raw,1,400000000); control_lf=canonical_decimal(control_lf_raw,1,1000000); canonical_hex(control_sha,64)
 need(ledger_terminal and control_terminal and all(32<=c<=126 for c in ledger_terminal+control_terminal),"terminal-args")
 canonical_hex(launcher_sha,64); canonical_hex(marker_sha,64)
 need(launcher_source.isascii() and marker_source.isascii() and b"\x00" not in launcher_source+marker_source,"source-encoding")
 need(hashlib.sha256(launcher_source).hexdigest().encode("ascii")==launcher_sha and hashlib.sha256(marker_source).hexdigest().encode("ascii")==marker_sha,"source-hash")
 outer_source=os.fsencode(sys.orig_argv[8]); need(sys.orig_argv[:8]==[PYTHON.decode("ascii"),"-I","-S","-B","-P","-X","utf8","-c"],"outer-vector")
 need(sys.executable==PYTHON.decode("ascii") and dict(os.environb)==ENV,"outer-runtime")
 need(sys.flags.isolated==1 and sys.flags.ignore_environment==1 and sys.flags.no_site==1 and sys.flags.no_user_site==1 and sys.flags.dont_write_bytecode==1 and sys.flags.safe_path==1 and sys.flags.utf8_mode==1 and sys.flags.hash_randomization==1,"outer-flags")
 need(resource.getrlimit(resource.RLIMIT_NOFILE)[1]==HARD_NOFILE and fd_census(HARD_NOFILE,attempt_start+total_ns)==(0,1,2),"outer-initial-fds")
 need(attempt_start<=((1<<63)-1)-total_ns,"deadline-headroom"); total_deadline=attempt_start+total_ns; work_deadline=total_deadline-RESERVE_NS; after(work_deadline,"outer-validation")
 before(work_deadline,"pipe-in"); in_r,in_w=os.pipe2(os.O_CLOEXEC); after(work_deadline,"pipe-in"); close_capture(in_w,work_deadline,cleanup_failures,"stdin-w"); in_w=-1
 before(work_deadline,"pipe-out"); out_r,out_w=os.pipe2(os.O_CLOEXEC); after(work_deadline,"pipe-out")
 before(work_deadline,"pipe-err"); err_r,err_w=os.pipe2(os.O_CLOEXEC); after(work_deadline,"pipe-err")
 before(work_deadline,"pipe-tele"); tele_r,tele_w=os.pipe2(os.O_CLOEXEC); after(work_deadline,"pipe-tele")
 for fd in (out_r,err_r,tele_r): set_nonblock(fd,work_deadline)
 openfds=fd_census(HARD_NOFILE,work_deadline)
 actions=[(os.POSIX_SPAWN_DUP2,in_r,0),(os.POSIX_SPAWN_DUP2,out_w,1),(os.POSIX_SPAWN_DUP2,err_w,2),(os.POSIX_SPAWN_DUP2,tele_w,3)]
 actions.extend((os.POSIX_SPAWN_CLOSE,fd) for fd in openfds if fd>=4)
 argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",launcher_source,probe,auth,str(os.getpid()).encode("ascii"),hashlib.sha256(outer_source).hexdigest().encode("ascii"),marker_source,marker_sha,launcher_sha,str(total_deadline).encode("ascii"),str(total_ns).encode("ascii"),str(ledger_bytes).encode("ascii"),str(ledger_lf).encode("ascii"),ledger_sha,ledger_terminal,str(control_bytes).encode("ascii"),str(control_lf).encode("ascii"),control_sha,control_terminal)+extra
 need(all(type(item) is bytes and b"\x00" not in item for item in argv),"launcher-argv")
 before(work_deadline,"spawn-launcher"); leader=os.posix_spawn(PYTHON,argv,ENV,file_actions=tuple(actions),setsid=True,setsigmask=(),setsigdef=tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))); after(work_deadline,"spawn-launcher")
 need(leader>1,"launcher-pid"); slots[leader]=(1,None)
 for fd in (in_r,out_w,err_w,tele_w):
  close_capture(fd,work_deadline,cleanup_failures,"parent-child-end")
 in_r=out_w=err_w=tele_w=-1
 poller=select.poll(); poller.register(out_r,select.POLLIN|select.POLLHUP|select.POLLERR); poller.register(err_r,select.POLLIN|select.POLLHUP|select.POLLERR); poller.register(tele_r,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(40000):
  if slots[leader][0]: wait_owned(slots,leader,work_deadline)
  out_eof=drain(out_r,stdout_raw,RAW_CAP,work_deadline,"stdout") or out_eof
  err_eof=drain(err_r,stderr_raw,RAW_CAP,work_deadline,"stderr") or err_eof
  tele_eof=drain(tele_r,telemetry_raw,TELE_CAP,work_deadline,"telemetry") or tele_eof
  if slots[leader][0]==0 and out_eof and err_eof and tele_eof: break
  before(work_deadline,"outer-poll"); poller.poll(max(0,min(10,(work_deadline-mono()+999999)//1000000))); after(work_deadline,"outer-poll")
 else: raise Fail("outer-iterations")
 after(work_deadline,"launcher-complete")
 need(slots[leader][1]==0 and out_eof and err_eof and tele_eof,"launcher-completion")
 parse_worker(bytes(stdout_raw),probe,auth,leader,bytes(stderr_raw),bytes(telemetry_raw),total_ns)
 after(work_deadline,"parse-complete")
 try:
  before(work_deadline,"group-zero"); os.killpg(leader,0); after(work_deadline,"group-zero")
 except ProcessLookupError as e:
  after(work_deadline,"group-zero"); need(e.errno==errno.ESRCH,"group-zero-errno"); group_absent=1
 need(group_absent==1,"group-still-present")
 result=b"PASS"
except BaseException as e:
 if primary==b"none":
  if isinstance(e,Fail): primary=os.fsencode(str(e)).replace(b"_",b"-")
  elif isinstance(e,OSError): primary=("oserror-%d"%(e.errno if e.errno is not None else -1)).encode("ascii")
  else: primary=("exception-"+type(e).__name__).encode("ascii","strict").lower()
 if mono()>work_deadline: timed=1
finally:
 cleanup_deadline=total_deadline
 if leader>1 and leader in slots and slots[leader][0]:
  try:
   wait_owned(slots,leader,cleanup_deadline)
   if slots[leader][0]:
    before(cleanup_deadline,"term-group"); os.killpg(leader,signal.SIGTERM); after(cleanup_deadline,"term-group"); term_sent=1
    term_deadline=min(cleanup_deadline,mono()+100000000)
    for unused in range(1024):
     if slots[leader][0]: wait_owned(slots,leader,term_deadline)
     if slots[leader][0]==0: break
     before(term_deadline,"term-poll"); select.poll().poll(max(0,min(5,(term_deadline-mono()+999999)//1000000))); after(term_deadline,"term-poll")
    if slots[leader][0]:
     wait_owned(slots,leader,cleanup_deadline)
     if slots[leader][0]: before(cleanup_deadline,"kill-group"); os.killpg(leader,signal.SIGKILL); after(cleanup_deadline,"kill-group"); kill_sent=1
    for unused in range(4096):
     if slots[leader][0]: wait_owned(slots,leader,cleanup_deadline)
     if slots[leader][0]==0: break
     before(cleanup_deadline,"kill-poll"); select.poll().poll(max(0,min(5,(cleanup_deadline-mono()+999999)//1000000))); after(cleanup_deadline,"kill-poll")
   need(slots[leader][0]==0,"launcher-unreaped")
 except BaseException as e:
   cleanup_failures.append(("process:"+type(e).__name__).encode("ascii","strict").lower())
 if leader>1 and leader in slots and slots[leader][0]==0 and group_absent==0:
  try:
   before(cleanup_deadline,"cleanup-group-zero"); os.killpg(leader,0); after(cleanup_deadline,"cleanup-group-zero"); cleanup_failures.append(b"group-present")
  except ProcessLookupError as e:
   after(cleanup_deadline,"cleanup-group-zero");
   if e.errno==errno.ESRCH: group_absent=1
   else: cleanup_failures.append(b"group-zero-errno")
  except BaseException as e: cleanup_failures.append(("group:"+type(e).__name__).encode("ascii","strict").lower())
 if out_r>=0:
  try: out_eof=drain(out_r,stdout_raw,RAW_CAP,cleanup_deadline,"cleanup-stdout") or out_eof
  except BaseException as e: cleanup_failures.append(("stdout:"+type(e).__name__).encode("ascii","strict").lower())
 if err_r>=0:
  try: err_eof=drain(err_r,stderr_raw,RAW_CAP,cleanup_deadline,"cleanup-stderr") or err_eof
  except BaseException as e: cleanup_failures.append(("stderr:"+type(e).__name__).encode("ascii","strict").lower())
 if tele_r>=0:
  try: tele_eof=drain(tele_r,telemetry_raw,TELE_CAP,cleanup_deadline,"cleanup-telemetry") or tele_eof
  except BaseException as e: cleanup_failures.append(("telemetry:"+type(e).__name__).encode("ascii","strict").lower())
 for fd,label in ((in_r,"in-r"),(in_w,"in-w"),(out_r,"out-r"),(err_r,"err-r"),(tele_r,"tele-r"),(out_w,"out-w"),(err_w,"err-w"),(tele_w,"tele-w")): close_capture(fd,cleanup_deadline,cleanup_failures,label)
 attempt_finish=mono()
 if attempt_finish<attempt_start or attempt_finish>total_deadline:
  cleanup_failures.append(b"total-deadline")
 if cleanup_failures and result==b"PASS": result=b"FAIL"
 cleanup_token=b"none" if not cleanup_failures else b"present"
 if result==b"PASS" and (primary!=b"none" or cleanup_token!=b"none"): result=b"FAIL"
 rows=[b"P27E001V4|outer=report|schema=4",b"P27E001V4|probe="+probe,b"P27E001V4|auth_id="+auth,b"P27E001V4|outer_source_bytes="+str(len(outer_source)).encode("ascii"),b"P27E001V4|outer_source_sha256="+hashlib.sha256(outer_source).hexdigest().encode("ascii"),b"P27E001V4|launcher_source_bytes="+str(len(launcher_source)).encode("ascii"),b"P27E001V4|launcher_source_sha256="+hashlib.sha256(launcher_source).hexdigest().encode("ascii"),b"P27E001V4|marker_source_bytes="+str(len(marker_source)).encode("ascii"),b"P27E001V4|marker_source_sha256="+hashlib.sha256(marker_source).hexdigest().encode("ascii"),b"P27E001V4|leader_pid="+str(leader).encode("ascii"),b"P27E001V4|leader_raw_status="+str(slots.get(leader,(0,-1))[1] if leader in slots and slots[leader][1] is not None else -1).encode("ascii"),b"P27E001V4|leader_reaped="+str(int(leader in slots and slots[leader][0]==0)).encode("ascii"),b"P27E001V4|group_absent="+str(group_absent).encode("ascii"),b"P27E001V4|sigterm_sent="+str(term_sent).encode("ascii"),b"P27E001V4|sigkill_sent="+str(kill_sent).encode("ascii"),b"P27E001V4|timed="+str(timed).encode("ascii"),b"P27E001V4|primary_failure="+primary,b"P27E001V4|cleanup_failure="+cleanup_token,b"P27E001V4|stdout_bytes="+str(len(stdout_raw)).encode("ascii"),b"P27E001V4|stdout_sha256="+hashlib.sha256(stdout_raw).hexdigest().encode("ascii"),b"P27E001V4|stdout_hex="+bytes(stdout_raw).hex().encode("ascii"),b"P27E001V4|stderr_bytes="+str(len(stderr_raw)).encode("ascii"),b"P27E001V4|stderr_sha256="+hashlib.sha256(stderr_raw).hexdigest().encode("ascii"),b"P27E001V4|stderr_hex="+bytes(stderr_raw).hex().encode("ascii"),b"P27E001V4|telemetry_bytes="+str(len(telemetry_raw)).encode("ascii"),b"P27E001V4|telemetry_sha256="+hashlib.sha256(telemetry_raw).hexdigest().encode("ascii"),b"P27E001V4|telemetry_hex="+bytes(telemetry_raw).hex().encode("ascii"),b"P27E001V4|attempt_start_ns="+str(attempt_start).encode("ascii"),b"P27E001V4|attempt_finish_ns="+str(attempt_finish).encode("ascii"),b"P27E001V4|attempt_elapsed_ns="+str(attempt_finish-attempt_start if attempt_finish>=attempt_start else -1).encode("ascii"),b"P27E001V4|attempt_bound_ns="+str(total_ns).encode("ascii"),b"P27E001V4|result="+result]
 report=b"\n".join(rows)+b"\n"
 try: write_exact(1,report,total_deadline)
 except BaseException: pass
OUTER CONTROLLER V4 SOURCE END
```

The outer source has no source-file, image-file, procfs, mountinfo, pathname,
inventory, or cleanup call. Its direct-child wait transition stores the raw
status and removes live ownership in one `physical_reap` assignment before
any deadline test, drain, parse, or other fallible work. Primary failure is
write-once; cleanup failures are separate and can only demote PASS.

## 5. Exact owned-launcher source

The launcher is the outer controller's one direct child, session leader, and
deadline-owned helper. It performs every potentially blocking identity,
procfs, source-file, mount, inventory, and cleanup operation. A synchronous
call is bracketed by internal checks, but that is not claimed to bound the
syscall. Containment comes from the still-live outer controller, which can
terminate the whole owned group if the launcher does not return by the total
deadline. The launcher accepts a successful call only after its post-call
deadline check.

```text
OWNED LAUNCHER V4 SOURCE BEGIN
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
LEDGER=b"/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md"
CONTROL=b"/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V4.md"
PY_BYTES=30626264
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
CAP=262144
TELE_CAP=262144
HARD_NOFILE=1048576
ABORT=0

class Fail(Exception): pass

def need(v,code):
 if not v: raise Fail(code)

def mono():
 v=time.monotonic_ns(); need(type(v) is int and v>=0,"clock-value"); return v

def before(deadline,code):
 n=mono(); need(n<=deadline,code+"-pre"); return n

def after(deadline,code):
 n=mono(); need(n<=deadline,code+"-post"); return n

def canonical_decimal(raw,minimum=0,maximum=(1<<63)-1):
 need(type(raw) is bytes and raw and all(48<=c<=57 for c in raw),"decimal-grammar")
 value=int(raw); need(str(value).encode("ascii")==raw and minimum<=value<=maximum,"decimal-canonical"); return value

def canonical_hex(raw,count=None):
 need(type(raw) is bytes and raw and (count is None or len(raw)==count) and all(c in b"0123456789abcdef" for c in raw),"hex-canonical")
 if count is None: need(len(raw)%2==0 and bytes.fromhex(raw.decode("ascii")).hex().encode("ascii")==raw,"hex-roundtrip")
 return raw

def call(deadline,label,fn,*args,**kwargs):
 before(deadline,label); value=fn(*args,**kwargs); after(deadline,label); return value

def close_capture(fd,deadline,failures,label):
 if fd<0: return
 try: call(deadline,label+"-close",os.close,fd)
 except BaseException as e: failures.append((label+":"+type(e).__name__).encode("ascii","strict").lower())

def set_nonblock(fd,deadline):
 flags=call(deadline,"fcntl-get",fcntl.fcntl,fd,fcntl.F_GETFL)
 call(deadline,"fcntl-set",fcntl.fcntl,fd,fcntl.F_SETFL,flags|os.O_NONBLOCK)

def write_exact(fd,data,deadline):
 set_nonblock(fd,deadline); poller=select.poll(); poller.register(fd,select.POLLOUT|select.POLLERR|select.POLLHUP); pos=0
 for unused in range(8192):
  if pos==len(data): after(deadline,"write-complete"); return
  before(deadline,"write")
  try: count=os.write(fd,data[pos:]); after(deadline,"write"); need(count>0,"write-zero"); pos+=count; continue
  except BlockingIOError: after(deadline,"write")
  except InterruptedError: after(deadline,"write"); continue
  before(deadline,"write-poll"); poller.poll(max(0,min(10,(deadline-mono()+999999)//1000000))); after(deadline,"write-poll")
 raise Fail("write-iterations")

def drain(fd,buf,cap,deadline,label,forward=-1):
 eof=False
 for unused in range(256):
  before(deadline,label+"-read")
  try: chunk=os.read(fd,4096)
  except BlockingIOError: after(deadline,label+"-read"); break
  except InterruptedError: after(deadline,label+"-read"); continue
  after(deadline,label+"-read")
  if not chunk: eof=True; break
  buf.extend(chunk); need(len(buf)<=cap,label+"-cap")
  if forward>=0: write_exact(forward,chunk,deadline)
 return eof

def physical_reap(slots,pid,status):
 slots[pid]=(0,status)

def wait_owned(slots,pid,deadline):
 need(pid in slots and slots[pid][0]==1,"wait-ownership")
 before(deadline,"waitpid")
 try: got,status=os.waitpid(pid,os.WNOHANG)
 except InterruptedError: after(deadline,"waitpid"); return 0
 except ChildProcessError as e: raise Fail("wait-echild") from e
 if got==pid: physical_reap(slots,pid,status)
 after(deadline,"waitpid"); need(got in (0,pid),"wait-return"); return got

def fd_census(limit,deadline):
 got=[]
 for fd in range(limit):
  before(deadline,"fd-census")
  try: fcntl.fcntl(fd,fcntl.F_GETFD); after(deadline,"fd-census")
  except OSError as e:
   after(deadline,"fd-census")
   if e.errno==errno.EBADF: continue
   raise
  got.append(fd)
 return tuple(got)

def hash_fd(fd,size,deadline,label):
 call(deadline,label+"-seek",os.lseek,fd,0,os.SEEK_SET); digest=hashlib.sha256(); total=0
 for unused in range((size+1048575)//1048576+1):
  before(deadline,label+"-read")
  try: chunk=os.read(fd,min(1048576,size-total+1))
  except InterruptedError: after(deadline,label+"-read"); continue
  after(deadline,label+"-read")
  if not chunk: break
  total+=len(chunk); need(total<=size,label+"-growth"); digest.update(chunk)
 need(total==size,label+"-short"); return digest.hexdigest().encode("ascii")

def stat_key(value):
 return (value.st_dev,value.st_ino,value.st_mode,value.st_nlink,value.st_uid,value.st_gid,value.st_size)

def exact_terminal(raw,lf,terminal):
 need(raw.count(b"\n")==lf and raw.endswith(b"\n") and b"\r" not in raw and b"\x00" not in raw,"control-frame")
 lines=raw.split(b"\n"); need(lines[-1]==b"" and len(lines)>=2 and lines[-2]==terminal,"control-final-line")
 need(sum(1 for line in lines[:-1] if line==terminal)==1,"control-terminal-standalone-count")

def open_regular(path,size,lf,digest,terminal,deadline,label):
 fd=call(deadline,label+"-open",os.open,path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 initial=call(deadline,label+"-fstat",os.fstat,fd)
 need(stat.S_ISREG(initial.st_mode) and stat.S_IMODE(initial.st_mode)==0o644 and initial.st_nlink==1 and initial.st_uid==0 and initial.st_gid==0 and initial.st_size==size,label+"-stat")
 call(deadline,label+"-seek",os.lseek,fd,0,os.SEEK_SET); parts=[]; total=0
 for unused in range((size+1048575)//1048576+1):
  before(deadline,label+"-read")
  try: chunk=os.read(fd,min(1048576,size-total+1))
  except InterruptedError: after(deadline,label+"-read"); continue
  after(deadline,label+"-read")
  if not chunk: break
  parts.append(chunk); total+=len(chunk); need(total<=size,label+"-growth")
 raw=b"".join(parts); need(len(raw)==size and hashlib.sha256(raw).hexdigest().encode("ascii")==digest,label+"-content")
 exact_terminal(raw,lf,terminal)
 final=call(deadline,label+"-fstat-final",os.fstat,fd); pathstat=call(deadline,label+"-pathstat",os.stat,path,follow_symlinks=False)
 need(stat_key(initial)==stat_key(final)==stat_key(pathstat),label+"-replacement")
 return fd,stat_key(initial)

def recheck_regular(fd,path,key,size,lf,digest,terminal,deadline,label):
 held=call(deadline,label+"-fstat",os.fstat,fd); pathstat=call(deadline,label+"-pathstat",os.stat,path,follow_symlinks=False)
 need(stat_key(held)==stat_key(pathstat)==key,label+"-identity")
 call(deadline,label+"-seek",os.lseek,fd,0,os.SEEK_SET); raw=bytearray()
 for unused in range((size+1048575)//1048576+1):
  before(deadline,label+"-read")
  try: chunk=os.read(fd,min(1048576,size-len(raw)+1))
  except InterruptedError: after(deadline,label+"-read"); continue
  after(deadline,label+"-read")
  if not chunk: break
  raw.extend(chunk); need(len(raw)<=size,label+"-growth")
 need(len(raw)==size and hashlib.sha256(raw).hexdigest().encode("ascii")==digest,label+"-hash")
 exact_terminal(bytes(raw),lf,terminal)

def bind_images(outer_pid,deadline):
 link=call(deadline,"python-link-lstat",os.lstat,PYTHON); need(stat.S_ISLNK(link.st_mode) and stat.S_IMODE(link.st_mode)==0o777 and link.st_nlink==1 and link.st_uid==0 and link.st_gid==0 and link.st_size==10,"python-link")
 need(call(deadline,"python-readlink",os.readlink,PYTHON)==b"python3.12","python-link-target")
 resolved=call(deadline,"python-open",os.open,PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 self_fd=call(deadline,"self-image-open",os.open,b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC)
 outer_path=("/proc/%d/exe"%outer_pid).encode("ascii"); outer_fd=call(deadline,"outer-image-open",os.open,outer_path,os.O_RDONLY|os.O_CLOEXEC)
 a=call(deadline,"python-fstat",os.fstat,resolved); b=call(deadline,"self-image-fstat",os.fstat,self_fd); c=call(deadline,"outer-image-fstat",os.fstat,outer_fd)
 need(stat_key(a)==stat_key(b)==stat_key(c) and stat.S_ISREG(a.st_mode) and stat.S_IMODE(a.st_mode)==0o755 and a.st_nlink==1 and a.st_uid==0 and a.st_gid==0 and a.st_size==PY_BYTES,"image-identity")
 need(hash_fd(resolved,PY_BYTES,deadline,"python-hash")==PY_SHA and hash_fd(self_fd,PY_BYTES,deadline,"self-hash")==PY_SHA and hash_fd(outer_fd,PY_BYTES,deadline,"outer-hash")==PY_SHA,"image-hash")
 return resolved,self_fd,outer_fd,stat_key(a),stat_key(link)

def recheck_images(resolved,self_fd,outer_fd,key,link_key,deadline):
 a=call(deadline,"terminal-python-fstat",os.fstat,resolved); b=call(deadline,"terminal-self-fstat",os.fstat,self_fd); c=call(deadline,"terminal-outer-fstat",os.fstat,outer_fd); p=call(deadline,"terminal-python-path",os.stat,PYRES,follow_symlinks=False); link=call(deadline,"terminal-link-lstat",os.lstat,PYTHON)
 need(stat_key(a)==stat_key(b)==stat_key(c)==stat_key(p)==key and stat_key(link)==link_key,"terminal-image-identity")
 need(call(deadline,"terminal-link-read",os.readlink,PYTHON)==b"python3.12","terminal-link-target")
 need(hash_fd(resolved,PY_BYTES,deadline,"terminal-python-hash")==PY_SHA and hash_fd(self_fd,PY_BYTES,deadline,"terminal-self-hash")==PY_SHA and hash_fd(outer_fd,PY_BYTES,deadline,"terminal-outer-hash")==PY_SHA,"terminal-image-hash")

def component_open(deadline):
 rootfd=call(deadline,"root-open",os.open,b"/",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW)
 tmpfd=call(deadline,"tmp-open",os.open,b"/tmp",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW)
 root=call(deadline,"root-fstat",os.fstat,rootfd); rootpath=call(deadline,"root-stat",os.stat,b"/",follow_symlinks=False)
 tmp=call(deadline,"tmp-fstat",os.fstat,tmpfd); tmppath=call(deadline,"tmp-stat",os.stat,b"tmp",dir_fd=rootfd,follow_symlinks=False)
 need(stat_key(root)==stat_key(rootpath) and stat.S_ISDIR(root.st_mode) and root.st_uid==0 and root.st_gid==0,"root-component")
 need(stat_key(tmp)==stat_key(tmppath) and stat.S_ISDIR(tmp.st_mode) and tmp.st_uid==0 and tmp.st_gid==0 and stat.S_IMODE(tmp.st_mode)&0o1000,"tmp-component")
 return rootfd,tmpfd,stat_key(root),stat_key(tmp)

def mount_clear(safe,deadline):
 fd=call(deadline,"mountinfo-open",os.open,b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:
  raw=bytearray()
  for unused in range(257):
   before(deadline,"mountinfo-read")
   try: chunk=os.read(fd,4096)
   except InterruptedError: after(deadline,"mountinfo-read"); continue
   after(deadline,"mountinfo-read")
   if not chunk: break
   raw.extend(chunk); need(len(raw)<=1048576,"mountinfo-cap")
  else: raise Fail("mountinfo-iterations")
 finally: call(deadline,"mountinfo-close",os.close,fd)
 need(raw.endswith(b"\n") and b"\x00" not in raw,"mountinfo-frame")
 for line in bytes(raw).split(b"\n")[:-1]:
  parts=line.split(b" "); need(len(parts)>=10 and b" - " in line,"mountinfo-line"); need(parts[4]!=safe,"safe-mountpoint")

def safe_recheck(tmpfd,name,dirfd,key,safe,empty,deadline):
 held=call(deadline,"safe-fstat",os.fstat,dirfd); path=call(deadline,"safe-stat",os.stat,name,dir_fd=tmpfd,follow_symlinks=False)
 need(stat_key(held)==stat_key(path)==key and stat.S_ISDIR(held.st_mode) and stat.S_IMODE(held.st_mode)==0o700 and held.st_uid==0 and held.st_gid==0,"safe-identity")
 names=call(deadline,"safe-listdir",os.listdir,dirfd); need(type(names) is list,"safe-list-type")
 if empty: need(names==[],"safe-not-empty")
 mount_clear(safe,deadline); return tuple(sorted(os.fsencode(item) for item in names))

def rmdir_proof(tmpfd,tmpkey,name,dirfd,dirkey,deadline):
 held=call(deadline,"rmdir-pre-fstat",os.fstat,dirfd); path=call(deadline,"rmdir-pre-stat",os.stat,name,dir_fd=tmpfd,follow_symlinks=False); parent=call(deadline,"rmdir-parent-pre",os.fstat,tmpfd)
 need(stat_key(held)==stat_key(path)==dirkey and stat_key(parent)==tmpkey,"rmdir-pre-identity")
 need(stat.S_ISDIR(held.st_mode) and stat.S_IMODE(held.st_mode)==0o700 and held.st_uid==0 and held.st_gid==0 and held.st_nlink==2,"rmdir-pre-link")
 need(call(deadline,"rmdir-list",os.listdir,dirfd)==[],"rmdir-pre-empty")
 call(deadline,"rmdir",os.rmdir,name,dir_fd=tmpfd)
 post=call(deadline,"rmdir-post-fstat",os.fstat,dirfd); parent2=call(deadline,"rmdir-parent-post",os.fstat,tmpfd)
 need(post.st_dev==held.st_dev and post.st_ino==held.st_ino and stat.S_ISDIR(post.st_mode) and stat.S_IMODE(post.st_mode)==stat.S_IMODE(held.st_mode) and post.st_uid==held.st_uid and post.st_gid==held.st_gid and post.st_nlink==0,"rmdir-held-link-zero")
 need(stat_key(parent2)==tmpkey,"rmdir-parent-stable")
 absent=0
 try: call(deadline,"rmdir-path-after",os.stat,name,dir_fd=tmpfd,follow_symlinks=False)
 except FileNotFoundError: after(deadline,"rmdir-path-enoent"); absent=1
 need(absent==1,"rmdir-path-present"); return 1

def proc_identity(pid,deadline,label):
 path=("/proc/%d/stat"%pid).encode("ascii"); fd=call(deadline,label+"-open",os.open,path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:
  raw=bytearray()
  for unused in range(8):
   before(deadline,label+"-read")
   try: chunk=os.read(fd,512)
   except InterruptedError: after(deadline,label+"-read"); continue
   after(deadline,label+"-read")
   if not chunk: break
   raw.extend(chunk); need(len(raw)<=4096,label+"-cap")
 finally: call(deadline,label+"-close",os.close,fd)
 need(raw.endswith(b"\n") and raw.count(b"\n")==1,"proc-frame"); raw=bytes(raw); right=raw.rfind(b") "); left=raw[:right+1].find(b"("); need(right>1 and left>0,"proc-comm")
 fields=raw[right+2:-1].split(b" "); need(len(fields)>=20,"proc-fields")
 values=(raw[:left-1],fields[1],fields[2],fields[3],fields[19]); parsed=tuple(canonical_decimal(x) for x in values); return parsed

FIELDS={
 b"P00":(b"source_item_bytes",b"source_item_accounted_bytes",b"source_item_sha256",b"arg_max",b"spawn_returned",b"e2big",b"transport_feasible"),
 b"P01D":(b"python_image_dev",b"python_image_ino",b"python_image_mode",b"python_image_nlink",b"python_image_uid",b"python_image_gid",b"python_image_bytes",b"python_image_sha256",b"libc_confstr_hex",b"libc_path_hex",b"libc_map_dev",b"libc_map_ino",b"libc_open_dev",b"libc_open_ino",b"libc_mode",b"libc_nlink",b"libc_uid",b"libc_gid",b"libc_bytes",b"libc_sha256",b"posix_spawn_module",b"posix_spawn_name",b"posix_spawn_type",b"backend_surface",b"spawn_premise_satisfied"),
 b"P01C":(b"python_image_dev",b"python_image_ino",b"python_image_sha256",b"libc_path_hex",b"libc_map_dev",b"libc_map_ino",b"libc_sha256",b"libc_confstr_hex",b"posix_spawn_module",b"posix_spawn_name",b"child_raw_bytes",b"child_raw_sha256",b"child_pid",b"child_sid",b"child_pgid",b"spawn_premise_satisfied"),
 b"P02":(b"environment",b"environment_count",b"cwd_hex",b"flags",b"fds",b"fd_nodes",b"rlimit_cpu",b"rlimit_as",b"rlimit_fsize",b"rlimit_core",b"rlimit_nofile",b"rlimit_nproc"),
 b"P03":(b"soft_before",b"hard_before",b"soft_test",b"opened_fds",b"emfile",b"fds_after"),
 b"P04":(b"valid_signal_count",b"default_signal_count",b"defaults_csv",b"defaults_sha256",b"mask_empty",b"normalization_complete"),
 b"P05":(b"wnohang_zero",b"eintr",b"exit_pid",b"exit_raw",b"exit_code",b"echild",b"signal_pid",b"signal_raw",b"term_signal"),
 b"P06":(b"implementation_hex",b"adjustable",b"monotonic",b"declared_resolution_ns",b"observed_min_delta_ns",b"start_ns",b"end_ns",b"elapsed_ns",b"headroom_ns",b"deadline_ns",b"deadline_checked"),
 b"P07":(b"read_cloexec",b"write_cloexec",b"read_nonblock",b"write_nonblock",b"empty_eagain",b"initial_readable",b"byte_hex",b"eof_before_last_writer",b"hup_after_last_writer",b"eof_after_last_writer",b"terminal_elapsed_ns"),
 b"P08":(b"child_pid",b"child_sid",b"child_pgid",b"marker_sid",b"marker_pgid",b"live_pid_zero",b"raw_status",b"post_pid_esrch",b"reuse_proof"),
 b"P09":(b"child_pid",b"child_pgid",b"signal",b"raw_status",b"reap_start_ns",b"reap_end_ns",b"reap_elapsed_ns",b"reaped"),
 b"P10":(b"sample_count",b"pids",b"pgids",b"statuses",b"pid_duplicates",b"group_is_single_owned_launcher_group",b"reuse_proof"),
 b"P11":(b"capeff_hex",b"cap_fowner",b"open_result",b"atime_unchanged",b"created_dev",b"created_ino",b"cleanup_unlinked",b"cleanup_identity_observed",b"atomic_unlink_proof",b"scope_single_inode"),
 b"P12":(b"env_dev",b"env_ino",b"env_sha256",b"bash_dev",b"bash_ino",b"bash_sha256",b"child_raw_bytes",b"child_raw_sha256",b"child_pid",b"child_sid",b"child_pgid",b"executable_hex",b"environment",b"environment_count",b"underscore_absent",b"cwd_hex",b"real_payload_invoked",b"raw_status"),
 b"P13":(b"file_fsync_returned",b"hardlink_noreplace_returned",b"old_absent",b"inode_preserved",b"dir_fsync_returned",b"post_unlink_absent",b"created_dev",b"created_ino",b"cleanup_unlinked",b"cleanup_identity_observed",b"atomic_unlink_proof",b"durability_proof",b"rename_atomicity_proof",b"immutability_proof")}
COMMON=(b"marker_image_dev",b"marker_image_ino",b"marker_image_sha256",b"children_spawned",b"children_reaped",b"child_pids",b"raw_statuses",b"probe_start_ns",b"probe_finish_ns",b"probe_elapsed_ns",b"probe_bound_ns",b"primary_failure",b"cleanup_failure",b"result")

def parse_row(line,probe,key):
 prefix=b"P27E001V4|probe="+probe+b"|"+key+b"="
 need(line.startswith(prefix) and line.count(b"=")==2,"marker-row-order"); value=line[len(prefix):]
 need(value and value.isascii() and b"|" not in value and b"\r" not in value and b"\x00" not in value,"marker-row-value"); return value

def csv_decimal(raw):
 if raw==b"-": return ()
 parts=raw.split(b","); need(parts and all(parts),"csv-frame"); return tuple(canonical_decimal(item) for item in parts)

DECIMAL_KEYS=set((b"source_item_bytes",b"source_item_accounted_bytes",b"arg_max",b"spawn_returned",b"e2big",b"transport_feasible",b"python_image_dev",b"python_image_ino",b"python_image_nlink",b"python_image_uid",b"python_image_gid",b"python_image_bytes",b"libc_map_dev",b"libc_map_ino",b"libc_open_dev",b"libc_open_ino",b"libc_nlink",b"libc_uid",b"libc_gid",b"libc_bytes",b"spawn_premise_satisfied",b"child_raw_bytes",b"child_pid",b"child_sid",b"child_pgid",b"environment_count",b"soft_before",b"hard_before",b"soft_test",b"opened_fds",b"emfile",b"valid_signal_count",b"default_signal_count",b"mask_empty",b"normalization_complete",b"wnohang_zero",b"eintr",b"exit_pid",b"exit_raw",b"exit_code",b"echild",b"signal_pid",b"signal_raw",b"term_signal",b"adjustable",b"monotonic",b"declared_resolution_ns",b"observed_min_delta_ns",b"start_ns",b"end_ns",b"elapsed_ns",b"headroom_ns",b"deadline_ns",b"deadline_checked",b"read_cloexec",b"write_cloexec",b"read_nonblock",b"write_nonblock",b"empty_eagain",b"initial_readable",b"eof_before_last_writer",b"hup_after_last_writer",b"eof_after_last_writer",b"terminal_elapsed_ns",b"marker_sid",b"marker_pgid",b"live_pid_zero",b"raw_status",b"post_pid_esrch",b"reuse_proof",b"signal",b"reap_start_ns",b"reap_end_ns",b"reap_elapsed_ns",b"reaped",b"sample_count",b"pid_duplicates",b"group_is_single_owned_launcher_group",b"cap_fowner",b"atime_unchanged",b"created_dev",b"created_ino",b"cleanup_unlinked",b"cleanup_identity_observed",b"atomic_unlink_proof",b"scope_single_inode",b"env_dev",b"env_ino",b"bash_dev",b"bash_ino",b"underscore_absent",b"real_payload_invoked",b"file_fsync_returned",b"hardlink_noreplace_returned",b"old_absent",b"inode_preserved",b"dir_fsync_returned",b"post_unlink_absent",b"durability_proof",b"rename_atomicity_proof",b"immutability_proof",b"marker_image_dev",b"marker_image_ino",b"children_spawned",b"children_reaped",b"probe_start_ns",b"probe_finish_ns",b"probe_elapsed_ns",b"probe_bound_ns"))
CSV_KEYS=set((b"defaults_csv",b"pids",b"pgids",b"statuses",b"child_pids",b"raw_statuses"))
OCTAL_KEYS=set((b"python_image_mode",b"libc_mode"))
RLIMIT_KEYS=set((b"rlimit_cpu",b"rlimit_as",b"rlimit_fsize",b"rlimit_core",b"rlimit_nofile",b"rlimit_nproc"))

def grammar_value(key,value):
 if key.endswith(b"_sha256"): canonical_hex(value,64)
 elif key in DECIMAL_KEYS: canonical_decimal(value)
 elif key in CSV_KEYS: csv_decimal(value)
 elif key in OCTAL_KEYS: need(value and all(c in b"01234567" for c in value) and format(int(value,8),"o").encode("ascii")==value,"octal-canonical")
 elif key.endswith(b"_hex"):
  if key==b"capeff_hex": canonical_hex(value,16)
  elif key==b"byte_hex": canonical_hex(value,2)
  else: canonical_hex(value)
 elif key in RLIMIT_KEYS:
  parts=value.split(b","); need(len(parts)==2,"rlimit-pair"); canonical_decimal(parts[0]); need(parts[1]==b"-1" or (parts[1] and all(48<=c<=57 for c in parts[1]) and str(int(parts[1])).encode("ascii")==parts[1]),"rlimit-canonical")
 elif key==b"fd_nodes":
  entries=value.split(b","); need(entries and all(entry for entry in entries),"fd-nodes-frame")
  for entry in entries:
   parts=entry.split(b":"); need(len(parts)==3,"fd-node-fields"); tuple(canonical_decimal(part) for part in parts)
 else: need(all(32<=c<=126 for c in value),"text-canonical")

def validate_probe(values,probe,safe,total_ns):
 spawned=canonical_decimal(values[b"children_spawned"]); reaped=canonical_decimal(values[b"children_reaped"]); pids=csv_decimal(values[b"child_pids"]); statuses=csv_decimal(values[b"raw_statuses"])
 need(spawned==reaped==len(pids)==len(statuses) and all(pid>1 for pid in pids),"child-ledger")
 canonical_hex(values[b"marker_image_sha256"],64); need(values[b"marker_image_sha256"]==PY_SHA,"marker-image-sha")
 start=canonical_decimal(values[b"probe_start_ns"]); finish=canonical_decimal(values[b"probe_finish_ns"]); elapsed=canonical_decimal(values[b"probe_elapsed_ns"]); bound=canonical_decimal(values[b"probe_bound_ns"])
 need(start<=finish and elapsed==finish-start and elapsed<=bound<=total_ns,"probe-elapsed")
 need(values[b"primary_failure"]==b"none" and values[b"cleanup_failure"]==b"none" and values[b"result"]==b"PASS","probe-result")
 if probe==b"P00":
  returned=canonical_decimal(values[b"spawn_returned"]); e2big=canonical_decimal(values[b"e2big"]); need(values[b"source_item_bytes"]==b"251414" and values[b"source_item_accounted_bytes"]==b"251415" and returned in (0,1) and e2big in (0,1) and returned+e2big==1 and canonical_decimal(values[b"transport_feasible"])==returned and spawned==returned,"p00-fields"); canonical_hex(values[b"source_item_sha256"],64)
 elif probe==b"P01D":
  need(spawned==0 and values[b"python_image_bytes"]==b"30626264" and values[b"python_image_sha256"]==PY_SHA and values[b"libc_map_dev"]==values[b"libc_open_dev"] and values[b"libc_map_ino"]==values[b"libc_open_ino"] and values[b"spawn_premise_satisfied"]==b"0","p01d-fields"); canonical_hex(values[b"libc_sha256"],64)
 elif probe==b"P01C":
  need(spawned==1 and values[b"python_image_sha256"]==PY_SHA and values[b"spawn_premise_satisfied"]==b"1" and canonical_decimal(values[b"child_pid"])==pids[0] and canonical_decimal(values[b"child_sid"],2)==canonical_decimal(values[b"child_pgid"],2),"p01c-fields"); canonical_hex(values[b"libc_sha256"],64); canonical_hex(values[b"child_raw_sha256"],64)
 elif probe==b"P02":
  expected=b",".join((key+b"="+ENV[key]).hex().encode("ascii") for key in sorted(ENV)); need(spawned==0 and values[b"environment"]==expected and values[b"environment_count"]==b"10" and bytes.fromhex(canonical_hex(values[b"cwd_hex"]).decode("ascii"))==safe and values[b"fds"]==b"0,1,2" and values[b"flags"]==b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1","p02-fields")
 elif probe==b"P03": need(spawned==0 and values[b"soft_before"]==b"4096" and values[b"hard_before"]==b"1048576" and values[b"soft_test"]==b"64" and values[b"emfile"]==b"1" and values[b"fds_after"]==b"0,1,2","p03-fields")
 elif probe==b"P04": canonical_hex(values[b"defaults_sha256"],64); need(spawned==0 and values[b"mask_empty"]==values[b"normalization_complete"]==b"1" and canonical_decimal(values[b"default_signal_count"])==len(csv_decimal(values[b"defaults_csv"])),"p04-fields")
 elif probe==b"P05": need(spawned==2 and values[b"wnohang_zero"]==values[b"eintr"]==values[b"echild"]==b"1" and values[b"exit_code"]==b"23" and canonical_decimal(values[b"exit_pid"])==pids[0] and canonical_decimal(values[b"signal_pid"])==pids[1] and canonical_decimal(values[b"exit_raw"])==statuses[0] and canonical_decimal(values[b"signal_raw"])==statuses[1] and canonical_decimal(values[b"term_signal"])==int(signal.SIGTERM),"p05-fields")
 elif probe==b"P06":
  a=canonical_decimal(values[b"start_ns"]); b=canonical_decimal(values[b"end_ns"]); need(spawned==0 and a<=b and canonical_decimal(values[b"elapsed_ns"])==b-a and values[b"deadline_checked"]==b"1","p06-fields")
 elif probe==b"P07": need(spawned==0 and values[b"read_cloexec"]==values[b"write_cloexec"]==values[b"read_nonblock"]==values[b"write_nonblock"]==values[b"empty_eagain"]==values[b"hup_after_last_writer"]==values[b"eof_after_last_writer"]==b"1" and values[b"initial_readable"]==values[b"eof_before_last_writer"]==b"0" and values[b"byte_hex"]==b"78" and canonical_decimal(values[b"terminal_elapsed_ns"])==elapsed,"p07-fields")
 elif probe==b"P08": need(spawned==1 and canonical_decimal(values[b"child_pid"])==pids[0] and canonical_decimal(values[b"raw_status"])==statuses[0] and values[b"live_pid_zero"]==values[b"post_pid_esrch"]==b"1" and values[b"reuse_proof"]==b"0","p08-fields")
 elif probe==b"P09":
  a=canonical_decimal(values[b"reap_start_ns"]); b=canonical_decimal(values[b"reap_end_ns"]); need(spawned==1 and canonical_decimal(values[b"child_pid"])==pids[0] and canonical_decimal(values[b"raw_status"])==statuses[0] and a<=b and canonical_decimal(values[b"reap_elapsed_ns"])==b-a and b-a<=1000000000 and values[b"reaped"]==b"1","p09-fields")
 elif probe==b"P10":
  groups=csv_decimal(values[b"pgids"]); need(spawned==16 and values[b"sample_count"]==b"16" and csv_decimal(values[b"pids"])==pids and csv_decimal(values[b"statuses"])==statuses and len(groups)==16 and len(set(groups))==1 and values[b"group_is_single_owned_launcher_group"]==b"1" and values[b"reuse_proof"]==b"0","p10-fields")
 elif probe==b"P11": need(spawned==0 and len(values[b"capeff_hex"])==16 and canonical_hex(values[b"capeff_hex"],16) and values[b"open_result"] in (b"OK",b"EPERM") and values[b"cleanup_unlinked"]==values[b"cleanup_identity_observed"]==values[b"scope_single_inode"]==b"1" and values[b"atomic_unlink_proof"]==b"0","p11-fields")
 elif probe==b"P12":
  expected=b",".join((key+b"="+ENV[key]).hex().encode("ascii") for key in sorted(ENV)); need(spawned==1 and values[b"env_sha256"]==b"85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0" and values[b"bash_sha256"]==b"59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4" and canonical_decimal(values[b"child_pid"])==pids[0] and canonical_decimal(values[b"raw_status"])==statuses[0] and bytes.fromhex(canonical_hex(values[b"executable_hex"]).decode("ascii"))==PYTHON and values[b"environment"]==expected and values[b"environment_count"]==b"10" and values[b"underscore_absent"]==b"1" and values[b"real_payload_invoked"]==b"0" and bytes.fromhex(canonical_hex(values[b"cwd_hex"]).decode("ascii"))==safe,"p12-fields")
 elif probe==b"P13": need(spawned==0 and values[b"file_fsync_returned"]==values[b"hardlink_noreplace_returned"]==values[b"old_absent"]==values[b"inode_preserved"]==values[b"dir_fsync_returned"]==values[b"post_unlink_absent"]==values[b"cleanup_unlinked"]==values[b"cleanup_identity_observed"]==b"1" and values[b"atomic_unlink_proof"]==values[b"durability_proof"]==values[b"rename_atomicity_proof"]==values[b"immutability_proof"]==b"0","p13-fields")
 else: raise Fail("probe-unreachable")
 return spawned,reaped,start,finish,elapsed,bound

def parse_marker(raw,probe,safe,total_ns):
 need(raw.endswith(b"\n") and b"\r" not in raw and b"\x00" not in raw,"marker-frame")
 lines=raw.split(b"\n"); need(lines[-1]==b"" and all(lines[:-1]),"marker-lines")
 header=b"P27E001V4|marker=report|schema=4|probe="+probe; need(lines[0]==header,"marker-header")
 order=FIELDS[probe]+COMMON; need(len(lines)==len(order)+2,"marker-line-count")
 values={}
 for line,key in zip(lines[1:-1],order):
  values[key]=parse_row(line,probe,key); grammar_value(key,values[key])
 terminal=b"P27E001V4|probe="+probe+b"|result=PASS"
 need(lines[-2]==terminal and sum(1 for line in lines[:-1] if line==terminal)==1,"marker-terminal")
 return values,validate_probe(values,probe,safe,total_ns)

def abort_handler(signum,frame):
 global ABORT
 ABORT=1

def quarantine_failure(marker_pid,marker_slots,out_r,err_r,tele_r,marker_out,marker_err,nested_tele,deadline,probe,primary,failures):
 request=b"P27E001V4|launcher=cleanup-request|probe="+probe+b"|primary_failure="+primary+b"|marker_pid="+str(marker_pid).encode("ascii")+b"|marker_reaped="+str(int(marker_pid in marker_slots and marker_slots[marker_pid][0]==0)).encode("ascii")+b"|marker_raw_status="+str(marker_slots.get(marker_pid,(0,-1))[1] if marker_pid in marker_slots and marker_slots[marker_pid][1] is not None else -1).encode("ascii")+b"|marker_stdout_bytes="+str(len(marker_out)).encode("ascii")+b"|marker_stderr_bytes="+str(len(marker_err)).encode("ascii")+b"|nested_telemetry_bytes="+str(len(nested_tele)).encode("ascii")+b"\n"
 try: write_exact(3,request,deadline)
 except BaseException as e: failures.append(("request:"+type(e).__name__).encode("ascii","strict").lower())
 poller=select.poll()
 for fd in (out_r,err_r,tele_r):
  if fd>=0: poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 while True:
  try:
   if marker_pid in marker_slots and marker_slots[marker_pid][0]: wait_owned(marker_slots,marker_pid,deadline)
   if out_r>=0: drain(out_r,marker_out,CAP,deadline,"quarantine-out")
   if err_r>=0: drain(err_r,marker_err,CAP,deadline,"quarantine-err")
   if tele_r>=0: drain(tele_r,nested_tele,TELE_CAP,deadline,"quarantine-tele",3)
  except BaseException as e: failures.append(("quarantine:"+type(e).__name__).encode("ascii","strict").lower())
  if ABORT or mono()>=deadline:
   while True: signal.pause()
  before(deadline,"quarantine-poll"); poller.poll(max(0,min(10,(deadline-mono()+999999)//1000000))); after(deadline,"quarantine-poll")

primary=b"none"; cleanup_failures=[]; result=b"FAIL"; total_cleanup_pass=0
probe=b"invalid"; auth=b"0"*64; outer_pid=-1; marker_pid=-1; marker_slots={}; marker_status=-1
marker_out=bytearray(); marker_err=bytearray(); nested_tele=bytearray(); out_eof=err_eof=tele_eof=False
out_r=out_w=err_r=err_w=tele_r=tele_w=gate_r=gate_w=-1
ledger_fd=control_fd=resolved_fd=self_fd=outer_fd=rootfd=tmpfd=dirfd=-1
ledger_key=control_key=image_key=link_key=root_key=tmp_key=dir_key=None
safe=b""; name=b""; marker_source=b""; marker_sha=b""; launcher_sha=b""; total_deadline=mono(); total_ns=0
probe_start=mono(); probe_finish=probe_start; nested_spawned=nested_reaped=0

try:
 need(len(sys.argv)>=18 and sys.argv[0]=="-c","argv-count")
 probe=os.fsencode(sys.argv[1]); auth=os.fsencode(sys.argv[2]); outer_pid=canonical_decimal(os.fsencode(sys.argv[3]),2); outer_sha=os.fsencode(sys.argv[4]); marker_source=os.fsencode(sys.argv[5]); marker_sha=os.fsencode(sys.argv[6]); launcher_sha=os.fsencode(sys.argv[7]); total_deadline=canonical_decimal(os.fsencode(sys.argv[8]),1); total_ns=canonical_decimal(os.fsencode(sys.argv[9]),2000000000,10000000000)
 ledger_bytes=canonical_decimal(os.fsencode(sys.argv[10]),1,400000000); ledger_lf=canonical_decimal(os.fsencode(sys.argv[11]),1,1000000); ledger_sha=os.fsencode(sys.argv[12]); ledger_terminal=os.fsencode(sys.argv[13]); control_bytes=canonical_decimal(os.fsencode(sys.argv[14]),1,400000000); control_lf=canonical_decimal(os.fsencode(sys.argv[15]),1,1000000); control_sha=os.fsencode(sys.argv[16]); control_terminal=os.fsencode(sys.argv[17]); extra=tuple(os.fsencode(x) for x in sys.argv[18:])
 need(probe in FIELDS,"probe-id"); canonical_hex(auth,64); canonical_hex(outer_sha,64); canonical_hex(marker_sha,64); canonical_hex(launcher_sha,64); canonical_hex(ledger_sha,64); canonical_hex(control_sha,64)
 need(hashlib.sha256(os.fsencode(sys.orig_argv[8])).hexdigest().encode("ascii")==launcher_sha and hashlib.sha256(marker_source).hexdigest().encode("ascii")==marker_sha,"source-hash")
 need(sys.orig_argv[:8]==[PYTHON.decode("ascii"),"-I","-S","-B","-P","-X","utf8","-c"] and sys.executable==PYTHON.decode("ascii") and dict(os.environb)==ENV,"launcher-runtime")
 need(sys.flags.isolated==1 and sys.flags.ignore_environment==1 and sys.flags.no_site==1 and sys.flags.no_user_site==1 and sys.flags.dont_write_bytecode==1 and sys.flags.safe_path==1 and sys.flags.utf8_mode==1 and sys.flags.hash_randomization==1,"launcher-flags")
 need(os.getpid()==os.getsid(0)==os.getpgrp() and os.getppid()==outer_pid,"launcher-topology")
 need(mono()<=total_deadline and total_deadline-mono()<=total_ns,"launcher-deadline")
 need(resource.getrlimit(resource.RLIMIT_NOFILE)[1]==HARD_NOFILE,"launcher-hard-nofile")
 signal_defs=tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP)))); signal.pthread_sigmask(signal.SIG_SETMASK,set())
 for number in signal_defs: signal.signal(number,signal.SIG_DFL)
 need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==set() and all(signal.getsignal(number)==signal.SIG_DFL for number in signal_defs),"launcher-signals")
 signal.signal(signal.SIGTERM,abort_handler); signal.signal(signal.SIGINT,abort_handler)
 resolved_fd,self_fd,outer_fd,image_key,link_key=bind_images(outer_pid,total_deadline)
 ledger_fd,ledger_key=open_regular(LEDGER,ledger_bytes,ledger_lf,ledger_sha,ledger_terminal,total_deadline,"ledger")
 control_fd,control_key=open_regular(CONTROL,control_bytes,control_lf,control_sha,control_terminal,total_deadline,"control")
 rootfd,tmpfd,root_key,tmp_key=component_open(total_deadline)
 old_umask=os.umask(0o077); os.umask(0o077)
 name=b"p27-e001-host-v4-"+auth; safe=b"/tmp/"+name
 need(len(name)==len(b"p27-e001-host-v4-")+64 and b"/" not in name and b".." not in name and b"build" not in name and b"evidence" not in name and b"recovery-root" not in name,"safe-name")
 call(total_deadline,"safe-mkdir",os.mkdir,name,0o700,dir_fd=tmpfd)
 dirfd=call(total_deadline,"safe-open",os.open,name,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=tmpfd); call(total_deadline,"safe-fchmod",os.fchmod,dirfd,0o700)
 ds=call(total_deadline,"safe-opening-fstat",os.fstat,dirfd); dir_key=stat_key(ds); need(ds.st_dev==tmp_key[0] and ds.st_ino!=tmp_key[1],"safe-filesystem"); safe_recheck(tmpfd,name,dirfd,dir_key,safe,True,total_deadline)
 call(total_deadline,"launcher-chdir",os.chdir,safe); need(call(total_deadline,"launcher-getcwd",os.getcwdb)==safe,"launcher-cwd")
 resource.setrlimit(resource.RLIMIT_NOFILE,(4096,HARD_NOFILE)); resource.setrlimit(resource.RLIMIT_CPU,(3,3)); resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456)); resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576)); resource.setrlimit(resource.RLIMIT_CORE,(0,0)); nproc=resource.getrlimit(resource.RLIMIT_NPROC); nproc_hard=nproc[1]; nproc_soft=32 if nproc_hard==resource.RLIM_INFINITY else min(32,nproc_hard); need(nproc_soft>=4,"launcher-nproc"); resource.setrlimit(resource.RLIMIT_NPROC,(nproc_soft,nproc_hard))
 before(total_deadline,"marker-out-pipe"); out_r,out_w=os.pipe2(os.O_CLOEXEC); after(total_deadline,"marker-out-pipe")
 before(total_deadline,"marker-err-pipe"); err_r,err_w=os.pipe2(os.O_CLOEXEC); after(total_deadline,"marker-err-pipe")
 before(total_deadline,"marker-tele-pipe"); tele_r,tele_w=os.pipe2(os.O_CLOEXEC); after(total_deadline,"marker-tele-pipe")
 before(total_deadline,"marker-gate-pipe"); gate_r,gate_w=os.pipe2(os.O_CLOEXEC); after(total_deadline,"marker-gate-pipe")
 for fd in (out_r,err_r,tele_r): set_nonblock(fd,total_deadline)
 openfds=tuple(fd for fd in fd_census(HARD_NOFILE,total_deadline) if fd>=5)
 actions=[(os.POSIX_SPAWN_DUP2,out_w,1),(os.POSIX_SPAWN_DUP2,err_w,2),(os.POSIX_SPAWN_DUP2,tele_w,3),(os.POSIX_SPAWN_DUP2,gate_r,4)]
 actions.extend((os.POSIX_SPAWN_CLOSE,fd) for fd in openfds)
 argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",marker_source,probe,safe,marker_sha,str(total_deadline).encode("ascii"),str(total_ns).encode("ascii"))+extra
 before(total_deadline,"marker-spawn"); marker_pid=os.posix_spawn(PYTHON,argv,ENV,file_actions=tuple(actions),setsigmask=(),setsigdef=tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))); after(total_deadline,"marker-spawn")
 need(marker_pid>1,"marker-pid"); marker_slots[marker_pid]=(1,None)
 for fd,label in ((out_w,"out-w"),(err_w,"err-w"),(tele_w,"tele-w"),(gate_r,"gate-r")): close_capture(fd,total_deadline,cleanup_failures,label)
 out_w=err_w=tele_w=gate_r=-1
 ident=proc_identity(marker_pid,total_deadline,"marker-proc"); need(ident[0]==marker_pid and ident[1]==os.getpid() and ident[2]==os.getpgrp() and ident[3]==os.getsid(0),"marker-topology")
 ownership=b"P27E001V4|launcher=ownership|probe="+probe+b"|launcher_pid="+str(os.getpid()).encode("ascii")+b"|launcher_sid="+str(os.getsid(0)).encode("ascii")+b"|launcher_pgid="+str(os.getpgrp()).encode("ascii")+b"|marker_pid="+str(marker_pid).encode("ascii")+b"\n"
 write_exact(3,ownership,total_deadline); write_exact(gate_w,b"L",total_deadline); close_capture(gate_w,total_deadline,cleanup_failures,"gate-w"); gate_w=-1
 probe_start=mono(); poller=select.poll(); poller.register(out_r,select.POLLIN|select.POLLHUP|select.POLLERR); poller.register(err_r,select.POLLIN|select.POLLHUP|select.POLLERR); poller.register(tele_r,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(40000):
  if marker_slots[marker_pid][0]: wait_owned(marker_slots,marker_pid,total_deadline)
  out_eof=drain(out_r,marker_out,CAP,total_deadline,"marker-stdout") or out_eof
  err_eof=drain(err_r,marker_err,CAP,total_deadline,"marker-stderr") or err_eof
  tele_eof=drain(tele_r,nested_tele,TELE_CAP,total_deadline,"nested-telemetry",3) or tele_eof
  if marker_slots[marker_pid][0]==0 and out_eof and err_eof and tele_eof: break
  need(ABORT==0,"outer-abort"); before(total_deadline,"launcher-poll"); poller.poll(max(0,min(10,(total_deadline-mono()+999999)//1000000))); after(total_deadline,"launcher-poll")
 else: raise Fail("launcher-iterations")
 after(total_deadline,"marker-complete"); marker_status=marker_slots[marker_pid][1]
 need(marker_status==0 and out_eof and err_eof and tele_eof and len(marker_err)==0,"marker-completion")
 values,summary=parse_marker(bytes(marker_out),probe,safe,total_ns); nested_spawned,nested_reaped,probe_start,probe_finish,probe_elapsed,probe_bound=summary
 need(probe_finish<=total_deadline,"marker-finish-deadline")
 recheck_regular(ledger_fd,LEDGER,ledger_key,ledger_bytes,ledger_lf,ledger_sha,ledger_terminal,total_deadline,"terminal-ledger")
 recheck_regular(control_fd,CONTROL,control_key,control_bytes,control_lf,control_sha,control_terminal,total_deadline,"terminal-control")
 recheck_images(resolved_fd,self_fd,outer_fd,image_key,link_key,total_deadline)
 safe_recheck(tmpfd,name,dirfd,dir_key,safe,True,total_deadline)
 result=b"READY"
except BaseException as e:
 if primary==b"none":
  if isinstance(e,Fail): primary=os.fsencode(str(e)).replace(b"_",b"-")
  elif isinstance(e,OSError): primary=("oserror-%d"%(e.errno if e.errno is not None else -1)).encode("ascii")
  else: primary=("exception-"+type(e).__name__).encode("ascii","strict").lower()
finally:
 if result!=b"READY" and marker_pid>1: quarantine_failure(marker_pid,marker_slots,out_r,err_r,tele_r,marker_out,marker_err,nested_tele,total_deadline,probe,primary,cleanup_failures)
 if marker_pid>1 and marker_pid in marker_slots and marker_slots[marker_pid][0]:
  cleanup_failures.append(b"marker-live-after-ready")
 for fd,buf,cap,label,forward in ((out_r,marker_out,CAP,"final-marker-out",-1),(err_r,marker_err,CAP,"final-marker-err",-1),(tele_r,nested_tele,TELE_CAP,"final-marker-tele",3)):
  if fd>=0:
   try: drain(fd,buf,cap,total_deadline,label,forward)
   except BaseException as e: cleanup_failures.append((label+":"+type(e).__name__).encode("ascii","strict").lower())
 for fd,label in ((out_r,"out-r"),(out_w,"out-w"),(err_r,"err-r"),(err_w,"err-w"),(tele_r,"tele-r"),(tele_w,"tele-w"),(gate_r,"gate-r"),(gate_w,"gate-w")): close_capture(fd,total_deadline,cleanup_failures,label)
 if dirfd>=0:
  try:
   if ledger_fd>=0: recheck_regular(ledger_fd,LEDGER,ledger_key,ledger_bytes,ledger_lf,ledger_sha,ledger_terminal,total_deadline,"cleanup-ledger")
   if control_fd>=0: recheck_regular(control_fd,CONTROL,control_key,control_bytes,control_lf,control_sha,control_terminal,total_deadline,"cleanup-control")
   if resolved_fd>=0 and self_fd>=0 and outer_fd>=0: recheck_images(resolved_fd,self_fd,outer_fd,image_key,link_key,total_deadline)
   safe_recheck(tmpfd,name,dirfd,dir_key,safe,True,total_deadline)
   total_cleanup_pass=rmdir_proof(tmpfd,tmp_key,name,dirfd,dir_key,total_deadline)
  except BaseException as e: cleanup_failures.append(("filesystem:"+type(e).__name__).encode("ascii","strict").lower()); total_cleanup_pass=0
 for fd,label in ((ledger_fd,"ledger"),(control_fd,"control"),(resolved_fd,"resolved"),(self_fd,"self-image"),(outer_fd,"outer-image"),(dirfd,"safe-dir"),(tmpfd,"tmp-dir"),(rootfd,"root-dir")): close_capture(fd,total_deadline,cleanup_failures,label)
 probe_finish=mono()
 cleanup_token=b"none" if not cleanup_failures else b"present"
 final_result=b"PASS" if result==b"READY" and primary==b"none" and cleanup_token==b"none" and total_cleanup_pass==1 and marker_pid>1 and marker_status==0 and marker_slots.get(marker_pid,(1,None))[0]==0 and nested_spawned==nested_reaped and probe_start<=probe_finish and probe_finish-probe_start<=total_ns and probe_finish<=total_deadline else b"FAIL"
 if probe_finish<probe_start: probe_finish=probe_start
 terminal=(b"P27E001V4|worker=terminal|probe="+probe+b"|auth_id="+auth+b"|outer_pid="+str(outer_pid).encode("ascii")+b"|launcher_pid="+str(os.getpid()).encode("ascii")+b"|marker_pid="+str(marker_pid).encode("ascii")+b"|marker_raw_status="+str(marker_status).encode("ascii")+b"|marker_reaped="+str(int(marker_pid in marker_slots and marker_slots[marker_pid][0]==0)).encode("ascii")+b"|nested_spawned="+str(nested_spawned).encode("ascii")+b"|nested_reaped="+str(nested_reaped).encode("ascii")+b"|marker_stdout_bytes="+str(len(marker_out)).encode("ascii")+b"|marker_stdout_sha256="+hashlib.sha256(marker_out).hexdigest().encode("ascii")+b"|marker_stderr_bytes="+str(len(marker_err)).encode("ascii")+b"|marker_stderr_sha256="+hashlib.sha256(marker_err).hexdigest().encode("ascii")+b"|nested_telemetry_bytes="+str(len(nested_tele)).encode("ascii")+b"|nested_telemetry_sha256="+hashlib.sha256(nested_tele).hexdigest().encode("ascii")+b"|primary_failure="+primary+b"|cleanup_failure="+cleanup_token+b"|total_cleanup_pass="+str(total_cleanup_pass).encode("ascii")+b"|probe_start_ns="+str(probe_start).encode("ascii")+b"|probe_finish_ns="+str(probe_finish).encode("ascii")+b"|probe_elapsed_ns="+str(probe_finish-probe_start).encode("ascii")+b"|probe_bound_ns="+str(total_ns).encode("ascii")+b"|result="+final_result+b"\n")
 try:
  if marker_out: write_exact(1,bytes(marker_out),total_deadline)
  if marker_err: write_exact(2,bytes(marker_err),total_deadline)
  write_exact(1,terminal,total_deadline)
 except BaseException: pass
 if final_result!=b"PASS": raise SystemExit(90)
OWNED LAUNCHER V4 SOURCE END
```

`exact_terminal` splits on literal LF, requires the final empty element,
requires the terminal as the exact last nonempty line, and counts exact line
equality. A `terminal_marker=` field containing the same bytes is not counted.
The launcher is externally contained by the outer deadline even while it is
inside a synchronous syscall. Its post-rmdir proof compares stable device,
inode, directory type, mode, owner, and group, requires the frozen Linux held
directory link transition from 2 to 0, rechecks the parent, and requires
ENOENT for the exact pathname. A renamed held directory or deletion of a
replacement leaves the held link state nonzero and cannot PASS.

## 6. Exact unified-marker source

The marker owns every nested Python child. Its incremental telemetry records
the returned PID immediately after spawn and records the raw wait status
immediately after the one physical-reap assignment. The launcher forwards
those raw telemetry bytes while the marker is still live, so marker or
launcher failure cannot erase already observed nested ownership. Missing raw
status remains missing evidence; it is never fabricated as zero.

```text
UNIFIED MARKER V4 SOURCE BEGIN
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
ENV_TOOL=b"/usr/bin/env"
ENV_TOOL_BYTES=43976
ENV_TOOL_SHA=b"85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0"
BASH_TOOL=b"/usr/bin/bash"
BASH_TOOL_BYTES=1396520
BASH_TOOL_SHA=b"59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
CAP=131072
HARD_NOFILE=1048576
TELE_FD=3
ABORT=0

class Fail(Exception): pass

def need(v,code):
 if not v: raise Fail(code)

def mono():
 v=time.monotonic_ns(); need(type(v) is int and v>=0,"clock-value"); return v

def before(deadline,code):
 n=mono(); need(n<=deadline,code+"-pre"); return n

def after(deadline,code):
 n=mono(); need(n<=deadline,code+"-post"); return n

def canonical_decimal(raw,minimum=0,maximum=(1<<63)-1):
 need(type(raw) is bytes and raw and all(48<=c<=57 for c in raw),"decimal-grammar")
 value=int(raw); need(str(value).encode("ascii")==raw and minimum<=value<=maximum,"decimal-canonical"); return value

def call(deadline,label,fn,*args,**kwargs):
 before(deadline,label); value=fn(*args,**kwargs); after(deadline,label); return value

def close_capture(fd,deadline,failures,label):
 if fd<0: return
 try: call(deadline,label+"-close",os.close,fd)
 except BaseException as e: failures.append((label+":"+type(e).__name__).encode("ascii","strict").lower())

def set_nonblock(fd,deadline):
 flags=call(deadline,"fcntl-get",fcntl.fcntl,fd,fcntl.F_GETFL); call(deadline,"fcntl-set",fcntl.fcntl,fd,fcntl.F_SETFL,flags|os.O_NONBLOCK)

def write_exact(fd,data,deadline):
 set_nonblock(fd,deadline); poller=select.poll(); poller.register(fd,select.POLLOUT|select.POLLERR|select.POLLHUP); pos=0
 for unused in range(8192):
  if pos==len(data): after(deadline,"write-complete"); return
  before(deadline,"write")
  try: count=os.write(fd,data[pos:]); after(deadline,"write"); need(count>0,"write-zero"); pos+=count; continue
  except BlockingIOError: after(deadline,"write")
  except InterruptedError: after(deadline,"write"); continue
  before(deadline,"write-poll"); poller.poll(max(0,min(10,(deadline-mono()+999999)//1000000))); after(deadline,"write-poll")
 raise Fail("write-iterations")

def hash_fd(fd,size,deadline,label):
 call(deadline,label+"-seek",os.lseek,fd,0,os.SEEK_SET); digest=hashlib.sha256(); total=0
 for unused in range((size+1048575)//1048576+1):
  before(deadline,label+"-read")
  try: chunk=os.read(fd,min(1048576,size-total+1))
  except InterruptedError: after(deadline,label+"-read"); continue
  after(deadline,label+"-read")
  if not chunk: break
  total+=len(chunk); need(total<=size,label+"-growth"); digest.update(chunk)
 need(total==size,label+"-short"); return digest.hexdigest().encode("ascii")

def stat_key(value): return (value.st_dev,value.st_ino,value.st_mode,value.st_nlink,value.st_uid,value.st_gid,value.st_size)

def bind_image(deadline):
 link=call(deadline,"image-link-lstat",os.lstat,PYTHON); need(stat.S_ISLNK(link.st_mode) and stat.S_IMODE(link.st_mode)==0o777 and link.st_nlink==1 and link.st_uid==0 and link.st_gid==0 and link.st_size==10,"image-link")
 need(call(deadline,"image-readlink",os.readlink,PYTHON)==b"python3.12","image-target")
 resolved=call(deadline,"image-resolved-open",os.open,PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW); self_fd=call(deadline,"image-self-open",os.open,b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC)
 a=call(deadline,"image-resolved-stat",os.fstat,resolved); b=call(deadline,"image-self-stat",os.fstat,self_fd)
 need(stat_key(a)==stat_key(b) and stat.S_ISREG(a.st_mode) and stat.S_IMODE(a.st_mode)==0o755 and a.st_nlink==1 and a.st_uid==0 and a.st_gid==0 and a.st_size==PY_BYTES,"image-identity")
 need(hash_fd(resolved,PY_BYTES,deadline,"image-resolved-hash")==PY_SHA and hash_fd(self_fd,PY_BYTES,deadline,"image-self-hash")==PY_SHA,"image-hash")
 return resolved,self_fd,stat_key(a),stat_key(link)

def recheck_image(resolved,self_fd,key,link_key,deadline):
 a=call(deadline,"terminal-resolved-stat",os.fstat,resolved); b=call(deadline,"terminal-self-stat",os.fstat,self_fd); p=call(deadline,"terminal-image-path",os.stat,PYRES,follow_symlinks=False); link=call(deadline,"terminal-link-stat",os.lstat,PYTHON)
 need(stat_key(a)==stat_key(b)==stat_key(p)==key and stat_key(link)==link_key and call(deadline,"terminal-readlink",os.readlink,PYTHON)==b"python3.12","terminal-image-identity")
 need(hash_fd(resolved,PY_BYTES,deadline,"terminal-resolved-hash")==PY_SHA and hash_fd(self_fd,PY_BYTES,deadline,"terminal-self-hash")==PY_SHA,"terminal-image-hash")

def bind_tool(path,size,digest,deadline,label):
 fd=call(deadline,label+"-open",os.open,path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW); held=call(deadline,label+"-fstat",os.fstat,fd); pathstat=call(deadline,label+"-stat",os.stat,path,follow_symlinks=False)
 need(stat_key(held)==stat_key(pathstat) and stat.S_ISREG(held.st_mode) and stat.S_IMODE(held.st_mode)==0o755 and held.st_nlink==1 and held.st_uid==0 and held.st_gid==0 and held.st_size==size,label+"-identity")
 need(hash_fd(fd,size,deadline,label+"-hash")==digest,label+"-digest"); return fd,stat_key(held)

def recheck_tool(fd,path,size,digest,key,deadline,label):
 held=call(deadline,label+"-fstat",os.fstat,fd); pathstat=call(deadline,label+"-stat",os.stat,path,follow_symlinks=False)
 need(stat_key(held)==stat_key(pathstat)==key and hash_fd(fd,size,deadline,label+"-hash")==digest,label+"-recheck")

def mapped_libc(deadline):
 fd=call(deadline,"maps-open",os.open,b"/proc/self/maps",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:
  raw=bytearray()
  for unused in range(1025):
   before(deadline,"maps-read")
   try: chunk=os.read(fd,4096)
   except InterruptedError: after(deadline,"maps-read"); continue
   after(deadline,"maps-read")
   if not chunk: break
   raw.extend(chunk); need(len(raw)<=4194304,"maps-cap")
  else: raise Fail("maps-iterations")
 finally: call(deadline,"maps-close",os.close,fd)
 need(raw.endswith(b"\n") and b"\x00" not in raw,"maps-frame"); found=set()
 for line in bytes(raw).split(b"\n")[:-1]:
  parts=line.split(None,5)
  if len(parts)==6 and b"x" in parts[1] and parts[5].startswith(b"/") and parts[5].rsplit(b"/",1)[-1].startswith(b"libc.so"):
   device=parts[3].split(b":"); need(len(device)==2 and len(device[0])==2 and len(device[1])==2 and all(c in b"0123456789abcdef" for c in device[0]+device[1]),"maps-device")
   inode=canonical_decimal(parts[4]); found.add((parts[5],os.makedev(int(device[0],16),int(device[1],16)),inode))
 need(len(found)==1,"libc-mapping-count"); path,mapdev,mapino=found.pop(); need(not path.endswith(b" (deleted)"),"libc-deleted")
 libc_fd=call(deadline,"libc-open",os.open,path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW); held=call(deadline,"libc-fstat",os.fstat,libc_fd); pathstat=call(deadline,"libc-stat",os.stat,path,follow_symlinks=False)
 need(stat_key(held)==stat_key(pathstat) and stat.S_ISREG(held.st_mode) and held.st_dev==mapdev and held.st_ino==mapino and held.st_nlink==1,"libc-identity")
 digest=hash_fd(libc_fd,held.st_size,deadline,"libc-hash"); return libc_fd,path,mapdev,mapino,stat_key(held),digest

def recheck_libc(fd,path,mapdev,mapino,key,digest,deadline):
 held=call(deadline,"terminal-libc-fstat",os.fstat,fd); pathstat=call(deadline,"terminal-libc-stat",os.stat,path,follow_symlinks=False)
 need(stat_key(held)==stat_key(pathstat)==key and held.st_dev==mapdev and held.st_ino==mapino and hash_fd(fd,held.st_size,deadline,"terminal-libc-hash")==digest,"terminal-libc")

CHILD_SOURCE=b'''\
import errno
import hashlib
import os
import signal
import stat
import sys
import time
P=b"/root/miniconda3/bin/python3"
R=b"/root/miniconda3/bin/python3.12"
N=30626264
H=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
E={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
D=tuple(sorted(int(x)for x in signal.valid_signals()if int(x)not in(int(signal.SIGKILL),int(signal.SIGSTOP))))
class F(Exception):pass
def n(v,c):
 if not v:raise F(c)
def t():
 v=time.monotonic_ns();n(type(v)is int and v>=0,"clock");return v
def q(d,c):n(t()<=d,c)
def c(d,k,f,*a,**kw):q(d,k+"-pre");v=f(*a,**kw);q(d,k+"-post");return v
def h(fd,size,d,k):
 c(d,k+"-seek",os.lseek,fd,0,os.SEEK_SET);z=hashlib.sha256();m=0
 for u in range((size+1048575)//1048576+1):
  q(d,k+"-read-pre")
  try:x=os.read(fd,min(1048576,size-m+1))
  except InterruptedError:q(d,k+"-read-post");continue
  q(d,k+"-read-post")
  if not x:break
  m+=len(x);n(m<=size,k+"-growth");z.update(x)
 n(m==size,k+"-short");return z.hexdigest().encode("ascii")
def k(s):return(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
def image(d):
 l=c(d,"link-stat",os.lstat,P);n(stat.S_ISLNK(l.st_mode)and stat.S_IMODE(l.st_mode)==0o777 and l.st_nlink==1 and l.st_uid==0 and l.st_gid==0 and l.st_size==10 and c(d,"link-read",os.readlink,P)==b"python3.12","link")
 a=c(d,"resolved-open",os.open,R,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW);b=c(d,"self-open",os.open,b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC)
 x=c(d,"resolved-stat",os.fstat,a);y=c(d,"self-stat",os.fstat,b);n(k(x)==k(y)and stat.S_ISREG(x.st_mode)and stat.S_IMODE(x.st_mode)==0o755 and x.st_nlink==1 and x.st_uid==0 and x.st_gid==0 and x.st_size==N,"image")
 n(h(a,N,d,"resolved-hash")==H and h(b,N,d,"self-hash")==H,"hash");return a,b,x.st_dev,x.st_ino
def dec(s):
 b=os.fsencode(s);n(b and b.isdigit()and str(int(b)).encode("ascii")==b,"decimal");return int(b)
primary=b"none";cleanup=[];result=b"FAIL";mode=b"invalid";deadline=0;safe=b"";a=b=-1;phase=b"terminal";code=0
try:
 n(len(sys.argv)==4 and sys.argv[0]=="-c","argv");mode=os.fsencode(sys.argv[1]);deadline=dec(sys.argv[2]);safe=os.fsencode(sys.argv[3]);n(mode in(b"INFO",b"BLOCK0",b"EXIT23",b"TERM",b"CHAIN"),"mode")
 n(sys.orig_argv[:8]==[P.decode("ascii"),"-I","-S","-B","-P","-X","utf8","-c"]and sys.executable==P.decode("ascii")and dict(os.environb)==E,"runtime");n(sys.flags.isolated==1 and sys.flags.ignore_environment==1 and sys.flags.no_site==1 and sys.flags.no_user_site==1 and sys.flags.dont_write_bytecode==1 and sys.flags.safe_path==1 and sys.flags.utf8_mode==1 and sys.flags.hash_randomization==1,"flags");signal.pthread_sigmask(signal.SIG_SETMASK,set());[signal.signal(x,signal.SIG_DFL)for x in D];n(signal.pthread_sigmask(signal.SIG_BLOCK,set())==set()and all(signal.getsignal(x)==signal.SIG_DFL for x in D),"signals");n(c(deadline,"cwd",os.getcwdb)==safe,"cwd")
 a,b,dev,ino=image(deadline);source=os.fsencode(sys.orig_argv[8]);source_sha=hashlib.sha256(source).hexdigest().encode("ascii");env_sha=hashlib.sha256(b"\x00".join(k+b"="+E[k]for k in sorted(E))).hexdigest().encode("ascii");under=int(b"_"not in os.environb)
 phase=b"ready" if mode in(b"BLOCK0",b"EXIT23",b"TERM")else b"terminal";result=b"PASS"
 pid=c(deadline,"pid",os.getpid);sid=c(deadline,"sid",os.getsid,0);pgid=c(deadline,"pgid",os.getpgrp);line=b"P27E001V4|child=observation|mode="+mode+b"|pid="+str(pid).encode("ascii")+b"|sid="+str(sid).encode("ascii")+b"|pgid="+str(pgid).encode("ascii")+b"|image_dev="+str(dev).encode("ascii")+b"|image_ino="+str(ino).encode("ascii")+b"|image_sha="+H+b"|source_sha="+source_sha+b"|cwd_hex="+safe.hex().encode("ascii")+b"|environment_sha="+env_sha+b"|underscore_absent="+str(under).encode("ascii")+b"|phase="+phase+b"|primary_failure=none|cleanup_failure=none|result=PASS\n"
 q(deadline,"child-write-pre");n(os.write(1,line)==len(line),"child-write");q(deadline,"child-write-post")
 if mode in(b"BLOCK0",b"EXIT23"):
  q(deadline,"gate-read-pre");gate=os.read(3,1);q(deadline,"gate-read-post");n(gate==b"G","gate");code=23 if mode==b"EXIT23"else 0
 elif mode==b"TERM":q(deadline,"term-pre");os.kill(os.getpid(),15)
except BaseException as e:
 if primary==b"none":primary=(os.fsencode(str(e))if isinstance(e,F)else type(e).__name__.encode("ascii","strict").lower())
 result=b"FAIL";code=91
finally:
 for fd in(a,b):
  if fd>=0:
   try:os.close(fd)
   except BaseException as e:cleanup.append(type(e).__name__.encode("ascii","strict").lower())
raise SystemExit(code if result==b"PASS"and not cleanup else 92)
'''

def child_parse(raw,mode,phase,pid,source_sha,safe):
 need(raw.endswith(b"\n") and raw.count(b"\n")==1 and b"\r" not in raw and b"\x00" not in raw,"child-frame")
 line=raw[:-1]; keys=(b"mode",b"pid",b"sid",b"pgid",b"image_dev",b"image_ino",b"image_sha",b"source_sha",b"cwd_hex",b"environment_sha",b"underscore_absent",b"phase",b"primary_failure",b"cleanup_failure",b"result")
 parts=line.split(b"|"); need(len(parts)==2+len(keys) and parts[:2]==[b"P27E001V4",b"child=observation"],"child-field-count"); values={}
 for item,key in zip(parts[2:],keys):
  prefix=key+b"="; need(item.startswith(prefix) and item.count(b"=")==1,"child-order"); values[key]=item[len(prefix):]
 need(values[b"mode"]==mode and canonical_decimal(values[b"pid"],2)==pid and canonical_decimal(values[b"sid"],2)==os.getsid(0) and canonical_decimal(values[b"pgid"],2)==os.getpgrp(),"child-topology")
 canonical_decimal(values[b"image_dev"]); canonical_decimal(values[b"image_ino"]); need(values[b"image_sha"]==PY_SHA and values[b"source_sha"]==source_sha,"child-binding")
 need(values[b"cwd_hex"]==safe.hex().encode("ascii") and len(values[b"environment_sha"])==64 and all(c in b"0123456789abcdef" for c in values[b"environment_sha"]),"child-runtime")
 need(values[b"underscore_absent"]==b"1" and values[b"phase"]==phase and values[b"primary_failure"]==values[b"cleanup_failure"]==b"none" and values[b"result"]==b"PASS","child-result")
 return tuple(canonical_decimal(values[key]) for key in (b"pid",b"sid",b"pgid"))

def telemetry(kind,pid,mode,deadline,status=None):
 need(TELE_FD==3,"telemetry-closed")
 if kind==b"spawn": line=b"P27E001V4|child=spawn|pid="+str(pid).encode("ascii")+b"|mode="+mode+b"\n"
 elif kind==b"reap": line=b"P27E001V4|child=reap|pid="+str(pid).encode("ascii")+b"|mode="+mode+b"|raw_status="+str(status).encode("ascii")+b"\n"
 else: raise Fail("telemetry-kind")
 need(len(line)<=4096,"telemetry-pipe-buf"); write_exact(TELE_FD,line,deadline)

def raw_telemetry(pid,chunk,deadline):
 need(pid in raw_seq and chunk and len(chunk)<=512,"raw-telemetry-input"); sequence=raw_seq[pid]; line=b"P27E001V4|child=raw|pid="+str(pid).encode("ascii")+b"|seq="+str(sequence).encode("ascii")+b"|bytes="+str(len(chunk)).encode("ascii")+b"|sha256="+hashlib.sha256(chunk).hexdigest().encode("ascii")+b"|hex="+chunk.hex().encode("ascii")+b"\n"; need(len(line)<=4096,"raw-telemetry-pipe-buf"); write_exact(TELE_FD,line,deadline); raw_seq[pid]=sequence+1

slots={}; raw_seq={}; pids=[]; statuses=[]; spawned=0; reaped=0; owned=[]

def spawn_child(argv,mode,deadline,env=ENV,file_actions=()):
 global spawned
 before(deadline,"child-spawn"); pid=os.posix_spawn(argv[0],argv,env,file_actions=file_actions,setsigmask=(),setsigdef=tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))); after(deadline,"child-spawn")
 need(pid>1 and pid not in slots,"child-pid"); slots[pid]=(1,None,mode); raw_seq[pid]=0; pids.append(pid); spawned+=1; telemetry(b"spawn",pid,mode,deadline); return pid

def physical_reap(pid,status):
 live,unused,mode=slots[pid]; slots[pid]=(0,status,mode)

def wait_owned(pid,deadline):
 global reaped
 need(pid in slots and slots[pid][0]==1,"wait-ownership"); before(deadline,"child-waitpid")
 try: got,status=os.waitpid(pid,os.WNOHANG)
 except InterruptedError: after(deadline,"child-waitpid"); return 0
 except ChildProcessError as e: raise Fail("child-echild") from e
 if got==pid:
  physical_reap(pid,status); statuses.append(status); reaped+=1
  after(deadline,"child-waitpid"); telemetry(b"reap",pid,slots[pid][2],deadline,status); return pid
 after(deadline,"child-waitpid"); need(got==0,"child-wait-return"); return 0

def drain_child(pid,fd,buf,deadline,label):
 eof=False
 for unused in range(128):
  before(deadline,label+"-read")
  try: chunk=os.read(fd,512)
  except BlockingIOError: after(deadline,label+"-read"); break
  except InterruptedError: after(deadline,label+"-read"); continue
  after(deadline,label+"-read")
  if not chunk: eof=True; break
  buf.extend(chunk); need(len(buf)<=CAP,label+"-cap"); raw_telemetry(pid,chunk,deadline)
 return eof

def finish_child(pid,fd,deadline,initial=b""):
 set_nonblock(fd,deadline); buf=bytearray(initial); eof=False; poller=select.poll(); poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(20000):
  if slots[pid][0]: wait_owned(pid,deadline)
  eof=drain_child(pid,fd,buf,deadline,"child-stream") or eof
  if slots[pid][0]==0 and eof: after(deadline,"child-complete"); return slots[pid][1],bytes(buf)
  before(deadline,"child-poll"); poller.poll(max(0,min(10,(deadline-mono()+999999)//1000000))); after(deadline,"child-poll")
 raise Fail("child-iterations")

def ready_child(pid,fd,deadline):
 set_nonblock(fd,deadline); buf=bytearray(); poller=select.poll(); poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(20000):
  wait_owned(pid,deadline); need(slots[pid][0]==1,"child-before-ready")
  drain_child(pid,fd,buf,deadline,"child-ready")
  if bytes(buf).count(b"\n")==1: after(deadline,"child-ready-complete"); return bytes(buf)
  need(b"\n" not in buf,"child-ready-lines"); before(deadline,"child-ready-poll"); poller.poll(max(0,min(10,(deadline-mono()+999999)//1000000))); after(deadline,"child-ready-poll")
 raise Fail("child-ready-iterations")

def child_pipe(deadline):
 before(deadline,"child-pipe"); r,w=os.pipe2(os.O_CLOEXEC); after(deadline,"child-pipe"); owned.extend((r,w)); return r,w

def spawn_observed(source,mode,deadline,safe,gate=False,argv_override=None,env=ENV):
 r,w=child_pipe(deadline); gate_r=gate_w=-1
 if gate:
  before(deadline,"child-gate-pipe"); gate_r,gate_w=os.pipe2(os.O_CLOEXEC); after(deadline,"child-gate-pipe"); owned.extend((gate_r,gate_w))
 actions=[(os.POSIX_SPAWN_DUP2,w,1),(os.POSIX_SPAWN_CLOSE,r),(os.POSIX_SPAWN_CLOSE,w)]
 if gate: actions.extend(((os.POSIX_SPAWN_DUP2,gate_r,3),(os.POSIX_SPAWN_CLOSE,gate_r),(os.POSIX_SPAWN_CLOSE,gate_w)))
 else: actions.append((os.POSIX_SPAWN_CLOSE,3))
 argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",source,mode,str(deadline).encode("ascii"),safe) if argv_override is None else argv_override
 pid=spawn_child(argv,mode,deadline,env=env,file_actions=tuple(actions)); call(deadline,"child-w-close",os.close,w); owned.remove(w)
 if gate: call(deadline,"child-gate-r-close",os.close,gate_r); owned.remove(gate_r)
 return pid,r,gate_w

def cleanup_live(deadline,failures):
 for pid in tuple(pids):
  if slots[pid][0]:
   try: wait_owned(pid,deadline)
   except BaseException as e: failures.append(("wait:"+type(e).__name__).encode("ascii","strict").lower())
 for pid in tuple(pids):
  if slots[pid][0]:
   try: call(deadline,"child-term",os.kill,pid,signal.SIGTERM)
   except ProcessLookupError: failures.append(b"term-esrch")
 term=min(deadline,mono()+100000000)
 for unused in range(1024):
  for pid in tuple(pids):
   if slots[pid][0]:
    try: wait_owned(pid,term)
    except BaseException as e: failures.append(("term-wait:"+type(e).__name__).encode("ascii","strict").lower())
  if all(slots[pid][0]==0 for pid in pids): break
  before(term,"cleanup-term-poll"); select.poll().poll(max(0,min(5,(term-mono()+999999)//1000000))); after(term,"cleanup-term-poll")
 for pid in tuple(pids):
  if slots[pid][0]:
   try: wait_owned(pid,deadline)
   except BaseException as e: failures.append(("prekill-wait:"+type(e).__name__).encode("ascii","strict").lower())
   if slots[pid][0]:
    try: call(deadline,"child-kill",os.kill,pid,signal.SIGKILL)
    except ProcessLookupError: failures.append(b"kill-esrch")
 for unused in range(4096):
  for pid in tuple(pids):
   if slots[pid][0]:
    try: wait_owned(pid,deadline)
    except BaseException as e: failures.append(("kill-wait:"+type(e).__name__).encode("ascii","strict").lower())
  if all(slots[pid][0]==0 for pid in pids): break
  before(deadline,"cleanup-kill-poll"); select.poll().poll(max(0,min(5,(deadline-mono()+999999)//1000000))); after(deadline,"cleanup-kill-poll")

def row(rows,probe,key,value):
 if type(value) is int: value=str(value).encode("ascii")
 elif type(value) is str: value=value.encode("ascii")
 need(type(key) is bytes and type(value) is bytes and key and value and b"|" not in key+value and b"\n" not in key+value and b"\r" not in key+value and b"=" not in key+value,"row-frame")
 rows.append(b"P27E001V4|probe="+probe+b"|"+key+b"="+value)

def abort_handler(signum,frame):
 global ABORT
 ABORT=1

primary=b"none"; cleanup_failures=[]; result=b"FAIL"; rows=[]
ID=b"invalid"; SAFE=b""; MARKER_SHA=b""; DEADLINE=mono(); TOTAL_NS=0; EXTRA=()
resolved_fd=self_fd=libc_fd=env_fd=bash_fd=-1; image_key=link_key=None
probe_start=mono(); probe_finish=probe_start; p07_pending=0

try:
 need(len(sys.argv)>=6 and sys.argv[0]=="-c","argv-count")
 ID=os.fsencode(sys.argv[1]); SAFE=os.fsencode(sys.argv[2]); MARKER_SHA=os.fsencode(sys.argv[3]); DEADLINE=canonical_decimal(os.fsencode(sys.argv[4]),1); TOTAL_NS=canonical_decimal(os.fsencode(sys.argv[5]),2000000000,10000000000); EXTRA=tuple(os.fsencode(x) for x in sys.argv[6:])
 need(ID in (b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13"),"probe-id")
 need(len(MARKER_SHA)==64 and all(c in b"0123456789abcdef" for c in MARKER_SHA),"marker-sha")
 source=os.fsencode(sys.orig_argv[8]); need(hashlib.sha256(source).hexdigest().encode("ascii")==MARKER_SHA,"marker-source")
 need(sys.orig_argv[:8]==[PYTHON.decode("ascii"),"-I","-S","-B","-P","-X","utf8","-c"] and sys.executable==PYTHON.decode("ascii") and dict(os.environb)==ENV,"marker-runtime")
 need(sys.flags.isolated==1 and sys.flags.ignore_environment==1 and sys.flags.no_site==1 and sys.flags.no_user_site==1 and sys.flags.dont_write_bytecode==1 and sys.flags.safe_path==1 and sys.flags.utf8_mode==1 and sys.flags.hash_randomization==1,"marker-flags")
 need(SAFE.startswith(b"/tmp/p27-e001-host-v4-") and len(SAFE)==len(b"/tmp/p27-e001-host-v4-")+64 and call(DEADLINE,"marker-getcwd",os.getcwdb)==SAFE,"marker-cwd")
 need(resource.getrlimit(resource.RLIMIT_CPU)==(3,3) and resource.getrlimit(resource.RLIMIT_AS)==(268435456,268435456) and resource.getrlimit(resource.RLIMIT_FSIZE)==(1048576,1048576) and resource.getrlimit(resource.RLIMIT_CORE)==(0,0) and resource.getrlimit(resource.RLIMIT_NOFILE)==(4096,HARD_NOFILE),"marker-limits"); marker_nproc=resource.getrlimit(resource.RLIMIT_NPROC); need(4<=marker_nproc[0]<=32 and (marker_nproc[1]==resource.RLIM_INFINITY or marker_nproc[0]<=marker_nproc[1]),"marker-nproc")
 fds=[]; nodes=[]
 for fd in range(4096):
  before(DEADLINE,"initial-fd")
  try: fcntl.fcntl(fd,fcntl.F_GETFD); after(DEADLINE,"initial-fd")
  except OSError as e:
   after(DEADLINE,"initial-fd")
   if e.errno==errno.EBADF: continue
   raise
  fds.append(fd); held=call(DEADLINE,"initial-fstat",os.fstat,fd); need(stat.S_ISFIFO(held.st_mode),"initial-fd-type"); nodes.append((held.st_dev,held.st_ino))
 need(fds==[0,1,2,3,4] and len(set(nodes))==5,"initial-fds")
 marker_signal_defs=tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP)))); signal.pthread_sigmask(signal.SIG_SETMASK,set())
 for number in marker_signal_defs: signal.signal(number,signal.SIG_DFL)
 need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==set() and all(signal.getsignal(number)==signal.SIG_DFL for number in marker_signal_defs),"marker-signals")
 signal.signal(signal.SIGTERM,abort_handler); signal.signal(signal.SIGINT,abort_handler)
 set_nonblock(4,DEADLINE); gate=bytearray(); gate_eof=False; gate_poll=select.poll(); gate_poll.register(4,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(1024):
  before(DEADLINE,"marker-gate-read")
  try: chunk=os.read(4,2)
  except BlockingIOError: after(DEADLINE,"marker-gate-read"); chunk=None
  except InterruptedError: after(DEADLINE,"marker-gate-read"); continue
  else: after(DEADLINE,"marker-gate-read")
  if chunk==b"": gate_eof=True
  elif chunk: gate.extend(chunk); need(len(gate)<=2,"marker-gate-cap")
  if gate_eof: break
  before(DEADLINE,"marker-gate-poll"); gate_poll.poll(max(0,min(10,(DEADLINE-mono()+999999)//1000000))); after(DEADLINE,"marker-gate-poll")
 need(bytes(gate)==b"L" and gate_eof,"marker-gate"); call(DEADLINE,"marker-gate-close",os.close,4)
 resolved_fd,self_fd,image_key,link_key=bind_image(DEADLINE); probe_start=mono(); after(DEADLINE,"probe-start")
 if ID==b"P00":
  need(len(EXTRA)==0,"p00-extra"); need(len(CHILD_SOURCE)+2<251414,"p00-base-size")
  synthetic=CHILD_SOURCE+b"\n#"+b"x"*(251414-len(CHILD_SOURCE)-2); need(len(synthetic)==251414 and b"\x00" not in synthetic and synthetic.isascii(),"p00-source")
  returned=0; e2big=0
  try:
   pid,fd,unused_gate=spawn_observed(synthetic,b"INFO",DEADLINE,SAFE); returned=1; status,raw=finish_child(pid,fd,DEADLINE); call(DEADLINE,"p00-fd-close",os.close,fd); owned.remove(fd)
   need(status==0,"p00-status"); child_parse(raw,b"INFO",b"terminal",pid,hashlib.sha256(synthetic).hexdigest().encode("ascii"),SAFE)
  except OSError as e:
   need(e.errno==errno.E2BIG,"p00-errno"); e2big=1
  need(returned+e2big==1,"p00-branch")
  row(rows,ID,b"source_item_bytes",251414); row(rows,ID,b"source_item_accounted_bytes",251415); row(rows,ID,b"source_item_sha256",hashlib.sha256(synthetic).hexdigest()); row(rows,ID,b"arg_max",call(DEADLINE,"p00-argmax",os.sysconf,"SC_ARG_MAX")); row(rows,ID,b"spawn_returned",returned); row(rows,ID,b"e2big",e2big); row(rows,ID,b"transport_feasible",returned)
 elif ID==b"P01D":
  need(len(EXTRA)==0,"p01d-extra"); libc_fd,lpath,lmapdev,lmapino,lkey,ldigest=mapped_libc(DEADLINE); conf=call(DEADLINE,"libc-confstr",os.confstr,"CS_GNU_LIBC_VERSION"); need(type(conf) is str and conf.isascii(),"libc-confstr")
  row(rows,ID,b"python_image_dev",image_key[0]); row(rows,ID,b"python_image_ino",image_key[1]); row(rows,ID,b"python_image_mode",format(image_key[2],"o")); row(rows,ID,b"python_image_nlink",image_key[3]); row(rows,ID,b"python_image_uid",image_key[4]); row(rows,ID,b"python_image_gid",image_key[5]); row(rows,ID,b"python_image_bytes",image_key[6]); row(rows,ID,b"python_image_sha256",PY_SHA)
  row(rows,ID,b"libc_confstr_hex",conf.encode("ascii").hex()); row(rows,ID,b"libc_path_hex",lpath.hex()); row(rows,ID,b"libc_map_dev",lmapdev); row(rows,ID,b"libc_map_ino",lmapino); row(rows,ID,b"libc_open_dev",lkey[0]); row(rows,ID,b"libc_open_ino",lkey[1]); row(rows,ID,b"libc_mode",format(lkey[2],"o")); row(rows,ID,b"libc_nlink",lkey[3]); row(rows,ID,b"libc_uid",lkey[4]); row(rows,ID,b"libc_gid",lkey[5]); row(rows,ID,b"libc_bytes",lkey[6]); row(rows,ID,b"libc_sha256",ldigest); row(rows,ID,b"posix_spawn_module",os.posix_spawn.__module__); row(rows,ID,b"posix_spawn_name",os.posix_spawn.__name__); row(rows,ID,b"posix_spawn_type",type(os.posix_spawn).__name__); row(rows,ID,b"backend_surface",b"cpython-posix-builtin-plus-mapped-open-libc"); row(rows,ID,b"spawn_premise_satisfied",0)
  recheck_libc(libc_fd,lpath,lmapdev,lmapino,lkey,ldigest,DEADLINE)
 elif ID==b"P01C":
  need(len(EXTRA)==13,"p01c-extra"); path=bytes.fromhex(EXTRA[0].decode("ascii")); need(path.hex().encode("ascii")==EXTRA[0],"p01c-path-hex")
  expected=(path,canonical_decimal(EXTRA[1]),canonical_decimal(EXTRA[2]),int(EXTRA[3],8),canonical_decimal(EXTRA[4]),canonical_decimal(EXTRA[5]),canonical_decimal(EXTRA[6]),canonical_decimal(EXTRA[7]),EXTRA[8],bytes.fromhex(EXTRA[9].decode("ascii")).decode("ascii"),canonical_decimal(EXTRA[10]),canonical_decimal(EXTRA[11]),EXTRA[12])
  need(format(expected[3],"o").encode("ascii")==EXTRA[3] and len(EXTRA[8])==len(EXTRA[12])==64 and all(c in b"0123456789abcdef" for c in EXTRA[8]+EXTRA[12]),"p01c-canonical")
  libc_fd,lpath,lmapdev,lmapino,lkey,ldigest=mapped_libc(DEADLINE); conf=call(DEADLINE,"p01c-confstr",os.confstr,"CS_GNU_LIBC_VERSION"); actual=(lpath,lmapdev,lmapino,lkey[2],lkey[3],lkey[4],lkey[5],lkey[6],ldigest,conf,image_key[0],image_key[1],PY_SHA); need(actual==expected,"p01c-seal")
  pid,fd,unused_gate=spawn_observed(CHILD_SOURCE,b"INFO",DEADLINE,SAFE); status,raw=finish_child(pid,fd,DEADLINE); call(DEADLINE,"p01c-fd-close",os.close,fd); owned.remove(fd); need(status==0,"p01c-status"); cp,cs,cg=child_parse(raw,b"INFO",b"terminal",pid,hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii"),SAFE)
  row(rows,ID,b"python_image_dev",image_key[0]); row(rows,ID,b"python_image_ino",image_key[1]); row(rows,ID,b"python_image_sha256",PY_SHA); row(rows,ID,b"libc_path_hex",lpath.hex()); row(rows,ID,b"libc_map_dev",lmapdev); row(rows,ID,b"libc_map_ino",lmapino); row(rows,ID,b"libc_sha256",ldigest); row(rows,ID,b"libc_confstr_hex",conf.encode("ascii").hex()); row(rows,ID,b"posix_spawn_module",os.posix_spawn.__module__); row(rows,ID,b"posix_spawn_name",os.posix_spawn.__name__); row(rows,ID,b"child_raw_bytes",len(raw)); row(rows,ID,b"child_raw_sha256",hashlib.sha256(raw).hexdigest()); row(rows,ID,b"child_pid",cp); row(rows,ID,b"child_sid",cs); row(rows,ID,b"child_pgid",cg); row(rows,ID,b"spawn_premise_satisfied",1); recheck_libc(libc_fd,lpath,lmapdev,lmapino,lkey,ldigest,DEADLINE)
 elif ID==b"P02":
  need(len(EXTRA)==0,"p02-extra"); recheck_image(resolved_fd,self_fd,image_key,link_key,DEADLINE); close_capture(resolved_fd,DEADLINE,cleanup_failures,"p02-resolved"); close_capture(self_fd,DEADLINE,cleanup_failures,"p02-self"); resolved_fd=self_fd=-1; close_capture(TELE_FD,DEADLINE,cleanup_failures,"p02-telemetry"); TELE_FD=-1
  fds=[]; nodes=[]
  for fd in range(4096):
   before(DEADLINE,"p02-fd")
   try: flags=fcntl.fcntl(fd,fcntl.F_GETFD); after(DEADLINE,"p02-fd")
   except OSError as e:
    after(DEADLINE,"p02-fd")
    if e.errno==errno.EBADF: continue
    raise
   fds.append(fd); held=call(DEADLINE,"p02-fstat",os.fstat,fd); need(stat.S_ISFIFO(held.st_mode),"p02-fd-type"); nodes.append((held.st_dev,held.st_ino,flags))
  need(fds==[0,1,2] and len(set((x[0],x[1]) for x in nodes))==3,"p02-fds")
  environment=b",".join((key+b"="+ENV[key]).hex().encode("ascii") for key in sorted(ENV)); row(rows,ID,b"environment",environment); row(rows,ID,b"environment_count",10); row(rows,ID,b"cwd_hex",SAFE.hex()); row(rows,ID,b"flags",b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1"); row(rows,ID,b"fds",b"0,1,2"); row(rows,ID,b"fd_nodes",b",".join(("%d:%d:%d"%item).encode("ascii") for item in nodes))
  for key,which,want in ((b"rlimit_cpu",resource.RLIMIT_CPU,(3,3)),(b"rlimit_as",resource.RLIMIT_AS,(268435456,268435456)),(b"rlimit_fsize",resource.RLIMIT_FSIZE,(1048576,1048576)),(b"rlimit_core",resource.RLIMIT_CORE,(0,0)),(b"rlimit_nofile",resource.RLIMIT_NOFILE,(4096,HARD_NOFILE))):
   got=resource.getrlimit(which); need(got==want,"p02-limit"); row(rows,ID,key,("%d,%d"%got).encode("ascii"))
  nproc=resource.getrlimit(resource.RLIMIT_NPROC); need(nproc[0]>=4 and (nproc[1]==resource.RLIM_INFINITY or nproc[0]<=nproc[1]),"p02-nproc"); row(rows,ID,b"rlimit_nproc",("%d,%d"%nproc).encode("ascii")); resolved_fd,self_fd,image_key,link_key=bind_image(DEADLINE)
 elif ID==b"P03":
  need(len(EXTRA)==0,"p03-extra"); recheck_image(resolved_fd,self_fd,image_key,link_key,DEADLINE); close_capture(resolved_fd,DEADLINE,cleanup_failures,"p03-resolved"); close_capture(self_fd,DEADLINE,cleanup_failures,"p03-self"); resolved_fd=self_fd=-1; close_capture(TELE_FD,DEADLINE,cleanup_failures,"p03-telemetry"); TELE_FD=-1
  before_limit=resource.getrlimit(resource.RLIMIT_NOFILE); need(before_limit==(4096,HARD_NOFILE),"p03-before"); resource.setrlimit(resource.RLIMIT_NOFILE,(64,HARD_NOFILE)); heldfds=[]; emfile=0
  try:
   for unused in range(64):
    try: before(DEADLINE,"p03-pipe"); r,w=os.pipe2(os.O_CLOEXEC); after(DEADLINE,"p03-pipe"); heldfds.extend((r,w))
    except OSError as e: after(DEADLINE,"p03-pipe-error"); need(e.errno==errno.EMFILE,"p03-errno"); emfile=1; break
  finally:
   for fd in heldfds: close_capture(fd,DEADLINE,cleanup_failures,"p03-held")
  need(emfile==1,"p03-emfile"); remain=[]
  for fd in range(64):
   before(DEADLINE,"p03-census")
   try: fcntl.fcntl(fd,fcntl.F_GETFD); after(DEADLINE,"p03-census")
   except OSError as e:
    after(DEADLINE,"p03-census")
    if e.errno==errno.EBADF: continue
    raise
   remain.append(fd)
  need(remain==[0,1,2],"p03-after"); row(rows,ID,b"soft_before",4096); row(rows,ID,b"hard_before",HARD_NOFILE); row(rows,ID,b"soft_test",64); row(rows,ID,b"opened_fds",len(heldfds)); row(rows,ID,b"emfile",1); row(rows,ID,b"fds_after",b"0,1,2"); resolved_fd,self_fd,image_key,link_key=bind_image(DEADLINE)
 elif ID==b"P04":
  need(len(EXTRA)==0,"p04-extra"); definitions=tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP)))); signal.pthread_sigmask(signal.SIG_SETMASK,set())
  for number in definitions: signal.signal(number,signal.SIG_DFL)
  mask=signal.pthread_sigmask(signal.SIG_BLOCK,set()); need(mask==set(),"p04-mask")
  for number in definitions: need(signal.getsignal(number)==signal.SIG_DFL,"p04-default")
  csv=b",".join(str(x).encode("ascii") for x in definitions); row(rows,ID,b"valid_signal_count",len(signal.valid_signals())); row(rows,ID,b"default_signal_count",len(definitions)); row(rows,ID,b"defaults_csv",csv); row(rows,ID,b"defaults_sha256",hashlib.sha256(csv).hexdigest()); row(rows,ID,b"mask_empty",1); row(rows,ID,b"normalization_complete",1)
 elif ID==b"P05":
  need(len(EXTRA)==0,"p05-extra"); pid,fd,gate=spawn_observed(CHILD_SOURCE,b"EXIT23",DEADLINE,SAFE,gate=True); ready=ready_child(pid,fd,DEADLINE); child_parse(ready,b"EXIT23",b"ready",pid,hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii"),SAFE); first=wait_owned(pid,DEADLINE); need(first==0,"p05-wnohang")
  old=signal.getsignal(signal.SIGALRM)
  def alarm(signum,frame): raise InterruptedError(errno.EINTR,"bounded-probe")
  signal.signal(signal.SIGALRM,alarm); signal.setitimer(signal.ITIMER_REAL,0.02); interrupted=0
  try:
   before(DEADLINE,"p05-blocking-wait")
   try:
    got,status=os.waitpid(pid,0)
    if got==pid: physical_reap(pid,status); statuses.append(status); reaped+=1
    after(DEADLINE,"p05-blocking-wait"); telemetry(b"reap",pid,slots[pid][2],DEADLINE,status); raise Fail("p05-unexpected-reap")
   except InterruptedError as e: after(DEADLINE,"p05-blocking-wait"); need(e.errno==errno.EINTR,"p05-eintr-errno"); interrupted=1
  finally: signal.setitimer(signal.ITIMER_REAL,0.0); signal.signal(signal.SIGALRM,old)
  need(interrupted==1,"p05-eintr"); write_exact(gate,b"G",DEADLINE); close_capture(gate,DEADLINE,cleanup_failures,"p05-gate"); owned.remove(gate); status,raw=finish_child(pid,fd,DEADLINE,ready); close_capture(fd,DEADLINE,cleanup_failures,"p05-fd"); owned.remove(fd); need(os.WIFEXITED(status) and os.WEXITSTATUS(status)==23,"p05-exit")
  echild=0
  try: before(DEADLINE,"p05-echild"); os.waitpid(pid,os.WNOHANG); after(DEADLINE,"p05-echild")
  except ChildProcessError as e: after(DEADLINE,"p05-echild"); need(e.errno==errno.ECHILD,"p05-echild-errno"); echild=1
  pid2,fd2,unused_gate=spawn_observed(CHILD_SOURCE,b"TERM",DEADLINE,SAFE); status2,raw2=finish_child(pid2,fd2,DEADLINE); close_capture(fd2,DEADLINE,cleanup_failures,"p05-fd2"); owned.remove(fd2); child_parse(raw2,b"TERM",b"ready",pid2,hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii"),SAFE); need(os.WIFSIGNALED(status2) and os.WTERMSIG(status2)==signal.SIGTERM,"p05-signal")
  row(rows,ID,b"wnohang_zero",1); row(rows,ID,b"eintr",interrupted); row(rows,ID,b"exit_pid",pid); row(rows,ID,b"exit_raw",status); row(rows,ID,b"exit_code",23); row(rows,ID,b"echild",echild); row(rows,ID,b"signal_pid",pid2); row(rows,ID,b"signal_raw",status2); row(rows,ID,b"term_signal",int(signal.SIGTERM))
 elif ID==b"P06":
  need(len(EXTRA)==0,"p06-extra"); info=time.get_clock_info("monotonic"); resolution=time.clock_getres(time.CLOCK_MONOTONIC); resolution_ns=max(1,int(resolution*1000000000.0+0.999999999)); values=[mono() for unused in range(4096)]; after(DEADLINE,"p06-samples")
  need(all(values[i]<=values[i+1] for i in range(len(values)-1)),"p06-order"); deltas=[values[i+1]-values[i] for i in range(len(values)-1) if values[i+1]>values[i]]; need(deltas,"p06-progress"); start_clock=values[0]; end_clock=values[-1]; need(start_clock<=((1<<63)-1)-1000000000,"p06-headroom")
  row(rows,ID,b"implementation_hex",info.implementation.encode("ascii").hex()); row(rows,ID,b"adjustable",int(info.adjustable)); row(rows,ID,b"monotonic",int(info.monotonic)); row(rows,ID,b"declared_resolution_ns",resolution_ns); row(rows,ID,b"observed_min_delta_ns",min(deltas)); row(rows,ID,b"start_ns",start_clock); row(rows,ID,b"end_ns",end_clock); row(rows,ID,b"elapsed_ns",end_clock-start_clock); row(rows,ID,b"headroom_ns",(1<<63)-1-start_clock); row(rows,ID,b"deadline_ns",start_clock+1000000000); row(rows,ID,b"deadline_checked",1)
 elif ID==b"P07":
  need(len(EXTRA)==0,"p07-extra"); before(DEADLINE,"p07-pipe"); r,w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK); after(DEADLINE,"p07-pipe"); owned.extend((r,w)); duplicate=-1
  try:
   read_clo=int(bool(call(DEADLINE,"p07-rfd",fcntl.fcntl,r,fcntl.F_GETFD)&fcntl.FD_CLOEXEC)); write_clo=int(bool(call(DEADLINE,"p07-wfd",fcntl.fcntl,w,fcntl.F_GETFD)&fcntl.FD_CLOEXEC)); read_non=int(bool(call(DEADLINE,"p07-rfl",fcntl.fcntl,r,fcntl.F_GETFL)&os.O_NONBLOCK)); write_non=int(bool(call(DEADLINE,"p07-wfl",fcntl.fcntl,w,fcntl.F_GETFL)&os.O_NONBLOCK)); empty=0
   before(DEADLINE,"p07-empty")
   try: os.read(r,1); after(DEADLINE,"p07-empty")
   except OSError as e: after(DEADLINE,"p07-empty"); need(e.errno in (errno.EAGAIN,errno.EWOULDBLOCK),"p07-empty-errno"); empty=1
   poller=select.poll(); poller.register(r,select.POLLIN|select.POLLHUP|select.POLLERR); before(DEADLINE,"p07-initial-poll"); initial=int(bool(poller.poll(0))); after(DEADLINE,"p07-initial-poll"); need(initial==0,"p07-initial")
   before(DEADLINE,"p07-write"); count=os.write(w,b"x"); after(DEADLINE,"p07-write"); need(count==1,"p07-write-count"); before(DEADLINE,"p07-ready-poll"); events=poller.poll(max(0,min(1000,(DEADLINE-mono()+999999)//1000000))); after(DEADLINE,"p07-ready-poll"); need(events,"p07-ready")
   byte=call(DEADLINE,"p07-read-byte",os.read,r,1); need(byte==b"x","p07-byte"); duplicate=call(DEADLINE,"p07-dup",os.dup,w); owned.append(duplicate); close_capture(w,DEADLINE,cleanup_failures,"p07-w"); owned.remove(w); w=-1; eof_before=0
   before(DEADLINE,"p07-before-read")
   try: eof_before=int(os.read(r,1)==b""); after(DEADLINE,"p07-before-read")
   except OSError as e: after(DEADLINE,"p07-before-read"); need(e.errno in (errno.EAGAIN,errno.EWOULDBLOCK),"p07-before-errno")
   need(eof_before==0,"p07-before"); close_capture(duplicate,DEADLINE,cleanup_failures,"p07-dup"); owned.remove(duplicate); duplicate=-1; before(DEADLINE,"p07-hup-poll"); events=poller.poll(max(0,min(1000,(DEADLINE-mono()+999999)//1000000))); after(DEADLINE,"p07-hup-poll"); hup=int(any(fd==r and mask&select.POLLHUP for fd,mask in events)); eof=int(call(DEADLINE,"p07-eof-read",os.read,r,1)==b"")
   need((read_clo,write_clo,read_non,write_non,empty,initial,eof_before,hup,eof)==(1,1,1,1,1,0,0,1,1),"p07-observation")
   row(rows,ID,b"read_cloexec",read_clo); row(rows,ID,b"write_cloexec",write_clo); row(rows,ID,b"read_nonblock",read_non); row(rows,ID,b"write_nonblock",write_non); row(rows,ID,b"empty_eagain",empty); row(rows,ID,b"initial_readable",initial); row(rows,ID,b"byte_hex",byte.hex()); row(rows,ID,b"eof_before_last_writer",eof_before); row(rows,ID,b"hup_after_last_writer",hup); row(rows,ID,b"eof_after_last_writer",eof); p07_pending=1
  finally:
   for fd in (r,w,duplicate):
    if fd>=0: close_capture(fd,DEADLINE,cleanup_failures,"p07-final"); owned.remove(fd) if fd in owned else None
 elif ID==b"P08":
  need(len(EXTRA)==0,"p08-extra"); pid,fd,gate=spawn_observed(CHILD_SOURCE,b"BLOCK0",DEADLINE,SAFE,gate=True); ready=ready_child(pid,fd,DEADLINE); cp,cs,cg=child_parse(ready,b"BLOCK0",b"ready",pid,hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii"),SAFE); sid=call(DEADLINE,"p08-sid",os.getsid,pid); pgid=call(DEADLINE,"p08-pgid",os.getpgid,pid); need((cp,cs,cg)==(pid,sid,pgid) and sid==os.getsid(0) and pgid==os.getpgrp(),"p08-topology"); call(DEADLINE,"p08-kill-zero",os.kill,pid,0); write_exact(gate,b"G",DEADLINE); close_capture(gate,DEADLINE,cleanup_failures,"p08-gate"); owned.remove(gate); status,raw=finish_child(pid,fd,DEADLINE,ready); close_capture(fd,DEADLINE,cleanup_failures,"p08-fd"); owned.remove(fd); need(status==0,"p08-status"); absent=0
  try: call(DEADLINE,"p08-post-kill-zero",os.kill,pid,0)
  except ProcessLookupError as e: after(DEADLINE,"p08-post-esrch"); need(e.errno==errno.ESRCH,"p08-esrch-errno"); absent=1
  need(absent==1,"p08-post"); row(rows,ID,b"child_pid",pid); row(rows,ID,b"child_sid",sid); row(rows,ID,b"child_pgid",pgid); row(rows,ID,b"marker_sid",os.getsid(0)); row(rows,ID,b"marker_pgid",os.getpgrp()); row(rows,ID,b"live_pid_zero",1); row(rows,ID,b"raw_status",status); row(rows,ID,b"post_pid_esrch",1); row(rows,ID,b"reuse_proof",0)
 elif ID==b"P09":
  need(len(EXTRA)==0,"p09-extra"); pid,fd,gate=spawn_observed(CHILD_SOURCE,b"BLOCK0",DEADLINE,SAFE,gate=True); ready=ready_child(pid,fd,DEADLINE); child_parse(ready,b"BLOCK0",b"ready",pid,hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii"),SAFE); pgid=call(DEADLINE,"p09-pgid",os.getpgid,pid); need(pgid==os.getpgrp(),"p09-group"); begin=mono(); need(wait_owned(pid,DEADLINE)==0,"p09-pre-signal"); call(DEADLINE,"p09-kill",os.kill,pid,signal.SIGKILL); status,raw=finish_child(pid,fd,min(DEADLINE,begin+1000000000),ready); end=mono(); after(DEADLINE,"p09-finish"); duration=end-begin; close_capture(fd,DEADLINE,cleanup_failures,"p09-fd"); owned.remove(fd); close_capture(gate,DEADLINE,cleanup_failures,"p09-gate"); owned.remove(gate); need(0<=duration<=1000000000 and os.WIFSIGNALED(status) and os.WTERMSIG(status)==signal.SIGKILL,"p09-status"); row(rows,ID,b"child_pid",pid); row(rows,ID,b"child_pgid",pgid); row(rows,ID,b"signal",int(signal.SIGKILL)); row(rows,ID,b"raw_status",status); row(rows,ID,b"reap_start_ns",begin); row(rows,ID,b"reap_end_ns",end); row(rows,ID,b"reap_elapsed_ns",duration); row(rows,ID,b"reaped",1)
 elif ID==b"P10":
  need(len(EXTRA)==0,"p10-extra"); gotp=[]; gotg=[]; gots=[]
 for sample in range(16):
   pid,fd,unused_gate=spawn_observed(CHILD_SOURCE,b"INFO",DEADLINE,SAFE); status,raw=finish_child(pid,fd,DEADLINE); close_capture(fd,DEADLINE,cleanup_failures,"p10-fd"); owned.remove(fd); cp,cs,cg=child_parse(raw,b"INFO",b"terminal",pid,hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii"),SAFE); need(status==0 and cp==pid and cg==os.getpgrp(),"p10-child"); gotp.append(cp); gotg.append(cg); gots.append(status)
  row(rows,ID,b"sample_count",16); row(rows,ID,b"pids",b",".join(str(x).encode("ascii") for x in gotp)); row(rows,ID,b"pgids",b",".join(str(x).encode("ascii") for x in gotg)); row(rows,ID,b"statuses",b",".join(str(x).encode("ascii") for x in gots)); row(rows,ID,b"pid_duplicates",len(gotp)-len(set(gotp))); row(rows,ID,b"group_is_single_owned_launcher_group",1); row(rows,ID,b"reuse_proof",0)
 elif ID==b"P11":
  need(len(EXTRA)==0,"p11-extra"); status_fd=call(DEADLINE,"p11-status-open",os.open,b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
  try:
   status_raw=bytearray()
   for unused in range(257):
    before(DEADLINE,"p11-status-read")
    try: chunk=os.read(status_fd,4096)
    except InterruptedError: after(DEADLINE,"p11-status-read"); continue
    after(DEADLINE,"p11-status-read")
    if not chunk: break
    status_raw.extend(chunk); need(len(status_raw)<=1048576,"p11-status-cap")
  finally: call(DEADLINE,"p11-status-close",os.close,status_fd)
  caplines=[line for line in bytes(status_raw).split(b"\n") if line.startswith(b"CapEff:\t")]; need(len(caplines)==1,"p11-capeff-line"); caphex=caplines[0].split(b"\t",1)[1]; need(len(caphex)==16 and all(c in b"0123456789abcdef" for c in caphex),"p11-capeff"); cap=int(caphex,16); cap_fowner=int(bool(cap&(1<<3)))
  dir_anchor=call(DEADLINE,"p11-dir-open",os.open,b".",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW); owned.append(dir_anchor); directory=call(DEADLINE,"p11-dir-fstat",os.fstat,dir_anchor); need(stat.S_ISDIR(directory.st_mode) and stat.S_IMODE(directory.st_mode)==0o700 and directory.st_uid==0 and directory.st_gid==0,"p11-dir")
  anchor=-1; noatime=-1; created=None; removed=0
  try:
   anchor=call(DEADLINE,"p11-create",os.open,b"target",os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600,dir_fd=dir_anchor); owned.append(anchor); created_stat=call(DEADLINE,"p11-created-fstat",os.fstat,anchor); created=(created_stat.st_dev,created_stat.st_ino); need(stat.S_ISREG(created_stat.st_mode) and created_stat.st_nlink==1 and created_stat.st_uid==0 and created_stat.st_gid==0,"p11-created")
   need(call(DEADLINE,"p11-write",os.write,anchor,b"x")==1,"p11-write-count"); call(DEADLINE,"p11-fsync",os.fsync,anchor); call(DEADLINE,"p11-utime",os.utime,b"target",ns=(1000000000,1000000000),dir_fd=dir_anchor,follow_symlinks=False); call(DEADLINE,"p11-chown",os.chown,b"target",65534,65534,dir_fd=dir_anchor,follow_symlinks=False)
   opened=b""; unchanged=0
   try:
    noatime=call(DEADLINE,"p11-noatime-open",os.open,b"target",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW|os.O_NOATIME,dir_fd=dir_anchor); owned.append(noatime); opened=b"OK"; need(call(DEADLINE,"p11-noatime-read",os.read,noatime,1)==b"x","p11-read"); close_capture(noatime,DEADLINE,cleanup_failures,"p11-noatime"); owned.remove(noatime); noatime=-1; current=call(DEADLINE,"p11-current-stat",os.stat,b"target",dir_fd=dir_anchor,follow_symlinks=False); unchanged=int(current.st_atime_ns==1000000000); need(cap_fowner==1 and unchanged==1,"p11-noatime")
   except OSError as e: after(DEADLINE,"p11-noatime-error"); need(e.errno==errno.EPERM and cap_fowner==0,"p11-eperm"); opened=b"EPERM"
   held=call(DEADLINE,"p11-pre-fstat",os.fstat,anchor); path=call(DEADLINE,"p11-pre-stat",os.stat,b"target",dir_fd=dir_anchor,follow_symlinks=False); need((held.st_dev,held.st_ino)==created==(path.st_dev,path.st_ino) and held.st_nlink==path.st_nlink==1 and stat.S_ISREG(path.st_mode),"p11-pre-unlink")
   call(DEADLINE,"p11-unlink",os.unlink,b"target",dir_fd=dir_anchor); removed=1; held2=call(DEADLINE,"p11-post-fstat",os.fstat,anchor); need((held2.st_dev,held2.st_ino)==created and held2.st_nlink==0,"p11-held-after"); absent=0
   try: call(DEADLINE,"p11-post-stat",os.stat,b"target",dir_fd=dir_anchor,follow_symlinks=False)
   except FileNotFoundError: after(DEADLINE,"p11-post-enoent"); absent=1
   need(absent==1,"p11-path-after"); row(rows,ID,b"capeff_hex",caphex); row(rows,ID,b"cap_fowner",cap_fowner); row(rows,ID,b"open_result",opened); row(rows,ID,b"atime_unchanged",unchanged); row(rows,ID,b"created_dev",created[0]); row(rows,ID,b"created_ino",created[1]); row(rows,ID,b"cleanup_unlinked",1); row(rows,ID,b"cleanup_identity_observed",1); row(rows,ID,b"atomic_unlink_proof",0); row(rows,ID,b"scope_single_inode",1)
  finally:
   close_capture(noatime,DEADLINE,cleanup_failures,"p11-noatime-final"); owned.remove(noatime) if noatime in owned else None
   if created is not None and not removed:
    try:
     held=call(DEADLINE,"p11-cleanup-fstat",os.fstat,anchor); path=call(DEADLINE,"p11-cleanup-stat",os.stat,b"target",dir_fd=dir_anchor,follow_symlinks=False)
     if (held.st_dev,held.st_ino)==created==(path.st_dev,path.st_ino) and path.st_nlink==1 and stat.S_ISREG(path.st_mode): call(DEADLINE,"p11-cleanup-unlink",os.unlink,b"target",dir_fd=dir_anchor)
    except FileNotFoundError: after(DEADLINE,"p11-cleanup-enoent")
   close_capture(anchor,DEADLINE,cleanup_failures,"p11-anchor"); owned.remove(anchor) if anchor in owned else None; close_capture(dir_anchor,DEADLINE,cleanup_failures,"p11-dir"); owned.remove(dir_anchor) if dir_anchor in owned else None
 elif ID==b"P12":
  need(len(EXTRA)==0,"p12-extra"); env_fd,env_key=bind_tool(ENV_TOOL,ENV_TOOL_BYTES,ENV_TOOL_SHA,DEADLINE,"env-tool"); bash_fd,bash_key=bind_tool(BASH_TOOL,BASH_TOOL_BYTES,BASH_TOOL_SHA,DEADLINE,"bash-tool")
  command=b'exec /usr/bin/env -i LANG=C LC_ALL=C PATH=/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONIOENCODING=UTF-8:strict PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 PYTHONUTF8=1 TZ=UTC /root/miniconda3/bin/python3 -I -S -B -P -X utf8 -c "$1" CHAIN "$2" "$3"'
  argv=(ENV_TOOL,b"-i",BASH_TOOL,b"--noprofile",b"--norc",b"-c",command,b"p27-e001-v4-chain",CHILD_SOURCE,str(DEADLINE).encode("ascii"),SAFE)
  pid,fd,unused_gate=spawn_observed(CHILD_SOURCE,b"CHAIN",DEADLINE,SAFE,argv_override=argv,env={}); status,raw=finish_child(pid,fd,DEADLINE); close_capture(fd,DEADLINE,cleanup_failures,"p12-fd"); owned.remove(fd); cp,cs,cg=child_parse(raw,b"CHAIN",b"terminal",pid,hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii"),SAFE); need(status==0,"p12-status"); recheck_tool(env_fd,ENV_TOOL,ENV_TOOL_BYTES,ENV_TOOL_SHA,env_key,DEADLINE,"terminal-env"); recheck_tool(bash_fd,BASH_TOOL,BASH_TOOL_BYTES,BASH_TOOL_SHA,bash_key,DEADLINE,"terminal-bash")
  environment=b",".join((key+b"="+ENV[key]).hex().encode("ascii") for key in sorted(ENV)); row(rows,ID,b"env_dev",env_key[0]); row(rows,ID,b"env_ino",env_key[1]); row(rows,ID,b"env_sha256",ENV_TOOL_SHA); row(rows,ID,b"bash_dev",bash_key[0]); row(rows,ID,b"bash_ino",bash_key[1]); row(rows,ID,b"bash_sha256",BASH_TOOL_SHA); row(rows,ID,b"child_raw_bytes",len(raw)); row(rows,ID,b"child_raw_sha256",hashlib.sha256(raw).hexdigest()); row(rows,ID,b"child_pid",cp); row(rows,ID,b"child_sid",cs); row(rows,ID,b"child_pgid",cg); row(rows,ID,b"executable_hex",PYTHON.hex()); row(rows,ID,b"environment",environment); row(rows,ID,b"environment_count",10); row(rows,ID,b"underscore_absent",1); row(rows,ID,b"cwd_hex",SAFE.hex()); row(rows,ID,b"real_payload_invoked",0); row(rows,ID,b"raw_status",status)
 elif ID==b"P13":
  need(len(EXTRA)==0,"p13-extra"); dir_anchor=call(DEADLINE,"p13-dir-open",os.open,b".",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW); owned.append(dir_anchor); directory=call(DEADLINE,"p13-dir-fstat",os.fstat,dir_anchor); need(stat.S_ISDIR(directory.st_mode) and stat.S_IMODE(directory.st_mode)==0o700 and directory.st_uid==0 and directory.st_gid==0,"p13-dir")
  anchor=-1; created=None; a_present=0; b_present=0
  try:
   anchor=call(DEADLINE,"p13-create",os.open,b"a",os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600,dir_fd=dir_anchor); owned.append(anchor); created_stat=call(DEADLINE,"p13-created-stat",os.fstat,anchor); created=(created_stat.st_dev,created_stat.st_ino); need(stat.S_ISREG(created_stat.st_mode) and created_stat.st_nlink==1,"p13-created"); need(call(DEADLINE,"p13-write",os.write,anchor,b"P27E001\n")==8,"p13-write-count"); call(DEADLINE,"p13-file-fsync",os.fsync,anchor); a_present=1
   call(DEADLINE,"p13-link",os.link,b"a",b"b",src_dir_fd=dir_anchor,dst_dir_fd=dir_anchor,follow_symlinks=False); b_present=1; held=call(DEADLINE,"p13-link-fstat",os.fstat,anchor); path_a=call(DEADLINE,"p13-a-stat",os.stat,b"a",dir_fd=dir_anchor,follow_symlinks=False); path_b=call(DEADLINE,"p13-b-stat",os.stat,b"b",dir_fd=dir_anchor,follow_symlinks=False); need((held.st_dev,held.st_ino)==created==(path_a.st_dev,path_a.st_ino)==(path_b.st_dev,path_b.st_ino) and held.st_nlink==path_a.st_nlink==path_b.st_nlink==2,"p13-link-identity")
   call(DEADLINE,"p13-a-unlink",os.unlink,b"a",dir_fd=dir_anchor); a_present=0; old_absent=0
   try: call(DEADLINE,"p13-a-after",os.stat,b"a",dir_fd=dir_anchor,follow_symlinks=False)
   except FileNotFoundError: after(DEADLINE,"p13-a-enoent"); old_absent=1
   held=call(DEADLINE,"p13-transfer-fstat",os.fstat,anchor); path_b=call(DEADLINE,"p13-transfer-stat",os.stat,b"b",dir_fd=dir_anchor,follow_symlinks=False); preserved=int((held.st_dev,held.st_ino)==created==(path_b.st_dev,path_b.st_ino) and held.st_nlink==path_b.st_nlink==1); need(old_absent==1 and preserved==1,"p13-transfer"); call(DEADLINE,"p13-dir-fsync",os.fsync,dir_anchor)
   held=call(DEADLINE,"p13-pre-unlink-fstat",os.fstat,anchor); path_b=call(DEADLINE,"p13-pre-unlink-stat",os.stat,b"b",dir_fd=dir_anchor,follow_symlinks=False); need((held.st_dev,held.st_ino)==created==(path_b.st_dev,path_b.st_ino),"p13-pre-unlink"); call(DEADLINE,"p13-b-unlink",os.unlink,b"b",dir_fd=dir_anchor); b_present=0; held=call(DEADLINE,"p13-post-fstat",os.fstat,anchor); need((held.st_dev,held.st_ino)==created and held.st_nlink==0,"p13-held-after"); new_absent=0
   try: call(DEADLINE,"p13-b-after",os.stat,b"b",dir_fd=dir_anchor,follow_symlinks=False)
   except FileNotFoundError: after(DEADLINE,"p13-b-enoent"); new_absent=1
   need(new_absent==1,"p13-absent"); row(rows,ID,b"file_fsync_returned",1); row(rows,ID,b"hardlink_noreplace_returned",1); row(rows,ID,b"old_absent",old_absent); row(rows,ID,b"inode_preserved",preserved); row(rows,ID,b"dir_fsync_returned",1); row(rows,ID,b"post_unlink_absent",new_absent); row(rows,ID,b"created_dev",created[0]); row(rows,ID,b"created_ino",created[1]); row(rows,ID,b"cleanup_unlinked",1); row(rows,ID,b"cleanup_identity_observed",1); row(rows,ID,b"atomic_unlink_proof",0); row(rows,ID,b"durability_proof",0); row(rows,ID,b"rename_atomicity_proof",0); row(rows,ID,b"immutability_proof",0)
  finally:
   if created is not None:
    for fixed,present in ((b"a",a_present),(b"b",b_present)):
     if present:
      try:
       held=call(DEADLINE,"p13-cleanup-fstat",os.fstat,anchor); path=call(DEADLINE,"p13-cleanup-stat",os.stat,fixed,dir_fd=dir_anchor,follow_symlinks=False)
       if (held.st_dev,held.st_ino)==created==(path.st_dev,path.st_ino) and stat.S_ISREG(path.st_mode): call(DEADLINE,"p13-cleanup-unlink",os.unlink,fixed,dir_fd=dir_anchor)
      except FileNotFoundError: after(DEADLINE,"p13-cleanup-enoent")
   close_capture(anchor,DEADLINE,cleanup_failures,"p13-anchor"); owned.remove(anchor) if anchor in owned else None; close_capture(dir_anchor,DEADLINE,cleanup_failures,"p13-dir"); owned.remove(dir_anchor) if dir_anchor in owned else None
 else: raise Fail("probe-unreachable")
 need(ABORT==0,"marker-abort"); need(all(slots[pid][0]==0 for pid in pids) and spawned==reaped==len(pids)==len(statuses),"child-census"); recheck_image(resolved_fd,self_fd,image_key,link_key,DEADLINE); result=b"READY"
except BaseException as e:
 if primary==b"none":
  if isinstance(e,Fail): primary=os.fsencode(str(e)).replace(b"_",b"-")
  elif isinstance(e,OSError): primary=("oserror-%d"%(e.errno if e.errno is not None else -1)).encode("ascii")
  else: primary=("exception-"+type(e).__name__).encode("ascii","strict").lower()
finally:
 try: cleanup_live(DEADLINE,cleanup_failures)
 except BaseException as e: cleanup_failures.append(("children:"+type(e).__name__).encode("ascii","strict").lower())
 for fd in tuple(owned):
  close_capture(fd,DEADLINE,cleanup_failures,"owned-fd")
  if fd in owned: owned.remove(fd)
 for fd,label in ((libc_fd,"libc"),(env_fd,"env"),(bash_fd,"bash"),(resolved_fd,"resolved"),(self_fd,"self-image")): close_capture(fd,DEADLINE,cleanup_failures,label)

probe_finish=mono(); elapsed=probe_finish-probe_start if probe_finish>=probe_start else -1; cleanup_token=b"none" if not cleanup_failures else b"present"
prepass=result==b"READY" and primary==b"none" and cleanup_token==b"none" and elapsed>=0 and elapsed<=TOTAL_NS and probe_finish<=DEADLINE and all(slots[pid][0]==0 for pid in pids) and spawned==reaped==len(pids)==len(statuses)
if prepass and TELE_FD>=0:
 try: call(DEADLINE,"telemetry-final-close",os.close,TELE_FD); TELE_FD=-1
 except BaseException as e: cleanup_failures.append(("telemetry:"+type(e).__name__).encode("ascii","strict").lower()); cleanup_token=b"present"; prepass=False
if prepass:
 if p07_pending: row(rows,ID,b"terminal_elapsed_ns",elapsed)
 row(rows,ID,b"marker_image_dev",image_key[0]); row(rows,ID,b"marker_image_ino",image_key[1]); row(rows,ID,b"marker_image_sha256",PY_SHA); row(rows,ID,b"children_spawned",spawned); row(rows,ID,b"children_reaped",reaped); row(rows,ID,b"child_pids",b",".join(str(pid).encode("ascii") for pid in pids) if pids else b"-"); row(rows,ID,b"raw_statuses",b",".join(str(status).encode("ascii") for status in statuses) if statuses else b"-"); row(rows,ID,b"probe_start_ns",probe_start); row(rows,ID,b"probe_finish_ns",probe_finish); row(rows,ID,b"probe_elapsed_ns",elapsed); row(rows,ID,b"probe_bound_ns",TOTAL_NS); row(rows,ID,b"primary_failure",b"none"); row(rows,ID,b"cleanup_failure",b"none"); row(rows,ID,b"result",b"PASS")
 output=b"P27E001V4|marker=report|schema=4|probe="+ID+b"\n"+b"\n".join(rows)+b"\n"; terminal=b"P27E001V4|probe="+ID+b"|result=PASS"; lines=output.split(b"\n"); need(lines[-1]==b"" and lines[-2]==terminal and sum(1 for line in lines[:-1] if line==terminal)==1 and len(output)<=CAP,"marker-output-frame"); write_exact(1,output,DEADLINE)
else:
 if TELE_FD>=0:
  failure=b"P27E001V4|marker=failure|probe="+ID+b"|primary_failure="+primary+b"|cleanup_failure="+cleanup_token+b"|children_spawned="+str(spawned).encode("ascii")+b"|children_reaped="+str(reaped).encode("ascii")+b"|child_pids="+(b",".join(str(pid).encode("ascii") for pid in pids) if pids else b"-")+b"|raw_statuses="+(b",".join(str(status).encode("ascii") for status in statuses) if statuses else b"-")+b"\n"
  try: write_exact(TELE_FD,failure,DEADLINE); call(DEADLINE,"telemetry-failure-close",os.close,TELE_FD)
  except BaseException: pass
 raise SystemExit(90)
UNIFIED MARKER V4 SOURCE END
```

The child stub is frozen inside the marker record. Each child validates its
argv, exact flags, environment, cwd, actual source hash, symlink, held
resolved interpreter, `/proc/self/exe`, device/inode/type/mode/owner/size,
and two content hashes before its only accepted line. P00 adds only a newline,
one comment introducer, and inert `x` bytes after that complete stub. All
nested image and procfs work is contained first by the marker, then by the
owned launcher, then by the outer total deadline.

## 7. Closed process, FD, and failure topology

The outer starts with exactly FDs 0, 1, and 2, constructs four pipe nodes,
maps an already writer-closed read end to launcher stdin, and maps distinct
stdout, stderr, and telemetry nodes to 1, 2, and 3. Its file-actions close
every enumerated source FD at or above 4. The returned direct launcher is the
one session and process-group leader. No child can create another session or
group.

The launcher constructs exactly four new marker nodes: stdout, stderr,
incremental child telemetry, and the one-byte gate. It maps them to marker
FDs 1 through 4, retains the inherited EOF stdin at 0, excludes destination
FD 4 from its close list, and closes every enumerated source FD at or above
5. The marker verifies five pairwise-distinct FIFO nodes before gate
consumption. Nested children inherit no launcher or marker identity FD.
Ordinary children explicitly close telemetry FD 3; gated children replace
3 with their one-byte gate.

The finite successful lifecycle is:

```text
OUTER_VALIDATE_MEMORY_AND_FDS
-> SPAWN_OWNED_SESSION_LEADER
-> LAUNCHER_BIND_SELF_AND_OUTER_IMAGES
-> LAUNCHER_BIND_LEDGER_AND_CONTROL_FINAL_LINES
-> LAUNCHER_CREATE_AND_BIND_SAFE_DIRECTORY
-> SPAWN_SELF_BINDING_MARKER
-> MARKER_GATE_AND_SELF_BIND
-> RUN_ONE_CLOSED_PROBE
-> ATOMIC_NESTED_REAPS_AND_RAW_TELEMETRY
-> MARKER_FINAL_ELAPSED_AND_EXACT_REPORT
-> ATOMIC_MARKER_REAP
-> TERMINAL_SOURCE_IMAGE_FILESYSTEM_RECHECKS
-> HELD_DIRFD_RMDIR_LINK_2_TO_0_AND_PATH_ENOENT
-> EXACT_WORKER_FINAL_LINE
-> ATOMIC_LEADER_REAP_AND_GROUP_ABSENCE
-> EXACT_OUTER_REPORT
```

If a launcher failure occurs after marker spawn, the launcher emits one
cleanup-request record and enters failure-only quarantine. It neither exits
nor signals a descendant. The outer still owns an unreaped group leader and
reaches its earlier work deadline, sends TERM once, waits nonblocking, sends
KILL once if necessary, physically reaps the leader, and performs only a
nonsignaling group-zero observation. The quarantine's final `signal.pause`
is explicitly a non-PASS fallback under loss of the outer-owner premise; it
cannot produce a worker terminal or total-cleanup PASS. Thus a marker failure
cannot let the leader disappear before whole-group disposition.

## 8. Immutable telemetry, raw evidence, and physical reap

Outer, launcher, marker, and nested-child state initialize before their first
argument, environment, flag, identity, or source validation. Each has a
write-once primary-failure field. Cleanup failures are accumulated in a
separate object and only demote a candidate result. No cleanup exception
replaces primary causality.

Every wait helper handles one exact owned PID. On `waitpid` returning that
PID, its first state mutation is one `slots[pid]=(not_live, raw_status, ...)`
assignment. Only after that assignment may a deadline check, telemetry write,
drain, elapsed calculation, parser, or cleanup operation occur. ECHILD is an
error, never reap evidence. Cleanup reads the same slots and never re-waits a
physically reaped PID.

Marker telemetry is incremental and exact-line framed. Every successful
spawn emits returned PID and mode. Every nonempty nested stdout chunk is at
most 512 bytes and emits PID, canonical sequence, byte count, SHA-256, and
full lowercase hex. Every physical reap emits the same PID, mode, and raw
wait status after the ownership transition. The launcher forwards each raw
byte while retaining an identical copy. On PASS the outer requires one exact
launcher-ownership line followed by sequential child frames: one spawn, zero
or more ordered raw-chunk records on either side of one reap, then the next
spawn. It enforces exact field count/order/spelling, canonical PID/status and
sequence, mode agreement, raw byte/hash/hex equality, no pending child, and
exact counts. On failure, the outer report preserves stdout, stderr, and
telemetry as exact byte count, SHA-256, and lowercase hex. A missing status
stays visibly missing because no reap record exists.

## 9. Exact parsing and canonical encodings

No parser trims, strips, normalizes, decodes with replacement, or uses
`splitlines`. All accepted streams require terminal LF, retain the final
empty split element, forbid CR and NUL, and require ASCII. Record parsers
require exact part count, exact order, exact key spelling, one equals sign
per field, and no surplus field. Decimal values are nonempty ASCII digits and
must round-trip through `str(int(value))`, so signs, whitespace, and leading
zeros fail. SHA-256 and authorization values are exactly 64 lowercase hex
characters. Variable-length hex must be even, lowercase, and byte-round-trip
identical. CapEff is exactly 16 lowercase hex characters.

The ledger/control terminal rule uses LF splitting and exact line equality:
the final element must be empty, the preceding line must equal the supplied
terminal, and exactly one complete pre-final line may equal it. A prose field
such as `terminal_marker=<same bytes>` is not equal to that standalone line
and is not counted. Marker PASS and worker terminal records use the same
exact-final-line principle.

## 10. Complete probe catalog and terminal elapsed rule

All probes require common `probe_start_ns`, `probe_finish_ns`,
`probe_elapsed_ns`, and `probe_bound_ns`. The finish time is taken after the
branch, image recheck, owned-child cleanup, and descriptor cleanup. PASS
requires `0 <= finish-start == elapsed <= bound <= TOTAL_NS` and a fresh
post-completion deadline check. P07 additionally places that same elapsed
value in its branch-specific `terminal_elapsed_ns` field.

- P00 constructs exactly 251414 ASCII source bytes from the fully
  self-binding child stub plus inert comment padding. Exact success and zero
  raw status, or exact E2BIG before a PID exists, is observational PASS;
  only success sets transport feasibility.
- P01D self-binds Python, binds one executable libc mapping to the held
  no-follow object by device/inode, and reports discovery only.
- P01C consumes exactly thirteen canonically encoded discovery fields,
  rebinds every one, spawns one self-binding INFO child, retains its exact raw
  line/hash/PID/SID/PGID/status, and rechecks held Python and libc objects.
- P02 closes held image and telemetry FDs after image recheck, proves exact
  FDs 0/1/2, ten-key environment, cwd, flags, FIFO identities, and limits,
  then freshly rebinds its marker image before terminal acceptance.
- P03 similarly closes image and telemetry FDs, lowers only soft NOFILE to
  64, observes exact EMFILE, closes all returned FDs, proves only 0/1/2, and
  freshly rebinds its image.
- P04 normalizes every catchable valid signal, proves the empty mask and all
  defaults, and records the exact sorted list and hash.
- P05 uses a self-binding gated EXIT23 child for WNOHANG zero and the sole
  timer-bounded intentional blocking wait/EINTR observation. Its physical
  reap path is atomic. A second self-binding child reports ready before
  self-TERM; both PIDs and raw statuses are retained. ECHILD is observed only
  after the first recorded reap.
- P06 takes exactly 4096 monotonic samples, requires nondecrease and progress,
  signed-63 headroom, declared resolution, and bounded elapsed time.
- P07 checks CLOEXEC, nonblocking flags, EAGAIN, readiness, one byte, retained
  writer behavior, HUP, EOF, and the common terminal elapsed after every
  successful read, write, and poll post-check.
- P08 uses a self-binding gated child, binds its reported topology to the
  returned live PID, observes signal zero only while owned, releases it,
  atomically reaps it, and makes only a nonsignaling ESRCH observation after.
- P09 uses the same bound ready proof, WNOHANG immediately before its sole
  normal-body delivered SIGKILL, atomic physical reap, exact signal status,
  and a terminal interval no greater than 1000000000 ns.
- P10 serially spawns and atomically reaps exactly sixteen self-binding INFO
  children, one live at a time, retaining every PID, group, and raw status.
- P11 reads exactly one canonical CapEff line and confines O_NOATIME, held
  inode, fsync, owner change, unlink, link-zero, and ENOENT observations to
  fixed `target` beneath the fresh directory. It claims no atomic unlink.
- P12 binds held `/usr/bin/env` and `/usr/bin/bash` objects, executes the
  exact env-i/bash/second-env-i chain, and accepts only the same self-binding
  CHAIN child with exact flags, ten-key environment, underscore absence, cwd,
  executable, raw line, PID topology, and status. No real payload is invoked.
- P13 confines fixed `a` and `b` to the fresh directory, holds one inode,
  fsyncs it, uses exact-dirfd hard-link no-replace, unlinks `a`, fsyncs the
  directory, verifies `b`, unlinks it, and observes held link zero and two
  ENOENT states. It claims no crash durability, rename atomicity, pathname
  immutability, or atomic conditional unlink.

P00/P01C/P05/P08/P09/P12 have at most one live nested child; P05 has two
total; P10 has sixteen total and one live; all other probes have zero. P11
and P13 alone write filesystem objects. P12 alone uses a shell. P09 alone
delivers a normal-body SIGKILL. No branch calls setsid or setpgroup, scans
processes broadly, uses a pre-existing PID, or invokes production V8.

## 11. Exact paths, proc surfaces, and API closure

The exact non-generated absolute paths in the source bundle are Python, its
resolved object, the ledger, this V4 control, `/`, `/tmp`,
`/proc/self/exe`, `/proc/self/maps`, `/proc/self/status`,
`/proc/self/mountinfo`, `/usr/bin/env`, and `/usr/bin/bash`. The only dynamic
absolute proc paths are `/proc/<exact still-live outer PID>/exe` and
`/proc/<exact returned marker PID>/stat`. The only generated filesystem path
is `/tmp/p27-e001-host-v4-<AUTH_ID>`. Probe names are fixed `target`, `a`, and
`b`. There is no repository discovery or build/evidence/recovery-root path.

OUTER CONTROLLER V4 imports exactly `errno`, `fcntl`, `hashlib`, `os`,
`resource`, `select`, `signal`, `sys`, and `time`. Its operating surfaces are
`fcntl.fcntl`; `hashlib.sha256`; `os.close`, `fsencode`, `getpid`, `killpg`,
`pipe2`, `posix_spawn`, `read`, `waitpid`, and `write`; POSIX spawn
DUP2/CLOSE; `resource.getrlimit`; `select.poll`; `signal.valid_signals`; and
`time.monotonic_ns`. It has no source-file, pathname, procfs, image, mount,
inventory, mkdir, unlink, or rmdir operation.

OWNED LAUNCHER V4 imports exactly `errno`, `fcntl`, `hashlib`, `os`,
`resource`, `select`, `signal`, `stat`, `sys`, and `time`. Its operating
surfaces are the exact calls lexically present in its source: `fcntl.fcntl`;
`hashlib.sha256`; `os.chdir`, `close`, `fchmod`, `fstat`, `fsencode`,
`getcwdb`, `getpgrp`, `getpid`, `getppid`, `getsid`, `listdir`, `lseek`,
`lstat`, `mkdir`, `open`, `pipe2`, `posix_spawn`, `read`, `readlink`, `rmdir`,
`stat`, `umask`, `waitpid`, and `write`; POSIX spawn DUP2/CLOSE;
`resource.getrlimit` and `setrlimit`; `select.poll`; `signal.getsignal`,
`pause`, `pthread_sigmask`, `signal`, and `valid_signals`; `stat.S_ISDIR`,
`S_ISLNK`, `S_ISREG`, and `S_IMODE`; and `time.monotonic_ns`. It has no
delivered-signal call. Failure-only `signal.pause` cannot yield PASS and is
owned by the outer deadline state machine.

UNIFIED MARKER V4 imports the same ten modules as the launcher. Its operating
surfaces are `fcntl.fcntl`; `hashlib.sha256`; `os.chown`, `close`, `confstr`,
`dup`, `fsencode`, `fsync`, `fstat`, `getcwdb`, `getpgid`, `getpgrp`,
`getpid`, `getsid`, `kill`, `link`, `lseek`, `lstat`, `makedev`, `open`,
`pipe2`, `posix_spawn`, `read`, `readlink`, `stat`, `sysconf`, `unlink`,
`utime`, `waitpid`, and `write`; POSIX spawn DUP2/CLOSE and wait-status
macros; `resource.getrlimit` and `setrlimit`; `select.poll`;
`signal.getsignal`, `pthread_sigmask`, `setitimer`, `signal`, and
`valid_signals`; `stat.S_ISDIR`, `S_ISFIFO`, `S_ISLNK`, `S_ISREG`, and
`S_IMODE`; and `time.clock_getres`, `get_clock_info`, and `monotonic_ns`.
The nested child imports exactly `errno`, `hashlib`, `os`, `signal`, `stat`,
`sys`, and `time`, and uses only its lexically present image, clock, signal,
cwd, topology, gate, write, close, and self-TERM calls.

Across the bundle there is no dynamic import, eval, exec builtin, compile
builtin, ctypes, prctl, tempfile, pathlib, glob, shutil, subprocess,
multiprocessing, socket, network, package discovery, PTY, trace, walk, mount,
namespace, chroot, credential change, recursive deletion, wildcard, PATH
lookup, or shell other than exact P12.

## 12. Exact V3-to-V4 correction closure

V4 closes the E0337 findings in ten source-level classes while retaining the
prior exact environment, flags, limits, signal defaults, no-bytecode,
second-env, no-retry, held-image, raw framing, private directory, and
bounded-observation controls:

1. final terminal validation is exact EOF-line equality and standalone-line
   count, never substring count;
2. rmdir post-state freezes stable held device/inode/type/mode/owner/group,
   exact link 2-to-0, stable parent, and exact pathname ENOENT;
3. every potentially blocking source/image/procfs/filesystem/cleanup phase is
   inside the one launcher helper owned by the outer total deadline, or a
   nested helper transitively owned by it; no intrinsic syscall-time claim is
   made;
4. launcher binds itself and outer, marker binds itself on every branch, and
   every nested Python runs the self-binding child stub; P00 pads that stub
   rather than an inert all-comment program;
5. structured primary and cleanup telemetry begins before validation in all
   layers and preserves exact raw streams, returned PIDs, and observed raw
   statuses on every failure;
6. each physical reap performs the one ownership/status assignment before
   deadline checks, drains, elapsed work, parsing, or telemetry, and cleanup
   consumes that same ledger;
7. ownership, child, marker, worker, and terminal parsers freeze exact field
   count/order/spelling plus canonical decimal and lowercase hex grammar;
8. every wait/read/write/poll helper checks the deadline after completion,
   and every probe, including P07, records terminal nonnegative elapsed time
   within one authorized bound;
9. stdin EOF, destination-FD exclusions, inherited-FD closure, one session,
   and failure quarantine keep the exact leader unreaped until whole-group
   failure disposition;
10. incremental nested PID/status/raw-chunk telemetry and outer raw
    count/hash/hex retain evidence without inventing zero status, timeout,
    cleanup success, or causality.

## 13. Facts deliberately not proved

Even fifteen PASS observations do not prove future host state, production cwd
behavior, V8 execution, libc internal clone strategy, universal PID/PGID
nonreuse, scheduler fairness, signal latency, absence of uninterruptible
sleep, power-loss ordering, crash durability, storage persistence, rename
atomicity, pathname immutability, inode nonreuse, mount stability, or behavior
for another executable, source, argv, environment, filesystem, authorization,
process, or time. P00 E2BIG is observational PASS but a production transport
blocker. Failure-only quarantine explicitly proves no total-cleanup PASS.

No probe, child, launcher, outer source, actor, fixture, payload, validator,
binder, V8 source, build, evidence, recovery root, release, PDF, Paper28, or
publication action is authorized. No source block in this file was imported,
parsed, compiled, evaluated, or executed during authoring.

## 14. Frozen source identities and census

For each top-level record, locate its unique exact standalone BEGIN and END
lines, exclude both delimiter lines, and take every intervening byte including
the LF immediately before END. For the nested child, locate the unique exact
`CHILD_SOURCE=b'''\` and following standalone `'''` lines, exclude them, and
take every intervening byte including its final LF. Do not trim, dedent,
decode/re-encode, interpolate, normalize, import, parse, compile, evaluate, or
execute any record.

```text
OUTER_CONTROLLER_V4 bytes=21710 LF=277 sha256=9929fc3260e7303612adae55376f972b39e2bd50c1441b254803f6b99cad4ee0 final_byte=0a
OWNED_LAUNCHER_V4 bytes=42975 LF=457 sha256=8dfca2f38c2dad0823440a9b8c659f4ee5117b5ffaa1b9948e6876768dd79015 final_byte=0a
UNIFIED_MARKER_V4 bytes=57788 LF=576 sha256=1ded307944a79d51f60d00a487470307459ae562a380ffd38f114fb87e537443 final_byte=0a
NESTED_CHILD_V4 bytes=4701 LF=58 sha256=51b2f6514d5562cee788db2dcac77ef6a8bd79cbc550d4e8705907722f365710 final_byte=0a
```

Source census: 3 top-level frozen records; 1 nested frozen child record; 3
unique top-level BEGIN lines; 3 unique top-level END lines; 15 accepted probe
IDs; 15 closed probe branches; 5 nested child modes; 10 correction classes;
4 outer pipe nodes; 4 launcher-to-marker pipe nodes; 1 owned session/group;
0 launcher delivered-signal calls; 2 outer delivered group-signal call sites,
both only while the exact leader is unreaped; 2 marker cleanup exact-PID
delivered-signal call sites; 1 marker normal-body exact-PID SIGKILL call site;
1 nested self-TERM site; 2 filesystem-writing probes; 1 shell probe; 1
libc discovery/confirmation pair; 0 source executions; 0 probe attempts; 0
build/evidence/recovery-root accesses.

BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V4_AUTHOR_STOP
