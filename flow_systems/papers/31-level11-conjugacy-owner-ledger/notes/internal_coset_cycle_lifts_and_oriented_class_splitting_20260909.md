# P31：Coset 周期提升與有向共軛類分裂

日期：2026-09-09。第五次五篇整輪的內部有界理論筆記。只新增本文件，不執行矩陣／coset 枚舉、frozen 138 inputs、pair audit、producer、fixture、實驗或正式狀態更新。

## 0. 本輪定理的範圍與兩項關鍵區分

固定一個已證 **ambient primitive、hyperbolic、有向** 的 \(r\in G=\mathrm{PSL}_2(\mathbb Z)\)，以及 \(\Gamma=\Gamma_0(11)/\{\pm I\}\)。本輪將 [詞根與最小返回週期][roots] 的單元素接口擴展為整個 lifting family：

> r 在十二個 cosets 上的每個周期軌道 \(\mathcal O\)，給出一個不同的 subgroup primitive 有向共軛類；若周期長為 \(d_{\mathcal O}\)，相應元素可取 \(P_{\mathcal O}=H^{-1}R^{d_{\mathcal O}}H\)，其中 \(H\Gamma\in\mathcal O\)、R 是 r 的正跡 lift。這些類恰覆蓋 ambient 正向本原根與 r 共軛的全部 subgroup primitive 類。

這不是說 R 的**單一 ambient 元素共軛類**本身對應所有周期。固定 \(R^m\) 的 ambient class 只對應 \(d_{\mathcal O}\mid m\) 的 cycles；特別是 R 本身只對應 1-cycles。不同周期的首次返回提升通常落在不同正冪的 ambient classes 中。

本輪的長度倍乘是曲率負一的 **geodesic translation length**。原稿的實際流是 \(X_{\rm geo}/\rho_\epsilon\)，不是裸 geodesic flow；本輪不能僅據 coset 度數推斷不同提升的實際 time-changed periods 是同一 ambient period 的整數倍。§5 將這項推斷限制與合法的遍歷倍乘分開。

方法沿用 ARS academic-paper 的 argument-builder 單一有界論證階段。沒有啟動 full pipeline、改造原 owner 值域、產生 canonical bytes 或修改 \(k=2y+z\)、newform differential、Hecke、時鐘、`delta`／`kappa` 或 G/I/C 契約。

## 1. 群、左 cosets 與十二個射影狀態

記

\[
\widetilde G=\mathrm{SL}_2(\mathbb Z),\quad
G=\widetilde G/\{\pm I\},\quad
\widetilde\Gamma=\{M\in\widetilde G:M_{21}\equiv0\pmod {11}\},\quad
\Gamma=\widetilde\Gamma/\{\pm I\}.
\tag{1}
\]

R 始終是 r 的唯一正跡 lift，\(\operatorname{tr}R>2\)。ambient primitiveness 是已有前提，可由 [cyclic-word 證書][roots] 或先前 trace recurrence 確證，不由本輪期待的 cycle 數推定。

採用**左 coset 集合**

\[
X=G/\Gamma=\{h\Gamma:h\in G\},\qquad
\phi(h\Gamma)=h\infty\in\mathcal S:=\mathbb P^1(\mathbb F_{11}).
\tag{2}
\]

此處 \(\infty=[1:0]\)，整數矩陣先模 11，再按列向量左作用。\(\Gamma\) 恰為 infinity 的 stabilizer，所以 \(\phi\) 良定且單射；取

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
T^zS\infty=z
\]

又得滿射。因此 \(|X|=|\mathcal S|=12\)。矩陣 \(\pm H\) 的射影作用相同。

本筆記用的 permutation 是

\[
\tau_r(h\Gamma)=rh\Gamma,
\qquad\phi(\tau_rx)=\overline R\phi(x).
\tag{3}
\]

對一個 coset \(x=h\Gamma\)，令 \(d_x\ge1\) 是其最小返回時間。membership 與 return 的方向為

\[
\tau_r^j x=x
\iff r^jh\Gamma=h\Gamma
\iff h^{-1}r^jh\in\Gamma.
\tag{4}
\]

