# E001 Supervisor Host-Probe Recovery Control V3

Status: INERT PLAN AND INERT ASCII SOURCE TEXT ONLY. NO EXECUTION AUTHORITY.

## 1. Authority, frozen failures, and zero activity

This is the sole host-probe V3 path authorized by E0335. The failed V1 and
V2 controls remain immutable historical bytes. This file does not amend,
replace, reinterpret, run, import, parse, compile, evaluate, or extract any
source from either predecessor or from the frozen V8 control. Authoring this
file creates no cwd, file, pipe, process, fixture, report, evidence, or result.
It accesses no build, evidence, recovery root, payload, validator, binder, or
marker program. Its probe execution count is zero.

The exact E0335 authoring anchor is:

```text
path=/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md
dev=2431
ino=12439253869
mode=0644
nlink=1
uid=0
gid=0
bytes=1902081
LF=21036
sha256=6353bf3a87f4e9fd21f14e2fe390a24f20ed5b4ccf9d20eaf2f2708148b55121
terminal=BATCH07_P27_PROBE_RECOVERY_E001_ACTOR_DERIVATION_HOST_V2_STATIC_REVIEW_FAILURE_RECORDED_AND_V3_CONTROLS_AUTHORIZED
```

The frozen failed V2 identity is:

```text
path=papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V2.md
dev=2431
ino=5929957152
mode=0644
nlink=1
uid=0
gid=0
bytes=71264
LF=1747
sha256=3d355ed6f91163116c4df3ebfa63a77967bf464e3a5da684bf77131d5405543f
terminal=BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V2_AUTHOR_STOP
```

No later action exists unless a new ledger event binds this whole V3 file,
the exact byte identities of all three source records below, one exact probe
ID, one immutable authorization ID, and one attempt. There is no retry,
fallback, repair, parser widening, alternate executable, or second sample.
PASS is only a bounded observation and grants no actor, fixture, binder,
validator, payload, build, evidence, root, release, or publication action.

## 2. Frozen V8 and host premises

The only production-source premise remains the frozen V8 control:

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

No source block below contains or opens those V8 bytes. P00 uses only a
same-length synthetic ASCII comment. The exact production Python vectors are
retained as premises, not run here:

```text
watchdog=/root/miniconda3/bin/python3 -I -S -B -P -X utf8 -c SOURCE watchdog
supervisor=/root/miniconda3/bin/python3 -S -B -P -c SOURCE supervisor
recovery=/root/miniconda3/bin/python3 -S -B -P -c SOURCE recovery-binder
```

The outer controller, launcher, unified marker dispatcher, and every nested
synthetic Python use only the watchdog profile. They do not claim production
flag equivalence. The executable spelling is fixed. Its symlink must have
literal target `python3.12`; the resolved regular object and `/proc/self/exe`
must be the same held device/inode and must independently hash to:

```text
resolved_path=/root/miniconda3/bin/python3.12
resolved_bytes=30626264
resolved_sha256=9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101
```

P01D and P01C additionally bind the exact executable mapping of libc by the
device and inode encoded in `/proc/self/maps`, then compare those numbers to
an O_NOFOLLOW-opened regular object before hashing that held object. A current
pathname hash without mapped-object equality is never accepted.

The exact ten-key environment, in bytewise-key and insertion order, is:

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

No HOME, PWD, SHLVL, underscore, proxy, credential, loader, startup, user,
repository, or inherited entry may reach a Python child. P12 uses a second
`/usr/bin/env -i`; it does not rely on unsetting underscore.

## 3. Exact three-layer design and absolute limits

V3 freezes exactly three ASCII source records: OUTER CONTROLLER V3, COMMON
LAUNCHER V3, and UNIFIED MARKER V3. A later authorization supplies the two
inner sources literally as NUL-free argv items and supplies their already
bound SHA-256 values. Each running layer hashes its actual `sys.orig_argv[8]`
`-c` item. No layer reads source from a file, environment, stdin, repository,
or build path.

The outer controller is the only creator of the disposable cwd and the only
process allowed to remove it. It creates exactly one mode-0700 directory
directly beneath a held, component-verified `/tmp` dirfd. The name is
`p27-e001-host-v3-` plus the exact 64-lowercase-hex authorization ID. It
verifies empty inventory, same-filesystem identity, absence from mount-point
records, and lexical exclusion from every protected namespace before spawn,
before release, and at terminal cleanup. Its held dirfd and parent dirfd stay
open through removal. The residual stat/rmdir interval is disclosed as a
race-bounded observation, never an atomic exact-inode deletion proof. Any
interference, unexpected entry, identity change, or cleanup uncertainty is
FAIL and retains the directory for explicit disposition; there is no broad,
recursive, or automatic cleanup.

There is one owned session and process group. Its leader is the direct
launcher returned by the outer `posix_spawn(setsid=True)`. The marker and all
nested children inherit that group and may not call setsid or setpgroup. Every
delivered group signal is preceded by WNOHANG proof that the exact direct
leader is unreaped and by an exact `/proc/PID/stat` start-time, parent, group,
and session match. An unreaped direct child cannot have its PID reused. Once
the outer controller reaps the leader, it delivers no PID or group signal.
Post-reap signal-zero is observation only; any extant or reused numeric group
is a non-signaling FAIL. No post-reap observation can reopen signaling.

Every poll, drain, wait, cleanup phase, source read, hash read, and identity
read has a fixed byte, iteration, and monotonic deadline bound. All ordinary
waits use WNOHANG. P05's sole blocking wait is bounded by an armed timer whose
handler raises `InterruptedError`, and it is also enclosed by marker,
launcher, and outer deadlines. `ChildProcessError` is always failure evidence;
it is never converted to a zero status or a reap success.

## 4. Exact outer-controller source

The future invocation is the exact watchdog flag prefix followed by this
source and these argv items in order:

```text
PROBE AUTH_ID LAUNCHER_SOURCE LAUNCHER_SHA256 MARKER_SOURCE MARKER_SHA256
DEADLINE_NS LEDGER_BYTES LEDGER_LF LEDGER_SHA256 LEDGER_TERMINAL
CONTROL_BYTES CONTROL_LF CONTROL_SHA256 CONTROL_TERMINAL [PROBE_ARGS...]
```

`DEADLINE_NS` is a decimal interval from 1000000000 through 10000000000.
Ledger and control files are the only repository paths the future outer
source may open, read-only and O_NOFOLLOW. Those exact narrow reads are for
opening and terminal identity binding only; no directory discovery occurs.

