# Paper30：第三内部 forcing 完整 Newton 结构与两两互素的接受处置

日期：2026-09-08。处置者：主控。仅本地研究记录，不是论文立项或产物验收。

状态：`TOP_NONZERO_AND_COMPLETE_NEWTON_ACCEPTED; FIRST_THREE_COPRIME_ACCEPTED`。
本轮四份证明及四份真正非作者独审均已完成，主控全文读取。
原命题统一覆盖全部素数 $p\ge5$、整数 $a\ge2$，无新增科学假设或范围削弱。

## 1. 同一对象与准确新锚点

保持固定参数、实际双谐波递推及 SUM action，取任意本原 $p^a$ 次根 $\zeta$，令

$$h=2-\zeta-\zeta^{-1},\quad K^+=\mathbb Q_p(h),\quad v_h(h)=1,$$
$$m=(p-1)/2,\quad M=p^{a-1}m=v_h(p),\quad D=3m+1=p+m,\quad
\chi=(-1)^{m+1}.$$

定义实际内部 forcing

$$\mathcal B_k(L)=-[x^{kp-1}]e^V-2L[x^{kp-2}]e^{2V},\quad k=1,2,3,$$
$$C_D=[L^D]\mathcal B_3,\qquad
S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl},\quad
U_{\rm cl}=\sum_{r=0}^pu_rL^r.$$

本轮准确得到

$$\boxed{pC_D=-\frac3{16}h^p+O(h^{p+1}),\qquad
u_p=-\frac3{16}p h^{-m}(1+O(h)),\qquad v_h(u_p)=M-m.}$$

这是此前最高项下界的首次非零证明。先在 $4^D$ 规范得到 $-3/4$，
再用 $4^D\equiv4$，不是 $16$，换回实际剩余 $-3/16$。
$p\ge5$ 保证该剩余非零。

三项同阶来源均已控制：

| 新输入 | 准确内容 | 接受依据 |
| --- | --- | --- |
| 第一 forcing 最高项下一层 | $[L^m]\mathcal B_1=-\chi H^m-\chi H^{m+1}/16+O(H^{m+2})$ 模 $p$；第三端点线性新层为 $-1/4$ | 作者全文及19项非作者检查 |
| 有限参照的首个 ghost | 缺陷常数 $\eta=1+h^p/4$ 同时缩放实际两条高带与完整端点，净新层贡献为零 | 作者全文及26项非作者检查 |
| 完整二次响应下一层 | $\mathfrak c_{2,1}=-1/2$；包含非恒定二次移位、平方系数变化和所有端点乘积 | 作者全文及独审全部10节 |

有限伴随身份只在 $\mathbb F_p$ 成立。六核的卷积计算使用其 $p$ 整特征零代表，
不将原响应端点的模 $p$ 等式升级为特征零等式，也不将伴随误差除以 $p$。
四次被加数先整体抵消为三次，再使用幂和，因此没有 $p=5$ 时非法的 $1/5$。
实际污染及三次反馈从 $p+1$ 阶起被排除；最小素数处恰达此边界，
当前误差控制不能外推到模 $h^{p+2}$。

## 2. 完整 Newton 图、因子型及单根域

既有中间系数界保持：

$$v_h(u_r)\ge M-p\quad(1\le r\le m),\qquad
v_h(u_r)\ge M-m-1\quad(m+1\le r<p).$$

令 $b=M-m$、$e_*=M-D>0$。准确差值

$$\frac{M-p}{m}-\frac bp=\frac{(p-m)e_*}{mp}>0,\qquad
\frac{M-m-1}{p-1}-\frac bp=\frac{e_*}{p(p-1)}>0$$

使所有中点严格位于首常端点连线上方。因此

$$\boxed{\operatorname{NP}(U_{\rm cl}):(0,0)\longrightarrow(p,M-m),
\qquad v_h(\beta)=-(M-m)/p.}$$

$\gcd(p,M-m)=1$ 强制负因子在 $K^+[L]$ 上不可约；特征零保证可分。
合并[既有统一正簇](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_DISPOSITION_20260907.md)，得到

$$\boxed{\operatorname{NP}(S):(0,m-1)\longrightarrow(m,0)\longrightarrow(D,M-m).}$$

第三 forcing 恰有次数 $m,p$ 的两个不可约因子，自身可分。
每个负根域 $F_\beta=K^+(\beta)$ 满足 $[F_\beta:K^+]=e=p,f=1$，为野全分歧扩张。
既有正簇的循环分裂域 $E$ 仍满足 $[E:K^+]=e=m,f=1$；其与任一负根域的合域满足

$$[EF_\beta:K^+]=e(EF_\beta/K^+)=mp,\qquad f(EF_\beta/K^+)=1.$$

这个合域未被认定为整个第三 forcing 的分裂域；不同负根域是否相同亦未判定。
中间系数各自下界层是否非零仍未逐项求出，但不妨碍上述完整下凸包结论。

## 3. 首三个内部 forcing 两两互素

第二 forcing 的真实次数是 $p$，不能以错误的“小于 $p$”排除公共负因子。
从同一纯偶递推和准确倍角缩放得到

$$[L^p]\mathcal B_2
=2\left(\frac4{4-h}\right)^{p-1}\mathcal B_1(h(4-h),0)
=4\chi h^m+O(h^{m+1}).$$

结合已接受的 $h^{-2m}p\mathcal B_2\equiv2\pmod h$ 以及
$u_0=-3\chi/64+O(h)$，两者的最高项／常数项之比分别为

