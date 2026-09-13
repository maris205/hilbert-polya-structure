# P29 內部論證：formal closed-orbit measure 的自然橫向權重與 Laplace 界

日期：2026-09-09 UTC。Goal 01 的有界紙面推進；只新增本筆記。

**摘要。** 對實際 Gaussian level-(3) 雙曲三流形的單位速測地流，
以完整四維橫向返回分母定義
\(a_{\gamma,r}=\ell_\gamma/|\det(I-P_\gamma^r)|\)。
下文證明每项權重嚴格為正，包含旋轉 holonomy 的分母有一致下界，
並由實際閉測地線計數得到總變差 \(O((1+L)^2)\) 與
\(\operatorname{Re}s>0\) 的共同 Laplace 絕對收斂域。
這是**依閉軌道係數定義的 formal closed-orbit measure 定理**，
不是已建立的非緊 flat-trace 分佈、傳播子跡公式或譜側恆等式。

ARS 的來源核對與 bounded argument-builder 用於分開一手文獻輸入、
Jacobi／算術／求和推導，以及不能隨收斂性一併宣告的算子結論。

## 1. 實際對象、權重與主定理

固定
\[
\Gamma(3)=\{B\in SL_2(\mathbb Z[i]):B\equiv I\pmod3\},\qquad
M=\bar\Gamma(3)\backslash\mathbb H^3,
\tag{1}
\]
曲率為 -1，\(S=SM\)，\(\phi_t\) 為單位速測地流。
本群的離散、無撓、有限體積與有界長返回包有限性沿用
[實際有限週期包筆記][packets]，不改其證據或計數單位。

\(\mathscr O\) 是有向本原週期軌道，按沿軌道時間平移取商；
\(\ell_\gamma>0\) 是本原弧長，\(r\ge1\) 是整數重複次數，
\(T_{\gamma,r}=r\ell_\gamma\)。不另計起點、矩陣共軛代表或負的 r。
\(P_\gamma=d\phi_{\ell_\gamma}|_{E^s\oplus E^u}\) 是完整四維
橫向返回，流方向不在此行列式中。

對完整自由同調角色 \(\chi_\theta\in\Theta\)，定義
\[
a_{\gamma,r}:=\frac{\ell_\gamma}{D_{\gamma,r}},\qquad
D_{\gamma,r}:=|\det(I-P_\gamma^r)|,
\]
\[
\mu^{\rm orb}_\theta:=\sum_{\gamma\in\mathscr O}\sum_{r\ge1}
a_{\gamma,r}\chi_\theta(r[\gamma])\delta_{T_{\gamma,r}}.
\tag{2}
\]
\(\theta=0\) 表示平凡角色。角色 torus 及相空間同調接口沿用
[正返回與角色筆記，§4][positive]；不在本篇計算其自由秩。

**定理（formal closed-orbit measure 的自然橫向權重界）。**
式 (2) 的每項 \(a_{\gamma,r}\) 嚴格為正且有限，並存在僅依赖本固定
流形的 \(A>0\)，對所有 unitary 角色 \(\theta\)、\(L\ge0\) 及
\(\sigma>0\) 同時有
\[
|\mu^{\rm orb}_\theta|([0,L])
\le\mu^{\rm orb}_0([0,L])
\le\frac A2(L+1)(L+2),
\tag{3}
\]
\[
\int_0^\infty e^{-\sigma t}\,d|\mu^{\rm orb}_\theta|(t)
\le\frac A{(1-e^{-\sigma})^2}<\infty.
\tag{4}
\]
所以這些局部複 Radon 測度的 Laplace 級數在
\(\operatorname{Re}s>0\) 全純，並在其緊子集上對全部 \(\theta\)
有共同絕對收斂控制。正返回支撐與一般角色障礙因此可在此明定
formal 測度模型中使用，不再另設其自然振幅的指數尾界。

## 2. 全局 systole：存在性及本群的可寫下界

先作不依賴有效常數的論證。取[三交換子筆記][clock]中一條已知
閉軌道，長度 \(\ell_*>0\)。[packets] 已證
\(\{(\gamma,r):r\ell_\gamma\le\ell_*\}\) 非空且有限，
所以它的正長度有正最小值；其餘長度大於 \(\ell_*\)。
這給全局閉軌道 systole \(s_0>0\)，不是非緊流形的全局
injectivity radius 下界。尖點仍使後者可能趨零。

