# P30 Goal01：由 cylinder 逼近取得整個固定 Hölder 空間的高頻界

日期：2026-09-09 UTC。主線先授權有界只讀推導，隨後明確授權將已完成的鏈保存為本獨占新檔。只新增本檔，不改舊筆記、現稿、程式、資料、鎖定輸入、歷史失敗紀錄或正式狀態。

## 0. 結論、範圍與證據責任

固定原等邊三圓盤、半徑 \(a>0\)、中心距 \(6a\)、單位歐氏速率及逐碰撞時鐘。全篇使用[一側 roof 筆記][roof]的同一個正 roof \(g\)、同一個符號度量與端點指數 \(\beta\)，不是幾何響應筆記的另一個 roof 或較小指數空間。

令

\[
\mathcal B_\beta=C^\beta(\Sigma_{\rm N}^+,d_\theta^+;\mathbb C),
\qquad q=\theta^\beta\in(0,1),
\]
\[
(\mathcal L_s^g u)(x)=\sum_{j\ne x_0}e^{-s g(jx)}u(jx),
\qquad
T_s=\lambda_t^{-1}\mathcal L_s^g,
\quad s=t+ib,\quad t\in\mathbb R,
\tag{1}
\]

其中 \(\lambda_t>0\) 是同一實算子的 RPF 主值。寫

\[
B=|b|,\qquad
\|u\|_{\beta,B}=\|u\|_\infty+B^{-1}[u]_\beta.
\tag{2}
\]

存在包含物理熵 \(h_T\) 的閉實區間 \(I\)、常數 \(B_0\ge e^2\)、\(C_*\ge1\)、\(K>0\)、\(c>0\)，使

\[
\boxed{
\|T_s^n\|_{\beta,B\to\beta,B}
\le C_*\min\{1,B^K e^{-cn}\}
\quad(t\in I,\ B\ge B_0,\ n\in\mathbb N_0).
}
\tag{3}
\]

特別地，這是**整個原固定 \(\mathcal B_\beta\)** 的結論。\(B\)-加權只更換同一空間上的等價範數，沒有改 roof、指數、符號度量或測試函數集合。由 (3) 還得到任意 \(0<\delta\le K\) 的

\[
\|T_s^n\|_{\beta,B\to\beta,B}
\le C_* B^\delta e^{-c\delta n/K},
\tag{4}
\]

以及歸一化逆算子

\[
\boxed{
\|(I-T_s)^{-1}\|_{\beta,B\to\beta,B}
\le C_R(1+\log B).
}
\tag{5}
\]

這些是本檔的後繼推論，不是把 Petkov–Stoyanov 原 Theorem 4 直接改寫成全符號空間定理。原定理的附加曲率勢必須分開處理；本檔從其 **Theorem 3 的零附加勢**重走純 roof 算子接口。也不聲稱恢復來源固定衰減常數、從第一個 \(\lfloor\log B\rfloor\) 塊即成立的原式。

責任分層如下：

- **既有本案證明：** 雙向物理編碼、全 trapped 非擦邊、物理 roof 的全局 Lipschitz 界、固定 \(g\) 的明確構造、實 RPF、LY、週期配分和增長率及 \(\lambda_{h_T}=1\)。
- **來源定理輸入：** Petkov–Stoyanov 的指定 Markov family、編碼與乘子身份、平面幾何假設，以及幾何 Lipschitz 空間上的 Theorem 3。
- **本檔補證：** 有限 cylinder 的定量幾何 Lipschitz 界、純 roof 對接、原 \(\beta\) 的帶頻率逼近、全部迭代時間的 (3)，及 (4)–(5)。

所有常數均為解析存在性／粗上界，沒有實測或數值擬合。幾何始終固定；沒有幾何參數族的一致性斷言。全篇沒有建立 \((I-\mathcal L_s^g)^{-1}\) 的非歸一化條帶結論，也沒有散射或量子 resolvent 身份。

## 1. 固定的符號 roof、標準過去與有限共邊界

\(\Sigma_{\rm N}\) 是三字母、相鄰不等的雙向自然障礙物碼，\(\Sigma_{\rm N}^+\) 是其單側版本。\(\pi_{\rm N}\) 刪去負座標；\(\sigma\) 表示相應左移。實際逐碰撞 roof 為 \(\tau\)，滿足 \(4a\le\tau\le8a\)。

依[一側 roof 筆記][roof] §2，標準過去 \(R x\) 保留全部非負座標，負座標在 \(x_0\) 與 \(b(x_0)\) 間交替，其中

\[
b(1)=2,\qquad b(2)=b(3)=1.
\]

已證一致收斂的級數及單側化是

\[
h(x)=\sum_{j\ge0}
  [\tau(\sigma^j x)-\tau(\sigma^j R x)],
\qquad
f^+\circ\pi_{\rm N}=\tau-h+h\circ\sigma.
\tag{6}
\]

