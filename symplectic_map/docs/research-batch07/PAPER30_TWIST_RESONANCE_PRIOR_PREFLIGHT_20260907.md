# Paper30 双谐波 twist map：共振系数先例定向预核

日期：2026-09-07。范围：旧九题筛选
[问题 2 与 §3.2](PAPER30_NEW_SYMPLECTIC_PROBLEM_SCREEN_20260907.md)。
这是八条查询上限内的一手文献预核，不是作者证明、正式候选评分、Route 评价、
篇幅估计或立项决定。只新增本报告，不改旧记录和批次状态。
使用 research-lit 技能；其一手阅读与证据分层要求决定了下面的版本限定和背景扣除。

## 1. 结论先行

总体结论：`uncertain`，不能授予新意 PASS。

- `matched`：一般 Fourier–Lindstedt 递推、树值表达、最小共振簇的支撑算术、
  零动量共振树的重求和消去，以及用最小树值求和定义首个共振极限系数，
  Berretti–Gentile 的公开一手全文已经明确给出。不能把这些方法或一般组合公式
  当作本题新增贡献。
- `no-matched`，**仅限本次实际阅读的一手文本**：没有看到针对
  \(V_{\epsilon,\lambda}=\epsilon\cos q+\lambda\epsilon^2\cos2q\)、
  固定每个互素 \(0<r<s\)、\(s\ge3\)，将约化作用量的
  \(\epsilon^s\cos(s\theta)\) 系数 \(C_{r,s}(\lambda)\) 的全部实根、重数、
  简单根后首个真实分裂阶做出明确分类的定理。
- `uncertain`：上述“没有看到”不是世界范围无先例证明；也不说明从旧递推到
  本题分类的距离必然足以构成新研究。已经取得作者公开全文，故旧记录的
  “Berretti–Gentile 全文未读”这一具体缺口得到实质推进；但尚未取得并逐项
  核对期刊定稿，且公开前后版本存在实际文字差异，不能把所有版本视为同一文本。

作者方向若继续，真正需要新增证据的是**全分母结构分类与消失后的真实动力结论**，
不是重新推导通用上同调递推、列出有限多个低分母多项式或重述双谐波竞争。

## 2. 精确对象与对照方式

本题映射为

\[
p'=p+\epsilon\sin q+2\lambda\epsilon^2\sin2q,\qquad q'=q+p'.
\]

旧筛选固定 \(r/s\)，以零均值周期修正消去非恒定配置变量，留下相位约化势；
当前待核对的对象是该约化势在 \(\epsilon\) 上的加权首项，
而不是不变曲线共轭函数的收敛半径。

为对应旧文符号，本题可以写成 \(T_{\epsilon,f}\)，但此时
\(f=f_{\epsilon,\lambda}=\sin x+2\lambda\epsilon\sin2x\) **本身随 \(\epsilon\) 变化**。
以下比较是阅读后的对象辨析，不是对本题系数的作者证明。

## 3. 实际取得的文献与阅读范围