本群另外有直接算術下界。若 \(B=I+3D\in\Gamma(3)\)，
\(\det B=1\) 給
\[
\tau:=\operatorname{tr}B=2-9\det D\in2+9\mathbb Z[i].
\tag{5}
\]
loxodromic B 不可能有 \(\tau=2\)，故
\(|\tau|\ge9-2=7\)。若其擴張特徵值為 \(\lambda\)，平移長度 T
滿足 \(|\lambda|=e^{T/2}\)，從而
\[
7\le|\lambda+\lambda^{-1}|
\le e^{T/2}+e^{-T/2}=2\cosh(T/2).
\]
因此可統一取
\[
\delta:=2\operatorname{arcosh}(7/2)>0,\qquad
T_{\gamma,r}\ge\ell_\gamma\ge\delta.
\tag{6}
\]
不聲稱 \(\delta\) 是精確 systole 或有達到此值的矩陣；
這只是作用於每個實際 loxodromic 元素的可證下界。

## 3. Jacobi 資料、穩定／不穩定束與旋轉 holonomy

在一條本原有向閉測地線上，令 \(W=\dot\gamma(0)^\perp\)，
\(H:W\to W\) 為法叢平行移動一次閉路後的返回。
\(M\) 定向且速度返回，故 \(H\in SO(2)\)，寫 \(H=R_\vartheta\)。
這裡 \(\vartheta\) 是法平面的 SO(2) 旋轉角。若 SL 提升的擴張
特徵值寫成 \(e^{\ell_\gamma/2+i\beta}\)，則
\(\vartheta=\pm2\beta\pmod{2\pi}\)，正負取決於 holonomy 約定。

横向測地線變分由法向 Jacobi 資料 \((u,v)\in W\oplus W\) 表示。
Jacobi 方程
\(D_t^2J+R(J,\dot\gamma)\dot\gamma=0\) 在曲率 -1 化為
\(D_t^2J-J=0\)。在平行標架下直接解得
\[
\binom{J(t)}{D_tJ(t)}=
\begin{pmatrix}\cosh t\,I&\sinh t\,I\\
\sinh t\,I&\cosh t\,I\end{pmatrix}\binom uv.
\tag{7}
\]
把 \(t=\ell_\gamma\) 的端點資料用閉路 holonomy 辨識回起點，得到
\[
P_\gamma=
\begin{pmatrix}H&0\\0&H\end{pmatrix}
\begin{pmatrix}\cosh\ell_\gamma\,I&\sinh\ell_\gamma\,I\\
\sinh\ell_\gamma\,I&\cosh\ell_\gamma\,I\end{pmatrix}.
\tag{8}
\]
因此 \(E^s=\{(u,-u)\}\)、\(E^u=\{(u,u)\}\)，其返回分別為
\(e^{-\ell_\gamma}H\)、\(e^{\ell_\gamma}H\)。複化後四個特徵值是
\[
e^{-\ell_\gamma\pm i\vartheta},\qquad
e^{\ell_\gamma\pm i\vartheta}.
\tag{9}
\]
若改以 deck transformation 的旋轉方向定義角度，可把
\(\vartheta\) 換成 \(-\vartheta\)；以下餘弦與分母不變。

令 \(T=r\ell_\gamma\)、\(\varphi=r\vartheta\)。直接相乘得
\[
\begin{aligned}
D_{\gamma,r}
&=(1-2e^{-T}\cos\varphi+e^{-2T})
  (1-2e^T\cos\varphi+e^{2T})\\
&=4(\cosh T-\cos\varphi)^2\\
&=e^{2T}|1-e^{-T+i\varphi}|^4.
\end{aligned}
\tag{10}
\]
\(T>0\) 時嚴格為正。由 (6)，
\[
D_{\gamma,r}\ge e^{2T}(1-e^{-\delta})^4,\qquad
0<a_{\gamma,r}\le C_\delta\ell_\gamma e^{-2T}
\le C_\delta T e^{-2T},
\quad C_\delta=(1-e^{-\delta})^{-4}.
\tag{11}
\]

完整四維行列式不能改成其平方根；後者只有 \(e^T\) 階，會改變
尾界。流方向若誤放入行列式則出現特徵值 1，也不是本定义。
若使用反時間返回 \(P_\gamma^{-1}\)，因 \(\det P_\gamma=1\) 且
橫向維數為 4，\(\det(I-P_\gamma^{-r})=\det(I-P_\gamma^r)\)。

## 4. 實際計數：重複已包括，起點不再乘一份

