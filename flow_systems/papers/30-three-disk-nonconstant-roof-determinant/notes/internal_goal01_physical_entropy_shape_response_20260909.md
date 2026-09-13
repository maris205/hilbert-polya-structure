# P30 goal01：真實物理熵的形狀響應與唯一雙側自然延拓

日期：2026-09-09 UTC。依本輪單檔授權只建立本筆記；不改任何舊筆記、原稿、程式、資料、鎖定輸入、正式回執或 Route／Stage 狀態，不運行科學程式。

**本新增合成仍待主整合審讀。** 以下是由明列上游命題與本頁直接證明組成的內部理論筆記，不是形式化驗證、外部獨立認證或新穎性聲明。

## 1. 共同實幾何鄰域及本頁命題

基準等邊三盤的半徑記為 \(a_0>0\)；當前圓心、半徑記為 \(C_i,a_i\)，其中 \(i=1,2,3\)。令

\[
\zeta=(\Delta C_i,\Delta a_i)_{i=1}^3\in U_{\mathbb R},
\qquad C_i=C_i^0+\Delta C_i,\quad a_i=a_0+\Delta a_i.
\tag{1}
\]

\(U_{\mathbb R}=U\cap\mathbb R^9\) 取為[熵身份筆記][entropy] §8.1 的共同實鄰域，必要時再縮小複鄰域 U，使其包含於同一局部全純壓力零點分支的定義域。盤標記、單位歐氏速率、首次碰撞和原物理時鐘均固定。a_0 不是變動的共同半徑。

本頁使用四項上游輸入，責任分開如下。

| 已完整讀取的筆記 | 本頁使用的命題及範圍 |
|---|---|
| [共同幾何全純筆記][geometry] §4–7 | 真實同碼配置、非擦邊、固定 Hölder 范數解析性及保週期共邊界；\(3a_0\le\tau_\zeta\le9a_0\)、\(2a_0\le\widehat g_\zeta\le10a_0\)。 |
| [壓力響應筆記][pressure] §3–6 | 當前較小 beta 空間上的實 RPF、正本徵測度、局部全純 h，以及 \(Dh=-h\mu^+(D\widehat g)/\mu^+(\widehat g)\)。 |
| [物理形狀首變分筆記][shape] §5 | 對任意雙側 code 逐點成立的 \(D\tau=-2\chi_0K_\delta+H_\delta\circ\sigma-H_\delta\)；其幾何證明不依賴 pressure 接口。 |
| [熵身份筆記][entropy] §8.1 | 每個 \(\zeta\in U_{\mathbb R}\) 的 \(h(\zeta)=h_T(\zeta)>0\)，其中 h_T 為同一單位速率物理流在雙向被困集上的拓撲熵。 |

舊壓力筆記的「本單元未識別物理熵」是其當時證明範圍；後續熵身份筆記提供新增接口，並不要求回改舊筆記或把舊結論倒寫成已完成。

固定上游同一 \(0<\theta<1\)、\(\alpha=\log(3/(2\sqrt6-1))/\log\theta\)、\(0<\beta<\alpha/2\) 及 \(q=\theta^\beta\in(0,1)\)，使用 \(\mathcal B^+=C^\beta(\Sigma^+,d_\theta^+)\) 與 \(\mathcal B^-=C^\beta(\Sigma,d_\theta)\)。兩個符號空間都是三字母相鄰不等的空間；\(\sigma^+,\sigma\) 是其左移，\(\pi:\Sigma\to\Sigma^+\) 保留非負座標。

**本頁命題。** 對每個當前實 \(\zeta\) 與實方向 \(\delta=(\delta C_i,\delta a_i)\)，存在下文明確構造的、RPF 一側概率 \(\mu_\zeta^+\) 的唯一雙側不變延拓 \(\overline\mu_\zeta\)，且

\[
\boxed{
Dh_T(\zeta)[\delta]
=2h_T(\zeta)\,
\frac{\displaystyle\int_\Sigma\chi_0(x)
       \bigl(n_0(x)\cdot\delta C_{x_0}+\delta a_{x_0}\bigr)
       \,d\overline\mu_\zeta(x)}
     {\displaystyle\int_\Sigma\tau_\zeta\,d\overline\mu_\zeta}.}
\tag{2}
\]

