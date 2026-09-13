# E001 Supervisor Host-Probe Recovery Control

Status: INERT PLAN ONLY. NOT AN EXECUTION AUTHORIZATION.

## 1. Authority boundary

This file defines a fail-closed plan for possible future host probes. It does not authorize this author, a validator, a binder, a build actor, a payload actor, or any other process to execute a probe, create a marker, inspect a process, signal a process, change a file, or consume a result. No probe described below was executed while authoring this file.

A future probe may run only after a new, probe-specific supervisor authorization names the probe ID, the exact source identity delimited in this file, the exact disposable path if one is needed, the expected E0331/V8/tool identities, and the one allowed attempt. Authorization of one probe does not authorize another probe. A PASS is only a measured host fact for the named attempt. It grants no build, validator, payload, binder, publication, or namespace authority.

The following are prohibited for every probe:

- network access or namespace creation;
- reading, printing, inheriting, or transmitting credentials, tokens, keys, cookies, proxy settings, or user configuration;
- package installation, removal, upgrade, or environment mutation;
- repository mutation, including locks, caches, bytecode, logs, markers, temporary files, and timestamps;
- access to build, evidence, root, stage, old, payload, validator, or binder namespaces;
- invocation of the real payload, any validator, any binder, any build command, or any repository executable;
- broad process enumeration, broad `kill`, `killall`, `pkill`, negative-PID signaling, or signaling a PGID not created and reported by the same probe attempt;
- attaching to, tracing, inspecting, waiting for, or signaling a pre-existing process;
- retry, fallback, repair, adaptation, acceptance widening, or a second sample after an unexpected result.

Any identity mismatch, parse mismatch, timeout, exception, unexpected return, extra output byte, missing cleanup confirmation, or environmental difference is FAIL. FAIL grants nothing. PASS also grants nothing beyond recording the bounded measurement.

## 2. E0331 anchor and closed identity binding

The only supplied ledger anchor is:

```text
path=E0331
dev=2431
ino=12439253869
mode=0644
nlink=1
uid=0
gid=0
bytes=1848081
lf=20661
sha256=72d732c9834c7670f22160e73c0391c668f40d271e4fdf1aba986b24217c6b30
terminal=BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V8_DUAL_STATIC_PASS_CONSUMED_AND_ACTOR_DERIVATION_HOST_CONTROL_AUTHORIZED
```

No V8 byte identity and no frozen tool identity is invented, inferred, shortened, or refreshed here. Their sole allowed values are the exact V8 identity and exact frozen tool identity records already contained in the anchored E0331 ledger. Until a future supervisor copies those records verbatim into a probe-specific sealed authorization, every probe is identity-blocked.

Immediately before any future probe, a read-only control actor must revalidate and report the complete E0331 tuple above, including path, device, inode, mode, link count, ownership, byte count, LF count, SHA-256, and terminal. It must also report, verbatim and in full, the E0331-bound V8 identity and every E0331-bound frozen identity used by that probe. Immediately after cleanup, it must repeat the same complete reports. A before/after difference is FAIL.

The only executable paths that may be relevant are:

```text
/usr/bin/env
/usr/bin/bash
/root/miniconda3/bin/python3.12
```

Each path may be used only when the applicable probe authorization carries its exact frozen E0331 identity. No PATH lookup, symlink substitution, alternate interpreter, shell fallback, `python`, or `python3` alias is allowed. The future control must compare the full frozen records before execution and again after cleanup. A comparison based only on pathname, version text, or hash is insufficient.

## 3. Common execution envelope

The following envelope is mandatory unless a probe section is stricter.

1. One attempt only. There is no retry.
2. The control has a 5 second outer monotonic deadline; P09 has a 2 second outer deadline. On timeout it may signal only a still-live synthetic PID created by that same attempt, first with the probe-specific exact signal. It must then reap that PID. It must not signal a negative PID or use a broad process command.
3. Maximum simultaneously live synthetic children: 2, except P10 where it is 1. Maximum total synthetic children: 4, except P10 where it is 16.
4. CPU cap: RLIMIT_CPU soft 2 seconds and hard 2 seconds in the synthetic process. Address-space cap: RLIMIT_AS soft and hard 134217728 bytes. File-size cap: RLIMIT_FSIZE soft and hard 1048576 bytes. Core cap: RLIMIT_CORE soft and hard 0. Synthetic-child cap: RLIMIT_NPROC soft and hard no greater than the inherited hard limit and no greater than 32. P03 may lower only its own soft RLIMIT_NOFILE as stated there and must not alter the hard limit.
5. Standard input is `/dev/null`. Standard output is one control-owned pipe. Standard error is a separate control-owned pipe and must reach EOF with zero bytes. No inherited descriptor other than 0, 1, and 2 is allowed. Every control descriptor is CLOEXEC unless its exact `dup2` file action makes it 0, 1, or 2. A descriptor census must confirm the intended set.
6. No shell is used except in P12, where the exact shell command bytes are fixed below.
7. No source file is materialized. Source bytes are passed as the final `-c` argument. P11 and P13 are the only probes allowed to create disposable filesystem objects, and each requires a separate path-specific authorization.
8. Locale-independent canonical output is ASCII only, LF terminated, with exactly one terminal LF. Output is at most 16384 bytes per probe. Fields appear in the order fixed by the probe. Decimal integers have no sign and no leading zero unless the value is zero. Hex is lowercase and has no `0x` prefix. Booleans are `0` or `1`. Lists are comma-separated with no spaces; an empty list is `-`.
9. The first output line is `P27E001|probe=<ID>|schema=1`. The last output line is `P27E001|probe=<ID>|result=PASS`. A failure is recorded by the external control, not normalized into PASS output.
10. The external control records raw stdout bytes, their byte count, LF count, and SHA-256. It parses only after hashing. It then emits a separately delimited canonical normalization with its own byte count, LF count, and SHA-256. Raw and normalized identities are never conflated.

The exact ten-key environment is:

```text
HOME=/nonexistent
LANG=C
LC_ALL=C
PATH=/usr/bin:/bin
P27_PROBE_MODE=E001
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
PYTHONNOUSERSITE=1
TMPDIR=/tmp
TZ=UTC
```

There are exactly ten entries, sorted by bytewise key order. No inherited entry is retained. In particular, there is no proxy, credential, Python path, startup, shell, repository, or dynamic-loader entry. P11 and P13 receive their authorized disposable path as an argv item, never as an additional environment key.

