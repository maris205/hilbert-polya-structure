# P30 Goal01：真實週期的幾何首變分與逐點共調恆等式

日期：2026-09-09 UTC。依本輪明確的單檔寫入授權，只建立本筆記；不改舊筆記、現稿、程式、資料、凍結輸入、正式回執或 Route／Stage 狀態。本檔採用 bounded Phase 3 紙面推導與 DA 核查，不是實驗或外部獨立認證。

## 1. 固定物件與解析分支

承接[共同幾何全純筆記][joint] §4–5 的固定 code 解析配置及其真實幾何識別。主線本輪已確認此上游接口可供本項推導使用；本檔不回改上游保留的歷史審讀文字。

在該共同鄰域的實參數切片內取當前幾何 \(\zeta_*\)。圓心為 \(C_i\)，半徑為 \(a_i>0\)，基準仍是原等邊三圓盤 \(a_i=a\)、中心間距 \(6a\)。標記、單位歐氏速率、每步一次碰撞及物理時鐘均不變。

令 \(\delta=(\delta C_i,\delta a_i)_{i=1}^3\) 是一個固定實參數方向。以下 \(\delta F\) 指 \(\left.\frac{d}{d\varepsilon}F(\zeta_*+\varepsilon\delta)\right|_{\varepsilon=0}\)，不是有限差分。參數只取足夠小的實 \(\varepsilon\)，使其留在同一幾何鄰域。

固定本原循環盤字 \(w=(i_0,\ldots,i_{m-1})\)，相鄰標記及首尾標記均不等；取雙向週期延拓 x。配置唯一性與移位等變性給 \(q_{j+m}=q_j\)。記

\[
q_j=C_{i_j}+a_{i_j}n_j,\qquad |n_j|=1,
\]

\[
\ell_j=|q_{j+1}-q_j|>0,\qquad
v_j^+=\frac{q_{j+1}-q_j}{\ell_j},\qquad v_j^-=v_{j-1}^+.
\tag{1}
\]

n_j 是障礙圓盤的**外法向**，指向撞球可行域。反射關係及非擦邊性是

\[
v_j^+-v_j^-=2\chi_jn_j,\qquad
\chi_j=-v_j^-\cdot n_j=v_j^+\cdot n_j>0.
\tag{2}
\]

上游 §4 保留跨盤正距離、入／出射符號及嚴格 no-eclipse 間隔，並以端點平方距離公式核對首次飛行。因此此分支仍是真實原時鐘軌道，不只是滿足反射方程的一組形式點。

## 2. 本原物理週期的首變分

**命題。** 固定 w 的物理本原週期 \(L_w=\sum_{j=0}^{m-1}\ell_j\) 滿足

\[
\boxed{
\delta L_w=-2\sum_{j=0}^{m-1}\chi_j
\bigl(n_j\cdot\delta C_{i_j}+\delta a_{i_j}\bigr).}
\tag{3}
\]

**證明。** 所有邊長正，且碰撞配置沿參數解析，所以逐邊微分合法。以模 m 下標重新索引，

\[
\begin{aligned}
\delta L_w
&=\sum_jv_j^+\cdot(\delta q_{j+1}-\delta q_j)\\
&=\sum_j(v_j^--v_j^+)\cdot\delta q_j\\
&=-2\sum_j\chi_jn_j\cdot\delta q_j.
\end{aligned}
\tag{4}
\]

另一方面，微分 \(|n_j|^2=1\) 給 \(n_j\cdot\delta n_j=0\)，而

\[
\delta q_j=\delta C_{i_j}+\delta a_{i_j}n_j+a_{i_j}\delta n_j.
\]

因此

\[
n_j\cdot\delta q_j=n_j\cdot\delta C_{i_j}+\delta a_{i_j},
\tag{5}
\]

代入 (4) 即得 (3)。這裡沒有假設碰撞點固定；其未知切向位移恰被反射法則消去。也沒有對 \(\chi_j\) 再求導，因為它出現在已完成的一階微分式中。

