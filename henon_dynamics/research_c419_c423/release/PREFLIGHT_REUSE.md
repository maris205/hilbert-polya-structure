# C419–C423 发布工具复用静态预检

2026-09-08 UTC。唯一写入本报告。状态：
**UNCHANGED_IMPLEMENTATION_REUSABLE_WITH_EXPLICIT_LEGACY_SCHEMA;
CURRENT_PAYLOAD_NOT_INVENTORIED_OR_VERIFIED**。

## 1. 协调者可据此作出的最小决定

**目前没有必须为本批改写 `exact_payload.py` 的功能性理由。**
它接收显式 `ROOT`，遍历该根的实际成员，不调用上一批数学、PDF、
评价或 Git 逻辑。其实现与测试的实际字节仍与上一批测试／代码审查
冻结身份相同，旧失败路径证据可以明确注明来源后沿用；不能改写成
本轮重新执行了测试。

唯一需要明示的旧批次标记是源码第 20 行：

```text
SCHEMA = "c414-c418-exact-payload-v1"
```

该字符串在实现中是**格式版本的精确标识**，不是允许操作的根目录
或本批编号验证。保持它可在 C419–C423 根上原字节复用，前提是本批
发布说明明确承认沿用此格式，而不把它解释为仍在封存 C414–C418。
本批根路径和新批准摘要必须在树外批准记录中另行明确。

推荐的最小路线是：不改实现／测试；必要时后续获授权后逐字复制
这两个文件作为本批可复现依赖，或使用固定来源路径和摘要；新增
本批操作说明而不改写旧历史收据。若协调者要求 schema 必须改名，
则那是明确的格式／源码变更：应赋予新的格式身份并在新副本上
实际重跑相应失败测试，不能继续宣称旧摘要下的测试就是新代码测试。
不建议仅为换批次标签而触发这种变更。

本批最终树尚有写作者工作，**目前没有批准 ledger、最终成员数、
字节总数、manifest 或封存 PASS**。这些都不能从上一批复用。

## 2. 完整阅读范围与实际身份

从仓库 `/root/autodl-tmp/hilbert-polya-structure` 阅读了：

- 仓库与 Hénon 指令、`henon-route-a-batch/SKILL.md`，及其完整
  [WORKFLOW.md](../../../.agents/skills/henon-route-a-batch/references/WORKFLOW.md)。
- 本批完整 [BATCH_PLAN.md](../BATCH_PLAN.md)，尤其两轮稿件、最终
  双目录构建、全部最终页检查、精确账本、失败路径和封存后只读验证门。
- 上一批 release 的完整
  [实现，279 行](../../continuation_c414_c418_round2/release/exact_payload.py)、
  [测试，315 行](../../continuation_c414_c418_round2/release/test_exact_payload.py)、
  [README，100 行](../../continuation_c414_c418_round2/release/README.md)、
  [TEST_REPORT，122 行](../../continuation_c414_c418_round2/release/TEST_REPORT.md)、
  [REVIEW_CODE，178 行](../../continuation_c414_c418_round2/release/REVIEW_CODE.md)，
  以及 [REVIEW_DOCUMENTATION，196 行](../../continuation_c414_c418_round2/release/REVIEW_DOCUMENTATION.md)。

最后一份仅用于辨明旧文档／链接门与代码／封存门的不同职责；没有
据它重新审查或声明本批五篇稿件／评价／页数。未扫描其他研究流。

只读重新取摘要的实际结果：

| 上批 release 文件 | 当前 SHA256 | 与相应旧收据的关系 |
| --- | --- | --- |
| `exact_payload.py` | `529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f` | 与 TEST_REPORT、REVIEW_CODE 相同 |
| `test_exact_payload.py` | `2c5dc213ba100b724b707ac34c0d364be5330710f3b5b0d7995ef06d61668434` | 与 TEST_REPORT、REVIEW_CODE 相同 |
| `README.md` | `ff574e92a53130bdb1e6fdc0523eb49787ca64584e947041db5cecb497f8273c` | 与 TEST_REPORT、REVIEW_CODE 相同 |
| `TEST_REPORT.md` | `cd685942b2283815fdd5672f5a8d65c50e5b879efa6e36f29c4ee6ae74762665` | 与 REVIEW_CODE 相同 |
| `REVIEW_CODE.md` | `946fba6dc06d5e3ec09003f132984b57456cf8b4edc41edf340ff6f8bbe91b9f` | 本轮读取身份 |
| `REVIEW_DOCUMENTATION.md` | `3a216b535a22a6c68346472dcb9c571541b407dff1f970e42229531c89720a33` | 本轮读取身份 |