```text
OUTER CONTROLLER V3 SOURCE BEGIN
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
CONTROL=b"/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity/notes/E001_SUPERVISOR_HOST_PROBE_RECOVERY_V3.md"
PY_BYTES=30626264
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
RAW_CAP=262144
TELE_CAP=32768
HARD_NOFILE=1048576

class Fail(Exception): pass

def need(v,code):
 if not v: raise Fail(code)

def checked(now,delta):
 need(type(now) is int and type(delta) is int and now>=0 and delta>0,"clock-input")
 need(now<=((1<<63)-1)-delta,"clock-headroom")
 return now+delta

def now():
 v=time.monotonic_ns(); need(type(v) is int and v>=0,"clock-negative"); return v

def elapsed(a,b,bound):
 need(type(a) is int and type(b) is int and 0<=a<=b,"elapsed-negative")
 v=b-a; need(v<=bound,"elapsed-bound"); return v

def sigdefs():
 return tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))

SIGDEFS=sigdefs()

def set_nonblock(fd):
 v=fcntl.fcntl(fd,fcntl.F_GETFL); fcntl.fcntl(fd,fcntl.F_SETFL,v|os.O_NONBLOCK)

def close_if(fd):
 if fd>=0:
  try: os.close(fd)
  except OSError: pass

def read_held(fd,size):
 need(type(size) is int and 0<=size<=400000000,"held-size")
 os.lseek(fd,0,os.SEEK_SET); parts=[]; total=0
 for unused in range((size+1048575)//1048576+1):
  try: x=os.read(fd,min(1048576,size-total+1))
  except InterruptedError: continue
  if not x: break
  parts.append(x); total+=len(x); need(total<=size,"held-growth")
 raw=b"".join(parts); need(len(raw)==size,"held-short"); return raw

def regular_open(path,size,lf,sha,terminal):
 fd=os.open(path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 a=os.fstat(fd)
 need(stat.S_ISREG(a.st_mode) and stat.S_IMODE(a.st_mode)==0o644 and a.st_nlink==1 and a.st_uid==0 and a.st_gid==0 and a.st_size==size,"control-stat")
 raw=read_held(fd,size); digest=hashlib.sha256(raw).hexdigest().encode("ascii")
 need(raw.count(b"\n")==lf and digest==sha,"control-content")
 term=terminal+b"\n"; need(raw.endswith(term) and raw.count(term)==1,"control-terminal")
 z=os.fstat(fd); p=os.stat(path,follow_symlinks=False)
 key=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(key(a)==key(z)==key(p),"control-replaced")
 return fd,key(a),digest

def regular_recheck(fd,path,key,size,lf,sha,terminal):
 a=os.fstat(fd); p=os.stat(path,follow_symlinks=False)
 got=(a.st_dev,a.st_ino,a.st_mode,a.st_nlink,a.st_uid,a.st_gid,a.st_size)
 q=(p.st_dev,p.st_ino,p.st_mode,p.st_nlink,p.st_uid,p.st_gid,p.st_size)
 need(got==key==q,"terminal-control-stat")
 raw=read_held(fd,size)
 need(raw.count(b"\n")==lf and hashlib.sha256(raw).hexdigest().encode("ascii")==sha,"terminal-control-hash")
 need(raw.endswith(terminal+b"\n") and raw.count(terminal+b"\n")==1,"terminal-control-line")

def hash_regular_fd(fd,size):
 raw=read_held(fd,size); return hashlib.sha256(raw).hexdigest().encode("ascii")

def bind_python():
 link=os.lstat(PYTHON)
 need(stat.S_ISLNK(link.st_mode) and stat.S_IMODE(link.st_mode)==0o777 and link.st_nlink==1 and link.st_uid==0 and link.st_gid==0 and link.st_size==10,"python-link-stat")
 need(os.readlink(PYTHON)==b"python3.12","python-link-target")
 pfd=os.open(PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 sfd=os.open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC)
 a=os.fstat(pfd); b=os.fstat(sfd)
 key=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(key(a)==key(b) and stat.S_ISREG(a.st_mode) and stat.S_IMODE(a.st_mode)==0o755 and a.st_nlink==1 and a.st_uid==0 and a.st_gid==0 and a.st_size==PY_BYTES,"python-image-stat")
 need(hash_regular_fd(pfd,PY_BYTES)==PY_SHA and hash_regular_fd(sfd,PY_BYTES)==PY_SHA,"python-image-hash")
 return pfd,sfd,key(a),(link.st_dev,link.st_ino,link.st_mode,link.st_nlink,link.st_uid,link.st_gid,link.st_size)

def recheck_python(pfd,sfd,key,lkey):
 a=os.fstat(pfd); b=os.fstat(sfd); p=os.stat(PYRES,follow_symlinks=False); l=os.lstat(PYTHON)
 k=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(k(a)==k(b)==k(p)==key and k(l)==lkey and os.readlink(PYTHON)==b"python3.12","terminal-python-stat")
 need(hash_regular_fd(pfd,PY_BYTES)==PY_SHA and hash_regular_fd(sfd,PY_BYTES)==PY_SHA,"terminal-python-hash")

def fd_census(limit):
 got=[]
 for fd in range(limit):
  try: fcntl.fcntl(fd,fcntl.F_GETFD)
  except OSError as e:
   if e.errno==errno.EBADF: continue
   raise
  got.append(fd)
 return tuple(got)

def component_open():
 rfd=os.open(b"/",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW)
 tfd=os.open(b"/tmp",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW)
 r=os.fstat(rfd); rp=os.stat(b"/",follow_symlinks=False)
 t=os.fstat(tfd); tp=os.stat(b"tmp",dir_fd=rfd,follow_symlinks=False)
 key=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(key(r)==key(rp) and stat.S_ISDIR(r.st_mode) and r.st_uid==0 and r.st_gid==0,"root-component")
 need(key(t)==key(tp) and stat.S_ISDIR(t.st_mode) and t.st_uid==0 and t.st_gid==0 and stat.S_IMODE(t.st_mode)&0o1000,"tmp-component")
 return rfd,tfd,key(r),key(t)

def mount_clear(safe):
 fd=os.open(b"/proc/self/mountinfo",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:
  chunks=[]; total=0
  for unused in range(257):
   try: x=os.read(fd,4096)
   except InterruptedError: continue
   if not x: break
   chunks.append(x); total+=len(x); need(total<=1048576,"mountinfo-cap")
  else: raise Fail("mountinfo-iterations")
 finally: os.close(fd)
 raw=b"".join(chunks); need(raw.endswith(b"\n") and b"\x00" not in raw,"mountinfo-frame")
 for line in raw.split(b"\n")[:-1]:
  p=line.split(b" "); need(len(p)>=10 and b" - " in line,"mountinfo-line")
  need(p[4]!=safe,"safe-mountpoint")

def safe_recheck(tfd,name,dfd,dkey,safe,empty):
 a=os.fstat(dfd); p=os.stat(name,dir_fd=tfd,follow_symlinks=False)
 k=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(k(a)==k(p)==dkey and stat.S_ISDIR(a.st_mode) and stat.S_IMODE(a.st_mode)==0o700 and a.st_uid==0 and a.st_gid==0,"safe-identity")
 names=os.listdir(dfd); need(type(names) is list,"safe-list")
 if empty: need(names==[],"safe-not-empty")
 mount_clear(safe); return tuple(sorted(os.fsencode(x) for x in names))

def proc_identity(pid):
 path=("/proc/%d/stat"%pid).encode("ascii")
 fd=os.open(path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:
  raw=b""
  for unused in range(8):
   try: x=os.read(fd,512)
   except InterruptedError: continue
   if not x: break
   raw+=x; need(len(raw)<=4096,"proc-stat-cap")
 finally: os.close(fd)
 need(raw.endswith(b"\n") and raw.count(b"\n")==1,"proc-stat-frame")
 q=raw.rfind(b") "); need(q>1,"proc-stat-comm")
 lead=raw[:q+1]; left=lead.find(b"("); need(left>0,"proc-stat-left")
 gotpid=int(lead[:left-1]); f=raw[q+2:-1].split(b" "); need(len(f)>=20,"proc-stat-fields")
 return gotpid,int(f[1]),int(f[2]),int(f[3]),int(f[19])

def wait_nohang(pid):
 for unused in range(16):
  try: return os.waitpid(pid,os.WNOHANG)
  except InterruptedError: continue
  except ChildProcessError as e: raise Fail("wait-echild") from e
 raise Fail("wait-eintr-bound")

def read_some(fd,buf,cap):
 eof=False
 for unused in range(256):
  try: x=os.read(fd,4096)
  except BlockingIOError: break
  except InterruptedError: continue
  if not x: eof=True; break
  buf.extend(x); need(len(buf)<=cap,"raw-cap")
 return eof

def write_bounded(fd,data,deadline):
 set_nonblock(fd); pos=0; poller=select.poll(); poller.register(fd,select.POLLOUT|select.POLLERR|select.POLLHUP)
 for unused in range(4096):
  if pos==len(data): return
  n=now(); need(n<deadline,"write-deadline")
  try:
   z=os.write(fd,data[pos:])
   need(z>0,"write-zero"); pos+=z; continue
  except BlockingIOError: pass
  except InterruptedError: continue
  poller.poll(max(0,min(25,(deadline-n+999999)//1000000)))
 raise Fail("write-iterations")

def parse_line(line):
 need(line and b"\r" not in line and b"\x00" not in line,"line-frame")
 try: line.decode("ascii")
 except UnicodeDecodeError as e: raise Fail("line-ascii") from e
 parts=line.split(b"|"); need(parts[0]==b"P27E001V3","line-prefix")
 d={}
 for item in parts[1:]:
  need(item.count(b"=")==1,"line-equals")
  k,v=item.split(b"=",1); need(k and k not in d and all(c in b"abcdefghijklmnopqrstuvwxyz_" for c in k),"line-key")
  need(v and b"|" not in v and b"\n" not in v,"line-value"); d[k]=v
 return d

FIELDS={
 b"P00":(b"source_item_bytes",b"source_item_accounted_bytes",b"source_item_sha256",b"arg_max",b"spawn_returned",b"e2big",b"transport_feasible"),
 b"P01D":(b"python_image_dev",b"python_image_ino",b"python_image_mode",b"python_image_nlink",b"python_image_uid",b"python_image_gid",b"python_image_bytes",b"python_image_sha256",b"libc_confstr_hex",b"libc_path_hex",b"libc_map_dev",b"libc_map_ino",b"libc_open_dev",b"libc_open_ino",b"libc_mode",b"libc_nlink",b"libc_uid",b"libc_gid",b"libc_bytes",b"libc_sha256",b"posix_spawn_module",b"posix_spawn_name",b"posix_spawn_type",b"backend_surface",b"spawn_premise_satisfied"),
 b"P01C":(b"python_image_dev",b"python_image_ino",b"python_image_sha256",b"libc_path_hex",b"libc_map_dev",b"libc_map_ino",b"libc_sha256",b"libc_confstr_hex",b"posix_spawn_module",b"posix_spawn_name",b"child_raw_bytes",b"child_raw_sha256",b"child_pid",b"child_sid",b"child_pgid",b"spawn_premise_satisfied"),
 b"P02":(b"environment",b"environment_count",b"cwd_hex",b"flags",b"fds",b"fd_nodes",b"rlimit_cpu",b"rlimit_as",b"rlimit_fsize",b"rlimit_core",b"rlimit_nofile",b"rlimit_nproc"),
 b"P03":(b"soft_before",b"hard_before",b"soft_test",b"opened_fds",b"emfile",b"fds_after"),
 b"P04":(b"valid_signal_count",b"default_signal_count",b"defaults_csv",b"defaults_sha256",b"mask_empty",b"normalization_complete"),
 b"P05":(b"wnohang_zero",b"eintr",b"exit_pid",b"exit_raw",b"exit_code",b"echild",b"signal_pid",b"signal_raw",b"term_signal"),
 b"P06":(b"implementation_hex",b"adjustable",b"monotonic",b"declared_resolution_ns",b"observed_min_delta_ns",b"start_ns",b"end_ns",b"elapsed_ns",b"headroom_ns",b"deadline_ns",b"deadline_checked"),
 b"P07":(b"read_cloexec",b"write_cloexec",b"read_nonblock",b"write_nonblock",b"empty_eagain",b"initial_readable",b"byte_hex",b"eof_before_last_writer",b"hup_after_last_writer",b"eof_after_last_writer"),
 b"P08":(b"child_pid",b"child_sid",b"child_pgid",b"marker_sid",b"marker_pgid",b"live_pid_zero",b"raw_status",b"post_pid_esrch",b"reuse_proof"),
 b"P09":(b"child_pid",b"child_pgid",b"signal",b"raw_status",b"reap_start_ns",b"reap_end_ns",b"reap_elapsed_ns",b"reaped"),
 b"P10":(b"sample_count",b"pids",b"pgids",b"statuses",b"pid_duplicates",b"group_is_single_owned_launcher_group",b"reuse_proof"),
 b"P11":(b"capeff_hex",b"cap_fowner",b"open_result",b"atime_unchanged",b"created_dev",b"created_ino",b"cleanup_unlinked",b"cleanup_identity_observed",b"atomic_unlink_proof",b"scope_single_inode"),
 b"P12":(b"env_dev",b"env_ino",b"env_sha256",b"bash_dev",b"bash_ino",b"bash_sha256",b"child_raw_bytes",b"child_raw_sha256",b"child_pid",b"child_sid",b"child_pgid",b"executable_hex",b"environment",b"environment_count",b"underscore_absent",b"cwd_hex",b"real_payload_invoked",b"raw_status"),
 b"P13":(b"file_fsync_returned",b"hardlink_noreplace_returned",b"old_absent",b"inode_preserved",b"dir_fsync_returned",b"post_unlink_absent",b"created_dev",b"created_ino",b"cleanup_unlinked",b"cleanup_identity_observed",b"atomic_unlink_proof",b"durability_proof",b"rename_atomicity_proof",b"immutability_proof")}
COMMON=(b"marker_source_sha256",b"marker_pid",b"marker_sid",b"marker_pgid",b"children_spawned",b"children_reaped",b"child_pids",b"raw_statuses",b"result")

def parse_marker(raw,probe,marker_sha):
 need(raw.endswith(b"\n") and b"\r" not in raw and b"\x00" not in raw,"marker-frame")
 lines=raw.split(b"\n"); need(lines[-1]==b"" and all(lines[:-1]),"marker-lf")
 need(len(lines)==2+len(FIELDS[probe])+len(COMMON),"marker-line-count")
 first=parse_line(lines[0]); need(first=={b"probe":probe,b"schema":b"3"},"marker-header")
 keys=[]; values={}
 for line in lines[1:-1]:
  d=parse_line(line); need(d.get(b"probe")==probe and len(d)==2,"marker-row")
  k=next(x for x in d if x!=b"probe"); need(k not in values,"marker-duplicate")
  keys.append(k); values[k]=d[k]
 need(tuple(keys)==FIELDS[probe]+COMMON,"marker-order")
 need(values[b"marker_source_sha256"]==marker_sha and values[b"result"]==b"PASS","marker-result")
 for key in (b"marker_pid",b"marker_sid",b"marker_pgid",b"children_spawned",b"children_reaped"):
  need(values[key].isdigit() and str(int(values[key])).encode("ascii")==values[key],"marker-decimal")
 need(values[b"children_spawned"]==values[b"children_reaped"],"marker-reap-count")
 return values

def decimal(v):
 need(v.isdigit(),"field-decimal")
 n=int(v); need(str(n).encode("ascii")==v,"field-canonical"); return n

def csv_decimal(v):
 if v==b"-": return ()
 q=v.split(b","); need(q and all(x for x in q),"field-csv"); return tuple(decimal(x) for x in q)

def validate_probe(v,probe,safe):
 count=decimal(v[b"children_spawned"]); pids=csv_decimal(v[b"child_pids"]); statuses=csv_decimal(v[b"raw_statuses"])
 need(len(pids)==len(statuses)==count and all(x>1 for x in pids),"child-records")
 if probe==b"P00":
  returned=decimal(v[b"spawn_returned"]); e2big=decimal(v[b"e2big"]); need(v[b"source_item_bytes"]==b"251414" and v[b"source_item_accounted_bytes"]==b"251415" and v[b"source_item_sha256"]==hashlib.sha256(b"#"*251414).hexdigest().encode("ascii"),"p00-fields"); need(returned in (0,1) and e2big in (0,1) and returned+e2big==1 and decimal(v[b"transport_feasible"])==returned and count==returned,"p00-result")
 elif probe==b"P01D":
  need(count==0 and v[b"python_image_bytes"]==b"30626264" and v[b"python_image_sha256"]==PY_SHA and v[b"libc_map_dev"]==v[b"libc_open_dev"] and v[b"libc_map_ino"]==v[b"libc_open_ino"] and v[b"spawn_premise_satisfied"]==b"0","p01d-fields")
 elif probe==b"P01C":
  need(count==1 and v[b"python_image_sha256"]==PY_SHA and v[b"spawn_premise_satisfied"]==b"1" and decimal(v[b"child_pid"])==pids[0] and decimal(v[b"child_sid"])==decimal(v[b"child_pgid"]),"p01c-fields")
 elif probe==b"P02":
  expected=b",".join((k+b"="+ENV[k]).hex().encode("ascii") for k in sorted(ENV)); need(count==0 and v[b"environment_count"]==b"10" and v[b"environment"]==expected and bytes.fromhex(v[b"cwd_hex"].decode("ascii"))==safe and v[b"fds"]==b"0,1,2" and v[b"flags"]==b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1","p02-fields")
 elif probe==b"P03":
  need(count==0 and v[b"soft_before"]==b"4096" and v[b"hard_before"]==b"1048576" and v[b"soft_test"]==b"64" and v[b"emfile"]==b"1" and v[b"fds_after"]==b"0,1,2","p03-fields")
 elif probe==b"P04":
  need(count==0 and v[b"mask_empty"]==b"1" and v[b"normalization_complete"]==b"1" and decimal(v[b"default_signal_count"])==len(csv_decimal(v[b"defaults_csv"])),"p04-fields")
 elif probe==b"P05":
  need(count==2 and v[b"wnohang_zero"]==v[b"eintr"]==v[b"echild"]==b"1" and v[b"exit_code"]==b"23" and decimal(v[b"exit_pid"])==pids[0] and decimal(v[b"signal_pid"])==pids[1] and decimal(v[b"exit_raw"])==statuses[0] and decimal(v[b"signal_raw"])==statuses[1] and decimal(v[b"term_signal"])==int(signal.SIGTERM),"p05-fields")
 elif probe==b"P06":
  a=decimal(v[b"start_ns"]); b=decimal(v[b"end_ns"]); e=decimal(v[b"elapsed_ns"]); need(count==0 and a<=b and e==b-a and decimal(v[b"deadline_ns"])==a+1000000000 and v[b"deadline_checked"]==b"1" and decimal(v[b"declared_resolution_ns"])>=1 and decimal(v[b"observed_min_delta_ns"])>=1,"p06-fields")
 elif probe==b"P07":
  need(count==0 and v[b"read_cloexec"]==v[b"write_cloexec"]==v[b"read_nonblock"]==v[b"write_nonblock"]==v[b"empty_eagain"]==v[b"hup_after_last_writer"]==v[b"eof_after_last_writer"]==b"1" and v[b"initial_readable"]==v[b"eof_before_last_writer"]==b"0" and v[b"byte_hex"]==b"78","p07-fields")
 elif probe==b"P08":
  need(count==1 and decimal(v[b"child_pid"])==pids[0] and decimal(v[b"raw_status"])==statuses[0] and v[b"live_pid_zero"]==v[b"post_pid_esrch"]==b"1" and v[b"reuse_proof"]==b"0","p08-fields")
 elif probe==b"P09":
  a=decimal(v[b"reap_start_ns"]); b=decimal(v[b"reap_end_ns"]); need(count==1 and decimal(v[b"child_pid"])==pids[0] and decimal(v[b"raw_status"])==statuses[0] and decimal(v[b"signal"])==int(signal.SIGKILL) and a<=b and decimal(v[b"reap_elapsed_ns"])==b-a and b-a<=1000000000 and v[b"reaped"]==b"1","p09-fields")
 elif probe==b"P10":
  pgids=csv_decimal(v[b"pgids"]); need(count==16 and v[b"sample_count"]==b"16" and csv_decimal(v[b"pids"])==pids and len(pgids)==16 and all(x==decimal(v[b"marker_pgid"]) for x in pgids) and csv_decimal(v[b"statuses"])==statuses and decimal(v[b"pid_duplicates"])==len(pids)-len(set(pids)) and v[b"group_is_single_owned_launcher_group"]==b"1" and v[b"reuse_proof"]==b"0","p10-fields")
 elif probe==b"P11":
  need(count==0 and v[b"open_result"] in (b"OK",b"EPERM") and v[b"cleanup_unlinked"]==v[b"cleanup_identity_observed"]==v[b"scope_single_inode"]==b"1" and v[b"atomic_unlink_proof"]==b"0" and ((v[b"open_result"]==b"OK" and v[b"cap_fowner"]==v[b"atime_unchanged"]==b"1") or (v[b"open_result"]==b"EPERM" and v[b"cap_fowner"]==v[b"atime_unchanged"]==b"0")),"p11-fields")
 elif probe==b"P12":
  expected=b",".join((k+b"="+ENV[k]).hex().encode("ascii") for k in sorted(ENV)); need(count==1 and v[b"env_sha256"]==b"85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0" and v[b"bash_sha256"]==b"59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4" and decimal(v[b"child_pid"])==pids[0] and decimal(v[b"raw_status"])==statuses[0] and bytes.fromhex(v[b"executable_hex"].decode("ascii"))==PYTHON and v[b"environment"]==expected and v[b"environment_count"]==b"10" and v[b"underscore_absent"]==b"1" and bytes.fromhex(v[b"cwd_hex"].decode("ascii"))==safe and v[b"real_payload_invoked"]==b"0","p12-fields")
 elif probe==b"P13":
  need(count==0 and v[b"file_fsync_returned"]==v[b"hardlink_noreplace_returned"]==v[b"old_absent"]==v[b"inode_preserved"]==v[b"dir_fsync_returned"]==v[b"post_unlink_absent"]==v[b"cleanup_unlinked"]==v[b"cleanup_identity_observed"]==b"1" and v[b"atomic_unlink_proof"]==v[b"durability_proof"]==v[b"rename_atomicity_proof"]==v[b"immutability_proof"]==b"0","p13-fields")
 else: raise Fail("probe-validator-unreachable")

need(len(sys.argv)>=16 and sys.argv[0]=="-c","argv-count")
probe=os.fsencode(sys.argv[1]); auth=os.fsencode(sys.argv[2]); launcher_source=os.fsencode(sys.argv[3]); launcher_sha=os.fsencode(sys.argv[4]); marker_source=os.fsencode(sys.argv[5]); marker_sha=os.fsencode(sys.argv[6])
delta=int(sys.argv[7]); ledger_bytes=int(sys.argv[8]); ledger_lf=int(sys.argv[9]); ledger_sha=os.fsencode(sys.argv[10]); ledger_terminal=os.fsencode(sys.argv[11]); control_bytes=int(sys.argv[12]); control_lf=int(sys.argv[13]); control_sha=os.fsencode(sys.argv[14]); control_terminal=os.fsencode(sys.argv[15]); extra=tuple(os.fsencode(x) for x in sys.argv[16:])
need(probe in FIELDS,"probe-id")
need(len(auth)==64 and all(c in b"0123456789abcdef" for c in auth),"auth-id")
need(1000000000<=delta<=10000000000,"deadline-range")
need(len(launcher_sha)==len(marker_sha)==len(ledger_sha)==len(control_sha)==64,"sha-length")
need(hashlib.sha256(launcher_source).hexdigest().encode("ascii")==launcher_sha and hashlib.sha256(marker_source).hexdigest().encode("ascii")==marker_sha,"inner-source-hash")
need(b"\x00" not in launcher_source and b"\x00" not in marker_source and launcher_source.isascii() and marker_source.isascii(),"inner-source-encoding")
outer_source=os.fsencode(sys.orig_argv[8]); outer_sha=hashlib.sha256(outer_source).hexdigest().encode("ascii")
need(sys.orig_argv[:8]==[PYTHON.decode("ascii"),"-I","-S","-B","-P","-X","utf8","-c"],"outer-vector")
need(sys.executable==PYTHON.decode("ascii") and dict(os.environb)==ENV,"outer-runtime")
need(sys.flags.isolated==1 and sys.flags.ignore_environment==1 and sys.flags.no_site==1 and sys.flags.no_user_site==1 and sys.flags.dont_write_bytecode==1 and sys.flags.safe_path==1 and sys.flags.utf8_mode==1 and sys.flags.hash_randomization==1,"outer-flags")
need(os.geteuid()==0 and os.getegid()==0,"outer-owner")
need(resource.getrlimit(resource.RLIMIT_NOFILE)[1]==HARD_NOFILE,"outer-hard-nofile")
need(fd_census(HARD_NOFILE)==(0,1,2),"outer-initial-fds")
initial_nodes=[]
for fd in (0,1,2):
 s=os.fstat(fd); need(stat.S_ISFIFO(s.st_mode),"outer-stdio-type"); initial_nodes.append((s.st_dev,s.st_ino))
need(len(set(initial_nodes))==3,"outer-stdio-nodes")

stage=b"opening"; failure=b"none"; timed=0; leader_pid=-1; leader_status=-1; leader_reaped=0; leader_start=-1; term_sent=0; kill_sent=0; group_absent=0; released=0; removed=0; cleanup_race_proof=0
stdout_raw=bytearray(); stderr_raw=bytearray(); tele_raw=bytearray(); stdout_eof=stderr_eof=tele_eof=False
lfd=cfd=pfd=sfd=rfd=tfd=dfd=-1
pipefds=[]; parentfds=[]; safe=b""; name=b""; dkey=None; pkey=None; lkey=None; ledger_key=None; control_key=None
start=now(); finish=start

try:
 stage=b"opening"
 pfd,sfd,pkey,lkey=bind_python()
 lfd,ledger_key,unused=regular_open(LEDGER,ledger_bytes,ledger_lf,ledger_sha,ledger_terminal)
 cfd,control_key,unused=regular_open(CONTROL,control_bytes,control_lf,control_sha,control_terminal)
 rfd,tfd,rkey,tkey=component_open()
 old_umask=os.umask(0o077); os.umask(0o077)
 name=b"p27-e001-host-v3-"+auth; safe=b"/tmp/"+name
 need(b"/build/" not in safe and b"evidence" not in safe and b"recovery" not in safe and b".." not in safe.split(b"/"),"safe-protected")
 os.mkdir(name,0o700,dir_fd=tfd)
 dfd=os.open(name,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,dir_fd=tfd)
 os.fchmod(dfd,0o700)
 ds=os.fstat(dfd); dkey=(ds.st_dev,ds.st_ino,ds.st_mode,ds.st_nlink,ds.st_uid,ds.st_gid,ds.st_size)
 need(ds.st_dev==tkey[0] and ds.st_ino!=tkey[1],"safe-filesystem")
 safe_recheck(tfd,name,dfd,dkey,safe,True)
 stage=b"pipes"
 pairs=[]
 for unused in range(5):
  a,b=os.pipe2(os.O_CLOEXEC); pipefds.extend((a,b)); pairs.append((a,b))
 need(len(set(pipefds))==10,"pipe-fd-distinct")
 nodes=[]
 for a,b in pairs:
  x=os.fstat(a); y=os.fstat(b); need(stat.S_ISFIFO(x.st_mode) and stat.S_ISFIFO(y.st_mode) and (x.st_dev,x.st_ino)==(y.st_dev,y.st_ino),"pipe-pair")
  nodes.append((x.st_dev,x.st_ino))
 need(len(set(nodes))==5,"pipe-node-distinct")
 stdin_r,stdin_w=pairs[0]; out_r,out_w=pairs[1]; err_r,err_w=pairs[2]; tele_r,tele_w=pairs[3]; release_r,release_w=pairs[4]
 for fd in (out_r,err_r,tele_r,release_w): set_nonblock(fd)
 close_if(stdin_w); pipefds.remove(stdin_w); stdin_w=-1
 openfds=tuple(fd for fd in fd_census(HARD_NOFILE) if fd>=5)
 actions=[(os.POSIX_SPAWN_DUP2,stdin_r,0),(os.POSIX_SPAWN_DUP2,out_w,1),(os.POSIX_SPAWN_DUP2,err_w,2),(os.POSIX_SPAWN_DUP2,tele_w,3),(os.POSIX_SPAWN_DUP2,release_r,4)]
 actions.extend((os.POSIX_SPAWN_CLOSE,fd) for fd in openfds)
 argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",launcher_source,probe,safe,marker_source,marker_sha,launcher_sha,str(delta).encode("ascii"))+extra
 need(all(b"\x00" not in x for x in argv),"launcher-argv-nul")
 stage=b"spawn"
 leader_pid=os.posix_spawn(PYTHON,argv,ENV,file_actions=tuple(actions),setsid=True,setsigmask=(),setsigdef=SIGDEFS)
 need(leader_pid>1,"launcher-pid")
 for fd in (stdin_r,out_w,err_w,tele_w,release_r):
  close_if(fd)
  if fd in pipefds: pipefds.remove(fd)
 parentfds=[out_r,err_r,tele_r,release_w]
 stage=b"ownership"
 ownership_deadline=checked(now(),1000000000)
 poller=select.poll()
 for fd in (out_r,err_r,tele_r): poller.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 ownership=None
 for unused in range(1024):
  q=wait_nohang(leader_pid)
  if q[0]==leader_pid: leader_reaped=1; leader_status=q[1]; raise Fail("launcher-before-ownership")
  if b"\n" in tele_raw:
   line=bytes(tele_raw[:tele_raw.index(b"\n")]); ownership=parse_line(line); break
  n=now(); need(n<ownership_deadline,"ownership-timeout")
  poller.poll(max(0,min(25,(ownership_deadline-n+999999)//1000000)))
  stdout_eof=read_some(out_r,stdout_raw,RAW_CAP) or stdout_eof
  stderr_eof=read_some(err_r,stderr_raw,RAW_CAP) or stderr_eof
  tele_eof=read_some(tele_r,tele_raw,TELE_CAP) or tele_eof
 else: raise Fail("ownership-iterations")
 need(ownership is not None and ownership.get(b"launcher")==b"ownership" and ownership.get(b"probe")==probe,"ownership-line")
 for key in (b"launcher_pid",b"launcher_sid",b"launcher_pgid",b"launcher_start",b"marker_pid",b"marker_pgid"):
  need(ownership.get(key,b"").isdigit(),"ownership-decimal")
 leader_start=int(ownership[b"launcher_start"])
 ident=proc_identity(leader_pid)
 need(int(ownership[b"launcher_pid"])==leader_pid and int(ownership[b"launcher_sid"])==leader_pid and int(ownership[b"launcher_pgid"])==leader_pid,"ownership-topology")
 need(ident==(leader_pid,os.getpid(),leader_pid,leader_pid,leader_start),"ownership-proc")
 need(int(ownership[b"marker_pid"])>1 and int(ownership[b"marker_pgid"])==leader_pid,"marker-topology")
 need(len(stdout_raw)==0 and len(stderr_raw)==0,"pre-release-output")
 regular_recheck(lfd,LEDGER,ledger_key,ledger_bytes,ledger_lf,ledger_sha,ledger_terminal)
 regular_recheck(cfd,CONTROL,control_key,control_bytes,control_lf,control_sha,control_terminal)
 recheck_python(pfd,sfd,pkey,lkey); safe_recheck(tfd,name,dfd,dkey,safe,True)
 stage=b"release"
 release_deadline=checked(now(),250000000)
 write_bounded(release_w,b"L",release_deadline); close_if(release_w); pipefds.remove(release_w); parentfds.remove(release_w); release_w=-1; released=1
 run_start=now(); run_deadline=checked(run_start,delta)
 stage=b"running"
 for unused in range(20000):
  if not leader_reaped:
   q=wait_nohang(leader_pid)
   if q[0]==leader_pid: leader_reaped=1; leader_status=q[1]
  stdout_eof=read_some(out_r,stdout_raw,RAW_CAP) or stdout_eof
  stderr_eof=read_some(err_r,stderr_raw,RAW_CAP) or stderr_eof
  tele_eof=read_some(tele_r,tele_raw,TELE_CAP) or tele_eof
  if leader_reaped and stdout_eof and stderr_eof and tele_eof: break
  n=now()
  if n>=run_deadline: timed=1; raise Fail("run-timeout")
  poller.poll(max(0,min(25,(run_deadline-n+999999)//1000000)))
 else: raise Fail("run-iterations")
 finish=now(); elapsed(run_start,finish,delta)
 need(leader_reaped and leader_status==0 and stdout_eof and stderr_eof and tele_eof,"launcher-completion")
 stage=b"parse"
 need(len(stderr_raw)==0,"launcher-stderr")
 values=parse_marker(bytes(stdout_raw),probe,marker_sha)
 validate_probe(values,probe,safe)
 need(int(values[b"marker_pgid"])==leader_pid and int(values[b"marker_pid"])==int(ownership[b"marker_pid"]),"marker-owned")
 need(bytes(tele_raw).endswith(b"\n") and b"\r" not in tele_raw and b"\x00" not in tele_raw,"tele-frame")
 tlines=bytes(tele_raw).split(b"\n"); need(tlines[-1]==b"" and len(tlines)==3,"tele-lines")
 own2=parse_line(tlines[0]); terminal=parse_line(tlines[1]); need(own2==ownership,"ownership-stable")
 need(terminal.get(b"launcher")==b"terminal" and terminal.get(b"probe")==probe,"terminal-line")
 expected={b"launcher_source_sha256":launcher_sha,b"marker_source_sha256":marker_sha,b"marker_pid":ownership[b"marker_pid"],b"marker_raw_status":b"0",b"marker_reaped":b"1",b"marker_stdout_bytes":str(len(stdout_raw)).encode("ascii"),b"marker_stdout_sha256":hashlib.sha256(stdout_raw).hexdigest().encode("ascii"),b"marker_stdout_eof":b"1",b"marker_stderr_bytes":b"0",b"marker_stderr_sha256":hashlib.sha256(b"").hexdigest().encode("ascii"),b"marker_stderr_eof":b"1",b"timed":b"0",b"abort_seen":b"0",b"cleanup_requested":b"0"}
 for k,v in expected.items(): need(terminal.get(k)==v,"terminal-field")
 need(terminal.get(b"elapsed_ns",b"").isdigit() and 0<=int(terminal[b"elapsed_ns"])<=delta,"terminal-elapsed")
 stage=b"terminal"
except BaseException as e:
 if isinstance(e,Fail): failure=os.fsencode(str(e))
 elif isinstance(e,TimeoutError): failure=b"timeout-exception"; timed=1
 elif isinstance(e,OSError): failure=("oserror-%d"%(e.errno if e.errno is not None else -1)).encode("ascii")
 else: failure=("exception-"+type(e).__name__).encode("ascii","strict")
 if leader_pid>1 and not leader_reaped:
  stage=b"cleanup-term"
  q=wait_nohang(leader_pid)
  if q[0]==leader_pid: leader_reaped=1; leader_status=q[1]
  if not leader_reaped:
   ident=proc_identity(leader_pid)
   if leader_start<0: leader_start=ident[4]
   need(ident==(leader_pid,os.getpid(),leader_pid,leader_pid,leader_start),"cleanup-leader-identity")
   try: os.killpg(leader_pid,signal.SIGTERM); term_sent=1
   except ProcessLookupError: pass
   coop=checked(now(),250000000)
   for unused in range(512):
    q=wait_nohang(leader_pid)
    if q[0]==leader_pid: leader_reaped=1; leader_status=q[1]; break
    stdout_eof=read_some(out_r,stdout_raw,RAW_CAP) or stdout_eof if out_r>=0 else stdout_eof
    stderr_eof=read_some(err_r,stderr_raw,RAW_CAP) or stderr_eof if err_r>=0 else stderr_eof
    tele_eof=read_some(tele_r,tele_raw,TELE_CAP) or tele_eof if tele_r>=0 else tele_eof
    if now()>=coop: break
   if not leader_reaped:
    ident=proc_identity(leader_pid); need(ident==(leader_pid,os.getpid(),leader_pid,leader_pid,leader_start),"escalation-leader-identity")
    try: os.killpg(leader_pid,signal.SIGKILL); kill_sent=1
    except ProcessLookupError: pass
    hard=checked(now(),1000000000)
    for unused in range(2048):
     q=wait_nohang(leader_pid)
     if q[0]==leader_pid: leader_reaped=1; leader_status=q[1]; break
     if now()>=hard: break
 if leader_reaped:
  try: os.killpg(leader_pid,0)
  except ProcessLookupError as z:
   if z.errno==errno.ESRCH: group_absent=1
  except PermissionError: group_absent=0
  drain_deadline=checked(now(),500000000)
  for unused in range(1024):
   if out_r>=0: stdout_eof=read_some(out_r,stdout_raw,RAW_CAP) or stdout_eof
   if err_r>=0: stderr_eof=read_some(err_r,stderr_raw,RAW_CAP) or stderr_eof
   if tele_r>=0: tele_eof=read_some(tele_r,tele_raw,TELE_CAP) or tele_eof
   if stdout_eof and stderr_eof and tele_eof: break
   if now()>=drain_deadline: break
 finish=now()
finally:
 if leader_reaped and leader_pid>1 and group_absent==0:
  try: os.killpg(leader_pid,0)
  except ProcessLookupError as z:
   if z.errno==errno.ESRCH: group_absent=1
 for fd in tuple(parentfds)+tuple(pipefds): close_if(fd)
 terminal_ok=0
 try:
  if lfd>=0: regular_recheck(lfd,LEDGER,ledger_key,ledger_bytes,ledger_lf,ledger_sha,ledger_terminal)
  if cfd>=0: regular_recheck(cfd,CONTROL,control_key,control_bytes,control_lf,control_sha,control_terminal)
  if pfd>=0 and sfd>=0: recheck_python(pfd,sfd,pkey,lkey)
  if dfd>=0: safe_recheck(tfd,name,dfd,dkey,safe,True)
  terminal_ok=1
 except BaseException:
  failure=b"terminal-identity"
 if terminal_ok and dfd>=0:
  try:
   before=os.fstat(dfd); path_before=os.stat(name,dir_fd=tfd,follow_symlinks=False)
   kb=(before.st_dev,before.st_ino,before.st_mode,before.st_nlink,before.st_uid,before.st_gid,before.st_size)
   kp=(path_before.st_dev,path_before.st_ino,path_before.st_mode,path_before.st_nlink,path_before.st_uid,path_before.st_gid,path_before.st_size)
   need(kb==kp==dkey and os.listdir(dfd)==[],"cleanup-precondition")
   os.rmdir(name,dir_fd=tfd)
   held=os.fstat(dfd); kh=(held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size)
   need(kh==dkey,"cleanup-held-identity")
   absent=0
   try: os.stat(name,dir_fd=tfd,follow_symlinks=False)
   except FileNotFoundError: absent=1
   need(absent==1,"cleanup-path-present"); removed=1
  except BaseException:
   failure=b"cleanup-filesystem"
 for fd in (lfd,cfd,pfd,sfd,dfd,tfd,rfd): close_if(fd)
 finish=max(finish,now())
 result=b"PASS" if failure==b"none" and stage==b"terminal" and leader_reaped==1 and leader_status==0 and group_absent==1 and stdout_eof and stderr_eof and tele_eof and terminal_ok==1 and removed==1 else b"FAIL"
 rows=[b"P27E001V3|outer=report|schema=3",b"P27E001V3|probe="+probe,b"P27E001V3|auth_id="+auth,b"P27E001V3|outer_source_bytes="+str(len(outer_source)).encode("ascii"),b"P27E001V3|outer_source_sha256="+outer_sha,b"P27E001V3|launcher_source_bytes="+str(len(launcher_source)).encode("ascii"),b"P27E001V3|launcher_source_sha256="+launcher_sha,b"P27E001V3|marker_source_bytes="+str(len(marker_source)).encode("ascii"),b"P27E001V3|marker_source_sha256="+marker_sha,b"P27E001V3|stage="+stage,b"P27E001V3|failure="+failure,b"P27E001V3|timed="+str(timed).encode("ascii"),b"P27E001V3|leader_pid="+str(leader_pid).encode("ascii"),b"P27E001V3|leader_start="+str(leader_start).encode("ascii"),b"P27E001V3|leader_raw_status="+str(leader_status).encode("ascii"),b"P27E001V3|leader_reaped="+str(leader_reaped).encode("ascii"),b"P27E001V3|sigterm_sent="+str(term_sent).encode("ascii"),b"P27E001V3|sigkill_sent="+str(kill_sent).encode("ascii"),b"P27E001V3|group_absent="+str(group_absent).encode("ascii"),b"P27E001V3|released="+str(released).encode("ascii"),b"P27E001V3|stdout_bytes="+str(len(stdout_raw)).encode("ascii"),b"P27E001V3|stdout_sha256="+hashlib.sha256(stdout_raw).hexdigest().encode("ascii"),b"P27E001V3|stdout_hex="+bytes(stdout_raw).hex().encode("ascii"),b"P27E001V3|stdout_eof="+str(int(stdout_eof)).encode("ascii"),b"P27E001V3|stderr_bytes="+str(len(stderr_raw)).encode("ascii"),b"P27E001V3|stderr_sha256="+hashlib.sha256(stderr_raw).hexdigest().encode("ascii"),b"P27E001V3|stderr_hex="+bytes(stderr_raw).hex().encode("ascii"),b"P27E001V3|stderr_eof="+str(int(stderr_eof)).encode("ascii"),b"P27E001V3|telemetry_bytes="+str(len(tele_raw)).encode("ascii"),b"P27E001V3|telemetry_sha256="+hashlib.sha256(tele_raw).hexdigest().encode("ascii"),b"P27E001V3|telemetry_hex="+bytes(tele_raw).hex().encode("ascii"),b"P27E001V3|telemetry_eof="+str(int(tele_eof)).encode("ascii"),b"P27E001V3|start_ns="+str(start).encode("ascii"),b"P27E001V3|finish_ns="+str(finish).encode("ascii"),b"P27E001V3|elapsed_ns="+str(finish-start if finish>=start else -1).encode("ascii"),b"P27E001V3|terminal_identity="+str(terminal_ok).encode("ascii"),b"P27E001V3|safe_removed="+str(removed).encode("ascii"),b"P27E001V3|cleanup_atomic_inode_proof=0",b"P27E001V3|result="+result]
 report=b"\n".join(rows)+b"\n"
 try: write_bounded(1,report,checked(now(),1000000000))
 except BaseException: pass
OUTER CONTROLLER V3 SOURCE END
```

