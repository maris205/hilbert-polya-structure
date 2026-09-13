# P30 goal01：RPF 壓力零點等於同一物理流的拓撲熵

日期：2026-09-09 UTC。授權範圍：主線先要求有限只讀推導，隨後明確授權將完整證明保存為本獨占新檔。只新增本檔，不改舊筆記、現稿、程式、資料、歷史、鎖定輸入或正式狀態；不運行科學程式。

## 0. 結論與本頁新增接口

保持原等邊三盤、半徑 \(a>0\)、中心距 \(6a\)、單位速率與逐碰撞標記。對本頁 §1 所列任一正 Hölder 代表 r，令 \(\lambda_t\) 是勢 \(-tr\) 的實 RPF 正主特徵值。則

\[
\boxed{\lambda_h=1\quad\Longleftrightarrow\quad h=h_T,}
\tag{1}
\]

其中 \(h_T\) 是原單位速率物理流在雙向被困集上的拓撲熵。

證明只使用：一字母週期配接、共同前綴 distortion、正本徵函數給出的權重增長比較、已落盤的 primitive 物理軌道雙射，以及已適用的經典 prime-orbit 計數定理。沒有引入未核讀的 suspension 熵／變分壓力大定理，也沒有把一般 Hölder 轉移算子的固定點和冒稱 ordinary trace。

本頁先在一個固定代表及其自身 Banach 空間上證明 (1)，再於 §8 比較舊 g 與新 \(\widehat g_0\)。兩者同週期和給相同的實 RPF 主值，不給跨空間全譜相同。§8.1 按後續明確授權，在已核對前提的真實幾何鄰域中逐點延伸這個身份。

## 1. 固定輸入及新舊 roof 的適用方式

令

\[
\Sigma=\{x\in\{1,2,3\}^{\mathbb Z}:x_i\ne x_{i+1}\},\qquad
\Sigma^+=\{x\in\{1,2,3\}^{\mathbb N_0}:x_i\ne x_{i+1}\}.
\tag{2}
\]

左移分別為 \(\sigma,\sigma^+\)，\(\pi:\Sigma\to\Sigma^+\) 保留非負座標。原物理 roof \(\tau\) 滿足 \(4a\le\tau\le8a\)；全部雙側容許盘字與真實被困碰撞後狀態一一對應。

本頁一次固定一個代表 r、一個符號度量 \(d_\theta^+\) 和一個指數 \(\beta>0\)，使

\[
r\in C^\beta(\Sigma^+,d_\theta^+),\qquad
2a\le r\le10a,\qquad
r\circ\pi=\tau-U_r+U_r\circ\sigma.
\tag{3}
\]

這些輸入分別由以下文件提供：

- 舊代表 \(r=g\)：[正一側 roof 筆記][old-roof] §3 式 (11)、(14)，端點指數為 \(\alpha/2\)。
- 新代表 \(r=\widehat g_0\)：[幾何響應筆記][pressure] §1、§3，指數取 \(0<\beta<\alpha/2\)，基準半徑 \(a_0\) 在本頁記為 a。該筆記已在較小指數的空間重新應用 RPF，並明確沒有把新舊 roof 說成逐點相同。
- 物理軌道與時間：[同軌道 classical-zeta 筆記][classical] §1、§3–5，使用真實首次碰撞、唯一雙側編碼、保週期共邊界及原單位速率。

本頁不重新選平均長度、不改 r 或時鐘，也不把不同代表的 Banach 空間視為相同。

對每個雙側 n 週期點，(3) 給

\[
S_nr(\pi x)=S_n\tau(x)\quad(\sigma^nx=x).
\tag{4}
\]

一側週期點有唯一雙側週期延拓，primitive 移位循環與 primitive 物理流軌道保最小週期雙射。此處只按循環移位去掉起始碰撞，不另按幾何對稱或反轉取商；兩碰撞往返軌道不能一律 double。下文固定點和尚未按 primitive 循環取商。

## 2. 實 RPF 主值與正權增長的明確上下界

定義

\[
(\mathcal L_tu)(x)=\sum_{j\ne x_0}e^{-tr(jx)}u(jx),\qquad
A_n(t)=\|\mathcal L_t^n1\|_\infty,\qquad t\in\mathbb R.
\tag{5}
\]