n_0 為障礙圓盤外法向；\(\chi_0=-v_0^-\cdot n_0=v_0^+\cdot n_0>0\)。所有積分測度均取當前參數及 \(s=h_T(\zeta)\)，不是任意不變概率，也不是已另行識別的物理流最大熵測度。

## 2. 一側 RPF 概率及其不變性

以下暫固定實 \(\zeta\)，簡記 \(h=h(\zeta)=h_T(\zeta)\)、\(g=\widehat g_\zeta\)，並令

\[
(Lf)(x)=\sum_{j\ne x_0}e^{-hg(jx)}f(jx),\qquad
Lv=v,\quad L^*\nu=\nu,\quad v>0,\quad \nu(v)=1.
\tag{3}
\]

這裡 \(\lambda(h,\zeta)=1\)；\(\nu\) 是正、有限、非零 Borel 本徵測度，v 是連續且嚴格正的 Hölder 本徵函數，均由[壓力響應筆記][pressure] §3–4 提供。令

\[
d\mu^+=v\,d\nu,\qquad
\mu^+(\Sigma^+)=\nu(v)=1.
\tag{4}
\]

對任意 Hölder F，逐逆分支有

\[
L\bigl(v(F\circ\sigma^+)\bigr)=F Lv=Fv.
\tag{5}
\]

以 \(\nu\) 積分並用 \(L^*\nu=\nu\)，得到

\[
\int F\circ\sigma^+\,d\mu^+=\int F\,d\mu^+.
\tag{6}
\]

有限柱集指示函數是局部常數，屬於 \(\mathcal B^+\)，故 (6) 已在生成 Borel 集的柱代數上證明 \((\sigma^+)_*\mu^+=\mu^+\)。也可用柱函數對連續函數的一致稠密性，把 (6) 延至全部連續 F。無須預先假設 \(\mu^+\) 不變。

## 3. 三字母配接給一側滿支撐

取任意允許詞 \(w=w_0\cdots w_{m-1}\)，\(m\ge1\)，令 \([w]_0^+\) 為對應非空一側柱集。對任意 \(x\in\Sigma^+\)，可在三字母中選

\[
b\notin\{w_{m-1},x_0\},\qquad y=w b x.
\tag{7}
\]

w 內部合法，兩個新接縫相鄰不等，故 y 合法，且 \((\sigma^+)^{m+1}y=x\)、\(y\in[w]_0^+\)。令 \(m_v=\min v>0\)、\(M_v=\max v<\infty\)。每條允許逆分支的權嚴格正，且 \(g\le10a_0\)、h>0，因此

\[
L^{m+1}\bigl(v1_{[w]_0^+}\bigr)(x)
\ge m_v e^{-10a_0h(m+1)}>0.
\tag{8}
\]

這只取求和中的一條合法逆分支，沒有宣稱任意無限制拼接都合法。由 \(\nu(v)=1\le M_v\nu(1)\) 以及本徵測度關係，

\[
\begin{aligned}
\mu^+([w]_0^+)
&=\int L^{m+1}\bigl(v1_{[w]_0^+}\bigr)\,d\nu\\
&\ge\frac{m_v}{M_v}e^{-10a_0h(m+1)}>0.
\end{aligned}
\tag{9}
\]

每個非空開集包含一個這樣的柱集，所以 \(\operatorname{supp}\mu^+=\Sigma^+\)。特別地，每個盤的碰撞柱 \([i]_0^+\) 都有正概率。這是正權、三字母配接及 RPF 測度性質的結論，不是由「某個週期曾訪問該盤」推出的概率結論。常數 \(m_v/M_v\) 在此允許依賴當前 \(\zeta\)。

## 4. 雙側自然延拓：相容性、明確存在、不變性與唯一性

### 4.1 左右有限邊緣相容

對每個有限允許詞定義 \(p(w)=\mu^+([w]_0^+)\)，非法詞約定 p=0，空詞 p=1。右端延長是柱集分割，左端延長由 (6) 的不變性給出：