This block is inert documentation. It has not been imported, parsed,
compiled, evaluated, or executed. Its exception path preserves raw bytes,
raw wait status, PID, source identities, stage-specific failure, timeout bit,
cleanup observations, and exact EOF flags. It never maps an arbitrary
exception to `timed=1` and never treats ECHILD as successful reap.

## 5. Exact common-launcher source

The launcher is the direct session/group leader and the outer controller's
only wait child. It establishes cwd, umask, limits, signal mask/dispositions,
FD topology, executable image, inner source identity, and marker topology
before emitting ownership. The marker is already spawned but blocked on its
private gate. Only the outer release byte can release it. The launcher never
delivers a PID or group signal. On any live-marker timeout or failure it emits
a cleanup request and remains the unreaped group leader while the outer
controller performs cooperative group TERM and bounded KILL escalation.

```text
COMMON LAUNCHER V3 SOURCE BEGIN
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
HARD_NOFILE=1048576
CAP=262144
ABORT=0

class Fail(Exception): pass

def need(v,code):
 if not v: raise Fail(code)

def checked(now,delta):
 need(type(now) is int and type(delta) is int and now>=0 and delta>0,"clock-input")
 need(now<=((1<<63)-1)-delta,"clock-headroom"); return now+delta

def now():
 v=time.monotonic_ns(); need(type(v) is int and v>=0,"clock-negative"); return v

def elapsed(a,b,bound):
 need(0<=a<=b and b-a<=bound,"elapsed-bound"); return b-a

def close_if(fd):
 if fd>=0:
  try: os.close(fd)
  except OSError: pass

def set_nonblock(fd):
 v=fcntl.fcntl(fd,fcntl.F_GETFL); fcntl.fcntl(fd,fcntl.F_SETFL,v|os.O_NONBLOCK)

def write_bounded(fd,data,deadline):
 set_nonblock(fd); pos=0; p=select.poll(); p.register(fd,select.POLLOUT|select.POLLERR|select.POLLHUP)
 for unused in range(4096):
  if pos==len(data): return
  n=now(); need(n<deadline,"write-deadline")
  try:
   z=os.write(fd,data[pos:]); need(z>0,"write-zero"); pos+=z; continue
  except BlockingIOError: pass
  except InterruptedError: continue
  p.poll(max(0,min(25,(deadline-n+999999)//1000000)))
 raise Fail("write-iterations")

def read_some(fd,buf):
 eof=False
 for unused in range(256):
  try: x=os.read(fd,4096)
  except BlockingIOError: break
  except InterruptedError: continue
  if not x: eof=True; break
  buf.extend(x); need(len(buf)<=CAP,"stream-cap")
 return eof

def wait_nohang(pid):
 for unused in range(16):
  try: return os.waitpid(pid,os.WNOHANG)
  except InterruptedError: continue
  except ChildProcessError as e: raise Fail("wait-echild") from e
 raise Fail("wait-eintr-bound")

def fd_census(limit):
 a=[]; flags={}
 for fd in range(limit):
  try: v=fcntl.fcntl(fd,fcntl.F_GETFD)
  except OSError as e:
   if e.errno==errno.EBADF: continue
   raise
  a.append(fd); flags[fd]=v
 return tuple(a),flags

def sigdefs():
 return tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))

SIGDEFS=sigdefs()

def normalize():
 signal.pthread_sigmask(signal.SIG_SETMASK,set())
 for n in SIGDEFS: signal.signal(n,signal.SIG_DFL)
 need(signal.pthread_sigmask(signal.SIG_BLOCK,set())==set(),"signal-mask")
 for n in SIGDEFS: need(signal.getsignal(n)==signal.SIG_DFL,"signal-default")

def hash_fd(fd,size):
 os.lseek(fd,0,os.SEEK_SET); h=hashlib.sha256(); total=0
 for unused in range((size+1048575)//1048576+1):
  try: x=os.read(fd,min(1048576,size-total+1))
  except InterruptedError: continue
  if not x: break
  total+=len(x); need(total<=size,"image-growth"); h.update(x)
 need(total==size,"image-short"); return h.hexdigest().encode("ascii")

def bind_image():
 need(os.readlink(PYTHON)==b"python3.12","python-target")
 pfd=os.open(PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW); sfd=os.open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC)
 a=os.fstat(pfd); b=os.fstat(sfd)
 key=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(key(a)==key(b) and stat.S_ISREG(a.st_mode) and stat.S_IMODE(a.st_mode)==0o755 and a.st_nlink==1 and a.st_uid==0 and a.st_gid==0 and a.st_size==PY_BYTES,"python-image")
 need(hash_fd(pfd,PY_BYTES)==PY_SHA and hash_fd(sfd,PY_BYTES)==PY_SHA,"python-hash")
 return pfd,sfd,key(a)

def recheck_image(pfd,sfd,key):
 a=os.fstat(pfd); b=os.fstat(sfd); p=os.stat(PYRES,follow_symlinks=False)
 k=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(k(a)==k(b)==k(p)==key and os.readlink(PYTHON)==b"python3.12","terminal-python")
 need(hash_fd(pfd,PY_BYTES)==PY_SHA and hash_fd(sfd,PY_BYTES)==PY_SHA,"terminal-python-hash")

def proc_identity(pid):
 path=("/proc/%d/stat"%pid).encode("ascii"); fd=os.open(path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:
  raw=b""
  for unused in range(8):
   try: x=os.read(fd,512)
   except InterruptedError: continue
   if not x: break
   raw+=x; need(len(raw)<=4096,"proc-cap")
 finally: os.close(fd)
 need(raw.endswith(b"\n") and raw.count(b"\n")==1,"proc-frame")
 q=raw.rfind(b") "); left=raw[:q+1].find(b"("); need(q>1 and left>0,"proc-comm")
 got=int(raw[:left-1]); f=raw[q+2:-1].split(b" "); need(len(f)>=20,"proc-fields")
 return got,int(f[1]),int(f[2]),int(f[3]),int(f[19])

def release_read(fd,deadline):
 set_nonblock(fd); raw=bytearray(); p=select.poll(); p.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR); eof=False
 for unused in range(1024):
  for inner in range(16):
   try: x=os.read(fd,2)
   except BlockingIOError: break
   except InterruptedError: continue
   if not x: eof=True; break
   raw.extend(x); need(len(raw)<=2,"release-cap")
  if eof: break
  n=now(); need(n<deadline,"release-timeout"); p.poll(max(0,min(25,(deadline-n+999999)//1000000)))
 need(bytes(raw)==b"L" and eof,"release-frame")

def abort_handler(signum,frame):
 global ABORT
 ABORT=1

need(len(sys.argv)>=7 and sys.argv[0]=="-c","argv-count")
probe=os.fsencode(sys.argv[1]); safe=os.fsencode(sys.argv[2]); marker_source=os.fsencode(sys.argv[3]); marker_sha=os.fsencode(sys.argv[4]); launcher_sha=os.fsencode(sys.argv[5]); delta=int(sys.argv[6]); extra=tuple(os.fsencode(x) for x in sys.argv[7:])
source=os.fsencode(sys.orig_argv[8])
need(hashlib.sha256(source).hexdigest().encode("ascii")==launcher_sha,"launcher-source")
need(hashlib.sha256(marker_source).hexdigest().encode("ascii")==marker_sha and marker_source.isascii() and b"\x00" not in marker_source,"marker-source")
need(probe in (b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13"),"probe-id")
need(1000000000<=delta<=10000000000,"deadline")
need(dict(os.environb)==ENV and sys.executable==PYTHON.decode("ascii"),"runtime")
need(sys.orig_argv[:8]==[PYTHON.decode("ascii"),"-I","-S","-B","-P","-X","utf8","-c"],"vector")
need(sys.flags.isolated==1 and sys.flags.ignore_environment==1 and sys.flags.no_site==1 and sys.flags.no_user_site==1 and sys.flags.dont_write_bytecode==1 and sys.flags.safe_path==1 and sys.flags.utf8_mode==1 and sys.flags.hash_randomization==1,"flags")
need(os.geteuid()==0 and os.getegid()==0,"owner")
need(safe.startswith(b"/tmp/p27-e001-host-v3-") and len(safe)==len(b"/tmp/p27-e001-host-v3-")+64 and b".." not in safe.split(b"/"),"safe-path")
os.chdir(safe); need(os.getcwdb()==safe,"cwd")
old_umask=os.umask(0o077); os.umask(0o077)
need(resource.getrlimit(resource.RLIMIT_NOFILE)[1]==HARD_NOFILE,"hard-nofile")
resource.setrlimit(resource.RLIMIT_NOFILE,(4096,HARD_NOFILE))
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
resource.setrlimit(resource.RLIMIT_CORE,(0,0))
np=resource.getrlimit(resource.RLIMIT_NPROC); nph=np[1]; nps=32 if nph==resource.RLIM_INFINITY else min(32,nph); need(nps>=4,"nproc"); resource.setrlimit(resource.RLIMIT_NPROC,(nps,nph))
normalize()
a,af=fd_census(HARD_NOFILE); b,bf=fd_census(HARD_NOFILE)
need(a==b==(0,1,2,3,4) and af==bf and all(af[x]==0 for x in a),"launcher-fds")
nodes=[]
for fd in a:
 s=os.fstat(fd); need(stat.S_ISFIFO(s.st_mode),"launcher-fd-type"); nodes.append((s.st_dev,s.st_ino))
need(len(set(nodes))==5,"launcher-fd-nodes")
pfd,sfd,pkey=bind_image()
self_ident=proc_identity(os.getpid())
need(self_ident[0]==os.getpid() and self_ident[1]==os.getppid() and self_ident[2]==os.getpid() and self_ident[3]==os.getpid(),"launcher-topology")
launcher_start=self_ident[4]
signal.signal(signal.SIGTERM,abort_handler)
signal.signal(signal.SIGINT,abort_handler)
for fd in (1,2,3): set_nonblock(fd)
out_r=out_w=err_r=err_w=gate_r=gate_w=-1
marker_pid=-1; marker_status=-1; marker_reaped=0; out_eof=err_eof=False; outs=bytearray(); errs=bytearray(); timed=0; cleanup=0; failure=b"none"; run_start=now(); run_finish=run_start

try:
 out_r,out_w=os.pipe2(os.O_CLOEXEC); err_r,err_w=os.pipe2(os.O_CLOEXEC); gate_r,gate_w=os.pipe2(os.O_CLOEXEC)
 set_nonblock(out_r); set_nonblock(err_r)
 openfds=tuple(fd for fd in fd_census(HARD_NOFILE)[0] if fd>=4)
 actions=[(os.POSIX_SPAWN_DUP2,out_w,1),(os.POSIX_SPAWN_DUP2,err_w,2),(os.POSIX_SPAWN_DUP2,gate_r,3)]
 actions.extend((os.POSIX_SPAWN_CLOSE,fd) for fd in openfds)
 argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",marker_source,probe,safe,marker_sha,str(delta).encode("ascii"))+extra
 marker_pid=os.posix_spawn(PYTHON,argv,ENV,file_actions=tuple(actions),setsigmask=(),setsigdef=SIGDEFS)
 need(marker_pid>1,"marker-pid")
 close_if(out_w); out_w=-1; close_if(err_w); err_w=-1; close_if(gate_r); gate_r=-1
 mi=proc_identity(marker_pid)
 need(mi[0]==marker_pid and mi[1]==os.getpid() and mi[2]==os.getpgrp() and mi[3]==os.getsid(0),"marker-topology")
 own=(b"P27E001V3|launcher=ownership|probe="+probe+b"|launcher_pid="+str(os.getpid()).encode("ascii")+b"|launcher_sid="+str(os.getsid(0)).encode("ascii")+b"|launcher_pgid="+str(os.getpgrp()).encode("ascii")+b"|launcher_start="+str(launcher_start).encode("ascii")+b"|marker_pid="+str(marker_pid).encode("ascii")+b"|marker_pgid="+str(os.getpgrp()).encode("ascii")+b"\n")
 write_bounded(3,own,checked(now(),250000000))
 release_read(4,checked(now(),1000000000)); close_if(4)
 write_bounded(gate_w,b"L",checked(now(),250000000)); close_if(gate_w); gate_w=-1
 run_start=now(); deadline=checked(run_start,delta); p=select.poll(); p.register(out_r,select.POLLIN|select.POLLHUP|select.POLLERR); p.register(err_r,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(20000):
  if not marker_reaped:
   q=wait_nohang(marker_pid)
   if q[0]==marker_pid: marker_reaped=1; marker_status=q[1]
  out_eof=read_some(out_r,outs) or out_eof; err_eof=read_some(err_r,errs) or err_eof
  if marker_reaped and out_eof and err_eof: break
  if ABORT: cleanup=1; raise Fail("outer-term")
  n=now()
  if n>=deadline: timed=1; cleanup=1; raise Fail("marker-timeout")
  p.poll(max(0,min(25,(deadline-n+999999)//1000000)))
 else: cleanup=1; raise Fail("marker-iterations")
 run_finish=now(); elapsed(run_start,run_finish,delta)
 need(marker_reaped and marker_status==0 and out_eof and err_eof and len(errs)==0,"marker-completion")
 recheck_image(pfd,sfd,pkey); need(os.getcwdb()==safe,"terminal-cwd")
 write_bounded(1,bytes(outs),checked(now(),500000000)); write_bounded(2,bytes(errs),checked(now(),500000000))
 terminal=(b"P27E001V3|launcher=terminal|probe="+probe+b"|launcher_source_sha256="+launcher_sha+b"|marker_source_sha256="+marker_sha+b"|marker_pid="+str(marker_pid).encode("ascii")+b"|marker_raw_status="+str(marker_status).encode("ascii")+b"|marker_reaped=1|marker_stdout_bytes="+str(len(outs)).encode("ascii")+b"|marker_stdout_sha256="+hashlib.sha256(outs).hexdigest().encode("ascii")+b"|marker_stdout_eof=1|marker_stderr_bytes="+str(len(errs)).encode("ascii")+b"|marker_stderr_sha256="+hashlib.sha256(errs).hexdigest().encode("ascii")+b"|marker_stderr_eof=1|timed=0|abort_seen=0|cleanup_requested=0|elapsed_ns="+str(run_finish-run_start).encode("ascii")+b"\n")
 write_bounded(3,terminal,checked(now(),500000000)); close_if(3)
except BaseException as e:
 cleanup=1
 if isinstance(e,Fail): failure=os.fsencode(str(e))
 elif isinstance(e,OSError): failure=("oserror-%d"%(e.errno if e.errno is not None else -1)).encode("ascii")
 else: failure=("exception-"+type(e).__name__).encode("ascii")
 if marker_pid>1 and not marker_reaped:
  q=wait_nohang(marker_pid)
  if q[0]==marker_pid: marker_reaped=1; marker_status=q[1]
 run_finish=now()
 request=(b"P27E001V3|launcher=cleanup_request|probe="+probe+b"|failure="+failure+b"|marker_pid="+str(marker_pid).encode("ascii")+b"|marker_raw_status="+str(marker_status).encode("ascii")+b"|marker_reaped="+str(marker_reaped).encode("ascii")+b"|timed="+str(timed).encode("ascii")+b"|abort_seen="+str(ABORT).encode("ascii")+b"\n")
 try: write_bounded(3,request,checked(now(),250000000))
 except BaseException: pass
 hold=checked(now(),1500000000)
 for unused in range(4096):
  if marker_pid>1 and not marker_reaped:
   q=wait_nohang(marker_pid)
   if q[0]==marker_pid: marker_reaped=1; marker_status=q[1]
  if out_r>=0: out_eof=read_some(out_r,outs) or out_eof
  if err_r>=0: err_eof=read_some(err_r,errs) or err_eof
  if now()>=hold: break
  time.sleep(0.001)
 finally_line=(b"P27E001V3|launcher=failure_terminal|probe="+probe+b"|launcher_source_sha256="+launcher_sha+b"|marker_source_sha256="+marker_sha+b"|marker_pid="+str(marker_pid).encode("ascii")+b"|marker_raw_status="+str(marker_status).encode("ascii")+b"|marker_reaped="+str(marker_reaped).encode("ascii")+b"|marker_stdout_bytes="+str(len(outs)).encode("ascii")+b"|marker_stdout_sha256="+hashlib.sha256(outs).hexdigest().encode("ascii")+b"|marker_stdout_eof="+str(int(out_eof)).encode("ascii")+b"|marker_stderr_bytes="+str(len(errs)).encode("ascii")+b"|marker_stderr_sha256="+hashlib.sha256(errs).hexdigest().encode("ascii")+b"|marker_stderr_eof="+str(int(err_eof)).encode("ascii")+b"|timed="+str(timed).encode("ascii")+b"|abort_seen="+str(ABORT).encode("ascii")+b"|cleanup_requested=1|elapsed_ns="+str(run_finish-run_start if run_finish>=run_start else -1).encode("ascii")+b"\n")
 try: write_bounded(3,finally_line,checked(now(),250000000))
 except BaseException: pass
 raise SystemExit(90)
finally:
 for fd in (out_r,out_w,err_r,err_w,gate_r,gate_w,pfd,sfd,3,4): close_if(fd)
COMMON LAUNCHER V3 SOURCE END
```

