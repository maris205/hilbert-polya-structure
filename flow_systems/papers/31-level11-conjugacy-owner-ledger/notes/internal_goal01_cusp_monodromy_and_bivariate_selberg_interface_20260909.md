# P31 Goal 01：cusp monodromy 與雙變量 Selberg 接口

日期：2026-09-09。保存緊接前一紙面輪次已閉合的有界結果。
本次唯一寫入目標為本文件；不修改既有筆記、原稿、鎖、receipts、Route 或 Stage。
沒有科學程式、實驗、producer、closed-orbit census 或 frozen-input replay。
方法採 ARS 的 claim/proof/counterclaim 組織；不是 full pipeline 或正式審稿。

**結論與界線。** 實際 cuspform 時鐘在所有 parabolic 上的週期為零。
誘導表示的每個 parabolic 矩陣可經依賴參數的整可逆 gauge 化為固定酉矩陣。
Fedosova–Pohl 的來源可給每個固定表示切片的 Selberg zeta 亞純延拓。
雙變量乘積的共同右域及實際 clock 的 ratio 在本文直接證明；
**聯合參數的亞純延拓及對角線延拓仍未證明**，不能由逐切片定理直接宣布。

## 1. 固定同一流、時鐘、指標與方向

沿用 [P26 Frozen dynamical system][clock]、[天然 holonomy 筆記][holonomy]
與 [Euler 絕對收斂筆記][euler]，令
\[
G=\mathrm{PSL}_2(\mathbb Z),\quad
\Gamma=\Gamma_0(11)/\{\pm I\},\quad [G:\Gamma]=12,
\]
\[
f(z)=\eta(z)^2\eta(11z)^2,\quad
\omega=2\pi i f(z)\,dz,\quad
\alpha=\operatorname{Re}\omega,\quad
\rho_\varepsilon(v)=1+\varepsilon\alpha(v),\quad
X_\varepsilon=X_{\rm geo}/\rho_\varepsilon.
\tag{1}
\]
\(\varepsilon\in\mathbb R\) 固定，且 \(0<c_0\le1\) 滿足
\(\rho_\varepsilon\ge c_0\)。在既有正密度區間，可取
\(c_0=1-|\varepsilon|\|\alpha(v)\|_\infty>0\)。
\(\rho\) 是 slowness；\(\ell\) 是曲率負一、單位速 geodesic 的幾何長度。

固定 \(Y_0(11)\) 上的 rank-\(m\) 酉平坦局部系，即
\(\nu:\Gamma\to U(m)\)，保持既有正向 monodromy convention。閉形式給實同態
\[
I(\gamma)=\int_\gamma\alpha,\qquad
T_\varepsilon(P)=\ell(P)+\varepsilon I(P)\ge c_0\ell(P).
\tag{2}
\]
對獨立複參數 \(w\) 定義
\[
\chi_w(\gamma)=\nu(\gamma)e^{-w\varepsilon I(\gamma)},\qquad
\eta_w=\operatorname{Ind}_\Gamma^G\chi_w,\quad \dim\eta_w=12m.
\tag{3}
\]
\(\nu,\varepsilon,\alpha\) 不隨 \(w\) 選權；\(\eta_w\) 一般非酉。
這是原閉形式 connection 的參數族，不是新的流或重新擬合的 clock。

\(\mathcal P_G,\mathcal P_\Gamma\) 均指 primitive 有向 hyperbolic 共軛類，
只作各群實際的共軛商，不額外識別取逆。若逆元本已共軛，只算原來的一個類。
identity、elliptic、parabolic 均不進入下述閉軌乘積。

## 2. Cusp 局部座標證明：所有 parabolic 的 I 都為零

**引理 1。** 對每個 \(\Gamma\) 的 parabolic 元素 \(p\)，\(I(p)=0\)。

