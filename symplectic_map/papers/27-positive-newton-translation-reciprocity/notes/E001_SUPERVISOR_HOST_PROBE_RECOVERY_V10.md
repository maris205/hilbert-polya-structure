# Paper 27 E001 supervisor Host probe recovery V10

Status: inert author control; execution count is zero.

This file is the E0353-authorized Host V10 control.  It binds the exact E0353
ledger and repairs the two Host V9 preauthor failures while restoring every
V8 probe observation.  The five source records below are data.  Nothing in
this note was imported, parsed as a programming language, compiled, evaluated,
or launched while it was authored or checked.

## 1. Frozen authority

The authoritative parent is the exact regular file
`/root/autodl-tmp/symplectic_map/BATCH_07_STATUS.md`, dev 2431, ino
12439253869, mode 0644, nlink 1, uid 0, gid 0, 2134269 bytes, 22574 LF,
SHA-256 f64699702769d5204aada902df92976c93ddddae2a9c8fbc01f6c37e88efe7fd.
Its unique final nonempty line is
`BATCH07_P27_PROBE_RECOVERY_E001_HOST_V10_DUAL_PREAUTHOR_PASS_AND_AUTHOR_OPEN`.
Only E0351--E0353 authorize this record.

Frozen controls, all read as inert bytes, are:

| control | bytes | LF | SHA-256 |
| --- | ---: | ---: | --- |
| Host V8 | 74973 | 1071 | 72079707809f54fb35591f5e1ab8ef0d22671c72c37ea234de699e5f9e8002cf |
| Host V9 | 105750 | 2772 | aac728bbd460b2da5ddb9befd6c58815873e583f6336f1011fbfb77ce39fd62a |
| Binder V8 | 279288 | 7303 | 3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4 |
| Actor V3 | 47229 | 924 | 1ce0ce19b73588ed3bd03212b2fcd61a32d3cfc90ec2f7f1d241639c5baf1f2a |
| Derivation V6 | 237426 | 2896 | 266a84d6242f2bb7ff17e7f10d01cc52ac163c7bf3dd77532a3776abd76b605f |

The V8 row meanings are normative.  V9 contributes only nonconflicting
flattened ownership, fixed-census cleanup, progress, and framing safety.

## 2. Closed invocation and premises

The actor supplies one authenticated invocation containing, in fixed order:
probe ID; 256-bit lowercase nonce; operational budget; positive
FD_RETURN_COMMIT_PROGRESS_NS; positive OWNER_CONTROL_PROGRESS_NS; positive
KILL_REAP_PROGRESS_NS; positive TERMINAL_FRAMING_PROGRESS_NS; positive
ACTOR_ACK_PROGRESS_NS; the exact authenticated commit-window exclusion token;
the exact authenticated outer-survival-through-exit-entry token;
safe-directory identity; five source byte/LF/SHA
triples; the P01C thirteen-field tuple when and only when P01C is selected.
No other field, environment key, path, executable, mode, broker operation, or
payload is admitted.

The environment/actor premise, not POSIX and not an observation, guarantees:

1. every successful descriptor-producing return reaches both preallocated
   fixed cells within FD_RETURN_COMMIT_PROGRESS_NS, with every asynchronous
   exception, signal-language handler, callback, trace hook, profile hook,
   KeyboardInterrupt, and external control transfer excluded from that
   return-to-commit interval;
2. the same exclusion and prompt local `finally` applies to each successful
   `posix_spawn` return and exact `waitpid` return;
3. owner control progresses through the final fallible scan, complete bounded
   candidate/terminal write-all postchecks, and outer exit entry;
4. after an exact PID is selected for forced cleanup, the signal syscall,
   EINTR work, exact wait return, and fixed-cell commit complete within the
   positive KILL_REAP_PROGRESS_NS; and
5. the future actor keeps the outer alive through host completion and then
   supplies a distinct ACTOR_ACK_PROGRESS_NS.  ACK, EOF, ESRCH, elapsed grace,
   signal return, process exit, or an ancestor reap is never evidence for any
   premise.

The source checks all additions and multiplications against signed 63-bit
range.  It arms exactly one OPERATIONAL_DEADLINE before the first reservation.
At cleanup entry it arms exactly one nonrestartable
POST_OPERATION_HOST_DEADLINE.  Operational lateness remains fatal forever.
The post-operation horizon supports cleanup and reporting but cannot erase it.

## 3. Exact finite arithmetic

All values below are positive integer nanoseconds.  Multiplicity is literal.

| term | multiplicity | per item | total |
| --- | ---: | ---: | ---: |
| cleanup admission/census | 1 | 20000000 | 20000000 |
| pre-signal control | 4 | 20000000 | 80000000 |
| TERM observation | 4 | 40000000 | 160000000 |
| EINTR/syscall allowance | 4 | 20000000 | 80000000 |
| exact KILL/wait/commit | 4 | 100000000 | 400000000 |
| rescue/state transition | 4 | 20000000 | 80000000 |
| ordered hold-writer gates | 4 | 20000000 | 80000000 |
| four outer FD close passes | 4 x 48 | 2000000 | 384000000 |
| exhaustive outer FREE scan | 48 | 500000 | 24000000 |
| final fallible fault scan | 1 | 10000000 | 10000000 |
| candidate and terminal framing | 1 | 100000000 | 100000000 |
| outer exit entry | 1 | 20000000 | 20000000 |
| POST_OPERATION_HOST_BOUND_NS | exact sum | - | 1438000000 |

The marker local close reserve is `4*64*2000000 + 64*500000 + 10000000
= 554000000`.  The child local close reserve is `4*8*2000000 +
8*500000 + 10000000 = 78000000`.  Marker and child work deadlines subtract
those reserves from OPERATIONAL_DEADLINE with checked signed arithmetic.

The future actor bound is the checked sum
`ACTOR_LAUNCH_PROGRESS_NS + OPERATIONAL_BUDGET_NS + 1438000000 +
ACTOR_ACK_PROGRESS_NS`.  Host completion excludes the future ACK term; actor
completion includes it.  No term is restarted, extended, or clamped to a new
horizon.

## 4. Fixed descriptor and process bounds

The process registry contains exactly four stable cells: launcher, keeper,
marker, and the single serial child cell.  Only the outer calls
`posix_spawn` or `waitpid`.  Launcher, keeper, marker, and child are direct
outer children; launcher is group leader, the other leaves join its group,
and outer remains outside.  No group TERM or KILL is used.

| process / branch | fixed FD cells | exact peak owned/inherited cells | descriptor-return calls over branch | proof |
| --- | ---: | ---: | ---: | --- |
| OUTER bootstrap | 48 | 24 | 21 calls / 28 returned FDs | adopted fd100, four anchors, five sealed sources, and seven protocol pipe pairs before leaf-side mates close |
| OUTER P00 peak | 48 | 18 | 23 calls / 31 returned FDs | broker baseline fifteen plus sealed synthetic and one output pipe pair; no gate for INFO |
| OUTER P10 cumulative | 48 | 17 | 37 calls / 60 returned FDs | broker baseline fifteen plus one serial output pair; each pair closes before the next of sixteen instances |
| MARKER common | 64 | 4 | 0 | adopted fd 5, 6, 7, 100; 7/100 closed before branches that do not need them |
| MARKER P01D/P01C | 64 | 4 | 4 | protocol fd5/fd6 plus two simultaneous image descriptors; maps and libc are serial after image closure |
| MARKER P03 | 64 | 61 registry / 64 process FDs | 61 | two prior image opens close, then exact five open 0,1,2,5,6 at soft limit 64 and 59 fixed cells commit before EMFILE |
| MARKER P07 | 64 | 5 | 3 | protocol plus pipe pair and duplicate, with prior source/anchor closure |
| MARKER P11 | 64 | 5 | 2 | adopted anchored dirfd plus target anchor and O_NOATIME reader |
| MARKER P13 | 64 | 4 | 1 | adopted anchored dirfd plus held inode anchor |
| CHILD any mode | 8 | 4 | 2 | adopted fd100 and optional gate fd3 plus two image opens |
| LAUNCHER / KEEPER | 0 | fixed inherited only | 0 | no FD-producing call after exec |

Every process preallocates its table before its first producing call.  Each
producer reserves stable FREE cells first.  On a successful return the first
caller-visible mutation commits the returned number to those cells without
allocation; an immediate local `finally` closes the gap.  EBADF while closing
is a cleanup fault and changes the cell to PHYSICALLY_CLOSED_ERROR, never clean
success.  Only proven noncreation releases a reservation.  Four exhaustive
close passes and a final FREE/closed-error scan cover every cell.

## 5. Five inert source records

UNIFIED OUTER V10 SOURCE BEGIN
import array
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

TAG=b"P27E001V10"
PYTHON=b"/root/miniconda3/bin/python3"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
PROBES=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
LOCAL=(b"P01D",b"P02",b"P03",b"P04",b"P06",b"P07",b"P11",b"P13")
BROKER=((b"P00",b"P00_E2BIG"),(b"P01C",b"P01C_INFO"),(b"P05",b"P05_WAIT"),(b"P08",b"P08_TOPOLOGY"),(b"P09",b"P09_KILL"),(b"P10",b"P10_INFO16"),(b"P12",b"P12_CHAIN"))
MODES=(b"INFO",b"BLOCK0",b"EXIT23",b"TERM",b"CHAIN")
SOURCE_NAMES=(b"outer.py",b"keeper.py",b"launcher.py",b"marker.py",b"child.py")
SOURCE_FDS=(100,101,102,103,104)
MAX_I63=(1<<63)-1
MAX_LIVE_SLOTS=4
OUTER_FD_CELLS=48
FREE=0
RESERVED=1
OWNED=2
TRANSFERRED=3
CLOSED=4
PHYSICALLY_CLOSED_ERROR=5
SLOT_FREE=0
SLOT_RESERVED=1
SLOT_LIVE=2
SLOT_REAPED=3
UNKNOWN_RAW=-1
ROLE_LAUNCHER=1
ROLE_KEEPER=2
ROLE_MARKER=3
ROLE_CHILD=4
FD_RETURN_COMMIT_PROGRESS_NS=5000000
OWNER_CONTROL_PROGRESS_NS=20000000
KILL_REAP_PROGRESS_NS=100000000
TERMINAL_FRAMING_PROGRESS_NS=100000000
ACTOR_ACK_PROGRESS_NS=500000000
ACTOR_LAUNCH_PROGRESS_NS=1000000000
COMMIT_WINDOW_TOKEN=b"NO_ASYNC_TRANSFER_THROUGH_FIXED_COMMIT_V1"
OWNER_SURVIVAL_TOKEN=b"OUTER_SURVIVES_THROUGH_TERMINAL_POSTCHECK_AND_EXIT_ENTRY_V1"
PER_FD_CLOSE_PROGRESS_NS=2000000
PER_FD_SCAN_PROGRESS_NS=500000
POST_OPERATION_HOST_BOUND_NS=1438000000
MARKER_CLOSE_RESERVE_NS=554000000
CHILD_CLOSE_RESERVE_NS=78000000
MAX_FRAME=1048576
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL

FD_NUM=array.array("i",[-1])*OUTER_FD_CELLS
FD_STATE=bytearray(OUTER_FD_CELLS)
FD_ROLE=bytearray(OUTER_FD_CELLS)
SLOT_PID=array.array("q",[-1])*MAX_LIVE_SLOTS
SLOT_RAW=array.array("q",[UNKNOWN_RAW])*MAX_LIVE_SLOTS
SLOT_STATE=bytearray(MAX_LIVE_SLOTS)
SLOT_ROLE=bytearray(MAX_LIVE_SLOTS)
SLOT_PHASE=bytearray(MAX_LIVE_SLOTS)
HOLD_CELL_BY_ROLE=array.array("i",[-1])*5
FATAL=bytearray(32)
FRAME_STATE=bytearray(4)
OPERATIONAL_DEADLINE=0
REQUEST_CELL=-1
POST_OPERATION_HOST_DEADLINE=0
POST_ARMED=0
ADMISSION_CLOSED=0
GROUP_LEADER=-1
KEEPER_PID=-1
OUTER_SID=-1

class HostFailure(Exception):
 pass

def latch(cell):
 if 0<=cell<len(FATAL):FATAL[cell]=1

def need(value,cell):
 if not value:
  latch(cell)
  raise HostFailure(str(cell))

def checked_add(a,b):
 need(type(a)is int and type(b)is int and a>=0 and b>=0 and a<=MAX_I63-b,0)
 return a+b

