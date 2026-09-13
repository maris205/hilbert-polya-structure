# Paper31：指定 b 投影不可分解机制的全阶诊断 V1

日期：2026-09-12 UTC；clock 实读 17:25:20。作者：`/root/p31_b_indecomposability_mechanism`。
原 Claim 状态：`NOT CURRENTLY JUSTIFIED / BOUNDED_MECHANISM_AUDIT / NO_CANDIDATE_ADMISSION`。
结论：得到全阶标记分离与双函数生成短引理；拟从模单位把任意中间覆盖强迫成保 $j$ 模商的机制未闭合。
这不是原全称命题的反例，也不是其证明；不得把本件短引理换作更易通过的新长文中心。

## 1. Claim、Assumptions 与 Notation

原问题保持：对每个整数 $N\ge4$，在 $\mathbf C$ 上令 $F_N=\mathbf C(X_1(N))$，
指定 Tate 参数 $b=T$ 给出 $\beta_N:X_1(N)\to\mathbf P^1_b$。
要证明不存在 $\mathbf C(b)\subsetneq K\subsetneq F_N$，或识别真实例外。
中间域 $K=\mathbf C(Y)$ 中的 $Y$ 是任意光滑射影连通曲线，不预设有理、模曲线、Galois 商或属零。
全对称单值群还需要实际惯性；本件不承担并行分支的惯性全阶研究。

原模型为 $v^2+huv-Tv=u^3-Tu^2$，以 $R=(0,0)$ 为标记点，$b=T,c=1-h$。
精确 $N$ 阶正规化及指定函数已在[入口诊断](PAPER31_QPI_MODULAR_B_MONODROMY_FEASIBILITY_V1_20260912.md)固定。
$j$ 专指遗忘标记后椭圆曲线的经典模不变量；小写 $b$ 不与其它旧多项式同名。
本件全部构造在特征零；不改变有限好点厚度、正特征量词、正文22–30页或整批4/5状态。

## 2. Strategy 与 Dependency Map

1. 把 $b$ 拉到满级 $X(N)$，对所有精确阶标记构造等变族 $b_{\mathbf v}$。
2. 用尖点阶的分段线性公式，证明不同标记除符号外连除子都不同。
3. 在 $\mathbf C(X(N))/\mathbf C(j)$ 中应用 Galois 对应，得到 $\mathbf C(j,b)=F_N$。
4. 检验该结论是否排除任意中间域：它只排除含 $j$ 的中间域。
5. 给出自足复合映射反例，定位“生成元／原始单位／局部分歧”升级为不可分解的失效处。

依赖外部的是尖点除子公式与经典满级 Galois 描述；标记分离的全阶符号算术论证和反例在下文给出。
本件的新推导仍是既有模单位与 primitive-family 方法的短应用，未作新颖性分数或发表价值主张。

## 3. 满级对象与统一尖点阶

令 $L_N=\mathbf C(X(N))$，$G=\mathrm{SL}_2(\mathbf Z/N\mathbf Z)/\{\pm I\}$。
经典满级覆盖给 $L_N/\mathbf C(j)$ 为 Galois 扩张，群为 $G$。
原始行向量 $\mathbf v=(v_1,v_2)\in(\mathbf Z/N\mathbf Z)^2$ 指 $\gcd(v_1,v_2,N)=1$。
在 $E_\tau=\mathbf C/(\mathbf Z\tau+\mathbf Z)$ 中置 $P_{\mathbf v}=(v_1\tau+v_2)/N$，
并在短 Weierstrass 方程 $y^2=x^3+Ax+B$ 上定义

$$b_{\mathbf v}=\frac{(x(2P_{\mathbf v})-x(P_{\mathbf v}))^3}{(2y(P_{\mathbf v}))^2}.$$