| 一手文献与状态 | 本次实际阅读 | 对精确问题的判定 |
| --- | --- | --- |
| A. Berretti, G. Gentile, *Scaling properties for the radius of convergence of Lindstedt series: generalized standard maps*, J. Math. Pures Appl. 79 (2000), no. 7, 691–713；DOI 10.1016/S0021-7824(00)00167-7。书目由 [Roma Tre 机构记录](https://iris.uniroma3.it/handle/11590/143062)核对。 | [mp_arc 99-377 作者提交记录](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=99-377)及其[公开 PostScript](https://web.ma.utexas.edu/mp_arc/c/99/99-377.ps.gz)：§1–3、§4 消去引理、§6–7；另读 INFN 的 [FM2000-6 公开全文](https://ipparco.roma1.infn.it/pagine/deposito/2000/bergen.ps.gz)对应关键段落和[作者 TeX 源](https://ipparco.roma1.infn.it/pagine/deposito/2000/bergen.tex.gz)中的定理、系数定义与消去恒等式。 | 通用递推及最小树系数 `matched`；本题全实根分类在所读文本中 `no-matched`；期刊定稿级排除 `uncertain`。 |
| A. Berretti, G. Gentile, *Non-universal behaviour of scaling properties for generalized semistandard and standard maps*, Nonlinearity 14 (2001), no. 5, 1029–1039；DOI 10.1088/0951-7715/14/5/307。书目由 [Roma Tre 机构记录](https://iris.uniroma3.it/handle/11590/139305)核对。 | 准确后续论文定向命中；实际读 [INFN FM2000-14 作者全文](https://ipparco.roma1.infn.it/pagine/deposito/2000/bg4.ps.gz)的 §1–5，尤其 §2 主定理、§4 同号树值下界及 §5 与标准映射比较。 | 正 Fourier 系数下无抵消估计 `matched`；signed 参数全根分类 `no-matched`。这是直接后续核查，不扩成新文献路线。 |
| M. Mugnaine 等，*Isochronous islands in the two-harmonic standard map*，2025，arXiv:2504.20177。 | [官方记录](https://arxiv.org/abs/2504.20177)及[作者 HTML](https://arxiv.org/html/2504.20177v1)的 §2 模型、§3、§4；没有下载 arXiv PDF。 | 双谐波模型、固定点/island transitions `matched`；全部轨道分母的首项根结构 `no-matched`。 |
| M. Mugnaine 等，*Isochronous bifurcations dependence on the driving mode phase shift in two-harmonic standard maps*，arXiv:2505.00179（2025 提交；旧记录对应期刊题名为 *Dependence of isochronous bifurcations on the driving-mode phase shift in two-harmonic standard maps*, Phys. Rev. E 112 (2025), 034216）。 | [官方记录](https://arxiv.org/abs/2505.00179)及[作者 HTML](https://arxiv.org/html/2505.00179v1)的 §II 模型、§III–IV、附录固定点方程和谱判据。期刊题名沿用旧记录，不声称本次重新阅读全文期刊版。 | 相位、固定点竞争、有限 mode-pair 分岔结构 `matched`；固定任意 \(r/s\) 的 \(\epsilon^s\) 系数分类 `no-matched`。 |

这里使用作者公开预印本作为一手内容证据；准确期刊书目不意味着手头文件就是
出版社定稿。旧 Wenzel–Biham–Jayaprakash 的单正弦分母阶先例继续按旧记录扣除，
本次未重开其全文检索，不冒称重新核验。

## 4. Berretti–Gentile：哪些结论真正已经给出

以下式号按 INFN `bergen` 公开版本；mp_arc 早版的引言编号不同。

### 4.1 主定理的对象、参数和假设

§1 式 (1.1)、(1.8)–(1.10)研究实、解析、零均值的固定周期函数 \(f\)，以及
非平凡同伦不变曲线的共轭方程
\(D_\omega u=\epsilon f(\alpha+u)\)。Theorem 2 使用
\(\omega\to p/q\) 的复平面非切向锥，按
\(\epsilon\mapsto\epsilon(\omega-p/q)^{2/r^*(f)}\) 缩放，得到解析的极限共轭函数。
\(r^*\) 来自式 (1.17)–(1.18) 的支撑算术和最小普通节点数。
[作者全文，§1](https://ipparco.roma1.infn.it/pagine/deposito/2000/bergen.ps.gz)

这不等于在 \(\omega=r/s\) 上直接给出全部相位的周期轨道。尤其不能把
该主定理中的复参数非切向极限替换成本题固定实有理数下的有限维约化。
本题两个谐波分别具有权重 1、2；旧 \(r^*\) 的节点计数将每次使用 \(f\)
都计作同一阶，所以不能仅将旧 \(r^*\) 或旧首个普通阶系数重命名为本题的
\(s\) 或 \(C_{r,s}(\lambda)\)。

### 4.2 通用递推和最小树系数：明确覆盖

§2 式 (2.1)给出一般 Fourier–Taylor 系数的递推，式 (2.2)给出
\([2(\cos(2\pi\omega\nu)-1)]^{-1}\) 传播子；式 (2.3)–(2.4)是标记树值表示。
§6 Lemma 7 筛出缩放极限中保留的树；Lemma 10 与式 (6.9)将极限方程的
系数 \(\mathcal C_{p/q}^{\nu}(f)\) 写为最小节点树的有限求和。
[作者全文，§2、§6](https://ipparco.roma1.infn.it/pagine/deposito/2000/bergen.ps.gz)

因此，“任意支撑可以递推”“共振首项来自有限树和”“支撑有最小共振组合”
均已覆盖。把一般递推代入两个非零 Fourier mode，再按其参数幂重排，
至少属于非常直接的既有算法特化；不能仅凭新记号或新路径宣称新方法。

但式 (6.9)只取固定 \(f\) 的最小普通节点阶。本题加权 \(\epsilon^s\)
会汇合不同普通节点数的贡献，且还要将共轭/方程系数与约化作用量的相位导数
正确对应。旧系数有不同根线传播子及归一化约定，不能不证明对应便直接令二者相等。
在这些已读段落中，没有本题 \(\lambda\) 多项式全实根或重数定理。

### 4.3 “resonance cancellation”不等于调谐参数令共振首项为零

§2 定义的 resonant cluster 满足节点 Fourier 标签之和为零。
§3 Proposition 2 用根线重接使零 Fourier 模式的可解性条件逐阶消去；
§4 Lemma 5 和 §5 对重接树族进一步消去外来动量展开的零阶与一阶项，
获得小除数所需的二阶增益。§6 则说明带此类共振簇的项在所取缩放极限中消失。
[作者全文，§2–6](https://ipparco.roma1.infn.it/pagine/deposito/2000/bergen.ps.gz)

本题所问的是总相位频率为 \(\pm s\) 的**非零**谐波，在不同参数贡献之间相消。
因此零动量树消去确实是已有强背景，却不是 \(C_{r,s}(\lambda)\) 的实零点分类。

### 4.4 2001 直接续篇也不是全部参数的非消失定理

续篇的半标准映射只有正 Fourier 标签，故没有上述零总标签的共振簇；
§4 式 (4.5)进一步选定 \(f_\nu>F>0\) 的有限 Fourier 支撑。
同一普通阶的树值于是具有共同复相位，能够用无抵消下界证明收敛半径上界。
§5 用指定正系数子类比较广义标准映射，并控制相应函数类上的下确界。
[2001 论文作者全文，§3–5](https://ipparco.roma1.infn.it/pagine/deposito/2000/bg4.ps.gz)

这类选定同号子族上的估计不能直接推出任意实 \(\lambda\) 的无根、全根实性、
简单性或重根排除；它也不自动给出本题不同加权阶汇合后的符号结构。
若作者未来获得某个无需抵消的参数半轴结论，应先扣除这一明确旧机制。

## 5. Mugnaine 两项的定向排除

2504.20177 的式 (1)已经使用任意两个整数 mode 和独立幅值；§3 明确改变
\(K_2\)追踪固定点分岔，结论讨论 saddle-node、pitchfork 和 intermediate modes。
2505.00179 的 §III 明确计算 \(y=0\) 上的 period-one elliptic points；
其表 1 的“全部”是 \(1\le m_1<m_2\le6\) 的 mode 对和指定相位/幅值范围，
附录也从 period-one 方程与二阶特征方程出发。
[前文 §2–4](https://arxiv.org/html/2504.20177v1)，
[后文 §III、附录](https://arxiv.org/html/2505.00179v1)

这里 forcing mode 整数与周期轨道旋转数的分母不是同一个量。
这些文本足以扣除模型新意和一般 islands 竞争机制，但不能把其有限 mode-pair
图表直接解释成 \(C_{r,s}(\lambda)\) 对所有 \(s\) 的根分类。
本次没有把两篇再广泛重搜，也未将数值 bifurcation plot 当严格全根证明。

## 6. 版本、访问与剩余义务

1. **确已读到作者全文。** mp_arc 原页面含 HTML BASE；浏览器抽取器对某些
   相对链接错误拼到 `mp_arc-bin` 而返回 404。读取原 HTML 后按其声明的 BASE
   访问公开 `mp_arc/c/99/99-377.ps.gz`成功。这是正常链接解析，不是访问绕过。
   INFN 的公开 PS 与 TeX 也成功读取。仅在工作区外临时目录转换为 PDF/文本，
   工作区内没有新增文献 PDF 或其他资产。
2. **定稿级限定仍保留。** Roma Tre 页面/作者 PDF入口在本次工具访问中遇到
   超时或证书验证失败，未关闭证书验证。出版社 DOI全文未成功打开。
   mp_arc 与 INFN 公开版的引言、定理编号、结论文字有差异；INFN版 Remark 3
   对一般有限收敛半径明确保留条件，而 2001 续篇还自述补足前文相关上界问题。
   本报告只借用所读定义/递推/树结构，不借这些版本中的强缩放语句推出任意参数非消失。
3. **未取得的新意结论。** 精确 \(C_{r,s}\) 与已有 \(\mathcal C\) 的身份关系、
   全分母根结构的可证明性，以及它是否只是通用递推的短特化，均不由本报告证明。
   本次没有命中明确分类，不能反向转成原创性认证。
4. **内容所留真正差距。** 完整实根集合及重数；若存在简单根，其消失后的下一
   非恒定约化项和真实周期几何。这里列的是输入问题未被所读文献直接解决的部分，
   不是作者已经建立的结果，也不承诺正文容量。

## 7. 查询账单：恰八条

1. `"Scaling properties for the radius of convergence of Lindstedt series" generalized standard maps Berretti Gentile`
2. `site.arxiv.org Berretti Gentile "generalized standard maps"`
3. `site.mat.uniroma3.it/users/gentile "generalized standard maps" "bg3"`
4. `"Scaling properties" "generalized standard maps" pdf`
5. `"Scaling properties" "generalized standard maps" "sin" Gentile`
6. `"Berretti" "Gentile" "generalized semistandard" mp_arc`
7. `"standard map" "resonance" "two harmonics" coefficient polynomial`
8. `"standard map" "Lindstedt" "cancellation" "harmonics"`

其余操作仅打开既有准确一手链接、命中机构页及其公开文件。最后两条没有新增
精确全根分类证据；未采用百科、AI摘要、二手书目或搜索空结果支持科学排除。
arXiv只访问 metadata/HTML，未下载PDF；未付费、发信、上传或请求受限内容。
