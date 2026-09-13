# P31 Goal 01：非零週期與精確可酉化邊界

日期：2026-09-09。保存主代理已核可的有界紙面證明。
本輪只新增本文件，不改舊筆記、原稿、鎖、receipts、Route 或 Stage；
不執行科學程式、實驗、owner 枚舉或 frozen-input replay。
採 ARS 的有界 claim/proof/counterclaim 組織，不啟動完整研究流程或 Route B。

**結論。** 實際 cuspform 的實週期同態不是零同態，而且某個 hyperbolic
元素具有非零週期。對固定正 rank 的原酉局部系，下述三個平坦表示的精確邊界是
\[
\boxed{
\kappa_w\text{ 可酉化}
\iff\chi_w\text{ 可酉化}
\iff\eta_w\text{ 可酉化}
\iff\varepsilon\operatorname{Re}w=0.}
\tag{1}
\]
固定 \(\varepsilon\ne0\) 時恰為 \(\operatorname{Re}w=0\)；
\(\varepsilon=0\) 時所有 \(w\) 都可酉化。這是同一 classical 參數族的結構
結論，不是「其他自伴模型均不可能」的 no-go。

## 1. 實際輸入、規範與可酉化的意思

沿用 [P26 Frozen dynamical system][clock] 及 [P31 cusp 接口筆記][cusp]：
\[
G=\mathrm{PSL}_2(\mathbb Z),\qquad
\Gamma=\Gamma_0(11)/\{\pm I\},\qquad [G:\Gamma]=12,
\]
\[
f(z)=\eta(z)^2\eta(11z)^2,\qquad
\omega=2\pi i f(z)\,dz,\qquad
\alpha=\operatorname{Re}\omega.
\tag{2}
\]
這裡的 \(f\) 是已固定的非零 weight-two cuspform；本文件承接該輸入，
不重新選形式、不把 \(2\pi i\) 省略，也不以未核算的矩陣或週期值代替它。

固定 \(\varepsilon\in\mathbb R\) 於原正密度區間，保持
\[
\rho_\varepsilon(v)=1+\varepsilon\alpha(v),\qquad
X_\varepsilon=X_{\rm geo}/\rho_\varepsilon,\qquad
\rho_\varepsilon\ge c_0>0.
\tag{3}
\]
固定 \(\nu:\Gamma\to U(m)\)，其中 \(m\ge1\)。令
\[
I(\gamma)=\int_\gamma\alpha,\qquad
\kappa_w(\gamma)=e^{-w\varepsilon I(\gamma)},\qquad
\chi_w=\nu\otimes\kappa_w,\qquad
\eta_w=\operatorname{Ind}_\Gamma^G\chi_w.
\tag{4}
\]
\(I:\Gamma\to\mathbb R\) 是實同態；閉性保證 based-loop 同倫不變，
路徑拼接使積分相加。群與正向 loop 的慣例保持既有接口。

有限維表示「可酉化」指存在一個被全部 holonomy 保持的正定 Hermitian form，
等價於一次固定 similarity 將該表示共軛進 \(U(n)\)。
對 associated flat bundle，這等價於存在與平坦 connection 相容的
**平行正定 Hermitian metric**。這不是任意光滑 Hermitian metric 的存在問題；
後者不要求被 holonomy 保持，不能消除本文的 obstruction。

## 2. 實際群類型與緊化

**引理 1。** \(\Gamma\) 沒有非平凡 elliptic 元素。

**證明。** 假設某 determinant-one 整數代表
\(g=(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})\)，\(11\mid c\)，
在 \(G\) 中非平凡 elliptic。其整數跡只能為 \(t=a+d=0,\pm1\)。
由 \(ad-bc=1\) 得 \(ad\equiv1\pmod{11}\)，故
\[
a^2-ta+1\equiv0\pmod{11},\qquad
(2a-t)^2\equiv t^2-4\pmod{11}.
\tag{5}
\]
右側是 \(7\) 或 \(8\)；模 \(11\) 平方只有 \(0,1,3,4,5,9\)，矛盾。
中心 \(\{\pm I\}\) 已商掉，不在非平凡 elliptic 的討論內。□