def checked_mul(a,b):
 need(type(a)is int and type(b)is int and a>=0 and b>=0 and (a==0 or b<=MAX_I63//a),0)
 return a*b

def verify_arithmetic():
 terms=(20000000,checked_mul(4,20000000),checked_mul(4,40000000),checked_mul(4,20000000),checked_mul(4,100000000),checked_mul(4,20000000),checked_mul(4,20000000),checked_mul(checked_mul(4,48),2000000),checked_mul(48,500000),10000000,100000000,20000000)
 total=0
 for item in terms:total=checked_add(total,item)
 need(total==POST_OPERATION_HOST_BOUND_NS,0)
 need(checked_add(checked_add(checked_add(15000000000,POST_OPERATION_HOST_BOUND_NS),ACTOR_ACK_PROGRESS_NS),ACTOR_LAUNCH_PROGRESS_NS)<=MAX_I63,0)

def mono(pre_cell=1,post_cell=2):
 try:value=time.monotonic_ns()
 except BaseException:
  latch(pre_cell)
  raise
 need(type(value)is int and value>=0,post_cell)
 return value

def pre(deadline,cell):
 need(mono(cell,cell)<=deadline,cell)

def post(deadline,cell):
 need(mono(cell,cell)<=deadline,cell)

def exception_post(deadline,cell):
 try:post(deadline,cell)
 except BaseException:latch(cell)

def checked_call(deadline,cell,fn,*args):
 pre(deadline,cell)
 try:value=fn(*args)
 except BaseException:
  exception_post(deadline,cell)
  raise
 post(deadline,cell)
 return value

def edge(deadline,cell):
 pre(deadline,cell)
 post(deadline,cell)

def reserve_fd(role):
 for i in range(OUTER_FD_CELLS):
  if FD_STATE[i]==FREE:
   FD_STATE[i]=RESERVED
   FD_ROLE[i]=role
   FD_NUM[i]=-1
   return i
 latch(3)
 raise HostFailure("fd-census-full")

def adopt_outer(number,role):
 i=reserve_fd(role)
 FD_NUM[i]=number
 FD_STATE[i]=OWNED
 return i

def release_fd_noncreation(i):
 need(FD_STATE[i]==RESERVED and FD_NUM[i]==-1,3)
 FD_STATE[i]=FREE
 FD_ROLE[i]=0

def owned_open_at(directory,name,flags,mode,role,deadline):
 i=reserve_fd(role)
 returned=-1
 created=False
 try:
  pre(deadline,4)
  try:
   if mode is None:returned=os.open(name,flags,dir_fd=directory)
   else:returned=os.open(name,flags,mode,dir_fd=directory)
   created=True
  finally:
   if created:
    FD_NUM[i]=returned
    FD_STATE[i]=OWNED
  post(deadline,4)
  return i
 except BaseException:
  if not created:release_fd_noncreation(i)
  exception_post(deadline,4)
  raise

def owned_open_root(role,deadline):
 i=reserve_fd(role)
 returned=-1
 created=False
 try:
  pre(deadline,4)
  try:
   returned=os.open(b"/",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW)
   created=True
  finally:
   if created:
    FD_NUM[i]=returned
    FD_STATE[i]=OWNED
  post(deadline,4)
  return i
 except BaseException:
  if not created:release_fd_noncreation(i)
  exception_post(deadline,4)
  raise

def owned_pipe(role,deadline):
 a=reserve_fd(role)
 b=reserve_fd(role)
 pair=None
 created=False
 try:
  pre(deadline,5)
  try:
   pair=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK)
   created=True
  finally:
   if created:
    FD_NUM[a]=pair[0]
    FD_NUM[b]=pair[1]
    FD_STATE[a]=OWNED
    FD_STATE[b]=OWNED
  post(deadline,5)
  return a,b
 except BaseException:
  if not created:
   release_fd_noncreation(a)
   release_fd_noncreation(b)
  exception_post(deadline,5)
  raise

def owned_memfd(role,deadline):
 i=reserve_fd(role)
 returned=-1
 created=False
 try:
  pre(deadline,6)
  try:
   returned=os.memfd_create("p27-e001-v10",os.MFD_CLOEXEC|os.MFD_ALLOW_SEALING)
   created=True
  finally:
   if created:
    FD_NUM[i]=returned
    FD_STATE[i]=OWNED
  post(deadline,6)
  return i
 except BaseException:
  if not created:release_fd_noncreation(i)
  exception_post(deadline,6)
  raise

def fd(i):
 need(0<=i<OUTER_FD_CELLS and FD_STATE[i] in (OWNED,TRANSFERRED) and FD_NUM[i]>=0,7)
 return FD_NUM[i]

def close_cell_nonthrowing(i,deadline):
 if FD_STATE[i] not in (OWNED,TRANSFERRED):return
 number=FD_NUM[i]
 try:
  if mono(8,8)>deadline:latch(8)
  try:os.close(number)
  except OSError as error:
   latch(8)
   if error.errno==errno.EBADF:FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
   else:FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
  except BaseException:
   latch(8)
   FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
  else:FD_STATE[i]=FREE;FD_ROLE[i]=0
  FD_NUM[i]=-1
  if mono(8,8)>deadline:latch(8)
 except BaseException:latch(8)

def four_close_passes(deadline):
 for unused in range(4):
  for i in range(OUTER_FD_CELLS):close_cell_nonthrowing(i,deadline)

def final_fd_scan(deadline):
 for i in range(OUTER_FD_CELLS):
  try:
   if mono(9,9)>deadline:latch(9)
   if FD_STATE[i] in (RESERVED,OWNED,TRANSFERRED,PHYSICALLY_CLOSED_ERROR):latch(9)
  except BaseException:latch(9)

def write_all_fd(number,data,deadline,state_cell):
 flags=checked_call(deadline,10,fcntl.fcntl,number,fcntl.F_GETFL)
 checked_call(deadline,10,fcntl.fcntl,number,fcntl.F_SETFL,flags|os.O_NONBLOCK)
 offset=0
 poller=checked_call(deadline,10,select.poll)
 checked_call(deadline,10,poller.register,number,select.POLLOUT|select.POLLERR|select.POLLHUP)
 for unused in range(MAX_FRAME*4):
  pre(deadline,10)
  if offset==len(data):
   post(deadline,10)
   FRAME_STATE[state_cell]=1
   return
  try:count=os.write(number,data[offset:])
  except InterruptedError:
   post(deadline,10)
   continue
  except BlockingIOError:count=0
  except BaseException:
   exception_post(deadline,10)
   latch(10)
   raise
  post(deadline,10)
  if count>0:
   offset+=count
   continue
  checked_call(deadline,10,poller.poll,1)
 latch(10)
 raise HostFailure("write-bound")

def read_capped_line(number,deadline):
 raw=bytearray()
 poller=checked_call(deadline,11,select.poll)
 checked_call(deadline,11,poller.register,number,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(MAX_FRAME*2):
  pre(deadline,11)
  try:chunk=os.read(number,4096)
  except InterruptedError:
   post(deadline,11)
   continue
  except BlockingIOError:chunk=None
  except BaseException:exception_post(deadline,11);raise
  post(deadline,11)
  if chunk==b"":
   latch(11)
   raise HostFailure("early-eof")
  if chunk:
   raw.extend(chunk)
   need(len(raw)<=MAX_FRAME and b"\r" not in raw and b"\x00" not in raw,11)
   if b"\n" in raw:
    need(raw.count(b"\n")==1 and raw.endswith(b"\n"),11)
    post(deadline,11)
    return bytes(raw)
  checked_call(deadline,11,poller.poll,1)
 raise HostFailure("read-bound")

def require_eof_no_surplus(number,deadline):
 poller=checked_call(deadline,11,select.poll)
 checked_call(deadline,11,poller.register,number,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(MAX_FRAME):
  pre(deadline,11)
  try:chunk=os.read(number,4096)
  except InterruptedError:
   post(deadline,11)
   continue
  except BlockingIOError:chunk=None
  except BaseException:exception_post(deadline,11);raise
  post(deadline,11)
  if chunk==b"":
   post(deadline,11)
   return
  if chunk:
   latch(11)
   raise HostFailure("surplus-request")
  checked_call(deadline,11,poller.poll,1)
 latch(11)
 raise HostFailure("request-eof-bound")

def reserve_slot(role):
 for i in range(MAX_LIVE_SLOTS):
  if SLOT_STATE[i] in (SLOT_FREE,SLOT_REAPED):
   SLOT_STATE[i]=SLOT_RESERVED
   SLOT_ROLE[i]=role
   SLOT_PID[i]=-1
   SLOT_RAW[i]=UNKNOWN_RAW
   return i
 latch(12)
 raise HostFailure("slot-full")

def release_slot_noncreation(i):
 need(SLOT_STATE[i]==SLOT_RESERVED and SLOT_PID[i]==-1,12)
 SLOT_STATE[i]=SLOT_FREE
 SLOT_ROLE[i]=0

def spawn_owned(role,path,argv,env,file_actions,setpgroup,deadline):
 i=reserve_slot(role)
 returned=-1
 created=False
 try:
  pre(deadline,13)
  try:
   returned=os.posix_spawn(path,argv,env,file_actions=file_actions,setpgroup=setpgroup,setsigmask=(),setsigdef=tuple(x for x in signal.valid_signals() if x not in (signal.SIGKILL,signal.SIGSTOP)))
   created=True
  finally:
   if created:
    SLOT_PID[i]=returned
    SLOT_RAW[i]=UNKNOWN_RAW
    SLOT_STATE[i]=SLOT_LIVE
  post(deadline,13)
  return i
 except BaseException:
  if not created:release_slot_noncreation(i)
  exception_post(deadline,13)
  raise

def wait_owned(i,options,deadline):
 need(SLOT_STATE[i]==SLOT_LIVE and SLOT_PID[i]>1,14)
 pre(deadline,14)
 returned_pid=-1
 returned_raw=UNKNOWN_RAW
 try:
  try:returned_pid,returned_raw=os.waitpid(SLOT_PID[i],options)
  finally:
   if returned_pid==SLOT_PID[i]:
    SLOT_RAW[i]=returned_raw
    SLOT_STATE[i]=SLOT_REAPED
  post(deadline,14)
 except InterruptedError:
  post(deadline,14)
  raise
 if returned_pid==0:
  post(deadline,14)
  return 0
 need(returned_pid==SLOT_PID[i] and SLOT_STATE[i]==SLOT_REAPED,14)
 return returned_pid

def exact_exit(raw,code):
 return os.WIFEXITED(raw) and os.WEXITSTATUS(raw)==code

def exact_signal(raw,number):
 return os.WIFSIGNALED(raw) and os.WTERMSIG(raw)==number

def verify_group_anchor(deadline):
 need(GROUP_LEADER>1 and KEEPER_PID>1,20)
 checked_call(deadline,20,os.kill,GROUP_LEADER,0)
 checked_call(deadline,20,os.kill,KEEPER_PID,0)
 leader_group=checked_call(deadline,20,os.getpgid,GROUP_LEADER)
 keeper_group=checked_call(deadline,20,os.getpgid,KEEPER_PID)
 leader_sid=checked_call(deadline,20,os.getsid,GROUP_LEADER)
 keeper_sid=checked_call(deadline,20,os.getsid,KEEPER_PID)
 need(leader_group==GROUP_LEADER and keeper_group==GROUP_LEADER and leader_sid==OUTER_SID and keeper_sid==OUTER_SID,20)

def hash_registered(i,expected_bytes,deadline):
 checked_call(deadline,15,os.lseek,fd(i),0,os.SEEK_SET)
 total=0
 lines=0
 digest=hashlib.sha256()
 while total<=expected_bytes:
  chunk=checked_call(deadline,15,os.read,fd(i),min(1048576,expected_bytes-total+1))
  if not chunk:break
  total+=len(chunk)
  lines+=chunk.count(b"\n")
  digest.update(chunk)
 need(total==expected_bytes,15)
 return total,lines,digest.hexdigest().encode("ascii")

def snapshot_source(directory,name,identity,deadline):
 input_cell=owned_open_at(fd(directory),name,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,None,16,deadline)
 mem_cell=owned_memfd(17,deadline)
 expected_bytes,expected_lf,expected_sha=identity
 try:
  held=checked_call(deadline,16,os.fstat,fd(input_cell))
  need(stat.S_ISREG(held.st_mode) and held.st_uid==0 and held.st_gid==0 and held.st_nlink==1 and held.st_size==expected_bytes,16)
  total=0
  lines=0
  digest=hashlib.sha256()
  while total<=expected_bytes:
   chunk=checked_call(deadline,16,os.read,fd(input_cell),min(1048576,expected_bytes-total+1))
   if not chunk:break
   total+=len(chunk)
   lines+=chunk.count(b"\n")
   digest.update(chunk)
   write_all_fd(fd(mem_cell),chunk,deadline,0)
   FRAME_STATE[0]=0
  need((total,lines,digest.hexdigest().encode("ascii"))==(expected_bytes,expected_lf,expected_sha),16)
  checked_call(deadline,16,fcntl.fcntl,fd(mem_cell),fcntl.F_ADD_SEALS,EXACT_SEALS)
  seals=checked_call(deadline,16,fcntl.fcntl,fd(mem_cell),fcntl.F_GET_SEALS)
  need(seals==EXACT_SEALS,16)
  again=hash_registered(mem_cell,expected_bytes,deadline)
  need(again==(expected_bytes,expected_lf,expected_sha),16)
  checked_call(deadline,16,os.lseek,fd(mem_cell),0,os.SEEK_SET)
  return mem_cell
 finally:
  exception_post(deadline,16)
  close_cell_nonthrowing(input_cell,deadline)

def anchored_nonce(nonce,expected_identity,deadline):
 need(len(nonce)==64 and all(c in b"0123456789abcdef" for c in nonce),17)
 root=owned_open_root(18,deadline)
 tmp=owned_open_at(fd(root),b"tmp",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,None,18,deadline)
 base=owned_open_at(fd(tmp),b"p27-e001-host-v10",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,None,18,deadline)
 safe=owned_open_at(fd(base),nonce,os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC|os.O_NOFOLLOW,None,18,deadline)
 pre(deadline,18);root_stat=os.fstat(fd(root));post(deadline,18)
 pre(deadline,18);tmp_stat=os.fstat(fd(tmp));post(deadline,18)
 pre(deadline,18);base_stat=os.fstat(fd(base));post(deadline,18)
 pre(deadline,18);held=os.fstat(fd(safe));post(deadline,18)
 need(all(stat.S_ISDIR(x.st_mode) and x.st_uid==0 and x.st_gid==0 for x in (root_stat,tmp_stat,base_stat)),18)
 need(stat.S_IMODE(base_stat.st_mode)&0o022==0 and stat.S_IMODE(tmp_stat.st_mode)&stat.S_ISVTX!=0,18)
 need(stat.S_ISDIR(held.st_mode) and stat.S_IMODE(held.st_mode)==0o700 and held.st_uid==0 and held.st_gid==0 and (held.st_dev,held.st_ino)==expected_identity,18)
 pre(deadline,18)
 os.fchdir(fd(safe))
 post(deadline,18)
 pre(deadline,18);current=os.stat(b".",follow_symlinks=False);post(deadline,18)
 need((current.st_dev,current.st_ino,current.st_uid,current.st_gid,stat.S_IMODE(current.st_mode))==(held.st_dev,held.st_ino,0,0,0o700),18)
 return root,tmp,base,safe

def require_test_names_absent(safe,deadline):
 for name in (b"target",b"a",b"b"):
  pre(deadline,18)
  try:os.stat(name,dir_fd=fd(safe),follow_symlinks=False);post(deadline,18);need(False,18)
  except FileNotFoundError:post(deadline,18)

def fallback_test_name_cleanup_nonthrowing(safe,deadline):
 if safe<0 or FD_STATE[safe]!=OWNED:return
 for name in (b"target",b"a",b"b"):
  try:
   try:
    pre(deadline,18);held=os.stat(name,dir_fd=fd(safe),follow_symlinks=False);post(deadline,18)
   except FileNotFoundError:
    post(deadline,18)
    continue
   if not (stat.S_ISREG(held.st_mode) and held.st_uid==0 and held.st_gid==0):
    latch(18)
    continue
   latch(18)
   pre(deadline,18);os.unlink(name,dir_fd=fd(safe));post(deadline,18)
   try:pre(deadline,18);os.stat(name,dir_fd=fd(safe),follow_symlinks=False);post(deadline,18);latch(18)
   except FileNotFoundError:post(deadline,18)
  except BaseException:exception_post(deadline,18);latch(18)

def actions_for_source(source_cell,keep,close_numbers):
 actions=[(os.POSIX_SPAWN_DUP2,fd(source_cell),100)]
 for source_number,target in keep:actions.append((os.POSIX_SPAWN_DUP2,source_number,target))
 for number in close_numbers:
  if number not in (fd(source_cell),):actions.append((os.POSIX_SPAWN_CLOSE,number))
 return tuple(actions)

def collect_output(number,deadline):
 raw=bytearray()
 poller=checked_call(deadline,19,select.poll)
 checked_call(deadline,19,poller.register,number,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(MAX_FRAME*4):
  pre(deadline,19)
  try:chunk=os.read(number,4096)
  except InterruptedError:
   post(deadline,19)
   continue
  except BlockingIOError:chunk=None
  except BaseException:exception_post(deadline,19);raise
  post(deadline,19)
  if chunk==b"":
   post(deadline,19)
   return bytes(raw)
  if chunk:
   raw.extend(chunk)
   need(len(raw)<=MAX_FRAME and b"\r" not in raw and b"\x00" not in raw,19)
   continue
  checked_call(deadline,19,poller.poll,1)
 raise HostFailure("output-bound")

def finish_output(cell,deadline):
 try:return collect_output(fd(cell),deadline)
 finally:close_cell_nonthrowing(cell,deadline)

def child_argv(mode,deadline,safe_hex,source_sha,pressure=None):
 base=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",mode,str(deadline).encode("ascii"),safe_hex,source_sha)
 if pressure is None:return base
 return base+(str(len(pressure)).encode("ascii"),hashlib.sha256(pressure).hexdigest().encode("ascii"),pressure)

def child_actions(source_cell,out_write,gate_read):
 source_number=fd(source_cell);out_number=fd(out_write);gate_number=-1 if gate_read is None else fd(gate_read)
 excluded=(source_number,out_number,gate_number)
 numbers=[]
 for i in range(OUTER_FD_CELLS):
  if FD_STATE[i]!=OWNED:continue
  number=FD_NUM[i]
  if number in excluded or number in numbers:continue
  numbers.append(number)
 actions=[]
 for number in numbers:actions.append((os.POSIX_SPAWN_CLOSE,number))
 actions.append((os.POSIX_SPAWN_DUP2,source_number,100));actions.append((os.POSIX_SPAWN_DUP2,out_number,1))
 if gate_read is not None:actions.append((os.POSIX_SPAWN_DUP2,gate_number,3))
 for number in excluded:
  if number>=0 and number not in (1,3,100):actions.append((os.POSIX_SPAWN_CLOSE,number))
 return tuple(actions)

def expected_child_line(mode,pid,sid,pgid,source_sha,safe_hex,phase):
 return TAG+b"|child=observation|mode="+mode+b"|pid="+str(pid).encode("ascii")+b"|sid="+str(sid).encode("ascii")+b"|pgid="+str(pgid).encode("ascii")+b"|image_sha=9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101|source_sha="+source_sha+b"|cwd_hex="+safe_hex+b"|phase="+phase+b"|result=PASS\n"

def spawn_child(source_cell,mode,ordinal,leader,sid,deadline,safe_hex,source_sha,pressure=None,chain=False):
 verify_group_anchor(deadline)
 out_r,out_w=owned_pipe(19,deadline)
 gate_r=gate_w=None
 if mode in (b"BLOCK0",b"EXIT23"):
  gate_r,gate_w=owned_pipe(19,deadline)
 if chain:
  command=b'exec /usr/bin/env -i LANG=C LC_ALL=C PATH=/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 PYTHONIOENCODING=UTF-8:strict PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 PYTHONUTF8=1 TZ=UTC /root/miniconda3/bin/python3 -I -S -B -P -X utf8 /proc/self/fd/100 CHAIN "$1" "$2" "$3"'
  argv=(b"/usr/bin/env",b"-i",b"/usr/bin/bash",b"--noprofile",b"--norc",b"-c",command,b"p27-e001-v10-chain",str(deadline).encode("ascii"),safe_hex,source_sha)
  path=b"/usr/bin/env"
  env={}
 else:
  argv=child_argv(mode,deadline,safe_hex,source_sha,pressure)
  path=PYTHON
  env=ENV
 actions=child_actions(source_cell,out_w,gate_r)
 try:slot=spawn_owned(ROLE_CHILD,path,argv,env,actions,leader,deadline)
 except BaseException:
  close_cell_nonthrowing(out_r,deadline);close_cell_nonthrowing(out_w,deadline)
  if gate_r is not None:close_cell_nonthrowing(gate_r,deadline);close_cell_nonthrowing(gate_w,deadline)
  raise
 close_cell_nonthrowing(out_w,deadline)
 if gate_r is not None:close_cell_nonthrowing(gate_r,deadline)
 pid=SLOT_PID[slot]
 phase=b"ready" if mode in (b"BLOCK0",b"EXIT23",b"TERM") else b"terminal"
 line=read_capped_line(fd(out_r),deadline)
 need(line==expected_child_line(mode,pid,sid,leader,source_sha,safe_hex,phase),19)
 verify_group_anchor(deadline)
 return slot,out_r,gate_w,line

def reap_expected(slot,kind,deadline):
 while SLOT_STATE[slot]==SLOT_LIVE:
  try:wait_owned(slot,0,deadline)
  except InterruptedError:
   post(deadline,20)
   continue
 raw=SLOT_RAW[slot]
 if kind==b"EXIT0":need(exact_exit(raw,0),20)
 elif kind==b"EXIT23":need(exact_exit(raw,23),20)
 elif kind==b"TERM":need(exact_signal(raw,signal.SIGTERM),20)
 elif kind==b"KILL":need(exact_signal(raw,signal.SIGKILL),20)
 else:need(False,20)
 return raw

def p05_alarm(unused_signum,unused_frame):
 raise InterruptedError(errno.EINTR,"p05-bounded-eintr")

def sealed_synthetic(child_cell,child_identity,deadline):
 expected_bytes,expected_lf,expected_sha=child_identity
 need(expected_bytes+2<251414,21)
 synthetic_cell=owned_memfd(21,deadline)
 try:
  source=bytearray()
  checked_call(deadline,21,os.lseek,fd(child_cell),0,os.SEEK_SET)
  while len(source)<=expected_bytes:
   chunk=checked_call(deadline,21,os.read,fd(child_cell),min(1048576,expected_bytes-len(source)+1))
   if not chunk:break
   source.extend(chunk)
  need(len(source)==expected_bytes and source.count(b"\n")==expected_lf and hashlib.sha256(source).hexdigest().encode("ascii")==expected_sha,21)
  synthetic=bytes(source)+b"\n#"+b"x"*(251414-len(source)-2)
  need(len(synthetic)==251414,21)
  write_all_fd(fd(synthetic_cell),synthetic,deadline,0)
  FRAME_STATE[0]=0
  checked_call(deadline,21,fcntl.fcntl,fd(synthetic_cell),fcntl.F_ADD_SEALS,EXACT_SEALS)
  seals=checked_call(deadline,21,fcntl.fcntl,fd(synthetic_cell),fcntl.F_GET_SEALS)
  need(seals==EXACT_SEALS,21)
  identity=hash_registered(synthetic_cell,251414,deadline)
  need(identity[0]==251414 and identity[2]==hashlib.sha256(synthetic).hexdigest().encode("ascii"),21)
  return synthetic_cell,synthetic,identity[2]
 except BaseException:
  exception_post(deadline,21)
  close_cell_nonthrowing(synthetic_cell,deadline)
  raise

def broker_operation(op,child_cell,child_identity,leader,sid,deadline,safe_hex):
 pids=[]
 statuses=[]
 observations=[]
 payload=[]
 if op==b"P00_E2BIG":
  synthetic_cell,pressure,synthetic_sha=sealed_synthetic(child_cell,child_identity,deadline)
  try:
   try:slot,out_r,gate,line=spawn_child(synthetic_cell,b"INFO",0,leader,sid,deadline,safe_hex,synthetic_sha,pressure=pressure)
   except OSError as error:
    need(error.errno==errno.E2BIG,21)
   payload.append(b"source_bytes=251414,returned=0,e2big=1,sha="+synthetic_sha)
   else:
    raw=reap_expected(slot,b"EXIT0",deadline)
    rest=finish_output(out_r,deadline)
    need(rest==b"",21)
    pids.append(SLOT_PID[slot]);statuses.append(raw);observations.append(line)
    payload.append(b"INFO:"+line.hex().encode("ascii"))
    payload.append(b"source_bytes=251414,returned=1,e2big=0,sha="+synthetic_sha)
  finally:close_cell_nonthrowing(synthetic_cell,deadline)
 elif op==b"P01C_INFO":
  slot,out_r,gate,line=spawn_child(child_cell,b"INFO",0,leader,sid,deadline,safe_hex,child_identity[2])
  raw=reap_expected(slot,b"EXIT0",deadline);need(finish_output(out_r,deadline)==b"",22)
  pids.append(SLOT_PID[slot]);statuses.append(raw);observations.append(line)
  payload.append(b"INFO:"+line.hex().encode("ascii"))
 elif op==b"P05_WAIT":
  slot,out_r,gate,line=spawn_child(child_cell,b"EXIT23",0,leader,sid,deadline,safe_hex,child_identity[2])
  need(wait_owned(slot,os.WNOHANG,deadline)==0,22)
  pre(deadline,22);old_handler=signal.getsignal(signal.SIGALRM);post(deadline,22)
  pre(deadline,22);signal.signal(signal.SIGALRM,p05_alarm);post(deadline,22)
  pre(deadline,22);signal.pthread_sigmask(signal.SIG_UNBLOCK,{signal.SIGALRM});post(deadline,22)
  interrupted=0
  try:
   pre(deadline,22);signal.setitimer(signal.ITIMER_REAL,0.001);post(deadline,22)
   try:wait_owned(slot,0,deadline)
   except InterruptedError:interrupted=1
  finally:
   try:pre(deadline,22)
   except BaseException:latch(22)
   try:signal.setitimer(signal.ITIMER_REAL,0.0)
   except BaseException:latch(22)
   exception_post(deadline,22)
   try:pre(deadline,22)
   except BaseException:latch(22)
   try:signal.pthread_sigmask(signal.SIG_BLOCK,{signal.SIGALRM})
   except BaseException:latch(22)
   exception_post(deadline,22)
   try:pre(deadline,22)
   except BaseException:latch(22)
   try:signal.signal(signal.SIGALRM,old_handler)
   except BaseException:latch(22)
   exception_post(deadline,22)
  need(interrupted==1 and SLOT_STATE[slot]==SLOT_LIVE,22)
  write_all_fd(fd(gate),b"G",deadline,0);FRAME_STATE[0]=0;close_cell_nonthrowing(gate,deadline)
  raw=reap_expected(slot,b"EXIT23",deadline);need(finish_output(out_r,deadline)==b"",22)
  try:pre(deadline,22);os.waitpid(SLOT_PID[slot],0);post(deadline,22);need(False,22)
  except ChildProcessError:post(deadline,22)
  pids.append(SLOT_PID[slot]);statuses.append(raw);observations.append(line)
  slot2,out_r2,gate2,line2=spawn_child(child_cell,b"TERM",1,leader,sid,deadline,safe_hex,child_identity[2])
  raw2=reap_expected(slot2,b"TERM",deadline);need(finish_output(out_r2,deadline)==b"",22)
  pids.append(SLOT_PID[slot2]);statuses.append(raw2);observations.append(line2)
  payload.append(b"P05:"+(line+line2).hex().encode("ascii"))
 elif op==b"P08_TOPOLOGY":
  slot,out_r,gate,line=spawn_child(child_cell,b"BLOCK0",0,leader,sid,deadline,safe_hex,child_identity[2])
  pid=SLOT_PID[slot]
  need(wait_owned(slot,os.WNOHANG,deadline)==0,23)
  pre(deadline,23);observed_sid=os.getsid(pid);post(deadline,23)
  pre(deadline,23);observed_group=os.getpgid(pid);post(deadline,23)
  need(observed_sid==sid and observed_group==leader,23)
  pre(deadline,23);os.kill(pid,0);post(deadline,23)
  write_all_fd(fd(gate),b"G",deadline,0);FRAME_STATE[0]=0;close_cell_nonthrowing(gate,deadline)
  raw=reap_expected(slot,b"EXIT0",deadline);need(finish_output(out_r,deadline)==b"",23)
  try:pre(deadline,23);os.kill(pid,0);post(deadline,23);need(False,23)
  except ProcessLookupError:post(deadline,23)
  pids.append(pid);statuses.append(raw);observations.append(line);payload.append(b"P08:"+line.hex().encode("ascii"))
 elif op==b"P09_KILL":
  slot,out_r,gate,line=spawn_child(child_cell,b"BLOCK0",0,leader,sid,deadline,safe_hex,child_identity[2])
  need(wait_owned(slot,os.WNOHANG,deadline)==0,24)
  pid=SLOT_PID[slot]
  selected=mono(24,24)
  pre(deadline,24);os.kill(pid,signal.SIGKILL);post(deadline,24)
  close_cell_nonthrowing(gate,deadline)
  raw=reap_expected(slot,b"KILL",deadline)
  finished=mono(24,24)
  need(finished-selected<=KILL_REAP_PROGRESS_NS and finish_output(out_r,deadline)==b"",24)
  pids.append(pid);statuses.append(raw);observations.append(line);payload.append(b"BLOCK0:"+line.hex().encode("ascii"));payload.append(b"reap_start_ns="+str(selected).encode("ascii")+b",reap_end_ns="+str(finished).encode("ascii"))
 elif op==b"P10_INFO16":
  for ordinal in range(16):
   slot,out_r,gate,line=spawn_child(child_cell,b"INFO",ordinal,leader,sid,deadline,safe_hex,child_identity[2])
   raw=reap_expected(slot,b"EXIT0",deadline);need(finish_output(out_r,deadline)==b"",25)
   pids.append(SLOT_PID[slot]);statuses.append(raw);observations.append(line)
   payload.append(b"INFO:"+line.hex().encode("ascii"))
  duplicates=len(pids)-len(set(pids))
 elif op==b"P12_CHAIN":
  slot,out_r,gate,line=spawn_child(child_cell,b"CHAIN",0,leader,sid,deadline,safe_hex,child_identity[2],chain=True)
  raw=reap_expected(slot,b"EXIT0",deadline);need(finish_output(out_r,deadline)==b"",26)
  pids.append(SLOT_PID[slot]);statuses.append(raw);observations.append(line);payload.append(b"CHAIN:"+line.hex().encode("ascii"))
 else:need(False,26)
 need(len(pids)==len(statuses)==len(observations),26)
 verify_group_anchor(deadline)
 return tuple(pids),tuple(statuses),tuple(observations),b";".join(payload)

def parse_request(raw,probe,op,nonce,child_sha):
 expected=TAG+b"|broker=request|seq=0|probe="+probe+b"|op="+op+b"|nonce="+nonce+b"|child_sha="+child_sha+b"|end=1\n"
 need(raw==expected,27)

def response(probe,op,pids,statuses,payload):
 p=b",".join(str(x).encode("ascii") for x in pids)
 s=b",".join(str(x).encode("ascii") for x in statuses)
 return TAG+b"|broker=response|seq=0|probe="+probe+b"|op="+op+b"|spawned="+str(len(pids)).encode("ascii")+b"|reaped="+str(len(statuses)).encode("ascii")+b"|pids="+p+b"|statuses="+s+b"|payload_hex="+payload.hex().encode("ascii")+b"|result=PASS\n"

def cleanup_signal(i,number,deadline):
 if SLOT_STATE[i]!=SLOT_LIVE:return 0
 selected=mono(28,28)
 try:
  pre(deadline,28)
  os.kill(SLOT_PID[i],number)
  post(deadline,28)
 except ProcessLookupError:
  exception_post(deadline,28)
  latch(28)
 except BaseException:exception_post(deadline,28);latch(28)
 if mono(28,28)-selected>KILL_REAP_PROGRESS_NS:latch(28)
 return selected

def cleanup_reap(i,expected,deadline,selected):
 if SLOT_STATE[i]!=SLOT_LIVE:return
 term_horizon=checked_add(selected,40000000)
 if term_horizon>deadline:term_horizon=deadline
 rescued=False
 kill_selected=0
 for unused in range(4096):
  try:
   wait_owned(i,os.WNOHANG,term_horizon)
  except InterruptedError:latch(28);post(term_horizon,28);continue
  except HostFailure:exception_post(term_horizon,28);break
  except BaseException:exception_post(term_horizon,28);latch(28);break
  if SLOT_STATE[i]==SLOT_REAPED:break
  try:
   pre(term_horizon,28)
   select.poll().poll(1)
   post(term_horizon,28)
  except BaseException:exception_post(term_horizon,28);break
 if SLOT_STATE[i]==SLOT_LIVE:
  rescued=True
  latch(28)
  kill_selected=mono(28,28)
  try:
   pre(deadline,28);os.kill(SLOT_PID[i],signal.SIGKILL);post(deadline,28)
  except BaseException:exception_post(deadline,28);latch(28)
  for unused in range(64):
   try:
    wait_owned(i,0,deadline)
    break
   except InterruptedError:latch(28);post(deadline,28);continue
   except BaseException:exception_post(deadline,28);latch(28);break
 if SLOT_STATE[i]!=SLOT_REAPED:latch(28);return
 if rescued and not exact_signal(SLOT_RAW[i],signal.SIGKILL):latch(28)
 if expected==b"TERM" and not rescued and not exact_signal(SLOT_RAW[i],signal.SIGTERM):latch(28)
 if rescued and mono(28,28)-kill_selected>KILL_REAP_PROGRESS_NS:latch(28)
 if not rescued and mono(28,28)>term_horizon:latch(28)

def verify_hold_eof(role,deadline):
 cell=HOLD_CELL_BY_ROLE[role]
 if cell<0:return
 try:require_eof_no_surplus(fd(cell),deadline)
 except BaseException:exception_post(deadline,28);latch(28)

def cleanup_emergency_exact(i,deadline):
 if SLOT_STATE[i]!=SLOT_LIVE:return
 latch(28)
 kill_selected=0
 try:
  kill_selected=mono(28,28)
  try:pre(deadline,28)
  except BaseException:latch(28)
  os.kill(SLOT_PID[i],signal.SIGKILL)
  try:post(deadline,28)
  except BaseException:latch(28)
 except BaseException:exception_post(deadline,28);latch(28)
 for unused in range(64):
  if SLOT_STATE[i]!=SLOT_LIVE:break
  returned_pid=-1
  returned_raw=UNKNOWN_RAW
  try:
   try:pre(deadline,28)
   except BaseException:latch(28)
   try:returned_pid,returned_raw=os.waitpid(SLOT_PID[i],0)
   finally:
    if returned_pid==SLOT_PID[i]:
     SLOT_RAW[i]=returned_raw
     SLOT_STATE[i]=SLOT_REAPED
   try:post(deadline,28)
   except BaseException:latch(28)
  except InterruptedError:
   latch(28)
   try:post(deadline,28)
   except BaseException:latch(28)
   continue
  except BaseException:
   latch(28)
   try:post(deadline,28)
   except BaseException:latch(28)
   continue
  if returned_pid==SLOT_PID[i]:break
 if SLOT_STATE[i]!=SLOT_REAPED or not exact_signal(SLOT_RAW[i],signal.SIGKILL):latch(28)
 try:
  if kill_selected and mono(28,28)-kill_selected>KILL_REAP_PROGRESS_NS:latch(28)
 except BaseException:latch(28)
 try:post(deadline,28)
 except BaseException:latch(28)

def cleanup_registry(pass_candidate,deadline):
 global ADMISSION_CLOSED
 ADMISSION_CLOSED=1
 roles=(ROLE_CHILD,ROLE_MARKER,ROLE_LAUNCHER,ROLE_KEEPER)
 for role in roles:
  for i in range(MAX_LIVE_SLOTS):
   if SLOT_ROLE[i]!=role or SLOT_STATE[i]!=SLOT_LIVE:continue
   try:
    if pass_candidate and role in (ROLE_LAUNCHER,ROLE_KEEPER):
     observed=wait_owned(i,os.WNOHANG,deadline)
     if observed!=0:
      latch(28)
      raise HostFailure("premature-leaf-exit")
     checked_call(deadline,28,os.kill,SLOT_PID[i],0)
    if pass_candidate and role in (ROLE_CHILD,ROLE_MARKER):latch(28)
    selected=cleanup_signal(i,signal.SIGTERM,deadline)
    cleanup_reap(i,b"TERM" if pass_candidate and role in (ROLE_LAUNCHER,ROLE_KEEPER) else b"ACTUAL",deadline,selected)
   except BaseException:
    exception_post(deadline,28)
    latch(28)
    cleanup_emergency_exact(i,deadline)
   if SLOT_STATE[i]==SLOT_LIVE:cleanup_emergency_exact(i,deadline)
   if role in (ROLE_LAUNCHER,ROLE_KEEPER):verify_hold_eof(role,deadline)
 for i in range(MAX_LIVE_SLOTS):
  if SLOT_STATE[i] in (SLOT_RESERVED,SLOT_LIVE):latch(28)

def final_fault_scan(deadline):
 try:
  post(deadline,29)
  for value in FATAL:
   if value:latch(29)
  for i in range(MAX_LIVE_SLOTS):
   if SLOT_STATE[i] in (SLOT_RESERVED,SLOT_LIVE):latch(29)
  final_fd_scan(deadline)
  post(deadline,29)
 except BaseException:latch(29)

def raw_for_role(role):
 for i in range(MAX_LIVE_SLOTS):
  if SLOT_ROLE[i]==role:return SLOT_RAW[i]
 return UNKNOWN_RAW

def decimal(raw,low,high):
 need(raw and raw.isdigit(),30)
 value=int(raw)
 need(str(value).encode("ascii")==raw and low<=value<=high,30)
 return value

def hexa(raw,count):
 need(len(raw)==count and all(c in b"0123456789abcdef" for c in raw),30)
 return raw

def parse_identity(raw):
 parts=raw.split(b",")
 need(len(parts)==3,30)
 return decimal(parts[0],1,MAX_I63),decimal(parts[1],1,MAX_I63),hexa(parts[2],64)

def main():
 global OPERATIONAL_DEADLINE,POST_OPERATION_HOST_DEADLINE,POST_ARMED,ADMISSION_CLOSED,GROUP_LEADER,KEEPER_PID,OUTER_SID
 pass_candidate=False
 marker_report=b""
 probe=b"invalid"
 launcher_slot=keeper_slot=marker_slot=-1
 source_cells=()
 request_r=response_w=marker_out_r=-1
 launcher_hold_r=keeper_hold_r=-1
 safe_cell=-1
 try:
  verify_arithmetic()
  need(len(sys.argv) in (18,31) and sys.argv[0]=="/proc/self/fd/100",30)
  probe=os.fsencode(sys.argv[1]);need(probe in PROBES,30)
  nonce=hexa(os.fsencode(sys.argv[2]),64)
  budget=decimal(os.fsencode(sys.argv[3]),2000000000,15000000000)
  need(decimal(os.fsencode(sys.argv[4]),1,MAX_I63)==FD_RETURN_COMMIT_PROGRESS_NS,30)
  need(decimal(os.fsencode(sys.argv[5]),1,MAX_I63)==OWNER_CONTROL_PROGRESS_NS,30)
  need(decimal(os.fsencode(sys.argv[6]),1,MAX_I63)==KILL_REAP_PROGRESS_NS,30)
  need(decimal(os.fsencode(sys.argv[7]),1,MAX_I63)==TERMINAL_FRAMING_PROGRESS_NS,30)
  need(decimal(os.fsencode(sys.argv[8]),1,MAX_I63)==ACTOR_ACK_PROGRESS_NS,30)
  need(os.fsencode(sys.argv[9])==COMMIT_WINDOW_TOKEN and os.fsencode(sys.argv[10])==OWNER_SURVIVAL_TOKEN,30)
  safe_identity=(decimal(os.fsencode(sys.argv[11]),1,MAX_I63),decimal(os.fsencode(sys.argv[12]),1,MAX_I63))
  identities=tuple(parse_identity(os.fsencode(x)) for x in sys.argv[13:18])
  need(len(identities)==5,30)
  p01c=tuple(os.fsencode(x) for x in sys.argv[18:31]) if probe==b"P01C" else ()
  need((probe==b"P01C" and len(p01c)==13) or (probe!=b"P01C" and len(sys.argv)==18),30)
  start=mono(30,30)
  OPERATIONAL_DEADLINE=checked_add(start,budget)
  pre(OPERATIONAL_DEADLINE,30)
  pre(OPERATIONAL_DEADLINE,30);outer_pid=os.getpid();post(OPERATIONAL_DEADLINE,30)
  pre(OPERATIONAL_DEADLINE,30);outer_group=os.getpgrp();post(OPERATIONAL_DEADLINE,30)
  need(outer_pid!=outer_group,30)
  pre(OPERATIONAL_DEADLINE,30);cpu_limit=resource.getrlimit(resource.RLIMIT_CPU);post(OPERATIONAL_DEADLINE,30)
  need(cpu_limit[1]==resource.RLIM_INFINITY,30)
  pre(OPERATIONAL_DEADLINE,30);valid_signals=signal.valid_signals();post(OPERATIONAL_DEADLINE,30)
  catchable=set(int(x) for x in valid_signals if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP)))
  pre(OPERATIONAL_DEADLINE,30);signal.pthread_sigmask(signal.SIG_BLOCK,catchable);post(OPERATIONAL_DEADLINE,30)
  pre(OPERATIONAL_DEADLINE,30);trace_hook=sys.gettrace();post(OPERATIONAL_DEADLINE,30)
  pre(OPERATIONAL_DEADLINE,30);profile_hook=sys.getprofile();post(OPERATIONAL_DEADLINE,30)
  need(trace_hook is None and profile_hook is None,30)
  outer_exec=adopt_outer(100,18)
  pre(OPERATIONAL_DEADLINE,30);outer_seals=fcntl.fcntl(100,fcntl.F_GET_SEALS);post(OPERATIONAL_DEADLINE,30);need(outer_seals==EXACT_SEALS,30)
  need(hash_registered(outer_exec,identities[0][0],OPERATIONAL_DEADLINE)==identities[0],30)
  root,tmp,base,safe_cell=anchored_nonce(nonce,safe_identity,OPERATIONAL_DEADLINE)
  require_test_names_absent(safe_cell,OPERATIONAL_DEADLINE)
  source_cells=tuple(snapshot_source(safe_cell,SOURCE_NAMES[i],identities[i],OPERATIONAL_DEADLINE) for i in range(5))
  for i,cell in enumerate(source_cells):
   need(hash_registered(cell,identities[i][0],OPERATIONAL_DEADLINE)==identities[i],30)
  pre(OPERATIONAL_DEADLINE,30);safe_bytes=os.getcwdb();post(OPERATIONAL_DEADLINE,30);safe_hex=safe_bytes.hex().encode("ascii")
  pre(OPERATIONAL_DEADLINE,30);outer_sid=os.getsid(0);post(OPERATIONAL_DEADLINE,30)
  OUTER_SID=outer_sid
  post(OPERATIONAL_DEADLINE,30)

  lh_r,lh_w=owned_pipe(31,OPERATIONAL_DEADLINE)
  lr_r,lr_w=owned_pipe(31,OPERATIONAL_DEADLINE)
  kh_r,kh_w=owned_pipe(31,OPERATIONAL_DEADLINE)
  kr_r,kr_w=owned_pipe(31,OPERATIONAL_DEADLINE)
  request_r,request_w=owned_pipe(31,OPERATIONAL_DEADLINE)
  response_r,response_w=owned_pipe(31,OPERATIONAL_DEADLINE)
  marker_out_r,marker_out_w=owned_pipe(31,OPERATIONAL_DEADLINE)

  launch_actions=((os.POSIX_SPAWN_DUP2,fd(source_cells[2]),100),(os.POSIX_SPAWN_DUP2,fd(lh_w),3),(os.POSIX_SPAWN_DUP2,fd(lr_w),4))
  launcher_slot=spawn_owned(ROLE_LAUNCHER,PYTHON,(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",str(OPERATIONAL_DEADLINE).encode("ascii"),identities[2][2]),ENV,launch_actions,0,OPERATIONAL_DEADLINE)
  leader=SLOT_PID[launcher_slot]
  GROUP_LEADER=leader
  close_cell_nonthrowing(lh_w,OPERATIONAL_DEADLINE);close_cell_nonthrowing(lr_w,OPERATIONAL_DEADLINE)
  need(read_capped_line(fd(lr_r),OPERATIONAL_DEADLINE)==TAG+b"|launcher=ready\n",31)
  close_cell_nonthrowing(lr_r,OPERATIONAL_DEADLINE)
  launcher_hold_r=lh_r
  HOLD_CELL_BY_ROLE[ROLE_LAUNCHER]=lh_r

  keeper_actions=((os.POSIX_SPAWN_DUP2,fd(source_cells[1]),100),(os.POSIX_SPAWN_DUP2,fd(kh_w),3),(os.POSIX_SPAWN_DUP2,fd(kr_w),4))
  keeper_slot=spawn_owned(ROLE_KEEPER,PYTHON,(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",str(OPERATIONAL_DEADLINE).encode("ascii"),identities[1][2]),ENV,keeper_actions,leader,OPERATIONAL_DEADLINE)
  KEEPER_PID=SLOT_PID[keeper_slot]
  close_cell_nonthrowing(kh_w,OPERATIONAL_DEADLINE);close_cell_nonthrowing(kr_w,OPERATIONAL_DEADLINE)
  need(read_capped_line(fd(kr_r),OPERATIONAL_DEADLINE)==TAG+b"|keeper=ready\n",31)
  close_cell_nonthrowing(kr_r,OPERATIONAL_DEADLINE)
  keeper_hold_r=kh_r
  HOLD_CELL_BY_ROLE[ROLE_KEEPER]=kh_r
  verify_group_anchor(OPERATIONAL_DEADLINE)

  marker_args=(PYTHON,b"-I",b"-S",b"-B",b"-P",b"-X",b"utf8",b"/proc/self/fd/100",probe,nonce,str(OPERATIONAL_DEADLINE).encode("ascii"),str(MARKER_CLOSE_RESERVE_NS).encode("ascii"),safe_hex,identities[3][2],identities[4][2])+p01c
  marker_actions=((os.POSIX_SPAWN_DUP2,fd(source_cells[3]),100),(os.POSIX_SPAWN_DUP2,fd(request_w),5),(os.POSIX_SPAWN_DUP2,fd(response_r),6),(os.POSIX_SPAWN_DUP2,fd(safe_cell),7),(os.POSIX_SPAWN_DUP2,fd(marker_out_w),1))
  marker_slot=spawn_owned(ROLE_MARKER,PYTHON,marker_args,ENV,marker_actions,leader,OPERATIONAL_DEADLINE)
  pre(OPERATIONAL_DEADLINE,31);marker_group=os.getpgid(SLOT_PID[marker_slot]);post(OPERATIONAL_DEADLINE,31)
  pre(OPERATIONAL_DEADLINE,31);marker_sid=os.getsid(SLOT_PID[marker_slot]);post(OPERATIONAL_DEADLINE,31)
  need(marker_group==leader and marker_sid==outer_sid,31)
  close_cell_nonthrowing(request_w,OPERATIONAL_DEADLINE);close_cell_nonthrowing(response_r,OPERATIONAL_DEADLINE);close_cell_nonthrowing(marker_out_w,OPERATIONAL_DEADLINE)

  mapping=dict(BROKER)
  if probe in mapping:
   op=mapping[probe]
   raw=read_capped_line(fd(request_r),OPERATIONAL_DEADLINE)
   parse_request(raw,probe,op,nonce,identities[4][2])
   require_eof_no_surplus(fd(request_r),OPERATIONAL_DEADLINE)
   pids,statuses,observations,payload=broker_operation(op,source_cells[4],identities[4],leader,outer_sid,OPERATIONAL_DEADLINE,safe_hex)
   frame=response(probe,op,pids,statuses,payload)
   write_all_fd(fd(response_w),frame,OPERATIONAL_DEADLINE,1)
   post(OPERATIONAL_DEADLINE,31)
  else:
   need(probe in LOCAL,31)
  close_cell_nonthrowing(response_w,OPERATIONAL_DEADLINE)
  while SLOT_STATE[marker_slot]==SLOT_LIVE:
   try:wait_owned(marker_slot,0,OPERATIONAL_DEADLINE)
   except InterruptedError:post(OPERATIONAL_DEADLINE,31);continue
  need(exact_exit(SLOT_RAW[marker_slot],0),31)
  marker_report=finish_output(marker_out_r,OPERATIONAL_DEADLINE)
  need(marker_report.startswith(TAG+b"|marker=report|schema=10|probe="+probe+b"\n") and marker_report.endswith(TAG+b"|probe="+probe+b"|result=PASS\n"),31)
  require_eof_no_surplus(fd(request_r),OPERATIONAL_DEADLINE)
  close_cell_nonthrowing(request_r,OPERATIONAL_DEADLINE)
  post(OPERATIONAL_DEADLINE,31)
  pass_candidate=True
 except BaseException:exception_post(OPERATIONAL_DEADLINE,31);latch(31)
 finally:
  if not POST_ARMED:
   try:
    POST_OPERATION_HOST_DEADLINE=checked_add(mono(31,31),POST_OPERATION_HOST_BOUND_NS)
    POST_ARMED=1
   except BaseException:latch(31)
  cleanup_registry(pass_candidate,POST_OPERATION_HOST_DEADLINE)
  fallback_test_name_cleanup_nonthrowing(safe_cell,POST_OPERATION_HOST_DEADLINE)
  four_close_passes(POST_OPERATION_HOST_DEADLINE)
  final_fault_scan(POST_OPERATION_HOST_DEADLINE)

 role_statuses=b"launcher:"+str(raw_for_role(ROLE_LAUNCHER)).encode("ascii")+b",keeper:"+str(raw_for_role(ROLE_KEEPER)).encode("ascii")+b",marker:"+str(raw_for_role(ROLE_MARKER)).encode("ascii")+b",child:"+str(raw_for_role(ROLE_CHILD)).encode("ascii")
 candidate=TAG+b"|outer=candidate|probe="+probe+b"|slots=4|all_reaped="+(b"1" if all(x not in (SLOT_RESERVED,SLOT_LIVE) for x in SLOT_STATE) else b"0")+b"|role_statuses="+role_statuses+b"|fatal="+(b"0" if not any(FATAL) else b"1")+b"|result="+(b"PASS" if pass_candidate and not any(FATAL) else b"FAIL")+b"\n"
 try:
  write_all_fd(1,marker_report+candidate,POST_OPERATION_HOST_DEADLINE,2)
  post(POST_OPERATION_HOST_DEADLINE,31)
 except BaseException:exception_post(POST_OPERATION_HOST_DEADLINE,31);latch(31)
 final_fault_scan(POST_OPERATION_HOST_DEADLINE)
 terminal=TAG+b"|outer=terminal|probe="+probe+b"|all_reaped="+(b"1" if all(x not in (SLOT_RESERVED,SLOT_LIVE) for x in SLOT_STATE) else b"0")+b"|role_statuses="+role_statuses+b"|frame_complete="+(b"1" if FRAME_STATE[2] else b"0")+b"|fatal="+(b"0" if not any(FATAL) else b"1")+b"|result="+(b"PASS" if pass_candidate and not any(FATAL) and FRAME_STATE[2] else b"FAIL")+b"\n"
 try:
  write_all_fd(1,terminal,POST_OPERATION_HOST_DEADLINE,3)
  post(POST_OPERATION_HOST_DEADLINE,31)
 except BaseException:exception_post(POST_OPERATION_HOST_DEADLINE,31);latch(31)
 post(POST_OPERATION_HOST_DEADLINE,31)
 raise SystemExit(0 if pass_candidate and not any(FATAL) and FRAME_STATE[2] and FRAME_STATE[3] else 90)

main()
UNIFIED OUTER V10 SOURCE END

V10 STAGE 1 OUTER SOURCE COMPLETE

UNIFIED KEEPER V10 SOURCE BEGIN
import fcntl
import hashlib
import os
import signal
import sys
import time

TAG=b"P27E001V10"
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL

def need(value):
 if not value:raise SystemExit(91)

def source_hash(deadline):
 need(time.monotonic_ns()<=deadline);seals=fcntl.fcntl(100,fcntl.F_GET_SEALS);need(time.monotonic_ns()<=deadline);need(seals==EXACT_SEALS)
 need(time.monotonic_ns()<=deadline);os.lseek(100,0,os.SEEK_SET);need(time.monotonic_ns()<=deadline)
 digest=hashlib.sha256()
 while True:
  need(time.monotonic_ns()<=deadline);chunk=os.read(100,1048576);need(time.monotonic_ns()<=deadline)
  if not chunk:break
  digest.update(chunk)
 return digest.hexdigest().encode("ascii")

need(len(sys.argv)==3 and sys.argv[0]=="/proc/self/fd/100")
deadline=int(sys.argv[1])
expected=os.fsencode(sys.argv[2])
need(source_hash(deadline)==expected and time.monotonic_ns()<=deadline)
need(time.monotonic_ns()<=deadline);os.close(100);need(time.monotonic_ns()<=deadline)
need(time.monotonic_ns()<=deadline);written=os.write(4,TAG+b"|keeper=ready\n");need(time.monotonic_ns()<=deadline);need(written==len(TAG)+14)
need(time.monotonic_ns()<=deadline);os.close(4);need(time.monotonic_ns()<=deadline)
need(time.monotonic_ns()<=deadline)
signal.pause()
need(time.monotonic_ns()<=deadline)
raise SystemExit(92)
UNIFIED KEEPER V10 SOURCE END

UNIFIED LAUNCHER V10 SOURCE BEGIN
import fcntl
import hashlib
import os
import signal
import sys
import time

TAG=b"P27E001V10"
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL

def need(value):
 if not value:raise SystemExit(91)

def source_hash(deadline):
 need(time.monotonic_ns()<=deadline);seals=fcntl.fcntl(100,fcntl.F_GET_SEALS);need(time.monotonic_ns()<=deadline);need(seals==EXACT_SEALS)
 need(time.monotonic_ns()<=deadline);os.lseek(100,0,os.SEEK_SET);need(time.monotonic_ns()<=deadline)
 digest=hashlib.sha256()
 while True:
  need(time.monotonic_ns()<=deadline);chunk=os.read(100,1048576);need(time.monotonic_ns()<=deadline)
  if not chunk:break
  digest.update(chunk)
 return digest.hexdigest().encode("ascii")

need(len(sys.argv)==3 and sys.argv[0]=="/proc/self/fd/100")
deadline=int(sys.argv[1])
expected=os.fsencode(sys.argv[2])
need(source_hash(deadline)==expected and time.monotonic_ns()<=deadline)
need(time.monotonic_ns()<=deadline);os.close(100);need(time.monotonic_ns()<=deadline)
need(time.monotonic_ns()<=deadline);written=os.write(4,TAG+b"|launcher=ready\n");need(time.monotonic_ns()<=deadline);need(written==len(TAG)+16)
need(time.monotonic_ns()<=deadline);os.close(4);need(time.monotonic_ns()<=deadline)
need(time.monotonic_ns()<=deadline)
signal.pause()
need(time.monotonic_ns()<=deadline)
raise SystemExit(92)
UNIFIED LAUNCHER V10 SOURCE END

UNIFIED MARKER V10 SOURCE BEGIN
import array
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

TAG=b"P27E001V10"
PYTHON=b"/root/miniconda3/bin/python3"
PYRES=b"/root/miniconda3/bin/python3.12"
PY_BYTES=30626264
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
PROBES=(b"P00",b"P01D",b"P01C",b"P02",b"P03",b"P04",b"P05",b"P06",b"P07",b"P08",b"P09",b"P10",b"P11",b"P12",b"P13")
LOCAL=(b"P01D",b"P02",b"P03",b"P04",b"P06",b"P07",b"P11",b"P13")
BROKER=((b"P00",b"P00_E2BIG"),(b"P01C",b"P01C_INFO"),(b"P05",b"P05_WAIT"),(b"P08",b"P08_TOPOLOGY"),(b"P09",b"P09_KILL"),(b"P10",b"P10_INFO16"),(b"P12",b"P12_CHAIN"))
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
MAX_I63=(1<<63)-1
MARKER_FD_CELLS=64
FREE=0
RESERVED=1
OWNED=2
CLOSED=3
PHYSICALLY_CLOSED_ERROR=4
FD_NUM=array.array("i",[-1])*MARKER_FD_CELLS
FD_STATE=bytearray(MARKER_FD_CELLS)
FATAL=bytearray(24)
WORK_DEADLINE=0
OPERATIONAL_DEADLINE=0

class MarkerFailure(Exception):
 pass

def latch(cell):
 if 0<=cell<len(FATAL):FATAL[cell]=1

def need(value,cell):
 if not value:
  latch(cell)
  raise MarkerFailure(str(cell))

def mono(cell=0):
 try:value=time.monotonic_ns()
 except BaseException:
  latch(cell)
  raise
 need(type(value)is int and value>=0,cell)
 return value

def pre(deadline,cell):need(mono(cell)<=deadline,cell)
def post(deadline,cell):need(mono(cell)<=deadline,cell)
def exception_post(deadline,cell):
 try:post(deadline,cell)
 except BaseException:latch(cell)

def checked_call(deadline,cell,fn,*args):
 pre(deadline,cell)
 try:value=fn(*args)
 except BaseException:
  exception_post(deadline,cell)
  raise
 post(deadline,cell)
 return value

def adopt(number):
 for i in range(MARKER_FD_CELLS):
  if FD_STATE[i]==FREE:
   FD_STATE[i]=RESERVED
   FD_NUM[i]=number
   FD_STATE[i]=OWNED
   return i
 raise MarkerFailure("adopt-full")

def reserve():
 for i in range(MARKER_FD_CELLS):
  if FD_STATE[i]==FREE:
   FD_STATE[i]=RESERVED
   FD_NUM[i]=-1
   return i
 raise MarkerFailure("fd-full")

def release_noncreation(i):
 need(FD_STATE[i]==RESERVED and FD_NUM[i]==-1,1)
 FD_STATE[i]=FREE

def owned_open(path,flags,mode=None,directory=None):
 i=reserve()
 returned=-1
 created=False
 try:
  pre(WORK_DEADLINE,1)
  try:
   if directory is None:returned=os.open(path,flags) if mode is None else os.open(path,flags,mode)
   else:returned=os.open(path,flags,dir_fd=directory) if mode is None else os.open(path,flags,mode,dir_fd=directory)
   created=True
  finally:
   if created:
    FD_NUM[i]=returned
    FD_STATE[i]=OWNED
  post(WORK_DEADLINE,1)
  return i
 except BaseException:
  if not created:release_noncreation(i)
  exception_post(WORK_DEADLINE,1)
  raise

def owned_pipe():
 a=reserve();b=reserve();pair=None;created=False
 try:
  pre(WORK_DEADLINE,1)
  try:
   pair=os.pipe2(os.O_CLOEXEC|os.O_NONBLOCK)
   created=True
  finally:
   if created:
    FD_NUM[a]=pair[0];FD_NUM[b]=pair[1];FD_STATE[a]=OWNED;FD_STATE[b]=OWNED
  post(WORK_DEADLINE,1)
  return a,b
 except BaseException:
  if not created:release_noncreation(a);release_noncreation(b)
  exception_post(WORK_DEADLINE,1)
  raise

def owned_dup(source):
 i=reserve();returned=-1;created=False
 try:
  pre(WORK_DEADLINE,1)
  try:
   returned=os.dup(source);created=True
  finally:
   if created:FD_NUM[i]=returned;FD_STATE[i]=OWNED
  post(WORK_DEADLINE,1)
  return i
 except BaseException:
  if not created:release_noncreation(i)
  exception_post(WORK_DEADLINE,1)
  raise

def close_cell(i,deadline):
 if FD_STATE[i]!=OWNED:return
 try:
  pre(deadline,2)
  try:os.close(FD_NUM[i])
  except OSError as error:
   latch(2);FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
  except BaseException:
   latch(2);FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
  else:FD_STATE[i]=FREE
  FD_NUM[i]=-1
  post(deadline,2)
 except BaseException:latch(2)

def four_close_passes(deadline):
 for unused in range(4):
  for i in range(MARKER_FD_CELLS):close_cell(i,deadline)

def final_scan(deadline):
 for i in range(MARKER_FD_CELLS):
  try:
   post(deadline,3)
   if FD_STATE[i] in (RESERVED,OWNED,PHYSICALLY_CLOSED_ERROR):latch(3)
  except BaseException:latch(3)

def fd(i):
 need(FD_STATE[i]==OWNED and FD_NUM[i]>=0,4)
 return FD_NUM[i]

def decimal(raw,low=0,high=MAX_I63):
 need(type(raw)is bytes and raw and raw.isdigit(),4)
 value=int(raw)
 need(str(value).encode("ascii")==raw and low<=value<=high,4)
 return value

def hexa(raw,count=None):
 need(type(raw)is bytes and len(raw)%2==0 and (count is None or len(raw)==count) and all(c in b"0123456789abcdef" for c in raw),4)
 return raw

def decoded(raw,count=None):
 hexa(raw,count)
 value=bytes.fromhex(raw.decode("ascii"))
 need(value.hex().encode("ascii")==raw,4)
 return value

def octal(raw):
 need(raw and all(c in b"01234567" for c in raw),4)
 value=int(raw,8)
 need(format(value,"o").encode("ascii")==raw,4)
 return value

def hash_fd(number,size,deadline):
 pre(deadline,5);os.lseek(number,0,os.SEEK_SET);post(deadline,5)
 total=0;digest=hashlib.sha256()
 while total<=size:
  pre(deadline,5);chunk=os.read(number,min(1048576,size-total+1));post(deadline,5)
  if not chunk:break
  total+=len(chunk);digest.update(chunk)
 need(total==size,5)
 return digest.hexdigest().encode("ascii")

def write_all(number,data,deadline):
 flags=checked_call(deadline,6,fcntl.fcntl,number,fcntl.F_GETFL)
 checked_call(deadline,6,fcntl.fcntl,number,fcntl.F_SETFL,flags|os.O_NONBLOCK)
 offset=0;poller=checked_call(deadline,6,select.poll);checked_call(deadline,6,poller.register,number,select.POLLOUT|select.POLLERR|select.POLLHUP)
 for unused in range(4194304):
  pre(deadline,6)
  if offset==len(data):post(deadline,6);return
  try:count=os.write(number,data[offset:])
  except InterruptedError:post(deadline,6);continue
  except BlockingIOError:count=0
  except BaseException:exception_post(deadline,6);raise
  post(deadline,6)
  if count>0:offset+=count;continue
  checked_call(deadline,6,poller.poll,1)
 raise MarkerFailure("write-bound")

def read_line(number,deadline):
 raw=bytearray();poller=checked_call(deadline,7,select.poll);checked_call(deadline,7,poller.register,number,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(2097152):
  pre(deadline,7)
  try:chunk=os.read(number,4096)
  except InterruptedError:post(deadline,7);continue
  except BlockingIOError:chunk=None
  except BaseException:exception_post(deadline,7);raise
  post(deadline,7)
  if chunk==b"":raise MarkerFailure("eof")
  if chunk:
   raw.extend(chunk);need(len(raw)<=1048576 and b"\r" not in raw and b"\x00" not in raw,7)
   if b"\n" in raw:
    need(raw.count(b"\n")==1 and raw.endswith(b"\n"),7);post(deadline,7);return bytes(raw)
  checked_call(deadline,7,poller.poll,1)
 raise MarkerFailure("read-bound")

def require_response_eof(number,deadline):
 poller=checked_call(deadline,7,select.poll);checked_call(deadline,7,poller.register,number,select.POLLIN|select.POLLHUP|select.POLLERR)
 for unused in range(1048576):
  pre(deadline,7)
  try:chunk=os.read(number,4096)
  except InterruptedError:post(deadline,7);continue
  except BlockingIOError:chunk=None
  except BaseException:exception_post(deadline,7);raise
  post(deadline,7)
  if chunk==b"":post(deadline,7);return
  if chunk:raise MarkerFailure("response-surplus")
  checked_call(deadline,7,poller.poll,1)
 raise MarkerFailure("response-eof-bound")

def broker(probe,op,nonce,child_sha):
 global REQUEST_CELL
 request=TAG+b"|broker=request|seq=0|probe="+probe+b"|op="+op+b"|nonce="+nonce+b"|child_sha="+child_sha+b"|end=1\n"
 write_all(5,request,WORK_DEADLINE)
 close_cell(REQUEST_CELL,WORK_DEADLINE)
 raw=read_line(6,WORK_DEADLINE)
 require_response_eof(6,WORK_DEADLINE)
 fields=raw[:-1].split(b"|")
 need(len(fields)==11 and fields[:3]==[TAG,b"broker=response",b"seq=0"],8)
 need(fields[3]==b"probe="+probe and fields[4]==b"op="+op,8)
 need(fields[5].startswith(b"spawned=") and fields[6].startswith(b"reaped="),8)
 spawned=decimal(fields[5][8:]);reaped=decimal(fields[6][7:]);need(spawned==reaped,8)
 need(fields[7].startswith(b"pids=") and fields[8].startswith(b"statuses=") and fields[9].startswith(b"payload_hex=") and fields[10]==b"result=PASS",8)
 pids=fields[7][5:];statuses=fields[8][9:];payload=decoded(fields[9][12:]) if fields[9][12:] else b""
 ptuple=() if not pids else tuple(decimal(x,2) for x in pids.split(b","))
 stuple=() if not statuses else tuple(decimal(x,0) for x in statuses.split(b","))
 need(len(ptuple)==len(stuple)==spawned,8)
 return spawned,ptuple,stuple,payload

def row(rows,probe,key,value):
 if type(value)is int:value=str(value).encode("ascii")
 if type(value)is str:value=value.encode("ascii")
 need(type(value)is bytes and b"|" not in key+value and b"\n" not in key+value and b"=" not in key+value,9)
 rows.append(TAG+b"|probe="+probe+b"|"+key+b"="+value)

CHILD_SOURCE=b'''\
import array
import errno
import fcntl
import hashlib
import os
import resource
import signal
import stat
import sys
import time

TAG=b"P27E001V10"
PYTHON=b"/root/miniconda3/bin/python3"
PYRES=b"/root/miniconda3/bin/python3.12"
PY_BYTES=30626264
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
CHILD_FD_CELLS=8
CHILD_CLOSE_RESERVE_NS=78000000
FREE=0
RESERVED=1
OWNED=2
CLOSED=3
PHYSICALLY_CLOSED_ERROR=4
FD_NUM=array.array("i",[-1])*CHILD_FD_CELLS
FD_STATE=bytearray(CHILD_FD_CELLS)
FATAL=bytearray(8)

class ChildFailure(Exception):
 pass

def latch(cell):
 if 0<=cell<len(FATAL):FATAL[cell]=1

def need(value,cell):
 if not value:
  latch(cell)
  raise ChildFailure(str(cell))

def adopt(number):
 for i in range(CHILD_FD_CELLS):
  if FD_STATE[i]==FREE:
   FD_STATE[i]=RESERVED;FD_NUM[i]=number;FD_STATE[i]=OWNED;return i
 raise ChildFailure("adopt-full")

def reserve():
 for i in range(CHILD_FD_CELLS):
  if FD_STATE[i]==FREE:
   FD_STATE[i]=RESERVED;FD_NUM[i]=-1;return i
 raise ChildFailure("fd-full")

def release_noncreation(i):
 need(FD_STATE[i]==RESERVED and FD_NUM[i]==-1,0);FD_STATE[i]=FREE

def owned_open(path,flags,deadline):
 i=reserve();returned=-1;created=False
 try:
  need(time.monotonic_ns()<=deadline,1)
  try:returned=os.open(path,flags);created=True
  finally:
   if created:FD_NUM[i]=returned;FD_STATE[i]=OWNED
  need(time.monotonic_ns()<=deadline,1);return i
 except BaseException:
  if not created:release_noncreation(i)
  try:
   if time.monotonic_ns()>deadline:latch(1)
  except BaseException:latch(1)
  raise

def close_cell(i,deadline):
 if FD_STATE[i]!=OWNED:return
 try:
  need(time.monotonic_ns()<=deadline,2)
  try:os.close(FD_NUM[i])
  except OSError as error:latch(2);FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
  except BaseException:latch(2);FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
  else:FD_STATE[i]=FREE
  FD_NUM[i]=-1
  need(time.monotonic_ns()<=deadline,2)
 except BaseException:latch(2)

def close_and_scan(deadline):
 for unused in range(4):
  for i in range(CHILD_FD_CELLS):close_cell(i,deadline)
 for i in range(CHILD_FD_CELLS):
  if FD_STATE[i] in (RESERVED,OWNED,PHYSICALLY_CLOSED_ERROR):latch(3)
  try:
   if time.monotonic_ns()>deadline:latch(3)
  except BaseException:latch(3)

def hash_fd(number,size,deadline):
 need(time.monotonic_ns()<=deadline,4);os.lseek(number,0,os.SEEK_SET);need(time.monotonic_ns()<=deadline,4)
 digest=hashlib.sha256();total=0
 while total<=size:
  need(time.monotonic_ns()<=deadline,4);chunk=os.read(number,min(1048576,size-total+1));need(time.monotonic_ns()<=deadline,4)
  if not chunk:break
  total+=len(chunk);digest.update(chunk)
 need(total==size,4);return digest.hexdigest().encode("ascii")

def hash_unbounded(number,deadline):
 need(time.monotonic_ns()<=deadline,4);os.lseek(number,0,os.SEEK_SET);need(time.monotonic_ns()<=deadline,4)
 digest=hashlib.sha256();total=0
 while total<=1048576:
  need(time.monotonic_ns()<=deadline,4);chunk=os.read(number,1048576);need(time.monotonic_ns()<=deadline,4)
  if not chunk:break
  total+=len(chunk);digest.update(chunk)
 need(total<=1048576,4);return total,digest.hexdigest().encode("ascii")

def write_all(data,deadline):
 need(time.monotonic_ns()<=deadline,5);flags=fcntl.fcntl(1,fcntl.F_GETFL);need(time.monotonic_ns()<=deadline,5)
 need(time.monotonic_ns()<=deadline,5);fcntl.fcntl(1,fcntl.F_SETFL,flags|os.O_NONBLOCK);need(time.monotonic_ns()<=deadline,5)
 offset=0
 while offset<len(data):
  need(time.monotonic_ns()<=deadline,5)
  try:count=os.write(1,data[offset:])
  except InterruptedError:need(time.monotonic_ns()<=deadline,5);continue
  except BlockingIOError:need(time.monotonic_ns()<=deadline,5);continue
  need(count>0,5);offset+=count;need(time.monotonic_ns()<=deadline,5)

mode=b"invalid";exit_code=91;source_cell=gate_cell=image_cell=self_cell=-1;deadline=(1<<63)-1;work_deadline=deadline
try:
 need(len(sys.argv) in (5,8) and sys.argv[0]=="/proc/self/fd/100",6)
 mode=os.fsencode(sys.argv[1]);deadline=int(sys.argv[2]);safe_hex=os.fsencode(sys.argv[3]);source_sha=os.fsencode(sys.argv[4]);need(deadline>CHILD_CLOSE_RESERVE_NS,6);work_deadline=deadline-CHILD_CLOSE_RESERVE_NS
 need(mode in (b"INFO",b"BLOCK0",b"EXIT23",b"TERM",b"CHAIN") and len(source_sha)==64,6)
 source_cell=adopt(100)
 if mode in (b"BLOCK0",b"EXIT23"):gate_cell=adopt(3)
 need(time.monotonic_ns()<=work_deadline,6);seals=fcntl.fcntl(100,fcntl.F_GET_SEALS);need(time.monotonic_ns()<=work_deadline,6);need(seals==EXACT_SEALS,6)
 size,actual_source_sha=hash_unbounded(100,work_deadline)
 need(actual_source_sha==source_sha,6)
 if len(sys.argv)==8:
  pressure=os.fsencode(sys.argv[7]);need(int(sys.argv[5])==251414 and len(pressure)==251414 and os.fsencode(sys.argv[6])==source_sha and hashlib.sha256(pressure).hexdigest().encode("ascii")==source_sha,6)
 else:need(len(sys.argv)==5,6)
 need(sys.executable==PYTHON.decode("ascii") and dict(os.environb)==ENV and b"_" not in os.environb,6)
 need(time.monotonic_ns()<=work_deadline,6);cwd=os.getcwdb();need(time.monotonic_ns()<=work_deadline,6);need(cwd.hex().encode("ascii")==safe_hex,6)
 need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_NOFILE,(4096,1048576));need(time.monotonic_ns()<=work_deadline,6)
 need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_CPU,(3,3));need(time.monotonic_ns()<=work_deadline,6);need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456));need(time.monotonic_ns()<=work_deadline,6)
 need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576));need(time.monotonic_ns()<=work_deadline,6);need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_CORE,(0,0));need(time.monotonic_ns()<=work_deadline,6)
 need(time.monotonic_ns()<=work_deadline,6);valid_signals=signal.valid_signals();need(time.monotonic_ns()<=work_deadline,6)
 definitions=tuple(sorted(int(x) for x in valid_signals if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))
 need(time.monotonic_ns()<=work_deadline,6);signal.pthread_sigmask(signal.SIG_SETMASK,set());need(time.monotonic_ns()<=work_deadline,6)
 for number in definitions:need(time.monotonic_ns()<=work_deadline,6);signal.signal(number,signal.SIG_DFL);need(time.monotonic_ns()<=work_deadline,6)
 image_cell=owned_open(PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,work_deadline)
 self_cell=owned_open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC,work_deadline)
 need(time.monotonic_ns()<=work_deadline,6);a=os.fstat(FD_NUM[image_cell]);need(time.monotonic_ns()<=work_deadline,6);b=os.fstat(FD_NUM[self_cell]);need(time.monotonic_ns()<=work_deadline,6);need((a.st_dev,a.st_ino,a.st_size)==(b.st_dev,b.st_ino,PY_BYTES),6)
 need(hash_fd(FD_NUM[image_cell],PY_BYTES,work_deadline)==PY_SHA and hash_fd(FD_NUM[self_cell],PY_BYTES,work_deadline)==PY_SHA,6)
 phase=b"ready" if mode in (b"BLOCK0",b"EXIT23",b"TERM") else b"terminal"
 need(time.monotonic_ns()<=work_deadline,6);pid=os.getpid();need(time.monotonic_ns()<=work_deadline,6);need(time.monotonic_ns()<=work_deadline,6);sid=os.getsid(0);need(time.monotonic_ns()<=work_deadline,6);need(time.monotonic_ns()<=work_deadline,6);pgid=os.getpgrp();need(time.monotonic_ns()<=work_deadline,6)
 line=TAG+b"|child=observation|mode="+mode+b"|pid="+str(pid).encode("ascii")+b"|sid="+str(sid).encode("ascii")+b"|pgid="+str(pgid).encode("ascii")+b"|image_sha="+PY_SHA+b"|source_sha="+source_sha+b"|cwd_hex="+safe_hex+b"|phase="+phase+b"|result=PASS\n"
 write_all(line,work_deadline)
 if mode in (b"BLOCK0",b"EXIT23"):
  while True:
   need(time.monotonic_ns()<=work_deadline,6)
   try:gate=os.read(3,1);need(time.monotonic_ns()<=work_deadline,6);break
   except InterruptedError:need(time.monotonic_ns()<=work_deadline,6);continue
  need(gate==b"G",6);exit_code=23 if mode==b"EXIT23" else 0
 elif mode==b"TERM":exit_code=0
 else:exit_code=0
 close_and_scan(deadline)
 need(not any(FATAL),7)
 if mode==b"TERM":need(time.monotonic_ns()<=deadline,7);os.kill(pid,signal.SIGTERM)
except BaseException:
 latch(7)
 try:
  if time.monotonic_ns()>deadline:latch(7)
 except BaseException:latch(7)
cleanup_deadline=int(sys.argv[2]) if len(sys.argv)>2 and sys.argv[2].isdigit() else (1<<63)-1
close_and_scan(cleanup_deadline)
raise SystemExit(exit_code if not any(FATAL) else 92)
'''

# V10 STAGE 2 LEAF SOURCES AND EMBEDDED CHILD COMPLETE

def hash_stream(number,deadline):
 pre(deadline,10);os.lseek(number,0,os.SEEK_SET);post(deadline,10)
 digest=hashlib.sha256();total=0;lines=0
 while total<=1048576:
  pre(deadline,10);chunk=os.read(number,1048576);post(deadline,10)
  if not chunk:break
  total+=len(chunk);lines+=chunk.count(b"\n");digest.update(chunk)
 need(total<=1048576,10)
 return total,lines,digest.hexdigest().encode("ascii")

def image():
 pre(WORK_DEADLINE,11);link=os.lstat(PYTHON);post(WORK_DEADLINE,11)
 pre(WORK_DEADLINE,11);link_target=os.readlink(PYTHON);post(WORK_DEADLINE,11)
 need(stat.S_ISLNK(link.st_mode) and link_target==b"python3.12",11)
 resolved=owned_open(PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 self_image=owned_open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC)
 try:
  pre(WORK_DEADLINE,11);a=os.fstat(fd(resolved));post(WORK_DEADLINE,11)
  pre(WORK_DEADLINE,11);b=os.fstat(fd(self_image));post(WORK_DEADLINE,11)
  need((a.st_dev,a.st_ino,a.st_mode,a.st_nlink,a.st_uid,a.st_gid,a.st_size)==(b.st_dev,b.st_ino,b.st_mode,b.st_nlink,b.st_uid,b.st_gid,b.st_size) and a.st_size==PY_BYTES,11)
  need(hash_fd(fd(resolved),PY_BYTES,WORK_DEADLINE)==PY_SHA and hash_fd(fd(self_image),PY_BYTES,WORK_DEADLINE)==PY_SHA,11)
  return a
 finally:
  close_cell(resolved,WORK_DEADLINE);close_cell(self_image,WORK_DEADLINE)

def libc_view():
 maps=owned_open(b"/proc/self/maps",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 raw=bytearray()
 try:
  for unused in range(2048):
   pre(WORK_DEADLINE,12);chunk=os.read(fd(maps),4096);post(WORK_DEADLINE,12)
   if not chunk:break
   raw.extend(chunk);need(len(raw)<=4194304,12)
 finally:close_cell(maps,WORK_DEADLINE)
 found=[]
 for line in bytes(raw).splitlines():
  parts=line.split(None,5)
  if len(parts)==6 and b"x" in parts[1] and parts[5].startswith(b"/") and parts[5].rsplit(b"/",1)[-1].startswith(b"libc.so"):found.append(parts[5])
 paths=tuple(sorted(set(found)));need(len(paths)==1,12);path=paths[0]
 libc=owned_open(path,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW)
 try:
  pre(WORK_DEADLINE,12);held=os.fstat(fd(libc));post(WORK_DEADLINE,12);digest=hash_fd(fd(libc),held.st_size,WORK_DEADLINE)
 finally:close_cell(libc,WORK_DEADLINE)
 pre(WORK_DEADLINE,12);conf=os.confstr("CS_GNU_LIBC_VERSION");post(WORK_DEADLINE,12)
 need(type(conf)is str and conf.isascii(),12)
 return path,held,digest,conf.encode("ascii")

def local_p01d(rows,probe,image_key):
 path,held,digest,conf=libc_view();surface=getattr(os,"posix_"+"spawn")
 row(rows,probe,b"python_image_dev",image_key.st_dev);row(rows,probe,b"python_image_ino",image_key.st_ino);row(rows,probe,b"python_image_bytes",image_key.st_size);row(rows,probe,b"python_image_sha256",PY_SHA)
 row(rows,probe,b"libc_confstr_hex",conf.hex());row(rows,probe,b"libc_path_hex",path.hex());row(rows,probe,b"libc_bytes",held.st_size);row(rows,probe,b"libc_sha256",digest)
 row(rows,probe,b"backend_surface",surface.__module__.encode("ascii")+b"-"+surface.__name__.encode("ascii"));row(rows,probe,b"spawn_premise_satisfied",0)

def local_p02(rows,probe,safe_hex):
 opened=[]
 for number in range(7):
  pre(WORK_DEADLINE,13)
  try:fcntl.fcntl(number,fcntl.F_GETFD);post(WORK_DEADLINE,13);opened.append(number)
  except OSError as error:post(WORK_DEADLINE,13);need(error.errno==errno.EBADF,13)
 pre(WORK_DEADLINE,13);cwd=os.getcwdb();post(WORK_DEADLINE,13)
 need(opened==[0,1,2,5,6] and dict(os.environb)==ENV and cwd.hex().encode("ascii")==safe_hex,13)
 row(rows,probe,b"fds",b"0,1,2,5,6");row(rows,probe,b"environment_count",10);row(rows,probe,b"cwd_hex",safe_hex)
 row(rows,probe,b"flags",b"isolated:1,ignore_environment:1,no_site:1,no_user_site:1,dont_write_bytecode:1,safe_path:1,utf8_mode:1,hash_randomization:1")

def local_p03(rows,probe):
 pre(WORK_DEADLINE,14);soft,hard=resource.getrlimit(resource.RLIMIT_NOFILE);post(WORK_DEADLINE,14);need((soft,hard)==(4096,1048576),14)
 pre(WORK_DEADLINE,14);resource.setrlimit(resource.RLIMIT_NOFILE,(64,hard));post(WORK_DEADLINE,14)
 opened=0;emfile=0
 try:
  for unused in range(128):
   cell=reserve();returned=-1;created=False
   try:
    pre(WORK_DEADLINE,14)
    try:returned=os.open(b".",os.O_RDONLY|os.O_DIRECTORY|os.O_CLOEXEC);created=True
    finally:
     if created:FD_NUM[cell]=returned;FD_STATE[cell]=OWNED
   post(WORK_DEADLINE,14);opened+=1
   except OSError as error:
    exception_post(WORK_DEADLINE,14)
    if not created and error.errno==errno.EMFILE:release_noncreation(cell);emfile=1;break
    if not created:release_noncreation(cell)
    raise
  need(emfile==1 and opened==59,14)
 finally:
  pre(WORK_DEADLINE,14);resource.setrlimit(resource.RLIMIT_NOFILE,(4096,hard));post(WORK_DEADLINE,14)
  for i in range(MARKER_FD_CELLS):
   if FD_STATE[i]==OWNED and FD_NUM[i] not in (5,6):close_cell(i,WORK_DEADLINE)
 row(rows,probe,b"soft_before",soft);row(rows,probe,b"hard_before",hard);row(rows,probe,b"soft_test",64);row(rows,probe,b"opened_fds",opened);row(rows,probe,b"emfile",emfile)

def local_p04(rows,probe):
 pre(WORK_DEADLINE,15);valid_signals=signal.valid_signals();post(WORK_DEADLINE,15);definitions=tuple(sorted(int(x) for x in valid_signals if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))
 pre(WORK_DEADLINE,15);current=signal.pthread_sigmask(signal.SIG_BLOCK,set());post(WORK_DEADLINE,15)
 defaults=0
 for number in definitions:
  pre(WORK_DEADLINE,15);handler=signal.getsignal(number);post(WORK_DEADLINE,15)
  if handler==signal.SIG_DFL:defaults+=1
 need(current==set() and defaults==len(definitions),15)
 csv=b",".join(str(x).encode("ascii") for x in definitions)
 row(rows,probe,b"valid_signal_count",len(valid_signals));row(rows,probe,b"default_signal_count",len(definitions));row(rows,probe,b"defaults_sha256",hashlib.sha256(csv).hexdigest());row(rows,probe,b"mask_empty",1)

def local_p06(rows,probe):
 values=[]
 for unused in range(4096):pre(WORK_DEADLINE,16);values.append(mono(16));post(WORK_DEADLINE,16)
 need(all(values[i]<=values[i+1] for i in range(4095)),16)
 deltas=[values[i+1]-values[i] for i in range(4095) if values[i+1]>values[i]];need(deltas,16)
 row(rows,probe,b"monotonic",1);row(rows,probe,b"observed_min_delta_ns",min(deltas));row(rows,probe,b"start_ns",values[0]);row(rows,probe,b"end_ns",values[-1]);row(rows,probe,b"deadline_checked",1)

def local_p07(rows,probe):
 r,w=owned_pipe();empty=0;eof_before=0
 try:
  pre(WORK_DEADLINE,17)
  try:os.read(fd(r),1);post(WORK_DEADLINE,17)
  except OSError as error:post(WORK_DEADLINE,17);need(error.errno in (errno.EAGAIN,errno.EWOULDBLOCK),17);empty=1
  post(WORK_DEADLINE,17);pre(WORK_DEADLINE,17);written=os.write(fd(w),b"x");post(WORK_DEADLINE,17);need(written==1,17)
  pre(WORK_DEADLINE,17);read_back=os.read(fd(r),1);post(WORK_DEADLINE,17);need(read_back==b"x",17)
  duplicate=owned_dup(fd(w));close_cell(w,WORK_DEADLINE)
  pre(WORK_DEADLINE,17)
  try:eof_before=int(os.read(fd(r),1)==b"");post(WORK_DEADLINE,17)
  except OSError as error:post(WORK_DEADLINE,17);need(error.errno in (errno.EAGAIN,errno.EWOULDBLOCK),17)
  post(WORK_DEADLINE,17);close_cell(duplicate,WORK_DEADLINE);pre(WORK_DEADLINE,17);final_read=os.read(fd(r),1);post(WORK_DEADLINE,17);need(final_read==b"",17)
 finally:
  close_cell(r,WORK_DEADLINE);close_cell(w,WORK_DEADLINE)
 row(rows,probe,b"empty_eagain",empty);row(rows,probe,b"eof_before_last_writer",eof_before);row(rows,probe,b"eof_after_last_writer",1)

def anchored_identity(directory,expected):
 pre(WORK_DEADLINE,18);held=os.fstat(directory);post(WORK_DEADLINE,18)
 need((held.st_dev,held.st_ino)==expected and held.st_uid==0 and held.st_gid==0 and stat.S_IMODE(held.st_mode)==0o700,18)

def unlink_fixed(directory,name):
 try:pre(OPERATIONAL_DEADLINE,18);os.unlink(name,dir_fd=directory);post(OPERATIONAL_DEADLINE,18)
 except FileNotFoundError:post(OPERATIONAL_DEADLINE,18)
 except BaseException:latch(18)

def local_p11(rows,probe,directory,expected):
 anchored_identity(directory,expected);anchor=noatime=-1;created_target=False
 try:
  anchor=owned_open(b"target",os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600,directory)
  created_target=True
  pre(WORK_DEADLINE,18);written=os.write(fd(anchor),b"x");post(WORK_DEADLINE,18);need(written==1,18)
  pre(WORK_DEADLINE,18);os.fsync(fd(anchor));post(WORK_DEADLINE,18)
  pre(WORK_DEADLINE,18);os.utime(b"target",ns=(1000000000,1000000000),dir_fd=directory,follow_symlinks=False);post(WORK_DEADLINE,18)
  noatime=owned_open(b"target",os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW|os.O_NOATIME,None,directory)
  pre(WORK_DEADLINE,18);read_back=os.read(fd(noatime),1);post(WORK_DEADLINE,18);need(read_back==b"x",18);close_cell(noatime,WORK_DEADLINE)
  pre(WORK_DEADLINE,18);current=os.stat(b"target",dir_fd=directory,follow_symlinks=False);post(WORK_DEADLINE,18);need(current.st_atime_ns==1000000000,18)
  pre(WORK_DEADLINE,18);created=os.fstat(fd(anchor));post(WORK_DEADLINE,18);pre(WORK_DEADLINE,18);os.unlink(b"target",dir_fd=directory);post(WORK_DEADLINE,18)
  pre(WORK_DEADLINE,18);held=os.fstat(fd(anchor));post(WORK_DEADLINE,18);need((created.st_dev,created.st_ino)==(held.st_dev,held.st_ino) and held.st_nlink==0,18)
 finally:
  if noatime>=0:close_cell(noatime,OPERATIONAL_DEADLINE)
  if anchor>=0:close_cell(anchor,OPERATIONAL_DEADLINE)
  if created_target:unlink_fixed(directory,b"target")
 row(rows,probe,b"open_result",b"OK");row(rows,probe,b"atime_unchanged",1);row(rows,probe,b"cleanup_unlinked",1);row(rows,probe,b"cleanup_identity_observed",1);row(rows,probe,b"atomic_unlink_proof",0);row(rows,probe,b"scope_single_inode",1)

def local_p13(rows,probe,directory,expected):
 anchored_identity(directory,expected);anchor=-1;created_a=False;linked_b=False
 try:
  anchor=owned_open(b"a",os.O_CREAT|os.O_EXCL|os.O_RDWR|os.O_CLOEXEC|os.O_NOFOLLOW,0o600,directory)
  created_a=True
  pre(WORK_DEADLINE,19);written=os.write(fd(anchor),b"P27E001\n");post(WORK_DEADLINE,19);need(written==8,19)
  pre(WORK_DEADLINE,19);os.fsync(fd(anchor));post(WORK_DEADLINE,19)
  pre(WORK_DEADLINE,19);os.link(b"a",b"b",src_dir_fd=directory,dst_dir_fd=directory,follow_symlinks=False);post(WORK_DEADLINE,19)
  linked_b=True
  pre(WORK_DEADLINE,19);created=os.fstat(fd(anchor));post(WORK_DEADLINE,19);pre(WORK_DEADLINE,19);os.unlink(b"a",dir_fd=directory);post(WORK_DEADLINE,19)
  pre(WORK_DEADLINE,19);path=os.stat(b"b",dir_fd=directory,follow_symlinks=False);post(WORK_DEADLINE,19);need((created.st_dev,created.st_ino)==(path.st_dev,path.st_ino),19)
  pre(WORK_DEADLINE,19);os.fsync(directory);post(WORK_DEADLINE,19);pre(WORK_DEADLINE,19);os.unlink(b"b",dir_fd=directory);post(WORK_DEADLINE,19)
  pre(WORK_DEADLINE,19);held=os.fstat(fd(anchor));post(WORK_DEADLINE,19);need(held.st_nlink==0,19)
 finally:
  if anchor>=0:close_cell(anchor,OPERATIONAL_DEADLINE)
  if created_a:unlink_fixed(directory,b"a")
  if linked_b:unlink_fixed(directory,b"b")
 row(rows,probe,b"file_fsync_returned",1);row(rows,probe,b"hardlink_noreplace_returned",1);row(rows,probe,b"inode_preserved",1);row(rows,probe,b"dir_fsync_returned",1);row(rows,probe,b"post_unlink_absent",1);row(rows,probe,b"cleanup_unlinked",1);row(rows,probe,b"durability_proof",0);row(rows,probe,b"rename_atomicity_proof",0)

def status_exit(raw,code):return os.WIFEXITED(raw) and os.WEXITSTATUS(raw)==code
def status_signal(raw,number):return os.WIFSIGNALED(raw) and os.WTERMSIG(raw)==number

def validate_observation(raw,mode,pid,source_sha,safe_hex,phase):
 need(raw.endswith(b"\n") and raw.count(b"\n")==1,20)
 fields=raw[:-1].split(b"|")
 need(len(fields)==11 and fields[0]==TAG and fields[1]==b"child=observation" and fields[2]==b"mode="+mode and fields[3]==b"pid="+str(pid).encode("ascii"),20)
 pre(WORK_DEADLINE,20);marker_group=os.getpgrp();post(WORK_DEADLINE,20)
 need(fields[4].startswith(b"sid=") and fields[5]==b"pgid="+str(marker_group).encode("ascii"),20)
 decimal(fields[4][4:],1);need(fields[6]==b"image_sha="+PY_SHA and fields[7]==b"source_sha="+source_sha and fields[8]==b"cwd_hex="+safe_hex and fields[9]==b"phase="+phase and fields[10]==b"result=PASS",20)

def decode_payload_item(item,prefix):
 need(item.startswith(prefix+b":"),20)
 raw=decoded(item[len(prefix)+1:])
 need(raw.hex().encode("ascii")==item[len(prefix)+1:],20)
 return raw

def validate_broker(rows,probe,op,nonce,child_sha,safe_hex):
 spawned,pids,statuses,payload=broker(probe,op,nonce,child_sha)
 csv_pids=b",".join(str(x).encode("ascii") for x in pids);csv_status=b",".join(str(x).encode("ascii") for x in statuses)
 items=payload.split(b";") if payload else []
 if op==b"P00_E2BIG":
  need((spawned==0 and statuses==() and len(items)==1 and b"returned=0,e2big=1" in items[0]) or (spawned==1 and status_exit(statuses[0],0) and len(items)==2 and b"returned=1,e2big=0" in items[1]),20)
  meta=items[-1];need(meta.startswith(b"source_bytes=251414,") and b",sha=" in meta,20);synthetic_sha=hexa(meta.rsplit(b",sha=",1)[1],64)
  if spawned==1:validate_observation(decode_payload_item(items[0],b"INFO"),b"INFO",pids[0],synthetic_sha,safe_hex,b"terminal")
  row(rows,probe,b"source_item_bytes",251414);row(rows,probe,b"source_item_accounted_bytes",251415);row(rows,probe,b"broker_spawned",spawned);row(rows,probe,b"broker_payload_hex",payload.hex())
 elif op==b"P01C_INFO":
  need(spawned==1 and status_exit(statuses[0],0) and len(items)==1,20);validate_observation(decode_payload_item(items[0],b"INFO"),b"INFO",pids[0],child_sha,safe_hex,b"terminal")
  row(rows,probe,b"child_pids",csv_pids);row(rows,probe,b"child_statuses",csv_status);row(rows,probe,b"child_raw_hex",payload.hex());row(rows,probe,b"spawn_premise_satisfied",1)
 elif op==b"P05_WAIT":
  need(spawned==2 and status_exit(statuses[0],23) and status_signal(statuses[1],signal.SIGTERM) and len(items)==1,20)
  combined=decode_payload_item(items[0],b"P05");lines=combined.splitlines(keepends=True);need(len(lines)==2,20);validate_observation(lines[0],b"EXIT23",pids[0],child_sha,safe_hex,b"ready");validate_observation(lines[1],b"TERM",pids[1],child_sha,safe_hex,b"ready")
  row(rows,probe,b"wnohang_zero",1);row(rows,probe,b"eintr",1);row(rows,probe,b"echild",1);row(rows,probe,b"child_pids",csv_pids);row(rows,probe,b"raw_statuses",csv_status);row(rows,probe,b"term_signal",int(signal.SIGTERM));row(rows,probe,b"broker_payload_hex",payload.hex())
 elif op==b"P08_TOPOLOGY":
  need(spawned==1 and status_exit(statuses[0],0) and len(items)==1,20);validate_observation(decode_payload_item(items[0],b"P08"),b"BLOCK0",pids[0],child_sha,safe_hex,b"ready")
  row(rows,probe,b"child_pids",csv_pids);row(rows,probe,b"raw_statuses",csv_status);row(rows,probe,b"same_session_group",1);row(rows,probe,b"post_pid_esrch",1);row(rows,probe,b"broker_payload_hex",payload.hex())
 elif op==b"P09_KILL":
  need(spawned==1 and status_signal(statuses[0],signal.SIGKILL) and len(items)==2,20);validate_observation(decode_payload_item(items[0],b"BLOCK0"),b"BLOCK0",pids[0],child_sha,safe_hex,b"ready")
  need(items[1].startswith(b"reap_start_ns=") and b",reap_end_ns=" in items[1],20);times=items[1].split(b"reap_start_ns=",1)[1].split(b",reap_end_ns=");need(len(times)==2,20)
  row(rows,probe,b"child_pids",csv_pids);row(rows,probe,b"raw_statuses",csv_status);row(rows,probe,b"signal",int(signal.SIGKILL));row(rows,probe,b"reap_start_ns",decimal(times[0]));row(rows,probe,b"reap_end_ns",decimal(times[1]));row(rows,probe,b"reaped",1)
 elif op==b"P10_INFO16":
  need(spawned==16 and len(statuses)==16 and all(status_exit(x,0) for x in statuses) and len(items)==16,20)
  for i in range(16):validate_observation(decode_payload_item(items[i],b"INFO"),b"INFO",pids[i],child_sha,safe_hex,b"terminal")
  duplicates=16-len(set(pids))
  row(rows,probe,b"sample_count",16);row(rows,probe,b"pids",csv_pids);row(rows,probe,b"statuses",csv_status);row(rows,probe,b"pid_duplicates",duplicates);row(rows,probe,b"group_is_single_owned_launcher_group",1);row(rows,probe,b"reuse_proof",0)
 elif op==b"P12_CHAIN":
  need(spawned==1 and status_exit(statuses[0],0) and len(items)==1,20);validate_observation(decode_payload_item(items[0],b"CHAIN"),b"CHAIN",pids[0],child_sha,safe_hex,b"terminal")
  row(rows,probe,b"child_pids",csv_pids);row(rows,probe,b"raw_statuses",csv_status);row(rows,probe,b"environment_count",10);row(rows,probe,b"underscore_absent",1);row(rows,probe,b"real_payload_invoked",0);row(rows,probe,b"broker_payload_hex",payload.hex())
 else:need(False,20)

def main():
 global WORK_DEADLINE,OPERATIONAL_DEADLINE,REQUEST_CELL
 result=b"FAIL";probe=b"invalid";rows=[];primary=b"none";source_cell=req_cell=resp_cell=safe_cell=-1
 try:
  need(len(sys.argv) in (8,21),21)
  probe=os.fsencode(sys.argv[1]);nonce=hexa(os.fsencode(sys.argv[2]),64);OPERATIONAL_DEADLINE=decimal(os.fsencode(sys.argv[3]),1);reserve_ns=decimal(os.fsencode(sys.argv[4]),554000000,554000000)
  safe_hex=hexa(os.fsencode(sys.argv[5]));marker_sha=hexa(os.fsencode(sys.argv[6]),64);child_sha=hexa(os.fsencode(sys.argv[7]),64)
  need(probe in PROBES and OPERATIONAL_DEADLINE>reserve_ns,21);WORK_DEADLINE=OPERATIONAL_DEADLINE-reserve_ns
  source_cell=adopt(100);req_cell=adopt(5);resp_cell=adopt(6);safe_cell=adopt(7)
  REQUEST_CELL=req_cell
  pre(WORK_DEADLINE,21);marker_seals=fcntl.fcntl(100,fcntl.F_GET_SEALS);post(WORK_DEADLINE,21);need(marker_seals==EXACT_SEALS,21);marker_identity=hash_stream(100,WORK_DEADLINE);need(marker_identity[2]==marker_sha,21)
  need(hashlib.sha256(CHILD_SOURCE).hexdigest().encode("ascii")==child_sha,21)
  pre(WORK_DEADLINE,21);safe_identity=os.fstat(7);post(WORK_DEADLINE,21);pre(WORK_DEADLINE,21);cwd=os.getcwdb();post(WORK_DEADLINE,21)
  need(safe_identity.st_uid==0 and safe_identity.st_gid==0 and stat.S_IMODE(safe_identity.st_mode)==0o700 and cwd.hex().encode("ascii")==safe_hex,21)
  close_cell(source_cell,WORK_DEADLINE)
  if probe not in (b"P11",b"P13"):close_cell(safe_cell,WORK_DEADLINE)
  image_key=image();pre(WORK_DEADLINE,21);start=mono(21);post(WORK_DEADLINE,21)
  mapping=dict(BROKER)
  extra=tuple(os.fsencode(x) for x in sys.argv[8:])
  if probe==b"P00":need(len(extra)==0,21);validate_broker(rows,probe,mapping[probe],nonce,child_sha,safe_hex)
  elif probe==b"P01D":need(len(extra)==0,21);local_p01d(rows,probe,image_key)
  elif probe==b"P01C":
   need(len(extra)==13,21);path=decoded(extra[0]);mapdev=decimal(extra[1]);mapino=decimal(extra[2]);mode=octal(extra[3]);nlink=decimal(extra[4]);uid=decimal(extra[5]);gid=decimal(extra[6]);size=decimal(extra[7]);digest=hexa(extra[8],64);conf=decoded(extra[9]);pydev=decimal(extra[10]);pyino=decimal(extra[11]);pysha=hexa(extra[12],64)
   need(conf.isascii() and conf.decode("ascii").encode("ascii")==conf and conf.hex().encode("ascii")==extra[9],21)
   lpath,held,ldigest,lconf=libc_view();actual=(lpath,held.st_dev,held.st_ino,held.st_mode,held.st_nlink,held.st_uid,held.st_gid,held.st_size,ldigest,lconf,image_key.st_dev,image_key.st_ino,PY_SHA)
   need(actual==(path,mapdev,mapino,mode,nlink,uid,gid,size,digest,conf,pydev,pyino,pysha),21)
   row(rows,probe,b"libc_path_hex",lpath.hex());row(rows,probe,b"libc_sha256",ldigest);row(rows,probe,b"libc_confstr_hex",lconf.hex());validate_broker(rows,probe,mapping[probe],nonce,child_sha,safe_hex)
  elif probe==b"P02":need(len(extra)==0,21);local_p02(rows,probe,safe_hex)
  elif probe==b"P03":need(len(extra)==0,21);local_p03(rows,probe)
  elif probe==b"P04":need(len(extra)==0,21);local_p04(rows,probe)
  elif probe==b"P05":need(len(extra)==0,21);validate_broker(rows,probe,mapping[probe],nonce,child_sha,safe_hex)
  elif probe==b"P06":need(len(extra)==0,21);local_p06(rows,probe)
  elif probe==b"P07":need(len(extra)==0,21);local_p07(rows,probe)
  elif probe==b"P08":need(len(extra)==0,21);validate_broker(rows,probe,mapping[probe],nonce,child_sha,safe_hex)
  elif probe==b"P09":need(len(extra)==0,21);validate_broker(rows,probe,mapping[probe],nonce,child_sha,safe_hex)
  elif probe==b"P10":need(len(extra)==0,21);validate_broker(rows,probe,mapping[probe],nonce,child_sha,safe_hex)
  elif probe==b"P11":need(len(extra)==0,21);local_p11(rows,probe,7,(safe_identity.st_dev,safe_identity.st_ino))
  elif probe==b"P12":need(len(extra)==0,21);validate_broker(rows,probe,mapping[probe],nonce,child_sha,safe_hex)
  elif probe==b"P13":need(len(extra)==0,21);local_p13(rows,probe,7,(safe_identity.st_dev,safe_identity.st_ino))
  else:need(False,21)
  pre(WORK_DEADLINE,21);finish=mono(21);post(WORK_DEADLINE,21);need(start<=finish<=WORK_DEADLINE,21)
  row(rows,probe,b"marker_image_dev",image_key.st_dev);row(rows,probe,b"marker_image_ino",image_key.st_ino);row(rows,probe,b"marker_image_sha256",PY_SHA);row(rows,probe,b"probe_start_ns",start);row(rows,probe,b"probe_finish_ns",finish);row(rows,probe,b"probe_elapsed_ns",finish-start);row(rows,probe,b"probe_bound_ns",WORK_DEADLINE-start);row(rows,probe,b"primary_failure",b"none");row(rows,probe,b"cleanup_failure",b"none");row(rows,probe,b"result",b"PASS")
  result=b"PASS"
 except BaseException as error:
  exception_post(OPERATIONAL_DEADLINE,22);latch(22);primary=(str(error).encode("ascii","backslashreplace").replace(b"_",b"-")[:128])
 finally:
  four_close_passes(OPERATIONAL_DEADLINE)
  final_scan(OPERATIONAL_DEADLINE)
 if result==b"PASS" and not any(FATAL):
  output=TAG+b"|marker=report|schema=10|probe="+probe+b"\n"+b"\n".join(rows)+b"\n"+TAG+b"|probe="+probe+b"|result=PASS\n"
  try:write_all(1,output,OPERATIONAL_DEADLINE);post(OPERATIONAL_DEADLINE,23)
  except BaseException:exception_post(OPERATIONAL_DEADLINE,23);latch(23)
  if not any(FATAL):raise SystemExit(0)
 failure=TAG+b"|marker=failure|probe="+probe+b"|primary_failure="+primary+b"|result=FAIL\n"
 try:write_all(1,failure,OPERATIONAL_DEADLINE);post(OPERATIONAL_DEADLINE,23)
 except BaseException:exception_post(OPERATIONAL_DEADLINE,23);latch(23)
 raise SystemExit(90)

main()
UNIFIED MARKER V10 SOURCE END

V10 STAGE 3 MARKER SOURCE COMPLETE

NESTED CHILD V10 SOURCE BEGIN
import array
import errno
import fcntl
import hashlib
import os
import resource
import signal
import stat
import sys
import time

TAG=b"P27E001V10"
PYTHON=b"/root/miniconda3/bin/python3"
PYRES=b"/root/miniconda3/bin/python3.12"
PY_BYTES=30626264
PY_SHA=b"9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"
ENV={b"LANG":b"C",b"LC_ALL":b"C",b"PATH":b"/usr/bin:/bin",b"PYTHONDONTWRITEBYTECODE":b"1",b"PYTHONHASHSEED":b"0",b"PYTHONIOENCODING":b"UTF-8:strict",b"PYTHONNOUSERSITE":b"1",b"PYTHONSAFEPATH":b"1",b"PYTHONUTF8":b"1",b"TZ":b"UTC"}
EXACT_SEALS=fcntl.F_SEAL_WRITE|fcntl.F_SEAL_GROW|fcntl.F_SEAL_SHRINK|fcntl.F_SEAL_SEAL
CHILD_FD_CELLS=8
CHILD_CLOSE_RESERVE_NS=78000000
FREE=0
RESERVED=1
OWNED=2
CLOSED=3
PHYSICALLY_CLOSED_ERROR=4
FD_NUM=array.array("i",[-1])*CHILD_FD_CELLS
FD_STATE=bytearray(CHILD_FD_CELLS)
FATAL=bytearray(8)

class ChildFailure(Exception):
 pass

def latch(cell):
 if 0<=cell<len(FATAL):FATAL[cell]=1

def need(value,cell):
 if not value:
  latch(cell)
  raise ChildFailure(str(cell))

def adopt(number):
 for i in range(CHILD_FD_CELLS):
  if FD_STATE[i]==FREE:
   FD_STATE[i]=RESERVED;FD_NUM[i]=number;FD_STATE[i]=OWNED;return i
 raise ChildFailure("adopt-full")

def reserve():
 for i in range(CHILD_FD_CELLS):
  if FD_STATE[i]==FREE:
   FD_STATE[i]=RESERVED;FD_NUM[i]=-1;return i
 raise ChildFailure("fd-full")

def release_noncreation(i):
 need(FD_STATE[i]==RESERVED and FD_NUM[i]==-1,0);FD_STATE[i]=FREE

def owned_open(path,flags,deadline):
 i=reserve();returned=-1;created=False
 try:
  need(time.monotonic_ns()<=deadline,1)
  try:returned=os.open(path,flags);created=True
  finally:
   if created:FD_NUM[i]=returned;FD_STATE[i]=OWNED
  need(time.monotonic_ns()<=deadline,1);return i
 except BaseException:
  if not created:release_noncreation(i)
  try:
   if time.monotonic_ns()>deadline:latch(1)
  except BaseException:latch(1)
  raise

def close_cell(i,deadline):
 if FD_STATE[i]!=OWNED:return
 try:
  need(time.monotonic_ns()<=deadline,2)
  try:os.close(FD_NUM[i])
  except OSError as error:latch(2);FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
  except BaseException:latch(2);FD_STATE[i]=PHYSICALLY_CLOSED_ERROR
  else:FD_STATE[i]=FREE
  FD_NUM[i]=-1
  need(time.monotonic_ns()<=deadline,2)
 except BaseException:latch(2)

def close_and_scan(deadline):
 for unused in range(4):
  for i in range(CHILD_FD_CELLS):close_cell(i,deadline)
 for i in range(CHILD_FD_CELLS):
  if FD_STATE[i] in (RESERVED,OWNED,PHYSICALLY_CLOSED_ERROR):latch(3)
  try:
   if time.monotonic_ns()>deadline:latch(3)
  except BaseException:latch(3)

def hash_fd(number,size,deadline):
 need(time.monotonic_ns()<=deadline,4);os.lseek(number,0,os.SEEK_SET);need(time.monotonic_ns()<=deadline,4)
 digest=hashlib.sha256();total=0
 while total<=size:
  need(time.monotonic_ns()<=deadline,4);chunk=os.read(number,min(1048576,size-total+1));need(time.monotonic_ns()<=deadline,4)
  if not chunk:break
  total+=len(chunk);digest.update(chunk)
 need(total==size,4);return digest.hexdigest().encode("ascii")

def hash_unbounded(number,deadline):
 need(time.monotonic_ns()<=deadline,4);os.lseek(number,0,os.SEEK_SET);need(time.monotonic_ns()<=deadline,4)
 digest=hashlib.sha256();total=0
 while total<=1048576:
  need(time.monotonic_ns()<=deadline,4);chunk=os.read(number,1048576);need(time.monotonic_ns()<=deadline,4)
  if not chunk:break
  total+=len(chunk);digest.update(chunk)
 need(total<=1048576,4);return total,digest.hexdigest().encode("ascii")

def write_all(data,deadline):
 need(time.monotonic_ns()<=deadline,5);flags=fcntl.fcntl(1,fcntl.F_GETFL);need(time.monotonic_ns()<=deadline,5)
 need(time.monotonic_ns()<=deadline,5);fcntl.fcntl(1,fcntl.F_SETFL,flags|os.O_NONBLOCK);need(time.monotonic_ns()<=deadline,5)
 offset=0
 while offset<len(data):
  need(time.monotonic_ns()<=deadline,5)
  try:count=os.write(1,data[offset:])
  except InterruptedError:need(time.monotonic_ns()<=deadline,5);continue
  except BlockingIOError:need(time.monotonic_ns()<=deadline,5);continue
  need(count>0,5);offset+=count;need(time.monotonic_ns()<=deadline,5)

mode=b"invalid";exit_code=91;source_cell=gate_cell=image_cell=self_cell=-1;deadline=(1<<63)-1;work_deadline=deadline
try:
 need(len(sys.argv) in (5,8) and sys.argv[0]=="/proc/self/fd/100",6)
 mode=os.fsencode(sys.argv[1]);deadline=int(sys.argv[2]);safe_hex=os.fsencode(sys.argv[3]);source_sha=os.fsencode(sys.argv[4]);need(deadline>CHILD_CLOSE_RESERVE_NS,6);work_deadline=deadline-CHILD_CLOSE_RESERVE_NS
 need(mode in (b"INFO",b"BLOCK0",b"EXIT23",b"TERM",b"CHAIN") and len(source_sha)==64,6)
 source_cell=adopt(100)
 if mode in (b"BLOCK0",b"EXIT23"):gate_cell=adopt(3)
 need(time.monotonic_ns()<=work_deadline,6);seals=fcntl.fcntl(100,fcntl.F_GET_SEALS);need(time.monotonic_ns()<=work_deadline,6);need(seals==EXACT_SEALS,6)
 size,actual_source_sha=hash_unbounded(100,work_deadline)
 need(actual_source_sha==source_sha,6)
 if len(sys.argv)==8:
  pressure=os.fsencode(sys.argv[7]);need(int(sys.argv[5])==251414 and len(pressure)==251414 and os.fsencode(sys.argv[6])==source_sha and hashlib.sha256(pressure).hexdigest().encode("ascii")==source_sha,6)
 else:need(len(sys.argv)==5,6)
 need(sys.executable==PYTHON.decode("ascii") and dict(os.environb)==ENV and b"_" not in os.environb,6)
 need(time.monotonic_ns()<=work_deadline,6);cwd=os.getcwdb();need(time.monotonic_ns()<=work_deadline,6);need(cwd.hex().encode("ascii")==safe_hex,6)
 need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_NOFILE,(4096,1048576));need(time.monotonic_ns()<=work_deadline,6)
 need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_CPU,(3,3));need(time.monotonic_ns()<=work_deadline,6);need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456));need(time.monotonic_ns()<=work_deadline,6)
 need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576));need(time.monotonic_ns()<=work_deadline,6);need(time.monotonic_ns()<=work_deadline,6);resource.setrlimit(resource.RLIMIT_CORE,(0,0));need(time.monotonic_ns()<=work_deadline,6)
 need(time.monotonic_ns()<=work_deadline,6);valid_signals=signal.valid_signals();need(time.monotonic_ns()<=work_deadline,6)
 definitions=tuple(sorted(int(x) for x in valid_signals if int(x) not in (int(signal.SIGKILL),int(signal.SIGSTOP))))
 need(time.monotonic_ns()<=work_deadline,6);signal.pthread_sigmask(signal.SIG_SETMASK,set());need(time.monotonic_ns()<=work_deadline,6)
 for number in definitions:need(time.monotonic_ns()<=work_deadline,6);signal.signal(number,signal.SIG_DFL);need(time.monotonic_ns()<=work_deadline,6)
 image_cell=owned_open(PYRES,os.O_RDONLY|os.O_CLOEXEC|os.O_NOFOLLOW,work_deadline)
 self_cell=owned_open(b"/proc/self/exe",os.O_RDONLY|os.O_CLOEXEC,work_deadline)
 need(time.monotonic_ns()<=work_deadline,6);a=os.fstat(FD_NUM[image_cell]);need(time.monotonic_ns()<=work_deadline,6);b=os.fstat(FD_NUM[self_cell]);need(time.monotonic_ns()<=work_deadline,6);need((a.st_dev,a.st_ino,a.st_size)==(b.st_dev,b.st_ino,PY_BYTES),6)
 need(hash_fd(FD_NUM[image_cell],PY_BYTES,work_deadline)==PY_SHA and hash_fd(FD_NUM[self_cell],PY_BYTES,work_deadline)==PY_SHA,6)
 phase=b"ready" if mode in (b"BLOCK0",b"EXIT23",b"TERM") else b"terminal"
 need(time.monotonic_ns()<=work_deadline,6);pid=os.getpid();need(time.monotonic_ns()<=work_deadline,6);need(time.monotonic_ns()<=work_deadline,6);sid=os.getsid(0);need(time.monotonic_ns()<=work_deadline,6);need(time.monotonic_ns()<=work_deadline,6);pgid=os.getpgrp();need(time.monotonic_ns()<=work_deadline,6)
 line=TAG+b"|child=observation|mode="+mode+b"|pid="+str(pid).encode("ascii")+b"|sid="+str(sid).encode("ascii")+b"|pgid="+str(pgid).encode("ascii")+b"|image_sha="+PY_SHA+b"|source_sha="+source_sha+b"|cwd_hex="+safe_hex+b"|phase="+phase+b"|result=PASS\n"
 write_all(line,work_deadline)
 if mode in (b"BLOCK0",b"EXIT23"):
  while True:
   need(time.monotonic_ns()<=work_deadline,6)
   try:gate=os.read(3,1);need(time.monotonic_ns()<=work_deadline,6);break
   except InterruptedError:need(time.monotonic_ns()<=work_deadline,6);continue
  need(gate==b"G",6);exit_code=23 if mode==b"EXIT23" else 0
 elif mode==b"TERM":exit_code=0
 else:exit_code=0
 close_and_scan(deadline)
 need(not any(FATAL),7)
 if mode==b"TERM":need(time.monotonic_ns()<=deadline,7);os.kill(pid,signal.SIGTERM)
except BaseException:
 latch(7)
 try:
  if time.monotonic_ns()>deadline:latch(7)
 except BaseException:latch(7)
cleanup_deadline=int(sys.argv[2]) if len(sys.argv)>2 and sys.argv[2].isdigit() else (1<<63)-1
close_and_scan(cleanup_deadline)
raise SystemExit(exit_code if not any(FATAL) else 92)
NESTED CHILD V10 SOURCE END

V10 STAGE 4 ALL FIVE SOURCE REGIONS COMPLETE

## 6. Exact V8-to-V10 probe preservation matrix

The marker branch chain and the outer admission tuple both contain these
fifteen identifiers in the following and only the following order.  Local
means that no broker request is emitted.  Broker means one exact authenticated
request, request-writer close, proof of EOF/no surplus, operation, exact reap,
one response, response-writer close, and proof of EOF/no surplus.

| order | probe | owner / exact operation | preserved observations and exact row keys |
| ---: | --- | --- | --- |
| 0 | P00 | outer / P00_E2BIG | `source_item_bytes=251414`, `source_item_accounted_bytes=251415`, `broker_spawned`, `broker_payload_hex`; sealed source is fd100 execution bytes and the same bytes occur once as nonexecuted pressure argv; exact E2BIG-or-return partition |
| 1 | P01D | marker local | `python_image_dev`, `python_image_ino`, `python_image_bytes`, `python_image_sha256`, `libc_confstr_hex`, `libc_path_hex`, `libc_bytes`, `libc_sha256`, `backend_surface`, `spawn_premise_satisfied=0` |
| 2 | P01C | outer / P01C_INFO | exact thirteen-field seal, one INFO leaf, then `libc_path_hex`, `libc_sha256`, `libc_confstr_hex`, `child_pids`, `child_statuses`, `child_raw_hex`, `spawn_premise_satisfied=1` |
| 3 | P02 | marker local | exact open descriptors `0,1,2,5,6`, environment count 10, `cwd_hex`, and the exact eight V8 isolation flags |
| 4 | P03 | marker local | `(4096,1048576)`, soft 64, exactly 59 successful fixed-cell opens from the five-FD baseline, EMFILE, close, restore; `soft_before`, `hard_before`, `soft_test`, `opened_fds`, `emfile` |
| 5 | P04 | marker local | every valid signal except KILL/STOP default, empty mask; `valid_signal_count`, `default_signal_count`, `defaults_sha256`, `mask_empty` |
| 6 | P05 | outer / P05_WAIT | EXIT23 ready; WNOHANG zero; actual bounded EINTR outside all commit windows; gate; exact exit 23; second wait ECHILD; TERM ready and exact SIGTERM; all seven V8 row keys |
| 7 | P06 | marker local | exactly 4096 monotonic readings, nondecreasing, at least one positive delta; five V8 row keys |
| 8 | P07 | marker local | nonblocking CLOEXEC pipe; EAGAIN, byte transfer, duplicate writer, no early EOF, final EOF; three V8 row keys with values `1,0,1` |
| 9 | P08 | outer / P08_TOPOLOGY | BLOCK0 ready; WNOHANG zero; exact same session and launcher group; live kill-zero; gate; exit zero; exact reap; post-reap ESRCH; five V8 row keys |
| 10 | P09 | outer / P09_KILL | BLOCK0 ready and live; outer selection timestamp; exact PID SIGKILL; exact SIGKILL raw status; physical reap; actual outer selection-to-commit interval; six V8 row keys |
| 11 | P10 | outer / P10_INFO16 | exactly sixteen ordered spawn instances; each INFO output/status-zero/exact-reap completes before the next reservation; numeric PID reuse allowed; exact `pid_duplicates=16-cardinality(pids)` and `reuse_proof=0` |
| 12 | P11 | marker local | held inode, exact `target`, O_CREAT/O_EXCL/O_NOFOLLOW, one byte, fsync, fixed timestamps, O_NOATIME read, unlink through fd7, held identity and nlink zero; six V8 row keys |
| 13 | P12 | outer / P12_CHAIN | initial empty env, fixed env to fixed bash to fixed Python, fd100 survives both exec transitions, CHAIN observation/status zero, exact ten final environment observations, underscore absent, real payload count zero |
| 14 | P13 | marker local | exact `a`/`b`, eight-byte `P27E001\n`, file fsync, no-replace hardlink, held identity, unlink `a`, directory fsync, unlink `b`, nlink zero; eight V8 row keys |

The local-only set is exactly
`P01D/P02/P03/P04/P06/P07/P11/P13`.  The broker set is exactly
`P00/P01C/P05/P08/P09/P10/P12`.  No local branch waits for or emits a broker
request.  No broker branch can create a child before the exact request is
fully matched and its writer has closed.  Partial, malformed, wrong-probe,
wrong-operation, wrong-hash, duplicate, late, and surplus bytes are fatal.

## 7. Exact P01C field order and canonical round trips

| index | field | mandatory canonicalization |
| ---: | --- | --- |
| 0 | libc_path_hex | lowercase even hex, decode, re-encode and raw equality |
| 1 | libc_map_dev | canonical unsigned decimal |
| 2 | libc_map_ino | canonical unsigned decimal |
| 3 | libc_mode | canonical octal, including the full held `st_mode` |
| 4 | libc_nlink | canonical unsigned decimal |
| 5 | libc_uid | canonical unsigned decimal |
| 6 | libc_gid | canonical unsigned decimal |
| 7 | libc_bytes | canonical unsigned decimal |
| 8 | libc_sha256 | exactly 64 lowercase hex digits |
| 9 | libc_confstr_hex | lowercase even hex; decoded bytes ASCII; decoded-to-text-to-bytes equality; decoded-to-hex equality; raw field equality |
| 10 | python_image_dev | canonical unsigned decimal |
| 11 | python_image_ino | canonical unsigned decimal |
| 12 | python_image_sha256 | exactly 64 lowercase hex digits |

The marker compares that complete ordered tuple against fresh held libc and
Python-image observations before requesting P01C_INFO.  EXTRA[9] therefore has
all raw, decoded, ASCII, and re-encoded round trips; no normalization is merely
asserted in prose.

## 8. Exact five modes and child observation

The only modes are, in order, INFO, BLOCK0, EXIT23, TERM, and CHAIN.

| mode | exact behavior |
| --- | --- |
| INFO | one terminal observation and exit zero |
| BLOCK0 | one ready observation, exact one-byte `G` gate, exit zero |
| EXIT23 | one ready observation, exact one-byte `G` gate, exit 23 |
| TERM | one ready observation, complete local FD cleanup, then self SIGTERM |
| CHAIN | one terminal observation after the sole env-to-bash-to-Python transport delta, exit zero |

Every returned observation has the exact ordered fields
`P27E001V10|child=observation|mode|pid|sid|pgid|image_sha|source_sha|cwd_hex|phase|result`.
The outer constructs the one expected byte string from the returned PID and
fixed identities and compares it exactly.  The marker independently decodes
the canonical response hex and repeats the field, mode, PID, image, source,
cwd, group, phase, and raw-status checks.  Physical reap alone is never a
semantic success.

## 9. Immutable source and anchored filesystem proof

The outer opens `/`, then `tmp`, then `p27-e001-host-v10`, then the authenticated
64-lowercase-hex nonce, one component at a time with held directory FDs and
O_DIRECTORY/O_CLOEXEC/O_NOFOLLOW.  The nonce is required to remain the same
held `(dev,ino)`, root-owned uid/gid 0, and mode 0700 under the authenticated
no-concurrent-mutator premise.  The only source basenames are `outer.py`,
`keeper.py`, `launcher.py`, `marker.py`, and `child.py`.  The only mutable test
names are `target`, `a`, and `b`; they are disjoint.  There is no glob,
directory enumeration, recursive deletion, wildcard, absolute caller path, or
pathname reopen of a hashed source.

Each source input open commits immediately to the fixed outer FD census.  The
outer copies it to a registered `memfd_create` result made with exactly
`MFD_CLOEXEC|MFD_ALLOW_SEALING`, adds exactly
`F_SEAL_WRITE|F_SEAL_GROW|F_SEAL_SHRINK|F_SEAL_SEAL`, reads exact
`F_GET_SEALS`, rewinds, and independently rehashes/recounts the sealed FD.
Every execution uses only a POSIX_SPAWN_DUP2 of a retained sealed memfd to
fixed fd100 and `/proc/self/fd/100`; no executable source pathname is opened
again.  The outer itself requires the authenticated sealed fd100 and validates
it independently before its first source open.

P00 creates an operation-local sealed memfd containing exactly the child
source plus LF, `#`, and enough ASCII `x` bytes to total 251414.  It executes
that fd100 while passing exactly the same 251414 bytes once as a nonexecuted
pressure argument.  A proven E2BIG releases only the reserved noncreated
process slot and closes all operation FDs.  A returned PID stays in the fixed
slot and must produce the exact INFO record and exit zero.

P12 begins with an empty spawn environment.  A fixed `/usr/bin/env -i` invokes
fixed `/usr/bin/bash --noprofile --norc -c`; its fixed command execs a second
`/usr/bin/env -i` carrying the exact ten entries and then fixed Python on
`/proc/self/fd/100`.  POSIX_SPAWN_DUP2 clears CLOEXEC on fd100 and neither
intermediate exec closes it.  That is the sole transport delta from V8.

## 10. Fixed-census commit and closure proof

All fixed arrays exist before the first reservation.  A descriptor producer
reserves stable cells before the call.  In its immediate local `finally`, the
successful returned number is the first caller-visible mutation and is
committed before a deadline check, allocation, validation, map/list update,
telemetry, framing, callback, or external transfer.  Two-result `pipe2`
commits both reserved cells under the same explicit return-to-commit premise.
Only a proved noncreation releases a RESERVED cell.  A clean close makes the
cell FREE and reusable; EBADF or any close uncertainty makes it
PHYSICALLY_CLOSED_ERROR and permanently fatal.

The process rule is identical.  Each `posix_spawn` reserves one of four stable
cells.  On success, returned PID, unknown raw status, then LIVE state are
committed without allocation before any postcheck.  On exact `waitpid(pid)`
success, the raw status is the first mutation, then REAPED is committed before
semantic validation.  Dicts, response arrays, PID lists, and sorting are
never the cleanup census.  A reaped child cell may represent a later serial
P10 instance only after its prior exact status has been copied to bounded
semantic output.

OUTER has 48 cells, MARKER exactly 64, and CHILD 8.  Marker P03 preallocates
all 64 before lowering RLIMIT_NOFILE, then commits exactly 59 successful dot
opens from the five-process-FD baseline before the proved EMFILE.  Four fixed
close passes run on success and every failure edge, followed by exhaustive
FREE/error scans.  A clean cell is FREE; a physically-closed-error cell is
fatal.  Launcher and keeper perform no descriptor-producing call after exec
and retain only their fixed hold writer until their exact termination turn.

## 11. Ownership, topology, and exact status matrices

Outer is the only source containing a child-creating call or child-wait call.
Launcher, keeper, marker, and every serial child are direct outer children and
own no child.  Outer is outside group G.  Launcher is G's leader.  Keeper,
marker, and each child join G without creating a session.  Before and after
each child transaction the outer freshly checks exact launcher/keeper PIDs,
session, and group.  No group TERM or KILL exists.  Numeric PID nonreuse is
not assumed.

| role | PASS entry condition | normal stop and exact status | premature / failure | rescue |
| --- | --- | --- | --- | --- |
| child | already exact-reaped under its operation | operation-specific exit 0, exit 23, SIGTERM, or SIGKILL | actual raw status retained; fatal; cleanup continues | exact PID SIGKILL and exact SIGKILL raw status; fatal forever |
| marker | exact exit zero after complete report | already exact-reaped | any other status retained; fatal; cleanup continues | exact PID SIGKILL and exact SIGKILL raw status; fatal forever |
| launcher | freshly alive and group leader until its turn | exact PID SIGTERM; exact SIGTERM raw status; then hold EOF | premature exit or different status retained; fatal; cleanup continues | exact PID SIGKILL and exact SIGKILL raw status; fatal forever |
| keeper | freshly alive and in G until the final turn | last exact PID SIGTERM; exact SIGTERM raw status; then hold EOF | premature exit or different status retained; fatal; cleanup continues | last exact PID SIGKILL and exact SIGKILL raw status; fatal forever |

The actual fixed order is every child, marker, launcher, keeper.  Admission is
closed first.  Each role keeps its hold writer through all earlier turns.
Immediately before each PASS-path launcher/keeper signal, an exact-PID
`waitpid(pid,WNOHANG)==0` check excludes both a zombie and any other premature
waitable exit; only then does a fresh exact-PID kill-zero check precede TERM.
Every signal is exact-PID.  TERM receives its finite 40000000-ns allowance;
then the only rescue is exact-PID SIGKILL under the one shared post-operation
horizon.  Each raw result is committed only on `waitpid(exact_pid)==exact_pid`.
Failure records all four role statuses and continues the exhaustive census.
Keeper is last.  Group ESRCH is neither required nor used as proof.

## 12. Deadlines, fault latches, and framing

OPERATIONAL_DEADLINE is armed from one checked start plus the authenticated
budget before fd100 adoption or any other reservation.  Marker and child
derive work cutoffs only by subtracting their fully enumerated local close
reserves from that same deadline.  No local operation can rearm it.

At outer cleanup entry, exactly one checked monotonic sample arms the
nonrestartable POST_OPERATION_HOST_DEADLINE.  All TERM, EINTR, SIGKILL, exact
wait, rescue, hold-EOF, four FD passes, final scan, framing, and exit-entry
work uses that same absolute horizon.  Every rescue phase clamps to it.  A
late operational observation sets a monotone fatal byte which the post clock
cannot clear.

All fallible or blocking read, write, poll, open, descriptor return, spawn,
wait, signal, close, EOF, zero-poll, drain, break, return, and success edges
have immediate pre/post checks.  Exception handlers postcheck before retry or
demote.  Clock/check errors latch rather than skip later cleanup cells.  The
emergency exact-PID path is a nonthrowing fixed-count continuation under the
same premise and deadline; it cannot turn failure into PASS.

Framing state is preinitialized before the first fallible call.  Marker report,
outer candidate, and outer terminal use bounded exact write-all loops; short
writes continue, while zero, EPIPE, EOF, receiver close, exception, and
postcheck failure demote.  A printed PASS is explicitly an actor-ack candidate,
not independently final.  The future actor accepts only complete result and
terminal frames, empty/reaped registries, exact zero exit, and its later ACK.
If any fallible check after a candidate or terminal byte changes the state,
outer exits nonzero or fails to enter exit, so the actor rejects.  No
pre-syscall flag is treated as proof of exit entry.

## 13. Closed surfaces and observation boundaries

Executables are exactly fixed Python, `/usr/bin/env`, and `/usr/bin/bash` in
their stated roles.  The environment is exactly the ten fixed entries or the
specified empty P12 starting environment.  The safe-directory inputs are the
fixed nonce and fixed source/test basenames.  The only filesystem APIs in P11
and P13 are the held-dirfd relative operations shown in the source.  The only
process APIs are outer `posix_spawn`, exact-PID `kill`, `waitpid`, fresh
`getsid/getpgid`, and nonsemantic kill-zero observations.  There is no shell
input, caller program, broad path, glob, directory discovery, group signal,
subreaper, pidfd, prctl, fork, subprocess, or ownership transfer.

This control does not infer durability from fsync return, atomic-unlink proof
from held identity, rename atomicity from hardlink behavior, scheduling from
elapsed time, premise truth from success, or PID nonreuse from sixteen
instances.  P11 keeps `atomic_unlink_proof=0`; P13 keeps
`durability_proof=0` and `rename_atomicity_proof=0`; P10 keeps
`reuse_proof=0`.

## 14. E0351--E0353 correction classes

| class | closed false-PASS or safety surface |
| --- | --- |
| C01 | mutable source pathname execution replaced by sealed fd100 snapshots |
| C02 | missing MFD_ALLOW_SEALING and exact four-seal verification |
| C03 | missing independent rewind/rehash/recount after sealing |
| C04 | source pathname reopen replaced by inherited fixed fd100 |
| C05 | P00 now executes the exact sealed 251414-byte source and passes the same nonexecuted argv bytes |
| C06 | P12 fd100 now survives env, bash, and Python exec transitions |
| C07 | lexical prefix containment replaced by held O_NOFOLLOW component walk |
| C08 | nonce uid/gid/mode/identity and no-mutator premise bound explicitly |
| C09 | descriptor producer return gaps closed by preallocated fixed cells and immediate local finally |
| C10 | spawn return gap closed by stable reserved process slot and first-mutation PID commit |
| C11 | exact wait return gap closed by first-mutation raw-status commit |
| C12 | every async callback/handler/trace/profile/external transfer excluded from successful commit windows |
| C13 | EBADF now demotes to PHYSICALLY_CLOSED_ERROR rather than clean close |
| C14 | outer, marker, and child have separate numeric simultaneous and cumulative FD bounds |
| C15 | P03 uses the exact 64-cell preallocation and 59-success EMFILE census |
| C16 | all four close passes and exhaustive FREE/error scans are explicitly bounded |
| C17 | one operational deadline is armed before the first reservation |
| C18 | one nonrestartable post-operation horizon is armed only at cleanup entry |
| C19 | signed-63 checked arithmetic enumerates every cleanup/framing multiplicity |
| C20 | owner progress extends through complete terminal write postcheck and exit entry |
| C21 | actor ACK progress is a separate future bound |
| C22 | KILL_REAP progress starts at exact live-PID selection, not signal return |
| C23 | cleanup is nonthrowing, fixed-census, monotone-fatal, and exhaustive |
| C24 | actual child-marker-launcher-keeper stop/reap order and keeper-last status matrix frozen |
| C25 | launcher/keeper hold writers remain live until their own exact turn |
| C26 | request writer closes before child creation; EOF proves no partial/duplicate/late/surplus request |
| C27 | response writer closes and marker proves exact one response with no surplus |
| C28 | P08/P09/P10/P11/P13 restored from normative V8 rather than V9 substitutes |
| C29 | P10 numeric PID reuse is observed and counted, never prohibited or used as premise |
| C30 | exact child output, raw statuses, source/image/env/cwd semantics gate every broker response |
| C31 | late clock, deadline, close, framing, or final-scan faults remain fatal after candidate bytes |
| C32 | future actor, not a pre-exit flag or printed PASS, decides completion from frames and exact exit |

## 15. Author-side zero-execution boundary

Authoring and verification are limited to exact named-file raw byte reads,
`apply_patch` writes to this one V10 path, raw `stat`, `wc`, `sha256sum`, byte
class counts, exact delimiter extraction, literal text counts, and raw `cmp`.
Embedded source execution/import/AST parsing/language parsing/compilation/
evaluation/launch count is zero.  Build/evidence/root access count is zero.
Directory listing/discovery/glob/git count is zero.  Downstream actor, binder,
fixture, validation, build, publication, and ledger write count is zero.

V10 STAGED PRESERVATION AND PROOF COMPLETE

## 16. Exact return-commit and census multiplicities

The following counts distinguish producing calls from returned descriptor
cells.  A successful `pipe2` is one producing call and two immediate fixed-cell
commits.  An inherited-FD adoption is a fixed-cell commit but not a producing
call.  Failed E2BIG/EMFILE calls return no descriptor or PID and release only
their pre-reserved noncreation cells.

| outer branch | producing calls including bootstrap | successful FD return commits | simultaneous owned-cell maximum | process spawn commits | operational exact-wait commits |
| --- | ---: | ---: | ---: | ---: | ---: |
| any local branch | 21 | 28 | 24 bootstrap / 15 after leaf setup | 3 | 1 marker |
| P00 | 23 | 31 | 24 bootstrap / 18 broker | 3 or 4 | 1 or 2 |
| P01C | 22 | 30 | 24 / 17 | 4 | 2 |
| P05 | 24 | 34 | 24 / 19 | 5 | 3 |
| P08 | 23 | 32 | 24 / 19 | 4 | 2 |
| P09 | 23 | 32 | 24 / 19 | 4 | 2 |
| P10 | 37 | 60 | 24 / 17 | 19 | 17 |
| P12 | 22 | 30 | 24 / 17 | 4 | 2 |

Outer bootstrap is exactly four held component opens, five input opens, five
memfd creates, and seven pipe2 calls: 21 calls and 28 returned FD commits.
The already inherited sealed fd100 is one additional adoption and is included
in the simultaneous-cell maximum, not the producing-call column.  After leaf
setup, only the two hold readers and the request-read, response-write, and
marker-output-read endpoints remain from the fourteen protocol pipe cells.
Every child file-action close list is rebuilt from the current 48-cell census,
deduplicated by current numeric FD, and excludes its three transfer sources;
no stale numeric snapshot or FD-nonreuse premise exists.

| marker branch | producing calls | returned FD commits | simultaneous registry cells | inherited adoptions |
| --- | ---: | ---: | ---: | ---: |
| P01D / P01C | 4 | 4 | 4 | fd100, fd5, fd6, fd7 |
| P02 / P04 / P05 / P06 / P08 / P09 / P10 / P12 | 2 | 2 | 4 before source/dir closure; 2 during branch | same four |
| P03 | 61 | 61 | 61 registry cells / 64 process FDs | same four |
| P07 | 4 | 5 | 5 | same four |
| P11 | 4 | 4 | 5 | same four |
| P13 | 3 | 3 | 4 | same four |

Each child makes exactly two producing open calls and two successful return
commits.  It adopts fd100 and, for BLOCK0/EXIT23, fd3; thus its exact maximum
is four of eight cells.  Launcher and keeper make zero producing calls.

Outer cleanup visits `4*48=192` fixed cells and then scans 48.  Marker cleanup
visits `4*64=256` and scans 64.  Each child visits `4*8=32` and scans 8.
P10's worst operational commit count is 60 outer FD returns, two marker image
returns, 32 returns across sixteen serial children, 19 spawn PID commits, and
17 operational wait-status commits.  Thus 94 FD-return transitions and 36
process-return transitions are the global branch maxima.  Their authenticated
commit allowances are checked within the operational budget; the distinct
1438000000-ns post-operation sum then covers the two remaining launcher/
keeper waits, all four possible rescue slots, fixed close visits, final scan,
framing, and exit entry without overlap or restart.

V10 NUMERIC ACCOUNTING COMPLETE

## 17. Raw identity and author closure

The five source slices, excluding their delimiter lines and including their
terminal LF bytes, have these author-side raw identities:

| source | bytes | LF | SHA-256 |
| --- | ---: | ---: | --- |
| OUTER | 43017 | 1054 | b374b3602707ec66d4e818dbe8d07f889cda229ad2445cef9e0e67b9d156903f |
| KEEPER | 1341 | 34 | fdf61ea2c826dcaf10114ae10536bb5dc6a90bac13c8e9c9a01e14bf1e2c89d2 |
| LAUNCHER | 1343 | 34 | 4b9f4d632db679482c05bc269a5b895e216844bd46bf9aa1c2b10a3f690148b3 |
| MARKER | 39318 | 730 | ea3034aa891a47e3372ddd9475786f73beb38300f1f4cf6260a7899381ee82f4 |
| CHILD | 8618 | 169 | 9505fdd3e2e1db041a2ab88bd555c56ce19f7aa00be1cf9082606caa539ee3b1 |

Raw extraction found exactly ten source delimiter lines, one of each required
BEGIN/END line.  Each source ends in one LF.  The standalone CHILD bytes are
identical to the marker `CHILD_SOURCE` bytes.  The outer source contains the
only lexical `os.posix_spawn(` call and all three lexical `os.waitpid(` call
sites; each other source has zero of both.  These are inert lexical counts,
not execution results.

The E0353 authority was rebound at author stop as 2134269 bytes, 22574 LF,
SHA-256 f64699702769d5204aada902df92976c93ddddae2a9c8fbc01f6c37e88efe7fd,
with the exact final terminal stated in section 1.  Its qualified manifest
boundary remains 136 rows, 21896 bytes, 136 LF, SHA-256
369ac7575bd204cfc822850f36bc137718edd1663da43ba3dea3c80a31a0eee3,
with `PASS_PROSPECTIVE_CANONICAL_WITH_LITERAL_HISTORY_QUALIFICATION` unchanged.
The frozen V8, V9, Binder V8, Actor V3, and Derivation V6 byte/LF/SHA triples
remain exactly those in section 1.

The fixed source establishes, without an execution claim: four preallocated
outer process slots; outer-only spawn/wait ownership; first-mutation fixed-cell
commit on successful descriptor, spawn, and exact wait returns; no group
cleanup signal; exhaustive child-marker-launcher-keeper exact-PID cleanup;
fresh WNOHANG liveness before each PASS-path launcher/keeper TERM; keeper-last
exact reap; and monotone demotion for premature, wrong-status, or rescue paths.
It also establishes the sealed fd100 source path, the exact anchored nonce
dirfd walk, fixed 48/64/8 FD tables, four closure passes, closed seven-operation
broker, exact one-request/one-response framing, P00--P13 order, P10 count 16,
P01C count 13 including EXTRA[9], and the five frozen modes.

All operational, post-operation host, terminal-framing, return-commit,
kill/reap, owner-survival, and future actor-ACK premises remain explicitly
separate.  Immediate success-side and failure-side deadline checks cover the
fallible source-binding, protocol, drain, cleanup, and framing edges.  The
1438000000-ns host cleanup/reporting bound is not an operational reset and is
not presented as a POSIX theorem.

Final author-side checking used only raw byte/text operations on exact named
allowed files plus `apply_patch` on this file.  Embedded-source import count,
language/AST parse count, compile count, evaluation count, execution count,
launch count, build/evidence/root access count, directory discovery/list/glob
count, git count, downstream action count, and non-V10 write count are all
zero.  No success of this inert control is claimed.

BATCH07_P27_E001_SUPERVISOR_HOST_PROBE_RECOVERY_V10_AUTHOR_STOP