本批计划读取身份为
`d799d12bf69d92fe7ba459f75a7fc597baafcdd5963f9125bc38bb5463d89a22`；
批次工作流为
`730e66e9af5df951bf333b63513fb47d13b78b0066ff28483d9e71586878c875`。
这些摘要只定位本次静态输入，不批准活动树的最终成员。

## 3. 依赖与真正的跨根适用性

实现只导入 Python 标准库：`argparse, hashlib, json, os, pathlib,
re, secrets, stat, sys`。测试另用 `copy, subprocess, tempfile,
unittest/mock`，并导入同目录可见的 `exact_payload`。没有本批外的
数学代码、pip 依赖、网络、LaTeX、评价器或 Git 调用。

根目录由 CLI 第 257 行提供，传到 `scan/open_root`。相对成员名
在该根下产生；源码没有硬编码上一批真实路径、C414–C418 文件表、
页数、成员数或旧批准 pin。测试临时目录名前缀 `c414-release-test-`
只是名字，不改变扫描范围或验证逻辑。测试的子进程使用当前
`sys.executable` 与实际导入的 `release.__file__`，不偷偷转去旧
真实封存树。

因此，从仓库根显式指定本批完整绝对根路径，可保持调用工作目录
在 payload 外，也不需要导入、修改或重新执行上一批研究任务。
若后续选择复制测试，须将实现与测试成对放置，确保导入的确是
具有上述摘要的实现；不能复制测试而意外从另一个 `PYTHONPATH`
位置导入同名模块。当前预检未复制任何工具。

需要沿用的实际格式／文件系统政策：

- 只有根下 `PAYLOAD_LEDGER.json`、`MANIFEST.sha256` 是保留元数据；
  子目录里的同名文件仍是普通 payload。
- 所有实际普通文件均参与扫描，包括被 Git 忽略的日志、辅助文件、
  页面 PNG、隐藏文件和字节码。没有 Git allowlist 可替代实际成员集。
- payload 路径采用 ASCII `[A-Za-z0-9_.-]+` 分量；拒绝空分量、
  `.`、`..`、空格、非 ASCII、反斜线、控制符和冒号。
- 拒绝符号链接、非普通文件和多重硬链接；空目录也不被静默忽略。
  普通目录必须恰为实际文件的祖先。它不会替协调者删除“多余”文件。
- 元数据有 16 MiB 读取上限，普通二进制 payload 内容没有同样上限。
  当前未测量最终 ledger/manifest 大小，也没有假定限制一定满足。

这些政策未与本批 BATCH_PLAN 冲突，但**当前真实树是否满足它们
仍未知**。若最终发现不合政策的作者路径／链接／空目录，应先做
明确的处置决定并完成受影响引用检查，再批准新账本；不能以工具
复用为由静默删除或忽略它们。

## 4. 关键保证与实际失败路径覆盖

下表的源码行号针对上述固定摘要。测试方法已经逐个在实际测试
源码中找到；“旧已执行”仅指 TEST_REPORT 的 2026-09-07 收据。

