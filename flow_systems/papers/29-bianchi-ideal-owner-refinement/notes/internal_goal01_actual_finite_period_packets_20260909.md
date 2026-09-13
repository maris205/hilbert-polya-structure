# P29 內部論證：實際 Gaussian 群的有限週期返回包

日期：2026-09-09 UTC。Goal 01 的有界紙面推進；本次只新增本筆記，
不改先前交付的[正返回與一般角色筆記][positive]。
目的在於補掉其中固定弧長模型的「完整同長包有限」假設：
對實際 \(\bar\Gamma(3)\)，這是可證的幾何事實，不必另設解析尾界。
這不提供 owner census、共軛分類算法、權重增長界或全域跡公式。

ARS 的 bounded argument-builder 用於區分：來源支持的有限體積／
尖點分解、下文的具體有限性證明，以及時鐘和權重仍需的限制。

## 1. 實際對象、計數單位與來源依賴

固定
\[
\Gamma(3)=\{A\in SL_2(\mathbb Z[i]):A\equiv I\pmod3\},\qquad
\Gamma=\bar\Gamma(3)\subset PSL_2(\mathbb C),\qquad
M=\Gamma\backslash\mathbb H^3.
\tag{1}
\]
雙曲曲率為 -1，相空間 \(SM\) 上使用單位速測地流，舊時間為弧長。
\(\Gamma\) 的離散、無撓性已由本輪[三交換子筆記，§2][clock]核查。
例如 \(B=I+3D\) 給 \(\operatorname{tr}B\in2+9\mathbb Z[i]\)；
有限階的特徵值迫使跡為 2，進而 B=I。故 M 是流形。

有限指數不依賴枚舉：模 3 約化
\(SL_2(\mathbb Z[i])\to SL_2(\mathbb Z[i]/3\mathbb Z[i])\)
的值域有限、核為 \(\Gamma(3)\)；投影至 PSL 後仍為有限指數。
本篇既不需要證約化滿射，也不聲稱算出確切指數。

外部幾何輸入以作者稿核對如下。

- [Pfaff–Raimbault，arXiv:1503.04785v2，正文 p.2][pr] 明列
  Bianchi 商有限體積、主同餘子群有限指數，以及 \(N(\mathfrak a)\ge9\)
  時的 neat 條件；其商有有限個尖點。本案 \(N((3))=9\) 正適用。
- [Müller–Pfaff，arXiv:1307.4914v1，§2，正文 p.10][mp] 的
  (2.12)–(2.13) 給緊部與有限個精確不交尖點的分解。
  同稿 p.11 的 (2.18)–(2.19) 還明列閉測地線與非橢圓半單共軛類
  對應及有界長度計數上界；下文另外給出本群的紙面有限性證明。

令 \(\mathscr O\) 為**有向本原週期軌道，按沿軌道時間平移取商**。
所討論的返回類是 \((\gamma,r)\)，其中 \(\gamma\in\mathscr O\)、
\(r\in\mathbb Z_{\ge1}\)，弧長為 \(r\ell_\gamma\)。
正反向分別保留；其無向商只是再作有限辨識。
不計同一軌道上的無窮多起點，也不計同一共軛類的無窮多矩陣代表。
非零流軌道的首次正返回給唯一的本原週期及整數重複次數。

**命題 1。** 對每個有限 \(L>0\)，
\[
\mathscr R_L:=
\{(\gamma,r):\gamma\in\mathscr O,\ r\ge1,\ r\ell_\gamma\le L\}
\quad\text{是有限集。}
\tag{2}
\]

## 2. 只截尖點的共同緊核

由上述 cusp decomposition，取足夠高且彼此不交的有限個尖點鄰域
\(U_1,\ldots,U_k\)，使
\[
K=M\setminus\bigcup_{j=1}^k U_j
\tag{3}
\]
是緊的截斷核，包含邊界。每個尖點的提升分支是 horoball；
標準座標中為 \(\{(z,y):y>Y\}\)，商的截面是緊平坦曲面。

