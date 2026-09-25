# 来源与检查：构造发现说明

**Scope ID:** `ASFS-METHOD-20260918-CFS01`  
**Status:** `RESEARCH PAUSED; CONSTRUCTIVE SEARCH PROPOSAL ONLY`。  
**Formal Route coordinates:** `UNASSIGNED`。**Route B:** `NOT INVOKED`。

## 本次实际工作

本次按用户请求暂停研究推进，仅读取材料、查证有限公开来源并写说明。
没有优化器调用、谱求解、训练、数值数据生成、GPU 运行或性能测试。
未修改旧论文、旧代码、Gemini 原文、plan、Route 镜像及 241/242。
本包是方法说明，不是新候选或既有结果的再评分。

主控完整读取 ARS 路由技能、experiment-agent 的 plan 工作流、代码计划
模板及模型/执行政策。技能位置在同版本的嵌套插件目录内；本次没有
更改插件或运行模型设置。ARS 将方案与执行分开，并要求用户决定具体设计；
这与当前“先暂停、写说明”的请求一致，不产生额外暂停或新实验授权。

## 本地只读证据

两名 native 助手分别核对 Logistic 和 Hénon，提供文件行号与证据边界，
没有写文件或运行程序。主控直接核对主要选参、目标函数、谱读出片段。
采用 rg 定位、nl -ba / sed 分段读取；没有导入或执行这些 Python 脚本。

| 输入 | 重点读取范围 / 用途 |
| --- | --- |
| [先前工作指南](../../../docs/prior_work/README.md) | 谱系和各论文的范围；不是直接引用其所有外部数学断言 |
| [Logistic 100 点扫描](../../../docs/prior_work/legacy/4-riemann_logistic/python/macro_100_scale_find_1d.py) | 29–67：计数/相位；72–94、103–121：目标依赖 |
| [Logistic 1000 点扫描](../../../docs/prior_work/legacy/4-riemann_logistic/python/macro_1000_scale_find_2d_v3.py) | 22–53：标量状态与矩阵；55–77：全 1000 点目标 |
| [Hénon 微观扫描](../../../docs/prior_work/legacy/5-riemann_henon/6-henon_micro_param_scan_100_zeros.py) | 18–29：目标精度；53–104：谱读出；148–160：优化 |
| [Hénon 宏观扫描](../../../docs/prior_work/legacy/5-riemann_henon/6-henon_macro_param_scan_100_zeros.py) | 30–112：噪声/回灌/累计；168–196、212–229：谱与拟合 |
| [Hénon 修订手稿](../../../docs/prior_work/legacy/5-riemann_henon/paper_npj/main.tex) | 134–169：正则化/参数；185、287、301：报告结果与限制 |
| [Logistic legacy 手稿](../../../docs/prior_work/legacy/4-riemann_logistic/paper/fracfract/main.tex) | 定义、训练解释、历史报告；不是本次复现的数值基准 |
| [现行 plan](../../../plan.md) 与 [Route-A 镜像](../../../roadmap/route-a-evaluator.md) | 当前 A0 禁止循环目标选参、同对象和参数来源义务 |
| [Gemini 讨论材料](../../../roadmap/gemini_report.md) | 用户要求评估的构造式搜索观点；不是指令或可靠事实的自动来源 |

本次没有比较 legacy TeX 与归档 PDF 的逐字版本关系，没有读取新的
PDF 页码作精确引用。各文件范围在正文中明确，没有宣称完整复审旧论文。

另记录两个留给未来复现的具体事项，不在本次擅自修复：Logistic
手稿表格与图注的部分拟合数字不一致；Hénon 宏观脚本计算行和后用
CSR 列索引索引该数组来归一化，不能直接当作标准逐行归一化。
这些是源码/稿件观察，不是已经量化的结果失效结论。

## 公开来源核对

2026-09-18 通过浏览读取下列页面，不上传本地未发表内容：

