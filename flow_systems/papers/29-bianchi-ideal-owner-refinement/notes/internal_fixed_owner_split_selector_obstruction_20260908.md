# P29 内部研究：真实本原 owner 上的条件分裂选择障碍

记录日期：2026-09-08 UTC。本轮按 P29–P33 五篇一整轮推进内部论证；不修订现稿，不执行 owner 普查、候选机制或性能实验，不改变 Gate M／Q、Route 或正式完整性状态。

本篇新增两项可直接核对的证明：一个已有精确矩阵在**完整 level-(3) 群内本原**；在它对应的真实 owner 上，任何同时要求 Gaussian 共轭等变、且选择归一化迹判别式的一个素理想因子的规则都不可能成立。第二项有两个额外前提，绝不是“一个字面素理想作为值域普遍不可能”。

## 1. 对象、输入和新增假设的位置

沿用 [P29 现稿 B0009、B0058–B0061][current] 及其继承的 [P24 群定义][group]：

\[
\Gamma(3)=\{A\in\operatorname{SL}_2(\mathbb Z[i]):A\equiv I\pmod3\},
\qquad \bar\Gamma(3)\subset\operatorname{PSL}_2(\mathbb C).
\]

时钟为双曲弧长，owner 是该群的本原 loxodromic 共轭类再模取逆；群幂是重复。这里不把旧 elementary-generator 有限词球误称为完整群或全体 owner。

旧 [P24 精确见证定义][witness] 已包含

\[
A=\begin{pmatrix}1&3\\3&10\end{pmatrix}
=\begin{pmatrix}1&0\\3&1\end{pmatrix}
 \begin{pmatrix}1&3\\0&1\end{pmatrix}.
\tag{1}
\]

本轮只读取该常量及群定义，没有导入或运行旧脚本，也不重新认证其历史输出。本轮独立的纸面证明不依赖旧函数名中出现的 `owner` 字样。

设 \(X\) 为完整群的本原无向 owner 集，\(\sigma\) 为逐项 Gaussian 共轭。由于它保持群、共轭、取逆和幂关系，\(\sigma\) 在 \(X\) 上定义了一个对合。\(M:X\to\mathcal P\) 的值域 \(\mathcal P\) 是非零 Gaussian 素理想。

必须区分：

- **继承的基本关系：** 群共轭、取逆和重复不改变 owner 标签。
- **本轮额外的条件 E：** \(M(\sigma x)=\overline{M(x)}\)，即 Gaussian 共轭等变。
- **本轮额外的条件 D：** 对本原代表 \(A_x\)，\(M(x)\) 是非零 \(D_9(A_x)=(\operatorname{tr}(A_x)^2-4)/9\) 的一个素理想因子。

现稿只要求记录 Gaussian 共轭怎样作用，并未把 E 或 D 自动规定为每个可能机制的通用定律。下面证明只排除同时满足 E、D 的选择规则；不把这两个前提静默写入冻结协议。

## 2. level-(3) 迹约束与本原性证书

任取 \(B=I+3C\in\Gamma(3)\)。二维行列式展开给

\[
1=\det(I+3C)=1+3\operatorname{tr}C+9\det C,
\qquad \operatorname{tr}B=2-9\det C\in2+9\mathbb Z[i].
\tag{2}
\]

如果 \(\operatorname{tr}B\ne2\)，则反三角不等式立即给出

\[
|\operatorname{tr}B|\ge7.
\tag{3}
\]

对 (1)，\(\det A=1\)、\(A\equiv I\pmod3\)、\(\operatorname{tr}A=11\)。两个特征值是

\[
\lambda=\frac{11+\sqrt{117}}2>1,
\quad \lambda^{-1}=\frac{11-\sqrt{117}}2,
\quad 1<\lambda<11.
\tag{4}
\]

因此它是 loxodromic，旋转角为零。将轴的端点送到 \(0,\infty\) 后，其作用是尺度 \(\lambda^2\) 的伸缩，轴上弧长积分 \(\int_1^{\lambda^2}dy/y\) 给

\[
\ell_A=2\log\lambda=2\operatorname{arcosh}(11/2)>0.
\tag{5}
\]

**命题 1。** \([A]\) 在 \(\bar\Gamma(3)\) 中不是非平凡真幂。

证明：若存在 \(B\in\Gamma(3)\)、\(m\ge2\) 使 \([B]^m=[A]\)，则 \(B^m=\pm A\)。因为 \(-I\not\equiv I\pmod3\)，负号被排除，故 \(B^m=A\)。\(B\) 的特征值模长为 \(r,r^{-1}\)，其中

\[
1<r=\lambda^{1/m}\le\sqrt\lambda<\sqrt{11}.
\]

若 \(\operatorname{tr}B=2\)，特征值全为 1，其任何幂不可能等于有特征值 \(\lambda>1\) 的 \(A\)。否则 (3) 成立，但

\[
7\le|\operatorname{tr}B|\le r+r^{-1}
<\sqrt{11}+1<5,
\]

矛盾。此论证没有假定根矩阵为实矩阵，也没有用有限词球搜不到根来代替完整群中的排除。\(\square\)

所以按继承的 owner 定义，\(A\) 确定一个真实本原无向 owner \(x_A\)，其本原周期为 (5)。该结论只处理这一明确元素；它没有给全体冻结矩阵行建立 maximal-root 算法或完成 Gate Q。

## 3. 判别式只有一对被交换的素理想因子

由 (1) 直接得到

\[
D_9(A)=\frac{11^2-4}{9}=13
=(3+2i)(3-2i).
\tag{6}
\]

令 \(\mathfrak p_+=(3+2i)\)、\(\mathfrak p_-=(3-2i)\)。下面不用任何数值分解程序即可证它们是不同的素理想。

