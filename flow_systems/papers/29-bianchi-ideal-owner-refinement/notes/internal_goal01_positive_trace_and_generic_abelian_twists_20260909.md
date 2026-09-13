# P29 內部論證：正返回原子與一般自由同調角色

日期：2026-09-09 UTC。Goal 01 的有界紙面推進；唯一新增本筆記。
結論是指定測度／角色模型的條件障礙，不是任意帶權跡、算子或
全局行列式的否定，也不更改 Route、Stage、舊鎖或既有 FAIL／BLOCK。

ARS 的 bounded argument-builder 用於分開：實際群見證、測度唯一性、
一般角色的例外集，以及尚不能交換的時鐘／角色量詞。

## 1. 群、三條實際閉返回及算術輸入

沿用完整 Gaussian level-(3) 群
\(\Gamma(3)=\{A\in SL_2(\mathbb Z[i]):A\equiv I\pmod3\}\)
在 PSL 中的像 \(\bar\Gamma\)，令 \(M=\bar\Gamma\backslash\mathbb H^3\)。
時鐘先固定為曲率 -1 的單位速弧長，X 表示相空間上的單位速測地流生成元。
本輪同伴筆記[零同調時鐘障礙][clock]提供全群本原性與相空間同調接口；
本篇已讀回該新筆記並逐式比較其三見證；以下只需矩陣、長度與零同調資料。
不把新三見證說成[舊單位長度筆記][units]已經證過的結論。

令
\[
P=\begin{pmatrix}1&3\\0&1\end{pmatrix},\quad
Q_n=\begin{pmatrix}1&0\\3n&1\end{pmatrix},\quad
C_n=[P,Q_n]=
\begin{pmatrix}1+9n+81n^2&-27n\\27n^2&1-9n\end{pmatrix}.
\tag{1}
\]
兩生成元皆在 \(\Gamma(3)\)，所以 \(C_n\) 是實際群交換子，
在群的整係數阿貝爾化中為零。\(n=1,2,3\) 的跡為 83、326、731，
皆大於 2；擴張特徵值與返回長度為
\[
\lambda_1=(83+9\sqrt{85})/2,\quad
\lambda_2=163+18\sqrt{82},\quad
\lambda_3=(731+27\sqrt{733})/2,\qquad
\ell_i=2\log\lambda_i>0.
\tag{2}
\]
它們滿足 \(\lambda_i^2-T_i\lambda_i+1=0\)，是正實代數單位。

平方類 85、82、733 獨立：乘積為平方時，先由 5 與 2 的賦值
分別排除前兩個非零指數，再由 \(27^2<733<28^2\) 排除第三個。
因此多二次域存在獨立翻轉每個平方根的自同構，將相應
\(\lambda_i\) 變為 \(\lambda_i^{-1}\)，固定另外兩個。
若清分母後 \(\prod_i\lambda_i^{n_i}=1\)，以每個翻轉比較，得到
\(\lambda_i^{2n_i}=1\)，故 \(n_i=0\)。因此三個 \(\ell_i\)
在 \(\mathbb Q\) 上線性獨立。

令 \(V_p=\operatorname{span}_{\mathbb Q}\{\log p:p\text{ 為有理素數}\}\)，
只含有限線性組合，\(\mathcal P_p=\{k\log p:k\ge1\}\subset V_p\)。有
\[
\forall c>0\quad\exists i\in\{1,2,3\}:c\ell_i\notin V_p.
\tag{H}
\]
若 \(c\) 為有理數，任一反例等式清分母後令一個非平凡正實
代數單位的整數冪等於正有理數；正有理單位只能為 1，矛盾。
若 \(c\) 無理且三個 \(c\ell_i\) 皆在 \(V_p\)，則
\(e^{\ell_i}\) 與 \(e^{c\ell_i}\) 全為代數數；
\(\ell_1,\ell_2,\ell_3\) 與 \(1,c\) 的兩組有理獨立性
違反六指數定理。所用標準定理的矩陣表述見
[Waldschmidt 的期刊原文摘要][six]，不是四指數猜想。

本篇的測度推理實際只需三個**正權閉返回**。
即使未援用上游本原性，若 \(C_i=D_i^{r_i}\) 是本原軌道的重複，
只要該重複具有正權，它在以下論證仍是合法見證；
\(r_i[D_i]=[C_i]=0\) 在自由同調中仍給零頻率。
本原性不可由「是交換子」推出，亦不以有限找根未見代替證明。