For Python marker probes other than P12, the exact argv form is:

```text
argv[0]=/root/miniconda3/bin/python3.12
argv[1]=-I
argv[2]=-S
argv[3]=-c
argv[4]=<exact bytes between the named SOURCE BEGIN and SOURCE END delimiters>
```

The delimiter lines and the LF immediately after `SOURCE BEGIN` and immediately before `SOURCE END` are excluded from source identity. All bytes between them are literal ASCII with LF line endings. No dedent, trim, tab expansion, interpolation, newline conversion, or terminal-LF insertion is allowed. The raw source identity is exactly that delimiter-defined byte string. Its normalized identity is identical to its raw identity. This delimiter rule deliberately makes no unexecuted hash claim. Before a future launch, the external control must calculate the source byte count, LF count, and SHA-256, compare them to the values sealed in the new authorization, and report them. A hash calculated only after launch cannot authorize the launch.

Allowed common Python imports are restricted further by each probe. Importing a package from `site-packages`, importing a repository module, writing bytecode, or evaluating dynamic source is FAIL. Allowed common APIs are ordinary constants and pure formatting operations plus the APIs explicitly named in the probe. `subprocess`, `socket`, `urllib`, `requests`, `ctypes`, `multiprocessing`, `pathlib`, `tempfile`, `shutil`, `glob`, `pkgutil`, `importlib`, `eval`, `exec`, and `compile` are prohibited.

## 4. P01 - CPython identity, flags, posix_spawn file actions, and setsid

Purpose: verify the exact authorized CPython 3.12 identity and report its runtime flags, then test one synthetic child created by `os.posix_spawn` with explicit file actions and `setsid=True`.

Allowed imports/APIs: `os`, `sys`; `os.pipe2`, `os.posix_spawn`, `os.read`, `os.close`, `os.waitpid`, `os.getpid`, `os.getsid`, `os.getpgid`; the three POSIX spawn file-action constants; `sys.version_info`, `sys.hexversion`, `sys.implementation`, `sys.flags`, `sys.executable`.

Child argv is the same absolute Python path with `-I -S -c` and the literal child source `import os;print("%d,%d,%d"%(os.getpid(),os.getsid(0),os.getpgid(0)),flush=True)`. Child env is the exact ten-key environment. File actions are, in order, `DUP2(write_fd,1)`, `CLOSE(read_fd)`, `CLOSE(write_fd)`. The child has no stderr output and `setsid=True`. Timeout is 3 seconds. Caps and FDs are the common envelope.

Expected output grammar and checks, in fixed order:

```text
P27E001|probe=P01|schema=1
P27E001|probe=P01|version=3.12.<decimal>
P27E001|probe=P01|hexversion=<lowercase-hex>
P27E001|probe=P01|implementation=cpython
P27E001|probe=P01|executable_hex=<lowercase-hex>
P27E001|probe=P01|flags=<comma-separated-name:decimal-list>
P27E001|probe=P01|spawn_pid=<decimal>
P27E001|probe=P01|child_sid=<decimal>
P27E001|probe=P01|child_pgid=<decimal>
P27E001|probe=P01|raw_status=0
P27E001|probe=P01|result=PASS
```

The decoded executable must equal the absolute frozen path, major/minor must be 3.12, implementation must be CPython, `no_site`, `no_user_site`, `ignore_environment`, `isolated`, and `safe_path` must each be 1, and child SID and PGID must both equal the returned child PID. Any unsupported `setsid`, file-action error, leaked output, or different status is FAIL. Cleanup closes both pipe ends and reaps only the returned PID.

```text
P01 SOURCE BEGIN
import os
import sys
ID="P01"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
vi=sys.version_info
out("version","%d.%d.%d"%(vi.major,vi.minor,vi.micro))
out("hexversion",format(sys.hexversion,"x"))
out("implementation",sys.implementation.name)
out("executable_hex",os.fsencode(sys.executable).hex())
names=("debug","inspect","interactive","optimize","dont_write_bytecode","no_user_site","no_site","ignore_environment","verbose","bytes_warning","quiet","hash_randomization","isolated","dev_mode","utf8_mode","warn_default_encoding","safe_path","int_max_str_digits")
out("flags",",".join(n+":"+str(int(getattr(sys.flags,n))) for n in names))
r,w=os.pipe2(os.O_CLOEXEC)
child='import os;print("%d,%d,%d"%(os.getpid(),os.getsid(0),os.getpgid(0)),flush=True)'
fa=((os.POSIX_SPAWN_DUP2,w,1),(os.POSIX_SPAWN_CLOSE,r),(os.POSIX_SPAWN_CLOSE,w))
pid=os.posix_spawn(sys.executable,(sys.executable,"-I","-S","-c",child),dict(os.environ),file_actions=fa,setsid=True)
os.close(w)
data=b""
while True:
 b=os.read(r,128)
 if not b: break
 data+=b
os.close(r)
got_pid,sid,pgid=(int(x) for x in data.strip().split(b","))
wp,status=os.waitpid(pid,0)
assert wp==pid and got_pid==pid and sid==pid and pgid==pid and status==0
out("spawn_pid",str(pid))
out("child_sid",str(sid))
out("child_pgid",str(pgid))
out("raw_status",str(status))
out("result","PASS")
P01 SOURCE END
```

## 5. P02 - exact environment and initial FD containment

Purpose: verify that the synthetic process sees exactly the ten authorized environment entries and only descriptors 0, 1, and 2 before the transient `/proc/self/fd` enumeration descriptor.

Allowed imports/APIs: `os`; `os.environ`, `os.listdir`, `os.readlink`. Read access is limited to `/proc/self/fd` entries for the current synthetic PID. No other `/proc` path is allowed.

Timeout is 2 seconds. No child is created. Expected output is the header, one `env=` line whose value is the comma-separated lowercase hex encoding of each exact `key=value` byte string in bytewise key order, `fds=0,1,2`, then PASS. The enumeration implementation must account for its own transient directory FD; any persistent extra FD is FAIL.

```text
P02 SOURCE BEGIN
import os
ID="P02"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
items=[]
for k in sorted(os.environb): items.append((k+b"="+os.environb[k]).hex())
out("env",",".join(items))
fds=[]
for n in os.listdir("/proc/self/fd"):
 if n.isdigit():
  try: os.readlink("/proc/self/fd/"+n)
  except FileNotFoundError: continue
  fds.append(int(n))
fds.sort()
assert fds==[0,1,2]
out("fds",",".join(str(x) for x in fds))
out("result","PASS")
P02 SOURCE END
```

