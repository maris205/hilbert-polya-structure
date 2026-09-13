# Paper30：新一轮预筛与 Artin–Schreier 归约处置

日期：2026-09-07。状态：`AUXILIARY_PROOFS_ACCEPTED_FULL_MIXED_OPEN`。
主控已全文读取本轮实际作者输入与新独立报告。
这是有界证明预筛的处置，不是正式候选评分或完整分类论文。
Batch07 仍本地接受 $3/5$；Paper30 未立项，Paper31 未开展。
`route_applicability: NOT_APPLICABLE`。

## 1. 本轮两个不同问题的实际结果

[九问题作者预筛](PAPER30_NEW_SYMPLECTIC_PROBLEM_SCREEN_20260907.md)
比较了真正不同的族内问题，主控已全文读取。跨系统族的 Floer 想法仍为
`ROUND2_CLUE`，不因预筛自行获得执行权限或并入当前论文。

其中共振 kicked-chain 问题已经完成真实有限链的一致小耦合定理和独立核查，
但作者自然正文中心 $17.25$ 页，当前包未进入正式候选阶段。
数学及完整处置见[耦合链阶段结果](PAPER30_RESONANT_LATTICE_SCREEN_DISPOSITION_20260907.md)。
本文件不重复或重审那条已关闭支线，也不把它并入以下 AS 问题计篇幅。

## 2. 先前非加性 AS 作者预筛的保留状态

[非加性 AS 作者记录](PAPER30_ARTIN_SCHREIER_NONADDITIVE_PROBE_20260907.md)
完整保留，主控已读完 $509$ 行。它反驳了原先过宽的“非 $p$ 幂次数即无
非平凡 AS 特征类”猜测；不能重新使用该猜测作为下一步证明前提。
其反例包含素于特征次数的真实例子，故补一句 $p\nmid d$ 也不足以修复宽泛禁阻。

该稿还在明确稀疏模板 $a xy+A(x)+B(y)$ 内给出特征类分类，区分
指定 deck 生成元的固定类与允许非平凡 deck 作用的底层覆盖提升。
它不能用于任意 mixed 多项式的最高项排除。
本轮新独立审查没有重审该整份模板记录，故不为其全部命题补造独立通过状态。
其中二次、特征 $3$ 的已有非零类，在本轮新桥接中被重新直接验证。

## 3. 新的全部 mixed 桥接已独立通过

固定代数闭域 $K$、奇特征 $p$、
$F=(x^2+c-y,x)$、$\sigma=F^*$ 与 $\lambda\in\mathbb F_p^*$。
令 $A=K[x,y]$、$Q=A/\wp(A)$、$\wp(h)=h^p-h$，这里分母是加法像而非理想，
并令
$$
\overline C_\lambda=A/((\sigma-\lambda)A+K),
\qquad \phi\langle h\rangle=\langle h^p\rangle.
$$
[新作者证明](PAPER30_AS_FROBENIUS_COINVARIANT_PROBE_20260907.md)
及[窄独立核查](PAPER30_AS_FROBENIUS_COINVARIANT_INDEPENDENT_CHECK_20260907.md)
建立了以下实际结论，主控均已全文读取：

1. 全部多项式上的自然 $\mathbb F_p$-线性同构
   $$
   Q^{\sigma=\lambda}\cong
   \ker(\phi-1:\overline C_\lambda\to\overline C_\lambda).
   $$
   轨道基的实际重写证明在特征 $p$ 下重新核对；常数、$\lambda=1$、
   代表选择与半线性均已处理，不是套用特征零定理。
2. 在每个非空轨道取最小普通次数代表，设最高轨道次数为 $D$。
   若某个最高代表的二进制指数对满足 $2a\ge b,2b\ge a$，则
   $\delta(\phi v)=pD>D$。不同来源经移位进入同一目标轨道的风险已被严格排除。