| 本批需要的边界 | 实现位置及机制 | 实际测试覆盖与边界 |
| --- | --- | --- |
| 批准 ledger pin，不能即时重算后自批 | 158–161、265：先检查外给小写 64 位摘要，再比 ledger 原始字节 | `test_missing_ledger_and_invalid_pin`、CLI missing-pin；不能鉴别操作者是否错误地从活动 ledger 重新生成了所传 pin，因此树外 literal 审批仍属人工职责 |
| 精确成员，不仅核验已列项 | 75–139 扫实际树；199–209 先比较完整路径集合，再逐项比 path/bytes/hash | hidden/ignored/binary、missing/unexpected、same-length tamper；没有只用 `sha256sum -c` 的成员盲区 |
| manifest 包含 ledger、自排除、精确字节 | 193–196、210–215：排序、格式、最终 LF 和内容整体比较 | success、manifest-corruptions：缺 ledger、自包含、重复／反序／多余项、错路径、CRLF／无 LF 均有实际变体 |
| 篡改 payload 后重算 manifest 仍失败 | ledger 不变，209 的字节／摘要仍与批准项不符 | `test_recomputed_manifest_cannot_bless_payload_tamper`：已封存后改同长度内容并重算 manifest，用原 pin 验证失败 |
| 篡改后连 ledger 也重算仍失败 | 161 在结构／payload 比较之前拒绝新 ledger 对旧 pin | `test_recomputed_ledger_and_manifest_cannot_bless_payload_with_old_pin`，以及 unsealed 的 `test_recomputed_ledger_cannot_bless_unsealed_tamper_with_old_pin` |
| 非法 ledger 即使摘要匹配也失败 | 150–189：重复 key、严格类型／形状、排序、唯一性、总量、规范 JSON | malformed、schema-types/totals/order、unsafe/self-reference、noncanonical 测试给实际坏字节或结构传**匹配**摘要，避免仅靠摘要变化“碰巧拒绝” |
| 根／祖先和内部 symlink | 58–72 逐分量 `O_NOFOLLOW`；86–102 不跟随链接且只准普通文件 | root/ancestor、文件／目录／悬空链接及 ledger symlink 具体现例；manifest symlink 未单列，但经过相同的文件类型守卫，不冒称每个保留名都单测 |
| hardlink／FIFO／空目录 | 98–100 检查 `S_ISREG` 与 `st_nlink==1`，137 对目录集作精确比较 | `test_fifo_hardlink_empty_directory_and_unsafe_actual_name`。硬链接检查也能拒绝另一个链接在根外的情形，但那个位置变体未单列测试 |
| 验证拒绝前零发布写入 | 245–250：两次完整 preflight 都通过后才发布 | 失败 helper 比较前后名字／类型／mode／nlink／链接目标／文件字节，并 mock publisher 未调用；second-preflight 是显式注入失败，不是实测所有并发情形 |
| 不覆写已有 manifest | 215 先拒绝既有 seal；225、234 用排他 temp 和同目录硬链接发布，不用覆盖式 rename | 既有好／坏 manifest 的 seal 拒绝、直接 publisher 的 no-replace/own-temp-cleanup；不是崩溃回滚保证 |
| `python -O` 不绕过验证 | `require` 用显式异常，不用可移除 assert | 旧整套正常／优化各 21 方法；另有实际 `-B -O` 子进程同长度 tamper 拒绝 |
| 真 CLI 生命周期 | 254–275 的参数／退出码／PASS 输出路径 | CLI check→seal→verify→reseal；前一轮不是只测试内部 helper |

实现的发布阶段暂时用硬链接把自己新建的 temp 发布为 manifest，
随后去掉 temp，使最终 manifest 回到单链接；这与最终树拒绝多重
硬链接不矛盾。若发布中途失败，可能遗留 manifest 或 temp，代码
和旧说明均未承诺任意 I/O 故障下无条件回滚。必须调查真实退出
和遗留状态，不能直接重新 inventory 并换 pin 将失败产物合法化。

## 5. 旧测试收据与当前 Python 环境可复用到什么程度

旧 TEST_REPORT 记录：Linux/POSIX、Python 3.12.3；正常运行
21 个方法、0.553 秒、exit 0，优化运行 21 个方法、0.638 秒、
exit 0。当前只运行环境版本／文件系统信息读取，实际输出为：

```text
python3: /root/miniconda3/bin/python3
Python 3.12.3 | packaged by Anaconda, Inc. |
(main, Apr 19 2024, 16:50:38) [GCC 11.2.0]
Linux 5.15.0-78-generic x86_64
old release root: xfs, block_size=4096
current batch root: xfs, block_size=4096
```

源码、测试、已记录 Python 版本及平台类别一致，又没有新增第三方
运行时依赖，因而**合理的最小做法是复用旧收据为同一已测试实现
的回归／失败路径证据**，无需因批次编号变化重跑数学或重写验证器。
这不是“本轮 21+21 又通过”，也不是将旧真实树的 seal PASS 移植过来。

证据精度的真实限制：旧报告未记录解释器可执行文件摘要、完整构建串、
内核、测试时临时目录的实际挂载／选项或完整环境变量。当前两根均为
XFS，也不能反推旧 tempfile 当时位于何种挂载。因此不能宣称环境
已作逐字／全平台等同性证明；旧 Linux/POSIX 测试也不推出 Windows、
网络文件系统、特殊挂载或 hostile-writer 环境兼容。

若协调者要求比上述“同实现、同已记录版本／平台”更严格的环境
冻结证据，或将改 schema、路径政策、运行时／文件系统，则应在
授权后于 payload 外的新临时夹具补做正常／优化测试并记录实际环境。
那属于明确环境／输入缺口触发的受影响检查，不是盲目重复 PASS。
当前无这类改动，也未在此次只读预检擅自执行任何测试。

## 6. 真正没有覆盖的内容，不应包装成新 bug 或既有 PASS

1. **非原子全树快照。** `stamp` 能发现读文件时和遍历目录时
   观察到的变化，但不能保证已读文件在后续不被原地写入；第二次
   preflight 到发布之间也有窗口。停止全部写作者是合同前提，不能
   以“两次扫描”替代。当前 writers active 正是不能提前批准的理由。