This block is inert documentation and was not imported, parsed, compiled,
evaluated, or executed. All launcher reads and writes are nonblocking and
deadline-bounded. It reports the actual marker PID and raw wait status. It
never fabricates reap from ECHILD, never strips a stream, and never signals.

## 6. Exact unified-marker source

The same frozen dispatcher source serves all fifteen probe IDs. A probe ID
selects exactly one closed branch; unknown and malformed IDs fail before gate
release. Every nested successful spawn is recorded by returned PID and raw
wait status. All nested processes remain in the launcher group. Cleanup sends
only exact-PID signals to still-unreaped direct children; after a child is
reaped its number is permanently removed from the signalable set.

```text
UNIFIED MARKER V3 SOURCE BEGIN
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

class Fail(Exception): pass
class Abort(BaseException): pass

def need(v,code):
 if not v: raise Fail(code)

def checked(n,d):
 need(type(n) is int and type(d) is int and n>=0 and d>0 and n<=((1<<63)-1)-d,"clock-headroom"); return n+d

def now():
 v=time.monotonic_ns(); need(type(v) is int and v>=0,"clock-negative"); return v

def elapsed(a,b,bound):
 need(type(a) is int and type(b) is int and 0<=a<=b and b-a<=bound,"elapsed-bound"); return b-a

def set_nonblock(fd):
 v=fcntl.fcntl(fd,fcntl.F_GETFL); fcntl.fcntl(fd,fcntl.F_SETFL,v|os.O_NONBLOCK)

def close_if(fd):
 if fd>=0:
  try: os.close(fd)
  except OSError: pass

def sigdefs():
 return tuple(sorted(int(x) for x in signal.valid_signals() if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))

SIGDEFS=sigdefs()

def write_bounded(fd,data,deadline):
 set_nonblock(fd); p=select.poll(); p.register(fd,select.POLLOUT|select.POLLERR|select.POLLHUP); pos=0
 for unused in range(4096):
  if pos==len(data): return
  n=now(); need(n<deadline,"write-deadline")
  try:
   z=os.write(fd,data[pos:]); need(z>0,"write-zero"); pos+=z; continue
  except BlockingIOError: pass
  except InterruptedError: continue
  p.poll(max(0,min(25,(deadline-n+999999)//1000000)))
 raise Fail("write-iterations")

def read_gate(fd,deadline):
 set_nonblock(fd); raw=bytearray(); eof=False; p=select.poll(); p.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(1024):
  for inner in range(16):
   try: x=os.read(fd,2)
   except BlockingIOError: break
   except InterruptedError: continue
   if not x: eof=True; break
   raw.extend(x); need(len(raw)<=2,"gate-cap")
  if eof: break
  n=now(); need(n<deadline,"gate-timeout"); p.poll(max(0,min(25,(deadline-n+999999)//1000000)))
 need(bytes(raw)==b"L" and eof,"gate-frame")

def wait_nohang(pid):
 for unused in range(16):
  try: return os.waitpid(pid,os.WNOHANG)
  except InterruptedError: continue
  except ChildProcessError as e: raise Fail("wait-echild") from e
 raise Fail("wait-eintr-bound")

def wait_bounded(pid,deadline):
 for unused in range(20000):
  q=wait_nohang(pid)
  if q[0]==pid: return q[1]
  n=now(); need(n<deadline,"child-wait-timeout"); time.sleep(min(0.001,(deadline-n)/1000000000.0))
 raise Fail("child-wait-iterations")

def read_child(pid,fds,deadline):
 bufs={fd:bytearray() for fd in fds}; eof={fd:False for fd in fds}; status=None; p=select.poll()
 for fd in fds: set_nonblock(fd); p.register(fd,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(20000):
  if status is None:
   q=wait_nohang(pid)
   if q[0]==pid: status=q[1]
  for fd in fds:
   if eof[fd]: continue
   for inner in range(64):
    try: x=os.read(fd,4096)
    except BlockingIOError: break
    except InterruptedError: continue
    if not x: eof[fd]=True; p.unregister(fd); break
    bufs[fd].extend(x); need(len(bufs[fd])<=CAP,"child-stream-cap")
  if status is not None and all(eof.values()): return status,tuple(bytes(bufs[fd]) for fd in fds)
  n=now(); need(n<deadline,"child-stream-timeout"); p.poll(max(0,min(25,(deadline-n+999999)//1000000)))
 raise Fail("child-stream-iterations")

def hash_fd(fd,size):
 os.lseek(fd,0,os.SEEK_SET); h=hashlib.sha256(); total=0
 for unused in range((size+1048575)//1048576+1):
  try: x=os.read(fd,min(1048576,size-total+1))
  except InterruptedError: continue
  if not x: break
  total+=len(x); need(total<=size,"hash-growth"); h.update(x)
 need(total==size,"hash-short"); return h.hexdigest().encode("ascii")

def bind_image():
 need(os.readlink(PYTHON)==b"python3.12","python-target")
 pfd=os.open(PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW); sfd=os.open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC)
 a=os.fstat(pfd); b=os.fstat(sfd); key=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(key(a)==key(b) and stat.S_ISREG(a.st_mode) and stat.S_IMODE(a.st_mode)==0o755 and a.st_nlink==1 and a.st_uid==0 and a.st_gid==0 and a.st_size==PY_BYTES,"python-image")
 need(hash_fd(pfd,PY_BYTES)==PY_SHA and hash_fd(sfd,PY_BYTES)==PY_SHA,"python-hash")
 return pfd,sfd,key(a)

def recheck_image(pfd,sfd,key):
 a=os.fstat(pfd); b=os.fstat(sfd); p=os.stat(PYRES,follow_symlinks=False); k=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(k(a)==k(b)==k(p)==key and os.readlink(PYTHON)==b"python3.12","terminal-python")
 need(hash_fd(pfd,PY_BYTES)==PY_SHA and hash_fd(sfd,PY_BYTES)==PY_SHA,"terminal-python-hash")

def bind_tool(path,size,digest):
 fd=os.open(path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW); a=os.fstat(fd); key=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(stat.S_ISREG(a.st_mode) and stat.S_IMODE(a.st_mode)==0o755 and a.st_nlink==1 and a.st_uid==0 and a.st_gid==0 and a.st_size==size,"tool-stat")
 need(hash_fd(fd,size)==digest,"tool-hash"); p=os.stat(path,follow_symlinks=False); need(key(a)==key(p),"tool-path"); return fd,key(a)

def recheck_tool(fd,path,size,digest,key):
 a=os.fstat(fd); p=os.stat(path,follow_symlinks=False); k=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(k(a)==k(p)==key and hash_fd(fd,size)==digest,"terminal-tool")

def mapped_libc():
 mfd=os.open(b"/proc/self/maps",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:
  raw=bytearray()
  for unused in range(1025):
   try: x=os.read(mfd,4096)
   except InterruptedError: continue
   if not x: break
   raw.extend(x); need(len(raw)<=4194304,"maps-cap")
  else: raise Fail("maps-iterations")
 finally: os.close(mfd)
 need(raw.endswith(b"\n") and b"\x00" not in raw,"maps-frame")
 found=set()
 for line in bytes(raw).split(b"\n")[:-1]:
  p=line.split(None,5)
  if len(p)==6 and b"x" in p[1] and p[5].startswith(b"/") and p[5].rsplit(b"/",1)[-1].startswith(b"libc.so"):
   dv=p[3].split(b":"); need(len(dv)==2 and p[4].isdigit(),"maps-device")
   found.add((p[5],os.makedev(int(dv[0],16),int(dv[1],16)),int(p[4])))
 need(len(found)==1,"libc-mapping-count")
 path,mapdev,mapino=found.pop(); need(not path.endswith(b" (deleted)"),"libc-deleted")
 fd=os.open(path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW); a=os.fstat(fd)
 need(stat.S_ISREG(a.st_mode) and a.st_dev==mapdev and a.st_ino==mapino and a.st_nlink==1,"libc-map-open")
 digest=hash_fd(fd,a.st_size)
 z=os.fstat(fd); need((a.st_dev,a.st_ino,a.st_mode,a.st_nlink,a.st_uid,a.st_gid,a.st_size)==(z.st_dev,z.st_ino,z.st_mode,z.st_nlink,z.st_uid,z.st_gid,z.st_size),"libc-held")
 return fd,path,mapdev,mapino,(a.st_dev,a.st_ino,a.st_mode,a.st_nlink,a.st_uid,a.st_gid,a.st_size),digest

def recheck_libc(fd,path,mapdev,mapino,key,digest):
 a=os.fstat(fd); p=os.stat(path,follow_symlinks=False); k=lambda s:(s.st_dev,s.st_ino,s.st_mode,s.st_nlink,s.st_uid,s.st_gid,s.st_size)
 need(k(a)==k(p)==key and a.st_dev==mapdev and a.st_ino==mapino,"terminal-libc")
 need(hash_fd(fd,a.st_size)==digest,"terminal-libc-hash")

def abort_handler(signum,frame): raise Abort("group-term")

need(len(sys.argv)>=5 and sys.argv[0]=="-c","argv-count")
ID=os.fsencode(sys.argv[1]); SAFE=os.fsencode(sys.argv[2]); MARKER_SHA=os.fsencode(sys.argv[3]); DELTA=int(sys.argv[4]); EXTRA=tuple(os.fsencode(x) for x in sys.argv[5:])
IDS=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
need(ID in IDS and 1000000000<=DELTA<=10000000000,"probe-args")
SOURCE=os.fsencode(sys.orig_argv[8]); need(hashlib.sha256(SOURCE).hexdigest().encode("ascii")==MARKER_SHA,"marker-source")
need(dict(os.environb)==ENV and sys.executable==PYTHON.decode("ascii"),"runtime")
need(sys.orig_argv[:8]==[PYTHON.decode("ascii"),"-I","-S","-B","-P","-X","utf8","-c"],"vector")
need(sys.flags.isolated==1 and sys.flags.ignore_environment==1 and sys.flags.no_site==1 and sys.flags.no_user_site==1 and sys.flags.dont_write_bytecode==1 and sys.flags.safe_path==1 and sys.flags.utf8_mode==1 and sys.flags.hash_randomization==1,"flags")
need(os.getcwdb()==SAFE and SAFE.startswith(b"/tmp/p27-e001-host-v3-"),"cwd")
need(resource.getrlimit(resource.RLIMIT_CPU)==(3,3) and resource.getrlimit(resource.RLIMIT_AS)==(268435456,268435456) and resource.getrlimit(resource.RLIMIT_FSIZE)==(1048576,1048576) and resource.getrlimit(resource.RLIMIT_CORE)==(0,0) and resource.getrlimit(resource.RLIMIT_NOFILE)==(4096,1048576),"limits")
fds=[]; nodes=[]
for fd in range(4096):
 try: fcntl.fcntl(fd,fcntl.F_GETFD)
 except OSError as e:
  if e.errno==errno.EBADF: continue
  raise
 fds.append(fd); s=os.fstat(fd); need(stat.S_ISFIFO(s.st_mode),"initial-fd-type"); nodes.append((s.st_dev,s.st_ino))
need(fds==[0,1,2,3] and len(set(nodes))==4,"initial-fds")
signal.signal(signal.SIGTERM,abort_handler); signal.signal(signal.SIGINT,abort_handler)
read_gate(3,checked(now(),1000000000)); os.close(3)

rows=[]; live=set(); pids=[]; statuses=[]; spawned=0; reaped=0; owned=[]; libc_fd=-1; py_fd=self_fd=env_fd=bash_fd=-1

def row(k,v):
 if type(v) is int: v=str(v).encode("ascii")
 elif type(v) is str: v=v.encode("ascii")
 need(type(k) is bytes and type(v) is bytes and k and v and b"|" not in k+v and b"\n" not in k+v and b"\r" not in k+v,"row-frame")
 rows.append(b"P27E001V3|probe="+ID+b"|"+k+b"="+v)

def spawn(argv,env=ENV,file_actions=()):
 global spawned
 pid=os.posix_spawn(argv[0],argv,env,file_actions=file_actions,setsigmask=(),setsigdef=SIGDEFS)
 need(pid>1,"nested-pid"); live.add(pid); pids.append(pid); spawned+=1; return pid

def reaped_status(pid,status):
 global reaped
 need(pid in live,"reap-membership"); live.remove(pid); statuses.append(status); reaped+=1

def cleanup_live():
 for pid in tuple(sorted(live)):
  q=wait_nohang(pid)
  if q[0]==pid: reaped_status(pid,q[1])
 for pid in tuple(sorted(live)):
  try: os.kill(pid,signal.SIGTERM)
  except ProcessLookupError: pass
 term=checked(now(),100000000)
 for unused in range(256):
  for pid in tuple(sorted(live)):
   q=wait_nohang(pid)
   if q[0]==pid: reaped_status(pid,q[1])
  if not live or now()>=term: break
 for pid in tuple(sorted(live)):
  q=wait_nohang(pid)
  if q[0]==pid: reaped_status(pid,q[1]); continue
  try: os.kill(pid,signal.SIGKILL)
  except ProcessLookupError: pass
 hard=checked(now(),250000000)
 for unused in range(512):
  for pid in tuple(sorted(live)):
   q=wait_nohang(pid)
   if q[0]==pid: reaped_status(pid,q[1])
  if not live or now()>=hard: break
 return not live

try:
 if ID==b"P00":
  need(len(EXTRA)==0,"p00-extra")
  synthetic=b"#"*251414; need(len(synthetic)==251414 and b"\x00" not in synthetic,"p00-source")
  argv=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",synthetic,b"watchdog")
  returned=0; e2big=0
  try:
   pid=spawn(argv); returned=1; status=wait_bounded(pid,checked(now(),2000000000)); reaped_status(pid,status); need(status==0,"p00-status")
  except OSError as e:
   need(e.errno==errno.E2BIG,"p00-errno"); e2big=1
  need(returned+e2big==1,"p00-branch")
  row(b"source_item_bytes",251414); row(b"source_item_accounted_bytes",251415); row(b"source_item_sha256",hashlib.sha256(synthetic).hexdigest()); row(b"arg_max",os.sysconf("SC_ARG_MAX")); row(b"spawn_returned",returned); row(b"e2big",e2big); row(b"transport_feasible",returned)
 elif ID==b"P01D":
  need(len(EXTRA)==0,"p01d-extra")
  py_fd,self_fd,pykey=bind_image(); libc_fd,lpath,lmapdev,lmapino,lkey,ldigest=mapped_libc(); conf=os.confstr("CS_GNU_LIBC_VERSION"); need(type(conf) is str and conf.isascii(),"libc-conf")
  row(b"python_image_dev",pykey[0]); row(b"python_image_ino",pykey[1]); row(b"python_image_mode",format(pykey[2],"o")); row(b"python_image_nlink",pykey[3]); row(b"python_image_uid",pykey[4]); row(b"python_image_gid",pykey[5]); row(b"python_image_bytes",pykey[6]); row(b"python_image_sha256",PY_SHA)
  row(b"libc_confstr_hex",conf.encode("ascii").hex()); row(b"libc_path_hex",lpath.hex()); row(b"libc_map_dev",lmapdev); row(b"libc_map_ino",lmapino); row(b"libc_open_dev",lkey[0]); row(b"libc_open_ino",lkey[1]); row(b"libc_mode",format(lkey[2],"o")); row(b"libc_nlink",lkey[3]); row(b"libc_uid",lkey[4]); row(b"libc_gid",lkey[5]); row(b"libc_bytes",lkey[6]); row(b"libc_sha256",ldigest)
  row(b"posix_spawn_module",os.posix_spawn.__module__); row(b"posix_spawn_name",os.posix_spawn.__name__); row(b"posix_spawn_type",type(os.posix_spawn).__name__); row(b"backend_surface",b"cpython-posix-builtin-plus-mapped-open-libc"); row(b"spawn_premise_satisfied",0)
  recheck_image(py_fd,self_fd,pykey); recheck_libc(libc_fd,lpath,lmapdev,lmapino,lkey,ldigest)
 elif ID==b"P01C":
  need(len(EXTRA)==13,"p01c-extra")
  expected=(bytes.fromhex(EXTRA[0].decode("ascii")),int(EXTRA[1]),int(EXTRA[2]),int(EXTRA[3],8),int(EXTRA[4]),int(EXTRA[5]),int(EXTRA[6]),int(EXTRA[7]),EXTRA[8],bytes.fromhex(EXTRA[9].decode("ascii")).decode("ascii"),int(EXTRA[10]),int(EXTRA[11]),EXTRA[12])
  py_fd,self_fd,pykey=bind_image(); libc_fd,lpath,lmapdev,lmapino,lkey,ldigest=mapped_libc(); conf=os.confstr("CS_GNU_LIBC_VERSION")
  actual=(lpath,lmapdev,lmapino,lkey[2],lkey[3],lkey[4],lkey[5],lkey[6],ldigest,conf,pykey[0],pykey[1],PY_SHA); need(actual==expected,"p01c-seal")
  child=b'import os;os.write(1,("%d,%d,%d\\n"%(os.getpid(),os.getsid(0),os.getpgid(0))).encode("ascii"))'
  r,w=os.pipe2(os.O_CLOEXEC); owned.extend((r,w)); actions=((os.POSIX_SPAWN_DUP2,w,1),(os.POSIX_SPAWN_CLOSE,r),(os.POSIX_SPAWN_CLOSE,w))
  pid=spawn((PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",child),file_actions=actions); os.close(w); owned.remove(w); status,data=read_child(pid,(r,),checked(now(),2000000000)); os.close(r); owned.remove(r); reaped_status(pid,status)
  raw=data[0]; need(status==0 and raw.endswith(b"\n") and raw.count(b"\n")==1,"p01c-child-frame"); fields=raw[:-1].split(b","); need(len(fields)==3 and all(x.isdigit() for x in fields),"p01c-child-fields"); cp,cs,cg=(int(x) for x in fields); need(cp==pid and cs==os.getsid(0) and cg==os.getpgrp(),"p01c-child-topology")
  row(b"python_image_dev",pykey[0]); row(b"python_image_ino",pykey[1]); row(b"python_image_sha256",PY_SHA); row(b"libc_path_hex",lpath.hex()); row(b"libc_map_dev",lmapdev); row(b"libc_map_ino",lmapino); row(b"libc_sha256",ldigest); row(b"libc_confstr_hex",conf.encode("ascii").hex()); row(b"posix_spawn_module",os.posix_spawn.__module__); row(b"posix_spawn_name",os.posix_spawn.__name__); row(b"child_raw_bytes",len(raw)); row(b"child_raw_sha256",hashlib.sha256(raw).hexdigest()); row(b"child_pid",cp); row(b"child_sid",cs); row(b"child_pgid",cg); row(b"spawn_premise_satisfied",1)
  recheck_image(py_fd,self_fd,pykey); recheck_libc(libc_fd,lpath,lmapdev,lmapino,lkey,ldigest)
 elif ID==b"P02":
  need(len(EXTRA)==0,"p02-extra")
  envitems=[(k+b"="+ENV[k]).hex() for k in sorted(ENV)]; f=[]; nodes=[]
  for fd in range(4096):
   try: flags=fcntl.fcntl(fd,fcntl.F_GETFD)
   except OSError as e:
    if e.errno==errno.EBADF: continue
    raise
   f.append(fd); s=os.fstat(fd); need(stat.S_ISFIFO(s.st_mode),"p02-fd-type"); nodes.append((s.st_dev,s.st_ino,flags))
  need(f==[0,1,2] and len(set((x[0],x[1]) for x in nodes))==3,"p02-fds")
  limits=((b"rlimit_cpu",resource.RLIMIT_CPU,(3,3)),(b"rlimit_as",resource.RLIMIT_AS,(268435456,268435456)),(b"rlimit_fsize",resource.RLIMIT_FSIZE,(1048576,1048576)),(b"rlimit_core",resource.RLIMIT_CORE,(0,0)),(b"rlimit_nofile",resource.RLIMIT_NOFILE,(4096,1048576)))
  row(b"environment",b",".join(x.encode("ascii") for x in envitems)); row(b"environment_count",10); row(b"cwd_hex",SAFE.hex()); row(b"flags",b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1"); row(b"fds",b"0,1,2"); row(b"fd_nodes",b",".join(("%d:%d:%d"%x).encode("ascii") for x in nodes))
  for key,which,want in limits:
   got=resource.getrlimit(which); need(got==want,"p02-limit"); row(key,("%d,%d"%got).encode("ascii"))
  np=resource.getrlimit(resource.RLIMIT_NPROC); need(4<=np[0]<=32 and (np[1]==resource.RLIM_INFINITY or np[0]<=np[1]),"p02-nproc"); row(b"rlimit_nproc",("%d,%d"%np).encode("ascii"))
 elif ID==b"P03":
  need(len(EXTRA)==0,"p03-extra")
  before=resource.getrlimit(resource.RLIMIT_NOFILE); need(before==(4096,1048576),"p03-before"); resource.setrlimit(resource.RLIMIT_NOFILE,(64,1048576)); held=[]; hit=0
  try:
   for unused in range(64):
    try: r,w=os.pipe2(os.O_CLOEXEC); held.extend((r,w))
    except OSError as e: need(e.errno==errno.EMFILE,"p03-errno"); hit=1; break
  finally:
   for fd in held: close_if(fd)
  need(hit==1 and resource.getrlimit(resource.RLIMIT_NOFILE)==(64,1048576),"p03-emfile")
  remain=[]
  for fd in range(64):
   try: fcntl.fcntl(fd,fcntl.F_GETFD)
   except OSError as e:
    if e.errno==errno.EBADF: continue
    raise
   remain.append(fd)
  need(remain==[0,1,2],"p03-after")
  row(b"soft_before",4096); row(b"hard_before",1048576); row(b"soft_test",64); row(b"opened_fds",len(held)); row(b"emfile",1); row(b"fds_after",b"0,1,2")
 elif ID==b"P04":
  need(len(EXTRA)==0,"p04-extra")
  defs=SIGDEFS; signal.pthread_sigmask(signal.SIG_SETMASK,set())
  for n in defs: signal.signal(n,signal.SIG_DFL)
  mask=signal.pthread_sigmask(signal.SIG_BLOCK,set()); need(mask==set(),"p04-mask")
  for n in defs: need(signal.getsignal(n)==signal.SIG_DFL,"p04-default")
  csv=b",".join(str(x).encode("ascii") for x in defs)
  row(b"valid_signal_count",len(signal.valid_signals())); row(b"default_signal_count",len(defs)); row(b"defaults_csv",csv); row(b"defaults_sha256",hashlib.sha256(csv).hexdigest()); row(b"mask_empty",1); row(b"normalization_complete",1)
 elif ID==b"P05":
  need(len(EXTRA)==0,"p05-extra")
  r,w=os.pipe2(os.O_CLOEXEC); owned.extend((r,w)); os.set_inheritable(r,True)
  child=b'import os,sys;os.read(int(sys.argv[1]),1);raise SystemExit(23)'
  pid=spawn((PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",child,str(r).encode("ascii"))); os.close(r); owned.remove(r)
  z=wait_nohang(pid); need(z==(0,0),"p05-wnohang")
  old=signal.getsignal(signal.SIGALRM)
  def alarm(signum,frame): raise InterruptedError(errno.EINTR,"bounded-probe")
  signal.signal(signal.SIGALRM,alarm); signal.setitimer(signal.ITIMER_REAL,0.02); intr=0
  try:
   try: os.waitpid(pid,0)
   except InterruptedError as e: need(e.errno==errno.EINTR,"p05-eintr-errno"); intr=1
  finally:
   signal.setitimer(signal.ITIMER_REAL,0.0); signal.signal(signal.SIGALRM,old)
  need(intr==1,"p05-eintr"); need(os.write(w,b"x")==1,"p05-release"); os.close(w); owned.remove(w)
  status=wait_bounded(pid,checked(now(),1000000000)); reaped_status(pid,status); need(os.WIFEXITED(status) and os.WEXITSTATUS(status)==23,"p05-exit")
  echild=0
  try: os.waitpid(pid,os.WNOHANG)
  except ChildProcessError as e: need(e.errno==errno.ECHILD,"p05-echild-errno"); echild=1
  child2=b'import os,signal;os.kill(os.getpid(),signal.SIGTERM)'
  pid2=spawn((PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",child2)); status2=wait_bounded(pid2,checked(now(),1000000000)); reaped_status(pid2,status2); need(os.WIFSIGNALED(status2) and os.WTERMSIG(status2)==signal.SIGTERM,"p05-signal")
  row(b"wnohang_zero",1); row(b"eintr",intr); row(b"exit_pid",pid); row(b"exit_raw",status); row(b"exit_code",23); row(b"echild",echild); row(b"signal_pid",pid2); row(b"signal_raw",status2); row(b"term_signal",int(signal.SIGTERM))
 elif ID==b"P06":
  need(len(EXTRA)==0,"p06-extra")
  info=time.get_clock_info("monotonic"); res=time.clock_getres(time.CLOCK_MONOTONIC); res_ns=max(1,int(res*1000000000.0+0.999999999)); vals=[time.monotonic_ns() for unused in range(4096)]
  need(all(type(x) is int and x>=0 for x in vals) and all(vals[i]<=vals[i+1] for i in range(len(vals)-1)),"p06-order"); deltas=[vals[i+1]-vals[i] for i in range(len(vals)-1) if vals[i+1]>vals[i]]; need(deltas,"p06-progress")
  limit=(1<<63)-1; start_clock=vals[0]; end_clock=vals[-1]; sample_elapsed=elapsed(start_clock,end_clock,DELTA); need(start_clock<=limit-1000000000,"p06-headroom"); deadline=start_clock+1000000000
  row(b"implementation_hex",info.implementation.encode("ascii").hex()); row(b"adjustable",int(info.adjustable)); row(b"monotonic",int(info.monotonic)); row(b"declared_resolution_ns",res_ns); row(b"observed_min_delta_ns",min(deltas)); row(b"start_ns",start_clock); row(b"end_ns",end_clock); row(b"elapsed_ns",sample_elapsed); row(b"headroom_ns",limit-start_clock); row(b"deadline_ns",deadline); row(b"deadline_checked",1)
 elif ID==b"P07":
  need(len(EXTRA)==0,"p07-extra")
  r,w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK); d=-1; owned.extend((r,w))
  try:
   rc=int(bool(fcntl.fcntl(r,fcntl.F_GETFD)&fcntl.FD_CLOEXEC)); wc=int(bool(fcntl.fcntl(w,fcntl.F_GETFD)&fcntl.FD_CLOEXEC)); rn=int(bool(fcntl.fcntl(r,fcntl.F_GETFL)&os.O_NONBLOCK)); wn=int(bool(fcntl.fcntl(w,fcntl.F_GETFL)&os.O_NONBLOCK))
   empty=0
   try: os.read(r,1)
   except OSError as e: need(e.errno in (errno.EAGAIN,errno.EWOULDBLOCK),"p07-empty-errno"); empty=1
   p=select.poll(); p.register(r,select.POLLIN|select.POLLHUP|select.POLLERR); initial=int(bool(p.poll(0))); need(initial==0,"p07-initial")
   need(os.write(w,b"x")==1,"p07-write"); events=p.poll(1000); need(events,"p07-ready"); byte=os.read(r,1); need(byte==b"x","p07-byte")
   d=os.dup(w); owned.append(d); os.close(w); owned.remove(w); w=-1; before=0
   try: before=int(os.read(r,1)==b"")
   except OSError as e: need(e.errno in (errno.EAGAIN,errno.EWOULDBLOCK),"p07-before-errno")
   need(before==0,"p07-before"); os.close(d); owned.remove(d); d=-1
   events=p.poll(1000); hup=int(any(fd==r and mask&select.POLLHUP for fd,mask in events)); eof=int(os.read(r,1)==b""); need((rc,wc,rn,wn,empty,hup,eof)==(1,1,1,1,1,1,1),"p07-observation")
   row(b"read_cloexec",rc); row(b"write_cloexec",wc); row(b"read_nonblock",rn); row(b"write_nonblock",wn); row(b"empty_eagain",empty); row(b"initial_readable",initial); row(b"byte_hex",byte.hex()); row(b"eof_before_last_writer",before); row(b"hup_after_last_writer",hup); row(b"eof_after_last_writer",eof)
  finally:
   for fd in (r,w,d):
    if fd>=0:
     close_if(fd)
     if fd in owned: owned.remove(fd)
 elif ID==b"P08":
  need(len(EXTRA)==0,"p08-extra")
  rr,rw=os.pipe2(os.O_CLOEXEC); gr,gw=os.pipe2(os.O_CLOEXEC); owned.extend((rr,rw,gr,gw)); os.set_inheritable(rw,True); os.set_inheritable(gr,True)
  child=b'import os,sys;os.write(int(sys.argv[1]),b"R");os.read(int(sys.argv[2]),1)'
  pid=spawn((PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",child,str(rw).encode("ascii"),str(gr).encode("ascii"))); os.close(rw); owned.remove(rw); os.close(gr); owned.remove(gr)
  set_nonblock(rr); ready=b""; ready_deadline=checked(now(),500000000); poll=select.poll(); poll.register(rr,select.POLLIN|select.POLLHUP)
  for unused in range(512):
   try: ready+=os.read(rr,1)
   except BlockingIOError: pass
   except InterruptedError: continue
   if ready==b"R": break
   n=now(); need(n<ready_deadline,"p08-ready-timeout"); poll.poll(max(0,min(10,(ready_deadline-n+999999)//1000000)))
  need(ready==b"R","p08-ready"); os.close(rr); owned.remove(rr)
  sid=os.getsid(pid); pgid=os.getpgid(pid); need(sid==os.getsid(0) and pgid==os.getpgrp(),"p08-topology"); os.kill(pid,0)
  need(os.write(gw,b"G")==1,"p08-release"); os.close(gw); owned.remove(gw); status=wait_bounded(pid,checked(now(),1000000000)); reaped_status(pid,status); need(status==0,"p08-status")
  absent=0
  try: os.kill(pid,0)
  except ProcessLookupError as e: need(e.errno==errno.ESRCH,"p08-esrch-errno"); absent=1
  need(absent==1,"p08-post")
  row(b"child_pid",pid); row(b"child_sid",sid); row(b"child_pgid",pgid); row(b"marker_sid",os.getsid(0)); row(b"marker_pgid",os.getpgrp()); row(b"live_pid_zero",1); row(b"raw_status",status); row(b"post_pid_esrch",1); row(b"reuse_proof",0)
 elif ID==b"P09":
  need(len(EXTRA)==0,"p09-extra")
  rr,rw=os.pipe2(os.O_CLOEXEC); hr,hw=os.pipe2(os.O_CLOEXEC); owned.extend((rr,rw,hr,hw)); os.set_inheritable(rw,True); os.set_inheritable(hr,True)
  child=b'import os,sys;os.write(int(sys.argv[1]),b"R");os.read(int(sys.argv[2]),1)'
  pid=spawn((PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",child,str(rw).encode("ascii"),str(hr).encode("ascii"))); os.close(rw); owned.remove(rw); os.close(hr); owned.remove(hr)
  set_nonblock(rr); ready=b""; rd=checked(now(),500000000); poll=select.poll(); poll.register(rr,select.POLLIN|select.POLLHUP)
  for unused in range(512):
   try: ready+=os.read(rr,1)
   except BlockingIOError: pass
   except InterruptedError: continue
   if ready==b"R": break
   n=now(); need(n<rd,"p09-ready-timeout"); poll.poll(max(0,min(10,(rd-n+999999)//1000000)))
  need(ready==b"R","p09-ready"); os.close(rr); owned.remove(rr); pgid=os.getpgid(pid); need(pgid==os.getpgrp(),"p09-group")
  begin=now(); q=wait_nohang(pid); need(q==(0,0),"p09-pre-signal"); os.kill(pid,signal.SIGKILL); status=wait_bounded(pid,checked(begin,1000000000)); end=now(); duration=elapsed(begin,end,1000000000); reaped_status(pid,status); os.close(hw); owned.remove(hw)
  need(os.WIFSIGNALED(status) and os.WTERMSIG(status)==signal.SIGKILL,"p09-status")
  row(b"child_pid",pid); row(b"child_pgid",pgid); row(b"signal",int(signal.SIGKILL)); row(b"raw_status",status); row(b"reap_start_ns",begin); row(b"reap_end_ns",end); row(b"reap_elapsed_ns",duration); row(b"reaped",1)
 elif ID==b"P10":
  need(len(EXTRA)==0,"p10-extra")
  child=b'import os;os.write(1,("%d,%d\\n"%(os.getpid(),os.getpgid(0))).encode("ascii"))'; gotp=[]; gotg=[]; gots=[]
  for sample in range(16):
   r,w=os.pipe2(os.O_CLOEXEC); owned.extend((r,w)); actions=((os.POSIX_SPAWN_DUP2,w,1),(os.POSIX_SPAWN_CLOSE,r),(os.POSIX_SPAWN_CLOSE,w))
   pid=spawn((PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"-c",child),file_actions=actions); os.close(w); owned.remove(w); status,data=read_child(pid,(r,),checked(now(),1000000000)); os.close(r); owned.remove(r); reaped_status(pid,status); raw=data[0]
   need(status==0 and raw.endswith(b"\n") and raw.count(b"\n")==1,"p10-frame"); fields=raw[:-1].split(b","); need(len(fields)==2 and all(x.isdigit() for x in fields),"p10-fields"); cp,cg=(int(x) for x in fields); need(cp==pid and cg==os.getpgrp(),"p10-topology"); gotp.append(cp); gotg.append(cg); gots.append(status)
  row(b"sample_count",16); row(b"pids",b",".join(str(x).encode("ascii") for x in gotp)); row(b"pgids",b",".join(str(x).encode("ascii") for x in gotg)); row(b"statuses",b",".join(str(x).encode("ascii") for x in gots)); row(b"pid_duplicates",len(gotp)-len(set(gotp))); row(b"group_is_single_owned_launcher_group",1); row(b"reuse_proof",0)
 elif ID==b"P11":
  need(len(EXTRA)==0,"p11-extra")
  status_fd=os.open(b"/proc/self/status",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
  try:
   status_raw=bytearray()
   for unused in range(257):
    try: x=os.read(status_fd,4096)
    except InterruptedError: continue
    if not x: break
    status_raw.extend(x); need(len(status_raw)<=1048576,"p11-status-cap")
  finally: os.close(status_fd)
  caplines=[x for x in bytes(status_raw).split(b"\n") if x.startswith(b"CapEff:\t")]; need(len(caplines)==1,"p11-capeff-line"); caphex=caplines[0].split(b"\t",1)[1]; need(caphex and all(c in b"0123456789abcdefABCDEF" for c in caphex),"p11-capeff"); cap=int(caphex,16); cap_fowner=int(bool(cap&(1<<3)))
  dfd=os.open(b".",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW); owned.append(dfd); ds=os.fstat(dfd); need(stat.S_ISDIR(ds.st_mode) and stat.S_IMODE(ds.st_mode)==0o700 and ds.st_uid==0 and ds.st_gid==0,"p11-dir")
  anchor=-1; noatime=-1; created=None; removed=0
  try:
   anchor=os.open(b"target",os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600,dir_fd=dfd); owned.append(anchor); st=os.fstat(anchor); created=(st.st_dev,st.st_ino); need(stat.S_ISREG(st.st_mode) and st.st_nlink==1 and st.st_uid==0 and st.st_gid==0,"p11-create")
   need(os.write(anchor,b"x")==1,"p11-write"); os.fsync(anchor); os.utime(b"target",ns=(1000000000,1000000000),dir_fd=dfd,follow_symlinks=False); os.chown(b"target",65534,65534,dir_fd=dfd,follow_symlinks=False)
   opened=b""; unchanged=0
   try:
    noatime=os.open(b"target",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW|os.O_NOATIME,dir_fd=dfd); owned.append(noatime); opened=b"OK"; need(os.read(noatime,1)==b"x","p11-read"); os.close(noatime); owned.remove(noatime); noatime=-1
    cur=os.stat(b"target",dir_fd=dfd,follow_symlinks=False); unchanged=int(cur.st_atime_ns==1000000000); need(cap_fowner==1 and unchanged==1,"p11-noatime")
   except OSError as e:
    need(e.errno==errno.EPERM and cap_fowner==0,"p11-eperm"); opened=b"EPERM"
   held=os.fstat(anchor); path=os.stat(b"target",dir_fd=dfd,follow_symlinks=False); need((held.st_dev,held.st_ino)==created==(path.st_dev,path.st_ino) and held.st_nlink==path.st_nlink==1 and stat.S_ISREG(path.st_mode),"p11-pre-unlink")
   os.unlink(b"target",dir_fd=dfd); removed=1; held2=os.fstat(anchor); need((held2.st_dev,held2.st_ino)==created and held2.st_nlink==0,"p11-held-after")
   absent=0
   try: os.stat(b"target",dir_fd=dfd,follow_symlinks=False)
   except FileNotFoundError: absent=1
   need(absent==1,"p11-path-after")
   row(b"capeff_hex",caphex.lower()); row(b"cap_fowner",cap_fowner); row(b"open_result",opened); row(b"atime_unchanged",unchanged); row(b"created_dev",created[0]); row(b"created_ino",created[1]); row(b"cleanup_unlinked",1); row(b"cleanup_identity_observed",1); row(b"atomic_unlink_proof",0); row(b"scope_single_inode",1)
  finally:
   close_if(noatime)
   if noatime in owned: owned.remove(noatime)
   if created is not None and not removed:
    try:
     held=os.fstat(anchor); path=os.stat(b"target",dir_fd=dfd,follow_symlinks=False)
     if (held.st_dev,held.st_ino)==created==(path.st_dev,path.st_ino) and path.st_nlink==1 and stat.S_ISREG(path.st_mode): os.unlink(b"target",dir_fd=dfd)
    except FileNotFoundError: pass
   close_if(anchor)
   if anchor in owned: owned.remove(anchor)
   close_if(dfd)
   if dfd in owned: owned.remove(dfd)
 elif ID==b"P12":
  need(len(EXTRA)==0,"p12-extra")
  env_fd,env_key=bind_tool(ENV_TOOL,ENV_TOOL_BYTES,ENV_TOOL_SHA); bash_fd,bash_key=bind_tool(BASH_TOOL,BASH_TOOL_BYTES,BASH_TOOL_SHA)
  command=b'exec /usr/bin/env -i LANG=C LC_ALL=C PATH=/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONIOENCODING=UTF-8:strict PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 PYTHONUTF8=1 TZ=UTC /root/miniconda3/bin/python3 -I -S -B -P -X utf8 -c "$1" "$2"'
  child=b'import os,sys;E={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"};assert dict(os.environb)==E and b"_" not in os.environb and sys.flags.isolated==1 and sys.flags.no_site==1 and sys.flags.dont_write_bytecode==1 and sys.flags.safe_path==1 and sys.flags.utf8_mode==1 and os.getcwdb()==os.fsencode(sys.argv[1]);R=("%d\\n%d\\n%d\\n%s\\n%s\\n%s\\n"%(os.getpid(),os.getsid(0),os.getpgid(0),os.fsencode(sys.executable).hex(),",".join((k+b"="+E[k]).hex() for k in sorted(E)),os.getcwdb().hex())).encode("ascii");os.write(1,R)'
  r,w=os.pipe2(os.O_CLOEXEC); owned.extend((r,w)); actions=((os.POSIX_SPAWN_DUP2,w,1),(os.POSIX_SPAWN_CLOSE,r),(os.POSIX_SPAWN_CLOSE,w)); argv=(b"/usr/bin/env",b"-i",b"/usr/bin/bash",b"--noprofile",b"--norc",b"-c",command,b"p27-e001-v3-chain",child,SAFE)
  pid=spawn(argv,env={},file_actions=actions); os.close(w); owned.remove(w); status,data=read_child(pid,(r,),checked(now(),2000000000)); os.close(r); owned.remove(r); reaped_status(pid,status); raw=data[0]
  need(status==0 and raw.endswith(b"\n") and b"\r" not in raw and b"\x00" not in raw,"p12-frame"); lines=raw.split(b"\n"); need(len(lines)==7 and lines[-1]==b"" and all(lines[:-1]),"p12-lines"); cp,cs,cg=(int(lines[i]) for i in range(3)); need(cp==pid and cs==os.getsid(0) and cg==os.getpgrp(),"p12-topology"); need(bytes.fromhex(lines[3].decode("ascii"))==PYTHON,"p12-python")
  want=b",".join((k+b"="+ENV[k]).hex().encode("ascii") for k in sorted(ENV)); need(lines[4]==want and bytes.fromhex(lines[5].decode("ascii"))==SAFE,"p12-observation")
  recheck_tool(env_fd,ENV_TOOL,ENV_TOOL_BYTES,ENV_TOOL_SHA,env_key); recheck_tool(bash_fd,BASH_TOOL,BASH_TOOL_BYTES,BASH_TOOL_SHA,bash_key)
  row(b"env_dev",env_key[0]); row(b"env_ino",env_key[1]); row(b"env_sha256",ENV_TOOL_SHA); row(b"bash_dev",bash_key[0]); row(b"bash_ino",bash_key[1]); row(b"bash_sha256",BASH_TOOL_SHA); row(b"child_raw_bytes",len(raw)); row(b"child_raw_sha256",hashlib.sha256(raw).hexdigest()); row(b"child_pid",cp); row(b"child_sid",cs); row(b"child_pgid",cg); row(b"executable_hex",lines[3]); row(b"environment",lines[4]); row(b"environment_count",10); row(b"underscore_absent",1); row(b"cwd_hex",lines[5]); row(b"real_payload_invoked",0); row(b"raw_status",status)
 elif ID==b"P13":
  need(len(EXTRA)==0,"p13-extra")
  dfd=os.open(b".",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW); owned.append(dfd); ds=os.fstat(dfd); need(stat.S_ISDIR(ds.st_mode) and stat.S_IMODE(ds.st_mode)==0o700 and ds.st_uid==0 and ds.st_gid==0,"p13-dir")
  anchor=-1; created=None; a_present=0; b_present=0
  try:
   anchor=os.open(b"a",os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600,dir_fd=dfd); owned.append(anchor); st=os.fstat(anchor); created=(st.st_dev,st.st_ino); need(stat.S_ISREG(st.st_mode) and st.st_nlink==1,"p13-create")
   need(os.write(anchor,b"P27E001\n")==8,"p13-write"); os.fsync(anchor); a_present=1
   os.link(b"a",b"b",src_dir_fd=dfd,dst_dir_fd=dfd,follow_symlinks=False); b_present=1
   held=os.fstat(anchor); sa=os.stat(b"a",dir_fd=dfd,follow_symlinks=False); sb=os.stat(b"b",dir_fd=dfd,follow_symlinks=False); need((held.st_dev,held.st_ino)==created==(sa.st_dev,sa.st_ino)==(sb.st_dev,sb.st_ino) and held.st_nlink==sa.st_nlink==sb.st_nlink==2,"p13-link")
   os.unlink(b"a",dir_fd=dfd); a_present=0; old_absent=0
   try: os.stat(b"a",dir_fd=dfd,follow_symlinks=False)
   except FileNotFoundError: old_absent=1
   held=os.fstat(anchor); sb=os.stat(b"b",dir_fd=dfd,follow_symlinks=False); preserved=int((held.st_dev,held.st_ino)==created==(sb.st_dev,sb.st_ino) and held.st_nlink==sb.st_nlink==1); need(old_absent==1 and preserved==1,"p13-transfer")
   os.fsync(dfd); held=os.fstat(anchor); sb=os.stat(b"b",dir_fd=dfd,follow_symlinks=False); need((held.st_dev,held.st_ino)==created==(sb.st_dev,sb.st_ino),"p13-pre-unlink")
   os.unlink(b"b",dir_fd=dfd); b_present=0; held=os.fstat(anchor); need((held.st_dev,held.st_ino)==created and held.st_nlink==0,"p13-held-after"); new_absent=0
   try: os.stat(b"b",dir_fd=dfd,follow_symlinks=False)
   except FileNotFoundError: new_absent=1
   need(new_absent==1,"p13-absent")
   row(b"file_fsync_returned",1); row(b"hardlink_noreplace_returned",1); row(b"old_absent",old_absent); row(b"inode_preserved",preserved); row(b"dir_fsync_returned",1); row(b"post_unlink_absent",new_absent); row(b"created_dev",created[0]); row(b"created_ino",created[1]); row(b"cleanup_unlinked",1); row(b"cleanup_identity_observed",1); row(b"atomic_unlink_proof",0); row(b"durability_proof",0); row(b"rename_atomicity_proof",0); row(b"immutability_proof",0)
  finally:
   if created is not None:
    for name,present in ((b"a",a_present),(b"b",b_present)):
     if present:
      try:
       held=os.fstat(anchor); path=os.stat(name,dir_fd=dfd,follow_symlinks=False)
       if (held.st_dev,held.st_ino)==created==(path.st_dev,path.st_ino) and stat.S_ISREG(path.st_mode): os.unlink(name,dir_fd=dfd)
      except FileNotFoundError: pass
   close_if(anchor)
   if anchor in owned: owned.remove(anchor)
   close_if(dfd)
   if dfd in owned: owned.remove(dfd)
 else: raise Fail("unreachable-probe")

 need(not live and spawned==reaped,"child-census")
 marker_pid=os.getpid(); marker_sid=os.getsid(0); marker_pgid=os.getpgrp(); need(marker_pgid==marker_sid and marker_pid!=marker_pgid,"marker-group")
 row(b"marker_source_sha256",MARKER_SHA); row(b"marker_pid",marker_pid); row(b"marker_sid",marker_sid); row(b"marker_pgid",marker_pgid); row(b"children_spawned",spawned); row(b"children_reaped",reaped); row(b"child_pids",b",".join(str(x).encode("ascii") for x in pids) if pids else b"-"); row(b"raw_statuses",b",".join(str(x).encode("ascii") for x in statuses) if statuses else b"-"); row(b"result",b"PASS")
 output=b"P27E001V3|probe="+ID+b"|schema=3\n"+b"\n".join(rows)+b"\n"
 need(len(output)<=CAP and output.endswith(b"\n") and b"\r" not in output and b"\x00" not in output,"output-frame")
 write_bounded(1,output,checked(now(),500000000))
except BaseException:
 cleanup_live()
 raise
finally:
 for fd in tuple(owned): close_if(fd)
 for fd in (libc_fd,py_fd,self_fd,env_fd,bash_fd): close_if(fd)
UNIFIED MARKER V3 SOURCE END
```

