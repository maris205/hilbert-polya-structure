# Paper30：有限阶乘块统一正常形的独立数学检查 V1

日期：2026-09-08。

## Claim and Review Scope

检查对象是 [FACTORIAL_BLOCK_NORMAL_FORM_DIAGNOSIS V1](PAPER30_TWIST_FACTORIAL_BLOCK_NORMAL_FORM_DIAGNOSIS_V1_20260908.md) 的 N1–N3 及其替代接口。目标全文 452 行，读取时 SHA256 为

`ebfe61b593e32d28b602a948d4e4ce5d4fe16fd00ec7a3a631975049b7b966b1`。

本件由未参与目标新推导的当前可用 Codex 子代理独立执行。审查是阅读作者证明后的非盲数学检查，不是人类审稿、跨模型交叉验证或另一份作者自查。实际派发配置由主控确认：`fork_turns=none`、`reasoning_effort=xhigh`，未指定模型覆盖，使用当前可用默认模型；不另作运行模型名称推断。使用 `research-review` 与 `proof-writer` 的证明审查要求；未调用 `gpt-5.4`、Codex MCP 或外部审稿服务，不把技能中的默认服务／模型名称写作本次实际执行身份。本件不提供新意、价值、容量或正式候选票，也不作 Route 评价。

范围固定为全部素数 $p\ge5$、整数 $a\ge2$、同一实际分支与

$$
h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,
\quad m=(p-1)/2,\quad M=p^{a-1}m.
$$

形式阶乘命题始终固定 $P_1=1/2$、$\alpha=1,2$，不扩展为独立幅度参数。检查没有引入新实验、新端点、新传播子移位或新科学量词。

## Status

**限定数学结论：PASS。** N1、N2 可在所述一般系数环上直接证明；N3 在原稿明列且本次保留的已接受低块、第一真实入口及原第二 forcing 端点引理下成立。没有发现需要修改 N1–N3 陈述的数学错误。

对应 `proof-writer` 状态为 `PROVABLE AS STATED`：这里的“原陈述”包括目标 Assumptions 中明确导入的事实。N3 不是仅由 N1／N2 无条件推出的定理；本次也不重新认证全部旧第二 forcing 证明。这个依赖条件是原有假设，不是为挽救新证明而增加的假设。

| 检查项 | 数学判定 | 精确范围／条件 |
| --- | --- | --- |
| $\mathfrak F_R$ 自由基及无隐藏 $p$ 挠元 | PASS | 自由基本身对任意交换 $R$ 成立；无 $p$ 挠元性质继承自 $R$ |
| 自然嵌入及缩放系数像 | PASS | 必须使用 $R\hookrightarrow R[1/p]$；不能删去无 $p$ 挠元假设 |
| 全部 $N<3p$ 的有限指数整性 | PASS | $p\ge5$ 保证 $N<p^2$；仅使用有限指数 |
| 单一阶乘公式同时生成两带 | PASS | $r=0,1,2$，余项为真正的 $pR$，不只是模 $h$ |
| 固定首系数的 Frobenius | PASS | 仅固定标量 $\alpha/2$ 可化简；不使用 $L^p=L$、$H^p=H$ 或 $b^p=b$ |
| N2 整块指数及跨块进位 | PASS | 整系数层保留 $x^p=p\eta$；只在模 $p$ 后令 $x^p=0$ |
| N3a 四项耦合与负下标 | PASS | 真实负带边缘系数留在 $pR$ 误差，不将实际系数置零 |
| 第一、第二块的非循环整性归纳 | PASS，依赖已声明入口 | 先第一块和第一模型，再原第二 forcing，最后第二块 |
| 两条实际递推和零常数模型 | PASS | 仅模型常数为零；实际 $Y_0,Z_0$ 及完整平方保留 |
| 形式代入与原始误差 | PASS | 有限参数次数保证 $H=h$ 合法；共同原始界仅为 $h^{M-m}$ |
| 端点升精度及替代边界 | PASS，条件接口 | 另有 $h^m$ 缺陷才达到 $h^M$；原第二 forcing 和后半响应义务不被删除 |

## Assumptions and Notation