**證明。** 選任一 cusp 的 scaling 座標，令 cusp width 為 \(h>0\)，
\(q=e^{2\pi iz/h}\)。權二 cusp 條件給
\[
f_{\rm cusp}(z)=\sum_{n\ge1}a_nq^n,\qquad
\omega=2\pi i f_{\rm cusp}(z)\,dz
      =h\sum_{n\ge1}a_nq^{n-1}\,dq.
\tag{4}
\]
最後一式在 \(q=0\) 全純，故小圓積分為零，取實部得到 cusp loop 的
\(\alpha\)-週期為零。任一 parabolic 對應某 cusp 的周邊生成元之非零整數冪，
到 based-loop 共軛；\(I\) 對冪相加、對共軛不變，故均為零。□

這個論證使用「cuspform」，不只使用一般 weight-two modular form 的閉性；
若存在 cusp 留數，結論不能照搬。由此
\[
\chi_w(p)=\nu(p)\qquad(p\in\Gamma\text{ parabolic},\ w\in\mathbb C).
\tag{5}
\]

## 3. 誘導 parabolic 的整可逆 gauge

以下用明示的右陪集 row-block 模型固定非交換乘法次序。
取代表 \(\Gamma a_i\)，令
\[
a_i g=\gamma_i(g)a_{\sigma_g(i)},\qquad \gamma_i(g)\in\Gamma,\qquad
(\eta_w(g))_{ij}=
\begin{cases}\chi_w(\gamma_i(g)),&j=\sigma_g(i),\\0,&\text{其餘}.
\end{cases}
\tag{6}
\]
因 \(\gamma_i(gh)=\gamma_i(g)\gamma_{\sigma_g(i)}(h)\)，這確為表示。
它也可寫成 \((\widetilde\chi_w(a_i g a_j^{-1}))_{ij}\)，其中群外值為零。
此處 row \(i\)、column \(\sigma_g(i)\) 的約定不可與 source-column 箭頭混抄；
cycle 的 ordered product 與下面的正向共軛類因子保持一致。

固定 ambient parabolic \(p\in G\)。對其一條長度 \(d\) 的 cycle \(O\)，
置 \(b_i=I(\gamma_i(p))\)。逐步消去相鄰代表得到
\[
\gamma_i(p)\gamma_{\sigma_p(i)}(p)\cdots
\gamma_{\sigma_p^{d-1}(i)}(p)
=a_i p^d a_i^{-1}=:P_O\in\Gamma.
\tag{7}
\]
\(P_O\) 是 parabolic，故 \(\sum_{i\in O}b_i=I(P_O)=0\)。
在每條 cycle 選一個起點令 \(t_i=0\)，遞推
\[
t_i-t_{\sigma_p(i)}=b_i,\qquad
D_p(w)=\operatorname{diag}_{i=1}^{12}
                 (e^{-w\varepsilon t_i}I_m).
\tag{8}
\]
cycle 總和為零恰保證遞推閉合。\(D_p\) 及其逆對所有 \(w\) 都整。
逐個非零 row block 檢查即得
\[
\boxed{\eta_w(p)=D_p(w)\eta_0(p)D_p(w)^{-1}.}
\tag{9}
\]
\(\eta_0(p)\) 在標準直和 Hermitian norm 下是 block-unitary 矩陣。
因此 \(\eta_w(p)\) 半單，全部 eigenvalues 模長為 \(1\)，且
\[
\det(\lambda I_{12m}-\eta_w(p))
=\prod_O\det(\lambda^{d_O}I_m-\nu(P_O)),
\tag{10}
\]
\[
\sup_{w\in K,\ n\in\mathbb Z}\|\eta_w(p)^n\|
\le\sup_{w\in K}\|D_p(w)\|\,\|D_p(w)^{-1}\|<\infty
\quad(K\subset\mathbb C\text{ 緊}).
\tag{11}
\]
這證明 non-expanding cusp monodromy，並有 compact-\(w\) 一致冪界。
沒有聲稱原固定框架中的 \(\eta_w(p)\) 必酉，也沒有聲稱一個共同 gauge
同時消掉所有 \(g\in G\) 的 twist。式 (11) 固定 \(p\)；有限個 cusp branches
可取有限個常數的最大值，並非對所有 hyperbolic 元素的 uniform norm bound。