## 6. P03 - hard RLIMIT_NOFILE and FD-census behavior

Purpose: report the inherited soft and hard RLIMIT_NOFILE, demonstrate a bounded self-only soft-limit reduction, reach EMFILE using pipes, and confirm cleanup restores the initial persistent FD census. The hard limit is never changed.

Allowed imports/APIs: `os`, `resource`, `errno`; current `/proc/self/fd` list/readlink only; `resource.getrlimit`, `resource.setrlimit`, `os.pipe2`, `os.close`.

The new soft limit is `min(original_soft, original_hard, 64)` and must be at least 16. At most 61 additional descriptors are retained. Timeout is 2 seconds. All opened descriptors are closed in a `finally` block. The process exits after the measurement, so its soft-limit change cannot affect the controller. Unexpected errno, hard-limit change, missing EMFILE, or final census other than 0,1,2 is FAIL.

Expected fixed fields are `soft_before`, `hard_before`, `soft_test`, `opened`, `emfile=1`, `fds_after=0,1,2`, and PASS.

```text
P03 SOURCE BEGIN
import errno
import os
import resource
ID="P03"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
def census():
 a=[]
 for n in os.listdir("/proc/self/fd"):
  if n.isdigit():
   try: os.readlink("/proc/self/fd/"+n)
   except FileNotFoundError: continue
   a.append(int(n))
 return sorted(a)
out("schema","1")
soft,hard=resource.getrlimit(resource.RLIMIT_NOFILE)
assert hard!=resource.RLIM_INFINITY and hard>=16
test=min(soft,hard,64)
assert test>=16
resource.setrlimit(resource.RLIMIT_NOFILE,(test,hard))
held=[]
hit=0
try:
 while True:
  try:
   r,w=os.pipe2(os.O_CLOEXEC)
   held.extend((r,w))
  except OSError as e:
   assert e.errno==errno.EMFILE
   hit=1
   break
finally:
 for fd in held: os.close(fd)
assert resource.getrlimit(resource.RLIMIT_NOFILE)==(test,hard)
after=census()
assert after==[0,1,2]
out("soft_before",str(soft))
out("hard_before",str(hard))
out("soft_test",str(test))
out("opened",str(len(held)))
out("emfile",str(hit))
out("fds_after",",".join(str(x) for x in after))
out("result","PASS")
P03 SOURCE END
```

## 7. P04 - signal default and mask normalization

Purpose: verify spawn-time signal defaulting and masking in one isolated synthetic child, without changing or signaling any pre-existing process.

Allowed imports/APIs: `os`, `sys`, `signal`; `os.posix_spawn`, pipe/read/close/waitpid; `signal.getsignal`, `signal.pthread_sigmask`; exact `setsigdef` and `setsigmask` spawn attributes.

The parent captures its SIGUSR1 and SIGUSR2 dispositions and mask and confirms they are unchanged after the child is reaped. The child is created with `setsigdef=(SIGUSR1,SIGUSR2)`, `setsigmask=(SIGUSR2,)`, and `setsid=True`. It reports SIGUSR1 default, SIGUSR2 default, SIGUSR1 unmasked, SIGUSR2 masked. Timeout is 3 seconds. No signal is delivered.

Expected fields are `usr1_default=1`, `usr2_default=1`, `usr1_masked=0`, `usr2_masked=1`, `parent_unchanged=1`, `raw_status=0`, and PASS.

```text
P04 SOURCE BEGIN
import os
import signal
import sys
ID="P04"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
before=(signal.getsignal(signal.SIGUSR1),signal.getsignal(signal.SIGUSR2),signal.pthread_sigmask(signal.SIG_BLOCK,()))
r,w=os.pipe2(os.O_CLOEXEC)
child='import signal; m=signal.pthread_sigmask(signal.SIG_BLOCK,()); print("%d,%d,%d,%d"%(signal.getsignal(signal.SIGUSR1)==signal.SIG_DFL,signal.getsignal(signal.SIGUSR2)==signal.SIG_DFL,signal.SIGUSR1 in m,signal.SIGUSR2 in m),flush=True)'
fa=((os.POSIX_SPAWN_DUP2,w,1),(os.POSIX_SPAWN_CLOSE,r),(os.POSIX_SPAWN_CLOSE,w))
pid=os.posix_spawn(sys.executable,(sys.executable,"-I","-S","-c",child),dict(os.environ),file_actions=fa,setsid=True,setsigdef=(signal.SIGUSR1,signal.SIGUSR2),setsigmask=(signal.SIGUSR2,))
os.close(w)
data=os.read(r,128)
assert os.read(r,1)==b""
os.close(r)
wp,status=os.waitpid(pid,0)
a,b,c,d=(int(x) for x in data.strip().split(b","))
after=(signal.getsignal(signal.SIGUSR1),signal.getsignal(signal.SIGUSR2),signal.pthread_sigmask(signal.SIG_BLOCK,()))
assert wp==pid and status==0 and (a,b,c,d)==(1,1,0,1) and before==after
out("usr1_default",str(a))
out("usr2_default",str(b))
out("usr1_masked",str(c))
out("usr2_masked",str(d))
out("parent_unchanged","1")
out("raw_status",str(status))
out("result","PASS")
P04 SOURCE END
```

## 8. P05 - waitpid, WNOHANG, EINTR, ECHILD, and raw status

Purpose: measure Python/host wait behavior only for synthetic children returned to this probe.

Allowed imports/APIs: `errno`, `os`, `signal`, `sys`; pipe operations, `os.posix_spawn`, `os.waitpid`, `signal.signal`, `signal.setitimer`; wait-status macros. No other PID is accepted.

Child A blocks on its inherited descriptor until the parent writes one byte, then exits 23. Before release, `waitpid(pid,WNOHANG)` must return `(0,0)`. While it is blocked, SIGALRM is delivered only to the probe parent; its handler raises `InterruptedError(errno.EINTR,"probe")`, and the exact-PID blocking wait must propagate that handler exception. The timer and disposition are restored. Child A is released and reaped; its raw status must be an ordinary exit with code 23. A second exact wait must raise ECHILD. Child B signals only itself with SIGTERM and is reaped; raw status must indicate SIGTERM. Timeout is 4 seconds.