这里短方程的 $B$ 不是 Tate 参数；一般 Weierstrass 坐标的分母必须换为 $(2y+a_1x+a_3)^2$。
该比值对短坐标缩放不变，$N\ge4$ 时分母非零，且 $3P_{\mathbf v}\ne O$ 保证分子非零。
Tate 正常形中 $x(2P)-x(P)=b$、$2y+a_1x+a_3=-b$，故比值就是原 $b$。
它是满级曲线上的模单位，且 $b_{-\mathbf v}=b_{\mathbf v}$。
若 $\gamma=\left(\begin{smallmatrix}\alpha&\beta\\\gamma_0&\delta\end{smallmatrix}\right)\in\mathrm{SL}_2(\mathbf Z)$，格同构 $z\mapsto(\gamma_0\tau+\delta)z$ 给
$b_{\mathbf v}(\gamma\tau)=b_{\mathbf v\gamma}(\tau)$，这里使用行向量右乘。

满级尖点可用原始列向量 $\mathbf w$ 模符号标记；取提升矩阵 $A\in\mathrm{SL}_2(\mathbf Z)$ 的首列为该向量。
这类列向量全都可出现：原始剩余向量可补成模 $N$ 行列式一矩阵，再提升到 $\mathrm{SL}_2(\mathbf Z)$。
记 $\|r\|_N=\min(\bar r,N-\bar r)$，$0\le\bar r<N$，并定义

$$\phi(t)=\begin{cases}t,&0\le t\le1/3,\\3-8t,&1/3\le t\le1/2.\end{cases}$$

则尖点 $\mathbf w$ 处的满级阶为

$$\operatorname{ord}_{\mathbf w}(b_{\mathbf v})=N\phi\!\left(\frac{\|\mathbf v\mathbf w\|_N}{N}\right).\tag{1}$$

来源：[van Hoeij–Smith, Theorem4.2、§6.1–6.3](https://arxiv.org/pdf/2004.13644)给 $b=-F_3$、尖点宽度和阶。
将其式子拉到满级后所有几何宽度均为 $N$，故得到(1)；等变性把标准标记推广到任意 $\mathbf v$。
唯一需要单独说明的是 $X_1(4)$ 的不规则尖点：其几何分歧阶为一，不是定义在 $\mathrm{SL}_2$ 中的宽度二。
满级有效群为 $\pm\Gamma(4)$，宽度四；拉回倍率为四除以一，因此(1)在 $N=4$ 也成立。
令 $U=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$。一般 $N\ge4$ 的满级宽度为 $N$：$U^k\equiv I\pmod N$ 当且仅当 $N\mid k$，而 $U^k\equiv-I$ 不可能。
这里没有把算术尖点行当作一个几何尖点，也没有忽略 $8\mid N$ 时的零阶尖点。

## 4. Lemma S：全 N 的标记分离

**断言。** 对所有 $N\ge4$ 及原始 $\mathbf v,\mathbf v'$，若 $b_{\mathbf v}/b_{\mathbf v'}\in\mathbf C^*$，
则 $\mathbf v'\equiv\pm\mathbf v\pmod N$；反向也成立，且反向的比值为一。
这是本件短引理的 `PROVABLE AS STATED`，不是原不可分解 Claim 的状态。

**Step 1：统一首标记。** 行列式一群在原始向量上传递；对两函数同时作一个变换，
可令 $\mathbf v=(1,0)$，并写 $\mathbf v'=(a,c)$。常数比值保证所有尖点阶相等。
在 $\mathbf w=(0,1)^t$ 使用(1)，得到 $\phi(\|c\|_N/N)=0$。
$\phi$ 在 $[0,1/2]$ 的零点只有零与 $3/8$，故 $c=0$，或 $8\mid N$ 且 $c\equiv\pm3N/8$。

**Step 2：排除八分之一边界候选。** 若后一情形成立，$c$ 在加法群中恰为八阶。
取三个原始列向量 $\mathbf w_k=(1,k)^t$，$k=0,1,2$，则 $a+kc$ 是三个不同剩余类。
式(1)要求它们全部满足 $\phi(\|a+kc\|_N/N)=1/N$。
在 $8\mid N$ 时，该方程只允许剩余类 $\pm1$：第二段候选折叠值 $(3N-1)/8$ 不是整数。
三个不同类不能全部属于两元素集合，所以 $c=0$。

