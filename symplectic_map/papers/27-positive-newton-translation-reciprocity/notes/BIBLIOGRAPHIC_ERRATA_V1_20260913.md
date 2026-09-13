# Paper27：冻结接受版本的三条书目作者名勘误

日期：2026-09-13 UTC。记录者：`/root`。
状态：`LOCAL_COMPANION_ERRATA / THREE_AUTHOR_FIELDS_CORRECTED_IN_RECORD / FROZEN_PDF_UNCHANGED`。
本件随Paper27本地交付阅读；不是新的论文版本、重新编译或追溯修改原验收。

## 1. 适用的精确版本

- [接受PDF](../build/final-20260905-r0/main.pdf)及其r1同字节副本：SHA-256 `ab195a2b49012e9b4b320ddbabffd9666c076b37b09a8b9dc20c400dd266a5b4`。
- 两根源 `references.bib`：SHA-256 `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5`。
- [原本地接受](LOCAL_ACCEPTANCE_20260905.md)：SHA-256 `c74faa836e06b700b5b41ed40df50435100adb25226b034f4e2bf101db2828ce`，保持原件。

## 2. 正确作者信息

统一跨论文审计的科学席与交付席分别发现P27/P28共用条目的作者名不一致。主控随后定点核验公开一手元数据，确认下表是P27作者字段笔误，而非两篇不同文献。

| P27键／PDF参考号 | 冻结书目中的作者字段 | 应读为 | 不变的文献身份与核验来源 |
|---|---|---|---|
| `hasselblatt_propp_2007`／[14] | B. Hasselblatt and T. Propp | Boris Hasselblatt and James Propp；缩写B. Hasselblatt and J. Propp | *Degree-growth of monomial maps*，DOI `10.1017/S0143385707000168`；[作者arXiv记录，实际v5](https://arxiv.org/abs/math/0604521v5) |
| `janeczko_jelonek_2008`／[15] | J. Janeczko and Z. Jelonek | Stanisław Janeczko and Zbigniew Jelonek；缩写S. Janeczko and Z. Jelonek | *Polynomial symplectomorphisms*，DOI `10.1112/blms/bdm112`；[作者学校所存论文首页](https://pages.mini.pw.edu.pl/~janeczkos/JJ3.pdf)、[本人发表目录第59项](https://pages.mini.pw.edu.pl/~janeczkos/pub1.htm) |
| `shao_sun_2025`／[19] | Y. Shao and Y. Sun | Enbo Shao and Xiaosong Sun；缩写E. Shao and X. Sun | *Dynamical degrees of affine-triangular automorphisms in dimension four*；[arXiv:2509.14584v1作者记录](https://arxiv.org/abs/2509.14584v1) |

本表只纠正上述三条author字段，标题、DOI／arXiv标识、文内指向及引用对象不改变；没有增加、删除或更换参考文献。
主控实际读P27相应bib条目与main.bbl、P28对应条目，以及P27正文§2的引用语境。三条均用于相邻研究定位，不是主定理必要证明的外部黑箱。
独立科学席负责跨文语境判断；本件的外部作者信息核验由主控承担，不倒签为两席亲读来源。

## 3. 核验与效力边界

本次只针对新发现的三条差异作三项定向检索，打开两个arXiv身份页及作者学校目录／PDF。
实际消费范围：Hasselblatt–Propp身份页标题与作者行（该入口实际为v5）；Shao–Sun固定v1身份页标题与作者行；Janeczko本人目录第59项及九页论文的第1页题名、DOI和作者文字。
这些均为书目元数据核验，不称三篇文献全文阅读、新一轮查新或数学证明审查；未读正文与旧来源缺口不改变。

三条错误是已确认且应披露的书目问题，不称PDF“无任何瑕疵”。它们不改变五篇定理、组合内独立性、PDF／源字节身份、页窗或已确认的本地恢复合同。
本次通过本附属勘误准确提供正确作者信息；冻结PDF中原字母仍然存在，没有虚称已嵌入修正。
按P27现有冻结／不再编译边界，不修改旧源、旧锁、旧接受记录、失败或构建树；任何将本表嵌入新PDF的未来工作都需另有适用的后继制作授权。
这不是当前批次新增科学必修项或启动后继构建的请求。当前交付为接受PDF连同本勘误，无投稿、上传或其它外部效力。