Expected fields are `wnohang_zero=1`, `eintr=1`, `exit_raw=<decimal>`, `exit_code=23`, `echild=1`, `signal_raw=<decimal>`, `term_signal=<decimal SIGTERM>`, and PASS.

```text
P05 SOURCE BEGIN
import errno
import os
import signal
import sys
ID="P05"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
r,w=os.pipe2(os.O_CLOEXEC)
os.set_inheritable(r,True)
child='import os,sys; os.read(int(sys.argv[1]),1); raise SystemExit(23)'
pid=os.posix_spawn(sys.executable,(sys.executable,"-I","-S","-c",child,str(r)),dict(os.environ),setsid=True)
os.close(r)
z=os.waitpid(pid,os.WNOHANG)
assert z==(0,0)
old=signal.getsignal(signal.SIGALRM)
def alarm(a,b): raise InterruptedError(errno.EINTR,"probe")
signal.signal(signal.SIGALRM,alarm)
signal.setitimer(signal.ITIMER_REAL,0.02)
intr=0
try:
 try: os.waitpid(pid,0)
 except InterruptedError as e:
  assert e.errno==errno.EINTR
  intr=1
finally:
 signal.setitimer(signal.ITIMER_REAL,0.0)
 signal.signal(signal.SIGALRM,old)
os.write(w,b"x")
os.close(w)
wp,exit_raw=os.waitpid(pid,0)
assert wp==pid and os.WIFEXITED(exit_raw) and os.WEXITSTATUS(exit_raw)==23
echild=0
try: os.waitpid(pid,os.WNOHANG)
except ChildProcessError as e:
 assert e.errno==errno.ECHILD
 echild=1
child2='import os,signal; os.kill(os.getpid(),signal.SIGTERM)'
pid2=os.posix_spawn(sys.executable,(sys.executable,"-I","-S","-c",child2),dict(os.environ),setsid=True,setsigdef=(signal.SIGTERM,),setsigmask=())
wp2,signal_raw=os.waitpid(pid2,0)
assert wp2==pid2 and os.WIFSIGNALED(signal_raw) and os.WTERMSIG(signal_raw)==signal.SIGTERM
out("wnohang_zero","1")
out("eintr",str(intr))
out("exit_raw",str(exit_raw))
out("exit_code",str(os.WEXITSTATUS(exit_raw)))
out("echild",str(echild))
out("signal_raw",str(signal_raw))
out("term_signal",str(os.WTERMSIG(signal_raw)))
out("result","PASS")
P05 SOURCE END
```

## 9. P06 - monotonic clock resolution, headroom, and checked deadlines

Purpose: measure monotonic clock properties and demonstrate checked deadline arithmetic. It does not sleep and does not infer future scheduling latency.

Allowed imports/APIs: `time`; `time.get_clock_info`, `time.clock_getres`, `time.monotonic_ns`.

The probe takes 4096 immediate samples. They must be nondecreasing and at least one positive delta must occur. It reports declared resolution rounded upward to integral nanoseconds, minimum observed positive delta, start, end, signed-63-bit headroom, and a checked 1 second deadline. It fails before addition if `start > 2^63-1 - 1000000000`. Timeout is 2 seconds.

Expected fields are `implementation_hex`, `adjustable=0`, `monotonic=1`, `declared_resolution_ns=<positive-decimal>`, `observed_min_delta_ns=<positive-decimal>`, `start_ns`, `end_ns`, `headroom_ns`, `deadline_ns`, `deadline_checked=1`, and PASS.

```text
P06 SOURCE BEGIN
import time
ID="P06"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
info=time.get_clock_info("monotonic")
res=time.clock_getres(time.CLOCK_MONOTONIC)
res_ns=max(1,int(res*1000000000.0+0.999999999))
vals=[time.monotonic_ns() for _ in range(4096)]
assert all(vals[i]<=vals[i+1] for i in range(len(vals)-1))
deltas=[vals[i+1]-vals[i] for i in range(len(vals)-1) if vals[i+1]>vals[i]]
assert deltas
limit=(1<<63)-1
start=vals[0]
assert start<=limit-1000000000
deadline=start+1000000000
out("implementation_hex",info.implementation.encode("ascii").hex())
out("adjustable",str(int(info.adjustable)))
out("monotonic",str(int(info.monotonic)))
out("declared_resolution_ns",str(res_ns))
out("observed_min_delta_ns",str(min(deltas)))
out("start_ns",str(start))
out("end_ns",str(vals[-1]))
out("headroom_ns",str(limit-start))
out("deadline_ns",str(deadline))
out("deadline_checked","1")
out("result","PASS")
P06 SOURCE END
```

## 10. P07 - pipe2 CLOEXEC, nonblocking poll, and independent EOF

Purpose: verify local pipe descriptor flags, readiness, and EOF dependency on all writer references.

Allowed imports/APIs: `errno`, `fcntl`, `os`, `select`; `os.pipe2`, `os.dup`, `os.read`, `os.write`, `os.close`; `fcntl.fcntl`; `select.poll`.

One pipe is created with O_CLOEXEC and O_NONBLOCK. Both ends must have FD_CLOEXEC and O_NONBLOCK. Empty read must raise EAGAIN/EWOULDBLOCK. Initial zero-time poll must not report readable data. After writing byte `x`, poll must report readable and the exact byte is read. The writer is duplicated; closing the original must not yield EOF. Closing the duplicate must yield POLLHUP and a zero-length read. Timeout is 2 seconds. Every descriptor is closed in `finally`.

Expected fields are `read_cloexec=1`, `write_cloexec=1`, `read_nonblock=1`, `write_nonblock=1`, `empty_eagain=1`, `initial_readable=0`, `byte_hex=78`, `eof_before_last_writer=0`, `hup_after_last_writer=1`, `eof_after_last_writer=1`, and PASS.

