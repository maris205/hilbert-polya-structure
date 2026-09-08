# C419–C423 封存后独立精确成员与字节核验

2026-09-08 UTC。结论：**PASS — 本次实际封存后、只读、独立
byte/member 核验通过，零已发现不符项**。本报告位于封存根外；
它不属于该 ledger 或 manifest，不应补入已经封存的 payload。
协调者尚须全文阅读并裁决本报告，本文不代替其最终交付决定。

## 1. 固定授权输入与独立性的范围

唯一实际检查根为：

```text
/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423
```

协调者明确确认全部 payload 写作者停止，且已经完成
inventory → 批准候选 → apply_patch 安装并 cmp → check → seal → verify。
协调者通过任务消息提供、且已记录在包外
[批准与执行收据](RELEASE_C419_C423.md) 中的 **literal PIN** 为：

```text
82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14
```

上述值直接作为独立脚本中的固定常量；不是在本次检查时对活动
ledger 取摘要后重新选择的“批准值”。本次先将原始 ledger 的实际
摘要与该外给字面值比较，成功后才解析内容和核对 payload。
协调者另外给出的 manifest 摘要也作为待核对声明而非成员来源：

```text
6d4be9ad32e930f36f4aa5266f83dd4dbe39cb9b4fd8a0c0489afb45581fdcbc
```

本次没有导入或调用既有 producer、其 preflight、CLI 或测试。
独立脚本使用 Python 标准库自行 os.walk/lstat 枚举、自行读取所有
实际文件、自行解析 ledger，并从实际文件集合及新算摘要重建 manifest。
没有仅用 sha256sum -c 已列项检查来代替精确成员比较。

读取了本批完整
[发布政策](research_c419_c423/release/README.md)、
[复用预检](research_c419_c423/release/PREFLIGHT_REUSE.md) 及包外批准
收据；另只读查看旧 release 的完整 README 和 exact_payload.py
第 1–75、142–216 行，确定格式常量、JSON 键／序列化和 manifest
字节约定。此静态格式读取不是导入或执行旧实现。
沿用的 schema `c414-c418-exact-payload-v1` 是格式标识，不是根目录
授权或本批编号；绝对根和新批准 PIN 由上述外部授权绑定。

仓库 henon-route-a-batch 技能在此仅用于最后的精确清单和封存后
收据门：不重跑已接受的数学、稿件审查、评价或 PDF 构建，也不扩大
Git、网络或发布权限。旧 21+21 测试不是此次重新执行的测试。

## 2. 实际执行和主要结果

工作目录在 payload 外，为：

```text
/root/autodl-tmp/hilbert-polya-structure
```

本次独立检查实际执行 **一次**，命令为：

```sh
python3 -B /tmp/c419-c423-independent.Fd75PVkM/check_release.py
```

实际退出码 **0**，返回 PASS JSON；没有失败后重算账本、换 PIN、
修复成员或重新封印。一次调用内部执行了两遍完整文件内容读取和
三次全树成员／元数据快照；不是声称重复运行了原 producer 两次。
脚本另外在首次内容遍历前先读取 ledger 以验证批准 PIN。
该脚本共 **243 行**，执行前后实际 SHA256 均为：

```text
dd82e57a5bd4ada73ad103b6429ce807034751f43914c5b8bedf4f42efdd9442
```

末节嵌入其完整实际源码，不依赖临时路径永久存在。若未来需要复现，
可将该代码原字节保存到另一个包外文件，以 python3 -B 从包外调用；
在输入未变化且检查已经通过的情况下，本报告不要求再跑一遍。

| 本次独立测得的对象 | 文件／条目数 | 字节数 | SHA256 或关系 |
| --- | ---: | ---: | --- |
| 全部 payload | 1062 | 66,117,408 | 每项长度和 SHA256 均与批准 ledger 一致 |
| 根 PAYLOAD_LEDGER.json | 1 | 209,134 | 82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14 |
| 根 MANIFEST.sha256 | 1063 条 | 136,358 | 6d4be9ad32e930f36f4aa5266f83dd4dbe39cb9b4fd8a0c0489afb45581fdcbc |
| 连同两份根元数据的所有实际普通文件 | 1064 | 66,462,900 | 两遍全量内容相同 |
| 实际子目录，不含根 | 181 | 不适用 | 恰为实际文件的全部非根祖先 |

