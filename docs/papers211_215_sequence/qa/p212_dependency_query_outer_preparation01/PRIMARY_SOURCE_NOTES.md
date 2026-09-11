# Primary technical source notes

Read as source material only, not host-runtime observations. All paraphrases
below concern the explicitly proposed Linux/Python mechanism. No local
runtime probe, kernel inventory or manuscript/body access follows from them.

- Linux kernel UAPI [stat.h](https://raw.githubusercontent.com/torvalds/linux/master/include/uapi/linux/stat.h):
  struct statx is 0x100 bytes with the documented basic fields/timestamps and
  device-number offsets used in the proposed decoder. Returned stx_mask
  identifies valid fields; compatibility values without their returned mask
  do not satisfy this proposal's all-basic-plus-birthtime gate. This is a
  source-layout basis, not evidence that this host supports that ABI/syscall.
- Linux man-pages [PR_SET_CHILD_SUBREAPER](https://man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html):
  a living subreaper can adopt orphaned descendant processes and wait for
  their termination. The attribute survives exec and is not automatically
  inherited by a forked child. This supports the proposed supervisor
  ownership mechanism, not an escaped-writer or exhaustive-history claim.
- Linux man-pages [wait(2)](https://man7.org/linux/man-pages/man2/wait.2.html):
  WNOWAIT leaves waitable status available; ECHILD is distinct from a
  nonblocking observation with no status available. The proposed source
  separately records waitid information, actual waitpid status and ECHILD.
- Linux man-pages [statx(2)](https://man7.org/linux/man-pages/man2/statx.2.html):
  descriptor-based empty-path and no-follow observations have explicit flags,
  and returned validity bits matter. The proposed source keeps the raw
  returned buffer and rejects unsupported required fields.
- Linux kernel [proc documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html),
  section 3.7: task children listings can be incomplete as children exit
  during collection. The outer source labels its own children-chain samples
  discrete and nonexhaustive; a race is not filled in as a successful census.
- Python 3.10 [os](https://docs.python.org/3.10/library/os.html):
  nonblocking waitid can return no result when no status is currently
  available, whereas ChildProcessError represents the ECHILD condition.
  Native returned wait statuses remain separately recorded.
- Python 3.10 [ctypes](https://docs.python.org/3.10/library/ctypes.html):
  CDLL with use_errno provides errno handling for the proposed libc calls.
  Explicit argtypes/restype and LP64 checks constrain this new mechanism;
  the source does not run find_library or infer a runtime-file closure.

An attempted guessed man7 ctypes.3 page was not a usable source. It supplied
no evidence and did not become a local host query or recovered result.
No document above proves current installed behavior or runtime acceptance.
