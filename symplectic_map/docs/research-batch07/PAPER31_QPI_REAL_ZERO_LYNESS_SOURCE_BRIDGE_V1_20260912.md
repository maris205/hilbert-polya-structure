# Paper31：零参数二周期 Lyness 的准确源桥接 V1

日期：2026-09-12 UTC。作者：`/root`。
用途：Phase B 新来源触发的实际同一性增量；不更改原全局数学或已冻结查新输入。
本稿待独立检查；不得先宣称全球首次解决旧猜想。

## Claim

固定 $T>0$，$\lambda=T^{1/3}>0$。原下外无 terminal 圆上的单步 $F_T$ 通过
$$\Phi_T(x,y)=\left(\frac{\lambda^2}{x},-\frac{\lambda y}{x}\right)=(U,V)$$
共轭于 Cima–Gasull–Mañosa 的零参数二步 Lyness 映射
$$L_{0,\lambda}=L_0\circ L_\lambda,\qquad L_\alpha(U,V)=\left(V,\frac{\alpha+V}{U}\right),$$
即
$$L_{0,\lambda}(U,V)=\left(\frac{\lambda+V}{U},\frac{\lambda+V}{UV}\right).$$
这里原一迭代等于文献的两次交替 Lyness 更新，不是原 $F_T^2$。
原正向 $\omega=du/(2v+hu-T)$ 对应文献正象限圆的逆时针方向。
文献能量 $E=V_{0,\lambda}$ 满足 $E=-h$，故
$$\rho^{\rm CGM}_{0,\lambda}(E)=\rho_T(-E),\qquad E>-h_-.$$
这使已接受原下外结论可严格传递到该零参数边界，包括其全部 $\lambda>0$ 的 $5/8$ 无穷端。
断言不包括全部正二参数 Lyness 平面的分类，也不包括此边界结果在文献中的首次证明优先权。

## Status

PROVABLE AS STATED（作者证明；独立检查另存）。

## Assumptions and notation

使用 [Q] 的完整正域双向共轭及圆身份，其新接口已获 [QR] 独立 PASS。
原完整几何和旋转定向采用 [G]、全局结论采用 [S]，数学接受由 [D] 给定；不重审这些未变输入。
文献 [CGM] 记 $F_{b,a}=F_b\circ F_a$，本稿用 $L$ 避免与原 $F_T$ 混淆。
$\rho_T$ 指原下外圆的已接受提升，$\rho^{\rm CGM}$ 指文献逆时针圆上的 $(0,1)$ 提升。

## Proof strategy and dependency map

1. 正域 QRT 接口再接一个单项式坐标变换，逐项核迭代和能量。
2. 计算原微分在正域的取向，再用平面雅可比符号核定文献的逆时针方向。
3. 仅传递已接受的下外端点／严格图；来源先后性与全二参数问题另列未决。

## Proof

### Step 1. 显式双向单步对应

用 [Q] 坐标 $p=-x/y,q=-y$，再 $a=\lambda/p,b=\lambda/q$，原映射变成
$$M_\lambda(a,b)=\left(\frac{a+\lambda}{ba^2},a\right).$$
令 $\Psi(a,b)=(ab,a)=(U,V)$，其正域逆为 $(a,b)=(V,U/V)$。
若 $a'=(a+\lambda)/(ba^2)$，则
$$\Psi M_\lambda(a,b)=(aa',a')
=\left(\frac{\lambda+V}{U},\frac{\lambda+V}{UV}\right)=L_{0,\lambda}\Psi(a,b).$$
三次变换都是整个正域上的微分同胚；其合成为 Claim 的 $\Phi_T$。
例如直接逆为 $x=\lambda^2/U,y=-\lambda V/U$，故确实落回 $x>0,y<0$。
这些等式逐一对应一次原迭代，没有作时间反转或额外平方。

### Step 2. 能量方向

把 [CGM] §2 显示的不变量在其参数 $(b,a)=(0,\lambda)$ 代入，得
$$V_{0,\lambda}(U,V)=\lambda U+\frac{\lambda V}{U}+\frac{\lambda}{V}+\frac{\lambda^2}{U}.$$
再代入 $(U,V)=(ab,a)$，这正是
$$\lambda\left(ab+\frac1a+\frac1b+\frac{\lambda}{ab}\right)=G_T(p,q)=-h.$$
因 [Q] 已证明全部正域非平衡圆恰为 $h<h_-$，文献能量范围准确是 $E>-h_-$。

### Step 3. 角度取向，不只比较数值常数