2. **不是批次内容判定器。** ledger 没有 batch-id 或根的绝对路径
   字段，也不要求五篇论文或任何固定必备文件。即使另一个根有完全
   相同的成员／字节，同一账本也会满足纯字节合同。协调者必须将
   已审内容、明确根路径、固定工具身份和批准 literal pin 绑定在
   树外记录中。正确运行工具不能弥补错误批准了一份不完整账本。
3. **不是权限／所有权／时间元数据签名。** 账本绑定 path、bytes、
   SHA256 和总数／总字节，未绑定 UID/GID、持久 mode、xattr 或
   mtime。`stamp` 中的 mode/ctime 用于扫描稳定性，不等于它们已被
   永久批准。当前 byte/member 合同无需改为系统镜像合同。
4. **未穷尽异常测试。** 未见 16 MiB 超限夹具，也未逐个注入
   `open/read/fsync/unlink` 的 I/O 错误或在每一个 stamp 间真实竞争
   写入。现有 second-pass 测试是控制注入。旧报告正确把 21 计为
   unittest 方法，而不是全部分支或全部攻击覆盖。本批未引入这些
   新保证，无须为保持原边界而假称旧测试已经覆盖它们。
5. **本批独立最终成员核验尚未有实际收据。** 原工具的测试辅助
   代码并不是独立生产核验器；`sha256sum -c` 单独运行也不排除
   多余成员。最终独立检查至少应重新取得实际成员集、按同一两项
   根元数据规则作集合相等比较，并逐一核对长度／摘要及 manifest。
   它不能只再次调用原 `preflight` 后改称“独立”。

这些限制与旧静态审查已声明的可信 pin／可信 verifier／静止
Linux-POSIX 树合同相符。本次没有找到需要立即修改实现的安全
修复项；若扩大其中任一保证，则必须另立实现与验证范围。

## 7. 必须留给本批最终输入的最小新检查

下列是真正未完成且不能以旧 receipt 替代的步骤，**本报告未执行**：

1. 完成本批两轮实际稿件／修订闭环、正式评价、每篇两个新目录
   的最终构建、字节比较和全部最终页视觉检查；所有将纳入发布的
   报告及依赖先写完。停止本批所有写作者和会产生日志／缓存的进程。
2. 明确最终根和复用工具身份／格式政策。对最终树生成真实候选
   inventory，并将候选捕获在 payload 外；不得把重定向目标先在
   根内创建成 ledger/manifest。实际评估成员、命名／链接／空目录
   政策及元数据尺寸，之后由协调者批准准确字节。
3. 安装**已批准**的 canonical ledger，在树外保存 literal SHA256
   和根路径／工具摘要。本批批准值是新值，不能拿旧 pin，也不能
   在 check/seal/verify 时即时 rehash 活动 ledger 当作批准来源。
4. 对本批静止树实际执行只读 `check`，再 `seal`，记录实际退出及
   失败处置。调用用 `python3 -B`、工作目录在 payload 外，避免
   Python 生成 `__pycache__` 或根内控制台收据成为未批准成员。
5. **封存后**实际运行 `verify` 及上节所述独立成员／摘要检查。
   既有 manifest 会阻止 `check/seal`，所以封存后用 `verify`，
   不重复 seal。保留封存后收据在树外；向已封存根内补一份报告
   或忽略文件都会破坏精确成员合同。

待这些步骤真实执行后才能报告最终 `N` 个 payload 文件、ledger
排除两个根元数据、manifest 包含 `N+1` 项等实际值。这里 `N`
只是说明规则的符号，没有以活动目录的暂时状态给出预测计数。

## 8. 本次执行收据

本次执行仅包括所列文件的静态完整阅读、源码行定位、SHA256、
`python3 -VV`／可执行路径、`uname`、两已知根的文件系统元数据及
定向 `git status`。旧 release 路径未显示修改；本批计划仍是新
未跟踪文件，这不是全仓库“干净”判断。当前 release 目录最初
尚未存在，本报告由授权文件编辑机制创建。

未导入实现模块，未运行 `inventory/check/preflight/seal/verify`
或测试，未执行任何数学程序／编译／扫描其他流，未生成 ledger
或 manifest，未复制工具、修改代码、修改稿件或进行 Git 写操作。
使用仓库 `henon-route-a-batch` 的发布／收据复用要求，保留“最终
输入新检查”与“已冻结工具旧测试可复用”的区别；该技能没有被
当成提前封存或扩大写权限的授权。