1. $R$ 是交换、无 $p$ 挠元的 $\mathbb Z_{(p)}$-代数，$P\in xR[x]$、$\deg P<p$、$P_1=1/2$。一般代数检查允许 $R/pR$ 有幂零元。
2. 实际环取 $R_{\rm act}=\mathcal O^+[L]$，其中 $\mathcal O^+=\mathbb Z_p[h]$，$v_h(h)=1$、$v_h(p)=M$。因此作为理想，$pR_{\rm act}=h^MR_{\rm act}$。
3. 形式环取 $R_{\rm for}=\mathbb Z_{(p)}[[H]][L]$，即相对于 $H$ 有统一有限 $L$ 次数界的参数多项式。低块 $P(H,x)$ 由真实 Chebyshev 递推给出，且 $P_i(h,L)=V_i$。
4. 实际递推保持

   $$
   d_n(h)V_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},
   \qquad d_n(h)=-D_n/h.
   $$

   对 $p\nmid n$、$1\le n<3p<p^a$，$d_n(h)$ 为单位；不把 $n=p,2p$ 当作单位步。
5. 已接受的低块与第一入口为

   $$
   V_i\in R_{\rm act}\ (1\le i<p),\quad V_1=1/2,\quad
   h^mV_p\in R_{\rm act},\quad
   h^mV_p\equiv\frac{(-1)^m}{2}(2-L^m)\pmod h.
   $$

6. 原第二 forcing 端点仅在第一块及其比较已完成后导入：

   $$
   p\mathcal B_2=2h^{2m}+O(h^{2m+1}),\qquad
   d_{2p}/h^{2m}=-4+O(h),\qquad
   V_{2p}=\mathcal B_2/(2d_{2p}).
   $$

   本次核查它的前向依赖和与新接口的兼容性；其已接受结论不是 N1／N2 的新推论。

下文模 $p$ 与模 $h$ 分开标明。所有 $O(h^q)$ 均表示参数多项式的逐系数理想包含。

## Proof Strategy and Dependency Map

新的代数部分按“首一关系的自由基 → 缩放系数坐标 → 统一阶乘剩余 → 有限指数乘法”独立复核。实际部分只对已知前缀应用该代数引理。

$$
\begin{aligned}
&\text{低块及实际 }V_p
\longrightarrow\text{第一块前缀整性}
\longrightarrow\text{第一桥和第一模型比较}\\
&\longrightarrow\text{原 A04 配对／响应／action 端点}
\longrightarrow pV_{2p}\text{ 整}
\longrightarrow\text{第二块前缀整性}\\
&\longrightarrow\text{完整四项桥及第二模型比较}.
\end{aligned}
$$

原 A04 端点只使用到实际 $V_{2p-1}$；新第二块在该端点之后出现。后续 A06 的基解、$Q$ 耦合消元、真实二阶传播子差和高精度端点仍是独立保留的义务。

## Proof Check

### Step 1. 自由基、嵌入和进位

令 $A=R[\eta]/(\eta^3)$。关于 $x$ 的首一多项式 $x^p-p\eta$ 使 $A[x]/(x^p-p\eta)$ 唯一分解为

$$
\sum_{j=0}^{p-1}a_j(\eta)x^j,\qquad
a_j(\eta)=\sum_{r=0}^2a_{rj}\eta^r.
$$

因而 $\{x^j\eta^r:0\le j<p,0\le r\le2\}$ 确为 $R$-自由基，两个关系不会暗中引入新的 $p$ 挠元。

映射 $\eta\mapsto x^p/p$ 将其送到 $R[1/p][x]/(x^{3p})$。第 $(r,j)$ 个坐标变成 $p^{-r}a_{rj}x^{rp+j}$；这些次数互不相同，且 $R\to R[1/p]$ 单射，故核为零。反过来，满足 $p^rF_{rp+j}\in R$ 的截断多项式恰可取 $a_{rj}=p^rF_{rp+j}$，证明所述像的精确刻画。

乘法也没有额外的闭包假设：若 $j+j'\ge p$，则

$$
(x^j\eta^r)(x^{j'}\eta^{r'})
=p\,x^{j+j'-p}\eta^{r+r'+1}.
$$

达到 $\eta^3$ 的项才为零。故约化商为