在 $(p,q)$ 平面上设 $G=G_T$，向量场 $Z=pq(-G_q,G_p)$。
每条 $G=E$ 是围住唯一极小点的简单闭曲线，[Q] 的子水平集是其内部，故 $Z$ 给逆时针定向。
在原椭圆模型的公共图上，[G] 给
$$u=-T/q,\qquad v=-Tp(q+1)/q,\qquad h=-G.$$
逐项消去后有
$$2v+hu-T=-\frac{Tp}{q}G_p,\qquad
\omega=-\frac{dq}{pqG_p}.$$
因此在 $G_p\ne0$ 的开弧上 $\omega(Z)=-1$；等式按光滑性延续到所有圆点。
延续所需开弧稠密：若 $G_p=0$ 沿非空圆弧成立，由 $T=p^2q(q+1)$ 得 $p$ 是 $q$ 的解析函数，
该曲线上 $G$ 不可能在开段常数，除非同时 $G_q=0$，而已知唯一临界点不在正则圆。
也可在 $G_q\ne0$ 的互补图从 $dG=0$ 得 $\omega=dp/(pqG_q)$，直接得到同一取值。
故原正向 $\omega$ 对应 $(p,q)$ 平面的顺时针方向。
双倒数 $R:(p,q)\mapsto(a,b)$ 的行列式为 $\lambda^2/(p^2q^2)>0$；$\Psi$ 的行列式为 $-a<0$。
二者复合反转平面方向，因而把刚才的顺时针送到 $(U,V)$ 的逆时针。
与 [CGM] §5 的实际方向一致，故没有 $1-\rho$ 的补角；结合 Step 2 给 Claim 的旋转数恒等式。

### Step 4. 严格传递的结果及其限度

由 [S] 下外端点，全部 $\lambda>0$ 均有
$$\lim_{E\to+\infty}\rho^{\rm CGM}_{0,\lambda}(E)=5/8.$$
设 $\lambda_c=(3/16)^{1/3}$。由于 $E=-h$，下外严格图准确变为：

| 零参数系数 | 按文献能量 $E$ 增大的行为 |
|---|---|
| $0<\lambda\le\lambda_c$ | 严格递减 |
| $\lambda_c<\lambda<1$ | 先增后减，唯一非退化极大 |
| $\lambda\ge1$ | 严格递增 |

这一传递没有扩展 [S] 的数学内容，仅给它的文献正常形解释。
[CGM] §5 的 $5/8$ 数值猜想由此成为本结果确实回答的一项已有明确问题；
是否已有后续证明或 BR2005 更早等价结论仍须核查，不能用“回答”偷换“首次回答”。∎

## Actual primary reading and source comparison

主代理本轮实际浏览 [CGM] arXiv:0912.5031v1（2009-12-26预印本；Phase B 给正式2012年书目）。
实际使用其 PDF 文本 §2 的 $F_{b,a}$／不变量／Theorem3（印刷pp3–4），
及 §5 的能量、零参数 $5/8$ 猜想（pp13–14）、逆时针说明（p15）和零参数数值列表（p18）。
其它返回段只作背景；不声称全文或原数值证明重新验算。
这两次定向 open 没有新增 query；独立于 Phase B 的36条和 [Q] 主代理11条。
四页 screenshot 尝试中三页 cache miss，另一页只返引用而未显示图像；再次单页亦未显示图像，故不报视觉验读。
[CGM] p18 的零参数列表前段与此表相符，最后一项原文把 $b\in\{1,5\}$ 也写成递减；与本严格传递不符。
原PDF别处同样有方向数值转录疑点，本件不静默替作者改成递增，也不将数值列表升级为定理。
主控采用原显式映射／能量及明确逆时针约定作比较，保留该列表文字差异供后续定位。

## Corrections or missing assumptions

无原全局声明修改；新断言仅为准确正常形、取向与既有结论的传递。
[Q]、Phase B 冻结时“零参数同一性未证明”是当时快照，本件检查通过后才由新处置覆盖。

## Open risks

需独立检查当前新坐标、能量和取向；BR2005后段、Duistermaat强正文及后续优先权缺口不因同一性自动消失。
不把整个原全局五行表称为已有猜想的原句，不把 $a,b>0$ 二参数图说成已解决。
没有 CAS、数值重演、参数扫描、下载、锁或新项目；本件只为同一中心的来源包含性提供真实增量。

[Q]: PAPER31_QPI_REAL_GLOBAL_TWIST_SOMOS_QRT_SOURCE_PROBE_V1_20260912.md
[QR]: PAPER31_QPI_REAL_POSITIVE_QRT_INTERFACE_MATH_REVIEW_V1_20260912.md
[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[S]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[D]: PAPER31_QPI_REAL_GLOBAL_TWIST_MATHEMATICS_DISPOSITION_V1_20260912.md
[CGM]: https://arxiv.org/pdf/0912.5031
