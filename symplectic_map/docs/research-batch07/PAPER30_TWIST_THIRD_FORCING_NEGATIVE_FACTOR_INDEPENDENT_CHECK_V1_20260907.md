# Paper30：第三 forcing 负赋值 $p$ 次因子独立边界审查

日期：2026-09-07；审查者：`negative_factor_counterexample`。

## Claim

固定 $p\ge5,a\ge2$，令 $m=(p-1)/2$, $M=p^{a-1}m$, $q_3=3m+1$, $e=M-q_3$。在 $K^+=\mathbb Q_p(h)$、$\mathcal O^+=\mathbb Z_p[h]$、$v_h(h)=1$ 中，已知
$$S=P_{\rm cl}U_{\rm cl},\quad \deg P_{\rm cl}=m,\quad \deg U_{\rm cl}=p,\quad U_{\rm cl}=\sum_{j=0}^p u_jL^j,\quad u_0=a_m\in(\mathcal O^+)^*,\quad u_j\in h^e\mathcal O^+.$$ 
审查能否由这些输入推出负因子的准确 Newton 多边形、因子型及简单性。

## Status

**NOT CURRENTLY JUSTIFIED**。上述同余只推出 $v_h(\beta)\le-e/p$，不足以决定三项目标；下列 DVR 多项式是逻辑比较，不是实际 forcing 反例。

## Assumptions and Notation

记 $\nu_j=v_h(u_j)\in\mathbb Z\cup\{+\infty\}$，$\nu_0=0$。Newton 点为 $(j,\nu_j)$，边斜率 $\sigma$ 对应根赋值 $-\sigma$；根在扩域中按延拓赋值理解。已知 $\nu_j\ge e$（$j\ge1$）。

## Proof Strategy and Dependency Map

先证明当前最大弱结论，再给同一系数下界的不同 Newton 图和残余因子。弱界只用单位常数项与 $\nu_j\ge e$；准确图需相关 $\nu_j$；因子型需每边残余式；简单性需判别式（或导数）证书。

## Proof

**1. 弱界。** 若 $t=v_h(\beta)>-e/p$，则 $v_h(u_j\beta^j)\ge e+jt>0$（$t\ge0$ 时更直接），常数项不能相消，故
$$v_h(\beta)\le-e/p,\qquad \sigma_1=\min_{j\ge1}\nu_j/j\ge e/p.$$

**2. DVR 比较 U1/U2/U3。** 取单位 $a$；未写出的次数可加入赋值高于下凸包的非零项。

- $U_1=a+h^eL^p$：唯一边 $(0,0)\to(p,e)$，全部根赋值 $-e/p$。
- $U_2=a+h^eL+h^{e+2e(p-1)}L^p$：顶点 $(0,0)\to(1,e)\to(p,e+2e(p-1))$，斜率 $e,2e$，根赋值为 $-e$（一重）及 $-2e$（$p-1$ 重）。
- 在 $p=5,a=2$ 时 $e=3$，取 $\bar a=2\in\mathbb F_5$，$U_{3,c}=a+c h^3L^2+h^{10}L^5$（$c=1,2$）。两者同图 $(0,0)\to(2,3)\to(5,10)$，但首边残余式分别为 $2+y^2$（不可约）和 $2+2y^2$（分裂）。故同一 Newton 图也不定因子型；这些只是逻辑比较。

**3. 等号边界。** $e\equiv(p+1)/2\pmod p$，所以 $\gcd(e,p)=1$。由于 $\nu_j$ 为整数，
$$\sigma_1=e/p\Longleftrightarrow \nu_p=e.$$
若 $\nu_p>e$，所有根严格满足 $v_h(\beta)<-e/p$；若 $\nu_p=e$，图为唯一边且根全取 $-e/p$。取 $v_h(\pi)=e/p$、$L=\pi^{-1}y$，归一化剩余为 $\bar u_0+\overline{u_ph^{-e}}y^p=(y-c)^p$，是特征 $p$ 下唯一的 $p$ 重剩余根，普通简单 Hensel 失效。条件性地，$\gcd(e,p)=1$ 还迫使此 $p$ 次因子不可约（真因子度数 $d$ 会给出首尾赋值差 $-de/p\notin\mathbb Z$），故特征零下可分；但目前未证明 $\nu_p=e$。

**4. 边界点值与碰撞。** 在 $t=-e/p$ 时，正因子给出 $v_h(P_{\rm cl}(\ell))=mt$，而 $U_{\rm cl}(\ell)$ 在唯一归一化剩余根处可额外抵消或为零，故现有开区间点值式不能自动延伸。正根赋值 $\ge1/m$，故跨 $P/U$ 不碰撞；负簇内部的同剩余类聚簇、根差和判别式仍未知。

**5. 最小新证书与 $p$ 分母。** 因 $P_{\rm cl}$ 首一，$u_p=[L^{3m+1}]S$；至少须计算
$$c_p=h^{-e}u_p=h^{-M}p^2[L^{3m+1}]\mathcal B_3\pmod h.$$
现有桥只给 $j>m$ 系数在 $h^e$ 中，且模 $h^M$ 恰舍去该层。相关 $[x^p]$ 响应和可能的 $p$ 分母不能由已核查的 $<p$ 阶整性外推；若 $c_p=0$，还须逐层求完整下凸包、每边残余因子及判别式。

## Corrections or Missing Assumptions

- 不把商在整参数处为单位误写成多项式环单位；不把弱界改成严格界或等号界。
- 不把正簇分裂域推广到负簇；DVR 比较式不冒充实际 forcing。

## Open Risks

1. $c_p$ 首层未知，故准确斜率及边界取等未知。
2. 等号边界有值群分母 $p$ 的野分歧；普通 Hensel、根简单性及分裂域未闭合。
3. 多边残余式可分裂或不可约；边界参数点值可能抵消。
4. 本审查未修改作者稿或入口，未扫描/重跑旧检查，也未产生外部效力。