### 1.1 右 coset 對照，不能省去反號

取逆給出 \(h\Gamma\mapsto\Gamma h^{-1}\) 的雙射，將 (3) 的左乘 r 變成
\(\Gamma h^{-1}\mapsto\Gamma h^{-1}r^{-1}\) 的右乘 \(r^{-1}\)。因此

\[
\langle r\rangle\backslash G/\Gamma
\quad\longleftrightarrow\quad
\Gamma\backslash G/\langle r\rangle
\tag{5}
\]

由取逆一一對應，但箭頭方向相反。
若用右 cosets 上右乘 r 表示正向 geodesic monodromy，對應的左 coset action 是 \(r^{-1}\)，而非 r。兩個逆 permutation 的 orbit 集合與最小周期相同，所以本輪的 cycle classification 不變；其提升元素仍使用 (4) 中的**正冪** \(h^{-1}r^{d_x}h\)。

## 2. 每個 cycle 的首次返回是 subgroup primitive

對 cycle \(\mathcal O\) 選任一 \(x=h\Gamma\in\mathcal O\)，令 \(d=d_x\)，並選 determinant-one lift H。定義

\[
\boxed{P_x=H^{-1}R^dH.}
\tag{6}
\]

由 (4)，\(P_x\in\widetilde\Gamma\)；它 determinant 1、正跡且 hyperbolic。這是 exact matrix formula，不是只到 \(\pm\) 的等式。

所用中心化子事實沿用 [ambient root 引理][coset]：對每個 \(d\ge1\)，

\[
C_G(r^d)=\langle r\rangle.
\tag{7}
\]

其自含依據是：在 R 的兩條實特徵線基底中，projective 中心化子是實一參數對角群；與離散 G 相交為非零離散循環子群，ambient primitive r 正是沿該方向的生成元。正跡排除 lift 共軛中的負號。

**引理 1。** (6) 在 \(\Gamma\) 中本原。

**證明。** 若 \([P_x]=a^k\)、\(a\in\Gamma\)、\(k\ge2\)，則 \(hah^{-1}\) 交換 \(r^d\)，由 (7) 可寫為 \(r^j\)。因 r 無限階，\(jk=d\)，故 \(0<j<d\)。另一方面 \(a=h^{-1}r^jh\in\Gamma\)，由 (4) 使 x 在 j 步返回，違反 d 的最小性。□

**引理 2（代表選擇）。** (6) 的 \(\Gamma\)-conjugacy class 只依賴 cycle，不依賴其起點或 coset representative。

**證明。** 同 cycle 的另一個代表可寫為 \(k=r^n h\gamma\)、\(\gamma\in\Gamma\)。它有相同 d，且

\[
k^{-1}r^dk=\gamma^{-1}h^{-1}r^dh\gamma.
\tag{8}
\]

故為同一 subgroup class。沿 cycle 換成 \(r^nh\) 時更得到同一 projective 元素；右乘 \(\gamma\) 才對應 subgroup 共軛。lift 的 central signs 不改矩陣共軛結果。□

因此可寫 \(\mathfrak p_{\mathcal O}=\operatorname{cl}_\Gamma(P_x)\)。這裡的 class 保留方向，沒有加上取逆等價。

## 3. 雙商給出所有 primitive lifts 的雙射

明確定義 lifting family

\[
\mathscr P_\Gamma(r)=
\left\{\operatorname{cl}_\Gamma(P):
P\text{ 正跡 hyperbolic 且 subgroup primitive},\quad
\exists h\in G,\ m\ge1:\ [P]=h^{-1}r^m h\right\}.
\tag{9}
\]

等價地，P 的正向 ambient primitive root 與 r 在 G 中共軛。因 r 已是 ambient primitive，不能在 (9) 中任意換成真冪。

**定理 3（完整提升分類）。**

\[
\boxed{
\langle r\rangle\backslash X
\simeq \langle r\rangle\backslash G/\Gamma
\xrightarrow[\mathcal O\mapsto\mathfrak p_{\mathcal O}]{\ \sim\ }
\mathscr P_\Gamma(r).}
\tag{10}
\]

