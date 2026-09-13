# Paper30 qPI：高层首 jet 与 N9 有限局部结构的数学处置

日期：2026-09-09。主控 `/root`。类型：有界数学合取接受。
`route_applicability: NOT_APPLICABLE`。不是正式候選评分、论文准入或 PDF 验收。
Batch07 仍为 3/5；Paper30 未立项、Paper31 未开展。

## 1. 接受及责任合取

主控已全文读取两份高层作者证明（数字分解230行、完整首 jet185行）及其222行非作者报告，
并将报告保留的首矩阵／首层理想依赖与
[已接受的全素数首层证明](PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_MATHEMATICS_DISPOSITION_V1_20260909.md)
按实际相同哈希合取。报告对 FJ.1 新责任为 PASS，对 FJ.2 推论保留的上游条件至此关闭。
没有改写原报告的历史交付状态，也没有由参加过纯配对作者工作的检查者代签首层全链。

另全文读取 $N=9$ 作者诊断214行、冻结脚本171行，以及新的324行非作者报告。
报告独立核准全部有限 H2.1–H2.3，实际运行冻结脚本并另作两种精确独立计算。
主控核对目标身份、精度／整除责任和低阶理想论证，接受该准确有限结论。
此前已运行且输入未变的脚本不因本次处置再跑；运行证据不替代理论检查。

两位检查者均已接触本方向，身份见各自报告；不是盲审、新意票或人类认证。
本处置不把这两项不同范围拼接成完整高层理想。

## 2. 全奇素数、全高度、m=1 的模平方结论

取任意奇素数 $p$、$a\ge2$、$N=p^a$、$\sigma=1+p+\cdots+p^{a-1}$，
参数 $\pi_a=\zeta_{p^a}-1$。任意单位时间的二阶 jet 在首层圆分环和第 $a$ 层圆分环之间，
通过指定同构 $\pi_1\mapsto\pi_a\bmod\pi_a^2$ 比较。
这是两个特征 $p$ 二阶商的同构，不是自然根嵌入；实际八截面模型逐中心相同。

在这个共同的完整开放模型上接受
$$\alpha_N^{[2]}=H^{\langle\sigma-1\rangle}\alpha_p^{[2]}.$$
乘数由局部 Hasse 提升的 $\sigma-1$ 次幂粘合，因 $p\mid\sigma-1$ 而与提升无关。
全部两个状态方向、任意单位时间二阶变化和四条完整末端线均保留。
延拓在非约化底环上使用实际图的 $u$ 非零因子，不靠集合稠密性。

由首层完整理想的同哈希接受，对每个光滑有限原能级附近，准确得到
$$\mathfrak c(\alpha_N)+(\pi_a^2)
=(\pi_a^2,\widetilde H^\sigma,\pi_a\widetilde H^{\sigma-1}).$$
Hasse 根 $h$ 重数为 $e_h$ 时，完成后是
$$ (\pi_a^2,z^{e_h\sigma},\pi_a z^{e_h(\sigma-1)}),\qquad\bar z=J-h.$$
沿光滑超奇异层的无分歧状态提升，原 $\alpha_N$ 公共系数阶至少二；普通层准确零。
乘回 $p^a$，得到下界 $a\varphi(p^a)+2$ 及普通层准确阶 $a\varphi(p^a)$。
**“至少二”不是“准确二”；上式是加上 $(\pi_a^2)$ 后的理想，不能删除左边的这一项。**

## 3. N9、两时间、第一末端原点的有限准确结论

只固定 $p=3,a=2,m=1$、$q=1+\pi=\zeta_9$、$t=1+\delta\pi$、$\delta\in\{0,1\}$，
以及原第一末端图 $x=u^{-1},y=1+uv$ 的点 $(u,v)=(0,0)$。
在 $R=\widehat{\mathbb Z[\zeta_9]_{(\pi)}}[[u,v]]$ 中，$\mathfrak m=(\pi,u,v)$，
写 $\alpha_9=A_u\,du+A_v\,dv$，并保持实际 $J_t=1+uv-v/(1+uv)-tu$。
接受以下准确范围：

- 两时间的四个点系数 $A_u,A_v$，以及两个点切向楔积系数的全部整系数多项式。
  系数准确 $\pi$ 赋值为二，切向点值准确赋值为四；不是只核数值浮点。
- 完整双状态四阶 jet，特别是
  $$\operatorname{in}_2\alpha_9=\pi^2(du+dv),$$
  $$T_4=(1+\delta)\pi^4+2\pi^3u+\pi^3v+2\pi(u+v)^3,$$
  其中 $T=A_u(J_t)_v-A_v(J_t)_u$；其零至三阶消失。