$$
\mathfrak F_R/p\mathfrak F_R=(R/pR)[x,\eta]/(x^p,\eta^3).
$$

模 $p$ 后，$\eta$ 仍是该自由基中的一个坐标，不能因 $x^p=0$ 把它置零。对实际环，$\mathcal O^+/p\mathcal O^+$ 有幂零元也不妨碍以上论证。

### Step 2. 一条阶乘计算的全部量词

对 $0\le r\le2$、$0\le s<p$，$rp+s<3p<p^2$，从而

$$
v_p((rp+s)!)=r,
\qquad
\frac{(rp+s)!}{p^r}
=r!\prod_{u=0}^{r-1}\prod_{i=1}^{p-1}(up+i)
\prod_{i=1}^{s}(rp+i).
$$

约化非零剩余类乘积得 $(p-1)!=-1$，于是

$$
\frac{p^r}{(rp+s)!}\equiv\frac{(-1)^r}{r!s!}\pmod p.
$$

这包括 $r=0$ 的空乘积，并未分别假设第一、第二带的剩余。

固定 $N=rp+j$，$0\le j<p$。由于 $P$ 无常数项，$[x^N]e^{\alpha P}$ 只含 $k\le N$ 的指数项。每个 $v_p(k!)\le r$，所以乘 $p^r$ 后整。模 $p$ 时 $k<rp$ 的项消失，仅余 $k=rp+s$、$0\le s\le j$。

在任意交换的特征 $p$ 商环中，Frobenius 给出

$$
(\overline{\alpha P})^p
=(\overline{\alpha P_1})^px^p+O(x^{2p}).
$$

这是必须先使用的式子。对当前固定的 $P_1=1/2$、$\alpha=1,2$，标量 $\overline{\alpha/2}$ 来自 $\mathbb F_p$，才有其 $p$ 次幂等于自身。对于当前第 $r$ 块，任何选入 $x^{2p}$ 或更高项的乘积，其总次数至少 $(r+1)p$，不贡献 $x^{rp+j}$。所以

$$
\begin{aligned}
\overline{p^r[x^{rp+j}]e^{\alpha P}}
&=\frac{(-1)^r}{r!}\left(\overline{\alpha/2}\right)^{pr}
  \sum_{s=0}^j\frac{\alpha^s}{s!}[x^j]\bar P^s\\
&=\frac{(-\alpha/2)^r}{r!}[x^j]\overline{\mathbf E_\alpha}.
\end{aligned}
$$

其中 $\mathbf E_\alpha=e^{\alpha P}\bmod x^p$ 的全部系数整。这证明 N1 及差属于 $pR$。在 $R_{\rm for}$ 中，同余保留完整 $H$，没有引入未受控的 $H$ 误差。

一般幅度 $P_1=b/2$ 的 Frobenius 首项常数会是 $(\alpha b/2)^p$，第一带的 $j=0$ 剩余相应为 $-(\alpha b/2)^p$；不能将本式外推为线性的 $b$ 版本。目标的固定量词正确。

### Step 3. 有限指数正规形及四项来源

由 Step 1 的坐标刻画和 Step 2，有

$$
e^{\alpha P}\in\mathfrak F_R,\qquad
\overline{e^{\alpha P}}
=\overline{\mathbf E_\alpha}\left(1-\frac\alpha2\eta+\frac{\alpha^2}{8}\eta^2\right).
$$

给定 $Y,Z\in R[x]_{<p}$，令 $B=\eta Y+\eta^2Z$，在嵌入环中记 $V=P+B=P+x^pY/p+x^{2p}Z/p^2$。在该特征零截断环中，$B^3=0$，指数乘法为准确有限恒等式：

$$
e^{\alpha(P+B)}=e^{\alpha P}
\left(1+\alpha\eta Y+
\eta^2\left(\alpha Z+\frac{\alpha^2}{2}Y^2\right)\right).
$$

除 $2$ 是合法的，右边属于 $\mathfrak F_R$。模 $p$ 后的 $\eta^2$ 坐标来自同一个乘法中的四项

$$
\frac{\alpha^2}{8}
-\frac{\alpha^2}{2}\bar Y
+\alpha\bar Z
+\frac{\alpha^2}{2}\bar Y^2
=\alpha\bar Z+\frac{\alpha^2}{2}(\bar Y-1/2)^2.
$$

