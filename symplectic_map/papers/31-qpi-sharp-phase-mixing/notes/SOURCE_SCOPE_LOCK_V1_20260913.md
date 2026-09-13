# Paper31 source scope lock V1

日期：2026-09-13。状态：`SCIENTIFIC_SCOPE_LOCKED_AFTER_FORMAL_ADMISSION`。
题名：*Sharp phase mixing for the autonomous q-Painlevé I map*。
唯一中心：原完整实曲面上、逐连通圆中心化的 sharp 确定性相关渐近。
`route_applicability: NOT_APPLICABLE`。纯数学、本地匿名制作；不声称正文或 PDF 已完成。

## 1. 同一已准入输入

以下科学文件保持冻结；本锁不回写原文件头的历史 pending。

| 入口 | 相对路径 | SHA-256 |
|---|---|---|
| 完整正式双席处置 | [formal disposition](../../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_CANDIDATE_DISPOSITION_V1_20260913.md) | `8693108fec4c8aa35310d40fd86c19e36429f79a1f46f225b2415e97f93e5ef7` |
| 完整候选与必要证明责任 | [candidate brief](../../../docs/research-batch07/PAPER31_QPI_Q2_COMPLETE_CANDIDATE_BRIEF_V1_20260913.md) | `2fc821378e667a068240518489a16f64e6c39661c277c530d204dede9940a1e9` |
| 共同38件实际输入及来源范围 | [input manifest](../../../docs/research-batch07/PAPER31_QPI_Q2_FORMAL_REVIEW_INPUT_MANIFEST_V1_20260913.md) | `f9ad246e2bbd62b9b8b495192bb24f166dc49c6e970c6dc13a2bf61829e9be2a` |
| 完整数学接受 | [mathematical disposition](../../../docs/research-batch07/PAPER31_QPI_Q2_DECAY_MATHEMATICS_DISPOSITION_V1_20260913.md) | `2ab0be2cf587012face38cbddf36f59cad6677c7d7441a2758b45c8a89e01d7f` |
| 准确系数与完整定理 | [G](../../../docs/research-batch07/PAPER31_QPI_Q2_GLOBAL_DECAY_PROOF_V1_20260913.md) | `48fff63450138a788e4442c7b94c90e454eeebee2c1960afd895d15577c0cf6f` |

两个 fresh 非作者分别完整四门 PASS；本锁只落实其已接受的科学范围，不重评或扩张之。
下列 M/N/K/E/G、GEO/B/MID/UP/INF/TW/PF 和旧原模型段的准确路径、整件身份及实际范围以共同清单为准。
清单中的接受报告和来源账用于溯源，不作为正文证明的替代引用。

## 2. 原对象与约定

固定任意实参数 $T>0$，保留原八中心曲面 $U_T=S_T\setminus D$ 的完整实点集、四条 terminal 及原 proper 能量映射。
原公共图中

$$F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\quad
h=-x+y+x/y-T/x,\quad \Omega=dx\wedge dy/(xy).$$

原 $F_T$、$h$、$\Omega$ 在合法完整曲面上的意义必须写清；不以删去分母例外的有理图替换 U。
完整正则纤维为 $v^2+huv-Tv=u^3-Tu^2$，原映射准确为 $+P$、$P=(0,T)$。
四 terminal 的像 $-2P,-P,O,P$ 全部保留；原坏能级为 $h_-<h_+$，前者含 acnode 与持续圆，后者为 saddle。
原 P30 模型和旧实圆／平移接口不计新意。

采用 $\iota_X\Omega=-dh$、$dh\wedge\eta=\Omega$、$\eta(X)=1$、正周期 $L$、$\theta=t/L$，
使 $d\mu=|\Omega|=L(h)|dh|d\theta$。符号 $\Omega$ 只用于辛形式，不与周期混用。
旧证明将周期写作 $\Omega$ 的地方，正文统一转写为 $L$，并逐项保留规范和倍率。
内积第一变量线性；$\Pi$ 为逐连通正则圆均值的正交条件期望，不是整纤维一个均值或原 F 不变子空间投影。
$\Pi$ 与 Koopman 交换，但上区间零模仍有换圆的 -1 方向；须保留错误整纤维中心化的反例。

## 3. 不可弱化的完整主定理

对原 $f,g\in C_c^\infty(U_T)$，允许支撑跨两节点、坏能层的持续圆和全部 terminal，定义

$$C_n(f,g)=\langle((I-\Pi)f)\circ F_T^n,(I-\Pi)g\rangle_{L^2(\mu)}.$$

不假设 $(I-\Pi)f$ 仍原光滑；节点处非 Hölder 的投影行为必须正确处理。
写 $n=2m+r$，$m\ge1$、$r=0,1$，保留

$$\begin{array}{ll}
T\notin\{3/16,1\}:& C_{2m+r}=m^{-1/2}\mathcal A_r(m)+O(m^{-3/2}),\\
T=3/16:& C_{2m+r}=m^{-1/2}\mathcal A_r(m)+m^{-1}\mathcal D_r(m)+O(m^{-3/2}),\\
T=1:& C_{2m+r}=m^{-2}\mathcal B_r(m)+O(m^{-3}).
\end{array}$$

全部主项系数按 G (1.2)–(1.5) 定义，不只写一个有界未定振幅：