This block is inert documentation. It has not been imported, parsed,
compiled, evaluated, or executed. P05's armed-timer wait is the only blocking
wait and cannot be accepted unless the exact EINTR branch is observed; every
other wait and every drain is WNOHANG/nonblocking plus a fixed deadline.

## 7. Five-pipe topology, ownership, and cleanup state machine

The outer source creates exactly five pipe nodes and ten distinct FD numbers:
stdin, marker stdout, marker stderr, launcher telemetry, and release. Each
node appears exactly twice, once at its read end and once at its write end.
The five node device/inode pairs are pairwise distinct. The child-facing
stdout, stderr, and telemetry descriptions are blocking at creation; only the
controller/launcher draining ends and explicit bounded controller writes are
made nonblocking. Thus a child never inherits the V2 EAGAIN hazard. Ordered
file actions duplicate exactly one end to each destination 0 through 4 and
close every other inherited descriptor. The launcher verifies exactly five
distinct FIFO nodes. Its marker verifies exactly four after its private gate
is installed. After that gate closes, the marker persistent transport is
exactly 0, 1, and 2.

The finite outer lifecycle is:

```text
OPEN_IDENTITIES -> CREATE_SAFE_CWD -> CREATE_FIVE_PIPES -> SPAWN_LEADER
-> RECEIVE_OWNERSHIP -> REVALIDATE_ALL -> RELEASE_L
-> DRAIN_AND_WNOHANG -> REAP_LEADER -> NONSIGNALING_GROUP_OBSERVATION
-> TERMINAL_REVALIDATION -> EMPTY_INVENTORY -> HELD_DIRFD_RMDIR -> REPORT
```

