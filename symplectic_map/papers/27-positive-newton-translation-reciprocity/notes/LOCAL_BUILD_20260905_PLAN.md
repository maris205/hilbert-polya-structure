# Paper27 简化本地构建计划

用户确认：“确认继续就行”。该确认采纳 BUILD_RECOVERY_REASSESSMENT_20260905.md 的控制流程替换范围。它不降低论文标准，不改判旧失败，不授权任何外部效力。本计划与新脚本是独立的新控制产物，旧账本/profile/validator/Runner 均保留。

实现：`notes/LOCAL_BUILD_20260905.py`。只允许 `--preflight`（只读非 build 路径）、`--self-test`（纯内存合成测试）、`--build`（独立审查 PASS 后一次新构建）。不运行任何旧冻结内嵌程序，不扩写 V35 或 Host 持久化协议。

精确新路径，均在本项目下；编排审查通过前不探测：

- `build/local-20260905-evidence`
- `build/local-20260905-r0`
- `build/local-20260905-r1`

三者均必须新建成功；已有同名目录/链接一律停止，不复用、删除、清理或尝试后缀。创建 evidence 的结果先在调用方捕获，目录存在后再独占写入 bootstrap 记录。仅一个主编排进程写入；所有审查者只读。若进程结果不明，保留状态且不自动重放，不要求在任意崩溃后同时保证无重复和必然进展。

## 与原验收标准的对应

| 验收 | 新编排保留方式 |
| --- | --- |
| 原文、证明、source/publication locks | 不修改源；三源 SHA-256 精确绑定；编译前后逐次重查原件与根内副本 |
| TeX 工具与依赖 | 固定 publication argv、11 项空环境起始表；原 87 逻辑/86 最终依赖锁；逐次前后校验内容、模式、链接及工具哈希 |
| 隔离与日志 | 两个等长新根，各五个空缓存目录；无 shell、close_fds、stdin 空、固定资源上限；四次 publication 指令；每次独占 intent/stdout/stderr/status/receipt |
| 时序证据 | 保存 R021–R053 的三轮 log/aux/fls 及 bbl/blg 快照；五份根清单；BibTeX 后 fls 不变；无重试或第五次 publication |
| 页数与引用 | 24–28 页证明正文、reference sentinel 与 PDF References 页互证、二十项源/bib/aux/bbl/可见文献编号一致 |
| 错误与警告 | final TeX log 严格拒绝 errors/undefined/overfull/rerun/缺字/字体替代等；保留全部残余 warning/underfull，语义良性判定留给独立产物审查，不自动免除 |
| PDF | 原 PDF1.5、匿名、epoch 时间、letter portrait、嵌入字体、内容锚点、禁止主动内容/内部路径；额外使用本机 PyMuPDF 只读解析压缩对象，不接受 parser repair，不写回 PDF |
| 确定性 | 源/PDF/aux/bbl/blg/log 原字节相等；仅三个 fls 快照允许根前缀→`<ROOT>`；清单只投影已绑定 fls SHA 字段，其他字段不改 |
| 终局 | 新编排先独立审查；构建后另行独立审查实际产物、warning、版面、数学/引用完整性与最终证据。脚本通过不是论文 release-grade PASS |

辅助 PDF 检查在本地使用已安装的 PyMuPDF 1.27.2.3 和 `/usr/bin/pdffonts`，不增加 TeX 输入，不安装软件，不发送 PDF。出版工具仍为锁定 pdfTeX/BibTeX。新增解析器用于读取对象/字体，接口依据 [PyMuPDF Document](https://pymupdf.readthedocs.io/en/latest/document.html) 与 [低层对象/流读取说明](https://pymupdf.readthedocs.io/en/latest/recipes-low-level-interfaces.html)。

使用 `paper-compile` 的编译与产物检查方法；用户已确认的固定四遍命令、严格零 overfull、旧失败保留、匿名本地交付优先于技能通用示例。故不使用 `latexmk -C`、自动安装、额外编译遍数、投稿或清理步骤。

## 实施状态

AUTHOR_DRAFT_PENDING_INDEPENDENT_REVIEW。允许先运行无 build 访问的 preflight/self-test 并修正新草稿；只有独立审查文件明确绑定最终脚本 SHA256 并给出 PASS 后才可调用 `--build`。这不是等待用户再次确认。

后续状态：`PREBUILD_DUAL_REVIEW_PASS_EXECUTION_OPEN`。两位独立 R2 审查均通过，主代理已消费为 `LOCAL_BUILD_20260905_REVIEW.md`，绑定脚本 SHA256 `49fba6fa53a6ecf7f4ebd23b2dca72db2a1079d83437088cf89b0c94e6936a9a`。下一步为本计划的一次实际执行；构建结果仍未证明。

首次审查修正：保留初次两份 FAIL 报告；已针对取消/超时的终止回收与不明状态 HOLD、正常 `file:line:error` header、仅用于 allowlist 的单层 `./` 路径拼写、References 后重复内容锚点增加修正和纯内存回归。PDF 检查器的 17 个确切本机 `.py`/共享库文件以 `66cb425ff3a012c077f5ee1f8b8e7019f8f4d8c471635a2cfc98acdbb3ee6a2b` 汇总哈希绑定，预检和解析前后核查。完整参考文献后缀与版面仍需独立人工式审阅，不将锚点检查当作语义完备性证明。