此處**只刪尖點，不刪緊的 Margulis tubes**。
若改取單純的 thick part，短閉測地線可能全部位於被刪的 tube，
就不能作下一步的「每條閉測地線交緊核」論證。

每條非平凡閉測地線必與 K 相交。否則其連通像位於某個 \(U_j\)，
將整條週期軌道提升為 \(\mathbb R\to\mathbb H^3\) 的完整測地線，
其像因連通性留在 \(U_j\) 原像的同一個 horoball 分支內。
但上半空間中完整測地線是豎直線，或與邊界正交的半圓；
豎直線在一端高度趨零，半圓在兩端高度趨零，皆不可能整條留在
\(y>Y\)。矛盾。

只需每條閉測地線**至少有一點**交 K；不聲稱所有閉测地線都
完整包含於同一個緊核，亦不需要先給每次 cusp excursion 的深度界。

## 3. 緊核的有限提升選集

令 \(q:\mathbb H^3\to M\) 為覆蓋投影。對每個 \(p\in K\)，選一個
均勻覆蓋的開集 \(U_p\)，及 \(p\in V_p\) 滿足
\(\overline{V_p}\) 緊且包含於 \(U_p\)。由緊性，有限個 \(V_j\)
覆蓋 K。對每個 \(U_j\) 選一個覆蓋反支 \(s_j\)，令
\[
\widetilde K=\bigcup_j s_j(\overline{V_j}),\qquad
o=(0,1),\qquad R=\max_{x\in\widetilde K}d(o,x)<\infty.
\tag{4}
\]
這是有限個緊集的聯集，且 \(q(\widetilde K)\supset K\)。
\(\widetilde K\) 只是覆蓋 K 的**提升選集**，不是一般無界的
\(q^{-1}(K)\)，更不是整個非緊 M 的有界基本域。

給定 \((\gamma,r)\in\mathscr R_L\)，在其與 K 的交點起算，並將
該點提升到 \(x\in\widetilde K\)。按既定方向提升軌道，整次返回
的兩端是 x 與 gx，某個 \(g\in\Gamma\) 保持這條有向測地軸。
由測地線在 \(\mathbb H^3\) 中最短，有
\[
d(x,gx)=r\ell_\gamma\le L,
\]
\[
d(o,go)\le d(o,x)+d(x,gx)+d(gx,go)
\le2R+L.
\tag{5}
\]
這已將每個返回共軛類放入固定的中心位移球，不需先限制重複次數。

## 4. Gaussian 矩陣位移恒等式的展開

對 g 取 Gaussian 整數提升
\(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb Z[i])\)。
把符號換成 -A 不影響以下公式。記
\[
D=|c|^2+|d|^2>0,\quad E=|a|^2+|b|^2,\quad
N=a\overline c+b\overline d.
\tag{6}
\]
上半空間 Möbius 作用在 \(o=(0,1)\) 給
\[
Ao=(w,h),\qquad w=N/D,\qquad h=1/D.
\tag{7}
\]
這來自一般作用的分母
\(|cz+d|^2+|c|^2y^2\)、高度分子 y，與水平分子
\((az+b)\overline{(cz+d)}+a\overline c\,y^2\)，代入 z=0、y=1。
雙曲距離公式因此是
\[
\cosh d(o,Ao)=\frac{|w|^2+h^2+1}{2h}
=\frac{|N|^2+1+D^2}{2D}.
\tag{8}
\]
直接展開平方，交叉項相消，得二維 Lagrange 恒等式
\[
|a\overline c+b\overline d|^2+|ad-bc|^2
=(|a|^2+|b|^2)(|c|^2+|d|^2)=ED.
\tag{9}
\]
由 \(ad-bc=1\)，(8) 化為
\[
\boxed{2\cosh d(o,Ao)=|a|^2+|b|^2+|c|^2+|d|^2.}
\tag{10}
\]
结合 (5)，四個 Gaussian 整數分別满足
\[
|a|,|b|,|c|,|d|\le\sqrt{2\cosh(2R+L)}.
\tag{11}
\]
有界圓盤中只有有限個 Gaussian 整數，故可能的矩陣、從而 PSL 元素
只有有限個。行列式與 level 條件只再縮小這個有限集合。

