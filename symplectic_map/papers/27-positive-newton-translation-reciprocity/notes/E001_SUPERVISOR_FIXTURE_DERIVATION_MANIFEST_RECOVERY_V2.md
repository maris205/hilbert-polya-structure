# E001 Supervisor Fixture Derivation Manifest Recovery V2

## 0. Status and authority boundary

This is one inert, exact byte-derivation control. It is not the derived fixture,
not an executable transport, not a probe, and not authority to materialize or run
anything. It creates no production hook. Its only output during authorship is this
ASCII/LF note at the exact E0333-reserved path.

Control id: E001-SUPERVISOR-FIXTURE-DERIVATION-MANIFEST-RECOVERY-V2

Parent event: B07-E0333-P27-PROBE-RECOVERY-E001-ACTOR-DERIVATION-HOST-STATIC-REVIEW-FAILURE-AND-V2-CONTROL-AUTHORIZATION

Frozen parent identity: bytes 1874108; LF 20846; SHA256
9f810b0b3426f95920fa69398de341676dd55137566b0bc44a6ddfe1e89bcccf;
terminal
BATCH07_P27_PROBE_RECOVERY_E001_ACTOR_DERIVATION_HOST_V1_STATIC_REVIEW_FAILURE_RECORDED_AND_V2_CONTROLS_AUTHORIZED.

V1 is an immutable failed predecessor. No V1 byte is edited, repaired, or treated
as authoritative by this file.

## 1. Exact sealed input and inert extraction

B is the byte substring of the exact V8 note after the sole delimiter line

    BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V8_PROGRAM_BEGIN\n

and before the LF that immediately precedes the sole delimiter line

    BATCH07_P27_RECOVERY_E001_SUPERVISOR_BINDER_V8_PROGRAM_END\n

The delimiter LF is not in B. This is raw delimiter-safe byte slicing only. It
does not import, tokenize with a language parser, parse, compile, evaluate, or
execute B.

Exact V8 note: dev 2431; ino 5917339790; mode 0644; nlink 1; uid 0; gid 0;
bytes 279288; LF 7303; SHA256
3a14f615b46ab8af96c444da012da957adbf3f22bfae47f35a8bdf06564dacb4.

Exact B: 251414 bytes; 6839 LF; SHA256
34449280b51dae17eeb5eb841296e99d25512867185525fec39dc73a39dfc076;
final byte decimal 41. B has no terminal LF. Byte census: apostrophe 0,
double quote 8298, dollar 0, backtick 0, CR 0, NUL 0, high byte 0.

The V1 arithmetic defect is corrected literally: len(e001ClockNow)=12,
len(e001RawStdout)=13, and len(e001RawStderr)=13 bytes.

## 2. Exact transformation algebra

Each record r freezes an original half-open interval [O,O+P_bytes) in B. P is the
exact preimage bytes shown as lowercase hex. Q is the exact postimage bytes shown
as lowercase hex. Records are applied simultaneously, equivalently by copying
untouched B spans in ascending O order or by applying them in descending O order.
All record intervals are pairwise disjoint. An anchor is the shortest recorded
bounded neighbor expansion used by the mechanical authoring scan whose complete
bytes occur exactly once in B. Global P occurrence count is reported separately;
it is not confused with anchor uniqueness. No locator ordinal or author choice is
left for a materializer.

I is the exact result. Its complete identity and all arithmetic are frozen below.
No output path follows from this identity. If separately authorized later, the
only admissible destination class is a newly created disposable directory below
/tmp/p27-e001-synthetic-supervisor, after proving it is outside the repository,
every build/evidence tree, every control tree, and every old object.

Changed-byte classes are closed:

- C1: one exact Python adapter/scenario block insertion after the final import;
- C2: exact synthetic locator/data substitution, never a branch/operator edit;
- C3: exact clock/sleep callee atom substitution;
- C4: exact spawn/wait/signal/topology callee atom substitution;
- C5: exact raw read/write/pipe/poll/close callee atom substitution;
- C6: exact runtime, signal-normalizer, or StrictPreflight constructor atom;
- C7: one inert Python comment trailer and the terminal LF.

## 3. Exact adapter and scenario block A

The following lines freeze A. Remove exactly the first two bytes `A|` from every
line and join the resulting lines with LF, including the LF after the last line.
There is no other decoding, formatting choice, or interpolation. The representation
is inert Markdown data; it is not a runnable marker.

A|# E001_SYNTHETIC_ADAPTER_BEGIN
A|E001SyntheticRoot = b"/tmp/p27-e001-synthetic-supervisor"
A|E001ScenarioTable = (
A|    ("S00", "E001-HANDSHAKE-OK", ("ready=52", "context=expected", "exit=0")),
A|    ("S01", "E001-HANDSHAKE-MALFORMED", ("ready=4e4f", "context=expected", "exit=0")),
A|    ("S02", "E001-RAW-SPLIT-LF", ("stdout=6f75742d41,0a6f75742d42,0a", "stderr=6572722d41,0a6572722d42,0a")),
A|    ("S03", "E001-EXIT-NONZERO", ("stdout=", "stderr=73796e7468657469632d6661696c0a", "exit=23")),
A|    ("S04", "E001-EXIT-SIGNAL", ("stdout=", "stderr=", "signal=15")),
A|    ("S05", "E001-DEADLINE-STICKY", ("clock=1000,1001,1010,1010,1011,1012", "deadline=1010", "exit_time=1011")),
A|    ("S06", "E001-OVERFLOW-STDOUT", ("stdout_limit_plus=1", "stderr=")),
A|    ("S07", "E001-OVERFLOW-STDERR", ("stdout=", "stderr_limit_plus=1")),
A|    ("S08", "E001-SUPERVISOR-LOSS", ("ready=", "lifeline=eof", "group=present,absent")),
A|    ("S09", "E001-REPORT-TRUNCATED", ("accepted=limit_minus_1", "close=success")),
A|    ("S10", "E001-CONTEXT-WRONG", ("context=wrong", "opposite=0")),
A|    ("S11", "E001-CONTEXT-OPPOSITE", ("context=opposite", "opposite=1")),
A|    ("S12", "E001-RECOVERY-DISPATCH", ("primary_exit=71", "recovery_ready=52", "recovery_exit=0")),
A|    ("S13", "E001-CLOSE-CALLBACK-FAULT", ("close=callback:E001_CLOSE_CALLBACK", "exit=0")),
A|    ("S14", "E001-CLOSE-SYNC-FAULT", ("close=sync:E001_CLOSE_SYNC", "exit=0")),
A|    ("S15", "E001-GROUP-ABSENT", ("group=present,absent,absent", "signal=ESRCH")),
A|    ("S16", "E001-COMMIT-AFTER-CLOSE-FAULT", ("close=success", "commit=E001_COMMIT_CLOSED")),
A|)
A|E001ScenarioIds = tuple(row[1] for row in E001ScenarioTable)
A|E001SyntheticState = {
A|    "scenario": "E001-HANDSHAKE-OK",
A|    "clock_index": 0,
A|    "next_fd": 100,
A|    "next_pid": 3101,
A|    "mode": "none",
A|    "reads": {},
A|    "writes": [],
A|    "closed": set(),
A|    "signals": [],
A|    "children": {},
A|    "timers": {},
A|    "report": bytearray(),
A|}
A|def e001Scenario():
A|    candidate = sys.argv[-1] if len(sys.argv) > 1 else "E001-HANDSHAKE-OK"
A|    if candidate not in E001ScenarioIds:
A|        candidate = "E001-HANDSHAKE-OK"
A|    E001SyntheticState["scenario"] = candidate
A|    return candidate
A|def e001ScenarioRow():
A|    selected = e001Scenario()
A|    for row in E001ScenarioTable:
A|        if row[1] == selected:
A|            return row
A|    raise RuntimeError("E001_SCENARIO_CLOSED")
A|def e001ClockNow():
A|    values = (1000, 1001, 1010, 1010, 1011, 1012)
A|    index = E001SyntheticState["clock_index"]
A|    E001SyntheticState["clock_index"] = min(index + 1, len(values) - 1)
A|    return values[index]
A|def e001SetTimer(callback, delay):
A|    token = len(E001SyntheticState["timers"]) + 1
A|    E001SyntheticState["timers"][token] = (callback, delay, 0)
A|    return token
A|def e001ClearTimer(token):
A|    if token in E001SyntheticState["timers"]:
A|        callback, delay, ignored = E001SyntheticState["timers"][token]
A|        E001SyntheticState["timers"][token] = (callback, delay, 1)
A|def e001Sleep(value):
A|    E001SyntheticState["clock_index"] = min(E001SyntheticState["clock_index"] + 1, 5)
A|def e001Runtime(mode, expected_fds, binding):
A|    E001SyntheticState["mode"] = mode
A|    E001SyntheticState["expected_fds"] = tuple(expected_fds)
A|    E001SyntheticState["binding"] = binding
A|def e001NormalizeSignals():
A|    E001SyntheticState["signals_normalized"] = 1
A|class e001StrictPreflight:
A|    def __init__(self, binding):
A|        self.control = type("E001SyntheticControl", (), {})()
A|        self.control.binding = binding
A|        self.closed = 0
A|    def verify(self):
A|        if self.closed:
A|            raise RuntimeError("E001_PREFLIGHT_CLOSED")
A|    def close(self):
A|        self.closed = 1
A|def e001Pipe2(flags):
A|    left = E001SyntheticState["next_fd"]
A|    E001SyntheticState["next_fd"] = left + 2
A|    E001SyntheticState["reads"][left] = []
A|    E001SyntheticState["reads"][left + 1] = []
A|    return left, left + 1
A|def e001Spawn(path, argv, env, **options):
A|    pid = E001SyntheticState["next_pid"]
A|    E001SyntheticState["next_pid"] = pid + 1
A|    E001SyntheticState["children"][pid] = {"argv": tuple(argv), "waited": 0, "status": 0}
A|    for fd in sorted(E001SyntheticState["reads"]):
A|        if not E001SyntheticState["reads"][fd]:
A|            E001SyntheticState["reads"][fd] = [b"R", b""]
A|            break
A|    return pid
A|def e001Signal(pid, value):
A|    if pid not in E001SyntheticState["children"]:
A|        raise OSError(errno.ESRCH, "E001_SYNTHETIC_ESRCH")
A|    E001SyntheticState["signals"].append((pid, value))
A|def e001GroupProbe(pgid, value):
A|    if e001Scenario() == "E001-GROUP-ABSENT":
A|        raise OSError(errno.ESRCH, "E001_SYNTHETIC_ESRCH")
A|    return None
A|def e001WaitPid(pid, options):
A|    child = E001SyntheticState["children"].get(pid)
A|    if child is None:
A|        raise ChildProcessError("E001_SYNTHETIC_ECHILD")
A|    if options != 0 and child["waited"] == 0:
A|        child["waited"] = 1
A|        return 0, 0
A|    child["waited"] = 1
A|    return pid, child["status"]
A|def e001RawStdout():
A|    if e001Scenario() == "E001-RAW-SPLIT-LF":
A|        return (b"out-A", b"\nout-B", b"\n")
A|    if e001Scenario() == "E001-OVERFLOW-STDOUT":
A|        return (b"X" * (STDOUT_CAP + 1),)
A|    return (PASS_LINE,)
A|def e001RawStderr():
A|    if e001Scenario() == "E001-RAW-SPLIT-LF":
A|        return (b"err-A", b"\nerr-B", b"\n")
A|    if e001Scenario() == "E001-OVERFLOW-STDERR":
A|        return (b"X" * (STDERR_CAP + 1),)
A|    if e001Scenario() == "E001-EXIT-NONZERO":
A|        return (b"synthetic-fail\n",)
A|    return ()
A|def e001Read(fd, size):
A|    if e001Scenario() == "E001-SUPERVISOR-LOSS":
A|        return b""
A|    queue = E001SyntheticState["reads"].setdefault(fd, [])
A|    if not queue:
A|        if fd % 2 == 0:
A|            queue.extend(e001RawStdout())
A|        else:
A|            queue.extend(e001RawStderr())
A|        queue.append(b"")
A|    value = queue.pop(0)
A|    if len(value) > size:
A|        queue.insert(0, value[size:])
A|        value = value[:size]
A|    return value
A|def e001Write(fd, data):
A|    value = bytes(data)
A|    E001SyntheticState["writes"].append((fd, value))
A|    return len(value)
A|def e001SetBlocking(fd, value):
A|    E001SyntheticState["blocking"] = (fd, int(bool(value)))
A|def e001Close(fd):
A|    if e001Scenario() == "E001-CLOSE-SYNC-FAULT":
A|        raise OSError(errno.EIO, "E001_CLOSE_SYNC")
A|    E001SyntheticState["closed"].add(fd)
A|class e001StatResult:
A|    def __init__(self, size=0, mode=33152, ino=1):
A|        self.st_dev = 1
A|        self.st_ino = ino
A|        self.st_mode = mode
A|        self.st_nlink = 1
A|        self.st_uid = 0
A|        self.st_gid = 0
A|        self.st_rdev = 0
A|        self.st_size = size
A|def e001Open(name, flags, mode=511, *, dir_fd=None):
A|    fd = E001SyntheticState["next_fd"]
A|    E001SyntheticState["next_fd"] = fd + 1
A|    E001SyntheticState["reads"][fd] = [b""]
A|    E001SyntheticState.setdefault("names", {})[fd] = bytes(name) if isinstance(name, bytes) else str(name).encode("ascii")
A|    return fd
A|def e001Stat(name, *, dir_fd=None, follow_symlinks=False):
A|    value = bytes(name) if isinstance(name, bytes) else str(name).encode("ascii")
A|    return e001StatResult(len(value), ino=(sum(value) % 100000) + 1)
A|def e001Fstat(fd):
A|    queue = E001SyntheticState["reads"].get(fd, [b""])
A|    return e001StatResult(sum(len(piece) for piece in queue), ino=fd + 1)
A|def e001Pread(fd, amount, offset):
A|    value = b"".join(E001SyntheticState["reads"].get(fd, [b""]))
A|    if e001Scenario() == "E001-REPORT-TRUNCATED" and value:
A|        value = value[:-1]
A|    return value[offset:offset + amount]
A|def e001Readlink(name, *, dir_fd=None):
A|    return b"synthetic-link-target"
A|class e001Scandir:
A|    def __init__(self, fd):
A|        self.fd = fd
A|        self.closed = 0
A|    def __iter__(self):
A|        return iter(())
A|    def close(self):
A|        self.closed = 1
A|class e001Poll:
A|    def __init__(self):
A|        self.members = {}
A|    def register(self, fd, mask):
A|        self.members[fd] = mask
A|    def unregister(self, fd):
A|        self.members.pop(fd, None)
A|    def poll(self, timeout):
A|        return [(fd, select.POLLIN | select.POLLHUP) for fd in sorted(self.members)]
A|def e001GetPid():
A|    return 3001 if E001SyntheticState["mode"] == "supervisor" else 3002
A|def e001GetPpid():
A|    return 3001
A|def e001GetSid(pid):
A|    return 3001
A|def e001GetPgrp():
A|    return 3001
A|def e001GetPgid(pid):
A|    return 3001
A|def e001Handshake():
A|    return b"R" if e001Scenario() == "E001-HANDSHAKE-OK" else b"NO"
A|def e001Context():
A|    values = {"E001-CONTEXT-WRONG": "E001-WRONG", "E001-CONTEXT-OPPOSITE": "recovery-binder"}
A|    return values.get(e001Scenario(), "watchdog")
A|def e001ReportOpen(name):
A|    E001SyntheticState["report"] = bytearray()
A|    return 1
A|def e001ReportWrite(handle, data):
A|    value = bytes(data)
A|    if e001Scenario() == "E001-REPORT-TRUNCATED" and value:
A|        value = value[:-1]
A|    E001SyntheticState["report"].extend(value)
A|    return len(value)
A|def e001ReportAppend(handle, data):
A|    return e001ReportWrite(handle, data)
A|def e001ReportRename(left, right):
A|    return None
A|def e001ReportCommit(handle):
A|    if e001Scenario() == "E001-COMMIT-AFTER-CLOSE-FAULT":
A|        raise OSError(errno.EIO, "E001_COMMIT_CLOSED")
A|def e001ReportClose(handle):
A|    if e001Scenario() == "E001-CLOSE-SYNC-FAULT":
A|        raise OSError(errno.EIO, "E001_CLOSE_SYNC")
A|    return None
A|# E001_SYNTHETIC_ADAPTER_END

## 4. A identity and expanded replacement registry

A is 9289 bytes, 232 LF, SHA256 db02405533d4bd1c529152df56876608cba1c85fd9883be53d8bae34477a4f01; final byte 10; strict ASCII/LF; apostrophe/dollar/backtick 0/0/0.

The registry has exactly 178 records: C1=1, C2=24, C3=22, C4=19, C5=101, C6=10, C7=1.

For R000 only, Q_hex is expressed as `P_hex || A || 0a`; A is copied exactly from Section 3 and is already fully byte-frozen. Every other P_hex and Q_hex is literal lowercase hex. `anchor` is offset/bytes/SHA256/count, and its count is one in every row. Left/right are the immediate at-most-16 B bytes outside P.