这与 $\eta$ 坐标 $\alpha(\bar Y-1/2)$ 一起给出 N2。跨 $x^p$ 的乘法项在整层带因子 $p\eta$；它们消失于模 $p$ 正规形，但属于准确桥的 $pR$ 余项。不能在原指数里预先删去这些进位项。

### Step 4. 实际桥的负下标不是实际置零

给定整的 $Y,Z$ 后，比较上述自由基坐标即可得到 N3a 的非负下标部分。指数低块在所需 $j<p$ 的系数上可用 $e^{\alpha P}$ 代替 $\mathbf E_\alpha$。

对第一带 $j=-1$，实际次数是 $p-1$，其指数系数整。因此

$$
p[x^{p-1}]e^{\alpha V}\in pR;
$$

右侧负下标主项为零，但实际左侧一般非零，可令余项等于该真实整系数。

对第二带 $j=-2,-1$，实际次数 $2p+j$ 落在第一块，故

$$
p[x^{2p+j}]e^{\alpha V}\in R,
\qquad p^2[x^{2p+j}]e^{\alpha V}\in pR.
$$

相应余项可取真实的 $p[x^{2p+j}]e^{\alpha V}$。这样保留了递推在最低几个 $j$ 上的实际 forcing，不是任意指定误差或抹去内部模态。

### Step 5. 已知前缀闭包与两次真实入口

第一入口给

$$
Y^{\rm act}_0=pV_p=(p/h^m)(h^mV_p)\in h^{M-m}R_{\rm act}.
$$

对 $p<n<2p$，假设所有 $pV_i$、$p\le i<n$ 已整，只将这些已知系数放入 $Y$，未知项取零、$Z=0$。这是当前系数计算所需的截断前缀。其指数通过 Step 3 属于 $\mathfrak F_{R_{\rm act}}$。

递推只读 $N=n-1,n-2$。令 $r=\lfloor n/p\rfloor$、$q=\lfloor N/p\rfloor$，则 $q\le r$；已知 $p^q[x^N]e^{\alpha V}$ 整，再乘 $p^{r-q}$ 仍整。把实际递推乘 $p^r$ 后除以单位 $d_n(h)$，得到 $p^rV_n$ 整。取 $r=1$ 即完成第一块，不需要任何第二块系数。

将第一桥代回递推得

$$
d_{p+j}(h)Y^{\rm act}_j+[x^j]J(h)Y^{\rm act}
=\tfrac12[x^j]J(h)+p\varepsilon_j^{(1)},\qquad
\varepsilon_j^{(1)}\in R_{\rm act}.
$$

目标先建立第一模型及 $h^{M-m}$ 比较，再使用原 A04 端点，顺序足够：原 A04 的实际 $V$ 只取至 $2p-1$；action 取第 $2p$ 阶系数，其势能只使用 $[x^{2p-1}]e^V$ 和 $[x^{2p-2}]e^{2V}$。配对项至多使用低块与第一高块，中央项是已经保留的 $V_p^2$。原首个响应只涉及第一模型和低块。

原 A04 端点的两个首层贡献分别为 $(2-L^m)$ 与 $L^m$，合成常数 $2$；其真实倍频关系为

$$
d_{2p}=d_p(4+hd_p).
$$

于是从已接受端点推得

$$
pV_{2p}=
\frac{h^{-2m}p\mathcal B_2}{2h^{-2m}d_{2p}}
=-\frac14+O(h),\qquad
Z^{\rm act}_0=p^2V_{2p}\in pR_{\rm act}=h^MR_{\rm act}.
$$

只有此后，才对 $2p<n<3p$ 以整的完整 $Y^{\rm act}$、已知 $Z$ 前缀重复上述单位步，取 $r=2$。因此第二块整性没有循环使用完整实际 $Z$；“未知前缀项暂取零”并不修改最终实际解。

整性完成后，模 $h$ 有 $Y^{\rm act}_0=Z^{\rm act}_0=0$，N3a 给

$$
p^2[x^{2p}]e^V\equiv1/8,\qquad
p^2[x^{2p-1}]e^{2V}\equiv0\pmod h.
$$

