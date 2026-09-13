# P31 Goal 01：誘導 Euler product 的明確絕對收斂域

日期：2026-09-09。內部有界理論筆記；保存緊接前一紙面輪次已完成的證明。
本次只新增本文件，不修改先前筆記、原稿、鎖、receipts、Route 或 Stage 狀態。
不執行科學程式、實驗、producer、closed-orbit census 或 frozen 138-input 檢查。
方法使用 ARS 的有界 claim/proof/counterclaim 組織與 `docs/workflow.md` 的證據邊界，
不是 full pipeline、正式審稿、publication readiness 或新實驗結果。

## 1. 固定輸入、方向與主定理

令 \(G=\mathrm{PSL}_2(\mathbb Z)\)、\(\Gamma=\Gamma_0(11)/\{\pm I\}\)，
並沿用 [P26 固定時鐘][clock] 及 [holonomy 筆記][holonomy]：
\[
\alpha=\operatorname{Re}(2\pi i f(z)\,dz),\quad
\rho_\varepsilon(v)=1+\varepsilon\alpha(v),\quad
X_\varepsilon=X_{\rm geo}/\rho_\varepsilon,
\qquad \rho_\varepsilon\ge c_0>0.
\tag{1}
\]
\(\varepsilon\in\mathbb R\) 固定。對原正密度區間，可以明確選
\(c_0=1-|\varepsilon|\|\alpha(v)\|_\infty>0\)。此處 \(\rho\) 是 slowness，
不是速度；所有 \(\ell\) 都是曲率負一、單位速 geodesic 的幾何長度。
固定 \(Y_0(11)\) 上 rank-\(m\) 酉平坦局部系，即 \(\nu:\Gamma\to U(m)\)，
並以 \(\nu(P)\) 記其正向閉軌 monodromy。
loop/deck convention 完全沿用 [holonomy 筆記 §§2–5][holonomy]，不另作矩陣取逆。

閉形式的實週期 \(I:\Gamma\to\mathbb R\) 為同態；令
\[
T_\varepsilon(P)=\ell(P)+\varepsilon I(P)\ge c_0\ell(P),\qquad
\kappa_{\varepsilon,s}(\gamma)=e^{-s\varepsilon I(\gamma)},\qquad
\eta_s=\operatorname{Ind}_\Gamma^G(\nu\otimes\kappa_{\varepsilon,s}).
\tag{2}
\]
\(\eta_s\) 的 rank 為 \(12m\)，一般非酉，且依賴 s。
其意義是同一閉形式修正 connection 的正向誘導傳輸，參數非事後選權。

記 \(\mathcal P_G,\mathcal P_\Gamma\) 為 primitive **有向 hyperbolic 共軛類**。
只取各群內的實際共軛商，**不額外識別取逆**；若 ambient 元素本已與其逆共軛，
則該共軛類仍只算一次。parabolic、elliptic 與 identity 不進入乘積。

**定理。** 在共同開半平面
\[
\boxed{\mathcal H_{c_0}=\{s\in\mathbb C:\operatorname{Re}s>2/c_0\}}
\tag{3}
\]
內，下列兩個 Euler products 絕對、局部一致收斂，定義非零全純函數，且
\[
\boxed{
\prod_{[P]\in\mathcal P_\Gamma}
\det(I_m-e^{-sT_\varepsilon(P)}\nu(P))^{-1}
=
\prod_{[R]\in\mathcal P_G}
\det(I_{12m}-e^{-s\ell(R)}\eta_s(R))^{-1}.}
\tag{4}
\]
本文件明確採 inverse-determinant 的 Euler convention；若需要 determinant
product，兩側同時取倒數即可。不包含 Selberg product 的額外橫向因子。
此定理不依賴 \(I\ne0\)、zero-transfer 或 H31 的否定；只需 (1)–(2)、酉性與
下述 finite-cover primitive-lift 分類及有限 factorization。

## 2. 正代表存在性：不使用 unique normal form

令
\[
S=\left[\begin{pmatrix}0&-1\\1&0\end{pmatrix}\right],\qquad
T=\left[\begin{pmatrix}1&1\\0&1\end{pmatrix}\right],\qquad U=ST.
\]
S、T 生成 G：對 determinant-one 整數矩陣的第一個欄向量用左乘 \(T^n\)
與 S 執行 Euclidean algorithm，可化為 \((\pm1,0)^t\)，餘下為 T 的冪到中心符號。
又 \(S^2=1,U^3=1\)，而 \(T=SU\)，所以 S、U 也生成 G。

