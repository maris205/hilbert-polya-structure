# Paper31：完整源 V2 实际审查处置

日期：2026-09-13 UTC。主控：`/root`。
状态：`COMPLETE_SOURCE_ACCEPTED_FOR_FIRST_NATURAL_BUILD / PDF_UNMEASURED`。
本件只处置完整英文源及唯一实际修正，不是论文最终接受；Batch07 仍4/5。

## 1. 真实首次源审查与唯一修正

主控已 FULL 读回 [V1 首次独立 actual 源审查](COMPLETE_SOURCE_ACTUAL_REVIEW_V1_20260913.md)
177行／18603 bytes，SHA `c2f15cd1dbe8ee2ccb3dfe85dfd2ea408b608f3403a38dcb4417063835fa990b`。
其首次亲读全部12源；结论为 `SCOPED_SOURCE_CORRECTION_REQUIRED`，唯一 M1 是完整 lift 被合并归属 P30 §2。
其它完整数学转录、主定理量词与英语叙事没有 required fix。该历史报告及完整 paper/v1 原样保留，不能追记为 V1 PASS。

主控仅复制完整源为 `paper/v2/`，修改引言、§2 与书目三件：

- 区分 JR §2.1 的初值空间／原 lift 描述与 P30 §2 的曲面／polar／complete-fibre 责任。
- 明说 JR 小节的有限域语境；在正文转录已接受 R30 Step1 的全点局部核验，包含三条完整局部式、第四线遗漏点、torus 对角、全几何分层与 étale 同构链。
- 新增真实固定 arXiv:2508.18578v2 条目。没有把有限域原文的同构声明当作本稿全实证明，没有删 terminal、改定义域或加科学假设。

来源核查以 [新增引用补充](LIFT_SOURCE_CITATION_SUPPLEMENT_V1_20260913.md) 62行／5992 bytes、
SHA `680f1016a6caa1b220591e41507b31c4637415202057f700b0adb5d8a024c6cb` 记录，主控 FULL 读回。
主控本人此前实际打开 JR 固定 v2 题录与 HTML §2.1 全部文字，非整篇/PDF；原 DOI open 技术失败不抹去。
新增补充另将官方搜索返回出版元数据与受限正式全文分开。本稿选固定预印本身份，不需要恢复受限入口。
主控本轮实际读 R30 1–160（按前后两段覆盖）与 P30 V4 §2 所需局部式；不重开未变数学包。

## 2. successor 的独立核验与主控接受

同一 fresh 非作者的 [M1 实际 V2 续查](SOURCE_M1_SUCCESSOR_REVIEW_V2_20260913.md)
93行／9156 bytes，SHA `1360aa0267dc69f76ecd3f58c2d56d27fda84b5410cd6edf3c60ef48edc23bfb`，主控已 FULL 读回。
该席亲读全部差分、变化段与上下文、对应 R30/P30 局部原式及完整引用补充；
结论 `M1 CLOSED / PASS`，`required_fixes: []`。
主控采纳“首次完整 V1 实读＋V2 实际差分核验＋其余9件字节不变”的 source PASS；
不把本次局部续查冒称第二次 FULL 全稿，不重新抽正式四门票。

## 3. 完整冻结源与机械复核

当前完整 V2 为12件、2454行／108337 bytes；精确集合见
[源 SHA 清单](SOURCE_V2_20260913.sha256)，12行／1164 bytes，
SHA `9f61d249df26d8997690be71d2d24f5d0f3727e07c4159bc4a78aa66a91cd89f`。
主控已 FULL 读原完整12件，后续完整目录差分及所有变化段也实际读回；9件未变逐字节核同。
V2 的只读机械复核：102唯一 labels、71个被引用 label 均存在；7 cite 与7 bib key恰相等；逐文件环境与非转义花括号平衡。
主文件、宏、字号、纸型、边距、正文/参考文献分界均未变。源停止编辑，生产仅复制此完整版本。

## 4. 下一门及效力边界

制作锁及正文22–30页硬窗保持。本件仅允许进入既定首次完整自然构建，不预授页数、字体、日志收敛、
同源双新根字节确定性、完整 actual PDF 或独立终局完整性 PASS。
首次完整稿 V1 已保存且未经编译；V2 是首次编译之前纠正真实引用接口的 successor。
因此首次生产仍使用未存在的 natural-20260913-r0，第二根 r1 只在第一根完整成功且正文窗实际通过后运行。
普通真实制作失败保留源／现场，最小修正用后续明确新版本和 absent 新根；不试排找页数，不移证，不改锁。
所有动作仅本地，无 CAS／数值／参数阶数枚举、投稿、上传或付费操作。