```text
P07 SOURCE BEGIN
import errno
import fcntl
import os
import select
ID="P07"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
r,w=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK)
d=-1
try:
 rc=int(bool(fcntl.fcntl(r,fcntl.F_GETFD)&fcntl.FD_CLOEXEC))
 wc=int(bool(fcntl.fcntl(w,fcntl.F_GETFD)&fcntl.FD_CLOEXEC))
 rn=int(bool(fcntl.fcntl(r,fcntl.F_GETFL)&os.O_NONBLOCK))
 wn=int(bool(fcntl.fcntl(w,fcntl.F_GETFL)&os.O_NONBLOCK))
 empty=0
 try: os.read(r,1)
 except OSError as e:
  assert e.errno in (errno.EAGAIN,errno.EWOULDBLOCK)
  empty=1
 p=select.poll(); p.register(r,select.POLLIN|select.POLLHUP)
 initial=int(bool(p.poll(0)))
 assert initial==0
 assert os.write(w,b"x")==1
 assert p.poll(0)
 byte=os.read(r,1)
 d=os.dup(w)
 os.close(w); w=-1
 before=0
 try:
  q=os.read(r,1)
  before=int(q==b"")
 except OSError as e: assert e.errno in (errno.EAGAIN,errno.EWOULDBLOCK)
 assert before==0
 os.close(d); d=-1
 events=p.poll(1000)
 hup=int(any(mask&select.POLLHUP for fd,mask in events if fd==r))
 eof=int(os.read(r,1)==b"")
 assert (rc,wc,rn,wn,empty,hup,eof)==(1,1,1,1,1,1,1)
 out("read_cloexec",str(rc))
 out("write_cloexec",str(wc))
 out("read_nonblock",str(rn))
 out("write_nonblock",str(wn))
 out("empty_eagain",str(empty))
 out("initial_readable",str(initial))
 out("byte_hex",byte.hex())
 out("eof_before_last_writer",str(before))
 out("hup_after_last_writer",str(hup))
 out("eof_after_last_writer",str(eof))
 out("result","PASS")
finally:
 for fd in (r,w,d):
  if fd>=0:
   try: os.close(fd)
   except OSError: pass
P07 SOURCE END
```

## 11. P08 - session/PGID containment and immediate signal-zero absence

Purpose: measure containment of one synthetic child and the immediate post-reap behavior of exact-PID and exact-PGID signal zero. The result is not proof against later PID or PGID reuse.

Allowed imports/APIs: `errno`, `os`, `sys`; pipe operations, `os.posix_spawn`, `os.getsid`, `os.getpgid`, `os.kill`, `os.killpg`, `os.waitpid`. Signals are zero only; no delivered signal is permitted.

The child has `setsid=True`, reports ready on one pipe, and blocks on a release pipe. The parent checks returned PID equals SID equals PGID, then signal zero succeeds for that exact PID and exact PGID. It releases and reaps the child, then immediately requires both exact checks to fail with ESRCH. Timeout is 3 seconds. Cleanup may release and reap only the returned PID. Negative-PID signaling is forbidden.

Expected fields are `pid`, `sid`, `pgid`, `live_pid_zero=1`, `live_pgid_zero=1`, `raw_status=0`, `post_pid_esrch=1`, `post_pgid_esrch=1`, `reuse_proof=0`, and PASS.

```text
P08 SOURCE BEGIN
import errno
import os
import sys
ID="P08"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
ready_r,ready_w=os.pipe2(os.O_CLOEXEC)
go_r,go_w=os.pipe2(os.O_CLOEXEC)
os.set_inheritable(ready_w,True); os.set_inheritable(go_r,True)
child='import os,sys; os.write(int(sys.argv[1]),b"R"); os.read(int(sys.argv[2]),1)'
pid=os.posix_spawn(sys.executable,(sys.executable,"-I","-S","-c",child,str(ready_w),str(go_r)),dict(os.environ),setsid=True)
os.close(ready_w); os.close(go_r)
assert os.read(ready_r,1)==b"R"
os.close(ready_r)
sid=os.getsid(pid); pgid=os.getpgid(pid)
assert sid==pid and pgid==pid
os.kill(pid,0); os.killpg(pgid,0)
os.write(go_w,b"G"); os.close(go_w)
wp,status=os.waitpid(pid,0)
assert wp==pid and status==0
pe=0
try: os.kill(pid,0)
except ProcessLookupError as e:
 assert e.errno==errno.ESRCH
 pe=1
ge=0
try: os.killpg(pgid,0)
except ProcessLookupError as e:
 assert e.errno==errno.ESRCH
 ge=1
assert pe==1 and ge==1
out("pid",str(pid))
out("sid",str(sid))
out("pgid",str(pgid))
out("live_pid_zero","1")
out("live_pgid_zero","1")
out("raw_status",str(status))
out("post_pid_esrch",str(pe))
out("post_pgid_esrch",str(ge))
out("reuse_proof","0")
out("result","PASS")
P08 SOURCE END
```

## 12. P09 - bounded SIGKILL and timely reap

Purpose: measure bounded delivery and reap latency for one synthetic child. This is the only probe allowed to deliver SIGKILL.

Allowed imports/APIs: `os`, `signal`, `sys`, `time`; pipe operations, `os.posix_spawn`, `os.kill`, `os.waitpid`, wait-status macros, `time.monotonic_ns`.

The child is placed in a new session, reports readiness on one private pipe, and blocks on a second private pipe. The parent validates the returned PID is the session and process-group leader. It calls `os.kill(pid,SIGKILL)` exactly once using the positive returned PID, then waits for that exact PID. The elapsed interval from immediately before kill to completed wait must not exceed 1000000000 ns; the outer timeout is 2 seconds. No PGID or negative-PID signal is allowed. Cleanup closes pipe descriptors and reaps the exact child if needed.

Expected fields are `pid`, `pgid`, `signal=<decimal SIGKILL>`, `raw_status=<decimal>`, `reap_elapsed_ns=<decimal not above 1000000000>`, `reaped=1`, and PASS.

```text
P09 SOURCE BEGIN
import os
import signal
import sys
import time
ID="P09"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
ready_r,ready_w=os.pipe2(os.O_CLOEXEC)
hold_r,hold_w=os.pipe2(os.O_CLOEXEC)
os.set_inheritable(ready_w,True); os.set_inheritable(hold_r,True)
child='import os,sys; os.write(int(sys.argv[1]),b"R"); os.read(int(sys.argv[2]),1)'
pid=os.posix_spawn(sys.executable,(sys.executable,"-I","-S","-c",child,str(ready_w),str(hold_r)),dict(os.environ),setsid=True)
os.close(ready_w); os.close(hold_r)
assert os.read(ready_r,1)==b"R"
os.close(ready_r)
pgid=os.getpgid(pid)
assert os.getsid(pid)==pid and pgid==pid
start=time.monotonic_ns()
os.kill(pid,signal.SIGKILL)
wp,status=os.waitpid(pid,0)
elapsed=time.monotonic_ns()-start
os.close(hold_w)
assert wp==pid and os.WIFSIGNALED(status) and os.WTERMSIG(status)==signal.SIGKILL and elapsed<=1000000000
out("pid",str(pid))
out("pgid",str(pgid))
out("signal",str(signal.SIGKILL))
out("raw_status",str(status))
out("reap_elapsed_ns",str(elapsed))
out("reaped","1")
out("result","PASS")
P09 SOURCE END
```