## 2. 正 Radon 返回測度的原子障礙

用有向本原軌道 \(\gamma\) 與 \(m\ge1\) 作索引，固定非負幾何權重
\(a_{\gamma,m}\)，且三個見證返回的權重嚴格為正。設
\[
\mu_0=\sum_{\gamma,m}a_{\gamma,m}\delta_{m\ell_\gamma}
\quad\text{為正 Radon 測度},\qquad
\int e^{-\sigma_0t}\,d\mu_0(t)<\infty
\tag{3}
\]
對某個實 \(\sigma_0\) 成立。局部有限可容許同長包有無限項，
但每個原子的總質量必須有限。常數時鐘嚴格定義為固定測度的推送
\(\mu_c=(t\mapsto ct)_*\mu_0\)，不另外逐軌改權。

**命題 1。** 對任何 \(c>0\)，\(\mu_c\) 不等於任何集中於
\(\mathcal P_p\) 的正測度 \(\nu\)。若 \(\nu\) 的 Laplace 變換
在共同右半平面收斂，兩個變換亦不可能在該半平面恆等。

證明。由 (H) 選 \(t_i=c\ell_i\notin\mathcal P_p\)。則
\[
\mu_c(\{t_i\})=
\sum_{m\ell_\gamma=\ell_i}a_{\gamma,m}>0,
\qquad \nu(\{t_i\})=0.
\tag{4}
\]
所有本原／重複同長碰撞只相加，不會消去見證。
這是單點質量比較；不把稠密空間 \(V_p\) 的拓撲閉包當離散支撐。
負的方向反轉以 \(|c|\) 計物理返回時間，故亦由此涵蓋。

Laplace 唯一性的紙面證明如下，後面亦可用於受控的複測度。
此處明確要求某個 \(\sigma\) 有
\(\int e^{-\sigma t}(d|\mu|+d|\nu|)<\infty\)，不是僅有條件收斂。
若 \(\mathcal L\mu(s)=\mathcal L\nu(s)\) 在共同右半平面成立，
可加大 \(\sigma\) 使其也位於該等式半平面內，再
令 \(\eta=e^{-\sigma t}(\mu-\nu)\) 為有限複測度。
把它經 \(u=e^{-t}\) 推至 \((0,1]\)，並在 0 賦質量 0。
變換相等給全部正整數矩為零；因所選 \(\sigma\) 已位於等式半平面，
零階矩直接等於 \(\mathcal L\mu(\sigma)-\mathcal L\nu(\sigma)=0\)。
多項式在 \(C[0,1]\) 稠密，故該測度、從而 \(\eta\) 為零，
與 (4) 矛盾。正測度標準版本亦見
[Schilling–Song–Vondraček，命題 1.2][laplace]。
等式若只在共同全純域的一個非空開集成立，恆等定理給同一結論。

## 3. 零軌道修正：可排除與不可偷渡的類

允許兩邊差額有
\[
h(t)\,dt+\sum_{j=0}^{N}d_j\delta_0^{(j)},\qquad
h\in L^1_{\rm loc}([0,\infty)),\quad
\int e^{-\sigma t}|h(t)|\,dt<\infty.
\tag{5}
\]
在時間端，前項沒有正時間原子，後項僅支撐於 0，不能抵消 (4)。
採用 \(\mathcal L\delta_0^{(j)}(s)=s^j\) 的分佈約定；
在變換端，(5) 為 \(\mathcal Lh(s)+\sum_jd_js^j\)。
由於返回／素冪測度在 0 無原子，各積分沿實 \(s\to+\infty\)
趨於 0；故擬議等式中的多項式也趨零，必須恆為零。
剩下有限傾斜複測度仍適用上一節唯一性與原子比較。

若零項在 0 不可積而需有限部分、分佈延拓或其他正則化，本篇
沒有自動包含它；必須先指定可唯一反演的分佈類與修正常規。
「變換端是解析／整函數」不是足夠限制：\(e^{-st_i}\) 本身就是
一個正時間原子的整函數變換。也不排除只在離散譜點取樣的等式。

## 4. 完整自由同調角色與完整同長包

