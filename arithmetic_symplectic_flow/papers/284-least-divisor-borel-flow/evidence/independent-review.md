# 284 独立内部复核：原卡、主稿与最终反方检查

**Candidate ID:** ANG-20260920-LDB01  
**Status:** DECLARED ALL-POINT CLOCK; DUPLICATE LOG-TWO PACKETS — STOP / FORK  
**Verdict:** 三个有界检查点完成；无待修改的数学阻断项。支持按冻结规则停止目标晋升，不支持删点、改时钟或扩大普查。

## 1. 输入、顺序与权限

| 实际读取输入 | SHA-256 |
|---|---|
| 原始 version-1 冻结卡 | 5e3f7d52e5d9b074004e9b487aaad296dd1226868021b95a86d489ed5b619f7f |
| 完整比较的主文，267 行 | dafaa17059606aa80614064ce042006753403e888ecec7e2f6533c930d0ddacd |

检查点 1 完整读取原卡后独立推导 owner、clock、0/1 稳定子与预列控制，先向主控发送结果，随后才读取主稿。卡片如事后追加 outcome，本报告仍绑定上述原始冻结字节，不把追加结论当作原卡证据。

检查点 2 全文比较主稿；检查点 3 专门尝试实际词、null branch、clock 与 packet 的反例。未提出需要作者修改的数学问题；没有为了构造批评而改变判据。

本审查者唯一写入本报告。卡、主文、其他包、companions 与注册表只读；没有数值运行、周期 census、外部检索或新候选推导。

## 2. 检查点 1：完整 Borel owner 与声明的时钟

原卡是完整 \(K=\widehat{\mathbb Z}\)，不是嵌入整数集合，也不是删去 null states 的测度商。全部正逆词只来自当前最小整除分支及余支平移。

若 \(d\) 合数，某个 \(2\le e<d\) 整除 \(d\)，故 \(dK\subset eK\) 而 \(B_d=\varnothing\)。素数 \(p\) 本身属于 \(B_p\)，故非空分支恰为素数分支；这是从原整数索引规则推出，而非预先换成 prime list。

更明确地，令 \(C_p=K\setminus\bigcup_{\ell<p,\ \ell\ {\rm prime}}\ell K\)，则 \(B_p=pC_p\)。它们是 clopen；除以 \(p\) 与其严格逆在实际像 \(C_p\) 上互逆。乘整数的单射性由 \(dx=0\bmod dm\Rightarrow x=0\bmod m\) 得到，不需把 \(K\) 当成整环。

\(B_2=2K\) 的除二分支已覆盖整个 \(K\)，所以全更新 onto。余集 \(U=K^\times\) 闭、非空、Haar-null；其严格平移像为 \(U+1\)。它不是开 chart。

零测结论直接来自有限 CRT：\(h(U)\le\prod_{p\le N}(1-1/p)\)，该乘积倒数至少为 \(\sum_{n\le N}1/n\)，故趋于无穷。没有删除 \(1,-1\) 等余支种子。

每个有限词是 Borel 子集间的严格 Borel 同构；同一 affine label 的实际域取其所有词域的可数并。由此箭头空间是可数 label 所标记的 \(K\) 副本中的 Borel 子集，源纤维可数，复合与逆均 Borel。

按 label 加 source 认箭头保留了实际 isotropy，同时去掉额外 word-lag；它没有加入同一 label 最大域上尚未由词生成的箭头，也没有做 germ quotient。

对一个出现于实际箭头的 label，写 \(q=A/N>0,\ r=B/N\)，并置 \(g=\gcd(A,N)\)。最大域非空当且仅当 \(g\mid B\)；此时可取整数 \(x_0,y_0\) 使

\[
D=x_0+(N/g)K,\qquad qD+r=y_0+(A/g)K.
\]

由任意 Borel 集的整数倍 Haar 缩放，得到

\[
h(qE+r)=q^{-1}h(E),\qquad E\subset D.
\]

非空最大域有正测度，故常数 IMAGE factor 唯一；换共同分母不改 \(q^{-1}\)。复合斜率相乘，故声明的全点 cocycle 是 \(c=\log q\)。

限制该版本到实际词域不增加箭头。特别地，除 \(p\) 的 clock 是 \(-\log p\)，余支平移的声明值是 0；后者不是由 null 实际域上的等式 \(0=J\,0\) 唯一确定。

完整 owner 的 Haar null-set class 被所有生成器及其逆保持；可数词给出 nonsingular Borel groupoid。这个事实与“特定 null 点上 clock 必然唯一”是两回事。

扩张箭头为 \((x,u)\mapsto(qx+r,u+\log q)\)。全部实参数平移给出完整联合 Borel 群胚作用，对象上的实坐标平移连续；没有推出 coarse quotient 的 standard Borel、Hausdorff 或 circle-embedding 结论。

## 3. 原卡的决定性稳定子检查

主审的 raw 证明先从整数控制图出发：正逆分支保留嵌入整数；0 的控制分量围绕除二自环，1 的控制分量围绕 \(1\to2\to1\)。离环最深处的有限闭路可消去严格回溯，余下仅为环幂。这是控制两点全部有限词的手段，不是其他种子的返回分类。