| id | O | P_hex | Q_hex | P bytes/LF/SHA256 | Q bytes/LF/SHA256 | delta bytes/LF | P count | anchor offset/bytes/SHA256/count | left16 | right16 | class | owner | seam | coverage |
|---|---:|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|
| R000 | 118 | 696d706f72742074696d650a0a | P_hex+A+0a | 13/2/a3f7a2e64605f32295c0985a8ee58c44a5965479d82bdced875e2b52330f66b0 | 9303/235/0dfad9bbe928e82857569f6a7fd22df7c330c65648adb445395796b2cafefcb8 | 9290/233 | 1 | 110/29/89739d99e5984ee0d582a897dceabcf2f3ad3cf9722f7c42a008a3ab2dea789d/1 | 737461740a696d706f7274207379730a | 574f524b203d2062222f726f6f742f61 | C1 | <module> | adapter-insert | all-17-scenarios |
| R010.001 | 140 | 2f726f6f742f6175746f646c2d746d702f73796d706c65637469635f6d6170 | 2f746d702f7032372d653030312d73796e7468657469632d73757065727669736f72 | 31/0/5ec9b3286ccc9a969a56102d036f81e733a25c9865f17aba65ff3ec1196d7727 | 34/0/257871f68240c596807d192a892bdfa27b7164e7f8273d2688e37349c9ab916f | 3/0 | 2 | 132/47/500f82bda6ef99a00cef23702d61540bdd172d3834dac0e7176c4c0ff32c8faa/1 | 2074696d650a0a574f524b203d206222 | 220a505954484f4e203d2062222f726f | C2 | <module> | workspace-root | synthetic-path-containment |
| R010.003 | 184 | 2f726f6f742f6d696e69636f6e6461332f62696e2f707974686f6e33 | 2f746d702f7032372d653030312d73796e7468657469632d73757065727669736f722f707974686f6e2d73747562 | 28/0/10658b016c4e2aeb86a28c64631f2452408cc3c40c8a383239cb1369dd9d52dd | 46/0/959ce2c39554d5e0b553b71eec4a718c2af2110cfc658b61ee29e5cf0d82b91c | 18/0 | 2 | 176/44/7c2eb6292e88e9d5fbaa884ff450466e4f511382c4c945d678f6f571b0fb730d/1 | 6d6170220a505954484f4e203d206222 | 220a454e565f544f4f4c203d2062222f | C2 | <module> | python-locator | synthetic-path-containment |
| R010.005 | 284 | 622242415443485f30375f5354415455532e6d6422 | 622273796e7468657469632d7374617475732e62696e22 | 21/0/ffdc69325ccb3f1f1ccfaf6159a314b269a17de48bc594fb1cf6b8e800353cda | 23/0/9776493ec29de416bf585f9bb3f07fd63f7dac3d832337ff27124f93b34f310d | 2/0 | 1 | 276/37/83b275f853c1394a492f0eab5f8a760ed83a8684a6ee8918291689a846ff5b91/1 | 220a5354415455535f4e414d45203d20 | 0a53454c465f4e414d45203d20622245 | C2 | <module> | status-name | synthetic-path-containment |
| R010.006 | 318 | 6222453030315f53555045525649534f525f42494e4445525f5245434f564552595f56382e6d6422 | 622273796e7468657469632d73757065727669736f722e707922 | 40/0/b64b76c6beecf743c08f8e722c7c5ac630ab8c9996bd83d21ffe90e89ad24409 | 26/0/9c1dde6882614ce1ea860bfb564a57a54d94d291dd7d83127d0568eadee2e974 | -14/0 | 1 | 310/56/9030cdc7da4ca1c6a0cabb77b0385c9d44c92b7eb4adafa206c97b5d829fc12c/1 | 6d64220a53454c465f4e414d45203d20 | 0a5041594c4f41445f434f4e54524f4c | C2 | <module> | self-name | synthetic-path-containment |
| R010.007 | 382 | 6222453030315f46495253545f434f50595f5245434f564552592e6d6422 | 622273796e7468657469632d696e7075742e62696e22 | 30/0/050dc88df830f20607289228bf7b6defaedbe470bdc451b9007d6b7b0b3204be | 22/0/5ed2af108cc24b0a97d0c42786c196d805b409e182abf38abe10ebd55d69e2db | -8/0 | 1 | 374/46/af50b4799e0d777fae3427517f5761405b7335a611220605dc1012f5793931e1/1 | 5f434f4e54524f4c5f4e414d45203d20 | 0a534f555243455f4e414d45203d2062 | C2 | <module> | input-control-name | synthetic-path-containment |
| R010.008 | 427 | 62224255494c445f56414c494441544f525f5245434f564552592e707922 | 622273796e7468657469632d636f70792e62696e22 | 30/0/5b8d5718e8c721b4e1785abe99a33674625439bd05086b4d8ad78c92bcf19c7f | 21/0/0b46ac33cc5197e909484305d157de7ea6c0694d4c507229ffb2a6014d749b52 | -9/0 | 2 | 419/46/f915c563f79c4c8909ddd150cb0669b320ba141f899192b20d74fccbd909aa61/1 | 220a534f555243455f4e414d45203d20 | 0a434f50595f4e414d45203d20622242 | C2 | <module> | copy-name | synthetic-path-containment |
| R010.009 | 470 | 62224255494c445f56414c494441544f525f5245434f564552592e707922 | 622273796e7468657469632d636f70792e62696e22 | 30/0/5b8d5718e8c721b4e1785abe99a33674625439bd05086b4d8ad78c92bcf19c7f | 21/0/0b46ac33cc5197e909484305d157de7ea6c0694d4c507229ffb2a6014d749b52 | -9/0 | 2 | 462/46/59b4880a4a4b5b6ac6f7c71f74c18602b27c0fcfc0f5d3fc52e7653f3e04c97c/1 | 7079220a434f50595f4e414d45203d20 | 0a5354415455535f524543454950545f | C2 | <module> | copy-name | synthetic-path-containment |
| R010.010 | 523 | 6222453030312e73746174757322 | 622273796e7468657469632d7374617475732e6f757422 | 14/0/b4bbb80df1beeacd81ddddfd32eaa4de494f3193a53477a06f0c758fa6de40e6 | 23/0/6cde7bfacda035ab1c08fb630a7c322bc80bc0a14c5b308f713273623ddd5605 | 9/0 | 1 | 515/30/5170948ce9277aa8eb0aaea4d761416271cc576cc7d60235d3ba318be1099dbb/1 | 5f524543454950545f4e414d45203d20 | 0a5354444552525f524543454950545f | C2 | <module> | status-receipt | synthetic-path-containment |
| R010.011 | 560 | 6222453030312e73746465727222 | 622273796e7468657469632d7374646572722e6f757422 | 14/0/294bc2923805659e2f6b7ab5a8c55a2d3aa0da2e3f7d92b2fe4c31566675260a | 23/0/7c3c9f89c6fc6cf8bf195bf19be9026b9dc741a5f9edcb50bf08618ac07d1ef7 | 9/0 | 1 | 552/30/1635a484158bcc6a16a4b692c13d215cb144c7730a988629913e8cde12f200f3/1 | 5f524543454950545f4e414d45203d20 | 0a5354444f55545f524543454950545f | C2 | <module> | stderr-receipt | synthetic-path-containment |
| R010.012 | 597 | 6222453030312e7374646f757422 | 622273796e7468657469632d7374646f75742e6f757422 | 14/0/197f6a1eff4a36a2bd8a7371adc06ffee84ba1bd203ffd9756655b5ce783327f | 23/0/efe7f28d11613d82e39b1ec4a3b90dbe4666dba3e894e8002ee188dfb36b6797 | 9/0 | 1 | 589/30/2dcac921ef6f01f15e3d732394993938ed65f6b825a0b7173a58549820734fae/1 | 5f524543454950545f4e414d45203d20 | 0a43414e4449444154455f4e414d4553 | C2 | <module> | stdout-receipt | synthetic-path-containment |
| R010.013 | 748 | 6222726f6f7422 | 6222746d7022 | 7/0/9427da7b54d16a6d8a6c297832cb3d37e30b64faa6070f6f6554c3892b73b914 | 6/0/5c5e4194a78af10986e406bd1b5a53caed08d3f7c645f41413816e84a60129dc | -1/0 | 2 | 732/39/9db3582f34070839215854f0dd5f4b6e1119c205c817eb37fbdf1faafdc067e8/1 | 504f4e454e5453203d20280a20202020 | 2c0a2020202062226175746f646c2d74 | C2 | <module> | root-component | synthetic-path-containment |
| R010.015 | 761 | 62226175746f646c2d746d7022 | 62227032372d6530303122 | 13/0/38c5301a738844140b52c8ba81246e6e6365e34f53cbc81a6c4e7c2659ef2ca7 | 11/0/1c1826eca9c6ac24b0ed3e19b5ab39881a1a05daec35a39f9a2ffc2cb29253ec | -2/0 | 1 | 753/29/e50af877a7429f31b527faa9e104e7ab2d4e65a83abd24028efd7ca67fc4288b/1 | 2020206222726f6f74222c0a20202020 | 2c0a20202020622273796d706c656374 | C2 | <module> | workspace-component | synthetic-path-containment |
| R010.016 | 780 | 622273796d706c65637469635f6d617022 | 622273796e7468657469632d73757065727669736f7222 | 17/0/922e878a292bdb107b89ec775add2c1aa83ed38350836ce0429c53b7af4fb1dd | 23/0/aea88b6f78c6cfb42a8b93341b04fc1a43514bd8371df048f810187554684d46 | 6/0 | 1 | 772/33/70db820b7ae0e2ec92e491c02456f0799fbc999f5113f3a812aca080d95614d5/1 | 75746f646c2d746d70222c0a20202020 | 2c0a290a4e4f5445535f434f4d504f4e | C2 | <module> | repository-component | synthetic-path-containment |
| R010.017 | 844 | 622270617065727322 | 622273796e74686574696322 | 9/0/b77085414785b315b8c681dfdd7e37b9fc476d5066322895aeee3624b61800b5 | 12/0/8506d1fb83d656680b91c66f0af32154738729c585a1308bbe8c945a20bac9a1 | 3/0 | 2 | 804/89/ca337de0682472f98d6dbcaa6ba2a187c36c477805067d3fcb25a60293dd00a1/1 | 504f4e454e5453202b20280a20202020 | 2c0a20202020622232372d706f736974 | C2 | <module> | paper-component | synthetic-path-containment |
| R010.019 | 859 | 622232372d706f7369746976652d6e6577746f6e2d7472616e736c6174696f6e2d7265636970726f6369747922 | 62227032372d6530303122 | 45/0/ad98710c9b656ce0459cb679432d2860ba7effc0de3db7167ca7be99e5b652bf | 11/0/1c1826eca9c6ac24b0ed3e19b5ab39881a1a05daec35a39f9a2ffc2cb29253ec | -34/0 | 2 | 843/77/da27784f4bb1b58cad71dad99fcef06ec94f356ad2ce67870ea1147ca9091a44/1 | 206222706170657273222c0a20202020 | 2c0a2020202062226e6f746573222c0a | C2 | <module> | paper27-component | synthetic-path-containment |
| R010.021 | 910 | 62226e6f74657322 | 6222636f6e74726f6c7322 | 8/0/25b8716449d8db8c148e009e81ee8707f44451e05b2f414d81a980e010977916 | 11/0/2ac94f410dfee149e8513a6da5c8767453ac0a4f850c88bb1c81887f6ce4c10a | 3/0 | 1 | 902/24/abf1c8ccb4d46b1ce768e25a0246aa9b3f9daad87d1b93aaee0d62277fa5b257/1 | 636970726f63697479222c0a20202020 | 2c0a290a45564944454e43455f504152 | C2 | <module> | notes-component | synthetic-path-containment |
| R010.018 | 975 | 622270617065727322 | 622273796e74686574696322 | 9/0/b77085414785b315b8c681dfdd7e37b9fc476d5066322895aeee3624b61800b5 | 12/0/8506d1fb83d656680b91c66f0af32154738729c585a1308bbe8c945a20bac9a1 | 3/0 | 2 | 935/89/4a6fbbb35a4f2e79817533704f6a5edc8a1b150a73f497bff51e74f4659fec2c/1 | 504f4e454e5453202b20280a20202020 | 2c0a20202020622232372d706f736974 | C2 | <module> | paper-component | synthetic-path-containment |
| R010.020 | 990 | 622232372d706f7369746976652d6e6577746f6e2d7472616e736c6174696f6e2d7265636970726f6369747922 | 62227032372d6530303122 | 45/0/ad98710c9b656ce0459cb679432d2860ba7effc0de3db7167ca7be99e5b652bf | 11/0/1c1826eca9c6ac24b0ed3e19b5ab39881a1a05daec35a39f9a2ffc2cb29253ec | -34/0 | 2 | 974/77/1a27a0bd40fa6a751426f1e29ffd2d51b9f87fa5031ae63d08f240164df95e3f/1 | 206222706170657273222c0a20202020 | 2c0a2020202062226275696c64222c0a | C2 | <module> | paper27-component | synthetic-path-containment |
| R010.022 | 1041 | 62226275696c6422 | 62226f75747075747322 | 8/0/e308fd305c028738ad159000e73ed67b55c6e712aff6912f61e06ee194b9bb28 | 10/0/fb644a6c098e1857b8cc18c2ed74fa18acff21e083589396f20578f7c8fb3c85 | 2/0 | 1 | 1033/24/5f81142fadcbbf737b8fc0b023a1afe716728c91b0ef10f0e66575db5fe80e3c/1 | 636970726f63697479222c0a20202020 | 2c0a290a45564944454e43455f4e414d | C2 | <module> | build-component | synthetic-path-containment |
| R010.023 | 1069 | 62227265636f766572792d3631303361396466306333642d65766964656e636522 | 622273796e7468657469632d72756e2d737461746522 | 33/0/2a3f4ccc87ade439a49548c99b6fa8c283effb73cd1c2cc654678f67fc5e90f4 | 22/0/0359ef439db90e03847159f54fb4bd87893e50814bf213656033410a36c5b2e7 | -11/0 | 1 | 1061/49/658bf025e6c5c63c1472a9d2aea9e22de65b086753ae1dac6c36093c30b276ab/1 | 45564944454e43455f4e414d45203d20 | 0a5553525f42494e5f434f4d504f4e45 | C2 | <module> | evidence-component | synthetic-path-containment |
| R010.014 | 1182 | 6222726f6f7422 | 6222746d7022 | 7/0/9427da7b54d16a6d8a6c297832cb3d37e30b64faa6070f6f6554c3892b73b914 | 6/0/5c5e4194a78af10986e406bd1b5a53caed08d3f7c645f41413816e84a60129dc | -1/0 | 2 | 1166/39/0362b0553ecca5cfd0bad50584dfb8441c7b0556e19369cead1de0baa963abbb/1 | 504f4e454e5453203d20280a20202020 | 2c0a2020202062226d696e69636f6e64 | C2 | <module> | root-component | synthetic-path-containment |
| R010.024 | 1195 | 62226d696e69636f6e64613322 | 62227032372d6530303122 | 13/0/f84c66b1594ca57fa7fc2b3b93acb473e2cc0ebc234724028b3b9f651a45b445 | 11/0/1c1826eca9c6ac24b0ed3e19b5ab39881a1a05daec35a39f9a2ffc2cb29253ec | -2/0 | 1 | 1187/29/76229f582085aa2ff68a61374bbd136e2d4dba3c70fba440f8b01f4e2ca5f251/1 | 2020206222726f6f74222c0a20202020 | 2c0a20202020622262696e222c0a290a | C2 | <module> | python-component | synthetic-path-containment |
| R045.001 | 12009 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 11985/57/fa6ebf601d9efacfc4a8be7b8efdec56e2ea116576e98be4df823b4a69e2a710/1 | 2020207472793a0a2020202020202020 | 6664290a202020202020202072657475 | C5 | close_fd | close | close-fault,stream-finalization |
| R045.002 | 12167 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 12143/57/84d08a4c5a6912243659652639064eba4c901d119850a79eb76156d152091221/1 | 2020207472793a0a2020202020202020 | 6664290a202020202020202072657475 | C5 | close_owned | close | close-fault,stream-finalization |
| R053.001 | 12593 | 6f732e707265616428 | 65303031507265616428 | 9/0/f0d99132c11de3bed255353b044bb82fb17d3fdfda5e20d597aec3eb1d69d373 | 10/0/7e3d7f55381789ee7ee7e4e57ec9d6f4cc20f984cddd783c7fab9737992b3e61 | 1/0 | 2 | 12585/25/2fd36c2d596bda269fa638a762108e2ba9199ebe21bd8341b3d4f2ef67ec212a/1 | 20202020202020207069656365203d20 | 66642c20616d6f756e742c206f666673 | C5 | pread_exact | pread | report-truncation,synthetic-input |
| R053.002 | 12824 | 6f732e707265616428 | 65303031507265616428 | 9/0/f0d99132c11de3bed255353b044bb82fb17d3fdfda5e20d597aec3eb1d69d373 | 10/0/7e3d7f55381789ee7ee7e4e57ec9d6f4cc20f984cddd783c7fab9737992b3e61 | 1/0 | 2 | 12816/25/8324ca660549e9de07d314be2f7e887800c433d056e4ce8e5cd4624fee2cd817/1 | 2073697a65290a202020206e65656428 | 66642c20312c2073697a6529203d3d20 | C5 | pread_complete | pread | report-truncation,synthetic-input |
| R041.001 | 12987 | 6f732e777269746528 | 65303031577269746528 | 9/0/69b370a3d20e2fc9252c6ee4b583b937450c727efea1f838f59c515ba85e9df5 | 10/0/9ccf444fcc3d2a26a5a41cdeca7ba2829ac45a52ecfa4a98be2173b1df9a9317 | 1/0 | 1 | 12979/25/c2f6bd243d5dea619b3d42a64e3f520e9f8c7adae15f26f0ce41c2455675d5a1/1 | 20202020202020616d6f756e74203d20 | 66642c20646174615b6f66667365743a | C5 | write_all | raw-write | handshake,report-framing |
| R071.001 | 18119 | 6e6f726d616c697a655f7369676e616c7328 | 653030314e6f726d616c697a655369676e616c7328 | 18/0/500b47340993fb0bc9147884dc3280f2928981800091161ff11dcfcc697e146c | 21/0/a9a69805990b1370942777b9839b71cd6c2e2bc89257b96f58903ee6398cebc5 | 3/0 | 5 | 18111/34/01b5d5abb059cda39af0bda7b80e64afe493fe3c5f427b04145dac1644ccc13a/1 | 2c20226e6f66696c6522290a20202020 | 290a2020202066697273742c20666972 | C6 | runtime | signal-normalizer | synthetic-signal-state |
| R052.001 | 18475 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 18467/25/893da60934e05efaa61af3308b91a1120402a7dbcdffba697b2354bedf6073b0/1 | 202020202020202076616c7565203d20 | 6664290a20202020202020206e656564 | C5 | runtime | fstat | synthetic-only-file-state |
| R050.001 | 19019 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 18995/56/c63938fb858a855856c2b4480b1d941397ee1d6961ab1c1797373dbe7c455e2c/1 | 20202020206664203d20747261636b28 | 62222f222c204449525f464c41475329 | C5 | __init__ | open | synthetic-only-file-state |
| R052.002 | 19107 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 19099/25/b0f5211172d74b1af4397c31d507db0dd83301c0ab8f9dab0314ad8598c3d0e0/1 | 617070656e64286e6f64655f6b657928 | 66642929290a2020202020202020666f | C5 | __init__ | fstat | synthetic-only-file-state |
| R050.002 | 19182 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 19158/56/e09097d4a0ef9fc2c2a3304830740c99b053590bc4a4b21150dfc5863da52437/1 | 20202020206664203d20747261636b28 | 636f6d706f6e656e742c204449525f46 | C5 | __init__ | open | synthetic-only-file-state |
| R052.003 | 19294 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 19286/25/0a68c0dacde79f895bab7f027af4e05e15dcfbd643a70c2aa579ced5ad6b1e37/1 | 617070656e64286e6f64655f6b657928 | 66642929290a0a20202020646566206c | C5 | __init__ | fstat | synthetic-only-file-state |
| R050.003 | 19968 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 19944/56/8edc4beefcf9c460da9d0b5596482bd5cd8a44eae694cb15c8e8bc39f6e57588/1 | 20202020206664203d20747261636b28 | 62222f222c204449525f464c41475329 | C5 | __init__ | open | synthetic-only-file-state |
| R052.004 | 20062 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 20046/41/9fd4ff81dfd1c4b895532c6c67a6ee64eea69ae428bb85b6f117a9c760e48e5f/1 | 735b305d203d206e6f64655f6b657928 | 666429290a2020202020202020202020 | C5 | __init__ | fstat | synthetic-only-file-state |
| R050.004 | 20165 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 20141/56/22414072d09412223c82bfa75a841ad015e6776d6fe27d769de347c80d68cee7/1 | 20202020206664203d20747261636b28 | 636f6d706f6e656e742c204449525f46 | C5 | __init__ | open | synthetic-only-file-state |
| R052.005 | 20287 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 20271/41/e8993bc76e4dcf0f5e3436797aac5b404664d53f2a8bf2f55b9eb2edc57ebae2/1 | 6465785d203d206e6f64655f6b657928 | 666429290a2020202020202020202020 | C5 | __init__ | fstat | synthetic-only-file-state |
| R052.006 | 20887 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 20871/41/23feb8d4e3c1edff3acb75d87e89cac6e6896f03382be08be8d793d1ad87b9ad/1 | 2e6b6579203d206e6f64655f6b657928 | 666429290a202020202020202073656c | C5 | __init__ | fstat | synthetic-only-file-state |
| R052.007 | 20971 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 20963/25/575f7707ee9eead33397d13ea467757eeae0d5aad5c6a033a1a6f5127a4f8e9e/1 | 20206e656564286e6f64655f6b657928 | 73656c662e66642929203d3d2073656c | C5 | verify | fstat | synthetic-only-file-state |
| R051.001 | 21127 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 21119/24/ced5c6eb3027a81d806fe0eb04768454d235dba4ba8af0e40d41e3246b7b7d87/1 | 202020202020206265666f7265203d20 | 73656c662e6e616d652c206469725f66 | C5 | verify | stat | synthetic-only-file-state |
| R050.005 | 21279 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 21271/24/afedc69e05b9685af9d7065e4528b0bcd8e1f62c54e40cd91d93c5ed2e82eb58/1 | 20206672657368203d20747261636b28 | 73656c662e6e616d652c20524541445f | C5 | verify | open | synthetic-only-file-state |
| R052.008 | 21376 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 21344/73/dec30712b7f0f2cd9a5ced99459d6235fac17a78bc22d42009e8c61e8f5f0c9b/1 | 20206e656564286e6f64655f6b657928 | 66726573682929203d3d2073656c662e | C5 | verify | fstat | synthetic-only-file-state |
| R052.009 | 21543 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 21511/73/6202b33a965de9640573e98dbb2a9d532636a457abd51dbe4d6b1258cd91444f/1 | 20206e656564286e6f64655f6b657928 | 66726573682929203d3d2073656c662e | C5 | verify | fstat | synthetic-only-file-state |
| R051.002 | 21619 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 21611/24/c08380b1c2afc33d9cb2bcf9800a2cbf20686a3bf8bda6b9413aee4ebca165ae/1 | 20202020202020206166746572203d20 | 73656c662e6e616d652c206469725f66 | C5 | verify | stat | synthetic-only-file-state |
| R051.003 | 22064 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 22048/40/05c422bcd75b65eade5fe1e9584fab1aa0a95fd5c3dc8acba09aba00b5c894ff/1 | 65630a202020206265666f7265203d20 | 6e616d652c206469725f66643d636861 | C5 | open_fixed | stat | synthetic-only-file-state |
| R050.006 | 22489 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 22465/56/04272ed26cc87e955ce5f3de9a7769fa4748a836abcec6e04e13631fd9e38d3d/1 | 0a202020206664203d20747261636b28 | 6e616d652c20524541445f464c414753 | C5 | open_fixed | open | synthetic-only-file-state |
| R052.010 | 22555 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 22523/73/025d6d95fee9c35e78f51bb6c89bbe4968c27421ad280072d9c288781b964c62/1 | 20206e656564286e6f64655f6b657928 | 66642929203d3d206e6f64655f6b6579 | C5 | open_fixed | fstat | synthetic-only-file-state |
| R051.004 | 22864 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 22856/24/acc1faaae762b8a855ce9eeec84960257d8c9abef362859c635c9770a42856ce/1 | 293a0a202020206265666f7265203d20 | 53454c465f4e414d452c206469725f66 | C5 | open_actor_self | stat | synthetic-only-file-state |
| R050.007 | 23301 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 23293/24/05194937cf0afb0296638ea1457bde1c84418efbf4ce4c952a20fe2df8d1e8e6/1 | 0a202020206664203d20747261636b28 | 53454c465f4e414d452c20524541445f | C5 | open_actor_self | open | synthetic-only-file-state |
| R052.011 | 23372 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 23340/73/8f2ba89d1109ec00be206214302be2e8b7e20849793135208bd3abae6b0c21b8/1 | 20206e656564286e6f64655f6b657928 | 66642929203d3d206e6f64655f6b6579 | C5 | open_actor_self | fstat | synthetic-only-file-state |
| R051.005 | 23832 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 23816/40/426e6828684115eb1ddc4841f88e63bdb2a0232381f0771ba7baf1b6f96a8f04/1 | 293a0a202020206265666f7265203d20 | 6e616d652c206469725f66643d636861 | C5 | open_tool | stat | synthetic-only-file-state |
| R050.008 | 24155 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 24131/56/05924cb9081f6504fef1867a89cc6dd8dd02d26f4fd007b061bfe449fb7c30e8/1 | 0a202020206664203d20747261636b28 | 6e616d652c20524541445f464c414753 | C5 | open_tool | open | synthetic-only-file-state |
| R052.012 | 24221 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 24189/73/080bdcb2a3a1f2abda4b9e4068d1a332daa485c4590c6881a59c816bb79ba6b0/1 | 20206e656564286e6f64655f6b657928 | 66642929203d3d206e6f64655f6b6579 | C5 | open_tool | fstat | synthetic-only-file-state |
| R010.002 | 26998 | 2f726f6f742f6175746f646c2d746d702f73796d706c65637469635f6d6170 | 2f746d702f7032372d653030312d73796e7468657469632d73757065727669736f72 | 31/0/5ec9b3286ccc9a969a56102d036f81e733a25c9865f17aba65ff3ec1196d7727 | 34/0/257871f68240c596807d192a892bdfa27b7164e7f8273d2688e37349c9ab916f | 3/0 | 2 | 26990/47/d521a397e109f68ce405d800c539f5b2bf8a6f072b094d7907a40402df2acde6/1 | 202020202020202062226364202d2d20 | 207c7c2065786974203132355c6e220a | C2 | build_inner | workspace-root | synthetic-path-containment |
| R010.004 | 27300 | 2f726f6f742f6d696e69636f6e6461332f62696e2f707974686f6e33 | 2f746d702f7032372d653030312d73796e7468657469632d73757065727669736f722f707974686f6e2d73747562 | 28/0/10658b016c4e2aeb86a28c64631f2452408cc3c40c8a383239cb1369dd9d52dd | 46/0/959ce2c39554d5e0b553b71eec4a718c2af2110cfc658b61ee29e5cf0d82b91c | 18/0 | 2 | 27292/44/c9375809560f4f80fbefc64002289c1c769d5f547b409677a5997deb6e0ac828/1 | 55544320220a20202020202020206222 | 202d53202d42202d50202d6320220a20 | C2 | build_inner | python-locator | synthetic-path-containment |
| R051.006 | 27800 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 27776/56/6b7f0967bd1a1cf6c9c40466f47501e1f1519a91eed6af1e1eb13520d86f97c7/1 | 202020202020206265666f7265203d20 | 5354415455535f4e414d452c20646972 | C5 | __init__ | stat | synthetic-only-file-state |
| R050.009 | 27930 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 27914/40/535a7f1f62e7623fcdb3fa7966dd5b6298a4f389c52d939331ef5c4eeecb2992/1 | 73656c662e6664203d20747261636b28 | 5354415455535f4e414d452c20524541 | C5 | __init__ | open | synthetic-only-file-state |
| R052.013 | 28021 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 28013/25/eb423fe6242789c273584e0795512a3d0d408bd9ea34f1a752edafb4f8ccbe8c/1 | 646765725f737461626c655f6b657928 | 73656c662e66642929203d3d206c6564 | C5 | __init__ | fstat | synthetic-only-file-state |
| R052.014 | 29334 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 29326/25/fa8ea3ef094e8d506738198bf484a355e7863b0e41a4346bdd80d651eaff1e8c/1 | 0a202020202020202068656c64203d20 | 73656c662e6664290a20202020202020 | C5 | verify | fstat | synthetic-only-file-state |
| R051.007 | 29476 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 29452/56/db4b6de3f4ca663ccbf450a8f4622b8657224df9419fc27d5e75426d4715c405/1 | 202020202020206265666f7265203d20 | 5354415455535f4e414d452c20646972 | C5 | verify | stat | synthetic-only-file-state |
| R050.010 | 29692 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 29676/40/694d2aee8848f9e682740fccf68cee28ca5894248bf77dceb9097c0fe3cea84b/1 | 20206672657368203d20747261636b28 | 5354415455535f4e414d452c20524541 | C5 | verify | open | synthetic-only-file-state |
| R052.015 | 29786 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 29778/25/17afb03a05d0a02084892f39d95ac8621a50f6e56f5293c6fa04f0dfff263913/1 | 202020202020206f70656e6564203d20 | 6672657368290a202020202020202020 | C5 | verify | fstat | synthetic-only-file-state |
| R052.016 | 30033 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 30025/25/b6c4889f440ff1d852633de622ade8c6fe151212c1030a592a840ae4c00d0dc6/1 | 202020202066696e616c5f6664203d20 | 6672657368290a202020202020202020 | C5 | verify | fstat | synthetic-only-file-state |
| R051.008 | 30074 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 30066/24/9bd1a1817c7b7b247ac5da8d7086c178909041b8360c931ad0cf2c36c8d9cb98/1 | 20202066696e616c5f70617468203d20 | 5354415455535f4e414d452c20646972 | C5 | verify | stat | synthetic-only-file-state |
| R051.009 | 30830 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 30822/24/2a34b627c3ddaa185ba84d1a95642745e0f5aa207332bb3b2bed705f1faae842/1 | 2e6b6579203d206e6f64655f6b657928 | 6e616d652c206469725f66643d636861 | C5 | __init__ | stat | synthetic-only-file-state |
| R051.010 | 30950 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 30942/24/406c5703e290ebd758719901a8e3ef8c03cae507eb6ae8c2fd1aaa53daf65cce/1 | 202020202020202076616c7565203d20 | 73656c662e6e616d652c206469725f66 | C5 | verify | stat | synthetic-only-file-state |
| R054.001 | 31356 | 6f732e726561646c696e6b28 | 65303031526561646c696e6b28 | 12/0/671880c9581af52d75a7ff7e33849c21a527a022639fa44a4081cf01ad9bdf9e | 13/0/09539add97c332409c8fa2541b90284a018f306e162a65e81ae85b3a6c3db0a5 | 1/0 | 1 | 31348/28/4fd659cd1c3da564a00b894da4586942fba9e277e1e3cc71c47edb8179e6cd78/1 | 22290a20202020202020206e65656428 | 73656c662e6e616d652c206469725f66 | C5 | verify | readlink | synthetic-only-link-state |
| R051.011 | 31463 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 31455/24/069200add5e094b7bbd492a14e6615738ba453d8619201e8dff04cab95be3a3d/1 | 20206e656564286e6f64655f6b657928 | 73656c662e6e616d652c206469725f66 | C5 | verify | stat | synthetic-only-file-state |
| R051.012 | 38150 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 38142/24/0e88ab7fbf9da950f9cc2496c03e0aba5faf4400cf08babfee4f1ff59e399b8c/1 | 202020202020202076616c7565203d20 | 7265636f72645b226e616d65225d2c20 | C5 | finalize_observation_path | stat | synthetic-only-file-state |
| R050.011 | 47000 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 46984/40/415894911daaa38d7b644aadc66fe1440d731546a726b7c55cd97230a1c4d5ec/1 | 726561645f6664203d20747261636b28 | 6e616d652c20524541445f464c414753 | C5 | <module> | open | synthetic-only-file-state |
| R052.017 | 47097 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 47081/41/b17feaf6c18b660d5415b670354e73b21a0521db7af66507c615dc37f9eaea2c/1 | 202020202020206f70656e6564203d20 | 726561645f6664290a20202020657863 | C5 | <module> | fstat | synthetic-only-file-state |
| R052.018 | 47919 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 47903/41/f0ff3b0f26a8855861a218456c1a4321657d6acc09f8a08c249bc1bffee6bca8/1 | 2066696e616c5f6f70656e6564203d20 | 726561645f6664290a20202020657863 | C5 | <module> | fstat | synthetic-only-file-state |
| R051.013 | 48300 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 48292/24/6acfe825889125364f85e69712a76d36f54b824d5348653213137e37edcba88b/1 | 202020202020206265666f7265203d20 | 534f555243455f4e414d452c20646972 | C5 | observe_source | stat | synthetic-only-file-state |
| R050.012 | 48960 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 48952/24/da5d8c850b10d4f21593e5e83b27dd2f213796ef57fb4b2ccbd3cf1d3c136c55/1 | 706174685f6664203d20747261636b28 | 534f555243455f4e414d452c20504154 | C5 | observe_source | open | synthetic-only-file-state |
| R052.019 | 49122 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 49034/185/ed14c1ad0389ea8e7ee0e69adf3354a86db5c81e305a0d37472085e711c5376d/1 | 202020206966206e6f64655f6b657928 | 706174685f6664292920213d206e6f64 | C5 | observe_source | fstat | synthetic-only-file-state |
| R051.014 | 51086 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 51070/40/c02eca1f96fcc49abef33e1bd48e232aae43995396236b9e33ec1a7907fa1b36/1 | 202020202020206265666f7265203d20 | 6e616d652c206469725f66643d646972 | C5 | observe_candidate | stat | synthetic-only-file-state |
| R050.013 | 51781 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 51773/24/12fa206dc8ccf8aa316f16b9fae1f6f0e5fb92d7ff082b45558e9027026bda4b/1 | 706174685f6664203d20747261636b28 | 6e616d652c20504154485f464c414753 | C5 | observe_candidate | open | synthetic-only-file-state |
| R052.020 | 51930 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 51842/185/61bb4f6e6e1bec297b6c89fa5420341384b6ce3fb46a2d8463fc0041ce0f9d00/1 | 202020206966206e6f64655f6b657928 | 706174685f6664292920213d206e6f64 | C5 | observe_candidate | fstat | synthetic-only-file-state |
| R051.015 | 53983 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 53975/24/577235147516ccf12014bfdc3e97643b86cff0c78ae643fe59391c6f9709dc92/1 | 202020202020206265666f7265203d20 | 45564944454e43455f4e414d452c2064 | C5 | begin_evidence | stat | synthetic-only-file-state |
| R050.014 | 54648 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 54624/56/6989581280f102e8786b75046d56d6df7abe95699c84bf5f3dfc4508174eb9be/1 | 706174685f6664203d20747261636b28 | 45564944454e43455f4e414d452c2050 | C5 | begin_evidence | open | synthetic-only-file-state |
| R052.021 | 54853 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 54765/185/f26991836e24adeace3299a19aae95bd464d43dd698f0367d8094e3f86cecd1b/1 | 202020206966206e6f64655f6b657928 | 706174685f6664292920213d206e6f64 | C5 | begin_evidence | fstat | synthetic-only-file-state |
| R050.015 | 55168 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 55144/56/348e24fc1db32f552cc1b99166b17b33cd2611267db4e2310cf270ef335ee754/1 | 746f72795f6664203d20747261636b28 | 45564944454e43455f4e414d452c2044 | C5 | begin_evidence | open | synthetic-only-file-state |
| R052.022 | 55399 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 55391/25/7832e4e66b44b163be322b8d31a70cba2698655aca27822cd448d3337d646d65/1 | 202020202020206f70656e6564203d20 | 6469726563746f72795f6664290a2020 | C5 | begin_evidence | fstat | synthetic-only-file-state |
| R052.023 | 57397 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 57381/41/c352764eee763e8903e39c1e410b21f0676a7910a94da09b19fbc1f098dbe708/1 | 5f6b6579203d206e6f64655f6b657928 | 706174685f666429290a202020202020 | C5 | finish_evidence | fstat | synthetic-only-file-state |
| R052.024 | 57638 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 57630/25/5dffd50a542803125e42291a2df86283cebebca4ddff32801f8fc3b80c5bed29/1 | 5f6b6579203d206e6f64655f6b657928 | 6469726563746f72795f666429290a20 | C5 | finish_evidence | fstat | synthetic-only-file-state |
| R051.016 | 58018 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 58010/24/9b37bc68d90dae0b08bb118e920c81546b996259c32dab8e0efb237d153ea901/1 | 20202020202020206669727374203d20 | 45564944454e43455f4e414d452c2064 | C5 | finish_evidence | stat | synthetic-only-file-state |
| R050.016 | 58980 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 58956/56/50525f51d8a8dba10dcab5b4fdfbcf0f608da00758bdc291866eaafa494ef0f2/1 | 706174685f6664203d20747261636b28 | 45564944454e43455f4e414d452c2050 | C5 | finish_evidence | open | synthetic-only-file-state |
| R052.025 | 59130 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 59122/25/81d4dd76aeb7be4329abf5be9b11ba6fa578725d9800991a0152952cc826fc61/1 | 5f6b6579203d206e6f64655f6b657928 | 66726573685f706174685f666429290a | C5 | finish_evidence | fstat | synthetic-only-file-state |
| R050.017 | 59584 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 59560/56/a181cc43cc3d6b5e9a2080fd19f08ee1a69cbe1de0d42ac1655c43c515ea4625/1 | 746f72795f6664203d20747261636b28 | 45564944454e43455f4e414d452c2044 | C5 | finish_evidence | open | synthetic-only-file-state |
| R052.026 | 59751 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 59743/25/251a616352155121752fa0338652c9345babd24ea9a2bbbc224f8fbf514623e7/1 | 5f6b6579203d206e6f64655f6b657928 | 66726573685f6469726563746f72795f | C5 | finish_evidence | fstat | synthetic-only-file-state |
| R051.017 | 60224 | 6f732e7374617428 | 653030315374617428 | 8/0/48f68cdc81369cac7917b514392317bcc3b5380a42302dacd029093b43be25fc | 9/0/9671e35ff80dce6fbc0bef7a52aaed9b78c2c5b35e4f085afd7c241677819384 | 1/0 | 17 | 60216/24/f36884b61e3797dcd172fcaf8e4393c721564e23483b81325ebd8f7eb5f19d03/1 | 202020202020202066696e616c203d20 | 45564944454e43455f4e414d452c2064 | C5 | finish_evidence | stat | synthetic-only-file-state |
| R050.018 | 66535 | 6f732e6f70656e28 | 653030314f70656e28 | 8/0/185f5f4a99a7466396f22b72916b9a79eb66b135e94580d23ff5523eea9d5c34 | 9/0/12c7e43d6dececaee2e85c5edba297523d0c40f9fc2d2a00c252fb0ac96aea4f | 1/0 | 18 | 66527/24/491d0990a128a6ea4bb3c2202bffe3c54a18b1a5ac446a2406be9e90ce1b191d/1 | 7363616e5f6664203d20747261636b28 | 62222e222c204449525f464c4147532c | C5 | inventory_fresh | open | synthetic-only-file-state |
| R052.027 | 66599 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 66575/57/8a65862b4f131f927cc9270beebcabf721d43ab33c32b9bed59f61b176e2fc94/1 | 202020206966206e6f64655f6b657928 | 7363616e5f6664292920213d20657870 | C5 | inventory_fresh | fstat | synthetic-only-file-state |
| R055.001 | 66751 | 6f732e7363616e64697228 | 653030315363616e64697228 | 11/0/9e64c843404731cde13441751329f7e0c190831736eb2c40f373bd3870736a64 | 12/0/b065dd44d43395f6e72d48a30de9e1f63725a25216890a404931ce0e1ed61830 | 1/0 | 1 | 66743/27/5ac7dae0436f8564a86c2fa8b427bb98484c58ad1fe8706778a989314b3060cb/1 | 20202020206974657261746f72203d20 | 7363616e5f6664290a20202020202020 | C5 | inventory_fresh | scandir | synthetic-only-inventory |
| R052.028 | 68341 | 6f732e667374617428 | 65303031467374617428 | 9/0/2b18aa84ce8e7835f45ba3f927802fe238dc55553a030d1f628eadbdc1d028cc | 10/0/7632ecc8b44c42525005804175386cd80f611adeb22f06a75101bbb0b70414bb | 1/0 | 28 | 68317/57/6f112397745009abfe3c129f56ef3a447a95635f6082cf751820b2e22b68a1e5/1 | 202020206966206e6f64655f6b657928 | 7363616e5f6664292920213d20657870 | C5 | inventory_fresh | fstat | synthetic-only-file-state |
| R020.001 | 179049 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 179041/34/0c11add7dca6fd3f450958e260ec4e15e1541d96263fb2364bb41dde7141a1ed/1 | 293a0a202020206265666f7265203d20 | 290a202020206966206265666f726520 | C3 | guarded_wait_once | clock | deadline,sticky-deadline |
| R033.001 | 179252 | 6f732e7761697470696428 | 653030315761697450696428 | 11/0/3eb3f6731914b4ff3a689224ff9cfebd6ba1c46d382c1080a1064098a1773b8a | 12/0/3c42e9595b72ca423ef5be59ec433d0259df1d86fc313b55b3a90faec8973c6c | 1/0 | 2 | 179244/27/ff88ee281f0902d208da291401362468c96ee039595615c90940b2bf7a1752dc/1 | 207374617475735f76616c7565203d20 | 7069642c206f732e574e4f48414e4729 | C4 | guarded_wait_once | wait | exit,signal,deadline |
| R020.002 | 179299 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 179283/50/3f147499c99945c6f918cba9ee9b5606fc17d36791f3ff1a100f7734f2b65aa5/1 | 20202020206f62736572766564203d20 | 290a2020202065786365707420496e74 | C3 | guarded_wait_once | clock | deadline,sticky-deadline |
| R020.003 | 179367 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 179343/66/ec8a098da78135522148c813d57ba4500dd04d36909db9dcf6f5caf484ebc80e/1 | 20202020206f62736572766564203d20 | 290a202020202020202072657475726e | C3 | guarded_wait_once | clock | deadline,sticky-deadline |
| R020.004 | 179688 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 179664/66/7579b73f8bec57054c661934ca2fdaa3e5dde910b6e4e2366937c6c3ad6159fe/1 | 20202020206f62736572766564203d20 | 290a202020202020202072657475726e | C3 | guarded_wait_once | clock | deadline,sticky-deadline |
| R021.001 | 181016 | 74696d652e736c65657028 | 65303031536c65657028 | 11/0/1e1cf2907bae3c166ec68f53467f0e8c757e13b064cfc5108c67a86ff5407c57 | 10/0/8318f94557c8d7c6b64f16faeb7196d31b60cf566fbbc1139bc7660864ded5f0 | -1/0 | 1 | 181008/27/96c598ea80686af7e38972b61a7667769666af7d696a867e881aca5f82367f81/1 | 727665645f6e730a2020202020202020 | 6d696e28302e30312c2072656d61696e | C3 | wait_deadline | sleep | deadline-poll |
| R033.002 | 181148 | 6f732e7761697470696428 | 653030315761697450696428 | 11/0/3eb3f6731914b4ff3a689224ff9cfebd6ba1c46d382c1080a1064098a1773b8a | 12/0/3c42e9595b72ca423ef5be59ec433d0259df1d86fc313b55b3a90faec8973c6c | 1/0 | 2 | 181140/27/2b9e0e78a456b63e1b54155020296e3db92335d8c6ae48c61084a1e5a6f279c5/1 | 207374617475735f76616c7565203d20 | 7069642c2030290a2020202020202020 | C4 | wait_blocking | wait | exit,signal,deadline |
| R020.005 | 181341 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 181333/34/8cab4a78f13147d643507352e8f12cb8d3211ec83bdec423813f91ca3bcbcec4/1 | 6f6465293a0a202020206e6f77203d20 | 290a202020206e656564286e6f77203c | C3 | remaining_poll_ms | clock | deadline,sticky-deadline |
| R020.006 | 181553 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 181545/34/918c47aa4ec048be1905ef9adac00d3b12cd06dfb83c052697e82b793f1006d2/1 | 636f6465293a0a202020206e65656428 | 29203c20646561646c696e652c20636f | C3 | require_before | clock | deadline,sticky-deadline |
| R044.001 | 181656 | 6f732e7365745f626c6f636b696e6728 | 65303031536574426c6f636b696e6728 | 16/0/f7c1800ac4828a442c7e49f24add1b4d5d9ef57614543d6cd59822a99a616b7a | 16/0/96d50eca9a10a849c75267c752f88ffb12dd005dc88116cfec5e9292b2d5350b | 0/0 | 8 | 181648/32/3d104aaa0afdba4ec0b21990627edb54c2115050a186a8d432252ef3a67565c2/1 | 696e652c20636f6465293a0a20202020 | 66642c2046616c7365290a2020202070 | C5 | read_token_eof | blocking | handshake,raw-dual-stream |
| R043.001 | 181696 | 73656c6563742e706f6c6c28 | 65303031506f6c6c28 | 12/0/bf1c9e8739b3df27211a2f733eda391e7e578ff603cd6bea74e107b67a1c87e4 | 9/0/68c398ed519219aa2cebc00cf9a4b5430a1d09ca2cdd52e90247d2de80bcdc45 | -3/0 | 3 | 181648/108/a8d5e71201f19da342709d3ab4e05eff551e5fa8f533571d6e712e45805ca300/1 | 65290a20202020706f6c6c6572203d20 | 290a20202020706f6c6c65722e726567 | C5 | read_token_eof | poll | deadline,raw-dual-stream,supervisor-loss |
| R040.001 | 182198 | 6f732e7265616428 | 653030315265616428 | 8/0/874160994e0c3f2eb96506c009e5fd940e5fcf15c638d2177ad61a611f022f38 | 9/0/04316f8445fd8e17304645f6bbd52605b42ec9c40e047aae727110176e3dcc94 | 1/0 | 7 | 182190/24/90ce7c3632e8e7f399baa7306ac2e058fb5859080d2275effa56ee865ac8442b/1 | 20202020202020207069656365203d20 | 66642c206c656e28746f6b656e29202b | C5 | read_token_eof | raw-read | handshake,raw-dual-stream,overflow,supervisor-loss |
| R044.002 | 182696 | 6f732e7365745f626c6f636b696e6728 | 65303031536574426c6f636b696e6728 | 16/0/f7c1800ac4828a442c7e49f24add1b4d5d9ef57614543d6cd59822a99a616b7a | 16/0/96d50eca9a10a849c75267c752f88ffb12dd005dc88116cfec5e9292b2d5350b | 0/0 | 8 | 182680/48/3bffbb9224b450bc37c53827c6bf6205c18b9fef9f3624ed6ea078a40c71e447/1 | 5f7374617274286664293a0a20202020 | 66642c2046616c7365290a2020202070 | C5 | wait_start | blocking | handshake,raw-dual-stream |
| R043.002 | 182736 | 73656c6563742e706f6c6c28 | 65303031506f6c6c28 | 12/0/bf1c9e8739b3df27211a2f733eda391e7e578ff603cd6bea74e107b67a1c87e4 | 9/0/68c398ed519219aa2cebc00cf9a4b5430a1d09ca2cdd52e90247d2de80bcdc45 | -3/0 | 3 | 182688/108/eb36a5ae32c58a4228a0e03364f792c6a9d19f58007f233e9fedc57d09d1e3e7/1 | 65290a20202020706f6c6c6572203d20 | 290a20202020706f6c6c65722e726567 | C5 | wait_start | poll | deadline,raw-dual-stream,supervisor-loss |
| R040.002 | 183056 | 6f732e7265616428 | 653030315265616428 | 8/0/874160994e0c3f2eb96506c009e5fd940e5fcf15c638d2177ad61a611f022f38 | 9/0/04316f8445fd8e17304645f6bbd52605b42ec9c40e047aae727110176e3dcc94 | 1/0 | 7 | 183048/24/f565faddadae6dc610a8d31201630955b4def1be9132cdd7a631489d56e1c877/1 | 20202020202020207069656365203d20 | 66642c2032290a202020202020202020 | C5 | wait_start | raw-read | handshake,raw-dual-stream,overflow,supervisor-loss |
| R040.003 | 183219 | 6f732e7265616428 | 653030315265616428 | 8/0/874160994e0c3f2eb96506c009e5fd940e5fcf15c638d2177ad61a611f022f38 | 9/0/04316f8445fd8e17304645f6bbd52605b42ec9c40e047aae727110176e3dcc94 | 1/0 | 7 | 183211/24/c557004f103abb4b08bd8217b371b2d018d5a5cd65e488bb68b81b2ffe27ac48/1 | 20202020202020206578747261203d20 | 66642c2031290a202020202020202020 | C5 | wait_start | raw-read | handshake,raw-dual-stream,overflow,supervisor-loss |
| R044.003 | 183379 | 6f732e7365745f626c6f636b696e6728 | 65303031536574426c6f636b696e6728 | 16/0/f7c1800ac4828a442c7e49f24add1b4d5d9ef57614543d6cd59822a99a616b7a | 16/0/96d50eca9a10a849c75267c752f88ffb12dd005dc88116cfec5e9292b2d5350b | 0/0 | 8 | 183363/48/136a21a6db5bce2081816ce5f294322913707f487f0036eb14f8a93679fd75bb/1 | 745f6c697665286664293a0a20202020 | 66642c2046616c7365290a2020202074 | C5 | prove_payload_input_live | blocking | handshake,raw-dual-stream |
| R040.004 | 183431 | 6f732e7265616428 | 653030315265616428 | 8/0/874160994e0c3f2eb96506c009e5fd940e5fcf15c638d2177ad61a611f022f38 | 9/0/04316f8445fd8e17304645f6bbd52605b42ec9c40e047aae727110176e3dcc94 | 1/0 | 7 | 183383/104/c87b728bba36efc0d67386e341e5d39e24c230475513af44fb87d96273f248da/1 | 20202020202020207069656365203d20 | 66642c2031290a202020206578636570 | C5 | prove_payload_input_live | raw-read | handshake,raw-dual-stream,overflow,supervisor-loss |
| R044.004 | 183555 | 6f732e7365745f626c6f636b696e6728 | 65303031536574426c6f636b696e6728 | 16/0/f7c1800ac4828a442c7e49f24add1b4d5d9ef57614543d6cd59822a99a616b7a | 16/0/96d50eca9a10a849c75267c752f88ffb12dd005dc88116cfec5e9292b2d5350b | 0/0 | 8 | 183547/32/9f963d9a939df70d5597a7028b3c8d2a6259697ec297be39ec3c2f464eb8ea19/1 | 6d7074792d6c69766522290a20202020 | 66642c2054727565290a0a6465662070 | C5 | prove_payload_input_live | blocking | handshake,raw-dual-stream |
| R044.005 | 183610 | 6f732e7365745f626c6f636b696e6728 | 65303031536574426c6f636b696e6728 | 16/0/f7c1800ac4828a442c7e49f24add1b4d5d9ef57614543d6cd59822a99a616b7a | 16/0/96d50eca9a10a849c75267c752f88ffb12dd005dc88116cfec5e9292b2d5350b | 0/0 | 8 | 183594/48/dbf80b9617fc7cced517bee2500189c31df72b2dae452187fb2f02a865999966/1 | 66656c696e65286664293a0a20202020 | 66642c2046616c7365290a2020202074 | C5 | probe_lifeline | blocking | handshake,raw-dual-stream |
| R040.005 | 183662 | 6f732e7265616428 | 653030315265616428 | 8/0/874160994e0c3f2eb96506c009e5fd940e5fcf15c638d2177ad61a611f022f38 | 9/0/04316f8445fd8e17304645f6bbd52605b42ec9c40e047aae727110176e3dcc94 | 1/0 | 7 | 183614/104/8ca9b880833f861789e2a44653418e6fa64320d4cf0640a0b0c3d963bcacb897/1 | 20202020202020207069656365203d20 | 66642c2031290a202020206578636570 | C5 | probe_lifeline | raw-read | handshake,raw-dual-stream,overflow,supervisor-loss |
| R060.001 | 183901 | 6f732e67657470696428 | 6530303147657450696428 | 10/0/ac6667ba75cea5a941084b9b116e35943c5bd980adc8c6d2452c8be2f55243d0 | 11/0/2cc17f8a5ac7e6b129d2385da21f110fdb23861034b7f517bd3ef7345bd1b7ba | 1/0 | 3 | 183893/26/360f4868cacf8a70dbd348e23ea4cc5862452500cf0dd1b120fc3adb9f3bcf1a/1 | 757065727669736f725f706964203d20 | 290a202020206e656564287375706572 | C4 | begin_line | getpid | supervisor-loss,topology |
| R020.007 | 192544 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 192536/34/e66204f7bcf3a1fa43d7864d7142814ff1fa2ddcdf3c9461dba7c2df88e4599f/1 | 6c696e65206973204e6f6e65206f7220 | 29203e3d20646561646c696e653a0a20 | C3 | capture_guard | clock | deadline,sticky-deadline |
| R020.008 | 192811 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 192803/34/0347702ea94dfaba1cb6490c4a0b4eaa3b3357a3671a1473de8c6a0beaa84365/1 | 6e67203d20646561646c696e65202d20 | 290a2020202069662072656d61696e69 | C3 | capture_poll_ms | clock | deadline,sticky-deadline |
| R040.006 | 195267 | 6f732e7265616428 | 653030315265616428 | 8/0/874160994e0c3f2eb96506c009e5fd940e5fcf15c638d2177ad61a611f022f38 | 9/0/04316f8445fd8e17304645f6bbd52605b42ec9c40e047aae727110176e3dcc94 | 1/0 | 7 | 195147/248/f8a8d7e77059c91d94d4dd701d57e02a672156cb3f782418155862f703eb810e/1 | 20202020202020207069656365203d20 | 66642c204348554e4b290a2020202020 | C5 | capture_read_once | raw-read | handshake,raw-dual-stream,overflow,supervisor-loss |
| R020.009 | 195305 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 195145/338/a1f937132a1aa25a4386543c52f6cfd5510952aa0952d341116c3d0e859f94b5/1 | 20202020206f62736572766564203d20 | 290a2020202065786365707420426c6f | C3 | capture_read_once | clock | deadline,sticky-deadline |
| R020.010 | 195372 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 195148/466/f81e212acf8f4b81e237317bfa0aa12932650892cced56696d84c2f3fc3b82f4/1 | 20202020206f62736572766564203d20 | 290a20202020202020206966206f6273 | C3 | capture_read_once | clock | deadline,sticky-deadline |
| R020.011 | 195538 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 195410/274/e78ce3653cd8ce6cbcb69fa7f81558d107e5ec0f7b2f1c476b41c82c463c623c/1 | 20202020206f62736572766564203d20 | 290a20202020202020206966206f6273 | C3 | capture_read_once | clock | deadline,sticky-deadline |
| R040.007 | 196648 | 6f732e7265616428 | 653030315265616428 | 8/0/874160994e0c3f2eb96506c009e5fd940e5fcf15c638d2177ad61a611f022f38 | 9/0/04316f8445fd8e17304645f6bbd52605b42ec9c40e047aae727110176e3dcc94 | 1/0 | 7 | 196528/248/6ccb66cdb852ae517a64c47d4f68b143608b0ed28443d0b8aef33e587495d58b/1 | 20202020202020207069656365203d20 | 66642c204348554e4b290a2020202020 | C5 | capture_lifeline_once | raw-read | handshake,raw-dual-stream,overflow,supervisor-loss |
| R020.012 | 196686 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 196526/338/9b42bd981c3231d7593fd8860b24d83325c63ffda5dfbcfd3aa1022fe8ef0909/1 | 20202020206f62736572766564203d20 | 290a2020202065786365707420426c6f | C3 | capture_lifeline_once | clock | deadline,sticky-deadline |
| R020.013 | 196753 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 196529/466/55678377f8aed09eb7779d0ce36e7fa0bd0b65bbd2385903920767ae0526f07b/1 | 20202020206f62736572766564203d20 | 290a20202020202020206966206f6273 | C3 | capture_lifeline_once | clock | deadline,sticky-deadline |
| R020.014 | 196919 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 196791/274/becbd845e16412342e5cb44c55fb8c6bfdb9e1abe9b574a29f7909d24298a4ad/1 | 20202020206f62736572766564203d20 | 290a20202020202020206966206f6273 | C3 | capture_lifeline_once | clock | deadline,sticky-deadline |
| R020.015 | 201513 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 201505/34/a1715cb84b265dddb9106243f3c8187b1370e9e702dc9a105d7453e586da69f1/1 | 46616c73650a202020206e6f77203d20 | 290a20202020646561646c696e65203d | C3 | enter_kill_reap | clock | deadline,sticky-deadline |
| R031.001 | 201746 | 6f732e6b696c6c28 | 653030315369676e616c28 | 8/0/fead1a75480e107f1108b1f250d6979f093eb96413facc5e515cea3b3c2128e5 | 11/0/205ba82f2e120b645fa062100b962a60719bce048bfb44ca341e91e88e33adb5 | 3/0 | 2 | 201738/24/44c6a58bfc1c48d888afecd5478fcf6546516d8567a491f07671255bb45198c9/1 | 2020207472793a0a2020202020202020 | 7069642c207369676e616c2e5349474b | C4 | enter_kill_reap | signal | signal-exit,deadline-cleanup |
| R044.006 | 202052 | 6f732e7365745f626c6f636b696e6728 | 65303031536574426c6f636b696e6728 | 16/0/f7c1800ac4828a442c7e49f24add1b4d5d9ef57614543d6cd59822a99a616b7a | 16/0/96d50eca9a10a849c75267c752f88ffb12dd005dc88116cfec5e9292b2d5350b | 0/0 | 8 | 202044/32/588dabf5dc4fa4776219dc17c0ea37aedeb8da77ea2457f5835d51224f8cc16d/1 | 6365645f6572726f72293a0a20202020 | 6f75745f66642c2046616c7365290a20 | C5 | capture_payload | blocking | handshake,raw-dual-stream |
| R044.007 | 202087 | 6f732e7365745f626c6f636b696e6728 | 65303031536574426c6f636b696e6728 | 16/0/f7c1800ac4828a442c7e49f24add1b4d5d9ef57614543d6cd59822a99a616b7a | 16/0/96d50eca9a10a849c75267c752f88ffb12dd005dc88116cfec5e9292b2d5350b | 0/0 | 8 | 202079/32/59206b37a215d6dc24d8a2fe7c6e98e3db99a76cc8320c1049eb72f2b2faf498/1 | 5f66642c2046616c7365290a20202020 | 6572725f66642c2046616c7365290a20 | C5 | capture_payload | blocking | handshake,raw-dual-stream |
| R044.008 | 202122 | 6f732e7365745f626c6f636b696e6728 | 65303031536574426c6f636b696e6728 | 16/0/f7c1800ac4828a442c7e49f24add1b4d5d9ef57614543d6cd59822a99a616b7a | 16/0/96d50eca9a10a849c75267c752f88ffb12dd005dc88116cfec5e9292b2d5350b | 0/0 | 8 | 202114/32/68c891afa5ec26345f1931afd93eb14653ad3b4f27986f3dee3fab4ccb2b4bee/1 | 5f66642c2046616c7365290a20202020 | 6c6966655f66642c2046616c7365290a | C5 | capture_payload | blocking | handshake,raw-dual-stream |
| R043.003 | 202167 | 73656c6563742e706f6c6c28 | 65303031506f6c6c28 | 12/0/bf1c9e8739b3df27211a2f733eda391e7e578ff603cd6bea74e107b67a1c87e4 | 9/0/68c398ed519219aa2cebc00cf9a4b5430a1d09ca2cdd52e90247d2de80bcdc45 | -3/0 | 3 | 202159/28/0c9ec09138084ad99d9e5cdd5ed87631bff58a1027b75df0df4baed6ed9be7ea/1 | 65290a20202020706f6c6c6572203d20 | 290a202020206d61736b73203d207365 | C5 | capture_payload | poll | deadline,raw-dual-stream,supervisor-loss |
| R045.003 | 229269 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 229213/121/4dba180285e8ee4d921a47daaf02a21d59e9a3ab438e8b35a8735f9ac132fe75/1 | 72793a0a202020202020202020202020 | 31290a20202020202020206578636570 | C5 | emit_and_exit | close | close-fault,stream-finalization |
| R045.004 | 229365 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 229357/25/05042d164ebe09e5678fcebac801120d5d886d884c62d0663c739b7b717d0d89/1 | 2020207472793a0a2020202020202020 | 31290a20202020657863657074204261 | C5 | emit_and_exit | close | close-fault,stream-finalization |
| R071.002 | 230044 | 6e6f726d616c697a655f7369676e616c7328 | 653030314e6f726d616c697a655369676e616c7328 | 18/0/500b47340993fb0bc9147884dc3280f2928981800091161ff11dcfcc697e146c | 21/0/a9a69805990b1370942777b9839b71cd6c2e2bc89257b96f58903ee6398cebc5 | 3/0 | 5 | 230036/34/24e69aab404a6e3e8d6483a023e3a39a23ee1a1a220f1ba2b13505959bff664e/1 | 697465292c0a20202020290a20202020 | 290a202020207061796c6f61645f6465 | C6 | spawn_payload | signal-normalizer | synthetic-signal-state |
| R020.016 | 230112 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 230096/50/90be11d22127d50f7bf9b8b17edb3a84806aecc6717eee4b24e86290c7224593/1 | 36345f616464280a2020202020202020 | 292c0a20202020202020205041594c4f | C3 | spawn_payload | clock | deadline,sticky-deadline |
| R030.001 | 230267 | 6f732e706f7369785f737061776e28 | 65303031537061776e28 | 15/0/31df13bbd38b806ec10b83328e469066a44abb27722e6e02f3effa919c07c797 | 10/0/76960ee047108b6b6b3000ceb60be573ce5aaa14786d77689b64d04e2950c115 | -5/0 | 2 | 230251/47/7e18d8159e124a07608fd0981f70708b84a588ed450e778fb56d4ff9eb2bd07b/1 | 646c696e650a20202020706964203d20 | 0a2020202020202020454e565f544f4f | C4 | spawn_payload | spawn | handshake,exit,signal,recovery-dispatch |
| R064.001 | 230935 | 6f732e6765747067696428 | 653030314765745067696428 | 11/0/1d7854664366aee924d81be4e248edf2806cd3a98ae1f33a7b1844ccf0f50903 | 12/0/1553148afe3eb3990ab1ffac71c3cd95319d73783aa8b16d33cf08f06da1e443 | 1/0 | 2 | 230927/27/620c490c6450b2ca2d25e0a0b220c5c4fe4764d13e765d7598b6c8603aa9c301/1 | 0a202020202020202070676964203d20 | 706964290a2020202065786365707420 | C4 | payload_topology | getpgid | topology |
| R062.001 | 231282 | 6f732e67657473696428 | 6530303147657453696428 | 10/0/b32444b755fcfe3161eb5e0dd3b9e8c4c5f2eab2b86c70d1f5827295bfe948bf | 11/0/9f3a8df4cdae81e24ae7171502a5ae2a282576c4106a52ab07b1aadcbed18eb6 | 1/0 | 4 | 231274/26/9a10577d758c46293112ee82098a0820ead5e1173a1f787443fed0fe7efa6a9d/1 | 3a0a2020202020202020736964203d20 | 706964290a2020202065786365707420 | C4 | payload_topology | getsid | topology |
| R073 | 233371 | 636f6e74657874203d20227761746368646f6722 | 636f6e74657874203d2065303031436f6e746578742829 | 20/0/63ee5f4dd6c23644564b7e93fe585ec1ef04a29f358d6681ea55152fb4c35549 | 23/0/bf2ba84352196f37a9d4644b3d7487415542fba2f2bc0158830d0f5b0a5e0530 | 3/0 | 1 | 233363/36/5668818cc6436eefdcfa8b7ba3b90f2ded49af82cb2a483e8bfbb365ce0eaa08/1 | 6365645f6572726f72293a0a20202020 | 0a20202020696620666f726365645f65 | C6 | finalize_watchdog | context-source | wrong-context,opposite-context |
| R045.005 | 233668 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 233588/169/2ad57b3bf5c2208c4ce43db75a995e8d28a15113fd1b1a75f388a2130fb0fd7e/1 | 72793a0a202020202020202020202020 | 31290a20202020202020206578636570 | C5 | finalize_watchdog | close | close-fault,stream-finalization |
| R045.006 | 237279 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 237239/89/a0718b024236ac756facc9cd92a06f6d495c90cab1cb2930fd4c9b4c80894ce7/1 | 72793a0a202020202020202020202020 | 31290a20202020202020206578636570 | C5 | finalize_watchdog | close | close-fault,stream-finalization |
| R070.001 | 237829 | 72756e74696d6528 | 6530303152756e74696d6528 | 8/0/d74a334bc6d77990d1c5d0140ea878f4b830cabc9494113b36cf1f833e25ba1e | 12/0/c13ef0f03fe369c4c367beaa4b8a56031154607ece29390a3942db1be5e3d82a | 4/0 | 4 | 237821/24/d895b9c1b6e2ee51915eadfdae128ef573c188a047a1be13f9c72222857b0bea/1 | 6f70656e203d20547275650a20202020 | 2273757065727669736f72222c202830 | C6 | supervisor_mode | runtime | no-host-runtime-preflight |
| R060.002 | 237937 | 6f732e67657470696428 | 6530303147657450696428 | 10/0/ac6667ba75cea5a941084b9b116e35943c5bd980adc8c6d2452c8be2f55243d0 | 11/0/2cc17f8a5ac7e6b129d2385da21f110fdb23861034b7f517bd3ef7345bd1b7ba | 1/0 | 3 | 237929/26/30d8b274239a971f91a10b61bc82fe579bbc32a240e32b95135fa7a5c40c4a9c/1 | 757065727669736f725f706964203d20 | 290a20202020202020206e6565642873 | C4 | supervisor_mode | getpid | supervisor-loss,topology |
| R062.002 | 237980 | 6f732e67657473696428 | 6530303147657453696428 | 10/0/b32444b755fcfe3161eb5e0dd3b9e8c4c5f2eab2b86c70d1f5827295bfe948bf | 11/0/9f3a8df4cdae81e24ae7171502a5ae2a282576c4106a52ab07b1aadcbed18eb6 | 1/0 | 4 | 237972/26/d67b6b5a83a40f7fd463165b8daa54f94a97e03b565895194374db4eb408da91/1 | 7065727669736f725f706964203d3d20 | 3029203d3d206f732e67657470677270 | C4 | supervisor_mode | getsid | topology |
| R063.001 | 237996 | 6f732e6765747067727028 | 653030314765745067727028 | 11/0/9bef41b2618723e26e9eb386a4df2d7110177b6aa01b681e8db561169ea2b291 | 12/0/3d6743707cd5e1d2c6f9e5ede9d8715ed376357ee38b478b29a09ff4632a73b0 | 1/0 | 2 | 237988/27/9db715e8128c4e48f946032fca584db4d10e6869ed3f7353892ee65009896594/1 | 6f732e676574736964283029203d3d20 | 292c202273757065727669736f722d73 | C4 | supervisor_mode | getpgrp | topology |
| R020.017 | 238149 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 238125/66/6c410f790a6adc49afbe4fdc2ff65b7cd10f4d273efe1d5cd6049d9d9e5c5ddb/1 | 20202020202020202020202020202020 | 292c0a20202020202020202020202020 | C3 | supervisor_mode | clock | deadline,sticky-deadline |
| R072.001 | 238485 | 537472696374507265666c6967687428 | 65303031537472696374507265666c6967687428 | 16/0/c1c56c3c9d96a3881eab771bbbcd7d039d4ef9cb3b25cd67871afe264459617e | 20/0/bac2fd7ed5dcd3fca6ae9cdbf02312261b7b2e6b1948836be2930675f290d485 | 4/0 | 2 | 238477/32/94dc542deb99f60730d660d1c0db3251c2fffe7c54bf35bcde5eade0c70c8a6b/1 | 20202020707265666c69676874203d20 | 62696e64696e67290a20202020202020 | C6 | supervisor_mode | preflight | no-production-input-access |
| R042.001 | 238676 | 6f732e706970653228 | 65303031506970653228 | 9/0/7b9baff7a3422afc86f09f60d2e5e690a67cf222a2d062eb5e232ca3344f0a28 | 10/0/d5d41a6ded14fa1a7d3230605275b294b4746d92c24bfb332509cb9247b3a6b2 | 1/0 | 4 | 238660/41/5e9b3212bd3c7d17c09a1bdd052e4d315ef7c2cc82217b947d65a2b4197be90b/1 | 642c206c6966655f7772697465203d20 | 6f732e4f5f434c4f45584543290a2020 | C5 | supervisor_mode | pipe | raw-dual-stream,supervisor-loss |
| R042.002 | 238733 | 6f732e706970653228 | 65303031506970653228 | 9/0/7b9baff7a3422afc86f09f60d2e5e690a67cf222a2d062eb5e232ca3344f0a28 | 10/0/d5d41a6ded14fa1a7d3230605275b294b4746d92c24bfb332509cb9247b3a6b2 | 1/0 | 4 | 238717/41/847b505cf2b3a6b0cdef77ad6942669c91ebc936a407a4cd6dd28b3ece9401ee/1 | 2c2072656164795f7772697465203d20 | 6f732e4f5f434c4f45584543290a2020 | C5 | supervisor_mode | pipe | raw-dual-stream,supervisor-loss |
| R071.003 | 239725 | 6e6f726d616c697a655f7369676e616c7328 | 653030314e6f726d616c697a655369676e616c7328 | 18/0/500b47340993fb0bc9147884dc3280f2928981800091161ff11dcfcc697e146c | 21/0/a9a69805990b1370942777b9839b71cd6c2e2bc89257b96f58903ee6398cebc5 | 3/0 | 5 | 239717/34/84c7972b2f661511d31ed2f93f35017827c00c9e6c2026f5472117cbe1ff29f4/1 | 202020202020290a2020202020202020 | 290a202020202020202072656164795f | C6 | supervisor_mode | signal-normalizer | synthetic-signal-state |
| R020.018 | 239799 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 239783/50/0fddbf33f5ef8ae25b4d311c725142a8e44b0321f77392c57b5c7b9f338dbd69/1 | 6464280a202020202020202020202020 | 292c0a20202020202020202020202052 | C3 | supervisor_mode | clock | deadline,sticky-deadline |
| R030.002 | 239914 | 6f732e706f7369785f737061776e28 | 65303031537061776e28 | 15/0/31df13bbd38b806ec10b83328e469066a44abb27722e6e02f3effa919c07c797 | 10/0/76960ee047108b6b6b3000ceb60be573ce5aaa14786d77689b64d04e2950c115 | -5/0 | 2 | 239898/47/5476ad8b3e0d4c111a9f2963a83892197d4cf744e0e2ab90670daa26dbeba5f9/1 | 290a2020202020202020706964203d20 | 0a202020202020202020202020505954 | C4 | supervisor_mode | spawn | handshake,exit,signal,recovery-dispatch |
| R062.003 | 241094 | 6f732e67657473696428 | 6530303147657453696428 | 10/0/b32444b755fcfe3161eb5e0dd3b9e8c4c5f2eab2b86c70d1f5827295bfe948bf | 11/0/9f3a8df4cdae81e24ae7171502a5ae2a282576c4106a52ab07b1aadcbed18eb6 | 1/0 | 4 | 241086/26/5d72a35943ae88d536d44ce4f91a700ebd2f41f7762ec182e0f72ceada2c56d5/1 | 207761746368646f675f736964203d20 | 706964290a2020202020202020726571 | C4 | supervisor_mode | getsid | topology |
| R064.002 | 241190 | 6f732e6765747067696428 | 653030314765745067696428 | 11/0/1d7854664366aee924d81be4e248edf2806cd3a98ae1f33a7b1844ccf0f50903 | 12/0/1553148afe3eb3990ab1ffac71c3cd95319d73783aa8b16d33cf08f06da1e443 | 1/0 | 2 | 241182/27/ac69b660bf6795cc729c7970cb9c1bf60a2436d2a6f2d33579ca017bbc8010e0/1 | 7761746368646f675f70676964203d20 | 706964290a2020202020202020726571 | C4 | supervisor_mode | getpgid | topology |
| R020.019 | 241442 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 241426/50/75a4fd5ee7503afa20298df20326bbac8c48e6de149f649913e8d33a7f819c0f/1 | 6464280a202020202020202020202020 | 292c0a20202020202020202020202041 | C3 | supervisor_mode | clock | deadline,sticky-deadline |
| R020.020 | 242994 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 242970/66/db6126d7d0330296937c2c619371cfeb69a790eb3e99c681aee5db49c8a1fb6e/1 | 20202020202020202020202020202020 | 292c0a20202020202020202020202020 | C3 | supervisor_mode | clock | deadline,sticky-deadline |
| R031.002 | 243538 | 6f732e6b696c6c28 | 653030315369676e616c28 | 8/0/fead1a75480e107f1108b1f250d6979f093eb96413facc5e515cea3b3c2128e5 | 11/0/205ba82f2e120b645fa062100b962a60719bce048bfb44ca341e91e88e33adb5 | 3/0 | 2 | 243530/24/9dc332220bd10b833e26792d88e4850afabaca5c98cabc61fb31161c648bc93b/1 | 20202020202020202020202020202020 | 636c65616e75705f7069642c20736967 | C4 | supervisor_mode | signal | signal-exit,deadline-cleanup |
| R020.021 | 243797 | 74696d652e6d6f6e6f746f6e69635f6e7328 | 65303031436c6f636b4e6f7728 | 18/0/7fa8c5c2020ec40b83a8503479f80ef2adf00541a509eb1e9cfa95be316dfcce | 13/0/4515efab5d7392fa9dff00ed953359b15c8afff6b9c9126939eb82c4a61bc5f1 | -5/0 | 21 | 243773/66/2098bec859836a49d612a756131c96ac9a22c30328155e6c0a541feef31df4bc/1 | 20202020202020202020202020202020 | 292c0a20202020202020202020202020 | C3 | supervisor_mode | clock | deadline,sticky-deadline |
| R045.007 | 244278 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 244206/153/d9fc3adceefb045ea39d710140256e4c6fc4bc77ec76eae61ecc91aa37a084fe/1 | 72793a0a202020202020202020202020 | 31290a20202020202020206578636570 | C5 | supervisor_mode | close | close-fault,stream-finalization |
| R070.002 | 244390 | 72756e74696d6528 | 6530303152756e74696d6528 | 8/0/d74a334bc6d77990d1c5d0140ea878f4b830cabc9494113b36cf1f833e25ba1e | 12/0/c13ef0f03fe369c4c367beaa4b8a56031154607ece29390a3942db1be5e3d82a | 4/0 | 4 | 244382/24/7c533243c6ca5e0cdbb67347cd6f505e661d7431673a73da3bce3c3ae3a185de/1 | 652862696e64696e67293a0a20202020 | 227761746368646f67222c2028302c20 | C6 | watchdog_mode | runtime | no-host-runtime-preflight |
| R061.001 | 244836 | 6f732e6765747070696428 | 653030314765745070696428 | 11/0/56378792a0a4d669db8f2503fb1a5ba4090dfba1cb52faa551991cc4e9c6c6ca | 12/0/4d6cd0a39ea6670faaa7d0e4b8d02f45bb0acedac54b21afd8d90cc6865876a1 | 1/0 | 1 | 244828/27/d2a10b10303c911d28550c6eaae7890c4b1a20d085003eeeae541fcffe8471ff/1 | 20290a20202020202020206e65656428 | 29203d3d2073757065727669736f725f | C4 | watchdog_mode | getppid | supervisor-loss,topology |
| R062.004 | 244902 | 6f732e67657473696428 | 6530303147657453696428 | 10/0/b32444b755fcfe3161eb5e0dd3b9e8c4c5f2eab2b86c70d1f5827295bfe948bf | 11/0/9f3a8df4cdae81e24ae7171502a5ae2a282576c4106a52ab07b1aadcbed18eb6 | 1/0 | 4 | 244894/26/935f5b00c5569dbcc2cf5e338cf7fdff1204178722a994659664bd646c76a684/1 | 22290a20202020202020206e65656428 | 3029203d3d2073757065727669736f72 | C4 | watchdog_mode | getsid | topology |
| R063.002 | 244974 | 6f732e6765747067727028 | 653030314765745067727028 | 11/0/9bef41b2618723e26e9eb386a4df2d7110177b6aa01b681e8db561169ea2b291 | 12/0/3d6743707cd5e1d2c6f9e5ede9d8715ed376357ee38b478b29a09ff4632a73b0 | 1/0 | 2 | 244966/27/7a23d75074789c936b03f39d8d1befb9775c7006018f230867d7414ef2514a0d/1 | 22290a20202020202020206e65656428 | 29203d3d2073757065727669736f725f | C4 | watchdog_mode | getpgrp | topology |
| R060.003 | 245043 | 6f732e67657470696428 | 6530303147657450696428 | 10/0/ac6667ba75cea5a941084b9b116e35943c5bd980adc8c6d2452c8be2f55243d0 | 11/0/2cc17f8a5ac7e6b129d2385da21f110fdb23861034b7f517bd3ef7345bd1b7ba | 1/0 | 3 | 245035/26/5595064e46b3ef132ab1327ffdf6bba97645cf206db668d74a4c67d117637792/1 | 22290a20202020202020206e65656428 | 2920213d2073757065727669736f725f | C4 | watchdog_mode | getpid | supervisor-loss,topology |
| R072.002 | 245152 | 537472696374507265666c6967687428 | 65303031537472696374507265666c6967687428 | 16/0/c1c56c3c9d96a3881eab771bbbcd7d039d4ef9cb3b25cd67871afe264459617e | 20/0/bac2fd7ed5dcd3fca6ae9cdbf02312261b7b2e6b1948836be2930675f290d485 | 4/0 | 2 | 245144/32/8722db2850f21e4a420416f7eec852b65d550c090815b2ae7315b05998e045a1/1 | 20202020202020737472696374203d20 | 62696e64696e67290a20202020202020 | C6 | watchdog_mode | preflight | no-production-input-access |
| R042.003 | 245579 | 6f732e706970653228 | 65303031506970653228 | 9/0/7b9baff7a3422afc86f09f60d2e5e690a67cf222a2d062eb5e232ca3344f0a28 | 10/0/d5d41a6ded14fa1a7d3230605275b294b4746d92c24bfb332509cb9247b3a6b2 | 1/0 | 4 | 245563/41/4487fef0b15c2b70fb18a6bbea73d881380be4345dd7613066f0edf6aa104765/1 | 61642c206f75745f7772697465203d20 | 6f732e4f5f434c4f45584543290a2020 | C5 | watchdog_mode | pipe | raw-dual-stream,supervisor-loss |
| R042.004 | 245632 | 6f732e706970653228 | 65303031506970653228 | 9/0/7b9baff7a3422afc86f09f60d2e5e690a67cf222a2d062eb5e232ca3344f0a28 | 10/0/d5d41a6ded14fa1a7d3230605275b294b4746d92c24bfb332509cb9247b3a6b2 | 1/0 | 4 | 245616/41/5edc3350765a1bb3b2854b62903cf90d6e28cba7679752f681de2b382ea5890e/1 | 61642c206572725f7772697465203d20 | 6f732e4f5f434c4f45584543290a2020 | C5 | watchdog_mode | pipe | raw-dual-stream,supervisor-loss |
| R045.008 | 247762 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 247690/153/8c589afbb960cbaf34d9d5a6956967454286a1296d68944315c06cd07d7070c2/1 | 72793a0a202020202020202020202020 | 31290a20202020202020206578636570 | C5 | watchdog_mode | close | close-fault,stream-finalization |
| R032.001 | 247891 | 6f732e6b696c6c706728 | 6530303147726f757050726f626528 | 10/0/87545abcf01c959319cfd14bc83c23db1c40ec4a589bb263cbcb87e2b0b84871 | 15/0/e9329a731b86b404091f0fccba3a0351d93557f588865c061a12dc1f0e594410 | 5/0 | 1 | 247883/26/b98142d69a9f1b1d05ab2f28b48b42383265b27f324132c5a82ba6ea242eee69/1 | 2020207472793a0a2020202020202020 | 706769642c2030290a20202020657863 | C4 | require_group_absent | group-probe | group-absent,recovery-dispatch |
| R070.003 | 248114 | 72756e74696d6528 | 6530303152756e74696d6528 | 8/0/d74a334bc6d77990d1c5d0140ea878f4b830cabc9494113b36cf1f833e25ba1e | 12/0/c13ef0f03fe369c4c367beaa4b8a56031154607ece29390a3942db1be5e3d82a | 4/0 | 4 | 248106/24/dc62529e0657a8cb8ae757192fdb7b14b9a0faa96b98f69fc5135fd61ad4712a/1 | 6572792d62696e646572220a20202020 | 227265636f766572792d62696e646572 | C6 | recovery_mode | runtime | no-host-runtime-preflight |
| R045.009 | 248616 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 248536/169/3f6565545cd67fdddd62fa2303e05c6ae3b27ccab1880528427d91a92b051d1e/1 | 72793a0a202020202020202020202020 | 31290a20202020202020206578636570 | C5 | recovery_mode | close | close-fault,stream-finalization |
| R045.010 | 249943 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 249887/121/5495011615fa8aea8cc07e6a0e92e3dfb7caa6383e42f53e45950046e36c7135/1 | 72793a0a202020202020202020202020 | 31290a20202020202020206578636570 | C5 | recovery_mode | close | close-fault,stream-finalization |
| R045.011 | 250763 | 6f732e636c6f736528 | 65303031436c6f736528 | 9/0/07011d77a1f1b45eb5c0315ca9a45417051ae278e15c34c9b07926d0925f543e | 10/0/9e98849ee37e63507b66a276ac50077a5ae6eaf22b3c2bf240d30edda6b2b484 | 1/0 | 11 | 250723/89/1c9e5c339b8f7807c10de5cac4a09e1c8ff6d3c7a36a1b4539d6e437c44b0da4/1 | 72793a0a202020202020202020202020 | 31290a20202020202020206578636570 | C5 | recovery_mode | close | close-fault,stream-finalization |
| R071.004 | 250934 | 6e6f726d616c697a655f7369676e616c7328 | 653030314e6f726d616c697a655369676e616c7328 | 18/0/500b47340993fb0bc9147884dc3280f2928981800091161ff11dcfcc697e146c | 21/0/a9a69805990b1370942777b9839b71cd6c2e2bc89257b96f58903ee6398cebc5 | 3/0 | 5 | 250926/34/662e79a373f94e5ed9e4f6a4c3b7d55b05d171204228a3ba2bd73923b9927e17/1 | 73652030290a0a7472793a0a20202020 | 290a202020206e656564286c656e2873 | C6 | <module> | signal-normalizer | synthetic-signal-state |
| R080 | 251399 | 202020206f732e5f65786974283129 | 202020206f732e5f657869742831290a2320453030315f53594e5448455449435f53555045525649534f525f464958545552455f454e440a | 15/0/5919901ff50bfc7f6e80ca79fca3b9c3df5243468ac1ba1049bcce1c529c8fcf | 56/2/4dafb505b268164593b3558d39533a8a44688d6111236ffdbddc16c9ae358ea4 | 41/2 | 10 | 251391/23/fe2d974b31cf87f1e3d7702994f24a3fbc17716c579daa6c7397051122089618/1 | 20202020636c6f73655f616c6c28290a | - | C7 | <module> | terminal-trailer | identity-only |