**Step 3：排除非平凡倍点。** 原始性此时给 $\gcd(a,N)=1$；可折叠为 $1\le a\le N/2$。
在 $\mathbf w=(1,0)^t$ 比阶得 $a=1$，或 $a=(3N-1)/8>N/3$。
后者要求 $N\equiv3\pmod8$，并在 $N\ge4$ 下强迫 $N\ge11$。
再取原始向量 $\mathbf w=(2,1)^t$；第一标记的阶为二。
第二标记的折叠值是 $N-2a=(N+1)/4<N/3$，因此其阶为 $(N+1)/4$。
相等要求 $N=7$，与前提矛盾。于是 $a=1$，撤销折叠及统一变换即得 $\mathbf v'=\pm\mathbf v$。证毕。

该证明同样排除任意正整数次幂相等时的异标记，但本件不据此另建“全幂族”候选。
符号、$N=4$、$8\mid N$ 及 $N\equiv3\pmod8$ 均已在全阶论证中覆盖；不需要逐阶验证。

## 5. Corollary J：双函数生成，严格限于保 j 中间域

回到原标记 $\mathbf e_2=(0,1)$，其固定群是通常 $\pm\Gamma_1(N)$ 的模 $N$ 像 $H$。
第4节内部使用的 $\mathbf e_1$ 对应共轭的下三角群；此处已经变回原 $X_1(N)$，没有偷换曲线。
Lemma S 说明 $\mathrm{Stab}_G(b_{\mathbf e_2})=H$，因此有限 Galois 对应给

$$\mathbf C(j,b)=L_N^{\mathrm{Stab}_G(b)}=L_N^H=F_N.\tag{2}$$

若 $\mathbf C(b)\subseteq K\subseteq F_N$ 且 $j\in K$，则(2)立即强迫 $K=F_N$。
这排除全部保 $j$ 的非平凡中间覆盖，而不只 diamond 商；等价地，$(j,b)$ 给曲线的双有理模型。
若真正的 proper $K$ 存在，则必有 $j\notin K$，且仍有 $K(j)=F_N$、$[K(j):K]=[F_N:K]$。
因此这种覆盖的泛纤维必须含不同 $j$ 的椭圆曲线；改变同一椭圆曲线标记的论证不能消除它。
式(2)不声称 $(j,b)$ 处处嵌入，也不排除特殊点处不同标记或不同曲线的数值碰撞。

## 6. 所拟充分性为何确实失败：一个自足反例

以下仅检验代数逻辑，不是原 $X_1(N)$ 或指定 $b$ 的反例，也不替代原全称目标。
在 $\mathbf P^1_t$ 取 $J=t^3$、$g=t^2+t$、$u=g(g-1)=t^4+2t^3-t$。
直接恒等式 $u-2J=t(J-1)$ 给

$$\mathbf C(J,u)=\mathbf C(t),\qquad t=\frac{u-2J}{J-1}.$$

然而 $\mathbf C(u)\subsetneq\mathbf C(g)\subsetneq\mathbf C(t)$，两个次数均为二。
$u$ 的四个零点为 $0,-1,(-1+\sqrt5)/2,(-1-\sqrt5)/2$，互异且全为单零点，唯一极点为 $\infty$。
删去这五点后 $u$ 是单位；该有理开曲线的单位群模常数由四个线性零点因子自由生成。
$u$ 的指数向量为 $(1,1,1,1)$，可延拓为整数格的一组基，所以甚至“为单位群某基的成员”也成立。
单零点还表明 $u$ 不可能是非平凡幂；该例直接对应原始单位论证的限度。