3. 因此非零固定元的最高层只能是一条奇反射例外轨道：
   $(a,b)=(n,2n+1)$ 或其交换，且 $D=3n+1$。
   每个这样的次数至多一条例外，但次数无限多；没有得出有限维异常空间。
4. 在 $p=3,c=0,\lambda=-1$ 时，反特征多项式一形式恰为
   $K\,d(xy)$，并有完整核分类
   $$
   \ker\phi=K\langle x\rangle.
   $$
   这是一条 $K$-线，不是多项式环 $K[x]$，更不是 $\ker(\phi-1)$ 的分类。

新报告的裁决为 `PROVABLE AS STATED / PROVED`，没有发现需修正的科学公式、
假设或量词。$p=3,5$ 的 single-letter 公式亦逐项通过。
核与固定空间的区别在作者稿、独立报告和本处置中均保留。

## 4. 原主问题仍未闭合

现在欠缺的是：对全部奇反射例外 word，计算 Frobenius 约化后的加权轨道和，
控制同一来源的平移项与不同低层来源之间的抵消；或给出一个完整的替代分类。
最高支撑必要条件没有解决这项无限族义务。

具体仍为 `OPEN / NOT CURRENTLY JUSTIFIED`：

- $p\ge5$ 的全部 mixed AS 特征类。
- $p=3,c=0$ 的全部 mixed 固定空间；即使已知道 $\ker\phi$，也不能推出固定空间为零。
- $p=3,c\ne0,\lambda=-1$ 的已知非零类是否穷尽全部 mixed 类。

本轮不为这些辅助结果建立正式候选包、不评分、不试写、不编译测页。
没有全局次数上界、有限异常块、全类消失或主问题已完成的声明。
后续若继续此方向，应直接处理上述真实消去义务，不重做未变且已通过的桥接。

## 5. 查新层级与标准工具扣除

一般 Artin–Schreier 正合列及 Frobenius 半线性固定空间语言是标准背景，
不作为新原理。主控核对了
[Stacks Project §59.63](https://stacks.math.columbia.edu/tag/0A3J)
的正合列及其有限维半线性结论；本题的 $\overline C_\lambda$ 是无限维，
不能把该有限维结论直接套来授予有限性。
Bousch 的轨道基思想、线性移位 obstruction 和通常的正合列方法也须扣除。

主控另外作了六条有界公开关键词查询：
`"Hénon" "positive characteristic" "foliation"`；
`"Hénon" "Artin" "Schreier"`；
`"polynomial automorphisms" "characteristic" "differential forms"`；
`"automorphisms" "foliations" "positive characteristic" "plane"`；
`"Henon" "invariant" "foliation" characteristic`；
`site:arxiv.org "Hénon" "étale"`。
结果主要是无关的复动力学叶状结构或一般资料，未定位直接覆盖新小引理的
一手分类定理。这个有限未命中不是世界新颖性认证；没有据此授予新意门通过。
没有使用非一手搜索摘要来支持当前数学结论。

## 6. 绑定输入与本地状态

| 文件 | 行数 | SHA256 |
| --- | ---: | --- |
| 九问题作者预筛 | 378 | `e303dd3014c1abab4d1616e04376c16544311bf46252e1da142ee35c5f57f033` |
| 旧非加性 AS 作者记录 | 509 | `fb872f9fc0be2082822ab437cbbb8dba74158d9ecb2c7bc657cf5e6a857ed29d` |
| 新 Frobenius 作者证明 | 336 | `05aba58b468f3c4a5a9201f032200adb96e5acc6216ca65920066d2b2b3fe4d6` |
| 新窄独立核查 | 260 | `5fc8746299f3c3868ecffa5bdacb6d105fec7adad86ffcd40124f0544804ef15` |

所有作者输入保持不变；本轮只增加独立记录与处置。已接受 Papers27–29
和所有旧失败／停止记录保留。没有改动正文下限、试写权限、论文计数或本地交付边界。