The ascending interval inequality was checked for all 177 adjacent pairs; no intervals overlap. Gap count 177; minimum 6; maximum 110699; decimal-LF framing bytes 662; LF 177; SHA256 7a3b6d947d2110970283c18fa3dd9f906724a0dd61867a894e9302d13fe6ef16.

## 5. Exact output identity and arithmetic

Sum D_bytes = 9319. Sum D_LF = 235. Therefore I is 260733 bytes and 7074 LF. I SHA256 is 2c86ae692706781860b311c9730b3cf5a3734aae352739b85afc1ba1fedb5c53. Final byte is 10 and there is exactly one terminal LF. I is strict ASCII with CR/NUL/high-byte 0/0/0. I byte census apostrophe/double-quote/dollar/backtick is 0/8674/0/0.

Independent untouched-span and descending-offset constructions must reproduce that identity. Exact interval framing `id<TAB>O<TAB>P_bytes<TAB>Q_bytes<LF>` is 3622 bytes, 178 LF, SHA256 bfa5374a5177d03b734f5d545d2a43e281234b4423798c01e594b1168031b49a.

No placeholder, future exact value, optional family, inferred offset, selected destination, or deferred adapter byte exists.

## 6. Complete declaration and branch skeleton lock

Outside A and C7, B and I each retain exactly 203 def and 13 class declarations. A contributes 48 def lines and 4 class lines, all excluded by C1.