$$2\chi p h^{-m}(1+O(h)),\qquad4\chi p h^{-m}(1+O(h)).$$

公共尺度下差的剩余为 $-2\ne0$，故次数同为 $p$ 的 $\mathcal B_2,U_{\rm cl}$ 不成比例。
负因子的不可约性排除它们有公共根；整参数单位式排除第二项与正簇有公共根。
第一 forcing 的根均在单位圈，结合既有第一／第二互素，得到

$$\boxed{\gcd(\mathcal B_i,\mathcal B_j)=1\quad(1\le i<j\le3).}$$

本处置不将第二 forcing 的准确次数、最高项和互素性扩张为其完整 Newton 图或简单性。

## 4. 全参数点值及尚未简化的负临界圈

记 $t_-=-(M-m)/p$、$t_+=(m-1)/m$，正根为 $\alpha_j$，负根为 $\beta_k$。
对任意有限扩域中的非零参数 $\ell$，令 $t=v_h(\ell)$，则

$$v_h(S(\ell))=
\begin{cases}
Dt+b,&t<t_-,\\
mt_-+b+\displaystyle\sum_{k=1}^pv_h(\ell-\beta_k),&t=t_-,\\
mt,&t_-<t<t_+,\\
(m-1)t_++\max_jv_h(\ell-\alpha_j),&t=t_+,\\
m-1,&t>t_+.
\end{cases}$$

$\ell=0$ 时为 $m-1$；根处允许无穷值。两临界圈均已包含，但负圈保留完整距离和，
不能换成尚未证明的单个最大距离。实际换算保持

$$v_h(\mathcal B_3(\ell))=D-2M+v_h(S(\ell)),\qquad
v_h(V_{3p}(\ell))=m+1-2M+v_h(S(\ell)).$$

## 5. 独审绑定与保留的文字边界

| 本轮作者证明 | 真正非作者独审 |
| --- | --- |
| [第一 forcing 下一层](PAPER30_TWIST_FIRST_FORCING_TOP_NEXT_LAYER_PROOF_V1_20260908.md) | [19项PASS](PAPER30_TWIST_FIRST_FORCING_TOP_NEXT_LAYER_INDEPENDENT_CHECK_V1_20260908.md) |
| [首 ghost](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_PROBE_V1_20260908.md) | [26项PASS](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_GHOST_INDEPENDENT_CHECK_V1_20260908.md) |
| [完整二次响应新层及实际非零项](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_PROBE_V1_20260908.md) | [全文PASS](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HP_RESPONSE_INDEPENDENT_CHECK_V1_20260908.md) |
| [完整 Newton 结构与互素](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_NEWTON_AND_COPRIME_PROOF_V1_20260908.md) | [26项PASS](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_NEWTON_AND_COPRIME_INDEPENDENT_CHECK_V1_20260908.md) |

按上表每行“作者、独审”的顺序，冻结 SHA256 为：

```text
e22080d67d9369db83428095141f1c8f63ad8bee7de5d3bec19135c8e76a8925
dcb820873b8efb08ce739cae60daeb06f2e946d8da2c664742d363f25d40b472
9a4b698fe1a4f4e236010e735c0105bb687fd9ebf554e36840e2b9302f8c4894
cfe56e4f4dc4143111062c4738a1cf53cdbcf8c1bbcb92f965677215ec5f888e
a21428c1dc49fcefc523c98cc8c8910ac1fc5627443769e1427f5d68c601bc48
9bae4ac0e7b611ff42a6d830892efb21bc42120aae6dd0dd488cddc67260e3f9
0de73ed23ab07d32b76823cdad81d3642fc259eaf1a20bfc981697d5bae0269c
b6015c4eec6c6dcebbb9545f704410f56820a58e9a9f5489a951799b8cbed02e
```

结构独审对新最高项原本只核条件应用；现在其三个实际输入及响应本身均已另获独审，
因此在本统一处置中依赖闭合，不再保留未证明的非零条件。
响应稿 §6 的特征零代表说明以该独审第7节为准，不授予额外强读。
结构稿所称倍角身份在旧分界稿 Step 4 的定位有偏差，实际在 Step 5、式(20)—(21)；
结构稿已自含重新推导，独审认定此处非阻断。冻结稿不为这些说明原地改写。

[上轮系数界与二次边界接受记录](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_UPPER_BOUNDARY_AND_QUADRATIC_DISPOSITION_20260908.md)
及全部更早证明、原约化错误与字面FAIL保持原样，未重跑未变审查。
作者协作和固定五的定向核算不替代上述一般证明与真正非作者独审。

## 6. 后续范围与产物状态

已闭合：第三内部 forcing 的完整 Newton 图、准确根赋值、不可约因子次数、简单性、
正簇完整分裂域、负簇单根域的次数和分歧，以及首三内部 forcing 两两互素。

仍开放：负根彼此的准确距离、负因子的完整野分裂域与 Galois 群、第二 forcing 的完整图和简单性；
非真共振三的幂的剩余互素问题、完整素数幂最终 $C,Q$、其他合数和实际参数根全实性。
这些开放任务不是已接受第三 Newton 图的缺失假设；也不将内部 forcing 结果冒充最终 $C,Q$ 的证明。
全局查新和去重后的论文价值仍需单独核验，数学接受本身不授予新意或正文容量。

Batch07 仍为本地验收3/5；Paper30未立项、Paper31未开展。
正文22–30页和独立验收要求保持；本轮未估页、未投正式候选票、未试写测页，
没有新论文项目、PDF、Route评价、投稿、上传或其他外部效力。