Before release, any failure closes the release end without writing `L`.
After release, normal completion requires exact marker PASS framing, empty
raw stderr, launcher zero raw status, three exact EOFs, marker PID agreement,
all child counts equal, terminal source hashes, and nonnegative bounded
elapsed values. Cleanup TERM and KILL are distinct states. Both perform a new
WNOHANG and exact leader `/proc/PID/stat` comparison before the delivered
signal. Reap is a one-way transition: no delivered signal is reachable from
or after `leader_reaped=1`. A post-reap signal-zero success means residual or
reused group and is FAIL without escalation.

The launcher has no signal API call. It either returns a complete normal
terminal line or emits an exact cleanup request/failure terminal while
remaining the owned leader until the outer controller's bounded disposition.
It cannot convert timeout, source, child, cleanup, parser, identity, or
controller failure into another class. The outer report preserves each raw
stream byte-for-byte as byte count, SHA-256, and hex; it records the actual
leader PID, start time, raw wait status, signal-delivery bits, exact EOF bits,
source identities, terminal checks, safe-cwd removal observation, and one
PASS/FAIL. No `.strip()` or `.splitlines()` occurs in any output parser.

## 8. Exact probe catalog and bounds

Every branch consumes exactly the declared `EXTRA` arity and rejects any
additional item. All nested Python invocations use the fixed watchdog profile,
the exact ten-key environment, complete signal defaults, empty mask, inherited
owned group, and no PATH lookup. Returned PIDs and all raw statuses appear in
the common terminal rows.

