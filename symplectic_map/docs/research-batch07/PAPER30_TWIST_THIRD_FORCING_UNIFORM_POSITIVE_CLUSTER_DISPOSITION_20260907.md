# Paper30：第三 forcing 的统一正根簇处置

日期：2026-09-07。状态：TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_ACCEPTED。

本轮继续此前一般 $p\ge11$ 的高阶响应／支撑义务，得到了统一覆盖全部
$p\ge5,a\ge2$ 的完整正赋值根簇定理。没有逐素数补表或由五、七的幂外推。
数学接受不等于论文立项：Batch07 仍为 Papers27–29 已验收 **3/5**，
Paper30 未立项、Paper31 未开始，22–30 页实质正文及最终独立验收要求保持。

## 1. 新输入与真正独立检查

三个新作者包和一个真正非作者报告共同绑定本轮证据。

| 文件 | 行数 | SHA256 |
| --- | ---: | --- |
| [高阶响应结构 V1](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md) | 393 | `af5cd169e101948d9732cf9f913181ba2697e9fa9b4a848eebd1ffda841f21d1` |
| [临界投影 V1](PAPER30_TWIST_THIRD_FORCING_CRITICAL_PROJECTION_PROBE_V1_20260907.md) | 482 | `c7bad052293f96ab95f7e48026472e06b114a21eb71d6c34e964b0903142e345` |
| [统一正簇 V1](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_PROBE_V1_20260907.md) | 475 | `870d90ff0e9eb85f9ae174c0a2f79a624454ed248db0acbd546b44e7856b28f6` |
| [真正非作者联合核查](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_INDEPENDENT_CHECK_20260907.md) | 391 | `e2c62baa7fe44890db9fa8edb2b673b5f8aff74e8bc318183d2d9a9f626f9afa` |

作者分工为：高阶结构由 `p30_twist_leading_structure_probe` 推导；
临界投影由 `p30_third_forcing_general_independent` 推导、主控共同完成有限和；
统一端点压缩与根簇由主控推导，两位作者交叉核算。
这些交叉核算均不算非作者审查。

真正非作者是 `p30_root_cluster_and_p5_independent`：本轮未参与上述推导或作者文件修改，
全文读取三个冻结输入后独立核算并给出 **44 项 PASS**，没有未解决的新问题。
主控已全文读取三份作者稿与联合报告，检查报告针对实际冻结输入；
未由代理的历史角色名推定独立性，也没有用作者消息代替审查。
其中10个局部代数身份还由核查者自写符号脚本精确验证，exit 0；
它们是44项检查的执行辅助，不另计为新的定理票，也不替代归纳、整性或局部域证明。

本轮只核查新增证明、实际调用和结论边界，没有重跑上一轮未变的39项。
先前已接受首层、第二层、特殊素数表、阶乘桥和原次数均作为明确依赖使用。
作者稿首冻前的录入修正未改变公式；主控一次静态检查误将行首数学分隔符数
当成全部分隔符数，定位为检查表达式遗漏同行闭合符后窄修，三个作者稿均通过。
该检查误报不是科学反例，也未触发旧证明重跑或通用基础设施改造。

## 2. 模型与实际规范不变

同一双谐波模型、固定参数、物理正 kick 与 SUM action 保持。任取素数
$p\ge5$、$a\ge2$ 和本原 $p^a$ 次根 $\zeta$，使用

$$
h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,\quad
m=(p-1)/2,\quad M=p^{a-1}m,\quad \chi=(-1)^{m+1},
$$
$$
K^+=\mathbb Q_p(h),\quad \mathcal O^+=\mathbb Z_p[h],\quad
v_h(h)=1,\quad v_h(p)=M,\quad q_3=3m+1,\quad e_*=M-q_3.
$$

实际 $V_n=\rho^nv_n(L/\rho)$、$d_n=-D_n/h$，并定义

$$
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V},\qquad
S=h^{-q_3}p^2\mathcal B_3.
$$

不与旧分母 $2p$ 的 $h=D_2$ 规范混用。已接受的实际次数 $3m+1$、
唯一 $S=P_{\rm cl}U_{\rm cl}$ 保持：$P_{\rm cl}$ 首一次数 $m$，
$U_{\rm cl}$ 次数 $p$，且

$$
P_{\rm cl}\equiv L^m\pmod h,\qquad
U_{\rm cl}\equiv a_m=[L^m]S\pmod{h^{e_*}},\qquad
a_m=-3\chi/64+O(h).
$$

