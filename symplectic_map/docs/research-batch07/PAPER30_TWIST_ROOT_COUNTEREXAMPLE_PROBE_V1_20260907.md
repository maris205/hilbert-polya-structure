# 双谐波共振首项：独立递推与反例诊断 V1

日期：2026-09-07。角色：有界独立作者诊断，不是正式候选评价。

## Claim

研究固定辛映射

$$
p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,
\qquad q'=q+p',
$$

其周期作用量取

$$
\mathcal A(q)=\sum_{j=0}^{s-1}
\left\{\frac12(q_{j+1}-q_j)^2-\epsilon\cos q_j
-\lambda\epsilon^2\cos2q_j\right\}.
$$

固定互素整数 $0<r<s$、$s\ge3$，写
$q_j=\theta+2\pi rj/s+u_j$，其中 $u$ 周期且 $\sum_j u_j=0$。
在该零均值子空间消去 $u$，定义约化作用量 $W_{r,s}$。
目标是独立确定

$$
W_{r,s}(\theta)=\text{相位无关项}
+\epsilon^s C_{r,s}(\lambda)\cos(s\theta)+O(\epsilon^{s+1})
$$

中 $C_{r,s}$ 的正确递推，并尝试反驳“任意分母时所有根皆实且简单”。
不将该全实根命题预设为定理。

## Status

全分母全实根／简单性：`NOT CURRENTLY JUSTIFIED`。

以下较弱命题：`PROVABLE AS STATED`。

1. 下述正频对角递推严格给出指定作用量规范的 $C_{r,s}$。
2. $\deg C_{r,s}=\lfloor s/2\rfloor$，全部系数非零且交替变号；所有实零点严格为正。
3. $s=3,4,5,6$ 的全部互素代表，其首项多项式根均为正、实且简单。

有界浮点诊断没有找到反例，但不能增加以上定理量词。
本报告不解决简单消失点之后的真实分裂阶，不作原创性或自然篇幅结论。

## Assumptions

- $r,s$ 固定；不提出任何对 $s$ 一致的小除数估计或余项。
- $\lambda$ 是任意固定实参数；解析消元在其任意固定紧邻域局部进行。
- 相位规范和作用量符号始终如上，不能与反号势函数的系数混用。

## Notation

令 $\omega=2\pi r/s$，$L u_j=2u_j-u_{j-1}-u_{j+1}$，并令

$$
D_k=4\sin^2(\pi rk/s)>0,\qquad 1\le k<s.
$$

$t$ 只用作“$\epsilon$ 次数等于正 Fourier 频率”的形式记号。
将 $iu_j$ 的该对角部分记为
$v(t)=\sum_{k=1}^{s-1}v_k t^k$，代入实际相位时 $t=\epsilon e^{i(\theta+\omega j)}$。
设 $E_n=[t^n]e^{v(t)}$，$F_n=[t^n]e^{2v(t)}$；规定负下标系数为零，
$E_0=F_0=1$。

## Proof Strategy

先利用零均值 Hessian 的可逆性获得实际解析消元，再以次数／频率过滤隔离首共振。
由约化作用量导数而非直接展开作用量提取归一化系数。
最后用正分母保证的符号归纳和低分母精确判别式作有限结论。

## Dependency Map

1. 解析消元依赖 $L$ 在零均值子空间正定。
2. 首共振定位依赖循环移位对称及 Fourier 频率不超过 $\epsilon$ 次数。
3. $C$ 的归一化依赖 $W'=\sum_j(\epsilon\sin q_j+2\lambda\epsilon^2\sin2q_j)$。
4. 系数符号与次数依赖 $D_k>0$、指数级数乘法和无抵消归纳。
5. 小分母根结论依赖精确式、判别式及第 4 步排除非正实根。

## Proof

### Step 1. 约化和首次可能共振

设 $\Pi$ 为零均值正交投影。驻值方程是

$$
Lu+\Pi\bigl(\epsilon\sin(\theta+\omega j+u_j)
+2\lambda\epsilon^2\sin(2\theta+2\omega j+2u_j)\bigr)=0.
$$

$L$ 的唯一周期核为常数，故在零均值子空间可逆。有限维实解析隐函数定理给出
以 $u=0,\epsilon=0$ 为中心的唯一局部解析解。该结论对固定 $r,s,\lambda$ 成立。