每個有向閉返回類都有其中的一個代表；同一 loxodromic 元素具有
唯一軸，其有向軸投影與位移長度確定這次閉返回。因此不同返回類
不會因選到同一元素而增加無限重數，(2) 得證。
此亦與 [Müller–Pfaff，(2.19)][mp] 的更強計數界一致；
本證明沒有列出任何代表，也沒有算出 R、cusp 數或共軛類清單。

## 5. 任意有限權重：局部 Radon，但非自動 Laplace

對每個返回給任意**有限數值**權重 \(b_{\gamma,r}\in\mathbb C\)，則
\[
\mu=\sum_{\gamma,r}b_{\gamma,r}\delta_{r\ell_\gamma}
\tag{12}
\]
在每個 \([0,L]\) 只有有限項，總變差有限，於是定義局部有限的
複 Radon 測度；非負權重時為正 Radon 測度。
此處「有限權重」指每項數值有限，不是只准有限多項非零。
沒有沿軌道起點另加一份原子，也不將群共軛代表重複計入。

有界長度有限性不提供無窮遠的振幅控制，故不能自動推出任何
Laplace 收斂半平面。例如對一條固定本原軌道 \(\gamma_1\)，取
\(b_{\gamma_1,r}=\exp((r\ell_{\gamma_1})^2)\)，其他權重取 1。
每项權重有限、局部 Radon 性成立，但任意實 \(\sigma\) 下
\[
\sum_{r\ge1}e^{-\sigma r\ell_{\gamma_1}}
\exp((r\ell_{\gamma_1})^2)
\tag{13}
\]
的項不趨零，故不存在絕對收斂的右半平面。
這是紙面邏輯反例，不是所選自然跡權重的主張。

## 6. 固定弧長的三包與常數時鐘的一般角色推論

沿用 [clock] 的三個本原零同調交換子 \(C_i\)、弧長 \(\ell_i\)，
及其已證算術性質
\[
\forall c>0\quad\exists i\in\{1,2,3\}:c\ell_i\notin
V_p:=\operatorname{span}_{\mathbb Q}\{\log p:p\text{ 為素數}\}.
\tag{14}
\]
沿用 [positive] 的完整自由同調角色 torus \(\Theta\)，先固定
嚴格正且有限的幾何振幅 \(a_{\gamma,r}\)，twist 只乘角色。
由命題 1，實際完整包
\[
\mathcal J_i=\{(\gamma,r):r\ell_\gamma=\ell_i\},\qquad
F_i(\theta)=\sum_{\mathcal J_i}
a_{\gamma,r}e^{i\langle\theta,r[\gamma]\rangle}
\tag{15}
\]
必定有限，故 \(F_i\) 是三角多項式，不需要另加解析尾界。
其零 Fourier 係數至少有正的 \(C_i\) 返回項，所以非恆零。
非零三角多項式的零集閉、Haar 零測且無內點；可按變數數目歸納，
以一維多項式的有限零點及 Fubini 證明，見 [positive，§5][positive]。
因此
\[
G=\Theta\setminus\bigcup_{i=1}^3\{F_i=0\}
\tag{16}
\]
是同一個開稠密、滿 Haar 測度集合。