Raw-byte lexical census outside double-quoted strings/comments (B = I outside A/C7): if=528; elif=35; else=114; for=173; while=8; try=102; except=112; finally=9; with=0; match=0; case=0; return=367; raise=2; break=7; continue=16; def=203; class=13; maximum parenthesis/bracket/brace depths=4/2/2.

Exact normalized skeleton rule: remove A/C7; replace each paired C2-C6 interval by byte X; replace double-quoted string and numeric contents by X while retaining delimiters; remove comments/trivia; retain identifiers, keywords, indentation transitions, delimiters and operators. Applying the same record pairing proves byte equality without a Python parser.

Complete declaration order; line SHA256 covers the declaration line without LF.

| ordinal | offset | indent | kind | name | line SHA256 |
|---:|---:|---:|---|---|---|
| 0 | 9248 | 0 | class | Stop | 376152f95270ed6ef0175e9a960b2363bbc439d6a76e92c8073673d29cb21b67 |
| 1 | 9275 | 4 | def | __init__ | aebff7645c827204e03e14d8ebe85689ebae0d8c6ee731bf8977645d62875308 |
| 2 | 9331 | 0 | def | stop | f8531acdbf3684bf0e5dae94bbe5e0a9f40107015f6eb2efa86a5bfd84774ec1 |
| 3 | 9369 | 0 | def | need | ac9886c4378a677460808ff9243bceec4eaaf822cd8fc32a61c27987eb946a6d |
| 4 | 9430 | 0 | def | canonical_binder_context | 632f391c58eaf7cf045ce8750c50bab7337031864fba831b3bd390e2d2cdcfce |
| 5 | 9867 | 0 | def | bit_good | c3d7317531a929b57f4039d9556d6f60db390aef5da408a9b4da8e8b498d1c33 |
| 6 | 9939 | 0 | def | bit_text | e3acd09e96cb6c4afc43476d32867a8d3face5ecc67782034b8151ad1dcc665f |
| 7 | 10021 | 0 | def | snapshot_index_good | d2952abc98dbd1b8a25bbdc95e5974be39c579948b62c033f14952f8f1261627 |
| 8 | 10104 | 0 | def | snapshot_index_text | d5f193adf290b10ee3d58392b029990e81e1156bcd07f53c3f81be912c90209c |
| 9 | 10208 | 0 | def | exact_dict_envelope | c8575eb6afa1024fbf1915486a5b04651233b9bd41a9bd947eaefb75dd8cd38a |
| 10 | 10528 | 0 | def | bounded_index_text | 28ae944124edf971ff4cdbda88e1c31667d102ef2a285af04a27b1b0e45e34c3 |
| 11 | 10676 | 0 | def | sha | 592dbaf6d40d22ff02e2a6a79d88c880abf28bc54e746b86c830877946d0ac66 |
| 12 | 10736 | 0 | def | node_key | 97c283e461a0194d7024b40a44b5fe6a33311c107a6e611e4154550534026a3d |
| 13 | 10958 | 0 | def | node_key_good | bd519e9421cc70475f87171cbe77b9f98ae52f07cb179ce4a406a4a656f10893 |
| 14 | 11189 | 0 | def | ledger_stable_key | e7bb48736f573159810f468ae00c4d45e9e69f887e1d5edaf848cc29b2c1db0e |
| 15 | 11397 | 0 | def | note_close_failure | 48558c1280cdfe7b390e3a15fbed8573493ec0c65fedd4ccd86f6eae58648ca5 |
| 16 | 11793 | 0 | def | track | 7ce01fdf1a2fd2dbcf1b57e2ef76ad68c197b82bd3561238ef42766b248a7946 |
| 17 | 11897 | 0 | def | close_fd | 1216320ef909f6641c603392d5aa992c75be51b1c8d549ec9ed3c73af2228547 |
| 18 | 12123 | 0 | def | close_owned | 4bf9c8b1dd221d8c5a30d2a8b89b9a7a24a6a6c2d7ca7f4d2f34fb3adaab7e11 |
| 19 | 12281 | 0 | def | close_all | 8a14457fa36f3d9bbaeb1f30c8356827e7c168dc332a702f12737cb2eea0d899 |
| 20 | 12419 | 0 | def | pread_exact | 653b851e65fb1ffaeeff04ea102b7d6fb2b8b231b375f83099f2d7871656be60 |
| 21 | 12752 | 0 | def | pread_complete | e9972e67a04fb866c43479617f3ab65beacb611bc908faaf838dbf289f498c4d |
| 22 | 12883 | 0 | def | write_all | dac6c15002df738c170a0e156ca3e3fdfea3f3c10f364573275fc445f6ca17e3 |
| 23 | 13134 | 0 | def | canonical_decimal | d91b6ccdef7efb28796ae12eaddaa13d4bbe43b22004f8d8c88f7a4983204363 |
| 24 | 13346 | 0 | def | canonical_hex | 57c43db1c3ec0bbec37c19333626b6bd9c548ebfcea9b7a5bf0c724dcf03d42a |
| 25 | 13524 | 0 | def | signal_defaults | 579a3671ad1f5922091123a2f6ca758ef6f371e533c214a6800406257cc77446 |
| 26 | 13806 | 0 | def | normalize_signals | dfab8973209e0f41d8eff4ad5690898e469ed1e89df37bb0ea88409b53706e44 |
| 27 | 14186 | 0 | def | fd_census | 42a08290926a67eeaead75bdf1de453bd008f5ebc862fb3f8d0450f2e852ab21 |
| 28 | 14545 | 0 | class | Binding | 4b56d7af4585a5957b6eb3bfd70fd01d2931500f027d860597c2a812ea0b1ecc |
| 29 | 14560 | 4 | def | __init__ | fd11d456ef26678571374ea3a950b88ce16ab044ed7771b4c5da8131662e791e |
| 30 | 16281 | 0 | def | runtime | d984e632934eb3667083232b194f6827cfa80e2df279ef686cbf305baf47aa3d |
| 31 | 18869 | 0 | class | Chain | 9181942c01af1abb65b4f8f24bf3e6318895e22dbfea181e033a91afdf54eb63 |
| 32 | 18882 | 4 | def | __init__ | 3ebba91d7d48e8c1042b665051c93b03a15e9e8c593e0aa27b79b73755dfcd01 |
| 33 | 19310 | 4 | def | leaf | 02f6f11f8992bffa13ff3bbf08bf92316738b75abe33b011f9d69847e661b991 |
| 34 | 19359 | 4 | def | rewalk | 1c7cd388df8dfaa21edc8e26cc8e4ad2462ab2f8dd6ef142011eed170c57152f |
| 35 | 19538 | 4 | def | close | afec3dcdde68b9502ae5d1666d101ddfb9460991cd02d8d376a1faa0dfe0b020 |
| 36 | 19693 | 0 | class | ObservedChain | d3b21fe80b620b3f9777cc98649013063773a0accafe650c3243232e979cbc14 |
| 37 | 19714 | 4 | def | __init__ | 3ebba91d7d48e8c1042b665051c93b03a15e9e8c593e0aa27b79b73755dfcd01 |
| 38 | 20400 | 4 | def | leaf | 02f6f11f8992bffa13ff3bbf08bf92316738b75abe33b011f9d69847e661b991 |
| 39 | 20489 | 4 | def | signature | b03c6ff0950f8d2ff77d078e0d9e83037d873272f1d0cf2272e95e161bdc1a52 |
| 40 | 20547 | 4 | def | close | afec3dcdde68b9502ae5d1666d101ddfb9460991cd02d8d376a1faa0dfe0b020 |
| 41 | 20725 | 0 | class | Record | dbe8b84f285823c1060a4a26722a5b99cebe9ea46c7ade965c219ad90ab19926 |
| 42 | 20739 | 4 | def | __init__ | bed1493d3806266e0d7eb82a15e2a3c62c2ce02c02d195a8e7b850d5c534c11d |
| 43 | 20927 | 4 | def | verify | 43aeb67bee45181961959acf7382862bd42d277b697f2ef68b52528ebc0411ab |
| 44 | 21871 | 4 | def | close | afec3dcdde68b9502ae5d1666d101ddfb9460991cd02d8d376a1faa0dfe0b020 |
| 45 | 21968 | 0 | def | open_fixed | 48cc4b7bc7ddf4f35a28116044171e1bf744a7e95b9d154b606d0d2922ee16e7 |
| 46 | 22814 | 0 | def | open_actor_self | 8fae7dc12dad3bf7c3c0b1f82cf1212b7102d96db7b03d5ddedc5bd54dafbbb5 |
| 47 | 23777 | 0 | def | open_tool | 638b152315345c4bb7a25e7754f326afb7292bbdb49e23432160ceb877e866eb |
| 48 | 24398 | 0 | def | extract_between | 53f37627ceaed7a5ed5bc31de21e07881b4d7060a7b0f3722a6fe42ed809aa34 |
| 49 | 24641 | 0 | def | extract_payload | 8dfeb0cda76014eeefcfeca4b0bce4084ca33366cc2fc3f709dd3e329f171362 |
| 50 | 25587 | 0 | def | extract_self | 915436a2d407afe3d0c8627eb6284146a64b08737639038f3351e551d00100c1 |
| 51 | 26114 | 0 | def | extract_launcher | 179e3bb7fddf87dcf1bd429363485594684c586c6170a6097651bfcfcc03dacb |
| 52 | 26899 | 0 | def | build_inner | 704e18513b57e13543146a2f9dca9882570dfc991277106f611c73e3efea9fb2 |
| 53 | 27649 | 0 | class | StatusPrefixRecord | 7dce2e075ebd9933e96c588d7865d81626887f477b2bae8ce07c6d15a0efd240 |
| 54 | 27675 | 4 | def | __init__ | 521ca8d4aafd0107bd1b3c44c4589a47e42121f6a0ed770337f8e73afbaedad9 |
| 55 | 28255 | 4 | def | check_metadata | 994d628a6d1d636339db85655688f1de365f86d5c98af3beafe275998d6fb757 |
| 56 | 28695 | 4 | def | check_data | 0d48b2e50937ed6479a8cac4971f866078fa532525f46159dad90b18b789094a |
| 57 | 29269 | 4 | def | verify | 43aeb67bee45181961959acf7382862bd42d277b697f2ef68b52528ebc0411ab |
| 58 | 30536 | 4 | def | close | afec3dcdde68b9502ae5d1666d101ddfb9460991cd02d8d376a1faa0dfe0b020 |
| 59 | 30660 | 0 | class | ToolLink | 8dd9a3236e54ed28375303aaccdd325d3c87ee85f039569662ba0fb66b8b7ec1 |
| 60 | 30676 | 4 | def | __init__ | 77a1fabc48fe6d637766a9260e8172c6887fe34170dac1eb7fa1a9bc3fcb5662 |
| 61 | 30912 | 4 | def | verify | 43aeb67bee45181961959acf7382862bd42d277b697f2ef68b52528ebc0411ab |
| 62 | 31564 | 0 | class | ControlInputs | 394151ae9eb65fb907b06d8d6de387d88e2a9b97dff2ff973ff4998da7f96827 |
| 63 | 31585 | 4 | def | __init__ | 521ca8d4aafd0107bd1b3c44c4589a47e42121f6a0ed770337f8e73afbaedad9 |
| 64 | 32717 | 4 | def | verify | 43aeb67bee45181961959acf7382862bd42d277b697f2ef68b52528ebc0411ab |
| 65 | 33168 | 4 | def | verify_complete | 53ca5be8e0c46c5c8024bc829022a185e8e8316324a164b9924655da2238059b |
| 66 | 34052 | 4 | def | close | afec3dcdde68b9502ae5d1666d101ddfb9460991cd02d8d376a1faa0dfe0b020 |
| 67 | 34444 | 0 | class | StrictPreflight | dad47e70b8366a100cc2de91953291cc77b57b0903a047dddad964f414a59ee4 |
| 68 | 34467 | 4 | def | __init__ | 521ca8d4aafd0107bd1b3c44c4589a47e42121f6a0ed770337f8e73afbaedad9 |
| 69 | 35140 | 4 | def | verify | 43aeb67bee45181961959acf7382862bd42d277b697f2ef68b52528ebc0411ab |
| 70 | 35384 | 4 | def | close | afec3dcdde68b9502ae5d1666d101ddfb9460991cd02d8d376a1faa0dfe0b020 |
| 71 | 35496 | 0 | def | type_name | a7b73391ea8c50757c34e07054471566c72a2136ef0b854294fc7b880d670921 |
| 72 | 35898 | 0 | def | empty_observation | 84a428619e48f1df556b86e7ee36fbec052d7973efc23cf8ef2aed526ef2b8f3 |
| 73 | 37604 | 0 | def | fill_metadata | 86fc001d55c15fe409897b428e32ff8251ecde31d3f160f6d1bf08fa2a84865e |
| 74 | 38078 | 0 | def | finalize_observation_path | a2042ddaeb51b88e405aec42cbe48d8cc10625372526513aeaef390b2e7fb70c |
| 75 | 40134 | 0 | def | close_observation | e9a579d0d9631f1d39a360ca331798192a8a6e60ef3ea25236892b9f03c57c42 |
| 76 | 40327 | 0 | def | observation_signature | f634f54e9c4ce91f15ebe34f766098bb4c74145ce3b58b3ce53dbd3609430031 |
| 77 | 41973 | 0 | def | observation_line | d6d23257c027b58803c7ff8f913867897c9387063c4f62cba5ed09a7ba52d501 |
| 78 | 42193 | 4 | def | rendered_bit | 46dce37128599ca0eca810c4a5f07756898907021ba7dae34b38755d120663d8 |
| 79 | 45376 | 0 | def | chain_component_line | db43fd4a71ec44e0bbdd5124da13e00ecafae426f0e09f82db53b9728d1565eb |
| 80 | 46795 | 0 | def | capture_regular_content | b40c8522302a5afd287b31e95c87d5fb310dac714779a67d48ccea4e45e0a35e |
| 81 | 48169 | 0 | def | observe_source | 5c63e0cd15e9c18d0a34ba5b8ec0d972e9df71dc8ca7901e6469d0503ead3ca9 |
| 82 | 50599 | 0 | def | candidate_expected | b622f6bd2d8e058ba412a368b2baf56953e052ed652df84a5bcf3c24dd288c54 |
| 83 | 50938 | 0 | def | observe_candidate | 7bc59b9d1db4f4a40d6816f114dd4f7a06e89fb31bef397bf2a8e93dcd5f177b |
| 84 | 53625 | 0 | def | begin_evidence | 5e68bacc0bd58d76cc7eb019a742f20fe36b3875679bb7e523dfa2937ef54eac |
| 85 | 55952 | 0 | def | fill_final_metadata | 1ed5f0a999bc6e1e69962c2005409d9c423878d5dd38003aec689b55df15502d |
| 86 | 56498 | 0 | def | finish_evidence | 5bbba407b560bc41af83e3f6d52858891623ea2b6021d3321fa1b28a5232bf9d |
| 87 | 64805 | 0 | def | close_evidence | d4b5ee2c7e640c17a719b773283b6cf548623481bb23589a2d3ca3f1e5eda42e |
| 88 | 65075 | 0 | def | new_inventory | bd935ba3da6c72a0b36b45f3f2aad1fd4d762dc1c441a05553f00d78cb2eaf5a |
| 89 | 65451 | 0 | def | add_inventory_reason | 53121286881a2f57f0afd6e45ec16e43a22badbbdb63af375d80c2a2ce265401 |
| 90 | 65724 | 0 | def | set_inventory_overflow | a7c9da654ad845524946d13c9bcce77020367d30456b166d105f36dda869f0e2 |
| 91 | 66179 | 0 | def | inventory_reason_text | 4dd3b4678d8dcb0adda620ad587152eab778b3e6a2469aee1ebbe7bd16e12f0c |
| 92 | 66357 | 0 | def | inventory_fresh | 899ec438fbcd2c957296607daa8a00058e58ca9d39b39b08c6bd81e198283335 |
| 93 | 69227 | 0 | def | unavailable_candidate | d7d541c1ba44c6095b354953ab1c8c65928ac78e3cde07c25fc059a498869e4b |
| 94 | 69432 | 0 | def | unavailable_snapshot | 47d8c55530a2d4c8057672522e05593b7b6474c63c662d528dbb13eacded7e52 |
| 95 | 69750 | 0 | def | take_snapshot | 89f0c34bcbffe5ac47192f4ea23d1f350273ef4b223ab75a0e839cce6881cb31 |
| 96 | 70226 | 0 | def | close_snapshot | f9b20561875185e379b8a83ab4c881c8b8af591d3dd461545428a5fe527a2d4c |
| 97 | 70500 | 0 | def | snapshot_signature | 906ae9e619e0584c18201ccb3f6329bd3ab92098822886b57c823de5f87c2b5d |
| 98 | 71079 | 0 | def | relation_lists | 5e633af99f1655d4239facc18d68bcd273aaef0fa9df3c3c49a9a1697f0b6bf9 |
| 99 | 72180 | 0 | def | candidate_is_valid | 4318e9c822d96985bfd140ea9ac54cab2af645d94b8bc51c4cab6a537174fb16 |
| 100 | 72577 | 0 | def | snapshot_anomalies | c5686d1d922e0946c621fef001e646d2f931d8e41595267a9816e8b25b583493 |
| 101 | 74435 | 0 | def | new_audit_schema | 216582ffd4c9850d8ac2fee824318b280e6c0fd54415a3f31abcf06454b0b495 |
| 102 | 76213 | 0 | def | schema_error | e1bfea99c2f884eac71a12a878e7da3dc0db3f6305fe896b61604aa764f6777c |
| 103 | 76631 | 0 | class | FailureBinderInputs | f44d4e0d1e37d5cd337eba6b4fffba729a80b241e24fd5a37b69fae415f66e90 |
| 104 | 76658 | 4 | def | __init__ | 1e786d5797df0f866e48f9ebaab310c977afd945eaf6cc75d4d5cc9663af516c |
| 105 | 77651 | 4 | def | verify_after | 91ca8d999f83d155bca2b8ac7d50bae1792bc00be33cd0d975a18854da23ff34 |
| 106 | 79167 | 4 | def | close | afec3dcdde68b9502ae5d1666d101ddfb9460991cd02d8d376a1faa0dfe0b020 |
| 107 | 80344 | 0 | class | UnavailableBinderInputs | 352542faa3397775683755bfd1da4643e53133cd049f8cc49c262295ec89d2ab |
| 108 | 80375 | 4 | def | __init__ | 1c82f5882fcb2a55651d803a9eddadb9a83185c69011459c0bc67ae52ffe4305 |
| 109 | 80514 | 4 | def | verify_after | 91ca8d999f83d155bca2b8ac7d50bae1792bc00be33cd0d975a18854da23ff34 |
| 110 | 80682 | 4 | def | close | afec3dcdde68b9502ae5d1666d101ddfb9460991cd02d8d376a1faa0dfe0b020 |
| 111 | 80731 | 0 | def | inventory_line | 075774a440dcc4c9259d8b6c2ed3997301b3cbeb692949075659d010626835f3 |
| 112 | 81829 | 0 | def | relation_line | 4f817a354dc1e2ac52553dc9766c559e7c9f96c4c45d20b05bc25c3d1e03f92c |
| 113 | 82459 | 0 | def | classify_phase | 959eb97c3a22258e8a2eab6107e43dc156b9f023cdb402595117860968732a9b |
| 114 | 85177 | 0 | def | candidate_evidence_dependency_good | b41bba69d8d2873b2757e6cb455ba86d6ce4b5c719641fbeebea600d71c77f7e |
| 115 | 85605 | 0 | def | derived_cache_values | 626e9d1b4adfa4ea8249874fa2c6ae1428987abfe5ce1b0125f7639322b1051b |
| 116 | 86482 | 0 | def | derive_schema | 2581da7129d1247dc98a43a73da91b5cc55f50400cd24ced948863f96942ad35 |
| 117 | 89618 | 0 | def | observation_errors_good | eee67acdcf9b42a94bb05b1307e20957ffd3ba1780937ad98f81bebc3f64015d |
| 118 | 90147 | 0 | def | project_observation_errors | c2e159a09910e46cfc98f6d4e4aba74323669b049dd25f2256e391e5340ff85e |
| 119 | 91667 | 0 | def | add_observation_error | a8c56068621af35ac1a32305c7221be360e1acd748c588df8f448aecb1893d82 |
| 120 | 92123 | 0 | def | observation_error_text | 032be50fdfa1c90881f0ad0750253839a365524dd67f02f7eb3eaa3f0195e328 |
| 121 | 93467 | 0 | def | safe_token | 28dfeab656f73c30d2073776512f1478269e3292f559e57c49113c6c3ca75269 |
| 122 | 93756 | 0 | def | normalize_schema_error | b13b6113ed549c861fe052dcd81cb021ec07a1b7a0068430f361f551e095d267 |
| 123 | 93914 | 0 | def | canonical_u64_text | 71ac3fe5621fd72c8f6abe0d788065eb2cbe4d92cd206beba173639f22129d4d |
| 124 | 94323 | 0 | def | canonical_mode_text | 84f1a889fed4fcda514e6cf6be494acbc7fecab43349ba9a2af6149ae391d5f6 |
| 125 | 94579 | 0 | def | canonical_hash_text | 30a12546f2df8331ded4c8f6e012a158dc5307b7cda372dddfadadf6f4bb08c7 |
| 126 | 94868 | 0 | def | canonical_inventory_frame | 00ddb3933fd45e51c0ab5b47a99e00b14761dfae4eef4c45cdc664a376284745 |
| 127 | 95043 | 0 | def | basename_good | 7c5d9257a690565f6214c3569c9fea609b80dc530c5783bb55f0f8bbd2af1671 |
| 128 | 95270 | 0 | def | chain_signature_good | 9d2b069aced258af84b8e88c7f73a0b404d307b2abc4cd1ac725abb9f628fd01 |
| 129 | 95471 | 0 | def | key_matches_scalars | 31503834fe181dd9f84f2689aefcb31b1e60ab9b0389b737c43220cfe9496f24 |
| 130 | 96614 | 0 | def | stable_claim_good | 55bd7cc6382dda27d30e1f883729d06a92df79f8ab653f9d6dc36c80574b05b2 |
| 131 | 97166 | 0 | def | exact_claim_good | d44f66c2bdb5c8236f8f180cfd7a75359cac6ae1fe769707decb9637a1b56d9e |
| 132 | 101393 | 0 | def | observation_semantics_good | 21f0896663fb8b2d4520488374ac98ad7d02e8a60815130bc0b3efe476a50c71 |
| 133 | 103701 | 0 | def | observation_shape_good | de9c3b68ba550ff487a5d35f31c98a2a364117b8cd87ff64e459546bbf26cc9e |
| 134 | 111530 | 0 | def | inventory_shape_good | 7e5291be4a89a5373563b1bfa391dba028c6c3dd13171cc6544053febc56451c |
| 135 | 113227 | 0 | def | bounded_bytes_tuple | 837d508d038dc3715ca7af5caf21068c9376c232e2a7239a92daed7088ee5554 |
| 136 | 113519 | 0 | def | bounded_token_tuple | b973df9d372347a187fb901c05da932269c9a8fe6ba84f356d358493b221533f |
| 137 | 113763 | 0 | def | construct_global_anomalies | 4d0390371c6bb1ad807147be89189b5c2cc30ac9889a00b186091028f9a2d0b4 |
| 138 | 116003 | 0 | def | validate_schema_shape | 65e303e39ba25a084af1ef589540c51f0ec28021a6f5888d669411ff695cca6f |
| 139 | 123580 | 0 | def | schema_outer_layout_good | 0b4c4e12be6e735c1322789d657aec12dce987bb1fc91b4f05dffc7ca52a6388 |
| 140 | 125760 | 0 | def | observation_metadata_names | eb8c14e73c3cf27680e8f124871bdd6500fa2f3a4c44cd0929e5e8421beac0ad |
| 141 | 126018 | 0 | def | clear_observation_metadata | 3837d499daad91ea2d7c291b5a7cb279382d42e9245e0c3d75fe076623eaac8d |
| 142 | 126231 | 0 | def | project_observation_metadata | aae2487eb3051881f6bb98d82e0c41932f5a9185803dbb5e81512a67a9b06b83 |
| 143 | 129608 | 0 | def | project_chain_signature | fc7e99fbcf5932005e154daa41b7d6c041418f23965e365285488b3eed1f5500 |
| 144 | 129896 | 0 | def | sanitize_observation | ff12fbf8b0aaa7b48a33d1873b74283be571b89dc54765b2e8cab61e3eafe347 |
| 145 | 142802 | 0 | def | project_inventory | d644de1d26a9c2ab2d2f0bb79f371e034093f10b28f0367b7d949597cd9b0b79 |
| 146 | 147934 | 0 | def | sanitize_schema | c035c82483a2d8d2ac1bbc30e0adc6c9e1e4988190b0840c18f6beee2b483b1d |
| 147 | 154015 | 0 | def | serialize_schema | f4263d9027b000ee3bc02d54cd14fe69b194170ae653547f220e47dde5e8cb26 |
| 148 | 161868 | 0 | def | binder_observe | 5f5016612e3907d9f18b8a96cc8e5b0d92760bf4fe8dd2f90ab66fea5c5de09c |
| 149 | 167477 | 0 | def | binder_provenance | 8a6545bc282147bad4ead193371d9c55ac38306c1d7ccf6050d3e5c9d2eeb39f |
| 150 | 167987 | 0 | def | rendered_binder_context_good | 5730475206492e42e3ac09d4551eafae5a829ee2d38687760cd524ac2f76b247 |
| 151 | 168720 | 0 | def | binder_header | 80d5e1b90a54d0323c705dd5a6f27abda0a25fc376da7474e01f63bf456cf395 |
| 152 | 170546 | 0 | def | schema_layout_failure | c00c26affbbd6d7fc5f53ca875ea1d7f97b2a6a7286df630ea68c0fd96583091 |
| 153 | 171441 | 0 | def | render_binder | 5f4803d27479da9542dd087a6e11cea66f3c48d29083dd350c22f5295efbfebc |
| 154 | 173745 | 0 | def | checked_u64_add | aee064823ec020829eef6da758f7062ca9acf0a9b1e75da26e13bb93e4d98d8a |
| 155 | 173979 | 0 | class | WaitObservation | 34debe4f3004ba2287d514180d084d8e9c4d14165668aca21a4cd2f61b9bf1bb |
| 156 | 174029 | 4 | def | __new__ | c3bc0a9f8618b5c09e20a805ae5e7ca7ab4216d53f5d03db305937627f344e94 |
| 157 | 177864 | 0 | def | known_unreaped_wait_good | 3741dbe3a5dc9ee141a904cb7b50a4e1846e264986b452d11f519cc9ecb81b66 |
| 158 | 178990 | 0 | def | guarded_wait_once | 1dc8f0a8ca25167cb6a814b753ba37faead2d37092490ae57355436f3e55b4b8 |
| 159 | 180551 | 0 | def | wait_deadline | 2fb9a669b95dee206e79e1759893c213404632c209bfb52955a4df4c3478b7a0 |
| 160 | 181063 | 0 | def | wait_blocking | 8c6f1da865f0d93d955afaeaf3a91c2d41406e655fe14cc04447888cfe577fe8 |
| 161 | 181292 | 0 | def | remaining_poll_ms | c68b4868cb2e72928d901462c622c1edcbe98288d9c24a56af8ec3198dbdffa5 |
| 162 | 181508 | 0 | def | require_before | f1fe401444d5fd8a2e73657847e23b6b54fd366ff0c23cbeb26c8d8de426517a |
| 163 | 181605 | 0 | def | read_token_eof | b2e409093af4942b01d38e41a13a684a3ca44764b486e3148d8faad11238734b |
| 164 | 182672 | 0 | def | wait_start | 88472c997d252ae83a07677edc6122ab680b9398bfd6fc62eddf90e5eeaf4217 |
| 165 | 183341 | 0 | def | prove_payload_input_live | 3a559f8f1fe8c1e3905a9308530bdbbc319865c37c8811015d8bb72fcd78a45f |
| 166 | 183582 | 0 | def | probe_lifeline | 68779ac261abc6e11c0b20758e9c0e91bf2cc985421cf848f19a4e835cc5afd9 |
| 167 | 183811 | 0 | def | begin_line | 8b6c1c2775879d09b3b78058d09b80f7353b8db2dbe302797f9596637ebdbc6b |
| 168 | 185914 | 0 | class | EOFObservation | 63de9a295c1d313fc90cc5146daae184c9d7bdbaccd48741c574b5c8e56a255e |
| 169 | 185963 | 4 | def | __new__ | ec99baa05f24ddf5fc52a5d2fea57d0c892f1a5fe179f9e7b43e9f35afcf8e0d |
| 170 | 186999 | 0 | def | empty_capture | 87ded5cfd945796ec959446bd56085ee1458c3e9af3da32f6bc087c5c52d30b9 |
| 171 | 188968 | 0 | def | recovery_capture | 5288f87cbf42a6ff147c35b807ac4d7d519ab4e9138678c75c507757a659363d |
| 172 | 190586 | 0 | def | mark_capture_error | 58395ee07a302863cf70b0d483002f7db73200fa97560436b939738ddda329a3 |
| 173 | 190850 | 0 | def | capture_errors_text | bbe09c26480813467148e0a15f45915bc106a0d4849adf9c18bdfba913f302bc |
| 174 | 191036 | 0 | def | capture_error_any | 89dd801da524bb0cce50887e18457e919e4b8c12823efe59c07d454226d074b4 |
| 175 | 191176 | 0 | def | u64_accumulate | 66a18feb93a50fd3cb319093dfd9afdec2130d2798ff20ee41d8a9898c00614c |
| 176 | 191447 | 0 | def | capture_piece | 857bcd3c8bc7a8304b581ea675312fe24ca995f608cdef0214e401024564c4e6 |
| 177 | 191886 | 0 | def | close_stream | a07a31d85ed651e3eeeadbb54dc86494ef741b81a4224b263bf1f227022fdd82 |
| 178 | 192343 | 0 | def | latch_capture_deadline | 20027707d09c3ee903dae99f4cfc33454ff3ef845c10d13e23781b0437296b5d |
| 179 | 192470 | 0 | def | capture_guard | 0420a33054f92adbea46544facd920cae4f405e76f01ba48656b98193e8db8dd |
| 180 | 192664 | 0 | def | capture_poll_ms | a1c7e69490385fec9c1c887dccbc4f540f9b8335c382d25c3afa082e56587c3a |
| 181 | 192992 | 0 | def | reduce_wait_observation | b5f8b1347d7897b94423f07e9ef3be6495bc6f80d173c8df11e4f1d6d2459954 |
| 182 | 194900 | 0 | def | capture_wait_once | b686d4582e7b8de647acc8e39fc4a7abed8f3d0da2c3a0c3ef61f7fa6e56ec60 |
| 183 | 195084 | 0 | def | capture_read_once | 9e902a8a591aec0b078ab0b7e03a3982ca95960caf74d5b373399c0022e51910 |
| 184 | 196487 | 0 | def | capture_lifeline_once | f9def61329645ad88057213dd4828911d78518ff654c3cad0a52c523c63cffd1 |
| 185 | 197442 | 0 | def | classify_capture_wait | ee94d315b9491ccf58ba58f598744a0706009855fd7e3d0850599f51cc7cb6d0 |
| 186 | 197911 | 0 | def | eof_observation_good | 7fd1b86b1ee6a99520053bf5e43db056a2a77a55522b093e5fd2762aaf6ab40c |
| 187 | 198714 | 0 | def | capture_complete_good | 7c6f47e9099d48d87ef8bf1346705e96456ed6bfc9dfcdf4684a54181cd8fec4 |
| 188 | 200060 | 0 | def | wait_ownership_errors_clear | 9a95babdc835839c136997092b020bf2d5fa8dca2462194916728217e9c4b13b |
| 189 | 200505 | 0 | def | enter_kill_reap | c002aa38113f091101d5f50da40521f9cc2231e6155b1f8bcadbabc4d2c927a2 |
| 190 | 201958 | 0 | def | capture_payload | 79ab6214cff1f5d72fb72ebf58a12bad9a052d33ce496ee25ede634ba83c6f38 |
| 191 | 206387 | 0 | def | optional_u64_text | 0a0ecbac8f62953bcdd2fc3a6585c58e483e3908cef50bad5e530665cb401120 |
| 192 | 206621 | 0 | def | result_bit_text | 33b3cf4b0ef71730f7e56f34f9c7a567e7a120fdea7562845ecb93711156567f |
| 193 | 206820 | 0 | def | result_u64_text | 0d07140b6344463d3ebda1105fe723e3af7ecaddaec37ab34408e0ec3441ca94 |
| 194 | 207044 | 0 | def | hash_field | 543257144b884b4ed2af4ef299a81e73b135dcd7e7d1d01f1df202739f890787 |
| 195 | 207133 | 0 | def | stored_hex | 9083315d88b6fc591fe38095ccb07a5e3942442fa5f8c28c7896087997ba9a01 |
| 196 | 207292 | 0 | def | stored_bytes | 6b5d443984e31c50781f5506b127a3aa6e27fde66b882d1ae5163ea2c15a8286 |
| 197 | 207424 | 0 | def | hex_kind | 0bffcedbc96f2b45b1cc98b21dcd2bb072b2d73b0cea31cb3d19ba04cbd055a2 |
| 198 | 207580 | 0 | def | wait_value | 28ed74dc05aa0844da0c72bb8857d6247818f019ee48d8f70055fbcd7b813f28 |
| 199 | 208200 | 0 | def | eof_value | e86e560737ef099c1d9744a7fd4fc422e40141180df8344b16c932a83ccca255 |
| 200 | 208790 | 0 | def | u64_int_good | d277821a68727e5e669269a86232e1fbd837b79e74003975215c790ba9effa38 |
| 201 | 208875 | 0 | def | hash_object_good | 93fb1a6fa2ce4a6080e4ccb692c88f1bdff7bf53be3d94c10111047121f16c52 |
| 202 | 209035 | 0 | def | validate_result_capture | e33e8fab4f1c90848d84cf1d2f099a163b7dd539e42d3713bdaa2da91c8615de |
| 203 | 217184 | 0 | def | result_layout_failure | 0c0495e6777f6c9706b5bef4d0b86d236dbb6616773d0bd49f2bc2672583fc74 |
| 204 | 217996 | 0 | def | result_line | 96e2bb1c1bef2c7a65bcc0626e944eaec3fd7a2605428205598152252ab36965 |
| 205 | 229149 | 0 | def | emit_and_exit | 6c5d5be2c91272fba7151214c848f1917bcc10ec6a7eeaf54a912203de145ff9 |
| 206 | 229443 | 0 | def | binding_argv_bytes | ce0c8bc0c1685f9b555eb6333845c8b3b8c4e5f62e3daacabe5ab298d981ef47 |
| 207 | 229541 | 0 | def | spawn_payload | 6d9e303484176e87f610c0ce5f964cc16aebe24262c459e6e17d8b6ebd8a498c |
| 208 | 230723 | 0 | def | payload_topology | 6bd29089f2c829a9b0daf6476a9ca7fa08ad018da48effd1e09b1bbebd2a1b1d |
| 209 | 231759 | 0 | def | payload_writer_close | e44f04d3e1457748916615499e09f0f2cf37c23e4ce8b6d3d28c21ef982b912c |
| 210 | 232287 | 0 | def | governed_payload_abort | 5f7c623e64caaf2e100dd77d75a0e810f4475684c67d4ef4351161804efa65e4 |
| 211 | 233309 | 0 | def | finalize_watchdog | afa993afd6921b04b8b35ccd40a5bb90fdfa95ab9394eacb8bc592cf81b064c2 |
| 212 | 237749 | 0 | def | supervisor_mode | ffec971fdf880186ce5f61e1087cf61f05b8ffea76f1e177c5ff3a347f336b04 |
| 213 | 244358 | 0 | def | watchdog_mode | fd62541dc9d93ae255e4e9d10e5566e34318cc051b6d41fe44f02486202e7912 |
| 214 | 247842 | 0 | def | require_group_absent | 218f83a15b02587392b5fbb8ae1ffcae3de7d1ba151f51f1983d442027c1eb2d |
| 215 | 248050 | 0 | def | recovery_mode | 2dd44f209b39738b65c980cd5798bcf9438c12d9b16cce047a3eab4ec7f59f58 |