逐阶求解上述方程，$\epsilon^n$ 系数的 Fourier 频率绝对值不超过 $n$：
基础 forcing 分别具有次数／频率 $(1,\pm1)$ 和 $(2,\pm2)$；乘法将次数、频率相加，
而 $L^{-1}\Pi$ 不增加频率。此归纳同时适用于代入后的作用量。

循环置换周期指标使 $W$ 在 $\theta\mapsto\theta+\omega$ 下不变。
互素性因此迫使其 Fourier 频率属于 $s\mathbb Z$。
所以所有次数 $n<s$ 的相位项均消失，次数 $s$ 至多含频率 $\pm s$。
变换 $q'_j=-q_{-j}$ 对应于 $\theta'=-\theta$、$u'_j=-u_{-j}$，
保持指定旋转数、作用量及零均值条件；唯一消元解随此变换而变换。
因此 $W$ 为偶函数，次数 $s$ 的相位项只有 $\cos(s\theta)$。

### Step 2. 正频递推和作用量归一化

次数等于正频率的项只能来自正频基础 forcing：如果任一基础频率为负，
其频率和会严格小于次数和。故计算此对角时可以删除所有负频来源。
在 $k<s$ 时零均值投影不会删除频率 $k$，并且 $L$ 在该模式上为 $D_k$。
用 $v=iu$ 将正频方程改写，得到

$$
\boxed{\quad
v_k=-\frac{\frac12E_{k-1}+\lambda F_{k-2}}{D_k},
\qquad 1\le k<s.\quad}
$$

这是三角递推，因为右边只涉及下标小于 $k$ 的 $v$。可用

$$
E_n=\frac1n\sum_{k=1}^{n}k v_kE_{n-k},
\qquad F_n=\sum_{a=0}^{n}E_aE_{n-a}
$$

实现而不进行 Fourier 全展开。

在约化临界点，全梯度为常数向量，而 $\sum_j\partial_\theta u_j=0$；
链式法则和 $\sum_j(Lu)_j=0$ 给出

$$
W'(\theta)=\sum_j
\bigl(\epsilon\sin q_j+2\lambda\epsilon^2\sin2q_j\bigr).
$$

其 $\epsilon^s e^{is\theta}$ 系数是
$s(E_{s-1}+2\lambda F_{s-2})/(2i)$。
另一方面 $\partial_\theta(C\cos s\theta)$ 的正频系数为 $isC/2$。
比较两式得到

$$
\boxed{\quad C_{r,s}(\lambda)=-E_{s-1}-2\lambda F_{s-2}.\quad}
$$

这里没有额外的 $s$ 因子，也没有来自负频部分的额外 $2$ 因子。

### Step 3. 全分母系数符号和次数

归纳命题是：对 $1\le n<s$，$v_n,E_n,F_n$ 的次数都是 $\lfloor n/2\rfloor$，
其 $\lambda^j$ 系数在 $0\le j\le\lfloor n/2\rfloor$ 上均非零且符号为
$(-1)^{n-j}$。其中 $v_1=-1/(2D_1)$ 直接成立。

假定此前系数满足命题。相同次数／频率的乘积中，符号乘积为
$(-1)^{n-j}$，所以指数级数内部没有符号抵消。
三角递推的第一项继承 $E_{n-1}$ 的符号，乘以负号后为 $(-1)^{n-j}$；
第二项的 $\lambda^j$ 来自 $F_{n-2}$ 的 $\lambda^{j-1}$，乘以负号后也为
$(-1)^{n-j}$。正分母 $D_n$ 不改变符号。
因此 $v_n$ 在允许范围内均有相应非零系数。

对 $E_n$ 的严格非零性，也可直接在 $e^v$ 中选择
$v_1^{n-2j}$ 和 $v_2$ 的 $\lambda$ 项共 $j$ 次；它贡献 $t^n\lambda^j$，
系数非零，并且其他贡献同号。$F_n$ 的论证由其卷积和 $E_0=1$ 得到。
这完成归纳。

最后代入 $C$ 的公式，两个来源仍同号，并且第二来源提供最高次系数，故

$$
C_{r,s}(\lambda)=\sum_{j=0}^{\lfloor s/2\rfloor}
(-1)^{s-j}a_j\lambda^j,\qquad a_j>0.
$$

