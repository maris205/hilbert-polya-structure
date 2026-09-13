# 实际正弦传播子的保根算子：定点先例与适用范围

日期：2026-09-07。主控使用 `research-lit`，仅作本轮新算子结构的定点来源检查。
这是文献辨析，不是独立数学审查、正式新意票或新的论文候选。
奇素数首项简单性和次项非零的已接受证明未重开。

## 1. 核对结果

有限次数的线性保实根算子已有完整分类。因而把正弦系数乘子放入该分类、
验证符号多项式或使用辐角证明，只能计作本题的工具应用，
不能把通用保根准则或其行列式描述当成本文新贡献。

| 一手材料 | 阅读范围与结论 | 当前用途及边界 |
| --- | --- | --- |
| Julius Borcea、Petter Brändén，*Pólya–Schur master theorems for circular domains and their boundaries*，Ann. of Math. (2) 170 (2009), no. 1, 465–492 | 已读[官方元数据](https://arxiv.org/abs/math/0607416)及[作者全文](https://arxiv.org/pdf/math/0607416)的引言、定义1–3、Theorem 1和Theorem 2陈述；采用作者v6，PDF第5页的有限次数定理 | 给定线性算子，其齐次二变量符号实稳定足以推出保实根。这里仅把它用于实际传播子这个线性算子，不用于非线性共振多项式递推。 |

该文 Theorem 2 的一个适用方向是：若
$T:\mathbb R_d[t]\to\mathbb R[t]$ 为实线性算子，且
$T[(z+w)^d]$ 在 $\operatorname{Im}z,\operatorname{Im}w>0$ 时不为零，
则 $T$ 保持实根性。对正的对角系数，非正实根输入的系数同号，
输出仍同号，因此其实根不会变成正根；常数项非零时也不会新增零根。
这是已有定理的应用，不是本轮重新证明的一般分类。

## 2. 五分母例外的符号核对

以下是主控由该定理作出的本题推论，已发送给结构作者进一步核对；
本文本身不充当这项推论的独立认证。
对 $s=5$、$r\equiv\pm2\pmod5$，令

$$D_n=4\sin^2(\pi rn/5),\qquad
\alpha=D_1^{-1}=D_4^{-1},\qquad
\beta=D_2^{-1}=D_3^{-1}.$$

对 $tP(t)$ 提取一个 $t$ 后，逆传播子对应的对角算子为
$T(t^k)=D_{k+1}^{-1}t^k$、$0\le k\le3$。其符号是

$$\begin{aligned}
T[(z+w)^3]
&=\alpha(w^3+z^3)+3\beta(zw^2+z^2w)\\
&=\alpha(z+w)\bigl(z^2+c zw+w^2\bigr),\\
c&=3\beta/\alpha-1
=3(3+\sqrt5)/2-1>2.
\end{aligned}$$

令 $u=(c+\sqrt{c^2-4})/2>0$，二次因子为
$(z+u w)(z+u^{-1}w)$。三个线性因子在上半平面乘积域都非零，
所以符号实稳定。有限次数定理确实覆盖这个逆算子的例外保根性；
不能只因某个二次测试没有失败，就声称已经得到完整保根结论。

对其他分母和分子，具体判别式与三角恒等式需另行证明。
是否存在某个实际共振多项式的非实根，也不是算子的单独失败所能回答：
递推右端只落在一个受限的非线性像中，未必能够产生算子反例的输入。

## 3. 与原科学问题的分离

实际首项 $C_{r,s}(\lambda)$ 来自包含 $e^v$ 和 $e^{2v}$ 的非线性消元。
对角传播子的输入变量是形式级数变量 $t$，而待分类首项的根变量是 $\lambda$。
两者不只是同一线性问题的不同记号。无论一个单独传播子保根或不保根，
都不能跳过这个对象差异，直接推出 $C_{r,s}$ 的全实性或反例。

本轮定点检索没有找到已直接陈述本题全部 $r,s$ 的传播子分类或
非线性首项全实根定理的材料；这只是本次来源匹配结果，
不等于证明全球不存在先例。全局新意仍未完成核对。
既有 Lindstedt 树、Hill 双谐波谱隙和 Suris 背景继续按
[原定点检查](PAPER30_TWIST_ROOT_STRUCTURE_PRIOR_20260907.md)扣除，未重新展开。

## 4. 实际检索边界

本轮查询为：

1. `site.arxiv.org finite multiplier sequences sin k theta real rooted polynomials`
2. `site.arxiv.org Borcea Branden Polya Schur finite degree diagonal operators real zeros`
3. `"sin" "multiplier sequence" polynomials`

Zotero/Obsidian 工具未配置；指定 arXiv 技能目录未找到抓取脚本，
故采用官方 arXiv 网页回退，没有下载论文PDF。
本地相关文件名筛选仅命中无关的素数乘子项目，未读取其PDF内容。
未把搜索摘要或二手介绍代替上表的一手定理陈述。
未作正式候选投票、正文估页、Route评价或外部写入。