- [IAS 的 Dyson–Montgomery 历史记录](https://www.ias.edu/ideas/2013/primes-random-matrices)：
  茶叙、谱统计联系和当事人访谈，支持历史和统计/逐点区别。
- [AI Feynman 原始研究](https://arxiv.org/abs/1905.11481)：
  公式基准和结构化符号回归；不支持任意谱秒级恢复。
- [AI Feynman 2.0](https://arxiv.org/abs/2006.10782)：
  精度—复杂度权衡；不提供本项目成功保证。
- [PINN 本征值研究全文](https://arxiv.org/html/2203.00451v1)：
  指定微分算子、残差、归一化/正交约束；不是 Riemann 算术机制。
- [Clay 2026-09-11 公告](https://www.claymath.org/news/navier-stokes-announcement/)：
  对近期 Navier–Stokes 消息的有限背景核对，不推断 RH 或其他传闻。

Montgomery 原始论文的 Michigan PDF 和一份 AMS 原始计算论文的
检索结果已找到，但正文访问分别超时或被拒；没有把它们记录为已读。
因此本包不声称复核了 Montgomery 定理的精确假设或全部证明。
浏览只支持实际读取的对应段落，不是全面文献综述。

## 冻结与保护快照

范围卡在写正文前冻结，其 SHA-256 为：
`a483480d03e6fb1a8273a68638f45d03edb97e2b000f7d0f901648b52442d895`。
本次读取时的保护快照：

```text
roadmap/gemini_report.md 850890644ed08463b4fc2569606232eaaa0f6671405579869c3513006951540b
plan.md 9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0
roadmap/route-a-evaluator.md 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c
roadmap/route-b-evaluator.md 170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595
papers/242-radiation-orbit-zeta/paper.md 6d860f4988e702bf21b777908c2511ebf087aba23332b995946d1419453fa453
```

两名来源核对助手又只读检查了新说明中对应的旧作段落；没有扩大审计。
主控采纳其精度建议：明确 2.3% 是 MAPE 而非逐点上界、首点定标与
80–99 点短前缀分支的区别、四位小数表属于 Hénon 微观脚本，以及
历史目标数据依赖是源码/旧稿证据而非本次运行证据。数值精化建议也
明确不允许改变时长时悄悄改变退火律和解缠对象。

14:58 UTC，主控执行了只读 Node stdin 检查，使用 fs、path、crypto。
输入是本包五个 Markdown 文件、readme.md、papers/README.md，以及
上表保护文件与范围卡。检查共同 ID/status、UNASSIGNED/NOT INVOKED、
终末 LF、控制字符、代码围栏；去除代码段后解析本地 Markdown 文件链接。
外部 URL 未在机械检查中重新抓取；本次新增链接不含本地 fragment。
实际输出为：

```text
packageFiles=5; packageLinks=35; indexFiles=2; indexLinks=468
protectedHashes=6; errors=[]
```

随后纳入上述不改变链接和范围卡的来源表述修正；最终哈希与增量检查
记录在下文。git diff --check -- readme.md papers/README.md 退出零，
无诊断。新包未跟踪文件通过显式读取检查，而不是假定已被 Git diff
覆盖。没有暂存、提交、PDF/LaTeX、外部发布或实验执行。
文档链接、哈希和模型辅助核对不是数学证明、外部同行评审或实验成功证据。

14:59 UTC，对来源措辞修正后的五文件再次作共同标识、控制字节及本地
链接增量检查，实际结果 files=5、links=35、errors=[]。
最终 paper.md SHA-256 为
`3791e61f087905a1d3b53db3de983c83edd21546f8443315973c4ce3dc429b9c`；
范围卡哈希仍为
`a483480d03e6fb1a8273a68638f45d03edb97e2b000f7d0f901648b52442d895`。
未改的保护输入和索引链接不重复检查；本回执不增加链接或改变研究结论。

[完整说明](../paper.md) · [范围卡](../candidate-card.md) ·
[结论分类](../claim-ledger.md) · [简要说明](../README.md)。