## 4. 一手來源：固定 w 可以用，聯合參數尚不能用

核對來源為 Ksenia Fedosova and Anke Pohl，
*Meromorphic continuation of Selberg zeta functions with twists having
non-expanding cusp monodromy*, Selecta Mathematica **26**, article 9 (2020)，
DOI [10.1007/s00029-019-0534-3][fp]。使用出版者 HTML 正文及下列定位。

| 定位 | 本案使用的有限範圍 |
| --- | --- |
| §2.4 | non-expanding 指每個 parabolic 矩陣的 eigenvalues 模長均為 \(1\)。 |
| Example 4.1、式 (30) | 明列 \(G=\mathrm{PSL}_2(\mathbb Z)\) 的 strict transfer setup；不是直接把 PGL billiard 的單一 Mayer operator 當作本案。 |
| Theorem 4.2(i)–(iv)、§4.3 式 (29) | 幾何有限 Fuchsian 群、strict setup、固定有限維 non-expanding 表示：右域核算子、Fredholm 實現及 \(z\) 的亞純延拓。 |
| Proposition 5.4、式 (43) | 有限指標 induction 保持 non-expanding cusp monodromy；提供 (6) 的 row-block 模型。 |
| Theorem 7.1(ii) | subgroup 表示與 induced 表示的 Selberg zeta 相等；這一項不要求 subgroup normal。 |

以上 passage 已在 2026-09-09 的前一紙面輪次核對，本次保存時再次確認；
只宣稱這些定義、定理陳述與相關公式的閱讀，不宣稱全文 proof audit。
本案 \(G\) 為幾何有限 Fuchsian 群，Example 4.1 解決所需 strict-setup 假設；
(9) 解決任意固定 \(w\) 的表示假設。因此確實得到
\[
z\longmapsto Z_G(z,\eta_w)
\quad\text{對每個固定 }w\in\mathbb C\text{ 可亞純延拓到 }\mathbb C.
\tag{12}
\]
半單性使來源的最大 Jordan 鏈長 \(d_0=1\)；對 eigenvalue \(1\) 若有鏈，
長度也為 \(1\)。固定切片可能的算子極點因而包含於
\[
\mathscr P=\{(1-j)/2:j\in\mathbb N_0\},
\tag{13}
\]
且其主部有限秩。這是容許位置的上界，不是宣稱每一點都有極點。
此處只援用 [Theorem 4.2][fp] 的固定表示結論。
尚未核得或證明足以直接代入 \(w=z\) 的 joint-param theorem；
也不聲稱文獻中絕無此類定理。來源的存在性不能替代本案的聯合依賴證明。

## 5. 雙變量乘積：有限 cycle 的 transverse k 與共同右域

定義尚未延拓的乘積
\[
\mathcal Z(z,w)=
\prod_{[R]\in\mathcal P_G}\prod_{k\ge0}
\det(I_{12m}-e^{-(z+k)L_R}\eta_w(R)),\qquad L_R=\ell(R).
\tag{14}
\]
對固定 \(R,k\)，令 \(q=e^{-(z+k)L_R}\)。由 (6) 的有限 block-cycle
determinant identity，
\[
\begin{aligned}
\det(I_{12m}-q\eta_w(R))
&=\prod_O\det(I_m-q^{d_O}e^{-w\varepsilon I(P_O)}\nu(P_O))\\
&=\prod_O\det\!\left(
I_m-e^{-(z+k)\ell(P_O)-w\varepsilon I(P_O)}\nu(P_O)\right).
\end{aligned}
\tag{15}
\]
這裡 \(P_O=a_iR^{d_O}a_i^{-1}\) 是 cover primitive lift，
\(\ell(P_O)=d_OL_R\)。特別地
\[
(e^{-(z+k)L_R})^{d_O}=e^{-(z+k)d_OL_R}
=e^{-(z+k)\ell(P_O)}.
\tag{16}
\]
\(d_O\) 同時乘入 \(zL_R\) 與 \(kL_R\)；cover 索引仍是同一個
\(k\in\mathbb N_0\)，不是漏乘 d，也不是在 cover 長度之外再乘一次 d。
本原 lift 的完整分類使用 [Euler 筆記 §3][euler] 所承接的 coset-cycle 證明。