同模型辅助审查另给出更经济的约化：相邻“逆分支、正分支”必严格相消，因为中间点只有一个选定正分支。反复消去得“正向 \(m\) 步、逆向 \(k\) 步”。

因此任意实际箭头 \(x\to y\) 的 label 必为

\[
A_k(y)^{-1}A_m(x),\qquad T^m x=T^k y.
\]

反过来，匹配的实际前缀确实给出这样的箭头。消去只证明当前源点处 label 相等，不把形式简化后的较大域加入 owner；不同前缀长度也不留下额外 lag。

在 0 上，\(A_m(0)(z)=2^{-m}z\)，故完整稳定子恰为

\[
G_0^0=\{(2^j,0,0):j\in\mathbb Z\}.
\]

在 1 上令 \(P(z)=(z+1)/2\)。偶数前缀为 \(P^k\)，奇数前缀为 \((z\mapsto z+1)\circ P^k\)。共同端点强迫两前缀同奇偶，所以

\[
G_1^1=\{(2^j,1-2^j,1):j\in\mathbb Z\}.
\]

两个集合中的每个 label 都可由实际环或严格逆环实现；不是仅从可见环推测整个稳定子。平移边 \(1\to2\) 与除二边 \(2\to1\) 的 affine labels 不互为逆，不能误消成恒等。

两点完整时间返回群均为 \((\log2)\mathbb Z\)，最小正时间严格为 \(\log2\)，正重复为 \(k\log2\)。clock 在各自稳定子上单射，故固定对象的 extension isotropy 均平凡，而 source isotropy 均为无限循环群。

0 的前向尾只含 0，1 的前向尾只含 1、2，二者不相交。共同尾判据排除全部实际连接箭头；实时间平移不改变这一障碍，故这是两个不同 primitive packets，不是重复或不同相位。

预列控制也闭合：实际平移 \(-1\to0\) 属第一个包；任意嵌入素数的实际除法 \(p\to1\) 属第二个包。共轭传递完整 isotropy 的 clock image，故素数点时间群仍为 \((\log2)\mathbb Z\)；连接箭头的 \(-\log p\) 不是它的闭返回时间。

这已经触发停止规则。只证明 **AT LEAST TWO** 不兼容的 log-two primitives；没有声称全局恰好两个包，也没有继续分类其他非整数种子。

## 4. 检查点 2：与完整主稿的比较

主文 Lemmas 1/4、Propositions 2/3 与 Theorem 5 的结果均符合上述 raw 推导。主文选择共同尾 lemma 组织完整性证明，而非扩展整数图分类，符合快速 gate 的范围。

复合校准已具体核对：对 \(x\to y\to z\) 的两种共同尾表示，把 \(y\) 处的两前缀延长到二者最大长度，同时分别延长 \(x,z\) 端的对应实际尾段。公共中间 affine label 相消，给出新共同尾表示；所有延长均沿实际已选分支。

主文没有把 label 商误作全部 affine action，没有把时钟方向颠倒，没有把 null 分支的声明值称为 a.e. 强迫值，也没有把固定对象 isotropy 与实际时间稳定子混同。

全文比较未发现需修正项。绑定的 267 行主文未因本审查要求发生修订。

## 5. 检查点 3：反方边界与限制

- 最强质疑是 clock 在实际 null branch 上并非内在唯一。卡与稿已明示额外最大域规则；它使本 owner 定义完整，但不关闭 naturalness。反方不能据此称对象“未定义”，也不能暗中换 clock 挽救目标。
- 零点包可能被认为是退化附加物，但完整源明确保留零点；删除它属于新 owner。素数输入全进入同一包的独立控制也仍成立。
- 有可见环并不自动证明最小时间；此处全部有限词的约化及完整稳定子排除了额外更小返回。
- 相同 \(\log2\) 不等于同一包；连接箭头的 \(\log p\) 也不等于 primitive period。稿件对两种混淆均作了明确排除。
- 本结论不否定其他 Borel 算术动力学、其他 all-point 规则或未准入 scout；没有替这些对象证明新定理。
- 保留未分类种子、null strata、自然性与 PROVES_TOO_MUCH 的开放边界。不添加粗拓扑、解析对象、T3 或形式 Route 信用。

## 6. 方法披露与冻结结论

采用 ARS academic-research-suite 三检查点。主审在主稿前完成 raw 推导，但与主控共享研究上下文；同模型辅助 affine_stabilizer_scope 仅读原卡，核对 0/1 全词稳定子及预列控制，未读主稿、未写文件、未做其他种子 census。

辅助的共同尾约化在主审读稿前返回并告知主控；主控稿中的共同尾证明也作了本报告的独立复合校准。这种执行顺序不被包装为不同模型误差结构或盲的外部同行评审。

本报告是内部同模型数学复核，非外部 peer review、机器形式验证或全局分类认证。全源／实际箭头／声明时钟的同对象账本保持完整。

最终维持 **STOP / FORK**：重复 primitive log-two packets 已否定单包目标；不更改规则或扩大普查。T3 未供应／未开展，经典 A0/A1/A2 不适用，formal coordinates UNASSIGNED，Route B NOT INVOKED；241/242 未触碰。