因此 \(Y_0(11)=\Gamma\backslash\mathbb H\) 是連通無撓曲面。
其緊化 \(X_0(11)\) 指把全部 cusp 加入後的 Riemann 面。
compactness 可直接由指標 \(12\) 解釋：\(\Gamma\) 的商可用有限份
\(G\) 標準基本域拼成，只有有限個 cusp ends。截去足夠深的 cusp 尾部後
留下緊核心；每個尾部在 cusp 座標中是穿孔圓盤，加入圓盤中心便得到
有限個閉圓盤與緊核心覆蓋的緊面。此處不另計算 genus。

在任一 cusp 的 scaling 座標，設寬度為 \(h>0\)、\(q=e^{2\pi iz/h}\)。
因 \(f\) 是 cuspform，
\[
f_{\rm cusp}(z)=\sum_{n\ge1}a_nq^n,\qquad
\omega=2\pi i f_{\rm cusp}(z)\,dz
=h\sum_{n\ge1}a_nq^{n-1}\,dq.
\tag{6}
\]
故 \(\omega\) 延拓為 \(X_0(11)\) 上的全純微分，特別沒有 cusp residue。
這裡用到了全純延拓；對只有閉性、或可能帶極點的微分，不能照搬以下
緊面調和函數論證。

## 3. 非零實週期同態與 hyperbolic 偵測

**引理 2。** \(I\not\equiv0\)。

**證明。** 反設所有 \(\Gamma\)-loop 的 \(I\) 都為零。
在 \(Y_0(11)\) 固定基點，沿路徑積分 \(\alpha\) 得到單值實函數 \(u\)，
滿足 \(du=\alpha\)。等價地，可先在單連通 \(\mathbb H\) 上取 primitive；
零週期使它 \(\Gamma\)-不變，因而下降。

在每個 cusp 圓盤，(6) 給全純 primitive \(H_c\)，\(dH_c=\omega\)。
穿孔圓盤上 \(d(u-\operatorname{Re}H_c)=0\)，所以
\[
u=\operatorname{Re}H_c+C_c.
\tag{7}
\]
它在 cusp 中心也全純實部式地延拓。曲面其他點的局部 primitive 同樣是
全純函數的實部，故 \(u\) 是整個連通緊面 \(X_0(11)\) 上的調和函數。
最大值原理使 \(u\) 為常數，於是 \(\alpha=0\)。

若局部 \(\omega=F(z)\,dz\)，則
\[
\operatorname{Re}\omega=(\operatorname{Re}F)\,dx
-(\operatorname{Im}F)\,dy.
\tag{8}
\]
其恆為零迫使 \(F=0\)，因此 \(\omega=0\)，與 (2) 的非零形式矛盾。□

這同時證明緊化上的 \(\alpha\) 非 exact：若 \(\alpha=du\)，其局部 primitive
必為全純 primitive 的實部加常數，故全局 \(u\) 緊且調和，只能為常數。
僅僅說「\(\omega\ne0\)」而跳過實部可能 exact 的問題是不足的。

**引理 3。** 存在 hyperbolic \(g\in\Gamma\) 使 \(I(g)\ne0\)。

**證明。** 每個 cusp 周邊 loop 的積分由 (6) 為零。
任一 parabolic 是某個 cusp 周邊生成元的非零整數冪，到群內共軛；
由同態性與共軛不變性，
\[
I(p)=0\qquad(p\in\Gamma\text{ parabolic}).
\tag{9}
\]
由引理 2 選 \(I(g)\ne0\)。它不是 identity，(9) 排除 parabolic，
引理 1 排除 elliptic。因此按 \(\mathrm{PSL}_2(\mathbb R)\) 的元素分類，
它必為 hyperbolic。□

此處只作存在性選取，不聲稱取得具體矩陣、word、owner ID、
非零週期的數值下界或 frozen 138-row 中的定位。非本原的見證同样足夠。

## 4. 原平坦線束與 rank-m 表示的 iff