全部 1062 项由原始批准
[ledger](research_c419_c423/PAYLOAD_LEDGER.json) 列出；本次实际枚举集与其
路径集相等，逐项长度／摘要相等，并重新求和验证总数及总字节。
清单包含 paper 子树全部 801 文件、十份 manuscript_reviews、五份
evaluations、三份 evaluation_revisions；完整一级分布见下方原始输出。
一级分类只是结果摘要，不是扫描 allowlist。

## 3. 实际检查的细节及边界

- 根及其祖先逐级 lstat，六个目录均为真实目录；检查前后
  device/inode/mode 身份一致。没有通过 resolve 将 symlink 合法化。
- os.walk(followlinks=False) 枚举每个实际名字，逐项 lstat；
  没有 Git、扩展名、隐藏名、日志、辅助文件或缓存过滤。
  每个实际成员都必须为目录或单链接普通文件；所有实际相对路径
  都满足 ASCII [A-Za-z0-9_.-]+ 分量规则，禁止空、点／双点分量。
  因而本次没有被接受的 symlink、特殊文件、多重硬链接或非法名字。
- 实际目录集合与普通文件全部祖先集合严格相等；181 个子目录中
  没有不被文件表示的空目录。不是先删除空目录再验收。
- 仅根 PAYLOAD_LEDGER.json 和 MANIFEST.sha256 是保留元数据；
  ledger 精确排除这两项，manifest 包含 ledger 并仅排除自身。
  子目录同名文件不会被保留名集合排除。
- 原始 ledger 先过外给 PIN，再过严格 JSON：拒绝重复键、非有限
  常量、额外／缺少键、错误结构、布尔值冒充整数、不合法长度／
  SHA256、非法或重复／不排序路径、根元数据自引用及不一致总量。
  以固定格式重新序列化并对原始字节做整体相等比较，包括最终 LF。
  两份实际元数据均低于 16 MiB；普通二进制 payload 不套用该限制。
- 使用实际文件集合及新读取计算出的 SHA256，按 ASCII 路径排序，
  重建每行“小写摘要 + 两空格 + 路径 + LF”的完整 manifest 字节串；
  与实际 manifest 原始字节完全相等。因此并非只检查行内摘要，
  而同时排除遗漏／额外／重复／错序条目及非规范分隔、CRLF 或缺 LF。
- 每个文件以 O_RDONLY/O_NOFOLLOW 打开；实际读取长度与初始 lstat
  大小一致，打开前后与读取前后的 lstat/fstat 均匹配。三次全量
  快照的全部名字与 device/inode/mode/nlink/size/mtime_ns/ctime_ns
  相同；两遍所有实际文件的长度、摘要及两份元数据原文一致。

另一内部代理只读审查了上述实际脚本源码，没有执行扫描、没有
读取真实 payload 来重复验收，也没有写文件；未发现范围内必改项。
这项静态辅助审查不是额外一次运行或通用验证器安全认证。

上述结果是在协调者声明停止全部写作者的 Linux/POSIX 环境下的
有限观察。它**不是原子全树快照、对恶意并发写者的防御、未来稳定性
保证或数字签名**；无法抵抗同时替换受信代码与外部批准 PIN。
访问时间 atime 不在稳定性比较中，普通只读访问仍可能由文件系统
更新 atime；没有声称系统级所有元数据零变化。祖先目录仅比较身份，
不要求包外其他工作导致的父目录时间变化一并冻结。

本次检查绑定文件相对路径、长度、SHA256 和总量；不把 UID/GID、
持久权限、xattr 或时间戳扩充成永久批准的系统镜像合同。
这是数学、来源、优先权、评价和构建之外的字节完整性门，
不提高任何 Route-A／Route-B 科学结论，也不代替人类同行评审。
本次未运行故障注入或新回归套件；不能把实际正常树的 PASS
夸大成每种非法输入已经实测拒绝。

## 4. 写入范围和交接

封存根内没有创建、编辑、删除、重新构建或生成缓存。
脚本的 payload 文件打开标志均为只读；实际运行
dont_write_bytecode=true。未做任何 Git、网络、数学程序、评价、
LaTeX 或 producer 调用；未修改既有账本和 manifest。

本次只创建包外临时目录及脚本，以及这份指定的包外报告。
命令输出由调用方接收后原样嵌入下节，不曾重定向进 payload。
临时脚本保留，完整源码也保留于本报告。没有移除任何实际成员，
没有自动换 PIN 或将不符项重新 inventory 合法化。

本报告写出后不再写 payload；由协调者全文审阅本报告、在包外记录
裁决及后续已授权的同步结果。这里不宣称已经发生 Git 提交、推送
或外部出版，也不开始 C424。