**命題 2。** 在共同開域
\[
\Omega_+=\{(z,w)\in\mathbb C^2:
\operatorname{Re}w>0,\quad A:=\operatorname{Re}z-(1-c_0)\operatorname{Re}w>2\},
\tag{17}
\]
(14) 與下式均絕對、局部一致收斂，定義同一個非零聯合全純函數：
\[
\boxed{\mathcal Z(z,w)=
\prod_{[P]\in\mathcal P_\Gamma}\prod_{k\ge0}
\det(I_m-e^{-(z+k)\ell(P)-w\varepsilon I(P)}\nu(P)).}
\tag{18}
\]

**證明。** 因 \(\operatorname{Re}w>0\)，(2) 給
\[
\left|e^{-(z+k)\ell(P)-w\varepsilon I(P)}\right|
=e^{-\operatorname{Re}w\,T_\varepsilon(P)
-(\operatorname{Re}z+k-\operatorname{Re}w)\ell(P)}
\le e^{-(A+k)\ell(P)}.
\tag{19}
\]
沿用 [Euler 筆記 (8)–(11)][euler] 已證的
\(N_\Gamma(x)\le192e^{2x}\)、\(\ell(P)\ge\ell_*=2\operatorname{arcosh}(3/2)\)
與 \(B_m(A)\)，cover trace-log 的絕對和滿足
\[
\begin{aligned}
&\sum_P\sum_{k\ge0}\sum_{r\ge1}
\frac{|\operatorname{tr}\nu(P)^r|}{r}
\left|e^{-r(z+k)\ell(P)-rw\varepsilon I(P)}\right|\\
&\hspace{1cm}\le
\frac{B_m(A)}{1-e^{-\ell_*}},\qquad
B_m(A)=\frac{192mA e^{-(A-2)\ell_*}}
{(A-2)(1-e^{-A\ell_*})}<\infty.
\end{aligned}
\tag{20}
\]
新增因子來自 \(\sum_{k\ge0}e^{-rk\ell(P)}
\le(1-e^{-\ell_*})^{-1}\)。對 \(\Omega_+\) 的任意緊集取 \(A_{\min}>2\)
便有一致支配，故級數聯合全純。

對 ambient 固定 \(R,k\)，cycle 特徵值滿足
\(\lambda^{d_O}\in e^{-(z+k)\ell(P_O)-w\varepsilon I(P_O)}
\operatorname{Spec}\nu(P_O)\)，故 spectral radius 至多 \(e^{-(A+k)L_R}<1\)。
其 trace-log 展開按 cycle 置 \(n=d_Or\)，出現的 \(d_O/n=1/r\)，
重排後的絕對和由 (20) 控制。這是譜與 trace 界，不冒充非 normal 矩陣的 norm 界。
因此有限等式 (15) 可作無窮重排，給 (18)。
兩側均由收斂 trace-log 的指數定義，非任意 scalar principal-log 選擇；
也由 \(|e^b-1|\le e^{|b|}|b|\) 得通常的 factor-minus-one 絕對收斂。□

## 6. 實際 clock 的 ratio：分母仍是 eta_s