允許矩陣 \(A=J_3-I_3\) 滿足 \(A^2=J_3+I_3>0\)。令 \(q=\theta^\beta\in(0,1)\)，則實勢 \(-tr\) 属於 RPF 來源的柱集變差空間 \(\mathcal F_q\)。若來源半范數以座標 \(0,\ldots,k\) 一致時的變差除以 \(q^k\) 定義，則

\[
|u|_q\le q[u]_\beta,\qquad
[u]_\beta\le\max\{2\|u\|_\infty,q^{-1}|u|_q\}.
\tag{6}
\]

因此在每個所選空間中可分別應用已核讀的 [Stoyanov, Theorem 2.1(a)][rpf]：有正主值 \(\lambda_t>0\) 和嚴格正本徵函數 \(v_t\)，且

\[
\mathcal L_tv_t=\lambda_tv_t,\qquad
0<m_t:=\min v_t\le v_t\le M_t:=\max v_t<\infty.
\tag{7}
\]

本頁只使用來源的正本徵對，不需要其全部譜分解或定量常數。令 \(C_t=M_t/m_t\ge1\)。從 \(v_t/M_t\le1\le v_t/m_t\) 出發，以正算子 \(\mathcal L_t^n\) 作用，得到逐點及上確界比較：

\[
C_t^{-1}\lambda_t^n
\le(\mathcal L_t^n1)(x)
\le C_t\lambda_t^n,\qquad
C_t^{-1}\lambda_t^n\le A_n(t)\le C_t\lambda_t^n.
\tag{8}
\]

故 \(\lim_nA_n(t)^{1/n}=\lambda_t\)，確實是既有筆記用增長率定義的同一個 lambda。

還可把 A_n 的下界加強。正性給 \(A_{n+m}\le A_nA_m\)。對固定 n，\(A_{kn}\le A_n^k\)；取 \(kn\) 次根再令 k 趨向無窮，由 (8) 得 \(\lambda_t\le A_n^{1/n}\)。因此

\[
\boxed{\lambda_t^n\le A_n(t)\le C_t\lambda_t^n.}
\tag{9}
\]

C_t 可以依賴固定 t、代表及其空間；此處不宣稱全部實 t、幾何參數或高頻共用一個 C。

## 3. 共同前綴 distortion 與恰一個字母的 closing

令

\[
G=[r]_\beta,\qquad D=\frac{Gq}{1-q}.
\tag{10}
\]

若合法點 y、z 的前 n 個符號一致，則第 j 次移位後仍有前 \(n-j\) 個符號一致。所以

\[
|S_nr(y)-S_nr(z)|
\le G\sum_{j=0}^{n-1}q^{n-j}
=D(1-q^n)\le D.
\tag{11}
\]

這裡幾何和從 q 而不是 1 開始；D 中的 q 不能漏掉。

令固定點加權和為

\[
W_n(t):=\sum_{\sigma_+^ny=y}e^{-tS_nr(y)}.
\tag{12}
\]

### 3.1 一字母 closing 的合法性、單射與代價

固定 tail \(x\in\Sigma^+\)。對每個使 \(wx\) 合法的長度 n 前綴 \(w=w_0\cdots w_{n-1}\)，選

\[
b(w)=\min\bigl(\{1,2,3\}\setminus\{w_{n-1},w_0\}\bigr),\qquad
z_w=(w\,b(w))^\infty.
\tag{13}
\]

兩個被排除的字母至多不同，故三字母集合保證 b(w) 存在。w 內部已合法；新接縫 \(w_{n-1}\to b(w)\) 和閉合接縫 \(b(w)\to w_0\) 都相鄰不等。因此 \(z_w\in\operatorname{Fix}(\sigma_+^{n+1})\)。

映射 \(w\mapsto z_w\) 單射，因 z_w 的前 n 個固定記錄位置就是 w。z_w 未必有最小週期 n+1，但 (12) 統計的是全部固定點，故不成問題；此步不能提前按循環移位取商。

z_w 與 wx 的前 n 符號一致，且新增一項 roof 至多 10a。由 (11)，

\[
|S_{n+1}r(z_w)-S_nr(wx)|\le D+10a.
\tag{14}
\]

對任意實 t，以正權逐項比較、在固定 x 上求和，再取 x 的上確界，得到

\[
\boxed{e^{-|t|(D+10a)}A_n(t)\le W_{n+1}(t),\qquad n\ge1.}
\tag{15}
\]

closing 長度恰為 1；乘性代價明確為 \(e^{|t|(D+10a)}\)，與 n、w、x 無關。