取引理 3 的 \(g\)，則
\[
|\kappa_w(g)|=\exp(-\varepsilon\operatorname{Re}w\,I(g)).
\tag{10}
\]
若 \(\varepsilon\operatorname{Re}w\ne0\)，右側不等於 \(1\)。
rank-one character 的 similarity 不改變其值，故 \(\kappa_w\) 不可酉化。
對 \(\chi_w(g)\)，原 \(\nu(g)\) 的全部 eigenvalues 模長為 \(1\)，所以
新 eigenvalues 的模長全部為 (10)，仍不等於 \(1\)。任何 similarity
都保留 eigenvalues，因此 \(\chi_w\) 也不可酉化。

反之，若 \(\varepsilon\operatorname{Re}w=0\)，由 \(I(\gamma)\in\mathbb R\)
可知對全部 \(\gamma\in\Gamma\)，\(|\kappa_w(\gamma)|=1\)。
故 \(\kappa_w\) 與 \(\chi_w=\nu\otimes\kappa_w\) 在原標準 metric 下即為酉。
這證明 (1) 的前兩個等價，而不只是在某個框架中「通常非酉」。

## 5. Induction 的真 block 與一般 cycle return

取右陪集代表 \(\Gamma a_i\)，包含 identity 代表 \(a_1=1\)，並用
[cusp 筆記 §3][cusp] 的 row-block 模型
\[
(\eta_w(h))_{ij}=\widetilde\chi_w(a_i h a_j^{-1}),
\tag{11}
\]
其中 \(\widetilde\chi_w\) 在 \(\Gamma\) 外為零。每個 \(h\) 的矩陣是
block-permutation matrix，非零 block 的次序保持此慣例。

因 \(g\in\Gamma\)，右乘 \(g\) 固定陪集 \(\Gamma\)。
它在整個陪集置換中是一條獨立的 1-cycle；對應 block 恰為
\(\chi_w(g)\)，且沒有與其他 cycles 連接的非零 block。
所以 \(\chi_w(g)\) 的 eigenvalues 真正包含在 \(\operatorname{Spec}\eta_w(g)\)。
若 \(\varepsilon\operatorname{Re}w\ne0\)，(10) 提供非單位模 eigenvalue，
從而 \(\eta_w\) 不可酉化。任何正定 Hermitian form 或整體 similarity
都不能移除這個譜障礙。

此處 \(d=1\) 是陪集置換的 cycle 長度，不是聲稱 \(g\) 是 ambient
primitive 元素；\(g\) 可以是 proper power，論證不受影響。

更一般地，對 ambient 元素 \(R\) 的長度 \(d_O\) cycle，return 為
\(P_O=a_iR^{d_O}a_i^{-1}\in\Gamma\)。有限 cycle 的特徵多項式是
\[
\det(\lambda^{d_O}I_m-\chi_w(P_O)).
\tag{12}
\]
因此該 cycle 的 eigenvalues 滿足
\[
\lambda^{d_O}\in e^{-w\varepsilon I(P_O)}
                 \operatorname{Spec}\nu(P_O),\qquad
|\lambda|=\exp\!\left(
-\frac{\varepsilon\operatorname{Re}w\,I(P_O)}{d_O}\right).
\tag{13}
\]
多次 return 的週期按同態性相乘，取 \(d_O\)-次根時必保留 (13) 的分母。
這裡的 cycle 度數與 group element 是否本原是不同概念。
若要從 ambient primitive 選 lift，本原性仍由既有 cycle/primitive-lift
分類判定，不能僅由 (12) 的 eigenvalue 值推認。

若 \(\varepsilon\operatorname{Re}w=0\)，原 \(\chi_w\) 酉；
有限 induction 的 block permutation 與每個 coefficient block 都酉，
故在 \(\bigoplus_{i=1}^{12}\mathbb C^m\) 的標準直和 metric 下，
全部 \(\eta_w(h)\) 也酉。結合必要性，(1) 全部成立。

特別地，\(\varepsilon=0\) 時 \(\kappa_w=1\)，
\(\eta_w=\operatorname{Ind}_\Gamma^G\nu\) 對所有 \(w\) 都酉。
\(m\ge1\) 是必要的正 rank 約定；零維表示不提供上述譜障礙。

## 6. Cusp 局部可酉不等於全群可酉