- $\sigma$ 是原 $F^2$ 的逐圆相位：下／中为 $2\rho$，上为实际双步回返 $\rho_+$。
- $\mathcal A_r$ 是所有实际驻圆和所有非零模的绝对收敛驻相和，系数为 $L\widehat f_{r,k}\overline{\widehat g_k}/\sqrt{|k\sigma''|}$，含准确 $\pi\operatorname{sgn}(k\sigma'')/4$ 相位。
- 原中心 $\varepsilon=h_--h$，$\sigma_E=\sigma_c+\beta\varepsilon+\gamma\varepsilon^2/2+\cdots$，$\beta=-2\rho'(h_-)$、$\gamma=2\rho''(h_-)$。
  $L\widehat f_{r,k}\overline{\widehat g_k}=\varepsilon A_k^{(r)}+\varepsilon^2R_k$，一阶 $A_k$ 只在 $k=\pm1$ 非零，但原函数类与余项仍是无限 Fourier。
- $\mathcal B_r$ 的单项为 $-A_k^{(r)}e^{2\pi ikm\sigma_c}/(2\pi k\beta)^2$；$\mathcal D_r$ 的单项为 $iA_k^{(r)}e^{2\pi ikm\sigma_c}/(2\pi k\gamma)$，后者只用于 $T=3/16$。
- 上外换圆的奇数振幅是交叉配对，须明确写出 G 的真实两圆相位；不能只发表 $F^2$ 结论后略去原 F。

对每固定 T、固定紧支撑能窗，主定理余项由原 $C^{20}$ 范数乘积控制；不要求参数阈值附近一致。
完整 saddle 固定平滑能量截断对每个指定整数 $N\ge1$ 为 $O(m^{-N})$，原 $C^{N+2}$ 足够。
每固定参数均有原光滑实／复观测实现非零归一化 limsup；不要求每对观测、每个时刻或每个奇偶子列都非零。
$T=1$ 的泛型条件是原一阶 jet 对中 $A_1,A_{-1}$ 不同时为零的开稠密条件；主项全消失至少为 $O(m^{-3})$。
负时由酉性与交换观测共轭处理；没有额外随机或非共振假设。

## 4. 全文必须承担的证明责任

| 责任 | 冻结原证据 | 正文不可删的内容 |
|---|---|---|
| 原完整状态与真实 +P | P30 指定段、GEO Step4 | P30 已证曲面可诚实引用；实数完整圆上的延拓和动力等式实际写出，不外推 FIX 的正特征声明 |
| 实圆组件、原测度与投影 | GEO、M | 三能区的圈数／保持或交换、terminal 正则性、正 coarea、原均值投影及非衰减反例 |
| 特征零非齐次 forcing | PF Steps1–2 | 真实还原恒等式、组合 primitive 的 Q(O)=0、全部移动端点、Wronskian；不能一句引未发表笔记 |
| 全参数驻圆分类 | B/MID/UP/INF/TW | 持续圆真实锚定，中间存在性，实际2P与表观奇点，可微无穷积分常数，T=1严格无驻点及所有驻点非退化 |
| 节点局部原动力 | N | 原F²解析短时间及其正值，周期上下侧 passage 次数，原观测角范数及投影正则性边界 |
| 全圆混合能量／角导数 | K Steps1–5 | 移动入口、Euler微分、流时隐函数、外弧／开接缝／周期gauge，原坐标范数的全模估计 |
| 原相位倒导数与反复积分 | K Step6、G §§3–4 | q=1/α′ 的符号、转置稳定、可积对数振幅、真实 qT^ja→0 边界及全k求和 |
| 原椭圆角与jet | E §§4–8 | 正向对称角、偶半径光滑下降、有限原范数全模余项、两个端点的准确系数与更快余项 |
| 完整拼合与最优性 | G §§5–8、E §9 | 绝对可积/Fubini、普通驻相统一余项、同能级持续圆双侧一次驻相、换圆奇偶及合法原实／复观测 |

上述旧未成篇 twist 链仍是必要正文负载，即使不计新意也不能外移；INF 仍供应全参数分类，不能用紧支撑为由删掉。
通用引理只写一次，消费时保留实际前提和倍率；普通驻相可沿 G 的自足标量证明写一次。
P30 可引用成果必须明确是本地未发表接受稿，不能伪造出版身份；给予当前论文读者足够的对象、假设与接口。
不消费的旧值域表、极大值积分方程、正特征、一般 r 法丛、周期计数、Q3 小分母不加入本稿。

## 5. 归属、非主张与修订

FHR 的跨 separatrix／原光滑全模及中心 jet 技术、HRSS 原变量端点机制、MRVB 频率混合框架、
标准 Morse／coarea／Fourier／驻相均准确归因；本稿不是普适新阻尼方法或“首次跨节点”。
离散 LLN 是 Cesàro，Markov 结论依赖随机扰动，不能冒作原确定性结果。
引用仅限正文实际消费且元数据已核准的条目，不因正式准入编造 BibTeX、阅读范围或文献穷尽。

不主张原未投影系统混合、单圆混合、CLT、谱统计、Hilbert–Pólya／Riemann 行列式、全局常数时间摆流，
不主张统一 T 极限、固定 C20 控制所有 N、全部高阶 jet 分类、所有时刻正下界或目标零点拟合。
此处符号改名和章节整合仅为忠实转写；若真实问题要求改科学量词，先记录证据并依原权限边界处置，不以排版名义改锁。
锁本身冻结后如需必要修正，保留 V1 并用明确 successor；正文完整后另冻 source-byte manifest，不预填不存在的源哈希。
正文、页数、PDF、双根确定性、fresh 实际稿件/PDF 和随后终局完整性分别验收。
无投稿、上传、托管、push、外发或付费资源效力；无 CAS、数值、参数／阶数枚举或 N≥10 扫描。