取任意 hyperbolic 元素的一個 S、U 詞。只用上述有限階關係合併相鄰的同類
syllables，再將首尾同類者經循環共軛移到一起合併；每次這種操作縮短 syllable
數，故終止。結果不可能為空詞或單一 \(S,U,U^2\)，因為那些元素非 hyperbolic。
終止後的 cyclically reduced alternating 詞可循環移位為
\[
SU^{e_1}\cdots SU^{e_k},\qquad e_j\in\{1,2\}.
\tag{5}
\]
這只證明存在一個代表，**沒有使用或宣稱唯一 normal form，也不需先證群無額外關係**。

在 G 中有
\[
SU=\mathsf L=\left[\begin{pmatrix}1&1\\0&1\end{pmatrix}\right],\qquad
SU^2=\mathsf R=\left[\begin{pmatrix}1&0\\1&1\end{pmatrix}\right].
\tag{6}
\]
若 (5) 只含一種塊，就是 parabolic \(\mathsf L^k\) 或 \(\mathsf R^k\)。
hyperbolic 情形必含兩種；其 determinant-one 整數矩陣乘積四個 entries 全為正。
例如第一次同時出現兩種塊時乘積已嚴格為正，其後再乘任一塊保持正性。
因此每個有向 hyperbolic 共軛類都有嚴格正整數矩陣代表。
取逆類也適用此論證，不需把方向合併；矩陣記號 \(\mathsf R\) 與軌道代表 R 不同。

## 3. 粗計數及 cover 計數的依賴

令 \(N_G(x)=\#\{[R]\in\mathcal P_G:\ell(R)\le x\}\)。對 §2 的正代表
\(M=(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})\)，若 \(\ell(M)\le x\)，則
\[
a+d=2\cosh(\ell(M)/2)\le Q:=2e^{x/2},\quad
a,d\le Q,\quad bc=ad-1,\quad 1\le b\le Q^2.
\]
選定 a、d、b 後，c 唯一；非整數上界以 floor 計數只會減少數量。
因此這些矩陣至多 \(Q^4\) 個，共軛類不會更多，故
\[
\boxed{N_G(x)\le16e^{2x}.}
\tag{7}
\]
這一矩陣上界還計入非本原類及可能的重複正代表，故對本原有向類仍成立。
它不是 prime-geodesic asymptotic，也不是實際枚舉。

對 cover，使用 [coset-cycle 筆記定理 3][cycles] 的完整分類，而非只靠群指標：

- 每個 subgroup primitive hyperbolic 類有唯一所屬的正向 ambient primitive family。
- 在 \(\Gamma\backslash G\) 上右乘該 R 的 cycles，與該 family 的全部不同
  subgroup primitive lifts 一一對應；最小 cycle 度數為 \(d_O\ge1\)。
- \(\ell(P_O)=d_O\ell(R)\)，且 \(\sum_Od_O=12\)，故一個 family 至多十二個 lifts。

此分類在 unit-tangent quotient 的十二層 flow cover 上成立，不要求 \(\Gamma\)
normal，也不把 ambient 二維 orbifold 當成無撓曲面。左右陪集換算為
\(h\Gamma\leftrightarrow\Gamma h^{-1}\)：左乘 r 對應右乘 \(r^{-1}\)。
本文採右乘 R 的正向 monodromy，其 lift 元素是 \(a_iR^{d_O}a_i^{-1}\)。

若 \(\ell(P)\le x\)，其 family 的 \(\ell(R)\le x\)；因此
\[
\boxed{N_\Gamma(x):=\#\{[P]\in\mathcal P_\Gamma:\ell(P)\le x\}
\le12N_G(x)\le192e^{2x}.}
\tag{8}
\]
只知 \([G:\Gamma]=12\) 而沒有上述 primitive 分類，不能跳過此依賴。
正跡 hyperbolic 整數矩陣的跡至少為 3，給出兩側共同的幾何長度下界
\[
\ell(P),\ell(R)\ge\ell_*:=2\operatorname{arcosh}(3/2)>0.
\tag{9}
\]

## 4. Cover 雙重 log 級數的明確絕對界