依 [Euler 筆記][euler] 定義直接 determinant 乘積及其倒數
\[
D_\varepsilon(s)=
\prod_{[P]\in\mathcal P_\Gamma}
\det(I_m-e^{-sT_\varepsilon(P)}\nu(P)),\qquad
\zeta_\varepsilon(s)=D_\varepsilon(s)^{-1}.
\tag{21}
\]
當 \(\operatorname{Re}s>2/c_0\)，兩個點 \((s,s)\)、\((s+1,s)\) 都在
\(\Omega_+\)，其 A 分別是 \(c_0\operatorname{Re}s\) 與
\(c_0\operatorname{Re}s+1\)。在 (18) 的絕對收斂域只移動 z，按 k telescoping：
\[
\boxed{
D_\varepsilon(s)=\frac{\mathcal Z(s,s)}{\mathcal Z(s+1,s)}
=\frac{Z_G(s,\eta_s)}{Z_G(s+1,\eta_s)},\qquad
\zeta_\varepsilon(s)=\frac{\mathcal Z(s+1,s)}{\mathcal Z(s,s)}.}
\tag{22}
\]
分母的 coefficient parameter 仍固定為 \(w=s\)，**不是 \(\eta_{s+1}\)**。
消去後留下 \(k=0\) 的 exponent
\(-s\ell(P)-s\varepsilon I(P)=-sT_\varepsilon(P)\)，故保留實際 clock。
(22) 目前僅是上述右半平面的等式，不是已完成的全平面 continuation。

## 7. 未證的 joint 義務與下一個最小問題

若要從 (12) 推進至 (22) 的對角線亞純延拓，仍需明確完成：

1. 在固定幾何 Banach 空間、固定 coefficient 維數 \(12m\) 上選定
   \(\mathcal L_{z,w}\)，證明離開固定 z 極點集合的聯合核算子全純性。
2. 對每個緊 w 集，控制 parabolic 分支尾項、參數導數及延拓餘項；
   (11) 是可用輸入，不是已完成的共同函數空間與核性估計。
3. 證明極點主部的有限秩局部一致有界、residue 與餘項對 w 全純，
   再建立聯合亞純 Fredholm determinant，並在 \(\Omega_+\) 匹配 (14)。
4. 證明可沿 \((s,s)\)、\((s+1,s)\) 限制，排除整條曲線落入不可限制的
   polar/indeterminate 情形，並處理 ratio 的分母及可能相消。

若以上義務閉合，才可由同一解析函數的合法限制與 (22) 推進實際 clock 的延拓；
「每個固定 w 都可延拓」不是本文件採用的聯合參數定理。

**下一個最小引理提議，未研究亦未證明。** 固定來源 Example 4.1 的一個
parabolic branch p 與其幾何函數空間，使用 (9) 將係數冪化為固定酉係數：
核對該 branch-tail operator 能否在固定 z 極點集合外聯合全純，
並取得 compact-w 一致的核性估計及有限秩 residue。先處理單一 branch，
不要在此提議階段宣布整個 operator、joint determinant 或 diagonal continuation。

## 8. 實際操作與不升格項目

本次讀取適用 ARS router、academic-paper workflow、argument-builder 指令、
docs/workflow.md 與兩份直接上游筆記；再次核對出版者 HTML 的上列定位，
以 apply_patch 僅新增本文件，隨後作文本與行數檢查。
另有同模型子代理對 (6)–(9)、(15)–(16)、(22) 作有界只讀代數檢查；
其一致意見不是獨立科學證據或外部 peer review。本文為 AI 輔助內部紙面推導。

沒有構造或執行 transfer operator，沒有新實驗、prime/zero fitting、owner 枚舉
或 frozen 138-row 定位。沒有更改時鐘、index、\(k=2y+z\)、Hecke 或既有 H31
失敗記錄；未證 ambient scalar physical roof、固定酉表示替換、自伴算子、
全局 determinant equality、cusp/scattering 正則化或任何 Route/Stage 升格。
固定表示的文獻延拓與本案未證的 joint-param 實現必須繼續分開。

[clock]: ../../26-level11-newform-time-change/README.md#frozen-dynamical-system
[holonomy]: internal_goal01_natural_holonomy_and_induced_transfer_20260909.md
[euler]: internal_goal01_induced_euler_product_absolute_convergence_20260909.md
[fp]: https://link.springer.com/article/10.1007/s00029-019-0534-3