- P00 passes one NUL-free 251414-byte synthetic comment as `-c` plus the
  `watchdog` argv item. Exact spawn success/zero raw status or exact E2BIG is
  observational PASS, but only success gives `transport_feasible=1`.
- P01D holds and hashes `/proc/self/exe` and the resolved Python object, then
  selects exactly one executable libc mapping. It compares the maps device
  and inode to the O_NOFOLLOW-opened libc object before hashing. It reports
  `spawn_premise_satisfied=0` and spawns no child.
- P01C consumes exactly thirteen presealed items, in this order:

```text
libc_path_hex libc_map_dev libc_map_ino libc_mode_octal libc_nlink libc_uid
libc_gid libc_bytes libc_sha256 libc_confstr_hex python_dev python_ino
python_sha256
```

  It requires total equality to a fresh held observation, calls the CPython
  builtin `os.posix_spawn` directly, records exact raw child bytes/hash,
  PID/SID/PGID and raw status, then rehashes both held images.
- P02 reports the exact environment in bytewise-key order, cwd, runtime flags,
  exact 0/1/2 FIFO map, five resource-limit tuples, and bounded NPROC tuple.
- P03 lowers only its own soft NOFILE to 64, makes at most 64 pipe attempts,
  requires EMFILE, closes every returned FD, and observes only 0/1/2.