\[
\sum_{b\ne w_{m-1}}p(wb)=p(w),\qquad
\sum_{c\ne w_0}p(cw)
=\mu^+((\sigma^+)^{-1}[w]_0^+)=p(w).
\tag{10}
\]

因此任意有限整數區間 \([j,k]\) 都可賦同一個長度分布

\[
\overline\mu([w]_{[j,k]})=p(w),\qquad |w|=k-j+1,
\tag{11}
\]

且向左右增加座標後再取邊緣，均回到原分布。不同有限座標集合可先補成一個區間再邊緣化；(10) 保證選取更大區間不改變結果。以下真正構造具有 (11) 的測度，而不把存在性當作假設。

### 4.2 用巢狀區間分割構造 Borel 概率

對中心區間 \([-r,r]\) 的全部允許詞 w，從 r=0 開始，按固定字典序構造 \([0,1)\) 的有限半開分割 \(\{I_w\}\)，要求 \(|I_w|=p(w)\)。第一層由 \(\sum_i p(i)=1\) 給出。

若長度 \(2r+1\) 的父詞 w 已分配區間 I_w，下一層在 I_w 內依固定順序放置其全部合法子詞 cwb 的相鄰半開區間，長度分別為 p(cwb)。由 (10)，

\[
\sum_{c,b}p(cwb)=p(w),
\tag{12}
\]

故這些子區間恰分割父區間；零長度者為空集，不造成歧義。所有區間均左閉右開，因此對每個 \(u\in[0,1)\)，每層恰有一個含 u 的 I_w，對應詞 \(w_r(u)\) 彼此為中央延伸。

這些相容中央詞給唯一的雙側允許序列 X(u)：對任意整數 j，取 \(r\ge|j|\)，以 \(w_r(u)\) 的 j 座標定義 X(u)_j，且其值不依賴 r。每對相鄰座標都出現在某個允許詞內，所以 \(X(u)\in\Sigma\)。對任意中央柱，

\[
X^{-1}([w]_{[-r,r]})=I_w.
\tag{13}
\]

一般有限柱是足夠長中央柱的有限不交聯集，故 X 對柱生成的 Borel 結構可測。令 \(\mathfrak m\) 為 \([0,1)\) 上的 Lebesgue 概率，定義

\[
\overline\mu=X_*\mathfrak m.
\tag{14}
\]

這是一個實際存在的 Borel 概率。由 (13) 及有限邊緣相容性，它滿足全部 (11)，不只中央柱的賦值。分割順序只是一種存在性構造；下節的唯一性保證最終 Borel 測度不依賴這個順序。

### 4.3 不變性、投影及唯一性

左移逆像滿足 \(\sigma^{-1}[w]_{[j,k]}=[w]_{[j+1,k+1]}\)。兩者由 (11) 具有相同概率，因此 \(\sigma_*\overline\mu=\overline\mu\)。非負座標柱又給

\[
\pi_*\overline\mu=\mu^+.
\tag{15}
\]

上述測度等式在柱集上成立後，延至全部 Borel 集：中央柱連同空集、全空間形成生成 Borel 結構的 \(\pi\)-系統，\(\pi\)-\(\lambda\) 論證保證兩個概率若在此一致便處處一致。

反之，設 \(\widetilde\mu\) 是任何 \(\sigma\)-不變 Borel 概率，且 \(\pi_*\widetilde\mu=\mu^+\)。雙側 \(\sigma\) 可逆，不變性因而對所有整數次移位成立。對任意 \([j,k]\) 及相應 w，

\[
[w]_{[j,k]}=(\sigma^j)^{-1}\pi^{-1}[w]_0^+,
\quad\Longrightarrow\quad
\widetilde\mu([w]_{[j,k]})=\mu^+([w]_0^+)=p(w).
\tag{16}
\]

因此 \(\widetilde\mu=\overline\mu\)。這是**固定 \(\mu^+\) 的唯一雙側不變延拓**，不是「\(\Sigma\) 上只有一個不變測度」的錯誤敘述。最後，(9)、(11) 使所有非空雙側柱都有正概率，故 \(\operatorname{supp}\overline\mu=\Sigma\)。恢復參數記號，這就是 (2) 所用的 \(\overline\mu_\zeta\)。