### 2.1 首撞、本原性與計數

上述首撞裕量使整個變分保持相同實際盤字。若本原 w 的物理軌道在較少碰撞後返回同一碰撞後狀態，確定性的前後首撞便迫使無限盤字有較短週期，與本原性矛盾。從初始碰撞狀態更早作連續時間返回，也必先作同一碰撞狀態的返回。因此 \(L_w\) 確為物理本原週期。

- 循環移位只重新排列 (3) 的求和項，不乘 m。
- 若輸入寫成 \(w^k\)，其總遍歷時間及導數分別為 \(kL_w\)、\(k\delta L_w\)，不是新增本原軌道。
- 同一圓盤或同一空間點被多次訪問時，每次碰撞都必須保留；例如[四碰撞見證][third]的 `1213` 兩次 P 具有不同出射速度，不能合併。
- 反向軌道具有同樣的長度及幾何導數，不意味著本公式或 owner 規則需要額外乘 2。本檔不修改方向、循環商或 ledger 約定。

## 3. 剛體運動與共同尺度的獨立檢驗

### 3.1 共同平移

取 \(\delta C_i=u\)、\(\delta a_i=0\)。由 (2) 的有限週期相消，

\[
2\sum_j\chi_jn_j=\sum_j(v_j^+-v_j^-)=0.
\tag{6}
\]

故 (3) 給 \(\delta L_w=0\)。這與把每個碰撞點共同平移 u 而所有邊長不變一致。

### 3.2 共同旋轉

令 \(\Omega^{\mathsf T}=-\Omega\)，取 \(\delta C_i=\Omega C_i\)、\(\delta a_i=0\)。旋轉後的真實同碼配置導數是 \(\delta q_j=\Omega q_j\)。由 \(n_j\cdot\Omega n_j=0\)，

\[
\begin{aligned}
-2\sum_j\chi_j n_j\cdot\Omega C_{i_j}
&=-2\sum_j\chi_j n_j\cdot\Omega q_j\\
&=\sum_jv_j^+\cdot\Omega(q_{j+1}-q_j)\\
&=\sum_j\ell_jv_j^+\cdot\Omega v_j^+=0.
\end{aligned}
\tag{7}
\]

這是零總力矩的有限軌道恆等式，不是假設各次碰撞的旋轉貢獻分別為零。

### 3.3 共同尺度與 Euler 恆等式

取 \(\delta C_i=C_i\)、\(\delta a_i=a_i\)。整個幾何按 \(1+\varepsilon\) 縮放，同碼配置亦如此，故 \(\delta\ell_j=\ell_j\)。直接在 (3) 核對，

\[
\begin{aligned}
-2\sum_j\chi_j(n_j\cdot C_{i_j}+a_{i_j})
&=-2\sum_j\chi_jn_j\cdot q_j\\
&=\sum_jv_j^+\cdot(q_{j+1}-q_j)\\
&=L_w.
\end{aligned}
\tag{8}
\]

所以 \(\boxed{\delta L_w=L_w}\)。這裡同步縮放的是圓心與半徑，不能與下一節固定圓心、只增半徑混淆。

## 4. 固定圓心增加半徑與 1213 精確核對

若 \(\delta C_i=0\)，所有半徑共同增加 \(\delta a_i=r_0>0\)，則

\[
\boxed{\delta L_w=-2r_0\sum_j\chi_j<0.}
\tag{9}
\]

更一般地，各 \(\delta a_i\ge0\) 且至少一個被 w 訪問的盤有嚴格增加，也給嚴格負導數。這些結論局限於保留同碼真實幾何的鄰域，不延伸到圓盤相交、失去 no-eclipse 或擦邊後。

為單獨檢查負號和重複碰撞係數，使用[四碰撞見證][third]。**固定**中心間距 \(d=6a\)，把三盤共同半徑另記為 r，取 r 在 a 附近；此处 a 只是基準尺度，不隨 r 改變。旋轉座標中的中心及盤 1 碰撞點是