[cusp 筆記][cusp] 已證每個 ambient parabolic \(p\) 有
\[
\eta_w(p)=D_p(w)\eta_0(p)D_p(w)^{-1},
\tag{14}
\]
其中 \(D_p^{\pm1}\) 整、\(\eta_0(p)\) 酉。故對所有 \(w\)，每個 cusp
monodromy 都可酉化；在 \(\Gamma\) 內更有 \(\chi_w(p)=\nu(p)\)。
但僅由各 \(p\) 分別可酉化，不能推出存在將全群酉化的共同 metric。
其存在性由 (1) 判定；引理 3 給出 \(\varepsilon\operatorname{Re}w\ne0\) 時的障礙。

對固定 \(\varepsilon\ne0\)，原 Euler 右域 \(\operatorname{Re}s>2/c_0\)
上的 \(\eta_s\) 因此一律不可酉化，不只是「通常非酉」。
這不撤銷已證的 non-expanding cusp monodromy 或 classical determinant 延拓。

## 7. 不與同一真實流的 unitary Koopman 混淆

上述結論只針對 (4) 的有限維平坦 holonomy 族。它本身不排除其他
自伴模型，亦不與同一真實時間流的普通 \(L^2\) Koopman 群矛盾。

具體令 \(M=T^1Y_0(11)\)，\(\mu_{\rm geo}\) 為有限且 geodesic-invariant
的 Liouville 測度。實際正時鐘 \(\rho_\varepsilon\) 有界，故
\[
Z_\varepsilon=\int_M\rho_\varepsilon\,d\mu_{\rm geo}\in(0,\infty),
\qquad
d\mu_\varepsilon=Z_\varepsilon^{-1}\rho_\varepsilon\,d\mu_{\rm geo}.
\tag{15}
\]
此處密度是 \(\rho_\varepsilon\)，不是其倒數。對 compactly supported smooth F，
\[
\int_M X_\varepsilon F\,d\mu_\varepsilon
=Z_\varepsilon^{-1}\int_M X_{\rm geo}F\,d\mu_{\rm geo}=0.
\tag{16}
\]
光滑密度的這個 invariance identity 與完整流給 \(\mu_\varepsilon\) 的不變性。
完整性來自原 complete geodesic flow 及 \(dt/du=\rho_\varepsilon\ge c_0>0\)，
所以正、負無窮 geodesic 時間都對應無窮的物理時間。
若真實時間流為 \(\Phi_\varepsilon^t\)，則
\[
(U_tF)(x)=F(\Phi_\varepsilon^t x)
\tag{17}
\]
在 \(L^2(M,\mu_\varepsilon)\) 上是普通 unitary Koopman 群。
它作用於標量觀測函數，不是 (4) 的有限維 coefficient representation。

普通 Koopman 的酉性不等於所需算術譜或全局量子 determinant 身份；
而 (1) 的非可酉化也不獨自排除任何其他自伴實現。
兩者均不能替代 operator domain、所需 trace identity、譜對應或 Route B 義務。
本文件沒有啟動或完成該 Route 的審查。

## 8. 證據範圍與本輪檢查

非零 cuspform、\(2\pi i\) 規範、正 clock 與 index 承接已固定本地輸入。
緊化、調和 primitive、模 \(11\) 判別與 eigenvalue obstruction
均在本文明寫；沒有新造具體矩陣或借第二代理的同意作獨立科學證據。
同模型有界只讀複核另檢查了 induction 的真 block、cycle 冪，
以及 (15) 的 time-change invariant density。

本輪確認新目標原先不存在，只以 apply_patch 新增本文件，然後一次讀回
並檢查行數、公式和本地引用。沒有改其他文件、執行科學程式、
更新正式稿或 Route／Stage 狀態。本文為 AI 輔助內部紙面證明；
ARS 的論證邊界具體用於區分局部 cusp 酉性、全群可酉化和普通 Koopman 酉性。

[clock]: ../../26-level11-newform-time-change/README.md#frozen-dynamical-system
[cusp]: internal_goal01_cusp_monodromy_and_bivariate_selberg_interface_20260909.md