## 7. Concrete lifecycle/callsite map

Every redirected boundary is one registry row. This owner aggregation is the complete C3-C6 map; C2 is locator-only, C1 adapter-only, C7 identity-only.

| owner | callsite count | record ids | families | scenario seams |
|---|---:|---|---|---|
| <module> | 4 | R050.011,R052.017,R052.018,R071.004 | R050,R052,R071 | synthetic-only-file-state,synthetic-signal-state |
| __init__ | 13 | R050.001,R052.002,R050.002,R052.003,R050.003,R052.004,R050.004,R052.005,R052.006,R051.006,R050.009,R052.013,R051.009 | R050,R051,R052 | synthetic-only-file-state |
| begin_evidence | 5 | R051.015,R050.014,R052.021,R050.015,R052.022 | R050,R051,R052 | synthetic-only-file-state |
| begin_line | 1 | R060.001 | R060 | supervisor-loss,topology |
| capture_guard | 1 | R020.007 | R020 | deadline,sticky-deadline |
| capture_lifeline_once | 4 | R040.007,R020.012,R020.013,R020.014 | R020,R040 | deadline,sticky-deadline,handshake,raw-dual-stream,overflow,supervisor-loss |
| capture_payload | 4 | R044.006,R044.007,R044.008,R043.003 | R043,R044 | deadline,raw-dual-stream,supervisor-loss,handshake,raw-dual-stream |
| capture_poll_ms | 1 | R020.008 | R020 | deadline,sticky-deadline |
| capture_read_once | 4 | R040.006,R020.009,R020.010,R020.011 | R020,R040 | deadline,sticky-deadline,handshake,raw-dual-stream,overflow,supervisor-loss |
| close_fd | 1 | R045.001 | R045 | close-fault,stream-finalization |
| close_owned | 1 | R045.002 | R045 | close-fault,stream-finalization |
| emit_and_exit | 2 | R045.003,R045.004 | R045 | close-fault,stream-finalization |
| enter_kill_reap | 2 | R020.015,R031.001 | R020,R031 | deadline,sticky-deadline,signal-exit,deadline-cleanup |
| finalize_observation_path | 1 | R051.012 | R051 | synthetic-only-file-state |
| finalize_watchdog | 3 | R073,R045.005,R045.006 | R045,R073 | close-fault,stream-finalization,wrong-context,opposite-context |
| finish_evidence | 8 | R052.023,R052.024,R051.016,R050.016,R052.025,R050.017,R052.026,R051.017 | R050,R051,R052 | synthetic-only-file-state |
| guarded_wait_once | 5 | R020.001,R033.001,R020.002,R020.003,R020.004 | R020,R033 | deadline,sticky-deadline,exit,signal,deadline |
| inventory_fresh | 4 | R050.018,R052.027,R055.001,R052.028 | R050,R052,R055 | synthetic-only-file-state,synthetic-only-inventory |
| observe_candidate | 3 | R051.014,R050.013,R052.020 | R050,R051,R052 | synthetic-only-file-state |
| observe_source | 3 | R051.013,R050.012,R052.019 | R050,R051,R052 | synthetic-only-file-state |
| open_actor_self | 3 | R051.004,R050.007,R052.011 | R050,R051,R052 | synthetic-only-file-state |
| open_fixed | 3 | R051.003,R050.006,R052.010 | R050,R051,R052 | synthetic-only-file-state |
| open_tool | 3 | R051.005,R050.008,R052.012 | R050,R051,R052 | synthetic-only-file-state |
| payload_topology | 2 | R064.001,R062.001 | R062,R064 | topology |
| pread_complete | 1 | R053.002 | R053 | report-truncation,synthetic-input |
| pread_exact | 1 | R053.001 | R053 | report-truncation,synthetic-input |
| probe_lifeline | 2 | R044.005,R040.005 | R040,R044 | handshake,raw-dual-stream,handshake,raw-dual-stream,overflow,supervisor-loss |
| prove_payload_input_live | 3 | R044.003,R040.004,R044.004 | R040,R044 | handshake,raw-dual-stream,handshake,raw-dual-stream,overflow,supervisor-loss |
| read_token_eof | 3 | R044.001,R043.001,R040.001 | R040,R043,R044 | deadline,raw-dual-stream,supervisor-loss,handshake,raw-dual-stream,handshake,raw-dual-stream,overflow,supervisor-loss |
| recovery_mode | 4 | R070.003,R045.009,R045.010,R045.011 | R045,R070 | close-fault,stream-finalization,no-host-runtime-preflight |
| remaining_poll_ms | 1 | R020.005 | R020 | deadline,sticky-deadline |
| require_before | 1 | R020.006 | R020 | deadline,sticky-deadline |
| require_group_absent | 1 | R032.001 | R032 | group-absent,recovery-dispatch |
| runtime | 2 | R071.001,R052.001 | R052,R071 | synthetic-only-file-state,synthetic-signal-state |
| spawn_payload | 3 | R071.002,R020.016,R030.001 | R020,R030,R071 | deadline,sticky-deadline,handshake,exit,signal,recovery-dispatch,synthetic-signal-state |
| supervisor_mode | 18 | R070.001,R060.002,R062.002,R063.001,R020.017,R072.001,R042.001,R042.002,R071.003,R020.018,R030.002,R062.003,R064.002,R020.019,R020.020,R031.002,R020.021,R045.007 | R020,R030,R031,R042,R045,R060,R062,R063,R064,R070,R071,R072 | close-fault,stream-finalization,deadline,sticky-deadline,handshake,exit,signal,recovery-dispatch,no-host-runtime-preflight,no-production-input-access,raw-dual-stream,supervisor-loss,signal-exit,deadline-cleanup,supervisor-loss,topology,synthetic-signal-state,topology |
| verify | 15 | R052.007,R051.001,R050.005,R052.008,R052.009,R051.002,R052.014,R051.007,R050.010,R052.015,R052.016,R051.008,R051.010,R054.001,R051.011 | R050,R051,R052,R054 | synthetic-only-file-state,synthetic-only-link-state |
| wait_blocking | 1 | R033.002 | R033 | exit,signal,deadline |
| wait_deadline | 1 | R021.001 | R021 | deadline-poll |
| wait_start | 4 | R044.002,R043.002,R040.002,R040.003 | R040,R043,R044 | deadline,raw-dual-stream,supervisor-loss,handshake,raw-dual-stream,handshake,raw-dual-stream,overflow,supervisor-loss |
| watchdog_mode | 9 | R070.002,R061.001,R062.004,R063.002,R060.003,R072.002,R042.003,R042.004,R045.008 | R042,R045,R060,R061,R062,R063,R070,R072 | close-fault,stream-finalization,no-host-runtime-preflight,no-production-input-access,raw-dual-stream,supervisor-loss,supervisor-loss,topology,topology |
| write_all | 1 | R041.001 | R041 | handshake,report-framing |