本篇外部計數輸入是 [Müller–Pfaff，作者稿 v1，正文 pp.10–11][mp]：
(2.18) 後以全部非橢圓半單元素的共軛類對應閉測地線，
(2.19) 給 \(\#\{c:\ell(c)\le L\}\le C_Me^{2nL}\)。
這裡 \(\dim M=2n+1=3\)，故指數是 2。它不是只計本原類的界；
\([g^r]\) 已包含，不能再把結果逐一乘上 \(\lfloor L/s_0\rfloor\)。
同頁 (2.20) 亦明列 systole 的正性。

在本篇有向正返回約定下，適當放大常數後有
\[
N(L):=\#\{(\gamma,r):\gamma\in\mathscr O,\ r\ge1,
r\ell_\gamma\le L\}\le C e^{2L}.
\tag{12}
\]
source 的群共軛類對應保留返回方向；即使採無向閉測地線約定，
提升為兩個方向也只需把 C 放大至兩倍。空間正反向是兩條不同的
有向流軌道，不等於把同一軌道上的無窮多起點加入計數。

每個固定本原軌道在 \(T\le L\) 下只有
\(1\le r\le\lfloor L/\ell_\gamma\rfloor\)；分子仍是
本原週期 \(\ell_\gamma\)，不是重複週期 \(r\ell_\gamma\)。
這與 scalar flow-flat 的標準局部周期係數形式一致，參见
[Dyatlov–Zworski，v4，正文 p.3 (1.5)、p.6 (2.4) 的 k=0][dz]。
該來源 p.1、p.5 的基本空間假設為緊流形；这里只核對係數約定，
不把其緊空間跡構造移植為本案的既成定理。

## 5. 分殼總變差與共同 Laplace 域

由實際有限包，(2) 首先在每個緊時間區間定義局部有限測度。
角色模長為 1，即使同時原子合併後發生消去，仍有
\(|\mu^{\rm orb}_\theta|\le\mu^{\rm orb}_0\)。

對 \(n=0,1,2,\ldots\)，令 \(I_n=(n,n+1]\)。由 (11)–(12)，
\[
\begin{aligned}
\mu^{\rm orb}_0(I_n)
&\le C_\delta(n+1)e^{-2n}N(n+1)\\
&\le C_\delta C e^2(n+1)=A(n+1),\qquad
A:=C_\delta C e^2.
\end{aligned}
\tag{13}
\]
把 \(n\le\lfloor L\rfloor\) 的界相加即得 (3)。這比單一指數界
更強；例如每個 \(\varepsilon>0\) 均有明確的粗界
\[
|\mu^{\rm orb}_\theta|([0,L])
\le2A(1+\varepsilon^{-1})^2e^{\varepsilon L}.
\tag{14}
\]
再按同一分殼，對每個 \(\sigma>0\)，
\[
\int e^{-\sigma t}\,d|\mu^{\rm orb}_\theta|(t)
\le A\sum_{n=0}^\infty(n+1)e^{-\sigma n}
=\frac A{(1-e^{-\sigma})^2}.
\tag{15}
\]
所以在 \(\operatorname{Re}s\ge\sigma>0\) 上有共同可和優函數；
Weierstrass 正常收斂給 Laplace 級數的全純性。這只是充分右域：
本篇不宣稱 \(\operatorname{Re}s=0\) 為精確收斂邊界，也不推出
全平面延拓、共振展開或行列式恒等。

## 6. 常數時鐘的推送與既有一般角色集合

仍嚴格使用**固定舊振幅再推送**的模型
\[
\mu^{\rm orb}_{c,\theta}:=(t\mapsto ct)_*\mu^{\rm orb}_\theta,
\qquad c>0.
\tag{16}
\]
對每個 \(c>0\)，其共同收斂域仍為 \(\operatorname{Re}s>0\)，且
\[
\int e^{-\sigma t}\,d|\mu^{\rm orb}_{c,\theta}|(t)
\le\frac A{(1-e^{-c\sigma})^2}.
\tag{17}
\]
右域可同時選給全部 c，但估計常數不是在 \(c\downarrow0\) 時
一致有界；若 \(c\ge c_0>0\) 則有共同控制。

