# Paper31：零参数二周期 Lyness 桥接独立数学审查 V1

批次日期标签：2026-09-12，沿用文件名，不作为执行时钟认证。审查者：`/root/p31_real_positive_qrt_interface_check`。
被审稿作者：`/root`。本轮仅核 [NEW] 新增桥接；既有 [Q]、[G]、[S] 及数学接受状态不重审。

## Claim

固定 $T>0$、$\lambda=T^{1/3}$，$\Phi_T(x,y)=(\lambda^2/x,-\lambda y/x)$ 在原下外 $C^1$ 上满足
$$\Phi_T F_T\Phi_T^{-1}=L_0\circ L_\lambda,\qquad L_\alpha(U,V)=\left(V,\frac{\alpha+V}{U}\right).$$
原单步对应两次交替 Lyness 更新；原正向微分 $\omega=du/(2v+hu-T)$ 对应目标圆的逆时针定向。
目标能量 $E=V_{0,\lambda}$ 等于 $-h$，从而 $\rho^{\rm CGM}_{0,\lambda}(E)=\rho_T(-E)$ 对全部 $E>-h_-$ 成立。
因此 [S] 的下外端点、严格单调性与唯一非退化极大按 [NEW] 的三行表传递。

## Status

**PASS — PROVABLE AS STATED。** 新 Claim 原样成立；没有必需数学修正。
通过对象包括坐标、能量、圆定向、迭代单位及严格表的转移，不包括来源优先权或全正二参数分类。

## Assumptions

- [Q] 已接受的正域接口为 $p=-x/y>0,q=-y>0$、$G=pq+p+q+T/(pq)=-h$。
- $R(p,q)=(\lambda/p,\lambda/q)=(a,b)$ 将原单步变为 $M_\lambda(a,b)=((a+\lambda)/(ba^2),a)$。
- [Q] 的非平衡正域圆准确是全部下外无 terminal 的 $C^1$；[G] 提供原微分及椭圆模型接口。
- [S] 的下外旋转数提升属于 $(0,1)$，采用 $\omega$ 正向，其严格表与端点作为已接受输入消费。

## Notation

$h$ 是原能量，$E$ 是 CGM 能量；$h_-=w_-(3-2w_-)$，其中 $w_-<0$、$T=w_-^3(w_--1)$。
$\Psi(a,b)=(ab,a)=(U,V)$；$Z=pq(-G_q,G_p)$ 是辅助切向量场，不是新增离散迭代。
本件的坐标 $a,b$ 不等于来源两参数的名称；来源参数顺序保持 $F_{b,a}=F_b\circ F_a$。

## Proof strategy and dependency map

1. 显式复合和逆映射核对单步及完整正域；来源不变量只作逐项参数代入。
2. 在正则圆上算 $\omega(Z)$，再消费平面雅可比符号，确定实值旋转提升而非仅模一相等。
3. 对已接受函数作 $h=-E$ 的链式法则；来源观察与独立数学结论分别记录。

## Proof

### Step 1. 共轭与迭代单位：PASS

$\Psi^{-1}(U,V)=(V,U/V)$，故它是整个正象限的微分同胚。
若 $a'=(a+\lambda)/(ba^2)$，则
$$\Psi M_\lambda(a,b)=(aa',a')=\left(\frac{\lambda+V}{U},\frac{\lambda+V}{UV}\right)=(L_0\circ L_\lambda)\Psi(a,b).$$
与既有 $R,D$ 复合给 $\Phi_T$，其逆为 $x=\lambda^2/U,y=-\lambda V/U$，全域无零分母。
每个 $L_\alpha$ 在 $\alpha\ge0$ 时的逆为 $L_\alpha^{-1}(U,V)=((\alpha+U)/V,U)$，故目标也双向保正。
一次 $F_T$ 准确对应一次复合 $L_0\circ L_\lambda$，不是 $F_T^2$，也不是其逆。
CGM 的旋转数本来就是复合映射的圆角，故后续旋转数不再乘二或除二；原上外回返完全未被引用。

### Step 2. 来源参数与能量：PASS

[CGM] §2 显示的 $F_{b,a}$ 在 $(b,a)=(0,\lambda)$ 下正是上述复合；不需要把其正参数定理外推到边界。
同段不变量直接代入给
$$V_{0,\lambda}(U,V)=\lambda U+\frac{\lambda V}{U}+\frac{\lambda}{V}+\frac{\lambda^2}{U}.$$
置 $(U,V)=(ab,a)$ 后为 $\lambda(ab+1/a+1/b+\lambda/(ab))=G=-h$，无额外比例或加性常数。
因此目标全部正则正域圆恰取 $E>-h_-$；$E=-h_-$ 仅为平衡点，不在圆旋转声明中。

### Step 3. 微分、平面方向与实值提升：PASS