令 \(H=H_1(\bar\Gamma;\mathbb Z)/\mathrm{tors}\cong\mathbb Z^b\)，
使用其完整自由角色 torus \(\Theta=\operatorname{Hom}(H,S^1)\cong\mathbb T^b\)
及歸一化 Haar 測度；有限自由秩是本命題明列的框架，本篇不計算 b。
這是平凡 torsion 角色的連通分量，不聲稱覆蓋所有離散 torsion 扭曲。
若使用相空間 \(T^1M\) 的自由同調，須沿用上游的 \(S^2\)-纖維接口。

先固定基底權重且全部 \(a_{\gamma,m}>0\)，twist 僅取
\(\chi_\theta(m[\gamma])=e^{i\langle\theta,m[\gamma]\rangle}\)：
\[
\mu_\theta=
\sum_{\gamma,m}a_{\gamma,m}e^{i\langle\theta,m[\gamma]\rangle}
\delta_{m\ell_\gamma},\qquad
\mu_{c,\theta}=(t\mapsto ct)_*\mu_\theta.
\tag{6}
\]
由 (3)，總變差受 \(\mu_0\) 控制，局部及 Laplace 絕對收斂均合法。
群共軛不改同調；逆向則改號，因此不能直接給無向 owner 單配
\(e^{i\langle\theta,[\gamma]\rangle}\)。若原索引無向，須明確提升為
兩個有向項，或使用其對稱和／平均；此時以下正零頻率推理仍成立。

定義**所有**同長返回的包，不能只算三個矩陣本身：
\[
\mathcal J_i=\{(\gamma,m):m\ell_\gamma=\ell_i\},\qquad
F_i(\theta)=\sum_{(\gamma,m)\in\mathcal J_i}
a_{\gamma,m}e^{i\langle\theta,m[\gamma]\rangle}.
\tag{7}
\]
Haar 正交性與包內絕對可和給
\[
\widehat F_i(0)=\int_\Theta F_i(\theta)\,d\theta
=\sum_{\mathcal J_i:\,m[\gamma]=0}a_{\gamma,m}
\ge a_{C_i}>0.
\tag{8}
\]
其中 \(a_{C_i}\) 表示該見證的返回項權重，而不是另加一個重複計數。
故每個 \(F_i\) 不恆為零。這不表示它處處非零，亦不把正平均
誤當逐點正性。固定弧長時其實 \(F_i(0)=\sum_{\mathcal J_i}a>0\)
已能證非恆零；零同調見證額外給出明確的零 Fourier 模下界。

## 5. 一般角色命題：有限包或解析性的一項充分補強

**命題 2。** 假設每個 \(\mathcal J_i\) 有限，或其角色級數
在 torus 鄰域正常收斂為解析函數；一項明確充分條件是對某
\(\varepsilon>0\) 有
\[
\sum_{(\gamma,m)\in\mathcal J_i}
a_{\gamma,m}e^{\varepsilon\|m[\gamma]\|}<\infty
\quad(i=1,2,3).
\tag{9}
\]
則存在不依賴 c 的開稠密滿 Haar 測度集合 \(G\subset\Theta\)，使
\[
\forall\theta\in G\ \forall c>0:\quad
\mu_{c,\theta}\text{ 不集中於 }\mathcal P_p.
\tag{10}
\]
因此也不能等於該支撐上的正測度，或具有指數總變差界的複測度，
亦不能在共同絕對收斂半平面有 Laplace 等式，允許第 3 節修正。

證明。有限包時 \(F_i\) 為非零三角多項式。其零集 Haar 測度為零：
一維時化為非零普通多項式的有限零點；高維時按最後一個變數展開，
至少一個低維係數不恆零，歸納與 Fubini 使全部係數同零的例外集
為零測，其餘纖維只有有限零點。\(b=0\) 時包係數是正數，零集為空。
在 (9) 下，\(F_i\) 延伸到複角度的一個帶狀域，故為實解析。
對非零實解析函數 \(|F_i|^2\) 用
[Mityagin，Proposition 0][zeros]，同樣得到零集 Haar 測度零。
這些零集閉且無內點。因此
\(G=\Theta\setminus\bigcup_{i=1}^3\{F_i=0\}\) 開稠密且滿測度。
取同一 \(\theta\in G\)，對任何 c 用 (H) 選 i，則
\(\mu_{c,\theta}(\{c\ell_i\})=F_i(\theta)\ne0\)，證畢。