## 5. 在固定 Banach 空間微分共邊界，再對當前測度積分

[共同幾何筆記][geometry] §7 給出共同固定的 R、\(N_*\) 和 Banach 值全純族，使

\[
\widehat g_\zeta\circ\pi
=\tau_\zeta-V_\zeta+V_\zeta\circ\sigma.
\tag{17}
\]

這裡 \(\widehat g_\zeta\in\mathcal B^+\)，\(\tau_\zeta,V_\zeta\in\mathcal B^-\)。拉回 \(F\mapsto F\circ\pi\) 是固定有界線性算子，范數至多 1；\(F\mapsto F\circ\sigma\) 在 \(\mathcal B^-\) 上的范數至多 \(q^{-1}\)。兩者均不隨幾何參數變動。因此在同一 Banach 范數中合法微分 (17)，得到

\[
(D\widehat g_\zeta[\delta])\circ\pi
=D\tau_\zeta[\delta]-DV_\zeta[\delta]
 +(DV_\zeta[\delta])\circ\sigma.
\tag{18}
\]

對**當前**概率 \(\overline\mu_\zeta\) 積分，全部函數有界，(15) 和 \(\sigma\)-不變性分別消去兩個共邊界：

\[
\begin{aligned}
\mu_\zeta^+(\widehat g_\zeta)
&=\int_\Sigma\tau_\zeta\,d\overline\mu_\zeta,\\
\mu_\zeta^+(D\widehat g_\zeta[\delta])
&=\int_\Sigma D\tau_\zeta[\delta]\,d\overline\mu_\zeta.
\end{aligned}
\tag{19}
\]

第一個等式使用 (17)，第二個使用 (18)。這不是對 \(\int\widehat g_\zeta\,d\mu_\zeta^+\) 求全導數時省略測度導數；本頁根本不作這種操作。

真正的導數輸入是[壓力響應筆記][pressure] §5–6 的譜微分式：在 \(P(h(\zeta),\zeta)=0\) 處，

\[
P_s=-\mu_\zeta^+(\widehat g_\zeta),\qquad
D_\zeta P[\delta]=-h\mu_\zeta^+(D\widehat g_\zeta[\delta]),
\qquad
Dh[\delta]=-h\frac{\mu_\zeta^+(D\widehat g_\zeta[\delta])}
                        {\mu_\zeta^+(\widehat g_\zeta)}.
\tag{20}
\]

左右本徵對的微分項已在上游 \(D\lambda=\nu((DL)v)\) 中消去。把 (19) 代入的是已證的導數表達式，不必證明測度的參數導數存在。

再以 [熵身份筆記][entropy] §8.1 的 \(h=h_T\) 逐點身份及 h 的實解析性，得到真實熵實解析，且

\[
\boxed{Dh_T(\zeta)[\delta]
=-h_T(\zeta)
\frac{\int D\tau_\zeta[\delta]\,d\overline\mu_\zeta}
     {\int\tau_\zeta\,d\overline\mu_\zeta},\qquad
3a_0\le\int\tau_\zeta\,d\overline\mu_\zeta\le9a_0.}
\tag{21}
\]

實解析性由同一實開集上與 h 相等得到；複參數分支僅是解析延拓，不把複幾何叫作物理流。熵身份來源中的 primitive 計數漸近只在上游逐點識別 h_T；本頁沒有對該漸近、其誤差、起點或隱含常數求參數微分，也不需要其參數一致性。

## 6. 逐點物理首變分合成為熵形狀公式

對當前實幾何的雙側真實配置，記 \(q_j=q_{j,\zeta}(x)\)、\(n_0=(q_0-C_{x_0})/a_{x_0}\)，並保持外法向與入／出射速度約定。令

\[
K_\delta=n_0\cdot\delta C_{x_0}+\delta a_{x_0},
\qquad H_\delta=v_0^-\cdot Dq_{0,\zeta}[\delta].
\tag{22}
\]

[形狀首變分筆記][shape] §5 直接由 \(v_0^+\cdot(Dq_1-Dq_0)\)、反射關係與 \(n_0\cdot Dq_0=n_0\cdot\delta C_{x_0}+\delta a_{x_0}\) 得到