同一筆記固定與 \(s\) 無關的正整數 \(m_*\)，並令

\[
g=\frac1{m_*}\sum_{j=0}^{m_*-1}f^+\circ\sigma^j,
\qquad 2a\le g\le10a,
\]
\[
v=\frac1{m_*}\sum_{j=0}^{m_*-2}(m_*-1-j)f^+\circ\sigma^j,
\qquad
g=f^+-v+v\circ\sigma.
\tag{7}
\]

這裡 \(f^+,g,v\in\mathcal B_\beta\)，\(v\) 實值且固定。既有端點指數為原雙側 Hölder 指數的一半；本檔不再降指數。符號超距離下的 \(\beta\) 不須被解釋為歐氏 Hölder 指數。

定義 \(\mathcal L_s^{f^+}\) 時只將 (1) 的 \(g\) 換成 \(f^+\)。直接把 (7) 代入每個前像權重，對全部 \(n\ge0\) 得到

\[
\boxed{
(\mathcal L_s^g)^n
=M_{e^{-sv}}(\mathcal L_s^{f^+})^nM_{e^{sv}}.
}
\tag{8}
\]

這是同一單側空間上的顯式乘子身份，不是由同週期和反推尚未證明的 Livšic 共邊界。有限平均沒有將一次迭代改成 \(m_*\) 次碰撞。

## 2. 來源 family 的定義域、邊界、穩定葉與時鐘

本檔來源為 Petkov–Stoyanov，*Correlations for pairs of periodic trajectories for open billiards*，*Nonlinearity* **22** (2009), 2657–2679；實讀[作者稿 `correl10.pdf`][ps]。以章節、條件與公式定位，不以本地 PDF 頁碼核驗作證。

採用來源 §2.1 **固定滿足 (a)–(d)** 的 Markov family
\(R_i=[U_i,S_i]\)，\(R=\bigcup_iR_i\)、\(U=\bigcup_iU_i\)。其首次返回為 \(P\)，真實返回時間為 \(\tau_{\rm M}\)，沿局部穩定葉投影後的映射為 \(\widetilde\sigma:U\to U\)。來源 (c) 避免相對邊界重碼；(d) 明定每次 \(x\to P(x)\) **恰有一次反射**。每個 \(R_i\) 位於指定前一次盤 \(p_i\) 和後一次盤之間。

Proposition 2 與 §2.3 提供

\[
\Psi:\Sigma_{\rm M}\longrightarrow R,
\qquad
\psi:\Sigma_{\rm M}^+\longrightarrow U,
\qquad \psi\sigma=\widetilde\sigma\psi,
\]
\[
S:\Sigma_{\rm M}^+\longrightarrow\Sigma_{\rm N}^+,
\qquad S\sigma=\sigma S,
\tag{9}
\]

且上述所需的編碼映射為雙射。來源的回溯映射 \(\omega\) 把自由飛行狀態送到其前一次碰撞後狀態；雙側公式是 \(S=\Phi^{-1}\omega\Psi\)，其中 \(\Phi\) 是自然碼到碰撞狀態的雙射。

來源 §2.3 特選 Markov 過去 \(\widehat e\)，使 \(\Psi\widehat e=\psi\)。因此在 \(U\) 上有精確的自然未來碼身份

\[
J:=S\psi^{-1}
=\pi_{\rm N}\Phi^{-1}\omega|_U.
\tag{10}
\]

§3.1 的 future-only／stable-fibre 論證與式 (3.2) 確保這是單側算子接口；自然碼第 \(j\) 個盤正是第 \(j\) 次 Markov 返回所對应矩形的前一次盤標籤。不能在這個特定 source family 上繼續假定「一次返回可能任意聚合多次碰撞」。但 \(\tau_{\rm M}\) 與碰撞 roof 仍有截面位置引起的共邊界，並非逐點相同。

以下 \(d_U\) 使用來源物理相空間的固定幾何距離。碰撞空間另用

\[
d_a((q_1,w_1),(q_2,w_2))
=|q_1-q_2|+a|w_1-w_2|,
\tag{11}
\]

其中 \(w_i\) 是單位速度；\(a\) 只是固定尺度下的量綱平衡，沒有改動物理時鐘。

## 3. 本案幾何補證：碰撞映射、回溯映射及 cylinder

### 3.1 碰撞映射在整個 trapped 碰撞集上的有限 Lipschitz 界

記碰撞後 trapped 集為 \(T_{\rm coll}\)，碰撞映射為 \(\mathsf B\)，以避免與頻率 \(B\) 混淆。[非擦邊筆記][nongrazing] §5.4 式 (27) 已在全體 \(T_{\rm coll}\) 上證明