特别地 $\deg C=\lfloor s/2\rfloor$。若 $\lambda=-x$、$x\ge0$，则
$C(-x)=(-1)^s\sum_j a_jx^j\ne0$，所以全部实零点严格为正。
这个结论不排除非实根，也不证明实根简单。

### Step 4. 精确小分母

对称性 $D_k(r,s)=D_k(s-r,s)$ 给出 $C_{r,s}=C_{s-r,s}$。
全部 $s=3,4,5,6$ 的互素代表如下：

$$
C_{1,3}=\lambda-\frac1{24},
$$

$$
C_{1,4}=\lambda^2-\frac34\lambda+\frac5{192},
$$

$$
C_{1,5}=\frac{-11+\sqrt5}{4}\lambda^2
+\frac{29+5\sqrt5}{48}\lambda
-\frac{67+15\sqrt5}{3840},
$$

$$
C_{2,5}=\frac{-11-\sqrt5}{4}\lambda^2
+\frac{29-5\sqrt5}{48}\lambda
-\frac{67-15\sqrt5}{3840},
$$

$$
C_{1,6}=-\frac43\lambda^3+\frac{39}{8}\lambda^2
-\frac{127}{96}\lambda+\frac{99}{2560}.
$$

二次式判别式分别为

$$
\frac{11}{24},\qquad
\frac{711+289\sqrt5}{2880},\qquad
\frac{711-289\sqrt5}{2880}.
$$

前两项为正；最后一项为正由 $711^2>5\cdot289^2$ 及 $711>0$ 得到。
三次式的判别式为

$$
\operatorname{disc}(C_{1,6})=\frac{285935111}{16588800}>0.
$$

实二次式正判别式给出两互异实根，实三次式正判别式给出三互异实根。
再用 Step 3 排除非正根，即得所列小分母全为正简单根。
线性式已直接给出正简单根 $1/24$。∎

## Corrections or Missing Assumptions

没有发现应当删除全实根猜想的反例，但同样没有给出该猜想的证明。
把“交替系数”升级成“全正实根”是不合法推论：交替系数只排除非正实根。
本报告既不引入新模型，也不以全实根为额外假设换取后续定理。

## Diagnostic Record

- 执行了一次临时代数浮点程序，以双精度三角值代入上述递推，对
  $3\le s\le20$、$1\le r\le s/2$ 的全部互素代表计算多项式根。
- 该次程序实际枚举了范围内全部代表，比最初“少量”诊断密；发现这一点后
  已向主控即时说明，不再增大范围。此事实不隐藏为挑选的少数成功样本。
- 在该范围内，所输出根均为正实数，未出现非实或接近重根的明显迹象。
  双精度多项式求根并非区间证书，不能证明这些全部有限结果，更不能证明全分母结论。
- 只对上面 $s=3,4,5,6$ 的结果追加了精确符号化递推与判别式。
  未把高分母浮点结果包装成数学验收、实验结果或发表产物。
- 按主控补充要求，将原程序保存为同前缀 `.py`，并原范围重跑一次保存同前缀
  `_RESULTS.json`；仍为上述 $63$ 个代表，没有增加输入。JSON 保存每个代表的
  双精度系数、根、虚部阈值标记和根间距，以及五个精确小分母结果。
- 作者稿核查期收到独立复查提示：Step 3 的归纳范围由含混的 $n\ge1$
  更正为 $1\le n<s$，与本稿已定义的截断级数一致；提取 $C$ 只需此范围，
  未改变数学式或扩大结论。
- 本文系数可由 Step 2 的三角递推直接重现；没有修改其他代理文件、旧论文、
  冻结产物或批次状态。Paper30 未立项，批次状态仍为 $3/5$。

复现命令（只向标准输出打印 JSON，不改动结果文件）：

```bash
python docs/research-batch07/PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907.py
```

脚本及保存结果：

- [复现脚本](PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907.py)
- [实际重跑结果](PAPER30_TWIST_ROOT_COUNTEREXAMPLE_PROBE_V1_20260907_RESULTS.json)

## Open Risks

1. 没有 Jacobi／正交多项式／总正性等能够证明全分母实根结构的表示。
2. 尚未证明 $C$ 与 $\partial_\lambda C$ 对任意互素 $r,s$ 无公共根。
3. 未分析简单消失点处下一非零共振项及其统一非消失性。
4. 本任务没有新增文献检索；递推和系数符号本身的新意不作判断。