只有普通絕對收斂時，(8) 仍成立，但不能自動得到稠密／滿測度。
紙面反例：取圓周上一個非負非零 \(C^\infty\) 函數 g，支撐於足夠短的弧，
令 \(f(\theta)=\int_{\mathbb T}g(x)g(x+\theta)\,dx/(2\pi)\)。其 Fourier 係數
為 \(|\widehat g(k)|^2\ge0\)，快速衰減、絕對可和，零階係數為正，
但兩個支撐不交時 f 在一段非空開弧恆為零。省略零係數項後，各項權重
可皆為正。這是對「僅絕對收斂即 generic」推理的反例，不冒充本群實例。
僅用 (3) 還能保住較弱結論：各 \(F_i\) 連續且 \(F_i(0)>0\)，
故平凡角色附近有共同非空開鄰域，對其中全部角色及全部 c 仍有 (10)。

## 6. 時鐘量詞：已證與尚未證

(10) 的量詞交換合法，是因為**同一固定帶權測度的常數推送**不改
\(\mathcal J_i\)、\(F_i\) 或 G；不需要對不可數多個 c 作零集聯集。
若真正的 trace normalization 令每包乘共同非零因子，亦不改零集。
若允許每個 \(a_{\gamma,m}\) 隨 c 不同地重定權，則不是 (6)，
本篇不聲稱存在同一個 G。

對正密度換時 \(ds=\rho\,dt\)、\(\rho=c+Xu+\alpha(X)\)，
其中 u 全局單值且 \(\alpha\) 閉，週期為
\[
T_\rho(\gamma)=c\ell_\gamma+\langle[\alpha],[\gamma]\rangle,
\qquad T_\rho(C_i)=c\ell_i.
\tag{11}
\]
正性與三個零同調見證要求 c>0；\(Xu\) 的閉軌積分為零。
但其他軌道的碰撞條件現在是
\[
c(m\ell_\gamma-\ell_i)
+\langle[\alpha],m[\gamma]\rangle=0,
\tag{12}
\]
故新完整包一般不同。對**每個固定**的可容許 \(\rho\)，若其正權
返回測度與三包重新滿足第 2、5 節假設，(8) 仍含零同調見證，
可證「對該 \(\rho\)，幾乎每個 \(\theta\) 不可純素冪支撐」。
此處不推出「存在同一滿測度角色集，對全部 \(\rho\) 同時成立」。
不同參數的零集不能僅因逐一為零測便交換量詞；振幅也可能隨換時變化。
即使 \(\alpha\) 恰當而所有週期只作常數縮放，也需確認實際振幅遵守 (6)。
要進一步統一，須另證碰撞包族及振幅的可數／統一控制，而非只用 (11)。

## 7. 意義、逃生接口與實際動作

本輪排除：正權返回測度；以及固定弧長／常數推送模型下，具有有限包
或解析尾界的一般自由阿貝爾角色。例外角色仍可能存在，命題未證其可行。
有號／複數的任意權重、非阿貝爾局部系統、supertrace、任意正光滑換時、
正則化後不同物件及算子行列式，均不由本命題概括否定。

可攻擊的逃生接口是：不以素數表擬合的內在 holonomy，是否能迫使某個
非一般角色在所需全部非素冪包精確消去？第一個 kill test 是對預先固定的
候選，精確證明三個完整包 \(F_i\) 在該角色全非零；這就一次排除全部 c。
一個包消去只是通過此必要測試，不是整體 trace 已成立。

僅讀取適用 ARS／工作流、兩份既有 P29 筆記，及本輪上游資料；
普通瀏覽核對上述三項外部定理來源，沒有外傳內部筆記。
六指數來源只援用期刊摘要已可讀的定理陳述；其下載 PDF 文字編碼
不可讀，不把下載或頁面截圖請求當作全文核讀成功。
證明為逐式紙面推導；未執行科學程序、符號代數、枚舉、實驗、build、
正式審查或 Route／Stage 步驟。只以 apply_patch 新增本檔並回讀校核。
本檔是 AI 輔助內部候選論證，仍須主線整合核驗，不作正式證明認證。

[clock]: internal_goal01_null_homology_clock_obstruction_20260909.md
[units]: internal_algebraic_unit_lengths_and_prime_log_obstruction_20260909.md
[six]: https://hrj.episciences.org/86
[laplace]: https://api.pageplace.de/preview/DT0400.9783110215311_A15706968/preview-9783110215311_A15706968.pdf
[zeros]: https://arxiv.org/pdf/1512.07276