\[
C_1=0,\quad C_{2,3}=(\sqrt3d/2,\mp d/2),\quad P(r)=(r,0).
\]

沿與原構造相同的中心射線，令

\[
D_d(r)=\sqrt{d^2-\sqrt3dr+r^2}.
\]

兩外盤仍正入射折返，P 的兩個方向仍相對其法向對稱。每邊長為 \(D_d(r)-r\)，因此

\[
T_4(r)=4\bigl(D_d(r)-r\bigr),
\]

\[
\frac{dT_4}{dr}
=4\left(\frac{2r-\sqrt3d}{2D_d(r)}-1\right)
=-4\left(1+\frac{\sqrt3d/2-r}{D_d(r)}\right).
\tag{10}
\]

而兩次 P 的入射餘弦均為 \((\sqrt3d/2-r)/D_d(r)\)，另兩次為 1；(9) 在 \(r_0=1\) 時正好給 (10)。特別在 \(r=a,d=6a\)，令 \(c=3\sqrt3-1\)、\(D=\sqrt{37-6\sqrt3}\)，得到

\[
\left.\frac{dT_4}{dr}\right|_{r=a}
=-4(1+c/D)<0.
\tag{11}
\]

這是同一真實四碰撞族的第二種精確計算，不是 toy roof、浮點核對或符號程序輸出。

## 5. 任意雙向 code 的逐點變分共調

不再要求 x 週期。對全部雙向盤字，定義

\[
K_\delta(x)=n_0(x)\cdot\delta C_{x_0}+\delta a_{x_0},
\qquad H_\delta(x)=v_0^-(x)\cdot\delta q_0(x).
\tag{12}
\]

當前參數處的 \(n_0,\chi_0,v_0^-\) 均由真實軌道定義。上游的 \(C^\beta\)-值配置解析性、正跨盤距離及固定移位的有界性，保證這些函數和 \(H_\delta\) 有界，並位於相應雙向 Hölder 空間。

由移位等變性，\(H_\delta(\sigma x)=v_0^+(x)\cdot\delta q_1(x)\)。直接微分原單次飛行時間，

\[
\begin{aligned}
\delta\tau(x)
&=v_0^+(x)\cdot(\delta q_1(x)-\delta q_0(x))\\
&=H_\delta(\sigma x)-H_\delta(x)
 +(v_0^-(x)-v_0^+(x))\cdot\delta q_0(x).
\end{aligned}
\]

使用反射和 (5)，得到逐點恆等式

\[
\boxed{\delta\tau
=-2\chi_0K_\delta+H_\delta\circ\sigma-H_\delta.}
\tag{13}
\]

這不是把週期積分關係反向套用某個未證共調定理，而是逐點直接算出的 coboundary；H 的定義及正負號已明列。

因此，對任何雙向 \(\sigma\)-不變概率測度 \(\mu\)，有界性容許積分，不變性使末兩項相消：

\[
\boxed{\int\delta\tau\,d\mu
=-2\int\chi_0K_\delta\,d\mu.}
\tag{14}
\]

此處不要求 \(\mu\) 是 equilibrium、遍歷或有週期原子；也不涉及對 \(\mu\) 求導。將 (13) 沿一條週期相加，則重新得到 (3)。

## 6. 與 pressure 的條件式接口：不是本檔的譜論證明

本節僅記錄如何對接另項 RPF／pressure 首導數證明。幾何主命題 (3)、逐點恆等式 (13) 及不變測度積分式 (14) 都不依賴本節。

假定在上游共同固定 Hölder 空間上，另已證明正一側 roof \(\widehat g_\zeta\) 的實參數 RPF／pressure 接口，採用符號約定

\[
P(s,\zeta)=\log\lambda_{s,\zeta},\qquad
\mathcal L_{s,\zeta}f(x)=\sum_{\sigma^+y=x}
e^{-s\widehat g_\zeta(y)}f(y),
\]