由 $d_{2p+1}\equiv-1\pmod h$ 推得 $p^2V_{2p+1}\equiv1/16\pmod h$，与 A05 原入口一致。这是整性之后的推论，不是整性的前提。

### Step 6. 两条单位模型、形式代入和原始误差

在正次数 $1\le j<p$ 上定义 $\mathcal D_kx^j=d_{kp+j}(H)x^j$，$k=1,2$。每个 $d_{kp+j}(0)=-(kp+j)^2$ 是 $p$-单位，且

$$
J=\frac x2e^P+2Lx^2e^{2P},\qquad
K=\frac x4e^P+2Lx^2e^{2P}
$$

均无常数项。模型精确定义为

$$
(\mathcal D_1+J)\mathscr Y=J/2,\qquad
(\mathcal D_2+J)\mathscr Z=-K(\mathscr Y-1/2)^2\pmod{x^p},
\qquad \mathscr Y_0=\mathscr Z_0=0.
$$

故先唯一确定 $\mathscr Y$，再由已知平方驱动唯一确定 $\mathscr Z$。两个对角逆只依赖 $H$，不含 $L$；固定有限的 $x$ 范围不会产生无界的参数次数。因此它们确属 $R_{\rm for}[x]/(x^p)$，代入 $H=h$ 按 $h$ 进收敛，保持逐系数整性。

第二桥分别取 $\alpha=1,2$ 代回递推时，线性 $Z$ 部分准确形成 $JZ$，平方部分准确形成 $K(Y-1/2)^2$，从而

$$
d_{2p+j}(h)Z^{\rm act}_j+[x^j]J(h)Z^{\rm act}
=-[x^j]K(h)(Y^{\rm act}-1/2)^2+p\varepsilon_j^{(2)}.
$$

系数 $K$ 中第一项为 $x e^P/4$，第二项为 $2Lx^2e^{2P}$，没有漏掉旧块乘第一阶乘带生成的交叉项。

设 $E=M-m$。第一常数差在 $h^E$，其余直接误差 $p\varepsilon_j^{(1)}$ 在 $h^M$。逐个正次数相减，只乘整系数、除单位，得到

$$
Y^{\rm act}-\mathscr Y(h)\in h^ER_{\rm act}[x]/(x^p).
$$

第二平方驱动之差为准确身份

$$
(Y^{\rm act}-1/2)^2-(\mathscr Y(h)-1/2)^2
=(Y^{\rm act}-\mathscr Y(h))(Y^{\rm act}+\mathscr Y(h)-1).
$$

第二因子整，没有再除以 $p$。结合 $Z^{\rm act}_0\in h^M$ 和第二递推中的 $p$ 倍误差，同一单位比较给

$$
Z^{\rm act}-\mathscr Z(h)\in h^ER_{\rm act}[x]/(x^p).
$$

模型常数为零从未被替换为实际常数为零。以上证明与 A06 原式 (20)–(25) 的输入变量、耦合方式及误差完全一致。

### Step 7. 精度边界和最小素数

任意有限整系数多项式组合的实际／模型差，均可逐因子抽出一个块差，所以共同保证仍是 $h^E$。若某一端点项确实另乘属于 $h^m$ 的实际传播子缺陷，才有

$$
h^E\cdot h^m=h^M.
$$

第一实际常数已经给出不能无条件提升的证据：$[L^0](h^mV_p)\bmod h=(-1)^m$ 非零，故

$$
v_h([L^0]Y^{\rm act}_0)=M-m.
$$

所以不可能把两个块整体的共同误差直接写成 $h^M$。目标保留原始界，也保留 A06 后半响应和高精度边界要求，未越界推断。

在 $p=5,a=2$ 的最小边界，$3p=15<25=p^a$、$M=10$、$m=2$、$E=8$；一般证明始终只用 $r!$ 中的 $r\le2$、$s!$ 中的 $s<p$，高块指数只除以 $2$。不存在遗漏 $3!$ 引起的边界问题；三次高块项已在特征零次数截断中消失。这里的数字仅说明一般不等式在端点仍严格成立，不作为无限量词证明的替代。

## Imported Lemmas and Actual Reading Range