由 [G] 的原有公式在本图得 $u=-T/q$、$v=-Tp(q+1)/q$、$h=-G$。
直接展开给
$$2v+hu-T=\frac{T}{q}\left(-pq-p+\frac{T}{pq}\right)=-\frac{Tp}{q}G_p,\qquad du=\frac{T}{q^2}dq.$$
故在 $G_p\ne0$ 处 $\omega=-dq/(pqG_p)$，而 $dq(Z)=pqG_p$，所以 $\omega(Z)=-1$。
延续没有遗漏：$G_p=0$ 等价于 $p=\sqrt{T/[q(q+1)]}$；若它占一个正则能级开弧，则以 $q$ 为坐标求导给 $G_q=0$。
这与正则性冲突，故 $G_p\ne0$ 的部分稠密；$\omega$ 与 $Z$ 光滑，等式延至全圆。
在 $G_q\ne0$ 的互补图也有 $\omega=dp/(pqG_q)$，仍取值 $-1$。
该圆所围闭盘为 $G\le E$ 的子水平集，梯度向外；$Z=pq(-G_q,G_p)$ 因此逆时针，原 $\omega$ 正向则顺时针。
$\det DR=\lambda^2/(p^2q^2)>0$，$\det D\Psi=-a<0$；正域微分同胚把圆盘内部送到内部，故复合反转圆边界方向。
于是原正向被送到 $(U,V)$ 的逆时针，与 [CGM] §5 的明确约定一致，不产生补角 $1-\rho$。
保向圆共轭先给旋转数模一相等；两端均选 $(0,1)$ 提升，遂得到准确实值等式 $\rho^{\rm CGM}(E)=\rho_T(-E)$。

### Step 4. 严格表、端点与边界交换：PASS

链式法则给 $(\rho^{\rm CGM})'(E)=-\rho_T'(-E)$、$(\rho^{\rm CGM})''(E)=\rho_T''(-E)$。
因此单调方向翻转，但非退化极大仍为非退化极大；唯一性也由 $E=-h$ 的一一性保留。
令 $\lambda_c=(3/16)^{1/3}$，所得表为

| 参数范围 | 按 $E$ 递增的严格行为 |
|---|---|
| $0<\lambda\le\lambda_c$ | 导数处处负 |
| $\lambda_c<\lambda<1$ | 先增后减，恰一非退化极大 |
| $\lambda\ge1$ | 导数处处正 |

两个阈值处的严格性直接消费 [S]，没有由邻近参数连续性猜出；$E\to\infty$ 正是 $h\to-\infty$，故极限为 $5/8$。
为核 p18 的相反参数顺序，另有 $(L_\lambda\circ L_0)L_\lambda=L_\lambda(L_0\circ L_\lambda)$、$\det DL_\lambda>0$。
并且 $V_{\lambda,0}(U,V)=\lambda V+\lambda U/V+\lambda^2/V+\lambda/U$ 满足 $V_{\lambda,0}\circ L_\lambda=V_{0,\lambda}$。
故两条零参数边界在同一能量、同一方向上对应；这不增加迭代次数，也不覆盖 $\lambda=0$ 或全部正二参数平面。∎

## Corrections or missing assumptions

无必修项。可选最小澄清：主稿来源列表比较处可补上述保向参数交换，以显式解释为何能比较其 $a=0$ 数值列表。
主稿唯一排版漏斜线已由作者修正；本意见只针对修正后的 123 行 / 7175 bytes 身份。

## Open risks and actual read scope

本轮两次 direct open 实际核到 [CGM] §2 印刷 pp3–4 的映射/不变量及 §5 pp13–15、18 的相关文本，非全文或图像验读。
其零参数 $5/8$ 是数值支持的问题陈述；p18 最后一项确写 “decreasing”，与本严格转移在 $\lambda\in\{1,5\}$ 的结果相冲突。
本件不静默改该词，也不以数值列表代替证明；回答该明确问题成立，不代表已认证首次证明或后续文献不存在。
FULL 读 proof-writer 技能、修正后 [NEW]、[S] 的 133 行 / 6753 bytes；既有 [Q]/[G] 仅消费上轮已读接口。
[NEW] SHA-256：`3c5809411c9979b6d6702dbb867af85fce78dff15fb568fddabc204dbc2d5ceb`。
没有 query、PDF 下载、CAS、数值、扫描、构建、再委派；旧 97 行审查与主稿、锁、冻结输入均未改。

[NEW]: PAPER31_QPI_REAL_ZERO_LYNESS_SOURCE_BRIDGE_V1_20260912.md
[Q]: PAPER31_QPI_REAL_GLOBAL_TWIST_SOMOS_QRT_SOURCE_PROBE_V1_20260912.md
[G]: PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md
[S]: PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md
[CGM]: https://arxiv.org/pdf/0912.5031