### 3.2 三組週期詞給反向上界

對每個 \(j\in\{1,2,3\}\)，固定一條首字母為 j 的合法 tail \(x^{(j)}\)，例如令 j 與某個不同字母永遠交替。

把 \(y=w^\infty\in\operatorname{Fix}(\sigma_+^n)\) 按 \(w_0=j\) 分成三組。週期合法性給 \(w_{n-1}\ne w_0=j\)，所以 \(w x^{(j)}\) 是 \(x^{(j)}\) 的合法 n 步前像。同一組不同固定點有不同的長度 n 記錄詞 w，因此映射到這些前像是單射。

由共同前綴比較 (11)，並允許把每組求和擴大到全部 n 步前像，

\[
\begin{aligned}
W_n(t)
&\le e^{|t|D}\sum_{j=1}^3
  \sum_{\substack{w:\,w_0=j\\w\ {\rm cyclically\ legal}}}
       e^{-tS_nr(w x^{(j)})}\\
&\le e^{|t|D}\sum_{j=1}^3\mathcal L_t^n1(x^{(j)})
\le3e^{|t|D}A_n(t).
\end{aligned}
\tag{16}
\]

n=1 沒有容許固定點，所以上界仍成立；下界 (15) 則從 n=1 起提供二週期點。

由 (9)、(15)–(16)，令 \(E_t=e^{-|t|(D+10a)}\)、\(U_t=3e^{|t|D}C_t\)，對全部 n≥2 有

\[
\boxed{E_t\lambda_t^{n-1}\le W_n(t)\le U_t\lambda_t^n.}
\tag{17}
\]

特別地，

\[
\lim_{n\to\infty}W_n(t)^{1/n}=\lambda_t.
\tag{18}
\]

這是由正權配接得出的固定點和增長率，不是任何 ordinary trace 公式。

## 4. RPF 一側的精確收斂集合，包含臨界點

定義允許無窮值的非負實級數

\[
F_r(t)=\sum_{n\ge1}\frac{W_n(t)}n\in[0,\infty].
\tag{19}
\]

若 \(\lambda_t<1\)，(17) 的上界被幾何級數控制，故 \(F_r(t)<\infty\)。若 \(\lambda_t>1\)，(17) 的下界使 \(W_n(t)/n\) 不趨零，故發散。

在 \(\lambda_t=1\) 時不能只用根判別法；(17) 明確給

\[
W_n(t)\ge E_t>0\quad(n\ge2),\qquad
F_r(t)\ge E_t\sum_{n\ge2}\frac1n=+\infty.
\tag{20}
\]

因此臨界點有調和發散，且

\[
\boxed{F_r(t)<\infty\quad\Longleftrightarrow\quad\lambda_t<1.}
\tag{21}
\]

## 5. 同一物理 primitive 軌道給另一個精確收斂集合

令 \(\mathcal P_{\rm phys}\) 是 primitive 相流軌道集合，\(\ell(\gamma)\) 為最小物理週期。[同軌道筆記][classical] §3–4 已建立保週期雙射。因 (19) 的所有實權項皆非負，直接用 Tonelli 重排，即使兩邊發散仍有

\[
F_r(t)=
\sum_{\gamma\in\mathcal P_{\rm phys}}
\sum_{k\ge1}\frac{e^{-tk\ell(\gamma)}}k.
\tag{22}
\]

確切重數是：若 primitive 符號循環的最小長度為 m，則在 \(n=km\) 層恰有 m 個固定點，每點的週期和為 \(k\ell(\gamma)\)，故係數為 \(m/(km)=1/k\)。沒有額外的起始點或方向因子。

每條閉物理軌道至少有兩次碰撞，且每次飛行至少 4a，所以

\[
\ell(\gamma)\ge\ell_*:=8a>0.
\tag{23}
\]

對 \(t>0\)，令 \(\mathcal D(t)=\sum_\gamma e^{-t\ell(\gamma)}\)。因 \(0<e^{-t\ell(\gamma)}\le e^{-t\ell_*}<1\)，

\[
\boxed{\mathcal D(t)\le F_r(t)
\le\frac{\mathcal D(t)}{1-e^{-t\ell_*}}.}
\tag{24}
\]

此式容許兩邊為無窮值；其上界只用 \(\sum_{k\ge1}u^k/k\le u/(1-u)\)。

### 5.1 經典計數輸入與非循環性

