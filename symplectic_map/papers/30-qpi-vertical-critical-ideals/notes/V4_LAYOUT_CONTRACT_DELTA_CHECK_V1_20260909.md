# Paper30 V3→V4 两处排版及页数合同补充的有界差异检查

日期：2026-09-09。检查者：/root/p30_vertical_alpha_high_jets_draft_v1。
结论：PASS_SCOPED_LAYOUT_AND_CONTRACT_DELTA；不是完整稿件或 PDF 接受。
作者关系：本人是本稿 §7–8 转写作者，不是 fresh 全文非作者。
本次只检查本人未撰写的 §3／§6 两处 V3→V4 变更及合同补充；
不得把本报告改称 fresh 完整非作者审查、数学重审或独立终局验收。

## 1. 授权与范围

主控本次调度明确传入：用户先收到“仅 Paper30 正文上限 30→40，其他不变”的提案，
紧邻回复以“可以。此外”开始；另提并行要求不撤销该同意。
据此核对已写入的 addendum，不重复询问，也不将旧结果中的待决定快照当作当前否决。
唯一写入文件为本报告；只读源、完整目录 diff、合同和必要日志，不编译、不试排、不测页。

## 2. 实际读取和输入身份

全文读取下列三项控制记录；SHA-256 均为本次实际计算：

| 文件（相对本 notes 目录） | 行数 | SHA-256 |
|---|---:|---|
| PUBLICATION_LOCK_20260909.md | 72 | e07f4bcb20f8aa445b41a5ceccd3d680036700fb63f26b9fc1379870c94573fa |
| PUBLICATION_PAGE_ADDENDUM_V2_20260909.md | 53 | 9cc96e76d8bd22dc7b76a4bb35791279c06fd1b83e24c3a74fe136f895a76380 |
| FIRST_COMPLETE_NATURAL_BUILD_RESULT_V1_20260909.md | 122 | ac86625f44ed62741ceefe84d62c67276f3cb8be5ee71a6edc00492c2375ebf5 |

完整读取 V4 main.tex 62 行及 macros.tex 9 行；两者与 V3 的字节相同。
全文读取 V3/V4 目录的完整 diff -ru 输出：仅两个文件各一个 hunk，无新增／删除源文件。
实际读取 §3 上下文 V3 280–365、V4 280–368，及 §6 上下文 V3 1–95、V4 1–98。
对 V3/V4 全部十一文件逐个计算 SHA-256，并用 cmp -s 独立核对相同／不同状态。
定向读取 r2 work/main.log 550–574 附近两条 overfull 记录；没有通读旧 PDF 或重作页数验收。
该日志 SHA-256 为 1424a5b431c99cc0c303f06d7496320ca4fddb3a01c37f23c2b8352f132f2c8f，与首次结果记录相同。

## 3. 全十一文件身份

路径相对各自 paper/v3/、paper/v4/；“同 V3”表示 cmp 确认逐字节相同，不是仅语义相同。

| 文件 | V3 SHA-256 | V4 SHA-256 |
|---|---|---|
| main.tex | 1d1a47776586fc72aa7041eaaf1098615b4bb1adc373f62546cbf71d6b6679b4 | 同 V3 |
| macros.tex | b4831759010e67ff47811ba1346c0a8aea47d0e2fc1bfa6e3f8312828b6b5dc3 | 同 V3 |
| references.bib | 418530c0bc71f2fbbf5aa0e65b8d2c984c5c68f7fca9dcbb65c2fa84550ab0ba | 同 V3 |
| sections/01-introduction.tex | 9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e | 同 V3 |
| sections/02-surface-pencil.tex | 573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f | 同 V3 |
| sections/03-spectral-jacobian.tex | 011c5415ac5d109c56cea3263ea9cad64db79a7f6102f12676c744bacb065b9b | 38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f |
| sections/04-closed-hasse.tex | 68efcc6780280d7e06c107bc993fe4c431d8131b59f1f4f9e6b874dd96c6000e | 同 V3 |
| sections/05-integral-trace.tex | 925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0 | 同 V3 |
| sections/06-first-layer.tex | f4232d918c4d78bacfc7c7a9dea2fbbe0aa60e634fbf27354d1708e02d84792d | e5ba6462600b04aee4d42f6d3ef85729ee2b3e7f5e6dfead92e37008d36ce392 |
| sections/07-odd-jets.tex | 046f8cf808cc64de570605b316bcb5b0c6970f52492a585f97f97597ae2d74f5 | 同 V3 |
| sections/08-two-jets.tex | 5cfee2a607e6ff1ab52192bb5c9b1a73cef6635c3e5dcfe26aa73fe1192b42a9 | 同 V3 |

## 4. 两处实际差异

§3 V3 第 315 行的行内式 $M(sz)A(z)=A(z)M(z)$ 及紧随的 since $s^r=1$
在 V4 改为同一等式和逗号位于无编号陈列式，后接原来的 since $s^r=1$。
等式、因子顺序、假设及后续谱线丛箭头／循环复合／固定除子差均不变；
该位置对应原日志 9.96825pt overfull（原 §3 313–321 行）。

§6 V3 第 47 行的两个行内式 $H^0(S_A,\mathcal O)=A\langle1\rangle$ 与 $H^{>0}(S_A,\mathcal O)=0$
在 V4 合放一条无编号陈列式，以 \quad\text{and}\quad 连接。
紧随的 for $A=A_2,k$、真实常数截面、系数映射和后续边界复形保持不变；
该位置对应原日志 6.8397pt overfull（原 §6 46–51 行）。
两处只改变数学模式及行间展示，未增删数学项、证明、量词、假设或 label；无编号式不推进公式计数器。
“修复针对正确的既有溢出”可以静态确认；“V4 已消除溢出”仍须实际新构建日志与 PDF 支持。

## 5. 合同及新根边界

Addendum 只将 Paper30 正文窗口改为 22–40；下限 22、参考文献另页另计均不变。
匿名英文、article 11pt、letter、单栏、1 inch、标准间距、完整证明正文及禁止删证明压版等仍有效。
完整实际 PDF 阅读、同源两新根字节确定性、fresh 非作者全文/PDF 审查和随后独立完整性验收均未取消。
main/macros 全文实读及九文件逐字节比较确认本次没有字号／边距／行距、章节、引文或科学范围变化。
原 publication lock 的实际 SHA 与 addendum 所载保留值一致；旧 39>30 失败没有被回写成通过。
2026-09-09 12:51:56 UTC 核对时，旧 natural-20260909-r0/、r2/ 均仍为目录，r2 日志身份亦匹配。
拟用 natural-20260909-r4/、r5/ 当时均不存在；本检查未创建、清理或覆盖任何构建根。
实际创建前仍须复核新根缺席；r5 只在 r4 实际正文窗口通过后依同源协议运行，不由本报告预先启动。

## 6. 有界结论与未授予事项

本次合同增补和 V3→V4 两处排版差异与给定授权一致，无需修改科学陈述或重审未变证明。
可交回主控依既定完整源冻结／生产程序接续；这不是报告作者另授权限或接受 Paper30。
本报告不认定 V4 实测页数、警告消失、PDF 可读性、字节确定性或 fresh 全文审查通过。
本人 §7–8 作者关系继续披露；此有界检查不占用也不替代后续 fresh 非作者完整稿／PDF 验收。
只保存本报告；全文读回并交付终态 SHA 后停写。