负簇恰有 $p$ 个根计重数，仍满足 $v_h(\beta)\le-e_*/p$。
本轮不会因剩余次数下降而删除它们。

## 3. 闭合的一般机制

### 3.1 高阶有理性不是经验规律

令 $u=x/4$、$R_{k,j}=[H^kL^j]P(H,L,4u)$。新证明给出：

- $R_{0,0}=-2\log(1-u)$。
- 对全部 $n=k+j\ge1$，$R_{k,j}$ 为只有 $u=1$ 可能有极点的有理函数，
  极点阶数至多 $2n$，在零端点为零、在无穷远有限。
- 对 $1\le n\le m$，整个有理函数为 $p$-整，且与真实有限低块约化一致。

证明从真实 Chebyshev 偶微分算子出发，显式构造逐项能量原函数。
两端导数为 $+1,-1$，故能量端点相同，消掉有理线性响应的唯一端点障碍。
整性则由前 $p$ 个 Taylor 系数恢复次数至多 $p-1$ 的有理分子，
不要求积分表达式的每个表面分母单独为单位。

“无穷远有限”不能改成“无穷远为零”：正总阶响应的正阶导数才在那里消失。
这一区别用于后续有限系数核的端点提取。

### 3.2 完整端点的算子取消

令 $\Omega_i=i\mathsf S_i$、$W=\sum_{i=1}^{p-1}\Omega_iP_iP_{p-i}$。
有理核给出全部预临界矩

$$
[H^kL^j]W=\delta_{j0}\frac{(k!)^2}{(2k+1)!}\qquad(k+j<m).
$$

取总次数算子 $\mathscr E=H\partial_H+L\partial_L$，完整四项三次端点满足

$$
\mathcal F_3=\frac38
\left\{\mathscr E^2+\frac{2(H-1)}{H-4}\mathscr E+\frac H{H-4}\right\}W
\pmod{H^m}.
$$

这里反射偶性仅用于 $H<m$ 的合法层，保留第一配对项才会消尽权重导数。
对 $j>0,k+j=m$，总次数乘子 $m(m+1/2)$ 在特征 $p$ 为零；
额外正 $H$ 因子只调用已经消失的低总阶混合矩。因此

$$
[H^kL^j]\mathcal F_3=0\qquad(j>0,\ k+j\le m).
$$

临界混合矩自身无需为零，也未被断言为零；其整体 $p$ 整性确保上述乘法合法。
这一步填补的是一般参数支撑，而不是再增加一个特殊素数层。

### 3.3 临界反射缺陷与真实常数碰撞

真实整数 Chebyshev 系数先取临界投影，再约化，给

$$
[H^m]d_i=2\chi i\,\mathbf1_{i>m},\qquad
[H^m]\mathsf S_i=-\chi\,\mathbf1_{i>m}.
$$

由此保留反对称端点的 $3\chi/16$ 修正。预临界标量层全部为零；
临界微分转移把未知高阶响应消去，仅留下已知低阶矩的有限和。
望远镜终项先在有理数中约去 $p$，再用 Wilson 定理约化，得到

$$
\mathcal F_3(H,0)=\frac{3\chi}{32}H^m+O(H^{m+1}).
$$

同阶必须保留已接受的四次移位项：

$$
\mathcal E=r^3\mathcal F_3(H,L)+r^4E_4(L)+O(H^{4m+1}),\quad
r=2\chi H^m+O(H^{m+1}),\quad E_4(0)=-3/32.
$$

所以实际总层来自两项之和，不是 $E_4(0)$ 单项：

$$
[H^{4m}]\mathcal E(H,0)
=(2\chi)^3\frac{3\chi}{32}+(2\chi)^4\left(-\frac3{32}\right)
=-\frac34.
$$

对全部 $p\ge5,a\ge2$，实际精度 $M\ge pm\ge4m+1$，
并有 $e_*=M-3m-1\ge m$。原实际桥因此足以得到

$$
S(0)=-\frac34h^{m-1}+O(h^m),\qquad
[L^j]S\in h^{m-j}\mathcal O^+\quad(1\le j<m).
$$

四次项在正规化后从 $h^{m-1}$ 起，满足全部上述正参数系数界；
没有在证明中将它删去。

## 4. 统一接受的实际正簇定理