現在把 (2) 的自然正振幅代入 [packets，§6][packets] 的三個完整包。
有限包的三角多項式有正零 Fourier 係數，得到同一個開稠密、
滿 Haar 測度 \(G\subset\Theta\)，使
\[
\forall\theta\in G\quad\forall c>0:\quad
\mu^{\rm orb}_{c,\theta}\text{ 不集中於 }
\{k\log p:k\in\mathbb Z_{\ge1},\ p\text{ 為有理素數}\}.
\tag{18}
\]
G 依賴本次明定自然權重，但不依賴 c；沒有跨不可數 c 取例外零集
的聯集。若比較目標 \(\nu\) 滿足
\(\int e^{-\sigma_\nu t}d|\nu|<\infty\)，則共同右域可取
\(\operatorname{Re}s>\max\{0,\sigma_\nu\}\)，從而能用
[positive，§2–§3][positive] 的 Laplace 唯一性與指定零項邊界。

式 (16) 不自動等於重新建立的換時算子之 flat trace。
例如 \(\psi_s=\phi_{s/c}\) 的本原周期為 \(c\ell_\gamma\)，若採
同一 scalar 周期係數規則，其形式分子將是 \(c\ell_\gamma\)，
而非本篇推送保留的 \(\ell_\gamma\)。这在係數層面提示一個整體 c
因子，但不證明任何換時傳播子的跡存在。一般 \(\rho\)、逐軌重定
振幅、束值跡或其他 determinant conventions 仍需各自重新核查。

## 7. 任意有限權重的反例與未完成的非緊跡接口

以上收斂性依賴 (10)–(11) 的自然振幅，不是任意有限權重的結論。
例如只在一條已知本原軌道 \(\gamma_*\) 的重複返回上指定
\(b_{\gamma_*,r}=e^{(r\ell_{\gamma_*})^2}\)，其餘取 0。
這仍是局部正 Radon 測度；但任意實 \(\sigma\) 下，項
\(e^{(r\ell_{\gamma_*})^2-\sigma r\ell_{\gamma_*}}\) 不趨零，
故不存在 Laplace 絕對收斂右半平面。反例不是自然權重 (2)。

本篇已定義並控制的是一個閉軌道原子測度。要把它辨認成實際
非緊流上某個 \(\operatorname{tr}^{\flat}U(t)\)，還必須指定
傳播子、作用束／密度及核，核查對角拉回的 wavefront 條件，
並說明非緊基底上推送、切斷或正則化的合法性與約定。
本次沒有完成這些步驟，也沒有證明譜側、連續譜／尖點項、
整函數修正或 global determinant 等式。

因此 (18) 是指定 formal 軌道測度族的障礙，不是所有 trace models、
非阿貝爾 twists、例外阿貝爾角色或 Route／Stage 的全面否定。

## 8. 來源定位、證據限制與實際動作

一手作者稿在本輪普通瀏覽中實際讀到：

- Müller–Pfaff，*The analytic torsion and its asymptotic behaviour for
  sequences of hyperbolic manifolds of finite volume*，arXiv:1307.4914v1，
  正文 pp.10–11 的 (2.18)–(2.20)。只取共軛類計數與 systole 背景。
- Dyatlov–Zworski，*Dynamical zeta functions for Anosov flows via microlocal
  analysis*，arXiv:1306.4203v4，正文 pp.1、3、5–6，尤其 (1.5)、(2.4)。
  只取 scalar 局部係數約定及其緊空間假設，不援用非緊跡結論。

版本身份另核對 arXiv 版本頁；頁碼指作者稿印頁。
Müller–Pfaff 的兩張瀏覽截圖请求回傳 internal error，故本次頁碼
定位依已讀 PDF 文字與式號，不聲稱成功完成截图或本地 PDF 結構檢查。
Jacobi 分母、(5)–(6) 的算術下界與 (13)–(17) 的估計是本篇展開
的紙面推導，不聲稱文獻逐字包含本篇定理。另一次同模型代理的
分母覆核只作校對，不列為獨立科學證據。

本篇為 AI 輔助內部論證，不是正式稿或證明認證。實際僅讀取適用
工作流、既有筆記及公開作者稿，以 apply_patch 新增本檔並作一次
靜態回讀／格式檢查；未執行科學、符號、census、枚舉、producer、
實驗或 build。舊筆記、鎖、失敗證據及所有 Route／Stage 狀態不改。

[packets]: internal_goal01_actual_finite_period_packets_20260909.md
[positive]: internal_goal01_positive_trace_and_generic_abelian_twists_20260909.md
[clock]: internal_goal01_null_homology_clock_obstruction_20260909.md
[mp]: https://arxiv.org/pdf/1307.4914v1
[dz]: https://arxiv.org/pdf/1306.4203v4
