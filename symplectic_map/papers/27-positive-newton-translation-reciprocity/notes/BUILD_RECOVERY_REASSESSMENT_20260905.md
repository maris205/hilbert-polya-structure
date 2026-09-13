# Paper27 构建恢复复核与已确认的控制流程替换

日期：2026-09-05（会话环境日期）。性质：只读诊断结果及方案提议，不是构建 PASS、执行许可或对旧失败的改判。

## 结论

原始物理故障的 parser 修复已存在，历史上已有针对该 parser 的真实运行 PASS；当前 RECOVERY validator 仍保留修复。现存恢复 profile 也已包含解决 bootstrap 循环依赖的明确例外。因此，不应再把“修正最初 parser”或“补上首次建目录例外”列为尚未实现的工作。

尚未证明的是完整 validator、控制执行链、实际两根构建及最终交付。E0406 的 Host durable-release 要求属于后续控制审查，不是本次定位到的原始构建失败原因。本复核不执行该链，不自行取消失败后的保护边界。

## 原始证据与本轮核验

| 事项 | 证据 | 能证明 / 不能证明 |
| --- | --- | --- |
| 原始失败 | BATCH_07_STATUS.md 第 16915–16921 行，E0282 | A000 的合法 `root=r0` 被自结果 parser 拒绝；仅 E001/E010/A000 执行，R000 未执行。不是 TeX 输出失败 |
| 用户恢复授权 | 账本第 16969–16971 行，E0283；当前可见用户原话 | 修正 validator、新 evidence/root、保留旧失败；不能直接推导新增 Host 分布式持久化契约 |
| 修复后的真实测试 | 账本第 17891–17915 行，E0295 | 历史 parser-only 运行 exit 0，53 positives / 138 negatives；不是全模块或完整构建 PASS，本轮未重跑 |
| 当前修复保留 | BUILD_VALIDATOR_RECOVERY.py 第 2970–3033 行 | 本轮直接读到六个 name-first 符号字段分支，合法值不再因 invalid-only 分支落入 UNVALIDATED；未 import/解析/执行文件 |
| Bootstrap 循环依赖 | 账本第 17965–17969 行，E0296 | 原计划要求在 evidence 目录创建前，把 receipt 写进该目录；不是论文数学故障 |
| 当前 bootstrap 例外 | BUILD_PROFILE_RECOVERY.md 第 517–526 行；INDEPENDENT_BUILD_PROFILE_RECOVERY_REVIEW.md 第 222–228 行 | 本轮读到首次建目录可直接捕获结果，随后恢复 receipt 要求；历史静态审查为 PASS，不是本轮运行证明 |
| 后续停止点 | E0406 | V34 生命周期审查失败，V35 未创建，Host 契约记为未授权/未实现；不声称这些失败已经解决 |

主代理核验了当前源文件哈希和上述原文；另一个独立、只读的代理从 E0246–E0298 追溯故障链。双方均未访问任何 build/evidence 树，未执行嵌入代码，也未承担新的论文或完整构建独立审查。

当前核验的 SHA-256：

- BATCH_07_STATUS.md：`d10dcffe32eb27d613c2362af18ad1512397d77ecafd6b643dacbb822b3cc3ef`
- paper/main.tex：`d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e`
- notes/BUILD_VALIDATOR_POSTFAIL.py：`6103a9df0c3d3fec652b9b39e0407b6a35eb369a7950d1b1724c8918fbe57693`
- notes/BUILD_VALIDATOR_RECOVERY.py：`6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817`
- notes/BUILD_PROFILE_RECOVERY.md：`ac1651c8ef5522f76f52b98a9deb300d5409c489d6e3ae4fa58e9d6e3fc4c985`

文件路径除账本外均相对于 Paper27 项目。本轮只核验列出的文件与片段，未重建全部依赖锁或 manifest。

## 提议：替换恢复控制链，保留论文验收标准

需要用户明确决定的是**是否替换现有失败后恢复控制流程**，而不是是否降低论文质量或接受未验证输出。

拟替换范围：停止扩写 V35 / Host durable-release 协议，另建有限、单写者的本地构建编排。首次新目录创建的结果先由调用方捕获，之后才写该目录内的日志；固定步骤顺序执行，失败或结果不明即停止并保留证据，不自动重放，也不承诺任意进程崩溃后的无重复且必然完成。后续恢复先核对实际状态，不靠超时推断任务失败。

保持不变：

- 所有旧失败、旧 evidence/root、冻结控制文件与既有审查原样保留；新工作使用另行确定并先审查的全新路径，不扫描旧 build 树，不清理、不覆盖。
- 冻结的数学范围、匿名正文、source/publication locks、已接受证明和引用边界不变。本方案不授权为凑页数而灌水或改变排版。
- 两个隔离根，每根固定 TeX → BibTeX → TeX → TeX；源、工具、依赖绑定及本地环境检查；不联网、不安装依赖、不启动实验。
- 24–28 页证明正文及 reference sentinel，二十条引用闭合，交叉引用已解析，零 overfull，残余 warning 逐项解释，字体、可读性、匿名性、元数据与内容完整性验收不变。
- PDF 与规定产物的确定性比较保留；仅允许既有合同明示的根前缀归一化，不用归一化掩盖其他差异。
- 新编排和必要的 validator 适配必须先由未参与实现的独立审查者检查；运行后再独立核查真实产物。已通过的 parser-only 测试不得冒充新编排测试。
- 任何新发现先真实记录；旧 FAIL 不改 PASS。只有 Paper27 获得新的 release-grade 完整性 PASS 后才推进 Paper28。无投稿、上传、外部消息或公开发布。

若用户确认上述替换范围，下一步是形成紧凑、精确、可审查的新编排与验收对应表，然后在审查通过后实际构建；不是继续新增抽象恢复协议。不在本提议中预先宣称执行成功，也不将确认视为放弃独立审查或所有未来权限限制。

## 当前状态

`USER_CONFIRMED_IMPLEMENTATION_OPEN`。用户已确认替换范围，原授权缺口已解决，不得继续以待确认阻塞。原账本、旧 validator/profile/V34、旧失败与旧根保持原样。新编排正在审查，尚无构建或 release-grade 完成声明；五篇论文的总体目标仍未完成。

后续授权记录：用户明确回复“确认继续就行”，采纳上述替换范围。此前等待确认是历史状态，现已解决。实施入口为 `LOCAL_BUILD_20260905_PLAN.md` 与 `LOCAL_BUILD_20260905.py`；新编排先独立审查，再实际构建，无需对此范围反复索取确认。