Lifecycle owners: handshake = read_token_eof/wait_start/probe_lifeline/supervisor_mode/watchdog_mode; raw dual streams = capture_read_once/capture_payload; exit/signal = guarded_wait_once/reduce_wait_observation/classify_capture_wait; deadline/sticky deadline = require_before/capture_guard/latch_capture_deadline/capture_payload; overflow = capture_piece/capture_complete_good/finalize_watchdog; supervisor loss = probe_lifeline/watchdog_mode/finalize_watchdog; report truncation = pread_exact/pread_complete/capture_regular_content/binder_observe; wrong/opposite context = e001Context/canonical_binder_context/rendered_binder_context_good/render_binder/result_line; recovery dispatch model = e001Spawn/e001WaitPid/e001GroupProbe/supervisor_mode/watchdog_mode/recovery_mode. No copied branch/operator is added or removed.

Unredirected host-call families are pure classification/encoding or unreachable behind e001Runtime/e001NormalizeSignals: os.WIFEXITED/WEXITSTATUS/WIFSIGNALED/WTERMSIG/WCOREDUMP, os.fsencode/fsdecode, os.getcwdb/geteuid/getegid/umask, resource.getrlimit, fcntl.fcntl. os._exit affects only a separately authorized disposable fixture process. None opens a path, creates a child, signals an external identity, or accesses build/evidence. Failure to prove this reachability boundary rejects materialization.