**滿射。** 若 P 如 (9)，取 \(x=h\Gamma\)。由 membership，\(d_x\mid m\)，而
\([P]=(h^{-1}r^{d_x}h)^{m/d_x}\)。引理 1 已證括號內是 subgroup primitive；P 亦本原，故 \(m=d_x\)，所以 P 來自該 cycle。

**單射。** 假設 \(\gamma(h^{-1}r^dh)\gamma^{-1}=k^{-1}r^ek\)、\(\gamma\in\Gamma\)。取正跡 lifts，令 R 的擴張特徵值為 \(\lambda>1\)。共軛保跡，而
\(\lambda^j+\lambda^{-j}\) 對正整數 j 嚴格遞增，所以 \(d=e\)。於是

\[
k\gamma h^{-1}\in C_G(r^d)=\langle r\rangle,
\qquad k=r^n h\gamma^{-1}
\tag{11}
\]

對某個整數 n 成立，兩 cosets 因而位於同一 cycle。□

這裡是 **centralizer quotient**，不是 \(N_G(\langle r\rangle)\) 的 normalizer quotient。後者可能還含 reverser，會進一步識別兩個不同的 inverse-oriented subgroup classes，違反目前的 owner 定義。

若把 ambient representative 換成 \(r'=a^{-1}ra\)，coset 雙射
\(h\Gamma\mapsto a^{-1}h\Gamma\) 與兩個 permutations 相容，且新提升矩陣仍為 \(H^{-1}R^dH\)。因此 (10) 依赖 ambient 共軛類而非選用矩陣；這仍不是跨人口 canonical serialization。

## 4. 固定 \(R^m\) 的 class splitting 與全部遍歷

令 \(\mathcal C_m\) 是 \(R^m\) 的 ambient conjugacy class 中落在 \(\Gamma\) 的 subgroup classes，m 為固定正整數。

**定理 4。**

\[
\boxed{
\mathcal C_m
\simeq\{\mathcal O:d_{\mathcal O}\mid m\},
\qquad
\mathcal O\longmapsto
\operatorname{cl}_\Gamma\bigl(P_{\mathcal O}^{m/d_{\mathcal O}}\bigr).}
\tag{12}
\]

**證明。** \(h^{-1}r^mh\in\Gamma\) 當且僅當 x 在 m 步返回，也即 \(d_x\mid m\)。同 cycle 的點給 subgroup 共軛；若不同點產生共軛，與 (11) 同樣的計算使用 \(C_G(r^m)=\langle r\rangle\)，迫使它們位於同一 cycle。所得元素正是 (6) 的 \(m/d_x\) 次遍歷。□

它與 [前 finite-coset 筆記 §8][coset] 的公式一致：

\[
\mathcal C_m\simeq
\operatorname{Fix}(\overline R^{m})/\langle\overline R\rangle.
\tag{13}
\]

不能把分母換成 \(\langle\overline R^{m}\rangle\)：在 fixed set 上後者每點皆不動，會把長度 d 的整個 cycle 錯算為 d 個 subgroup classes。

令 \(c_d\) 表示長度 d 的 cycle 數。則

\[
\#\operatorname{Fix}(\tau_r^m)=\sum_{d\mid m}d c_d,
\qquad\#\mathcal C_m=\sum_{d\mid m}c_d,
\qquad\sum_d d c_d=12.
\tag{14}
\]

特別地，\(\mathcal C_1\) 只含 1-cycles，且其元素均 subgroup primitive；\(\mathcal C_m\) 的元素本原當且僅當其 cycle 長度正好等於 m。這與「全部 primitive lifts 對應全部 cycles」是兩個不同陳述。

## 5. 遍歷度、測地長度與原時間變換

對正跡 R 的擴張特徵值 \(\lambda>1\)，定義曲率負一的測地長度

\[
\ell_{\rm geo}(R)=2\log\lambda
=2\operatorname{arcosh}(\operatorname{tr}R/2).
\tag{15}
\]

因 R 在實共軛後為 \(\operatorname{diag}(\lambda,\lambda^{-1})\)，上半平面作用是 \(z\mapsto\lambda^2z\)；沿垂直軸積分 \(dy/y\) 即得 (15)。正整數冪的擴張特徵值是 \(\lambda^d\)，故

\[
\boxed{
\ell_{\rm geo}(P_{\mathcal O})
=d_{\mathcal O}\ell_{\rm geo}(R),\qquad
\sum_{\mathcal O}\ell_{\rm geo}(P_{\mathcal O})
=12\ell_{\rm geo}(R).}
\tag{16}
\]

cycle 中的 d 個 cosets 是同一 lifted primitive orbit 的 d 個 fiber positions，不是 d 個不同 lifted owners。其首次閉合在 base primitive geodesic 的 d 次正向遍歷之後。亦可在
\(\Gamma\backslash\mathrm{PSL}_2(\mathbb R)\to G\backslash\mathrm{PSL}_2(\mathbb R)\)
的十二層覆蓋上理解：離散群左乘自由，標準 geodesic flow 右乘；§1.1 已說明其 monodromy 與本筆記 coset 箭頭的關係。無須把有 elliptic points 的 ambient 基底誤當無挠曲面。

**原時鐘限制。** P31 凍結的是正時間變換 \(X_{\rm geo}/\rho_\epsilon\)。若 \(\gamma_P\) 表示該有向幾何周期軌道，沿單位速 geodesic 參數 s，其實際周期是

\[
\mathcal T_\epsilon(P)=
\int_{\gamma_P}\rho_\epsilon\,ds.
\tag{17}
\]

對同一 subgroup orbit 的 k 次正向遍歷，確有
\(\mathcal T_\epsilon(P^k)=k\mathcal T_\epsilon(P)\)。但不同 cycles 是不同軌道；若另證 \(\rho_\epsilon\) 從同一 ambient flow 下降，則可以把其 periods 寫成 \(d_{\mathcal O}\) 乘同一 ambient period。這是充分條件，不聲稱該周期關係反過來迫使函數下降。本輪既不建立也不假定該下降，不能僅據 coset 度數推斷該周期關係。因此 (16) 的總長等式不被升格為原時間變換的總周期等式。

同理，取逆保持 \(\ell_{\rm geo}\)，但在沒有額外 reversal symmetry 的情況下，不可從本輪推出
\(\mathcal T_\epsilon(P^{-1})=\mathcal T_\epsilon(P)\)。newform、period coordinate \(k=2y+z\) 與 Hecke 資料均按原合同保留，不由 d 取代。

## 6. 不枚舉也能得到的 mod-11 cycle 型限制

下列是 determinant-one 線性代數的必要分類，不是對任何 frozen R 計算出的 cycle type。令 \(M\in\mathrm{SL}_2(\mathbb F_{11})\) 是 R 的 reduction，\(t=\operatorname{tr}M\)。其特徵多項式為 \(X^2-tX+1\)。

### 6.1 Scalar、重根非 scalar 與 split 情形

- 若 \(M=\pm I\)，射影作用是 identity，cycle 型為 \(1^{12}\)。
- 若特徵多項式重根但 M 非 scalar，乘適當 central sign 後為 \(I+N\)，其中 \(N\ne0\)、\(N^2=0\)。\((I+N)^j=I+jN\)，故 projective order 為 11。唯一 fixed line 是 \(\ker N\)，其餘 11 點構成一個 11-cycle，型為 \(1\cdot11\)。
- 若兩個不同 eigenvalues \(\lambda,\lambda^{-1}\) 在 \(\mathbb F_{11}\) 中，兩條 eigenlines 固定。其餘斜率乘以 \(\lambda^2\) 或其倒數；\((\lambda^2)^5=1\) 且 \(\lambda^2\ne1\)，所以 order 為 5，十個非零斜率分成兩個 5-cycles，型為 \(1^2 5^2\)。

### 6.2 Nonsplit 情形

若特徵多項式在 \(\mathbb F_{11}\) 不可約，取二次域
\(K=\mathbb F_{11}[\lambda]\)，其有 121 個元素。Frobenius \(x\mapsto x^{11}\) 保持該多項式；因 \(X^{11}-X\) 已有全部 11 個基域元素為根，不可能再含 \(\lambda\)，所以

\[
\lambda^{11}=\lambda^{-1},\qquad\lambda^{12}=1.
\tag{18}
\]

兩根不同，M 在 K 上可對角化。projective order d 是最小的 \(\lambda^d\in\{\pm1\}\)；由 \((\lambda^6)^2=1\)，得 d 整除 6，且 \(d>1\)，故 \(d\in\{2,3,6\}\)。

若 \(0<j<d\) 時 \(M^j\) 有基域 fixed line，則其一個 eigenvalue \(\lambda^j\) 或 \(\lambda^{-j}\) 在基域；Frobenius 使它等於自己的倒數，所以必為 \(\pm1\)。對角化後 \(M^j\) 便是 scalar，與 d 的最小性矛盾。因此每個 orbit 長度恰為 d，給出 \(2^6\)、\(3^4\)、\(6^2\)。

綜合得到有限的可能型：

| mod-11 射影類型 | 十二點 cycle 型 | subgroup primitive lifts 的遍歷度 | 提升類數 |
| --- | --- | --- | --- |
| identity | \(1^{12}\) | 十二個 1 | 12 |
| 非 scalar 重根 | \(1\cdot11\) | 1、11 | 2 |
| split semisimple | \(1^2 5^2\) | 1、1、5、5 | 4 |
| nonsplit，order 2 | \(2^6\) | 六個 2 | 6 |
| nonsplit，order 3 | \(3^4\) | 四個 3 | 4 |
| nonsplit，order 6 | \(6^2\) | 6、6 | 2 |

這是 \(\mathrm{PSL}_2(\mathbb F_{11})\) 的 action 限制，不是任意十二點 permutation 或整個 \(\mathrm{PGL}_2\) 的分類。它進一步限制 cycle 長度只能為 \(1,2,3,5,6,11\)，且提升類數只能為 \(2,4,6,12\)。原先 \(d\le12\) 的一般狀態上界仍然正確。

本輪沒有選擇實際 R、求取其 reduction、遍歷十二點或聲稱每種型都已由本案某個 frozen primitive input 實現。表中類數是 (9) 的理論 lifting family 大小，不是 frozen population 的 owner count。

## 7. 取逆、ambient reverser 與 subgroup 不自逆邊界

對 base \(r^{-1}\)，permutation 與 (3) 互逆，cycles 作為集合不變、箭頭反向。用同一 h，有

\[
H^{-1}R^{-d}H=P_{\mathcal O}^{-1}.
\tag{19}
\]

因此 inversion 給 \(\mathscr P_\Gamma(r)\) 與 \(\mathscr P_\Gamma(r^{-1})\) 的雙射，保持 cycle degree 及 geodesic length。

若 \(r\not\sim_G r^{-1}\)，兩個 lifting families 不相交：否則某個 subgroup primitive 元素的唯一正向 ambient root 同時與兩者共軛，矛盾。此時不能在單一 family 裡就地配對 inverse owners。

### 7.1 若 ambient class 確實自逆，cycle pairing 不是 identity

假設已有 exact ambient reverser J，滿足

\[
JRJ^{-1}=R^{-1}.
\tag{20}
\]

J 交換 R 的兩條特徵線；determinant 1 因而給 \(\operatorname{tr}J=0\)、\(J^2=-I\)。它不必屬於 subgroup。對 \(x=h\Gamma\)，改取 \(Jh\Gamma\) 得

\[
(JH)^{-1}R^d(JH)=H^{-1}R^{-d}H=P_{\mathcal O}^{-1}.
\tag{21}
\]

而 \(Jr=r^{-1}J\)，所以 J 將每個 r-cycle 送到一個同長、反向的 r-cycle。這才是在固定 base r 表示下的 inverse pairing；不能只因 r 與 \(r^{-1}\) 有相同的 orbit 集合，就把同一 cycle 當成自己的 inverse owner。

依 [上一輪的不自逆證明][roots]，任何正跡 hyperbolic \(P\in\widetilde\Gamma\) 都不與 \(P^{-1}\) subgroup 共軛：若有 subgroup reverser，其 trace 0 使它可寫為
\(\left(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\right)\)，determinant 1 與 \(c\equiv0\pmod {11}\) 強迫 \(a^2\equiv-1\pmod {11}\)，但模 11 的平方剩餘不含 \(-1\)。

因此 J 對 cycles 的作用無 fixed cycle。每個長度 d 的 cycles 必成雙出現；特別是 \(1\cdot11\) 型不可能出現在一個 ambient 自逆的 r 中。這是 conditional reverser 前提加定理 3 的推論，不是本輪已判定某個實際 ambient class 是否自逆。

即使 §6 已使所有理論 family 的類數為偶數，也不能反過來由偶數性推定 family inverse-closed，或在沒有 (20) 的情況下構造 inverse links。原 owner 定義仍是有向 subgroup class；normalizer quotient 或自動除以二均未獲准。

## 8. 有限全覆蓋證書可以要求什麼

對一個**已綁定的** exact ambient primitive R，未來若要實作本定理，至少須逐項驗證：

1. R 的 determinant、正跡、hyperbolicity、ambient primitiveness，以及生成元、quotient 和 input 版本。
2. 十二個 cosets 與 \(\mathcal S\) 的 exact correspondence；每個 successor、各 cycle closure、cycle 內互異性，以及 cycles 的互不重疊和 union 恰為全部十二點。
3. 每個代表 H 的 exact coset binding；(6) 的 matrix replay、subgroup membership、正跡與最小返回證書。第 2 項及引理 1 才給 subgroup primitiveness。
4. 定理 3 的 class partition、定理 4 的遍歷 exponent 與 subgroup root 接口；若使用 inverse links，另綁定 base inverse family 或 exact reverser 與 (21)。
5. frozen rows 到上述 ambient families／subgroup classes 的實際歸屬，以及原有 attachment、separation、coverage、inverse、encoding、G/I/C 和 replay 契約。

有限 cycle partition 可作理論全覆蓋證書，但本輪沒有產生任一實際 R 的這份 partition，也沒有用十二點的個數替代 138-input coverage。相同 cycle length、trace、geodesic length、同調或相同 reduction 都不代表同一 subgroup owner；本定理的注入性使用完整群的 centralizer，而不只使用模 11 的資料。

## 9. 實際動作與保全

已完整讀取當前 `AGENTS.md`、`docs/workflow.md`、ARS 0.1.28 router、academic-paper workflow 與 argument-builder 指令。只讀 [前 finite-coset 筆記][coset] 的 class splitting 段落及已證 root／inverse 接口，並直接核對 round6 原文的 \(X_{\rm geo}/\rho_\epsilon\)、有向 owner、\(k=2y+z\) 與 inverse branch 邊界。新增 finite-field、雙商、degree 與 clock 限定均在文內給出紙面推導。

本輪不需要新外部來源，不重訪 Conrad 的提取限定或任何舊失敗 PDF 通道。只以 `apply_patch` 新增本筆記；其餘操作為檔案定位、讀取、存在性與 SHA-256 檢查。沒有 symbolic／科學計算、矩陣或 coset 枚舉、source API、外部模型、Git 修復、實驗、正式稿 build 或 Route／Stage 變更。

讀取時相關舊檔 SHA-256 為：

- 詞根與 inverse 筆記：`7b100ca34fd524099055692cab7554143eec4adf2b299e5b108a5bad86f6d2f9`；
- ambient normal-form 筆記：`28f6e75b62598c3ff2638dca3458550c06bcb6774b8249e269cdec7499ef692e`；
- finite-coset 筆記：`a5b6344017fb6d04ea999ff1ba311eed87e20ba13a2f455c2930e9d696c3ffd1`；
- round6 原文：`4bc1a960b5527a5d389b5c70e29fa0dc7b3199b93a808dd3f347616dd686d1a3`。

Hashes 只用於來源身分與未修改檢查，不代替科學真實性或既有 input lock。舊筆記、正式稿、code、inputs、experiments/results、receipts、失敗記錄、root 總記錄及既有 PASS／FAIL／BLOCK 邊界均不由本 agent 修改。

[roots]: internal_cyclic_word_roots_and_inverse_class_separation_20260909.md
[coset]: internal_finite_coset_conjugacy_reduction_20260908.md