微分 $u'=(2t+1)(2t^2+2t-1)$ 有三个互异根，故所有有限分歧的 $e$ 均为二。
$t=-1/2$ 的分支值为 $5/16$，其上只有该点分歧；另两临界点映到 $-1/4$。
所以该复合覆盖连一枚单独二换位都有，但仍有二乘二中间分解。
该例证明“与另一个函数一起生成＋原始单位＋有限分歧至多二＋一枚二换位”不能推出不可分解。
它没有把 $J$ 冒称经典模 $j$；若要利用真正模曲线的额外结构，仍须另证那项结构如何约束所有 $K$。

## 7. Corrections、缺失引理与停止边界

本轮尝试的具体机制是“尖点除子分离所有标记，继而把任意中间域强迫为保 $j$ 的模商”。
前半由 Lemma S 和(2)完成；后半没有证明，且不可能仅凭前半及单位群生成定理得到。
若增加独立假设“每个 proper $\mathbf C(b)\subsetneq K\subsetneq F_N$ 都含 $j$”，则(2)将给原不可分解结论。
但这一假设本身就是缺失的全局几何限制，不是现成定理，也未被本件采纳为实际前提。
写中间分解为 $X_1(N)\xrightarrow{\pi}Y\xrightarrow{\bar b}\mathbf P^1_b$；除子拉回只给 $\operatorname{div}(b)=\pi^*\operatorname{div}(\bar b)$，不能推出 $j$ 也拉回。
尖点之外的中间映射还可能分歧；不能未经证明把它当作双曲均匀化的无分歧模覆盖。
即使另证某覆盖来自算术 Fuchsian 超群，也须检查其是否保经典 $j$，不能直接归入 $G$ 的子群。
原 M1 因而继续为 `NOT CURRENTLY JUSTIFIED`；本轮没有得到原构造反例，也没有证明不存在反例。
下一项有意义输入必须约束不同 $j$ 之间的指定 $b$ 等值对应，或直接控制全部中间覆盖；继续扩大标记稳定子检查不是同一缺口的解答。

## 8. 来源扣除、独立检查与冻结

[Streng, Theorem1.1](https://ahl.centre-mersenne.org/item/10.5802/ahl.160.pdf)描述有理模单位群的自由生成元；它不是 $\mathbf C(b)$ 极大子域定理。
[Jung–Koo–Shin, arXiv:1506.06317v3, Example3.1及Proposition4.1](https://arxiv.org/pdf/1506.06317)
已用尖点阶区分标记，并从 primitive Fricke family 的稳定子得到含 $j$ 的函数域生成。
本件按该既有方法扣除；未发现其正文直接陈述本件指定 $b$ 引理，不等于已完成穷尽查新。
该文的 family primitive、整数多项式 content primitive、单位格 primitive 与所需置换群 primitive 是四种不同命题。

本人全文读 proof-writer 技能及入口诊断173行；未重审其 $N=4,\ldots,9$ 核算。
本人一手读取：van Hoeij–Smith 引言、Theorem4.2及证明、§6.1–6.3所用段；Streng 摘要、引言至Theorem1.1及后续说明；
Jung–Koo–Shin 摘要、引言定义、Example3.1及Proposition4.1完整证明。没有宣称这三篇全文通读。
聊天型非作者检查由 `/root/p31_b_indecomposability_mechanism/full_level_stabilizer_check` 独立进行；不承担候选评分。
该检查补明行／列约定、短方程分母及不规则尖点几何宽度，全部已落实；原全称未因短引理检查而升级。
范围偏差：检查端额外做了有限 $N$ 的剩余类算术核对；作者获知后要求停止，未消费其结果作为全阶证据或证书。
本件仅依赖上面的全阶符号证明；未生成 $N\ge10$ 的精确阶方程／单值群表，没有稿件、GPU或外部写入。
冻结：提交哈希、行数、字节数后停止编辑；仅拥有本新文件，旧证明、旧FAIL、项目状态及其它文件未修改。