本頁使用 [Stoyanov, Corollary 6.4][classical-source] 的計數部分，已在 [同軌道筆記][classical] §2、§5 核對本案適用性：

\[
\Pi(T):=\#\{\gamma:\ell(\gamma)\le T\}
\sim\frac{e^{h_TT}}{h_TT},\qquad h_T>0.
\tag{25}
\]

原推論同時斷言存在計數誤差指數 \(c\in(0,h_T)\)，故正性是該既有定理的結論；此處沒有用待證的 \(\lambda_{h_T}=1\) 反過來驗證來源。h_T 是物理流熵，不是 (18) 的符號迭代增長率。

### 5.2 Laplace 計數式及 \(t=h_T\) 的調和型發散

對 \(t>0\)，以非負 integrand 的 Tonelli 等式寫成

\[
\begin{aligned}
\mathcal D(t)
&=\sum_\gamma t\int_{\ell(\gamma)}^\infty e^{-tT}\,dT\\
&=t\int_0^\infty e^{-tT}\Pi(T)\,dT.
\end{aligned}
\tag{26}
\]

這不是先假設級數收斂再作分部積分；兩邊可同為 \(+\infty\)。有限 T 下的 \(\Pi(T)\) 有限，也可由 \(n\le T/(4a)\) 及有限字母週期詞數直接看出。

由 (25)，存在 \(T_0>0\) 及 \(c_-,c_+>0\)，使 \(T\ge T_0\) 時

\[
c_-\frac{e^{h_TT}}T\le\Pi(T)\le
c_+\frac{e^{h_TT}}T.
\tag{27}
\]

所以 (26) 的尾部被正的常數倍
\(\int_{T_0}^\infty e^{-(t-h_T)T}\,dT/T\)
上下控制。它在 \(t>h_T\) 時收斂；在 \(0<t<h_T\) 時發散；在 \(t=h_T\) 時恰由 \(\int_{T_0}^\infty dT/T\) 的發散給出邊界判定。

由 (24)，

\[
F_r(t)<\infty\quad\Longleftrightarrow\quad t>h_T
\qquad(t>0).
\tag{28}
\]

對 \(t\le0\)，(25) 保證有無窮多條 primitive 軌道，而 (22) 中 k=1 的每項至少為 1，故 \(F_r(t)=+\infty\)。因此 (28) 也確定整條實軸的收斂集合。

## 6. 唯一的 RPF 零點與物理熵完全相等

由 \(2a\le r\le10a\)，任意 \(\delta>0\) 給逐權重比較，再由 (8) 取 n 次根，得到

\[
e^{-10a\delta}\lambda_t
\le\lambda_{t+\delta}
\le e^{-2a\delta}\lambda_t.
\tag{29}
\]

故 \(\log\lambda_t\) 連續、嚴格遞減，且對實參數差有 Lipschitz 上界 10a。又 \(\mathcal L_01=2\)，所以 \(\lambda_0=2\)；由 (29)，\(\lambda_t\le2e^{-2at}\to0\) 當 \(t\to+\infty\)。因此有唯一正數 h 使

\[
\lambda_h=1,\qquad
\{t:\lambda_t<1\}=(h,\infty),\qquad
\frac{\log2}{10a}\le h\le\frac{\log2}{2a}.
\tag{30}
\]

比較 (21) 與 (28) 得

\[
(h,\infty)=\{t:F_r(t)<\infty\}=(h_T,\infty).
\tag{31}
\]

兩個實端點必相同，否則可在它們中間選一個正 t，對同一非負級數得到收斂與發散的矛盾。因此

\[
\boxed{h=h_T,\qquad \lambda_{h_T}=1.}
\tag{32}
\]

若使用 RPF 譜壓力記號 \(P_r(t)=\log\lambda_t\)，這正是 \(P_r(h_T)=0\)。本頁沒有另行宣稱 \(P_r\) 已滿足某個未核讀的變分原理；其零點身份已由具體週期資料證明。

繼承 [同軌道筆記][classical] §5 的物理 roof 計數界後，這個 h 亦滿足 \(\log2/(8a)\le h\le\log2/(4a)\)。此較強界不是證明 (32) 的前提。

## 7. 初始解析域的附帶區分

對複數 s，週期級數的每一實體項的模為 \(e^{-(\operatorname{Re}s)S_nr}\)。由 (21)、(28)、(32)，原週期級數在 \(\operatorname{Re}s>h_T\) 絕對且局部一致收斂：給定緊集，選其實部下界 \(t_0>h_T\)，全部項由 \(F_r(t_0)<\infty\) 控制。