\[
P_s=-\mu^+_{s,\zeta}(\widehat g_\zeta),\qquad
\delta_\zeta P=-s\,\mu^+_{s,\zeta}(\delta\widehat g_\zeta).
\tag{15}
\]

並假定 \(\mu^+\) 有所用的雙向不變自然延拓 \(\overline\mu\)。[共同全純筆記][joint] §7 的全純共調關係

\[
\widehat g_\zeta\circ\pi
=\tau_\zeta-V_\zeta+V_\zeta\circ\sigma
\]

可在相同 Banach 空間中微分，再對當前參數的 \(\overline\mu\) 積分。由其不變性與 (14)，

\[
\mu^+(\delta\widehat g)=\int\delta\tau\,d\overline\mu
=-2\int\chi_0K_\delta\,d\overline\mu,
\qquad
\mu^+(\widehat g)=\int\tau\,d\overline\mu.
\tag{16}
\]

於是**在 (15) 的外部接口成立時**，條件合成為

\[
\boxed{\delta_\zeta P(s,\zeta)
=2s\int\chi_0K_\delta\,d\overline\mu_{s,\zeta}.}
\tag{17}
\]

若另有已證可微的正 pressure 零點 \(P(h(\zeta),\zeta)=0\)，則

\[
\boxed{\delta h
=2h\frac{\int\chi_0K_\delta\,d\overline\mu_{h,\zeta}}
{\int\tau\,d\overline\mu_{h,\zeta}}.}
\tag{18}
\]

分母為正。此條件接口下，固定圓心共同增加半徑給 \(\delta h>0\)；平移、旋轉給零；整體尺度方向由 \(\delta\tau=\tau\) 給 \(\delta h=-h\)。這些後果使用 (15) 及零點接口，不可僅由有限週期首變分直接宣告。

協作分工已對齊外法向、\(H_\delta\) 符號及負權重約定；pressure 單元獨立負責 (15) 與零點解析性。本檔不把未在本輪讀取的該單元證明當作幾何主命題的證據，也不以同伴同意充當獨立科學再現。

## 7. 範圍、DA 核查與實際動作

- 切向位移在 (5) 消失，不代表物理碰撞點不動；首變分的負號來自 \(v^- -v^+=-2\chi n\)，不能改用內法向後仍保留原符號。
- 共同尺度同時移動圓心與半徑，固定圓心增半徑只改後者；(8) 與 (9) 的相反符號沒有矛盾。四碰撞檢驗明確分開基準 a、固定 d 與變動半徑 r。
- 公式作用於每一條保留 code 的物理軌道，沒有宣稱所有週期的相對變化率都相同；只有共同剛體運動／尺度具有已明列的特殊恆等式。
- 本檔沒有證明物理穩定／不穩定切束、切向雙曲性、混合速率、統一高頻譜隙、核性、算子跡、dynamical／Fredholm／quantum determinant 身份或 Hilbert–Pólya 結論。同步更新仍只是幾何配置解析性的上游證明工具。
- ARS bounded Phase 3 與 DA 指引具體影響了首撞／本原性／循環重複計數、首變分負號、尺度與半徑方向的分開核對，以及幾何證明與條件 pressure 合成的分界。
- 本輪以 `rg --files` 定位並完整讀取共同幾何全純筆記，承接已讀的雙向編碼與四碰撞見證。新公式均由上文有限求和、向量微分及不變性直接證明，未援引未核讀的外部定理，沒有網路正文傳送。
- 寫前 `test ! -e` 確認新目標不存在，僅以 `apply_patch` 建立本檔。未運行主程式、科學／符號程序、數值迭代、軌道枚舉、實驗、artifact writer、稿件構建或正式驗證器；舊檔未寫。交接文字檢查不認證數學正確性或形式化完成。

原 Route、Gate、Stage 5／6 停止邊界及歷史失敗紀錄保持不變。

[joint]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_joint_geometry_holomorphy_20260909.md
[third]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_third_period_and_phase_obstruction_20260909.md
