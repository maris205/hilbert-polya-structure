# R5 文档检查与实际执行收据

2026-09-08 UTC。只核查本轮研究文档与三个共享索引；不运行数学
程序、旧认证、PDF 构建或正式 Route-A 评价。此文件是静态检查收据，
不是论文封存清单，也不以校验和替代证明审查。

## 实际检查与范围

19:39 UTC，执行只读文档解析：递归读取本轮目录中的 Markdown，
再加批次 `ADMISSION_DECISIONS.md`、`README.md` 和包外
`CURRENT_RESEARCH_STATE.md`。解析普通 Markdown 行内相对链接，
忽略网络 URL／纯锚点，去掉片段后按所在文件目录解析，并检查
目标存在性；逐行检查尾空白和 Git 冲突标记。没有做全仓库审计、
网络链接可达性或标题锚点正确性认证。

| 实际项目 | 结果 |
| --- | --- |
| 本轮 Markdown 文件 | 19 |
| 连同三个共享索引的检查文件 | 22 |
| 本地行内链接 | 207 |
| 缺失目标 | 0 |
| 行尾空白 | 0 |
| 冲突标记 | 0 |
| 本轮非 Markdown 文件 | 0 |
| `git diff --check` | 退出 0，无输出；tracked 变更检查 |
| `git diff --cached --name-only` | 空，无暂存内容 |

新增未跟踪文件的文本与链接由上述独立静态解析覆盖，不声称
`git diff --check` 自己检查了所有未跟踪文件。此收据填入后只
再检查该收据及最终索引状态，不触发任何数学或旧认证重跑。
本收据不新增行内链接，文件数与链接数保持上述值。

## 数学审查和最终证据一致性

协调者完整读取本轮所有支线证明／处置／来源报告及 GR5 完整
非作者审查；共享状态只人工读回最新变更段，不把历史全文的
程序读取说成人工重新审查所有旧论文。

GR5 的实质数学、来源与准入分别裁决；唯一陪集术语修订 M1 已
由作者修复、非作者回读关闭，协调者亦核对改动行与四份哈希。
最后检查的审查 SHA-256 与其交接值一致：

```text
GR5_REVIEW/REVIEW.md
5f7c71e513fa7259bca24063ddc16fb604078bb07d5ac9d6c3e04592f0fc2236

arithmetic/PROOF_PACKAGE.md
165f262916ae4cebaee51202fabbb9292c942942573c969de40b3bbbe58b46cb

arithmetic/FROZEN_CONTRACTS.md
99d7e2fc892bc62e1fa1eeb507cad8dfdb03386f33469477ba5922f8dda9c981

arithmetic/SOURCE_AUDIT.md
ccd2cc0e57088a70246fe34f53b58143e40c5be8170ffeca644ae8bf97a21a3e

arithmetic/DISPOSITION.md
1980928eb1f84f10503b2b9be1e492223c9ffdb480d84177a105c7723b884d52
```

哈希只核对实际输入字节，不是数学正确性的来源。Vieta 短引理的
协作贡献与此前辅助证明的限定非作者核查分别标记，不混作原全
atlas 准入审查。所有数学程序执行为 0，全批累计仍为 3。

## Git 和未执行事项

本地 HEAD 保持 `2895b07238d4cef2ed35faaad251e4cfceb08ec1`。
实际 `git status --short --untracked-files=normal` 仍只显示
`CURRENT_RESEARCH_STATE.md` 为 tracked 修改，本批与同八个继承
目录未跟踪；本轮只写本批和当前状态，没有改写继承目录。
未暂存、提交、推送、fetch、整合远端或核验最新远端状态。

没有新稿、TeX/PDF、正式 Route-A 评价、封存、GPU、付费模型、
外部稿件上传或旧认证重跑。当前是 3/5 项准入合同而非三篇成稿，
五篇交付尚未完成。`NO_BAD_EULER_OR_ROOT_NUMBER` 保持。