## 13. P10 - bounded PID/PGID reuse premise measurement

Purpose: collect a small sequential sample of synthetic PID and PGID allocation. It cannot prove that reuse will not occur before, during, or after another operation.

Allowed imports/APIs: `os`, `sys`; pipe operations, `os.posix_spawn`, `os.read`, `os.close`, `os.waitpid`.

Exactly 16 children are created and reaped sequentially, never more than one live. Each child has `setsid=True`, writes its PID and PGID, and exits zero. No signal is sent. The probe reports the exact ordered lists and duplicate counts. Both zero and nonzero duplicate counts are measurements, but the authorization must accept the grammar, not reinterpret either as proof. Timeout is 5 seconds; total children cap is 16.

Expected fields are `sample_count=16`, `pids=<16-decimal-list>`, `pgids=<16-decimal-list>`, `pid_duplicates=<decimal>`, `pgid_duplicates=<decimal>`, `absence_proof=0`, and PASS.

```text
P10 SOURCE BEGIN
import os
import sys
ID="P10"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
pids=[]; pgids=[]
child='import os; print("%d,%d"%(os.getpid(),os.getpgid(0)),flush=True)'
for i in range(16):
 r,w=os.pipe2(os.O_CLOEXEC)
 fa=((os.POSIX_SPAWN_DUP2,w,1),(os.POSIX_SPAWN_CLOSE,r),(os.POSIX_SPAWN_CLOSE,w))
 pid=os.posix_spawn(sys.executable,(sys.executable,"-I","-S","-c",child),dict(os.environ),file_actions=fa,setsid=True)
 os.close(w)
 data=b""
 while True:
  b=os.read(r,128)
  if not b: break
  data+=b
 os.close(r)
 wp,status=os.waitpid(pid,0)
 cp,cg=(int(x) for x in data.strip().split(b","))
 assert wp==pid and status==0 and cp==pid and cg==pid
 pids.append(cp); pgids.append(cg)
pd=len(pids)-len(set(pids)); gd=len(pgids)-len(set(pgids))
out("sample_count","16")
out("pids",",".join(str(x) for x in pids))
out("pgids",",".join(str(x) for x in pgids))
out("pid_duplicates",str(pd))
out("pgid_duplicates",str(gd))
out("absence_proof","0")
out("result","PASS")
P10 SOURCE END
```

## 14. P11 - O_NOATIME and CAP_FOWNER on one disposable file

Purpose: measure O_NOATIME behavior on a newly created, separately authorized, non-build disposable file and relate the observed result to the process's CAP_FOWNER effective bit. It does not authorize use of O_NOATIME on any repository, build, evidence, payload, or pre-existing file.

This probe is blocked unless a separate authorization supplies one exact absolute directory `D` outside the repository and all protected namespaces. `D` must be a new supervisor-created mode-0700 directory on a local filesystem, owned by uid 0, empty at entry, not a symlink, not a mount point, and named only for this attempt. The sole target is exactly `D/target`. The controller must lstat every path component before launch, reject symlinks, record device/inode/mode/link/uid/gid for `D`, and confirm the target does not exist. No wildcard or unresolved environment variable is allowed.

Allowed imports/APIs: `errno`, `os`, `sys`; read `/proc/self/status` only for the single `CapEff:` line; `os.open`, `os.write`, `os.read`, `os.close`, `os.fstat`, `os.stat`, `os.chown`, `os.utime`, `os.unlink`; constants O_CREAT, O_EXCL, O_RDWR, O_RDONLY, O_CLOEXEC, O_NOFOLLOW, O_NOATIME.

Argv adds `argv[5]=D`. The marker exclusively creates mode 0600 `D/target`, writes byte `x`, sets both timestamps to 1000000000 ns, closes it, chowns it to uid/gid 65534, and attempts exact `O_RDONLY|O_CLOEXEC|O_NOFOLLOW|O_NOATIME`. If CAP_FOWNER effective bit 3 is 1, the open must succeed; if it is 0, it must fail with EPERM. On success it reads exactly one byte and requires atime remain 1000000000 ns. It unlinks only the exact inode it created after verifying device/inode/link/type. The external controller removes `D` only after confirming it is empty and is still the authorized inode. Any cleanup uncertainty is FAIL and causes no wider deletion. Timeout is 2 seconds; one file, one byte, no retry.

Expected fields are `capeff_hex=<lowercase-hex>`, `cap_fowner=<0-or-1>`, `open_result=OK` or `open_result=EPERM`, `atime_unchanged=<0-or-1>`, `created_dev`, `created_ino`, `cleanup_unlinked=1`, and PASS. The accepted branch is fixed by the measured CapEff bit as stated above; any other errno is FAIL.

```text
P11 SOURCE BEGIN
import errno
import os
import sys
ID="P11"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
D=sys.argv[1]
assert os.path.isabs(D) and os.path.basename(D) not in ("",".","..")
target=D+"/target"
capline=None
with open("/proc/self/status","rb",buffering=0) as f:
 for line in f:
  if line.startswith(b"CapEff:\t"):
   capline=line.split()[1]
   break
assert capline is not None
capeff=int(capline,16); cap_fowner=int(bool(capeff&(1<<3)))
fd=os.open(target,os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600)
try:
 assert os.write(fd,b"x")==1
 st=os.fstat(fd)
 dev,ino=st.st_dev,st.st_ino
finally: os.close(fd)
os.utime(target,ns=(1000000000,1000000000),follow_symlinks=False)
os.chown(target,65534,65534,follow_symlinks=False)
opened=""; unchanged=0
try:
 fd=os.open(target,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW|os.O_NOATIME)
 opened="OK"
 try: assert os.read(fd,1)==b"x"
 finally: os.close(fd)
 unchanged=int(os.stat(target,follow_symlinks=False).st_atime_ns==1000000000)
 assert cap_fowner==1 and unchanged==1
except OSError as e:
 assert e.errno==errno.EPERM and cap_fowner==0
 opened="EPERM"
cur=os.stat(target,follow_symlinks=False)
assert cur.st_dev==dev and cur.st_ino==ino and cur.st_nlink==1 and (cur.st_mode&0o170000)==0o100000
os.unlink(target)
out("capeff_hex",capline.decode("ascii").lower())
out("cap_fowner",str(cap_fowner))
out("open_result",opened)
out("atime_unchanged",str(unchanged))
out("created_dev",str(dev))
out("created_ino",str(ino))
out("cleanup_unlinked","1")
out("result","PASS")
P11 SOURCE END
```