\[
D\tau_\zeta[\delta]
=-2\chi_0K_\delta+H_\delta\circ\sigma-H_\delta.
\tag{23}
\]

該式逐點成立，不只沿週期求和成立。所有量在當前實幾何下有界；共同幾何的解析性與正飛行長度使它們屬於相應 Hölder 空間。因此對已構造的不變概率積分，

\[
\int D\tau_\zeta[\delta]\,d\overline\mu_\zeta
=-2\int\chi_0K_\delta\,d\overline\mu_\zeta.
\tag{24}
\]

(24) 代入 (21) 正好得到 (2)。壓力導數前的負號和物理首變分前的負二相乘，產生熵形狀公式的正二；外面的 h_T 因子不能刪去。

## 7. 剛體、尺度與半徑方向的精確後果

以下每個方向均取於當前 \(\zeta\in U_{\mathbb R}\)，實變化參數足夠小以留在共同鄰域。結果只是一階局部響應，除明列的剛體／尺度恆等式外不宣稱各條軌道具有相同相對變化率。

### 7.1 共同平移：零

取 \(\delta C_i=u\in\mathbb R^2\)、\(\delta a_i=0\)。共同平移把真實同碼配置變為 \(q_j+\varepsilon u\)；唯一性識別它為變動幾何的同碼配置。每條飛行向量不變，所以 \(D\tau[\delta]=0\)。由 (21)，

\[
\boxed{Dh_T[(u,0)_{i=1}^3]=0,\qquad
\int\chi_0 n_0\,d\overline\mu_\zeta=0.}
\tag{25}
\]

第二式由 (24) 對所有 u 成立得到。它是平均相消，不是每次碰撞的 \(n_0\cdot u\) 都為零。

### 7.2 共同旋轉：零

令 B 為實反對稱二階矩陣，\(B^{\mathsf T}=-B\)，取 \(C_i(\varepsilon)=e^{\varepsilon B}C_i\)、半徑不變。此路徑在當前點的方向為 \(\delta C_i=BC_i\)、\(\delta a_i=0\)。真實同碼配置亦被共同旋轉，故

\[
D\tau[\delta]
=v_0^+\cdot B(q_1-q_0)
=\tau\,v_0^+\cdot Bv_0^+=0,
\quad
\boxed{Dh_T[(BC_i,0)_{i=1}^3]=0.}
\tag{26}
\]

相應地 \(\int\chi_0 n_0\cdot BC_{x_0}\,d\overline\mu_\zeta=0\)，仍是積分相消。繞任意固定點的旋轉可由此方向加一個共同平移得到。

### 7.3 整體尺度：負 h_T

取 \(C_i(\varepsilon)=(1+\varepsilon)C_i\)、\(a_i(\varepsilon)=(1+\varepsilon)a_i\)。方向是 \(\delta C_i=C_i\)、\(\delta a_i=a_i\)，包含圓心和半徑一起縮放。保持單位速度時，同碼配置及飛行長度都乘以 \(1+\varepsilon\)，所以 \(D\tau[\delta]=\tau\)。因此

\[
\boxed{Dh_T[(C_i,a_i)_{i=1}^3]=-h_T,\qquad
\int\chi_0(n_0\cdot C_{x_0}+a_{x_0})\,d\overline\mu_\zeta
=-\tfrac12\int\tau\,d\overline\mu_\zeta.}
\tag{27}
\]

這裡微分參數 \(\varepsilon\) 是無量綱相對尺度。若同一相似形狀改用絕對尺度 a 作參數，則相應寫法是 \(dh_T/da=-h_T/a\)；不能把兩種參數的導數混成同一數值。

### 7.4 固定圓心共同增加半徑：嚴格正

取 \(\delta C_i=0\)、\(\delta a_i=r_0>0\)。此時 \(K_\delta=r_0\)。非擦邊性給連續 \(\chi_0(x)>0\)；\(\Sigma\) 緊緻，所以當前參數存在 \(c_\chi=\min_x\chi_0(x)>0\)。由 (2)，