## 5. 本次调用的完整原始输出

```json
{
  "actual_regular_files_including_metadata": 1064,
  "actual_subdirectories_excluding_root": 181,
  "actual_total_bytes_including_metadata": 66462900,
  "all_stamps_unchanged": true,
  "approved_ledger_pin_literal": "82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14",
  "cwd": "/root/autodl-tmp/hilbert-polya-structure",
  "dont_write_bytecode": true,
  "exact_membership": true,
  "finished_utc": "2026-09-08T11:31:44.609120+00:00",
  "full_content_passes": 2,
  "full_walk_snapshots": 3,
  "ledger_bytes": 209134,
  "ledger_sha256": "82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14",
  "ledger_strict_canonical": true,
  "manifest_bytes": 136358,
  "manifest_canonical_actual_members": true,
  "manifest_entries": 1063,
  "manifest_sha256": "6d4be9ad32e930f36f4aa5266f83dd4dbe39cb9b4fd8a0c0489afb45581fdcbc",
  "missing_members": [],
  "payload_bytes": 66117408,
  "payload_count": 1062,
  "payload_reads_only": true,
  "payload_top_level_counts": {
    "(root files)": 10,
    "arithmetic": 5,
    "arithmetic_spectral": 22,
    "checkpoint_review": 1,
    "continuation_round2": 33,
    "continuation_round3": 30,
    "continuation_round4": 24,
    "continuation_round5": 22,
    "continuation_round6": 16,
    "continuation_round7": 17,
    "continuation_round8": 24,
    "continuation_round9": 25,
    "evaluation_revisions": 3,
    "evaluations": 5,
    "manuscript_reviews": 10,
    "mapping_class_review": 2,
    "nonlinear_geometry": 4,
    "papers": 801,
    "positive_characteristic": 5,
    "release": 3
  },
  "platform": "Linux-5.15.0-78-generic-x86_64-with-glibc2.35",
  "producer_imports_or_calls": 0,
  "python_executable": "/root/miniconda3/bin/python3",
  "python_version": "3.12.3 | packaged by Anaconda, Inc. | (main, Apr 19 2024, 16:50:38) [GCC 11.2.0]",
  "root": "/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423",
  "root_ancestor_directory_count_including_root": 6,
  "stamps_sha256": "0d27c986b9cc02eb841c316ad4b157282e6fa8620cbbae71f310bf22d606b03e",
  "started_utc": "2026-09-08T11:31:44.384079+00:00",
  "status": "PASS",
  "unexpected_members": []
}
```

## 6. 完整实际调用源码

以下代码块为上述 243 行脚本的完整原字节文本（含最终 LF）。