## 15. P12 - env to bash to CPython exec containment

Purpose: verify that the exact frozen `/usr/bin/env` to `/usr/bin/bash` to `/root/miniconda3/bin/python3.12` exec chain preserves one synthetic PID/session/PGID and yields exactly the ten-key environment, without naming or invoking the real payload.

This probe requires exact E0331-frozen identities for all three executables. Allowed controller APIs are `os.posix_spawn`, pipe operations, `os.waitpid`, `os.getsid`, and `os.getpgid`. The final Python marker imports only `os` and `sys`.

The exact executable is `/usr/bin/env`. Its exact argv is the following ordered byte sequence; angle-bracket labels refer to exact delimiter-defined bytes, not shell interpolation:

```text
/usr/bin/env
-i
HOME=/nonexistent
LANG=C
LC_ALL=C
PATH=/usr/bin:/bin
P27_PROBE_MODE=E001
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
PYTHONNOUSERSITE=1
TMPDIR=/tmp
TZ=UTC
/usr/bin/bash
--noprofile
--norc
-c
unset PWD SHLVL _; exec /root/miniconda3/bin/python3.12 -I -S -c "$1"
p27-e001-chain
<exact P12 SOURCE bytes>
```

The bash `-c` command bytes are exactly the single ASCII line shown above without a terminal LF. The three bash-added exported names PWD, SHLVL, and `_` are removed before exec. No expansion other than `$1` occurs. `argv[0]` for the shell command is `p27-e001-chain`; `$1` is the exact P12 source. The `env` process is spawned with an empty env, explicit stdout/stderr file actions, `setsid=True`, and no PATH lookup. Timeout is 3 seconds. The returned PID must equal the Python-reported PID, SID, and PGID. Output environment must exactly match the ten-key list. Stderr must be empty and raw status zero.

Expected fields are `pid`, `sid`, `pgid`, `executable_hex=<hex of exact Python path>`, `env=<same encoding as P02>`, `real_payload_invoked=0`, and PASS.

```text
P12 SOURCE BEGIN
import os
import sys
ID="P12"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
out("pid",str(os.getpid()))
out("sid",str(os.getsid(0)))
out("pgid",str(os.getpgid(0)))
out("executable_hex",os.fsencode(sys.executable).hex())
items=[]
for k in sorted(os.environb): items.append((k+b"="+os.environb[k]).hex())
out("env",",".join(items))
out("real_payload_invoked","0")
out("result","PASS")
P12 SOURCE END
```

## 16. P13 - fsync, rename, and path-check surface measurement

Purpose: measure only the successful return behavior of file fsync, same-directory rename, directory fsync, and path identity checks on new disposable objects. This probe cannot prove crash durability, filesystem atomicity to concurrent observers, storage-controller persistence, remote-filesystem behavior, absence of later replacement, or path immutability.

This probe is blocked unless a separate authorization supplies a new exact absolute directory `D` satisfying all P11 directory constraints. The only allowed objects are `D/a` and `D/b`. The external controller records and rechecks every path component and the exact inode of `D`. No observer process is created.

Allowed imports/APIs: `os`, `stat`, `sys`; `os.open`, `os.write`, `os.fsync`, `os.close`, `os.fstat`, `os.stat`, `os.rename`, `os.unlink`; O_DIRECTORY, O_RDONLY, O_CREAT, O_EXCL, O_RDWR, O_CLOEXEC, O_NOFOLLOW.

Argv adds `argv[5]=D`. The marker exclusively creates `a`, writes exact bytes `P27E001\n`, fsyncs the file, records its identity, renames `a` to `b` in the same directory, confirms `a` is absent and `b` is the same inode, fsyncs an FD opened on `D`, then unlinks the exact inode. The controller removes only the verified empty authorized `D`. Timeout is 2 seconds; one file of 8 bytes; no retry.

Expected fields are `file_fsync_returned=1`, `same_dir_rename_returned=1`, `old_absent=1`, `inode_preserved=1`, `dir_fsync_returned=1`, `created_dev`, `created_ino`, `cleanup_unlinked=1`, `durability_proof=0`, `immutability_proof=0`, and PASS.

```text
P13 SOURCE BEGIN
import os
import stat
import sys
ID="P13"
def out(k,v): print("P27E001|probe=%s|%s=%s"%(ID,k,v),flush=True)
out("schema","1")
D=sys.argv[1]
assert os.path.isabs(D) and os.path.basename(D) not in ("",".","..")
a=D+"/a"; b=D+"/b"
fd=os.open(a,os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600)
try:
 assert os.write(fd,b"P27E001\n")==8
 os.fsync(fd)
 st=os.fstat(fd)
 assert stat.S_ISREG(st.st_mode) and st.st_nlink==1
 dev,ino=st.st_dev,st.st_ino
finally: os.close(fd)
os.rename(a,b)
old_absent=int(not os.path.lexists(a))
cur=os.stat(b,follow_symlinks=False)
preserved=int(cur.st_dev==dev and cur.st_ino==ino and cur.st_nlink==1 and stat.S_ISREG(cur.st_mode))
assert old_absent==1 and preserved==1
dfd=os.open(D,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW)
try: os.fsync(dfd)
finally: os.close(dfd)
cur=os.stat(b,follow_symlinks=False)
assert cur.st_dev==dev and cur.st_ino==ino and cur.st_nlink==1
os.unlink(b)
out("file_fsync_returned","1")
out("same_dir_rename_returned","1")
out("old_absent",str(old_absent))
out("inode_preserved",str(preserved))
out("dir_fsync_returned","1")
out("created_dev",str(dev))
out("created_ino",str(ino))
out("cleanup_unlinked","1")
out("durability_proof","0")
out("immutability_proof","0")
out("result","PASS")
P13 SOURCE END
```