所以其指數在該初始域解析且不消失。另一方面，classical-zeta 的來源延拓可以越過 h_T；左側的延拓值不再由已發散的原非負實級數計算。在 h_T，§4 和 §5.2 分別給出調和型發散，與已有簡單極點結論相容；本文不以級數比較另證極點階數或留數。

本節談的是固定點和中逐項的絕對收斂。沒有將複數 n 層內的相消誤當成實體項絕對收斂，也沒有建立算子 ordinary trace。

## 8. 舊 g 與新 \(\widehat g_0\)：相同實主值而非相同全譜

在固定基準幾何上，舊 g 和新 \(\widehat g_0\) 都由 (3) 與同一 \(\tau\) 共邊界相連。對每個一側 n 週期點，其唯一雙側延拓給

\[
S_ng(y)=S_n\widehat g_0(y)=S_n\tau(x).
\tag{33}
\]

故對每個實 t 和每個 n，其固定點和完全相同：

\[
W_n^{\,g}(t)=W_n^{\,\widehat g_0}(t).
\tag{34}
\]

分別在各自空間使用 (18)，即得

\[
\boxed{\lambda_t^{\,g}
=\lim_n(W_n^{\,g}(t))^{1/n}
=\lim_n(W_n^{\,\widehat g_0}(t))^{1/n}
=\lambda_t^{\,\widehat g_0}
\quad(t\in\mathbb R).}
\tag{35}
\]

因此兩種實 RPF 零點都是 h_T。各自的 \(\beta,q,G,D,C_t\) 可以不同；它們在取 n 次根的增長率比較中消失。此處不要求兩個正 roof 逐點相同，也不要求在兩個 Banach 空間之間存在有界相似變換。

式 (35) 不識別全部複譜、本質譜、高頻常數、一般複參數的續延分支或其乘重，更不把舊端點 Hölder 空間的譜結論搬到較小指數的新空間。

### 8.1 已核對前提的實幾何鄰域推論