以下范围是本审查实际读取的正文，不将作者“已全文读取”的历史说明当成本次读取。除目标全文外，仅按本任务核对必要接口，未重开所有旧阶段。

| 简称与来源 | 本次正文读取范围 | 使用方式 |
| --- | --- | --- |
| [目标 NORMAL_FORM V1](PAPER30_TWIST_FACTORIAL_BLOCK_NORMAL_FORM_DIAGNOSIS_V1_20260908.md) | 1–452，全文 | N1–N3 及全部证明／非主张逐项核查 |
| [A03 POST_POLE_BLOCK V1](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md) | 6–276 | Claim、输入、Steps 1–3；对齐第一阶乘带、入口与实际有限桥 |
| [A04 SECOND_INTERNAL_FORCING V1](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md) | 7–580 | Claim、全部前向依赖及 Steps 1–7；确认常数 $2$ 端点仅依赖第一块及其比较 |
| [A05 SECOND_FACTORIAL_BLOCK V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md) | 6–236 | Claim、输入及 Steps 1–2；对齐入口 $1/16$、四类整性和前缀顺序 |
| [A06 SECOND_FACTORIAL_RESPONSE_BRIDGE V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md) | 6–428；559–597 | Claim、输入、Steps 1–4 与 Step 7；对齐四项耦合、零常数模型、实际误差及不替代的响应接口 |
| [A02 LOCAL_STRUCTURE V1](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md) | 6–193；245–344 | 按 A03／A04 前置依赖补读；定位低块、真实 $V_p$、$d_p$ 剩余和配对和来源 |

读取时各源 SHA256：

| 来源 | SHA256 |
| --- | --- |
| A03 | `0a70394315cfe78b860c6ac46eec53bb58ccb8b3e432c1108438f7e721ee4c34` |
| A04 | `278ce73d9844c8a30b93b8952b8a3a178aa577f1c808fce48c333be721c97f15` |
| A05 | `3ff45f425669adbd012245f5cf605083a72e3cccb131cc6469f787cc58920e04` |
| A06 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |
| A02 | `f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616` |

条件导入且不在本次重新完整认证的旧事实为：局部分圆环及分歧规范；A02 的低块形式分支、第一入口剩余、$d_p/h^{2m}$ 剩余、有限平方传播子与配对和；A04 已接受的真实移位／配对缺陷、第一响应与非驻值 action 端点结论。已核对它们所用变量和范围与目标一致，且 A04 不依赖 A05／A06 或新第二块整性。

本次没有读取 A06 Steps 5–6 或重新推导全部旧非标准端点。这不影响当前接口判定：目标不替代这些部分，且新证明提供的形式模型和实际比较与其原输入一致。A04 后续所需第一实际余项只要求属于 $pR_{\rm act}$；目标已满足，无须额外声称实际余项本身具有未证明的形式 $H$ 提升。

此外，全文读取 `AGENTS.md`、`docs/WORKFLOW.md` 及两项适用技能；仅定向读取当前批次接续中的对象和范围段落。没有查新、浏览外部论文、运行数学样本实验或重扫旧构建树。

## Corrections or Missing Assumptions

未发现本次 N1–N3 所需的新增修正或缺失假设。尤其不需要删除或削弱原参数量词。

必须随接口保留的条件已经写在作者原稿中：无 $p$ 挠元；固定 $P_1=1/2$ 和 $\alpha=1,2$；先整性后约化；两个非单位真实入口；原第二 forcing 常数 $2$；模型零常数与实际常数的区别；平方差；原始 $h^{M-m}$ 误差及端点额外缺陷。将来若删除其中任一条件，应重新检查受影响的断言，不能援引本 PASS 覆盖被扩张的版本。

## Open Risks and Delivery Boundary

本报告支持新有限代数作为原两条阶乘带及四项乘法整性证明的统一替代接口，并支持其非循环实际前缀应用。不据此宣称 B1–B4 全部被删除、完整端点已有新的短证明或自然正文容量已改变；不估节省页数。

本次唯一新增文件为本报告，作者目标和全部旧源保持不改。未改登记册、接受处置、候选票、稿件或 PDF，未创建 Paper30 项目，未作 Route 或对外操作。结论是限定数学审查结果，不是正式候选或产物验收结果。