\[
|\tau(x)-\tau(y)|\le105d_a(x,y),
\qquad 4a\le\tau\le8a.
\tag{12}
\]

寫下一碰撞點為 \(q'=q+\tau(x)w\)。對任意兩點，

\[
|q'_x-q'_y|
\le |q_x-q_y|+8a|w_x-w_y|+|\tau(x)-\tau(y)|
\le113d_a(x,y).
\tag{13}
\]

若下一碰撞位於同一盤，法向 \(n=(q'-c_i)/a\)，反射矩陣為
\(R_n=I-2nn^{\mathsf T}\)。由
\(\|R_n-R_{\widetilde n}\|\le4|n-\widetilde n|\)，

\[
\begin{aligned}
d_a(\mathsf Bx,\mathsf By)
&\le5|q'_x-q'_y|+a|w_x-w_y|\\
&\le566d_a(x,y).
\end{aligned}
\tag{14}
\]

若下一盤不同，當下盤相同時，[非擦邊筆記][nongrazing] §5.2 式 (24) 給速度間隔
\(\epsilon_*=(2\sqrt2-\sqrt3)/3>1/3\)，所以 \(d_a(x,y)\ge a\epsilon_*\)；當下盤不同時則 \(d_a(x,y)\ge4a\)。像空間的直徑至多 \(8a+2a=10a\)，故此時可用常數 \(30\)。綜合得到

\[
\boxed{d_a(\mathsf Bx,\mathsf By)\le Ld_a(x,y)
\quad(x,y\in T_{\rm coll})}
\tag{15}
\]

的某個固定有限 \(L\ge1\)；在 (11) 的距離中，\(L=566\) 是可用的粗選擇。本檔不依賴其數值。若改用加權歐氏平方和距離，須以固定範數等價因子放大 \(L\)，不能直接沿用同一數字。

這個全局界的關鍵是非擦邊與分支間的正間隔，不是宣稱一般有奇點的 billiard map 在整個相空間上光滑。

### 3.2 回溯到前一次碰撞的全局有限常數

來源 §2.3 將 \(\omega(p,w)=(q,w)\) 定義於 \(p=q+\ell w\)、\(w\cdot\nu(q)>0\) 的相應自由飛行分支，並給出其光滑性。此處只需要其在 \(U\) 上的限制。

每個 \(U_i\) 緊：它是緊 Markov 單側首字母 cylinder 經連續映射 \(\Psi\widehat e=\psi\) 的像。不同 \(R_i\) 由來源 §2.1(b) 在時間零即互不相交，故不同 \(U_i\) 也是有限個互不相交緊集，跨片距離有正下界。

在每個片上的回溯根，由已證非擦邊可用隱函數定理延拓到局部光滑分支。對這些局部鄰域取有限覆盖和 Lebesgue number，得到近點對的共同導數上界；對不夠近的點對，用像集直徑除以固定正距離。再合併有限個片及跨片間隔，得到

\[
\boxed{d_a(\omega x,\omega y)\le C_\omega d_U(x,y)
\quad(x,y\in U)}
\tag{16}
\]

的固定有限 \(C_\omega\)。此論證只要求有限常數，沒有為未指定的 Markov family 報出虛構數值，也沒有要求符號編碼的逆映射直接在原 \(\beta\) 下為 Lipschitz。

### 3.3 每個有限未來 cylinder 均可用，且代價至多指數增長

設 \(u_m\) 在自然碼長度 \(m\ge1\) 的 cylinders 上常值，索引為 \(0,\ldots,m-1\)。若 \(Jx\)、\(Jy\) 位於不同的此類 cylinders，存在 \(0\le j<m\) 使第 \(j\) 個盤不同。由盤間距、(10)、(15)–(16)，

\[
4a\le d_a(\mathsf B^j\omega x,\mathsf B^j\omega y)
\le L^jC_\omega d_U(x,y)
\le L^{m-1}C_\omega d_U(x,y).
\tag{17}
\]

若兩碼在同一 cylinder，函數差為零；否則用 \(2\|u_m\|_\infty\) 控制差值。因此

\[
\boxed{
u_m\circ J\in C_{\rm Lip}(U),\qquad
\operatorname{Lip}(u_m\circ J)
\le\frac{C_\omega}{2a}L^{m-1}\|u_m\|_\infty.
}
\tag{18}
\]

這是對複值 cylinder 也成立的差商估計。若 cylinder 從下一盤 \(1\) 而不是當前盤 \(0\) 起算，右側改為 \(L^m\)。以下統一選 \(\kappa>0\) 及 \(C_{\rm cyl}\ge1\)，使

\[
\|u_m\circ J\|_{{\rm Lip},B}
\le C_{\rm cyl}(1+B^{-1}e^{\kappa m})\|u_m\|_\infty,
\quad
\|F\|_{{\rm Lip},B}:=\|F\|_\infty+B^{-1}\operatorname{Lip}(F).
\tag{19}
\]

例如可將 \(L\) 放大至至少 \(e\)，再取 \(\kappa=\log L\)。有限字母與緊緻性本身只保證每個固定深度的正分離；(17) 的指數尺度另外使用了碰撞映射的有限全局 Lipschitz 常數。

## 4. 純 roof 幾何高頻輸入：不能直接刪除原 Theorem 4 的曲率勢

來源 §3.3 的 Theorem 3 允許任意符合其 Lipschitz 條件的實附加勢。此處取

\[
q_{\rm src}=0.
\]

來源所列平面假設 (P)、(NF)、(ND) 均在同節明說對 \(N=2\) 成立；(P) 後另據其所引 regularity 結果，給 stable 與 unstable laminations 的 Lipschitz 正則性。圓盤的光滑、嚴格凸、分離及 no-eclipse 已由固定幾何核對。這些是可引用的幾何定理输入，不是由符號兩分支矩陣的混合性代替。

記幾何算子為

\[
(\mathscr G_s F)(x)
=\sum_{\widetilde\sigma y=x}e^{-s\tau_{\rm M}(y)}F(y),
\tag{20}
\]

並記 Markov 符號 roof 為 \(r_{\rm M}=\tau_{\rm M}\circ\psi\)。固定有界實部窗口 \(A_*>|h_T|+1\)。Theorem 3 的零勢版本給某個 \(\sigma_0<s(0)\)、\(0<\varrho<1\)、\(C_{m src}<\infty\)，對來源實部範圍及

\[
B\ge e^2,\quad k_B=\lfloor\log B\rfloor\ge2,
\qquad n=p k_B+\ell,\quad p\ge1,\quad0\le\ell<k_B,
\]

有

\[
\|\mathscr G_s^nF\|_{{\rm Lip},B}
\le C_{\rm src}\varrho^{p k_B}
 e^{\ell P_{\rm M}(-t r_{\rm M})}
 \|F\|_{{\rm Lip},B}.
\tag{21}
\]

實部範圍為 \(t\ge\sigma_0\)、\(|t|\le A_*\)；\(s(0)\) 是 \(P_{\rm M}(-s(0)r_{\rm M})=0\) 的零點。下文將以本案週期配分和識別 \(s(0)=h_T\)。

為接到自然 roof，使用來源 §§3.1–3.2 的時間共邊界計算，但令所有附加勢及其共邊界為零。具體地，\(\lambda(x)\) 記從前一次碰撞到截面 \(x\) 的飛行時間，依來源符號令

\[
h_s(x)=e^{-s\lambda(x)},
\qquad
d_s(x)=\exp\{s[\lambda([x,y_p])-\lambda(x)]\},
\qquad x\in U_i,\ p=p_i.
\tag{22}
\]

\(y_p\) 使用與自然碼標準過去相應的參照不穩定葉。來源 §2.2 允許逐首盤任選固定過去；本檔選為 §1 同一交替過去。所以來源的 \(e\) 就是 \(R\)，其 \(\chi_f\) 與 (6) 的 \(h\) 逐項相同，\(\widetilde f=f^+\)。不用週期資料反推這個等式。

來源式 (3.4)、(3.7)、(3.9) 在零附加勢下，與一般權重乘子恆等式合併，對任意連續 \(u\) 給

\[
\boxed{
\bigl((\mathcal L_s^{f^+})^nu\bigr)\circ J
=\frac{d_s}{h_s}\,
  \mathscr G_s^n\left(\frac{h_s}{d_s}(u\circ J)\right).
}
\tag{23}
\]

這就是 Proposition 4／(3.13) 的**零附加勢重推版本**。原 Theorem 4 的曲率比值項沒有被冒認為本案的零勢。

來源 Lemma 1 的論證以 \(\lambda\) 的光滑性及相關 bracket 的一致 Lipschitz 性控制 (22)。對有界實部和 \(B\ge e^2\)，

\[
\left\|\frac{h_s}{d_s}\right\|_\infty+
\left\|\frac{d_s}{h_s}\right\|_\infty\le C_A,
\qquad
\operatorname{Lip}\left(\frac{h_s}{d_s}\right)+
\operatorname{Lip}\left(\frac{d_s}{h_s}\right)\le C_A B.
\tag{24}
\]

因此兩個乘子在 \(\|\cdot\|_{{\rm Lip},B}\) 下均一致有界。將 (21) 代入 (23)，對 \(u\circ J\in C_{\rm Lip}(U)\) 得

\[
\left\|\bigl((\mathcal L_s^{f^+})^n u\bigr)\circ J
\right\|_{{\rm Lip},B}
\le C\varrho^{n-\ell}
 e^{\ell P_{\rm M}(-t r_{\rm M})}
 \|u\circ J\|_{{\rm Lip},B}.
\tag{25}
\]

Theorem 3 已允許複值 observable；即便僅使用實值表述，拆實虛部也只增加固定常數。此處 (25) 仍是受限測試函數類的估計，尚未宣稱整個 \(\mathcal B_\beta\) 都是物理 Lipschitz。

## 5. source pressure、\(\lambda_t\) 與物理熵是同一個量

來源的指定 family 保持逐碰撞步數，而截面位置與 (6)–(7) 的共邊界在週期點上望遠鏡相消。由 \(S\) 的雙射和移位交換，對每個 \(n\) 的完整固定點和有

\[
\sum_{\sigma^n\xi=\xi,\ \xi\in\Sigma_{\rm M}^+}
 e^{-t S_n r_{\rm M}(\xi)}
=\sum_{\sigma^nx=x,\ x\in\Sigma_{\rm N}^+}
 e^{-t S_n f^+(x)}
=\sum_{\sigma^nx=x}e^{-tS_ng(x)}
=:W_n(t).
\tag{26}
\]

這裡不按 primitive orbit 取商，也沒有有限對一 Markov 重碼修正；所用的是來源特選 family 的雙射。

[壓力等於物理熵筆記][entropy] §3 已對固定 \(g\) 證明

\[
E_t\lambda_t^{n-1}\le W_n(t)\le U_t\lambda_t^n
\quad(n\ge2),\qquad
\lim_{n\to\infty}\frac1n\log W_n(t)=\log\lambda_t.
\tag{27}
\]

來源 §3.3 式 (3.15) 前的週期配分和壓力公式，結合 (26)–(27)，給

\[
\boxed{P_{\rm M}(-t r_{\rm M})=\log\lambda_t.}
\tag{28}
\]

再使用既有 \(\lambda_h=1\iff h=h_T\) 得 \(s(0)=h_T\)。此識別不以本檔高頻估計為前提：上游熵辨認已由原始週期軌道雙射與經典計數完成，沒有循環使用 (3)。

## 6. 實 RPF 給全部時間的弱界，LY 給全部時間的加權強界

對每個實 \(t\)，[固定頻率筆記][fixed] §2 提供同一 \(\mathcal B_\beta\) 中的正本徵函數 \(H_t\)，

\[
\mathcal L_t^gH_t=\lambda_tH_t,
\qquad \min H_t>0.
\tag{29}
\]

在任意固定實緊区間內，可使 \(\max H_t/\min H_t\) 局部一致有界，再取有限覆蓋。具體理由是：簡單孤立實本徵值附近取共軛對稱的 Riesz 圍道，算子範數連續性使投影连续且保持實函數；將投影作用於當地正 \(H_{t_0}\)，在足夠小實鄰域仍嚴格正。其本徵值由 RPF 識別為 \(\lambda_t\)。這與[低頻筆記][lowfreq] §7.1 的同一局部規範一致，不需要先建立高頻結果。

故在稍後固定的 \(I\) 上，正性給

\[
\|\mathcal L_t^{g,n}1\|_\infty\le C_I\lambda_t^n
\quad(n\ge0).
\tag{30}
\]

例如以 \(H_t^{-1}T_sM_{H_t}\) 做實 RPF 規範，零虛部是 Markov 算子，複權模不超過實轉移機率，因而其全部冪在 sup 範數為收縮。轉回原規範即

\[
\boxed{\|T_s^n u\|_\infty\le C_I\|u\|_\infty
\quad(n\ge0).}
\tag{31}
\]

沒有假定 \(H_t\circ J\) 物理 Lipschitz，也沒有將 \(T_s\) 本身誤稱為 sup 收縮。

由[一側 roof 筆記][roof]式 (24) 的 LY 界，記固定 distortion 常數為 \(D_g\)，

\[
\|T_s^nu\|_\beta
\le C_I\bigl(q^n[u]_\beta+(3+2|s|D_g)\|u\|_\infty\bigr)
\quad(n\ge1).
\tag{32}
\]

因 \(|t|\le A_*\)、\(B\ge e^2\)，\(|s|/B\) 有一致上界。結合 (31) 並以恆等算子補入 \(n=0\)，得到

\[
\boxed{
\|T_s^nu\|_{\beta,B}
\le C_{m LY}\left(q^n B^{-1}[u]_\beta+\|u\|_\infty\right),
\qquad
\|T_s^n\|_{\beta,B\to\beta,B}\le C_{m LY}
\quad(n\ge0).
}
\tag{33}
\]

這裡後一個界是全部時間的一致有界性，尚不是相消衰減。

另外，由 (8)、(31) 及 \(|e^{\pm sv}|\le e^{A_*\|v\|_\infty}\)，純 roof 規範
\(\widetilde T_s=\lambda_t^{-1}\mathcal L_s^{f^+}\) 也滿足

\[
\boxed{\|\widetilde T_s^n u\|_\infty\le C_f\|u\|_\infty
\quad(n\ge0).}
\tag{34}
\]

因此後文的逼近誤差不會帶出未控制的 \(\lambda_t^n\) 或逐步增長常數。

## 7. 選定 \(h_T\) 附近的實窗口並規範來源衰減

先按 §4 固定 \(A_*\) 並取得來源 \(\sigma_0<h_T\)、\(\varrho<1\)。既有 \(t\mapsto\lambda_t\) 连續且 \(\lambda_{h_T}=1\)，所以可選 \(\eta>0\)，使

\[
I=[h_T-\eta,h_T+\eta]
\subset(\sigma_0,\infty)\cap(-A_*,A_*),
\qquad
\lambda_-:=\inf_{t\in I}\lambda_t>\varrho.
\tag{35}
\]

定義

\[
\chi=\frac{\varrho}{\lambda_-}\in(0,1),
\qquad d=-\log\chi>0.
\tag{36}
\]

這是靠近 \(h_T\) 的固定小區間，不是任意給定實緊集的結論。若需要較大的實區間，須另作相應來源與規範的分析。

對 \(n\ge k_B\) 的來源分塊，(25)、(28) 給

\[
\lambda_t^{-n}\varrho^{n-\ell}
e^{\ell P_{\rm M}(-t r_{\rm M})}
=\left(\frac{\varrho}{\lambda_t}\right)^{n-\ell}
\le\chi^{n-\ell}
\le B^d e^{-dn},
\tag{37}
\]

因 \(0\le\ell<k_B\le\log B\)。取 (19) 的 cylinder \(u_m\)，由 \(J\) 雙射，sup 範數保留，從而

\[
\boxed{
\|\widetilde T_s^n u_m\|_\infty
\le C B^d e^{-dn}(1+B^{-1}e^{\kappa m})\|u_m\|_\infty
\quad(n\ge k_B).
}
\tag{38}
\]

此處的 \(B^d\) 只是將來源剩餘短塊 \(\ell\) 吸收進全時間記法的代價。尚未處理 \(p=0\)，即 \(n<k_B\) 的區段。

## 8. 逼近整個共邊界乘子後的輸入，而非預設其物理 Lipschitz 性

對 \(w\in\mathcal B_\beta\)，每個自然長度 \(m\) cylinder 固定一個合法延拓代表點，令 \(P_mw\) 在其上取代表點的值。[一側 roof 筆記][roof]式 (26) 給

\[
\|P_mw\|_\infty\le\|w\|_\infty,
\qquad
\|w-P_mw\|_\infty\le q^m[w]_\beta,
\qquad [P_mw]_\beta\le[w]_\beta.
\tag{39}
\]

這裡的有限秩近似不要求在 \(\mathcal B_\beta\) 的強範數收斂；後面只使用弱范數誤差。

對任意 \(u\in\mathcal B_\beta\)，先設

\[
w=e^{sv}u.
\tag{40}
\]

因 \(v\) 實值且固定，乘積差商給

\[
\|e^{\pm sv}\|_\infty\le e^{A_*\|v\|_\infty},
\qquad
[e^{\pm sv}]_\beta
\le |s|e^{A_*\|v\|_\infty}[v]_\beta.
\]

因此乘子 \(M_{e^{\pm sv}}\) 在 (2) 的範數下一致有界，且

\[
\|w\|_\infty\le C_v\|u\|_\infty,
\qquad [w]_\beta\le C_v B\|u\|_{\beta,B}.
\tag{41}
\]

令 \(w_m=P_mw\)。由 (34)、(39)、(41)，對全部 \(n\ge0\)，

\[
\|\widetilde T_s^n(w-w_m)\|_\infty
\le C Bq^m\|u\|_{\beta,B}.
\tag{42}
\]

另一方面，\(w_m\) 是真正 admissible 的 cylinder，可用 (38)。再以 (8) 左端乘子轉回原 \(g\)，對 \(n\ge k_B\) 得

\[
\|T_s^nu\|_\infty
\le C\left[
 B^d e^{-dn}(1+B^{-1}e^{\kappa m})+Bq^m
\right]\|u\|_{\beta,B}.
\tag{43}
\]

這一步沒有聲稱 \(e^{sv}\circ J\)、\(H_t\circ J\) 或任意 \(u\circ J\) 為物理 Lipschitz。被送入來源估計的是整個 \(w\) 的有限 cylinder 近似；共邊界乘子自身的正則性只在原固定符號 \(\beta\) 空間使用。

## 9. 選 \(m\) 隨 \(n\) 線性增長，並補全 \(p=0\) 與 \(n=0\)

置 \(\alpha_q=-\log q>0\)，選一個固定比例

\[
0<\varepsilon_0\le\min\left\{\frac14,\frac{d}{4\kappa}\right\},
\qquad
m(n)=\max\{1,\lfloor\varepsilon_0n\rfloor\}.
\tag{44}
\]

由 \(\varepsilon_0n-1\le m(n)\le\varepsilon_0n+1\)，

\[
q^{m(n)}\le q^{-1}e^{-\alpha_q\varepsilon_0n},
\qquad
e^{\kappa m(n)}\le e^\kappa e^{\kappa\varepsilon_0n}.
\tag{45}
\]

將 (45) 代入 (43)，用 \(B\ge1\) 及 \(\kappa\varepsilon_0\le d/4\)，可放寬為

\[
\|T_s^nu\|_\infty
\le C\left(B^d e^{-dn/2}
       +B e^{-\alpha_q\varepsilon_0n}\right)
\|u\|_{\beta,B}
\quad(n\ge k_B).
\tag{46}
\]

令

\[
c_1=\min\{d/2,\alpha_q\varepsilon_0\}>0,
\qquad
K\ge\max\{d,1,c_1\}.
\tag{47}
\]

\(K\) 可取更大的固定正數，不追求最小頻率損失。對 \(0\le n<k_B\le\log B\)，由 (31) 及

\[
B^K e^{-c_1 n}\ge B^{K-c_1}\ge1,
\tag{48}
\]

同一形式亦成立。因而長、短時間合併為

\[
\boxed{
\|T_s^nu\|_\infty
\le C_{m weak}B^K e^{-c_1n}\|u\|_{\beta,B}
\quad(n\ge0).
}
\tag{49}
\]

短時段完全使用實 RPF 的共同弱界，沒有把來源未覆蓋的 \(p=0\) 假裝包含在 (21) 中。\(B_0\ge e^2\) 也確保 \(k_B\) 不會退化為零。

## 10. 用兩段 LY 把弱衰減提升到原 \(\beta\) 強範數

將任意 \(n\ge0\) 寫成

\[
k=\lfloor n/2\rfloor,\qquad \ell=n-k\ge n/2.
\]

先對最後 \(\ell\) 步用 (33)，得到

\[
\|T_s^nu\|_{\beta,B}
\le C_{m LY}\left(
  q^\ell B^{-1}[T_s^ku]_\beta
  +\|T_s^ku\|_\infty\right).
\tag{50}
\]

第一項使用 (33) 的**全部時間強範數一致有界性**；第二項才使用 (49)。因此

\[
\|T_s^nu\|_{\beta,B}
\le C\left(q^\ell+B^K e^{-c_1k}\right)\|u\|_{\beta,B}
\le C_{m dec}B^K e^{-cn}\|u\|_{\beta,B},
\tag{51}
\]

其中可取

\[
c=\tfrac12\min\{\alpha_q,c_1\}>0.
\tag{52}
\]

奇數 \(n\) 的 \(e^{c_1/2}\) 因子已吸收進固定常數。這個順序沒有用小的 sup 範數直接冒充小的 Hölder 半範數，也沒有要求 \(P_m\) 在強範數近似恆等算子。

將 (51) 與 (33) 合併，取
\(C_*=\max\{1,C_{m LY},C_{m dec}\}\)，即得全部 \(n\ge0\) 的 (3)。每個固定 \(s\) 的所有冪使用同一算子；沒有對變動參數算子乘積作出結論。

## 11. 後繼推論：任意小頻率損失、對數起始時間與歸一化逆算子

### 11.1 任意較小的多項式頻率損失

對 \(x\ge0\)、\(0<r\le1\)，\(\min\{1,x\}\le x^r\)。取
\(x=B^K e^{-cn}\)、\(r=\delta/K\)，即得 (4)。

因此對每個固定 \(0<\delta\le K\)，可寫

\[
\|T_s^n\|_{\beta,B\to\beta,B}
\le C_*B^\delta\rho_\delta^n,
\qquad \rho_\delta=e^{-c\delta/K}\in(0,1).
\tag{53}
\]

\(\delta\) 趨零時，\(\rho_\delta\) 趨近 \(1\)。不能在縮小頻率 prefactor 時聲稱保留原衰減率。

### 11.2 本檔自己的 \(n\ge M\log B\) 結論

取固定 \(M=2K/c\)。若 \(n\ge M\log B\)，则

\[
B^K e^{-cn}\le e^{-cn/2},
\qquad
\|T_s^n\|_{\beta,B\to\beta,B}\le C_*e^{-cn/2}.
\tag{54}
\]

這是本檔證明所得的對數起始時間，其係數 \(M\) 不要求等於來源的 \(1\)。因此沒有把 (54) 標成原 Theorem 4 從第一個來源 log 塊起即成立的原式。

對每個固定 \(B\)，(2) 與原 \(\mathcal B_\beta\) 範數等價，故由 (3) 的冪次根極限還有

\[
r(T_s)\le e^{-c}<1,
\qquad
r(\mathcal L_s^g)\le\lambda_t e^{-c}.
\tag{55}
\]

這個譜界不要求把整个 \(\mathcal B_\beta\) 等同於 source admissible class。

### 11.3 只對 \(I-T_s\) 的 \(O(1+\log B)\) 逆算子界

令

\[
n_0=\left\lceil\frac Kc\log B\right\rceil.
\tag{56}
\]

由 (3)，前 \(n_0\) 項各至多 \(C_*\)，而

\[
\sum_{n\ge n_0}\|T_s^n\|_{\beta,B\to\beta,B}
\le C_* B^K\frac{e^{-cn_0}}{1-e^{-c}}
\le\frac{C_*}{1-e^{-c}}.
\tag{57}
\]

因此 Neumann 級數在同一 Banach 空間的算子範數收斂。有限部分和的左右乘積均為 \(I-T_s^{N+1}\)，而 (3) 使尾冪趨零；所以此級數確實是雙側逆，並給

\[
\begin{aligned}
\|(I-\lambda_t^{-1}\mathcal L_{t+ib}^g)^{-1}\|_{\beta,B\to\beta,B}
&\le C_*\left(
 \left\lceil\frac Kc\log B\right\rceil
 +\frac1{1-e^{-c}}\right)\\
&\le C_R(1+\log B).
\end{aligned}
\tag{58}
\]

這裡 \(\lambda_t\) 依賴 \(t=\operatorname{Re}s\)；本檔沒有因此聲稱歸一化族在複 \(s\) 下全純。尤其不能把 (58) 的逆算子直接換成 \((I-\mathcal L_s^g)^{-1}\)，更不能換成物理散射 resolvent。

## 12. 常數依賴、歷史邊界及實際核查

所有 \(C\)、\(L\)、\(C_\omega\)、\(\kappa\)、\(\varrho\)、\(d\)、\(K\)、\(c\)、\(M\) 可依賴固定三盤幾何、選定 source family、固定標準過去、\(m_*\)、\(g\)、\(\theta,\beta\)、實部窗口及最後選定的 \(I\)。它們不依賴 \(t\in I\)、\(b\) 的符號、\(B\ge B_0\)、\(n\)、輸入函數或 cylinder 深度。式 (18)–(19) 已將深度依賴顯式分離為 \(L^{m-1}\)／\(e^{\kappa m}\)。

[先前高頻來源接口筆記][interface]保存的是當時尚未建立 cylinder 定量橋和弱／強範數轉移時的邊界；本檔提供其後繼證明，不回寫或抹除歷史狀態。來源對整個符號函數類直接適用性的警告仍須尊重：本檔既不宣稱所有符號 Hölder 函數都是幾何 Lipschitz，也不以特徵值身份代替冪範數推導。

本輪用 ARS 的同階段論證整合與 Devil's Advocate 方式，明確查核了純 roof／曲率勢區分、同一標準過去、返回時鐘、\(p=0\) 短段、兩半 LY 的順序及 normalized／non-normalized 的界線。來源事實由遠端作者稿正文核讀；本案新幾何估計與抽象逼近另經同模型家族有界分工與主線推算。這不是外部独立科學再現或正式 Gate 證書。

本檔作者實際讀取了 source §§2.1–3.3 的相關定義、(3.2)、(3.4)、(3.7)、(3.9)、(3.13)、Lemma 1、Theorem 3 和 Theorem 4 正文，並核讀所引用本地非擦邊 §5、固定 roof 構造／LY、實 RPF、壓力配分和及低頻一致化證明。沒有下載本地 PDF 或聲稱執行本地 PDF 頁碼 preflight；定位使用可見的章節／式號。

保存採 `apply_patch` 唯一新增本檔，並作一次針對新檔的最小靜態文字檢查；不運行科學或符號程式、軌道枚舉、數值實驗、producer、checker、稿件構建或正式 Route 審核。沒有變更原時鐘、Route verdict、其他筆記或目標空間。

[roof]: internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[nongrazing]: internal_uniform_nongrazing_on_trapped_collisions_20260908.md
[fixed]: internal_goal01_fixed_frequency_spectral_gap_20260909.md
[entropy]: internal_goal01_pressure_equals_physical_entropy_20260909.md
[lowfreq]: internal_goal01_positive_variance_and_low_frequency_branch_20260909.md
[interface]: internal_goal01_geometric_high_frequency_source_interface_20260909.md
[ps]: https://www.math.u-bordeaux.fr/~vpetkov/publications/correl10.pdf