令 \(\sigma=\operatorname{Re}s\)、\(A=c_0\sigma>2\)。由 (8) 與非負 Tonelli，
\[
\sum_Pe^{-A\ell(P)}
=A\int_{\ell_*}^{\infty}N_\Gamma(t)e^{-At}\,dt
\le\frac{192A}{A-2}e^{-(A-2)\ell_*}.
\tag{10}
\]
這裡從 \(e^{-A\ell}=A\int_\ell^\infty e^{-At}\,dt\) 得等號，包含 \(\ell_*\)
的可能原子，不需遺漏端點或預先假定無窮和有限。
由 \(\nu(P)\) 酉，\(|\operatorname{tr}\nu(P)^r|\le m\)。因此
\[
\begin{aligned}
\sum_P\sum_{r\ge1}\frac{e^{-\sigma rT_\varepsilon(P)}
|\operatorname{tr}\nu(P)^r|}{r}
&\le\frac{m}{1-e^{-A\ell_*}}\sum_Pe^{-A\ell(P)}\\
&\le
\boxed{B_m(A):=\frac{192mA\,e^{-(A-2)\ell_*}}
{(A-2)(1-e^{-A\ell_*})}<\infty.}
\end{aligned}
\tag{11}
\]
第一步只用 \(1/r\le1\)、\(T_\varepsilon(P)\ge c_0\ell(P)\) 與幾何級數。
對任意 \(\sigma_0>2/c_0\)，用 \(A_0=c_0\sigma_0\) 逐項支配整個
\(\operatorname{Re}s\ge\sigma_0\)，即得局部一致的絕對收斂。

## 5. 非酉 induction：只主張譜界與 trace 界

對每個 \([R]\in\mathcal P_G\)，令
\[
W_R(s)=e^{-s\ell(R)}\eta_s(R).
\tag{12}
\]
[holonomy 筆記定理 4、6][holonomy] 在相容的起點框架下給
\[
\det(I-zW_R(s))
=\prod_O\det(I_m-z^{d_O}e^{-sT_\varepsilon(P_O)}\nu(P_O)).
\tag{13}
\]
各塊按正向 path lifting 與矩陣在向量上由右向左的乘法次序組成。
改起點只共軛，不能任意反轉 subgroup holonomy 或以 \(d_O\ell(R)\) 代替真週期。

由 (13)，每個屬於 d-cycle 的 eigenvalue \(\lambda\) 滿足
\(\lambda^d\in e^{-sT_\varepsilon(P_O)}\operatorname{Spec}\nu(P_O)\)。
所以在 \(\sigma>0\) 時
\[
\rho_{\rm sp}(W_R(s))\le e^{-c_0\sigma\ell(R)}<1,
\qquad
|\operatorname{Tr}W_R(s)^n|\le12m\,e^{-An\ell(R)}.
\tag{14}
\]
trace of powers 是 eigenvalues 冪的和，計代數重數；這一步不需酉性或 normality
作用於 \(W_R\) 本身。酉性只用在原 \(\nu(P_O)\) 的 eigenvalues 模長為 1。
**(14) 不是固定平坦框架中 \(\|W_R(s)\|\) 或 \(\|\eta_s(R)\|\) 的 uniform bound。**
一般非酉、非 normal 矩陣的 norm 可遠大於 spectral radius，不能作此升格。

對 (14) 用 (7)、(9) 與 §4 同樣的求和，得到
\[
\sum_R\sum_{n\ge1}\frac{|\operatorname{Tr}W_R(s)^n|}{n}
\le B_m(A).
\tag{15}
\]
常數仍為 192，因 ambient 計數的 16 乘以 rank \(12m\)。
固定陪集代表時，\(\eta_s(R)\) 的 entries 是固定 holonomy 乘上閉形式週期的
指數，故對每個 R 為 s 的 entire 函數。結合 (15)，其雙重級數局部一致全純。

## 6. 絕對重排、規範 log 與 Euler 等式

有限 cycle trace 公式是
\[
\operatorname{Tr}W_R(s)^n
=\sum_{O:\,d_O\mid n}d_O\,
e^{-s(n/d_O)T_\varepsilon(P_O)}
\operatorname{tr}\nu(P_O)^{n/d_O}.
\tag{16}
\]
展開右側 cycles 後的絕對和也由 (11) 控制：每個 cover primitive 恰來自一個
family 的一條 cycle，且置 \(n=d_Or\) 時 \(d_O/n=1/r\)。因此絕對收斂允許
重排；不是先作形式級數重排，再把所得結果當成收斂證明。
於 \(\mathcal H_{c_0}\) 得
\[
\sum_R\sum_{n\ge1}\frac{\operatorname{Tr}W_R(s)^n}{n}
=\sum_P\sum_{r\ge1}
\frac{e^{-srT_\varepsilon(P)}\operatorname{tr}\nu(P)^r}{r}.
\tag{17}
\]