写 $P_{\rm cl}=L^m+\sum_{j=0}^{m-1}b_jL^j$。对全部 $p\ge5,a\ge2$，

$$
b_0=16\chi h^{m-1}+O(h^m),\qquad
b_j\in h^{m-j}\mathcal O^+\quad(1\le j<m).
$$

全部中间系数点严格位于连接 $(0,m-1)$、$(m,0)$ 的直线上方。
因此只有一条 Newton 边；每个正根的准确赋值为

$$t_*=(m-1)/m.$$

取 $\kappa^m=-16\chi h^{m-1}$。赋值分母为 $m$，且 $\mu_m\subset\mathbb Q_p$，
故 $E=K^+(\kappa)$ 是全分歧循环 $m$ 次扩张。
在 $E$ 内的准确缩放 $P_{\rm cl}(\kappa y)/\kappa^m$ 约化为 $y^m-1$，
具有 $m$ 个不同简单剩余根。Hensel 提升给出全部实际根，
而每根的赋值分母又强制其生成域次数为 $m$。于是：

$$
P_{\rm cl}\ \text{不可约且可分},\qquad
K^+(\alpha_j)=\operatorname{Spl}_{K^+}(P_{\rm cl})=E,
$$
$$
[E:K^+]=e(E/K^+)=m,\quad f(E/K^+)=1,\qquad
v_h(\alpha_j)=v_h(\alpha_i-\alpha_j)=t_*\quad(i\ne j).
$$

按 $\omega_j\in\mu_m$ 标签，$\alpha_j=\omega_j\kappa+O(h)$。
对 $p\ge7$，已接受次首系数另给

$$
\alpha_j=\omega_j\kappa-\frac{41}{384m}h+O(h^{1+1/m}).
$$

$p=41$ 时平移系数自身更高赋值，公式和误差界仍成立。
上述分裂域仅指正簇 $m$ 次因子，不是完整 $3m+1$ 次 forcing 的分裂域。

对任意有限扩域中的非零 $\ell$，若 $t=v_h(\ell)>-e_*/p$，负因子在该点是单位，
所以

$$
v_h(S(\ell))=
\begin{cases}
mt,&t<t_*,\\
(m-1)t_*+\max_jv_h(\ell-\alpha_j),&t=t_*,\\
m-1,&t>t_*.
\end{cases}
$$

在共同有限扩域中理解距离，根处允许无穷值；$\ell=0$ 时为 $m-1$。
负端点 $t=-e_*/p$ 仍排除。实际 $\mathcal B_3,V_{3p}$ 的赋值分别加
$q_3-2M$、$m+1-2M$。这个结果包含非整参数的合法区间，
也保留临界根附近的额外抵消。

## 5. 保留项、下一义务与产物边界

[上一轮一般第二层与七的幂处置](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_AND_SEVEN_POWER_DISPOSITION_20260907.md)
全部保持，包括三个二阶矩、四次剩余多项式、原七的幂有限证书，
以及根界 V1 措辞失败和 V2 的窄修记录。
[五的幂二次域](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_AND_FIVE_POWER_DISPOSITION_20260907.md)
与七的幂三次域均被统一结果覆盖，原证明不改写。
[三的幂及此前结果](PAPER30_TWIST_THIRD_FORCING_DISPOSITION_20260907.md)
继续按其原精确范围接受；一般第一／第三 forcing 互素未被删除或放大。

下一一般对象是负赋值次数 $p$ 因子的准确斜率、因子型和简单性。
一般 $p\ge5$ 及非真共振三的幂的第二／第三 forcing 互素仍开放；
完整素数幂 $C,Q$、其他合数和实际参数根全实性也未完成。
不再把全部 $p\ge5$ 正簇的 Newton 边、不可约性、简单性、单根域和分裂域列为 OPEN。

本轮 `proof-writer` 要求使新证明明确分开：
高阶有理性、临界奇偶修正、真实误差桥和局部域推论；
未将数值观察、静态文件检查或运行成功代替定理证明。
通用 Lindstedt／Hill／Suris、Hensel／Kummer 工具仍从系统新意中扣除。
本件没有全局新意认证、自然正文估页或正式候选票，
没有 Paper30 项目、论文源码、PDF、Route 评价、对外上传、投稿或外部资源操作。
只更新本处置及当前 BATCH／发现状态／README 入口；历史尾部、原失败和已接受产物保留。