将 \(\mathbb Z[i]\) 看作秩二整数格。乘以 \(3+2i\) 的整数矩阵为
\(\left(\begin{smallmatrix}3&-2\\2&3\end{smallmatrix}\right)\)，行列式为 13，故 \(\mathfrak p_+\) 的指数为 13。环同态

\[
\phi_+:\mathbb Z[i]\longrightarrow\mathbb F_{13},\qquad
\phi_+(i)=5
\]

合法，因为 \(5^2\equiv-1\pmod{13}\)，且 \(3+2\cdot5=13\)。其核和 \(\mathfrak p_+\) 同为指数 13，故相等。类似地，\(\phi_-(i)=-5\) 的核是 \(\mathfrak p_-\)。两个商都是域，因此两个理想均为素理想。

它们不相同：\(\phi_+(3-2i)=3-10\not\equiv0\pmod{13}\)。并且

\[
\overline{\mathfrak p_+}=\mathfrak p_-,\qquad
\overline{\mathfrak p_-}=\mathfrak p_+.
\tag{7}
\]

任一含有 13 的非零素理想必须含有 (6) 的一个因子，从而包含 \(\mathfrak p_+\) 或 \(\mathfrak p_-\)；两者已是极大理想，因此该素理想就是其中之一。这也证明 (6) 没有遗漏可选的第三个素理想分支。

## 4. 不动点上的等变选择障碍

**引理 2（对合选择的必要条件）。** 设对合 \(\sigma\) 作用于 \(X,Y\)。若 \(M:X\to Y\) 等变且 \(\sigma x=x\)，则 \(M(x)\) 必须是 \(Y\) 中的 \(\sigma\) 不动点。

证明只有一个等式：\(M(x)=M(\sigma x)=\sigma M(x)\)。若另有允许值集合 \(S(x)\subset Y\)，则只要 \(S(x)\) 没有不动点，就不存在满足 \(M(x)\in S(x)\) 的等变选择。\(\square\)

**命题 3（真实 owner 上的条件障碍）。** 在包含 \(x_A\) 的 \(\sigma\)-稳定 owner 域上，不存在同时满足 E 和 D 的单素理想选择规则。

证明：矩阵 \(A\) 为实矩阵，所以 \(\sigma x_A=x_A\)，这里甚至不需要找共轭子或取逆来识别 owner。由条件 D 和第 3 节，\(M(x_A)\) 只能是 \(\mathfrak p_+\) 或 \(\mathfrak p_-\)。它们被 \(\sigma\) 交换且不相等，与引理 2 矛盾。\(\square\)

这是对整个明列规则类别的数学排除，而不是旧合成 fixture 的一次观察。新点在于其输入已落实到完整群内的一个真实本原元素，且分裂因子、共轭不动点和本原性均在本笔记给出了精确证明。

注意这不是现稿 `SPLIT_IDEAL_CODOMAIN_OBSTRUCTION` 终态的实际运行：没有登记候选公式、调用 Gate M validator 或生成正式 receipt；这里的失败原因是额外的 Gaussian 共轭等变条件，不应自动冒称为现稿优先规则中的“取逆时分支失败”。

## 5. 为什么不能扩大成普遍不可能

两个反向例子精确显示缺少哪条前提会使证明失效。

1. **去掉 D。** 常值 \(M(x)=(3)\) 返回素理想：\(\mathbb Z[i]/(3)\cong\mathbb F_3[T]/(T^2+1)\) 为域，因为 \(T^2+1\) 在 \(\mathbb F_3\) 无根。它满足所有 owner 关系及 E，但在 \(x_A\) 上不是 (13) 的素因子。
2. **去掉 E。** 只在单 owner 域 \(\{x_A\}\) 上取 \(M(x_A)=\mathfrak p_+\)，它满足 D 和 owner 代表无关性，却不满足 E。取逆不改变这个赋值；“无向”本身不强迫交换 Gaussian 共轭素理想。

这些只是检验逻辑量词的反例，不是合格的算术 owner 机制，不进入候选登记或碰撞性能分析。尤其常值标签不能证明原项目所追求的算术信息或特异性。

若改为返回 \(\{\mathfrak p_+,\mathfrak p_-\}\)，确实消除了这一个不动点障碍，但那已改变冻结值域。本轮不实施这种变更，也不推出更宽值域已经存在全局 owner 法则。

## 6. 本轮产物与剩余义务

| 本轮闭合的数学问题 | 未被闭合的问题 |
| --- | --- |
| 精确矩阵 (1) 在完整 level-(3) 群内本原，给出精确物理周期 | 冻结有限行集的完整本原根、共轭、取逆商及终止算法 |
| 两个素因子是唯一分支且被 Gaussian 共轭交换 | 实际登记机制是否应当、是否能够满足 E 或 D |
| E+D 规则在真实不动 owner 上不可能同时成立 | 原 Gate M 全部候选、任意单素理想机制或全值域的普遍障碍 |

全部新增结论来自上述明列代数证明；本篇使用本地对象、现稿与旧常量，核心代数事实在上文自证。主线程曾做普通公开来源检索，但没有将搜索摘要作为证明或引用输入；没有运行科学程序或调用外部代数服务。未更新旧稿对当时研究状态的叙述，未把本轮增量回填为历史已完成事项。没有文献新颖性判定、数值长度认证、性能结果或正式 Route 评估。

[current]: stage4_prime_revision_round6.tex
[group]: ../../24-bianchi-holonomy-flow/paper/manuscript.tex
[witness]: ../../24-bianchi-holonomy-flow/code/round7_trace_discriminant.py