定義常數時鐘為**同一固定帶權測度的推送**：
\[
\mu_{c,\theta}=(t\mapsto ct)_*
\sum_{\gamma,r}a_{\gamma,r}e^{i\langle\theta,r[\gamma]\rangle}
\delta_{r\ell_\gamma}.
\tag{17}
\]
則對全部 \(\theta\in G\) 及全部 \(c>0\)，(14) 選出的 i 滿足
\(\mu_{c,\theta}(\{c\ell_i\})=F_i(\theta)\ne0\)，該時間不屬於
\(\mathcal P_p=\{k\log p:k\in\mathbb Z_{\ge1},\ p\text{ 為素數}\}\)。
故不可能純素冪支撐。
G 不依賴 c，因為推送不改包或振幅；沒有取不可數個零集的聯集。
每包共同非零縮放也不改零集，但逐軌依 c 重定振幅不自動包括。
目標 Laplace 等式仍需共同指數總變差界；唯一性及零軌道修正沿用
[positive，§2–§3][positive]，不能由本次有限性論證免除。

## 7. 有全局下界的換時：僅作條件擴張

若 \(ds=\rho\,dt\)，\(\rho\) 為足夠正則的正函數且有明確全局下界
\(\rho\ge m_0>0\)，則時間變換保留有向軌道及整數重複，並有
\[
T_\rho(\gamma^r)=\int_0^{r\ell_\gamma}\rho(\phi_t x)\,dt
\ge m_0r\ell_\gamma.
\tag{18}
\]
所以新時間 \(\le L\) 的返回類包含於舊弧長 \(\le L/m_0\) 的有限集，
每個新完整同時包也有限。單有 \(\rho>0\) 在非緊 \(SM\) 上不能
推出這個全局下界；本篇不把正性偷換成一致正性。

若另外 \(\rho=c+Xu+\alpha(X)\)，u 全局單值、\(\alpha\) 閉，
三個零同調見證仍有 \(T_\rho(C_i)=c\ell_i\)，正性迫使 c>0。
對**每個固定**滿足下界的 \(\rho\)，固定其正振幅後，可以用新的
有限碰撞包證一般角色障礙。但新的包與振幅可能依賴 \(\rho\)，
因此只得到「每個 \(\rho\) 各有一個滿測度集合 \(G_\rho\)」，
不推出單一角色集合對全部此類 \(\rho\) 同時有效。
有限包也不消除 [positive，§6][positive] 的這項量詞與振幅邊界。

## 8. 來源使用、證據限制與實際動作

[pr] 讀到的作者稿為 v2，扉頁標示 2015-05-06；只援用正文 p.2
的群、有限體積、level 與尖點陳述，不使用其 torsion 增長結果。
[mp] 讀到的作者稿為 v1，扉頁標示 2013-07-18；核對正文 pp.10–11
的 (2.12)–(2.19)，不是僅凭題名或摘要。頁碼是 PDF 正文印頁。
這些公開來源支持標準幾何背景；本案 (5)–(11) 是展開的紙面推導。

本篇補的是實際有限性，不是有效幾何界、枚舉完成、primitive-root
或共軛判定程序，更不是完整 Gate Q、Route、Stage 或跡公式。
例外阿貝爾角色、任意複權重、非阿貝爾 holonomy 與全局算子問題
均不由此概括否定。
實際僅讀取適用 ARS／工作流及相關材料、普通瀏覽核對一手作者稿，
以 apply_patch 新增本檔並作只讀回讀與靜態檢查；未外傳內部筆記，
未執行科學／符號程序、census、枚舉、實驗、producer 或 build。
先前交付筆記、歷史失敗證據、舊鎖與所有 Route／Stage 狀態不改。
本檔為 AI 輔助內部論證，主線仍需整合核驗，不是正式證明認證。

[clock]: internal_goal01_null_homology_clock_obstruction_20260909.md
[positive]: internal_goal01_positive_trace_and_generic_abelian_twists_20260909.md
[pr]: https://arxiv.org/pdf/1503.04785v2
[mp]: https://arxiv.org/pdf/1307.4914v1