- P04 resets and verifies every valid signal except uncatchable KILL/STOP,
  reports the complete sorted list/hash, and proves the sampled mask empty.
- P05 records WNOHANG zero, one timer-bounded EINTR, exit-23 raw status,
  ECHILD after the actual reap, and a separate self-TERM child raw status.
- P06 takes exactly 4096 monotonic samples. It requires nondecrease, progress,
  signed-63 headroom, and `0 <= end-start <= DELTA`.
- P07 observes CLOEXEC, nonblocking EAGAIN, poll readiness, one byte, retained
  writer behavior, HUP, and EOF, with every FD in a `finally` closure.
- P08 records one held returned child, inherited SID/PGID, live signal zero,
  raw zero status, and immediate post-reap ESRCH. `reuse_proof=0` is mandatory.
- P09 is the sole normal-body delivered SIGKILL probe. WNOHANG proves its exact
  returned direct child unreaped immediately before delivery; reap requires
  a signal raw status and `0 <= end-start <= 1000000000`.
- P10 serially spawns and reaps exactly sixteen children, one live at a time.
  It exact-parses terminal-LF child frames and reports all PIDs, PGIDs, and raw
  statuses. It never claims PID non-reuse.
- P11 alone creates `target`. A held original FD anchors the inode through
  write/fsync, fixed atime, chown, O_NOATIME observation, pre-unlink pathname
  equality, unlink, held nlink-zero, and pathname absence. The private cwd
  bounds but cannot eliminate the final stat/unlink race, so
  `atomic_unlink_proof=0` is mandatory.
- P12 prebinds and holds exact `/usr/bin/env` and `/usr/bin/bash` objects by
  device/inode/content. It executes exact env-i/bash/second-env-i containment,
  requires the final ten-key environment and underscore absence, hashes the
  exact six-line raw child frame, and rehashes both held tools.
- P13 creates `a`, fsyncs a held inode, and uses exact-dirfd `link(a,b)` as an
  atomic no-replace construction. It proves the two-link identity before
  unlinking `a`, fsyncs the held directory, verifies `b` against the still-held
  inode, unlinks `b`, observes held nlink zero and absence, and claims no
  rename atomicity, crash durability, pathname immutability, or atomic
  conditional unlink proof.

Probe branch limits are fixed: P00/P01C/P05/P08/P09/P12 at most one live
child; P05 at most two total; P10 exactly sixteen total and one live; all
others zero. P11 and P13 are the only filesystem-writing probes. P12 is the
only shell-using probe. P09 is the only normal-body SIGKILL probe. No branch
uses setsid, setpgroup, a process-group signal, a broad process scan, or a
pre-existing PID.

## 9. Safe-cwd and filesystem closure

The outer source opens `/` and `/tmp` with O_DIRECTORY, O_CLOEXEC, and
O_NOFOLLOW, and compares held fstat tuples with no-follow component stats.
The new directory is made relative to the held `/tmp` dirfd under umask 077,
opened O_NOFOLLOW, fchmoded 0700, and required root-owned, same-device, empty,
and absent as a mount point. The simple fixed name grammar excludes slashes,
dot-dot, repository, build, evidence, recovery-root, stage, payload,
validator, binder, and every old namespace. The controller repeats component,
path, held-inode, empty-inventory, and mount observations before release and
at terminal disposition.

P11 and P13 operate only relative to a held `.` dirfd. They keep an open FD to
the created inode through final unlink. P13's hard-link construction fails
with EEXIST rather than replacing `b`; ordinary rename is absent. All cleanup
names are fixed literals. There is no glob, recursion, temporary-name search,
stat-based deletion of an unrelated inode, or broadened fallback. If a held
inode and pathname observation diverge, cleanup stops, the outer empty check
fails, and the directory is retained. The exact source explicitly records
that the remaining stat/unlink and stat/rmdir intervals are observations, not
atomic exact-inode proofs.

## 10. Complete closed API allowlists

These are exact source-level allowlists. Constants, attributes, byte/string
methods, container operations, arithmetic, comparison, formatting, and named
builtin exceptions lexically present in a frozen source are included; no
dynamic lookup or additional callable is allowed.

OUTER CONTROLLER V3 imports exactly `errno`, `fcntl`, `hashlib`, `os`,
`resource`, `select`, `signal`, `stat`, `sys`, and `time`. Its operating calls
are exactly: `fcntl.fcntl`; `hashlib.sha256`; `os.close`, `fchmod`, `fstat`,
`fsencode`, `geteuid`, `getegid`, `getpid`, `killpg`, `listdir`, `lseek`,
`lstat`, `mkdir`, `open`, `pipe2`, `posix_spawn`, `read`, `readlink`, `rmdir`,
`stat`, `umask`, `waitpid`, and `write`; POSIX spawn DUP2/CLOSE actions;
`resource.getrlimit`; `select.poll`; `signal.valid_signals`; `stat.S_ISDIR`,
`S_ISFIFO`, `S_ISLNK`, `S_ISREG`, and `S_IMODE`; `time.monotonic_ns`; and the
exact constants referenced in the source. Its exact-child `/proc/PID/stat`,
`/proc/self/exe`, and `/proc/self/mountinfo` reads are the only proc surfaces.

COMMON LAUNCHER V3 imports the same ten modules. Its operating calls are
exactly: `fcntl.fcntl`; `hashlib.sha256`; `os.chdir`, `close`, `fstat`,
`fsencode`, `getcwdb`, `geteuid`, `getegid`, `getpgrp`, `getpid`, `getppid`,
`getsid`, `lseek`, `open`, `pipe2`, `posix_spawn`, `read`, `readlink`, `stat`,
`umask`, `waitpid`, and `write`; POSIX spawn DUP2/CLOSE actions;
`resource.getrlimit` and `setrlimit`; `select.poll`; `signal.getsignal`,
`pthread_sigmask`, `signal`, and `valid_signals`; `stat.S_ISFIFO`, `S_ISREG`,
and `S_IMODE`; `time.monotonic_ns` and `sleep`; and the exact constants named.
Its only proc surfaces are `/proc/self/exe` and exact-child `/proc/PID/stat`.
There is no launcher `kill`, `killpg`, `fork`, or subprocess surface.

UNIFIED MARKER V3 imports the same ten modules. Its operating calls are
exactly: `fcntl.fcntl`; `hashlib.sha256`; `os.chown`, `close`, `confstr`,
`dup`, `fsencode`, `fsync`, `fstat`, `getcwdb`, `getpgid`, `getpgrp`, `getpid`,
`getsid`, `kill`, `link`, `lseek`, `makedev`, `open`, `pipe2`, `posix_spawn`,
`read`, `readlink`, `set_inheritable`, `stat`, `sysconf`, `unlink`, `utime`,
`waitpid`, and `write`; POSIX spawn DUP2/CLOSE actions and wait-status macros;
`resource.getrlimit` and `setrlimit`; `select.poll`; `signal.getsignal`,
`pthread_sigmask`, `setitimer`, `signal`, and `valid_signals`;
`stat.S_ISDIR`, `S_ISFIFO`, `S_ISREG`, and `S_IMODE`; `time.clock_getres`,
`get_clock_info`, `monotonic_ns`, and `sleep`; and exact named constants.
Its proc surfaces are `/proc/self/exe`, `/proc/self/maps`, and
`/proc/self/status`. Exact tool paths are Python, env, and bash only.

Across all three sources, APIs not on these lists are forbidden. In
particular there is no dynamic import, eval, exec builtin, compile builtin,
ctypes, prctl, tempfile, pathlib, glob, shutil, subprocess, multiprocessing,
socket, urllib, requests, package discovery, PTY, tracing, directory walk,
network, credential, namespace, mount, chmod outside the fresh dir, chroot,
shell except P12, broad signal, or production program call. `os.fsencode`,
`stat.S_ISFIFO`, every wait macro, and every actually used path/file API are
explicitly included.

## 11. Failure telemetry and exact raw framing

No source uses trimming, line-ending normalization, implicit decoding, or
`splitlines` for child or marker results. Exact parsers require terminal LF,
forbid CR and NUL, split only on literal LF, retain the required final empty
element, require ASCII, fixed line count/order, unique lowercase keys, exact
probe ID, exact source hash, canonical decimals, and one final PASS. Raw
streams are hashed before semantic parsing. P01C, P10, and P12 parse exact raw
frames and retain the raw child statuses; P01C and P12 additionally retain
raw byte count and SHA-256.

The outer failure class remains separate from `timed`. A source mismatch is
source failure; identity mismatch is identity failure; cwd/interference is
filesystem failure; spawn error is spawn failure; malformed ownership is
ownership failure; elapsed expiry alone is timeout; nonzero child/status/EOF
is child failure; grammar is parser failure; incomplete reap/group/empty
inventory is cleanup failure; and an unexpected internal exception is
controller failure. Each report includes raw hashes/hex even on failure,
subject to fixed caps. No exception is relabeled as timeout, no ECHILD is
relabeled as reaped, and no missing status becomes zero.

## 12. Exact correction closure over V2 findings

V3 makes the following source-level corrections, while preserving all prior
closed environment, flag, FD, signal, limit, containment, no-bytecode,
second-env, no-retry, and bounded-observation controls:

1. freezes the complete outer controller rather than delegating it to prose;
2. creates and binds the safe cwd, components, mount exclusion, inventory,
   held dirfds, terminal checks, and cleanup within that outer source;
3. freezes exact file actions, umask, ownership gate, release, deadlines,
   drains, reaps, parser, source hashes, terminal identities, and report;
4. replaces every unbounded wait/drain with WNOHANG/nonblocking bounded loops,
   retaining only P05's timer-bounded intentional EINTR wait;
5. allows delivered group signals only with the exact leader unreaped and
   continuously start-time/topology-bound, and makes post-reap state strictly
   non-signaling;
6. records every launcher and nested PID, every raw wait status, exact EOF,
   raw byte count/hash/hex, and distinct failure class;
7. requires every elapsed subtraction to have a nonnegative ordered pair and
   an explicit upper bound;
8. binds the executing Python object through `/proc/self/exe` plus the held
   resolved object, both by device/inode/content, at opening and terminal;
9. binds mapped libc device/inode from maps to the opened object before hash,
   and carries the complete tuple from discovery to confirmation;
10. binds env and bash objects around P12 and preserves exact raw framing and
    second-env underscore exclusion;
11. enumerates all actual APIs, including previously omitted `os.fsencode`
    and `stat.S_ISFIFO`;
12. replaces P13 ordinary rename with exact-dirfd hard-link no-replace then
    unlink, holds the inode through cleanup, and disclaims rename proof;
13. holds P11/P13 inode and private-directory FDs through removal and treats
    every residual stat/unlink or stat/rmdir race as failure, never proof;
14. keeps five distinct pipe nodes with ten distinct FD numbers and blocking
    child write descriptions, eliminating V2's impossible ten-node rule and
    nonblocking child-write hazard;
15. makes cleanup, escalation, direct reap, raw hashing, and terminal parser
    part of the frozen control rather than an unfrozen future choice.

## 13. Facts that remain unproved

Even all fifteen exact PASS results do not prove future host state, production
cwd behavior, V8 execution, glibc internal clone strategy, universal PID/PGID
non-reuse, scheduler fairness, signal latency, absence of uninterruptible
sleep, crash durability, power-loss ordering, storage persistence, rename
atomicity, pathname immutability, inode non-reuse, mount stability, or
capability/O_NOATIME behavior for another inode or instant. P00 E2BIG is an
observational PASS but a production transport blocker. No observation is
portable to a different executable, libc, source, argv, environment, cwd,
kernel, filesystem, authorization, process, or time.

No probe, actor, fixture, payload, validator, binder, V8 source, build,
evidence, recovery root, release, PDF, or Paper28 action is authorized. No
source block in this file was imported, parsed, compiled, evaluated, or
executed during authoring.

## 14. Frozen source identities and census

The extraction rule is byte-delimiter-only: locate the unique exact standalone
BEGIN and END lines for one named record; exclude both delimiter lines and
their bytes; take every intervening byte, including the LF after every source
line and the final source LF immediately before END. Do not trim, dedent,
decode/re-encode, interpolate, normalize, import, parse, compile, evaluate, or
execute the result. Under that rule the exact records are:

```text
OUTER_CONTROLLER_V3 bytes=34419 LF=494 sha256=bf06aebdeae5b205694071746eb5d07e7a964dbf03f2d4cd17e26a8b5e1b4a70 final_byte=0a
COMMON_LAUNCHER_V3 bytes=13670 LF=248 sha256=cd112d07abd57c141fbe398d7ad582f1874d23d5a5b4afde51ff1546b07ef555 final_byte=0a
UNIFIED_MARKER_V3 bytes=37072 LF=501 sha256=2c4ebf5551243f2d6a7fe04587011104b9613d438493a3ab48ea52f8769a4e49 final_byte=0a
```

Source census: 3 frozen records; 3 unique BEGIN lines; 3 unique END lines; 6
total source delimiter lines; 10 explicit imports per record; 15 accepted
probe IDs; 15 closed probe branches; 15 correction classes in section 12; 5
outer pipe nodes; 10 outer pipe-end FD numbers; 1 owned session/group; 0
launcher delivered-signal calls; 2 outer delivered-signal call sites (TERM and KILL),
both pre-reap only; 1 marker normal-body SIGKILL branch (P09); 2
filesystem-writing branches (P11/P13); 1 shell branch (P12); 1
discovery/confirmation pair (P01D/P01C); 0 source executions; 0 probe
attempts; 0 build/evidence/recovery-root accesses.

BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V3_AUTHOR_STOP