## 17. Probe-verifiable facts

Only the following bounded facts are eligible to be reported as probe-verifiable, and only for the exact host, process, executable identities, source identities, environment, and instant of the authorized attempt:

- P01: CPython-reported version/implementation/flags and the observed posix_spawn file-action/setsid result.
- P02: the marker's environment and persistent descriptor census.
- P03: inherited RLIMIT_NOFILE values and bounded EMFILE/census behavior after a self-only soft-limit change.
- P04: observed spawn-time signal dispositions and mask, plus unchanged parent signal state.
- P05: observed exact-child WNOHANG, handler-raised EINTR, ECHILD, and raw wait statuses.
- P06: declared and sampled monotonic properties, measured deltas, and checked arithmetic headroom.
- P07: observed pipe flags, readiness, byte transfer, writer-reference behavior, HUP, and EOF.
- P08: observed session/PGID containment and immediate signal-zero results before and after reap.
- P09: observed exact-PID SIGKILL raw status and measured reap interval.
- P10: the exact 16-sample PID/PGID allocation sequence and duplicate counts.
- P11: effective CAP_FOWNER bit, authorized disposable-file O_NOATIME result, and sampled atime.
- P12: the final marker's PID/session/PGID, exact environment, interpreter path, and zero exit through the fixed exec chain.
- P13: successful syscall returns and inode/path observations on the authorized disposable file.

These are observations, not portable guarantees. A probe result is stale immediately with respect to mutable host state unless a later authorization explicitly accepts that risk.

## 18. Unprovable retained premises

The following remain premises even if every probe passes:

- PID and PGID non-reuse outside the exact sampled intervals; signal zero cannot prove identity, ownership, or future absence.
- Scheduler fairness, universal signal-delivery latency, universal reap latency, and behavior under host pressure.
- Absence of kernel, libc, interpreter, filesystem, storage, or hardware faults not exercised by the bounded sample.
- Crash durability after fsync, ordering across power loss, device cache persistence, and equivalence of filesystem implementations.
- Rename atomicity for all observers, across directories or mounts, under crashes, or on filesystems other than the one sampled.
- Path immutability before or after each lstat/stat; a pathname is not an immutable capability, and device/inode equality alone does not exclude reuse.
- Symlink, mount, namespace, or ancestor replacement outside the exact checks; component checks are temporal observations.
- O_NOATIME semantics for any pre-existing, differently owned, remote, overlay, repository, build, or evidence file.
- Capability stability after the sampled CapEff line and applicability in a different user or mount namespace.
- Python, env, and bash behavior under different bytes, flags, identities, environment, descriptors, limits, locale, kernel, or time.
- Completeness of `/proc/self/fd` as a universal FD model, and portability to a host without the same procfs semantics.
- The real payload's safety, correctness, containment, determinism, or output. The real payload is deliberately never invoked.
- E0331, V8, frozen tools, repository trees, build outputs, evidence, or protected namespaces remaining unchanged after the final revalidation instant.

No probe is allowed to convert one of these premises into a claimed proof.

## 19. External control record and cleanup

For an authorized attempt, the external control record must contain, in this order:

1. probe ID and one-attempt authorization ID;
2. complete pre-probe E0331 identity and terminal;
3. complete pre-probe V8 identity copied verbatim from E0331;
4. complete pre-probe frozen identities copied verbatim from E0331 for every executable used;
5. exact source raw byte count, LF count, SHA-256, and delimiter name;
6. exact argv item lengths and lowercase hex encodings;
7. the ten exact environment entries and confirmation of zero inherited entries;
8. exact initial FD map and resource caps;
9. start monotonic_ns and checked deadline;
10. returned synthetic PIDs/PGIDs, limited only to the named probe;
11. raw stdout byte count, LF count, SHA-256, and delimiter-bound bytes;
12. raw stderr byte count and SHA-256, with byte count required to be zero;
13. raw wait status for every returned PID and confirmation all were reaped;
14. normalized output byte count, LF count, SHA-256, and delimiter-bound bytes;
15. cleanup confirmations for FDs, children, and, only for P11/P13, exact disposable inodes;
16. complete post-probe E0331, V8, and frozen-tool identities;
17. a final PASS or FAIL that grants no further authority.

Raw output delimiters are exactly `P27E001 <ID> RAW BEGIN` and `P27E001 <ID> RAW END`. Normalized output delimiters are exactly `P27E001 <ID> NORMALIZED BEGIN` and `P27E001 <ID> NORMALIZED END`. Delimiter lines are not part of the enclosed identity. The control must not print raw source as a shell command, must not evaluate a delimiter block, and must not treat documentation fences as executable content.

On any abort, the control closes only its own descriptors, signals only still-live exact synthetic PIDs from the same attempt when required by the probe cleanup rule, reaps them, and verifies their exact post-reap state. For P11/P13 it may unlink only the recorded disposable inode at the exact authorized path after a fresh identity check; it may remove only the exact authorized empty directory inode. If identity cannot be established, it stops without broader deletion and reports FAIL. No retry follows.

## 20. Whole-anchor report and inventory

E0331 remains bound to the supplied whole identity: dev 2431, ino 12439253869, mode 0644, nlink 1, uid 0, gid 0, 1848081 bytes, 20661 LF bytes, SHA-256 72d732c9834c7670f22160e73c0391c668f40d271e4fdf1aba986b24217c6b30, terminal `BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V8_DUAL_STATIC_PASS_CONSUMED_AND_ACTOR_DERIVATION_HOST_CONTROL_AUTHORIZED`. Its exact V8 and frozen-tool records remain ledger-derived only and must be reported whole before and after a future attempt; no substitute identity is present in this plan.

Inventory: P01 CPython/posix_spawn; P02 ten-key environment/FD containment; P03 RLIMIT_NOFILE/FD census; P04 signal normalization; P05 wait semantics; P06 monotonic clock/deadlines; P07 pipe2/poll/EOF; P08 session/PGID/signal-zero; P09 SIGKILL/reap; P10 bounded reuse sample; P11 O_NOATIME/CAP_FOWNER; P12 env/bash/Python exec chain; P13 fsync/rename/path surface. Total: 13 separately authorized, single-attempt probes. Current execution count: 0. Current authority granted: none.

BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_AUTHOR_STOP