## 8. Scenario, adapter, and containment proof

The exact S00-S16 tuples cover handshake success/malformed, separate raw stdout/stderr LF boundaries, nonzero/signal exit, sticky deadline, both overflows, supervisor loss, report truncation, wrong/opposite context, recovery dispatch, close callback/synchronous faults, group absence, and post-close commit fault. Scenarios change only adapter data/return/fault state. Unknown ids select frozen S00 before a synthetic boundary operation.

All path-capable calls are redirected: open=18, stat=17, fstat=28, pread=2, readlink=1, scandir=1. All exact production absolute locators and composed repository/build/evidence components are changed by 24 C2 records. A contains only /tmp/p27-e001-synthetic-supervisor. Exact negative locator counts in I are zero for `/root/autodl-tmp/symplectic_map`, `/root/miniconda3/bin/python3`, `b"build"`, `b"recovery-6103a9df0c3d-evidence"`, and `b"BUILD_VALIDATOR_RECOVERY.py"`. Generic protocol words remain only as copied branch labels/report fields, never path operands.

e001Signal accepts only e001Spawn pids; e001GroupProbe never signals a host. All e001 file, stream, poll, close, report, handshake and context operations are in-memory. A has no import, exec, eval, compile, dynamic loading, subprocess, shell, socket, network, environment read, host PID enumeration, numeric host signaling, recursive traversal, or production callback.

## 9. Fail-closed reproduction algorithm

A separately authorized materializer must re-establish E0333/V8 identities; raw-slice B between unique delimiters; reproduce every row/anchor; require each anchor count one and each P at O; require disjoint intervals; reconstruct A from Section 3; build I both ways; reproduce deltas, censuses, skeleton/declaration locks, negative locators and final identity; and write only after separate destination authority. Any mismatch creates no output.

It must never import, parse, compile, evaluate, or execute B, I, A, a marker, payload, or fixture. Hashing, counting, exact search, delimiter slicing and untouched-span copying are the complete allowed operations.

## 10. Authorship disposition

Authorship transformed bytes only in memory. It created no fixture, process, report, temporary directory, build/evidence/root object, stage, E010, A000, PDF, release, or Paper28 action. This file grants no execution/materialization authority. V1 and all earlier failures remain immutable.

BATCH07_P27_E001_SUPERVISOR_FIXTURE_DERIVATION_MANIFEST_RECOVERY_V2_AUTHOR_STOP