對 finite matrix B 若 \(\rho_{\rm sp}(B)<1\)，
\(\exp(\sum_{n\ge1}\operatorname{Tr}(B^n)/n)=\det(I-B)^{-1}\)。
這是各 eigenvalue 的標準 \(-\log(1-\lambda)\) 級數；不需選擇跨零點的任意
log branch。(14) 及 \(e^{-\sigma T_\varepsilon(P)}<1\) 使兩側每個 factor 適用。
將 (17) 指數化即得 (4)，並給出由此級數指定的規範 log。

以上也滿足通常 Euler product 的絕對收斂意義：若每個 factor 的規範 log 為
\(b_j\)，則 \(\sum_j|b_j|<\infty\)，而
\(|e^{b_j}-1|\le e^{|b_j|}|b_j|\)，故 \(\sum_j|\text{factor}_j-1|<\infty\)。
同理在閉子半平面逐項一致支配；乘積不依賴合法枚舉順序，且在 (3) 內非零全純。
這是本次真正新增的無窮乘積結論；舊 [holonomy 筆記][holonomy] 僅證有限乘積，
本文件不把當時明示未證的無窮收斂，改寫為其既有結果。

## 7. 來源核對、證據範圍與未解義務

- 本地 [P26 README，Frozen dynamical system][clock] 提供固定形式、真時鐘與正區間。
  本地 [holonomy 筆記 §§4–5][holonomy] 提供 s-dependent flat induction 與有限
  block-cycle factorization；[coset-cycle 筆記 §§2–3][cycles] 提供 primitive
  lifts 的完整分類。以上是明示依賴，不是外部獨立複核。
- Christopher-Lloyd Simon，*Arithmetic and Topology of Modular Knots*，2022 年博士
  論文，作者站點 [PDF][simon]，Lemma 2.18、Corollary 2.19。緊接前一紙面輪次已於
  2026-09-09 核對題名頁、作者、2022 年答辯資訊與這兩個 passage。
  Corollary 2.19 支持 hyperbolic 共軛類有 nonnegative \(\mathsf L,\mathsf R\)-word
  代表，其前文指出 hyperbolic 情形含兩種字母。本文以 (6) 的顯式矩陣命名為準，
  不要求文獻的 L/R 標籤相同。§2 另給只需存在性的群關係證明，§3 的粗計數與
  §§4–6 的解析估計由本文推導，不歸作該來源的定理。
- 外部來源核對使用作者 PDF 的可讀正文與章節定位，未運行本地 PDF preflight，
  不宣稱全文閱讀、完整 bibliography audit、獨立審稿或 novelty。

本文件是 AI 輔助的內部紙面證明；不是實驗、數值擬合或 census。
本輪動作限於適用 ARS 指令與本地檔案閱讀、前次有效來源核對的承接、新檔存在性
確認、`apply_patch` 新建及其文本／行數檢查；無科學程式、舊檔或舊鎖修改。

明確未解與未授權升格：

1. 半平面邊界 \(\operatorname{Re}s=2/c_0\)、最佳 abscissa 及其左側的 continuation
   均未處理；粗計數 K=2 不是最優 entropy 或 prime-geodesic theorem。
2. 未構造共同 Banach/Hilbert 空間上的 transfer operator、核性、trace formula、
   Fredholm determinant、meromorphic continuation 或 cusp/scattering 正則化。
3. 右側是 \(s\mapsto\eta_s\) 的 parameter-dependent Euler product，不是固定酉
   表示的普通替換，更不是固定 self-adjoint operator 的 determinant 等式。
4. 不推出物理時鐘下降；共同參數仍來自 ambient geodesic flow，真時鐘保存在
   vector-valued monodromy 中。既有 H31 失敗記錄不被修改或撤銷。
5. 未新增 prime/zero 頻率、定位 frozen 138 rows、產生 owner ID 或運行任何枚舉；
   原稿、Route、Stage 及任何正式結論的變更不在本文件授權內。

[clock]: ../../26-level11-newform-time-change/README.md#frozen-dynamical-system
[holonomy]: internal_goal01_natural_holonomy_and_induced_transfer_20260909.md
[cycles]: internal_coset_cycle_lifts_and_oriented_class_splitting_20260909.md
[simon]: https://christopherlloyd.github.io/works/pre-publications/2022-07-14_AriTopoModuKnots_compressed.pdf