主線在初版保存後明確授權補入本推論。[共同幾何筆記][geometry] §2–4、式 (5)、(16) 的參數為 \(\zeta=(\Delta C_i,\Delta a_i)_{i=1}^3\)，且共同鄰域 \(\Omega=\{\|\zeta\|_{\rm geom}<\eta\}\) 已選取 \(\eta<a/4\) 及 \(\eta<(3\sqrt3-2)a/8\)。必要時縮至 [壓力響應筆記][pressure] §5 的局部全純零點支所在共同鄰域 \(\Omega'\subset\Omega\)，令 \(\Omega'_{\mathbb R}=\Omega'\cap\mathbb R^9\)。

對每個 \(\zeta\in\Omega'_{\mathbb R}\)，障礙物仍為平面上的三個真實圓盤。半徑、跨盤距離及 no-eclipse 間隙分別有

\[
\begin{aligned}
a_i(\zeta)&>3a/4>0,\\
\operatorname{dist}(K_i(\zeta),K_j(\zeta))
&\ge4a-4\eta>3a\quad(i\ne j),\\
\operatorname{dist}\bigl(K_i(\zeta),
  \operatorname{conv}(K_j(\zeta)\cup K_k(\zeta))\bigr)
&\ge(3\sqrt3-2)a-4\eta>0
\quad(i,j,k\ {\rm distinct}).
\end{aligned}
\tag{36}
\]

所以每個實參數下都有三個不相交、緊緻、嚴格凸、光滑邊界的平面障礙物，满足來源的 no-eclipse 條件。平面 pinching (P) 自動成立；因此 [Stoyanov 的同一 Theorem 6.3／Corollary 6.4][classical-source] 可在每個這樣的實參數上個別應用，不需要以待證 h 身份補足任何來源前提。

[共同幾何筆記][geometry] §4–5、§7 已另行保持 nongrazing、全部雙側編碼的唯一真實首次飛行實現、\(3a\le\tau_\zeta\le9a\)，以及 \(2a\le\widehat g_\zeta\le10a\) 和保週期共邊界。[壓力響應筆記][pressure] §3 在同一較小 Hölder 空間上對每個實 \((t,\zeta)\) 給出 RPF。故本頁 §2–6 可逐點重用：令 \(D_\zeta=[\widehat g_\zeta]_\beta q/(1-q)\)，closing 代價仍為 \(e^{|t|(D_\zeta+10a)}\)，三組上界不變，RPF 比例 \(C_{t,\zeta}\) 允許依賴參數；§5 的物理最小週期下界改用 \(\ell_*=6a\)，而不是把基準的 8a 沿用到整個鄰域。

令 \(h_T(\zeta)\) 為該實幾何下原單位速率物理流熵。對每個固定實 \(\zeta\)，来源給出相應的 primitive 計數漸近和 \(h_T(\zeta)>0\)。同一正項級數的兩個收斂集合相等，因而

\[
\boxed{h(\zeta)=h_T(\zeta),\qquad
\lambda(h_T(\zeta),\zeta)=1
\quad(\zeta\in\Omega'_{\mathbb R}).}
\tag{37}
\]

這是逐點身份。來源的延拓邊界 \(c_0(\zeta)<h_T(\zeta)\)、計數誤差指數 \(c(\zeta)\)、隱含常數和漸近起點均不要求跨 \(\zeta\) 一致；本推論沒有從逐點漸近交換出參數微分或一致高頻估計。

由 (37)，[壓力響應筆記][pressure] 已建立的實解析 \(h(\zeta)\) 現在才可稱為該真實物理熵的實解析響應。其局部複全純延拓仍只是解析分支，不在複幾何上定義物理熵。本頁不進一步合成具體 shape 導數或自然雙側測度公式，也不聲稱幾何參數一致的高頻、source strip 或全平面結論。

## 9. 證據邊界與實際操作

新增接口為「實 RPF 主值 → 具體週期和增長／收斂集合 → 同一物理 primitive 計數 → 物理熵」。既有經典來源不是本頁新定理；本案配接推導也沒有被標記為外部獨立認證、形式化證明或研究新穎性結論。

沒有核性、trace-class、ordinary trace、Fredholm determinant、量子 determinant、Hilbert–Pólya 算子、其域或全局 determinant equality；沒有完整固定 Hölder 空間的高頻估計或新的全平面延拓。原 A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION、Gate 6 NOT_ACTIVATED、Stage 5／6 停止條件與歷史失敗記錄保持不變。

本次按已選 ARS 有限 argument-builder 指引，明列來源責任、配接合法性、重數、臨界發散及跨空間限制。完整讀取 [固定頻率譜筆記][fixed-frequency]、[幾何響應筆記][pressure]，使用前一已完成輪完整建立的 [同軌道筆記][classical] 與 [舊一側 roof 筆記][old-roof]。主線追加 §8.1 授權後，另完整讀取 [共同幾何筆記][geometry]，核對所用實幾何間隙、首次飛行／唯一編碼、roof 界及共邊界。另有同模型唯讀席檢查配接與正項重排，未以其同意冒稱獨立科學證據。

原 RPF 來源的 Cambridge PDF 本次直接讀取逾時；隨後成功核讀 [arXiv:1703.04276v1][rpf] §1 的空間定義及 Theorem 2.1(a)。沒有將逾時當作成功、沒有訪問受限全文或上傳私人材料。物理 prime-orbit 來源沿用前一輪已實際核讀的 [arXiv:0911.5000v4, Corollary 6.4][classical-source]；不新增 suspension 熵文獻。

寫前確認本目標不存在，以 apply_patch 僅建立本新檔。初版保存後完成一輪最小靜態檢查；主線隨後追加鄰域推論授權，僅在本新檔加入 §8.1 及相應引用／範圍說明，再對變更後的本檔作必要靜態複查。檢查限於控制字元、尾空白、衝突標記、公式分隔與編號、本地引用目標及 SHA-256；不運行科學、符號或數值程式、軌道枚舉、實驗、producer、稿件構建或正式驗證器。靜態檢查只管檔案完整性，不認證數學成立性。

[old-roof]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[fixed-frequency]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_fixed_frequency_spectral_gap_20260909.md
[pressure]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_pressure_zero_geometry_response_20260909.md
[classical]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_classical_zeta_continuation_same_orbits_20260909.md
[geometry]: /root/autodl-tmp/flow_systems/papers/30-three-disk-nonconstant-roof-determinant/notes/internal_goal01_joint_geometry_holomorphy_20260909.md
[rpf]: https://arxiv.org/pdf/1703.04276v1
[classical-source]: https://arxiv.org/pdf/0911.5000v4