- 实际单位行列式变换给 $I=(A_u,A_v)=(F,G)$，
  $$F=A_u,\qquad G=T-\bigl((1+\delta)\pi^2+2\pi u+\pi v\bigr)A_u,$$
  首式分别为 $\pi^2$ 和 $2\pi(u+v)^3$。准确的低阶初始理想结论仅为
  $$\bigl(\operatorname{in}_{\mathfrak m}I\bigr)_d
  =(\pi^2,\pi(u+v)^3)_d\quad(0\le d\le4).$$

这里 $v_\pi(3)=6$。有限模三计算的精度，以及微分前多保留一阶、状态微分保持理想 $(3)$，
均在独立报告中另证。关联分次环是 $\mathbb F_3[\pi,u,v]$，不是全局令 $\pi^6=0$。
点上评价理想为 $(\pi^2)$ 不等于整个 $R$ 中的理想；两分量均有不被 $\pi^2$ 整除的纯状态四次项。
高阶 syzygy、完整初始理想、完整形式正规形和全时间／全状态的准确二阶均未授予。

## 4. 新方向的状态，不由本次 PASS 代签

[全 tame 首层作者件](PAPER30_QPI_VERTICAL_ALPHA_ALL_TAME_HEIGHT1_PROOF_V1_20260909.md)
新证明全部素数、$p\nmid m$ 下原函数提升障碍的实际非零性，并与整数迹同余及 Čech 比较连接。
该件连同新的 prime trace 作者引理已派非作者全文检查。
[抽象 OC 检查](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_INDEPENDENT_CHECK_V1_20260909.md)
已由主控全文读，接受严格 A1–A4 条件下的抽象引理；实际 qPI 的 A3/A4 尚待该新检查，未预授。
该新路线不需要未证明的一般 $m$ 配对常数 $m^2$。

一般 tame-block 全奇素数高度的首 jet 作者件另在独立检查中；其报告未由本次 $m=1$ 通过推定。
新 Čech／算术提升障碍来源增量也在有界检索；标准机制应明确扣除。
所有正式旧失败票、锁定正文22–30页和完整验收条件均保持，不创建候选、稿件或 PDF。

## 5. 实际身份

所有路径相对本目录。仅核对本次必要目标与接受依赖，不重扫旧构建树。

| 目标／依赖 | SHA-256 |
|---|---|
| [数字分解作者](PAPER30_QPI_VERTICAL_ALPHA_FIRST_JET_ITERATION_V1_20260909.md) | `b304378b32bbd481a86b2416528797378d04a3f0050bdd6b52d5aa251ad064f4` |
| [完整首 jet 作者](PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_FACTORISATION_V1_20260909.md) | `9d53bee5abf8026dfa09d2bcb38713e0ace28ff082d9e87b3efa595ab5955a86` |
| [两项新责任独查](PAPER30_QPI_VERTICAL_ALPHA_GLOBAL_FIRST_JET_INDEPENDENT_CHECK_V1_20260909.md) | `3465766d223fdbf244a0a361fa539a828d1e19e398697b9038d14c913d3bc3c9` |
| [上游首层接受](PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_MATHEMATICS_DISPOSITION_V1_20260909.md) | `8a9395f73647cb309921702abd52088b788be8c565686c453a419cd5bb57b5d8` |
| [N9 作者](PAPER30_QPI_VERTICAL_ALPHA_P3_HEIGHT2_PROBE_V1_20260909.md) | `ef8e53646e2b5b702d5ae3e130a5fd14e8bcfd73d0e0a61db861a82730706a97` |
| [N9 脚本](PAPER30_QPI_VERTICAL_ALPHA_P3_HEIGHT2_PROBE_V1_20260909.py) | `26096c03b278415573564d6ff3aed945f4691c07d9b9df8a3c9b0b97e5597693` |
| [N9 独查](PAPER30_QPI_VERTICAL_ALPHA_P3_HEIGHT2_INDEPENDENT_CHECK_V1_20260909.md) | `703376cb6b72bf37de58fcb608695556c58aca2c89db08b329d070de01ed350e` |
| [抽象 OC 独查](PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_INDEPENDENT_CHECK_V1_20260909.md) | `cb5ec4eda57c74584a03c1aca4d78fa43ee898b8b6d73619f417d0d2bdd3083e` |

本次只有本地数学记录与接续更新，无新增实验、GPU、投稿、上传或其他外部效力。