\[
\boxed{Dh_T[(0,r_0)_{i=1}^3]
=2h_Tr_0\frac{\int\chi_0\,d\overline\mu_\zeta}
                 {\int\tau\,d\overline\mu_\zeta}>0.}
\tag{28}
\]

h_T>0、分母正且 \(\int\chi_0\ge c_\chi\)，嚴格號因此成立。這個方向沒有移動圓心，與 §7.3 的整體縮放不是同一變化，兩個符號相反沒有矛盾。

### 7.5 只增加指定盤的半徑：滿支撐後才得到嚴格正

固定 \(i\in\{1,2,3\}\)，只取 \(\delta a_i=r_0>0\)，其餘所有半徑、圓心方向為零。於是 \(K_\delta=r_0 1_{\{x_0=i\}}\)，且由 §3–4，

\[
\overline\mu_\zeta\{x_0=i\}=\mu_\zeta^+([i]_0^+)>0,
\qquad
\int\chi_0 1_{\{x_0=i\}}\,d\overline\mu_\zeta
\ge c_\chi\mu_\zeta^+([i]_0^+)>0.
\tag{29}
\]

將此方向導數除以 r_0（等價於取 \(r_0=1\)），得到

\[
\boxed{\frac{\partial h_T}{\partial a_i}(\zeta)
=2h_T\frac{\int\chi_0 1_{\{x_0=i\}}\,d\overline\mu_\zeta}
             {\int\tau\,d\overline\mu_\zeta}>0,\qquad i=1,2,3.}
\tag{30}
\]

若是任意其他不變測度，可能根本不訪問盤 i；僅有 \(\chi_0>0\) 不能排除該積分為零。本頁所用 RPF 概率的滿支撐已在 §3 明證，因而排除此問題。由線性性，固定圓心、各半徑方向非負且至少一盤嚴格增加，同樣有嚴格正的一階熵響應。

## 8. 證據範圍及實際操作

本頁新增的合成是「真實實鄰域上的熵身份 + 新空間的 RPF 壓力導數 + 明確雙側測度 + 逐點物理首變分」。自然延拓、滿支撐、合法共邊界微分和特殊方向均已寫出實際論證；沒有把另一個席位的同意當作獨立科學證據。

全頁鄰域估計只用上游實幾何界 \(3a_0\le\tau\le9a_0\) 及新正代表界 \(2a_0\le\widehat g\le10a_0\)。基準的 \(4a_0/8a_0\) 飛行界沒有被複用到變形鄰域。沒有微分 source prime-orbit 漸近；沒有交換軌道無窮和、漸近極限與幾何微分。

尚未建立的內容包括物理流最大熵測度身份、熵二階／方差公式、全頻率或 source strip 的幾何一致性，以及物理散射 resolvent、核性、ordinary trace、Fredholm／quantum determinant 或 Hilbert–Pólya 身份。這些不由本頁的一階公式自動推出；原 Route、Gate、Stage 停止條件與歷史失敗紀錄不變。

本次完整讀取表列四份上游筆記；外部 RPF 與 classical prime-orbit 定理的適用性由它們明列的已核讀接口承擔，沒有把本輪未重新打開的來源宣稱為本輪新增核讀。另有一個同模型只讀席檢查有限測度引理及其唯一性／嚴格正性前提，未讀寫文件、運行程式或新增來源。ARS 有限 Phase 3 合成及 DA 指引具體影響了源頭責任分開、雙側測度不預設存在、全支撐後的嚴格號、壓力與計數微分的區別，以及尺度／半徑方向的分離。

寫前以 `test ! -e` 確認本目標不存在；只用 `apply_patch` 新建本檔。寫後僅安排一次合併的最小靜態檢查，限於控制字元、尾空白、衝突標記、公式分隔／編號、本地鏈接和行數；它不認證數學正確性。未運行科學、符號或數值程式、軌道枚舉、實驗、artifact writer、稿件構建或正式驗證器，未修改任何舊檔或正式狀態。

[geometry]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_joint_geometry_holomorphy_20260909.md
[pressure]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_pressure_zero_geometry_response_20260909.md
[shape]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_physical_period_shape_derivative_20260909.md
[entropy]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_pressure_equals_physical_entropy_20260909.md