```python
#!/usr/bin/env python3
"""One-shot, independent, read-only C419-C423 byte/member audit."""
import datetime
import hashlib
import json
import os
import platform
import re
import stat
import sys

ROOT = "/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c419_c423"
APPROVED_PIN = "82583a3fe4f10fdf16f786de276127f99081129a0a2dfe5285349a06f0f36c14"
CLAIMED_MANIFEST_SHA = "6d4be9ad32e930f36f4aa5266f83dd4dbe39cb9b4fd8a0c0489afb45581fdcbc"
LEDGER = "PAYLOAD_LEDGER.json"
MANIFEST = "MANIFEST.sha256"
RESERVED = {LEDGER, MANIFEST}
META_LIMIT = 16 * 1024 * 1024
COMPONENT = re.compile(r"[A-Za-z0-9_.-]+", re.ASCII)
HEX = re.compile(r"[0-9a-f]{64}", re.ASCII)
START = datetime.datetime.now(datetime.timezone.utc).isoformat()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def stamp(info):
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
            info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def path_ok(path):
    require(type(path) is str and bool(path), "empty or non-string path")
    require(all(c not in ("", ".", "..") and COMPONENT.fullmatch(c)
                for c in path.split("/")), "unsafe path: " + repr(path))


def ancestors():
    result = {}
    current = "/"
    for part in [""] + ROOT.split("/")[1:]:
        if part:
            current = os.path.join(current, part)
        info = os.lstat(current)
        require(stat.S_ISDIR(info.st_mode), "root/ancestor is not a directory: " + current)
        result[current] = (info.st_dev, info.st_ino, info.st_mode)
    return result


def walk_snapshot():
    entries = {"": stamp(os.lstat(ROOT))}
    require(stat.S_ISDIR(entries[""][2]), "root is not a real directory")
    files, directories = set(), set()

    def walk_error(exc):
        raise exc

    for current, dirnames, filenames in os.walk(ROOT, topdown=True,
                                               followlinks=False, onerror=walk_error):
        relative = os.path.relpath(current, ROOT)
        relative = "" if relative == "." else relative
        require(relative in entries, "unrecorded traversed directory: " + relative)
        require(stamp(os.lstat(current)) == entries[relative],
                "directory changed before traversal: " + relative)
        require(len(set(dirnames + filenames)) == len(dirnames + filenames),
                "duplicate actual directory entry: " + relative)
        for name in sorted(dirnames + filenames):
            path = name if not relative else relative + "/" + name
            path_ok(path)
            require(path not in entries, "duplicate actual member: " + path)
            info = os.lstat(os.path.join(current, name))
            entries[path] = stamp(info)
            if stat.S_ISDIR(info.st_mode):
                require(name in dirnames, "directory classification changed: " + path)
                directories.add(path)
            else:
                require(stat.S_ISREG(info.st_mode), "symlink or special member: " + path)
                require(info.st_nlink == 1, "multiply linked file: " + path)
                require(name in filenames, "file classification changed: " + path)
                files.add(path)
        require(stamp(os.lstat(current)) == entries[relative],
                "directory changed during traversal: " + relative)
        dirnames.sort()
    represented = set()
    for path in files:
        parts = path.split("/")
        represented.update("/".join(parts[:i]) for i in range(1, len(parts)))
    require(directories == represented,
            "unrepresented/empty directories: " + repr(sorted(directories - represented)))
    require(RESERVED <= files, "root ledger or manifest missing")
    return entries, files, directories


def read_stable(path, baseline):
    absolute = os.path.join(ROOT, path)
    expected = baseline[path]
    metadata = path in RESERVED
    require(stamp(os.lstat(absolute)) == expected, "file changed before open: " + path)
    require(not metadata or expected[4] <= META_LIMIT, "metadata exceeds 16 MiB: " + path)
    fd = os.open(absolute, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC | os.O_NONBLOCK)
    try:
        require(stamp(os.fstat(fd)) == expected, "opened identity changed: " + path)
        digest, count, chunks = hashlib.sha256(), 0, []
        while True:
            block = os.read(fd, 1024 * 1024)
            if not block:
                break
            count += len(block)
            require(not metadata or count <= META_LIMIT, "metadata grew above limit: " + path)
            digest.update(block)
            if metadata:
                chunks.append(block)
        require(count == expected[4], "length differs from lstat: " + path)
        require(stamp(os.fstat(fd)) == expected, "file changed while reading: " + path)
    finally:
        os.close(fd)
    require(stamp(os.lstat(absolute)) == expected, "file identity changed after read: " + path)
    return count, digest.hexdigest(), b"".join(chunks) if metadata else None


def strict_ledger(raw):
    require(HEX.fullmatch(APPROVED_PIN) is not None, "invalid fixed approval PIN")
    require(hashlib.sha256(raw).hexdigest() == APPROVED_PIN, "external ledger PIN mismatch")

    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key: " + repr(key))
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError("nonfinite JSON constant: " + value)

    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique_object,
                       parse_constant=reject_constant)
    require(type(value) is dict and set(value) ==
            {"schema", "files", "payload_count", "payload_bytes"}, "wrong ledger shape")
    require(type(value["schema"]) is str and value["schema"] ==
            "c414-c418-exact-payload-v1", "wrong format identity")
    require(type(value["files"]) is list, "files is not a list")
    for key in ("payload_count", "payload_bytes"):
        require(type(value[key]) is int and value[key] >= 0, "invalid integer total: " + key)
    paths, expected = [], {}
    for entry in value["files"]:
        require(type(entry) is dict and set(entry) == {"path", "bytes", "sha256"},
                "wrong ledger entry shape")
        path_ok(entry["path"])
        path = entry["path"]
        require(path not in RESERVED, "root metadata in ledger payload")
        require(path not in expected, "duplicate ledger member: " + path)
        require(type(entry["bytes"]) is int and entry["bytes"] >= 0,
                "invalid entry byte count: " + path)
        require(type(entry["sha256"]) is str and HEX.fullmatch(entry["sha256"]),
                "invalid entry SHA256: " + path)
        paths.append(path)
        expected[path] = (entry["bytes"], entry["sha256"])
    require(paths == sorted(paths), "ledger paths not strictly sorted")
    require(value["payload_count"] == len(paths), "ledger count inconsistent")
    require(value["payload_bytes"] == sum(item[0] for item in expected.values()),
            "ledger byte total inconsistent")
    canonical = (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                            allow_nan=False) + "\n").encode("ascii")
    require(raw == canonical, "ledger bytes are not exact canonical JSON")
    return value, expected


def main():
    require(os.path.commonpath((os.getcwd(), ROOT)) != ROOT, "cwd is inside payload")
    before_ancestors = ancestors()
    baseline, files, directories = walk_snapshot()
    ledger_bytes, ledger_sha, ledger_raw = read_stable(LEDGER, baseline)
    ledger, expected = strict_ledger(ledger_raw)
    actual_payload = files - RESERVED
    require(actual_payload == set(expected),
            "exact membership mismatch; missing=" + repr(sorted(set(expected) - actual_payload)) +
            "; unexpected=" + repr(sorted(actual_payload - set(expected))))
    first = {}
    for path in sorted(files):
        first[path] = read_stable(path, baseline)
        if path in actual_payload:
            require(first[path][:2] == expected[path], "payload bytes/SHA256 mismatch: " + path)
    require(first[LEDGER] == (ledger_bytes, ledger_sha, ledger_raw), "ledger changed between reads")
    manifest_raw = first[MANIFEST][2]
    manifest_paths = sorted(files - {MANIFEST})
    manifest_expected = b"".join((first[path][1] + "  " + path + "\n").encode("ascii")
                                 for path in manifest_paths)
    require(manifest_raw == manifest_expected, "manifest not exact actual canonical inventory")
    require(first[MANIFEST][1] == CLAIMED_MANIFEST_SHA, "coordinator manifest SHA claim differs")
    middle, middle_files, middle_directories = walk_snapshot()
    require((middle, middle_files, middle_directories) == (baseline, files, directories),
            "actual names or metadata changed after first complete content pass")
    for path in sorted(files):
        require(read_stable(path, baseline) == first[path], "second content pass differs: " + path)
    final, final_files, final_directories = walk_snapshot()
    require((final, final_files, final_directories) == (baseline, files, directories),
            "actual names or metadata changed after second complete content pass")
    require(ancestors() == before_ancestors, "root/ancestor identity changed")
    count = len(actual_payload)
    payload_bytes = sum(first[path][0] for path in actual_payload)
    require((count, payload_bytes, ledger_bytes, len(manifest_paths)) ==
            (1062, 66117408, 209134, 1063), "coordinator count/length claim differs")
    require((count, payload_bytes) == (ledger["payload_count"], ledger["payload_bytes"]),
            "actual totals disagree with ledger")
    categories = {}
    for path in actual_payload:
        category = path.split("/")[0] if "/" in path else "(root files)"
        categories[category] = categories.get(category, 0) + 1
    report = {
        "status": "PASS", "started_utc": START,
        "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "root": ROOT, "cwd": os.getcwd(), "python_executable": sys.executable,
        "python_version": sys.version, "platform": platform.platform(),
        "dont_write_bytecode": sys.dont_write_bytecode,
        "approved_ledger_pin_literal": APPROVED_PIN,
        "ledger_bytes": ledger_bytes, "ledger_sha256": ledger_sha,
        "payload_count": count, "payload_bytes": payload_bytes,
        "manifest_entries": len(manifest_paths), "manifest_bytes": first[MANIFEST][0],
        "manifest_sha256": first[MANIFEST][1],
        "actual_regular_files_including_metadata": len(files),
        "actual_total_bytes_including_metadata": sum(item[0] for item in first.values()),
        "actual_subdirectories_excluding_root": len(directories),
        "root_ancestor_directory_count_including_root": len(before_ancestors),
        "full_content_passes": 2, "full_walk_snapshots": 3,
        "all_stamps_unchanged": True,
        "stamps_sha256": hashlib.sha256(json.dumps(baseline, sort_keys=True,
                                                   separators=(",", ":")).encode("ascii")).hexdigest(),
        "payload_top_level_counts": dict(sorted(categories.items())),
        "payload_reads_only": True, "producer_imports_or_calls": 0,
        "manifest_canonical_actual_members": True, "ledger_strict_canonical": True,
        "exact_membership": True, "missing_members": [], "unexpected_members": [],
    }
    print(json.dumps(report, sort_keys=True, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("FAIL " + type(exc).__name__ + ": " + str(exc), file=sys.stderr)
        sys.exit(1)
```

