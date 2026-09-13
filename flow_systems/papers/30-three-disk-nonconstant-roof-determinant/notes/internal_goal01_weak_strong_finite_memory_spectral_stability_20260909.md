# P30 Goal01：固定 Hölder 空間的雙范數有限記憶譜穩定性

日期：2026-09-10 UTC；檔名沿用主線指定的 Goal01 命名。範圍：本輪明確授權下唯一新增的內部理論筆記，只處理 Keller–Liverani（KL）假設、有限記憶商譜、孤立譜投影及其秩。不改舊檔、幾何、物理時鐘、roof、beta、底空間或正式狀態，不執行科學程式或枚舉。

## 0. 所補舊義務與準確結論

[原路線圖][roadmap] §4.3–4.4 要求把有限表示與同一算子對接，並給 rank／projection 誤差接口。[roof-input][input] §8 已指出：既有有限記憶 `g_m=P_mg` 只有 sup 誤差趋零，不能直接套用強范數小擾動門檻。本篇補的是同一固定 Banach 空間上、使用既有強／弱兩個范數的譜穩定接口。

在物理熵 h 附近選定一個實小窗口，並固定有限複參數窗口後，下文證明：

- `L_s^[m] -> L_s` 在 `B_beta -> C^0` 的混合算子范數收斂，所有近似共同滿足 KL 的實際假設。
- 對固定 s，位於共同本質譜上界之外的孤立譜有 KL 混合范數定量穩定性，包含代數重數。
- 對所明列的緊 `(s,zeta)` resolvent 集有統一可逆性、固定強范數逆界及定性的局部一致混合收斂；共同小圍道上的投影也局部一致混合收斂，秩保持。
- 有限記憶全算子一般不是有限秩，但 `|zeta|>q lambda_(t,m)` 的整個谱及代數重數與既有有限矩陣 `A_m(s)` 完全相同。

本篇不證明強范數擾動趋零，不將任何固定點 t 或固定 s 的結論自動升級到無限頻段，也不處理物理參數 s 的零點橋、完整 determinant 收斂或五通道總誤差。

## 1. 原固定物件與原有有限記憶近似

始終使用[一側 roof 筆記][roof]中的原三圓盤、半徑 a>0、盤心距 6a、單位速率、自然盤碼、固定標準過去及正代表 g。令

\[
\Sigma^+=\{x\in\{1,2,3\}^{\mathbb N_0}:x_j\ne x_{j+1}\},
\qquad q=\theta^\beta\in(0,1),
\]
\[
\mathcal B=\mathcal B_\beta=C^\beta(\Sigma^+,d_\theta;\mathbb C),
\quad |u|:=\|u\|_\infty,\quad
\|u\|:=\|u\|_\infty+[u]_\beta,
\quad [u]_\beta=\sup_{x\ne y}\frac{|u(x)-u(y)|}{q^{N(x,y)}}.
\tag{1}
\]

N 是首個不同座標的位置。弱范數只是在相同 B 上的 sup 范數；不把算子譜改算在 `C^0` 的完備化上。對有界強算子定義

\[
|||Q|||:=\sup_{\|u\|\le1}|Qu|.
\tag{2}
\]

每個深度 m 的柱集代表在 s 變化前固定。沿用[有限記憶筆記][memory] §1、§4 的 `P_m`、`F_m=ran P_m`、`g_m=P_mg` 及

\[
\begin{gathered}
2a\le g,g_m\le10a,\qquad G=[g]_\beta,\qquad
\epsilon_m:=Gq^m,\\
|g_m-g|\le\epsilon_m,\qquad [g_m]_\beta\le G,\\
(\mathcal L_s^{[m]}u)(x)=\sum_{j\ne x_0}e^{-s g_m(jx)}u(jx),\qquad
A_m(s)=\mathcal L_s^{[m]}\big|_{\mathcal F_{m-1}}\quad(m\ge2).
\end{gathered}
\tag{3}
\]

`L_s` 的定義以真實正代表 g 取代 g_m。近似 g_m 一般不保原物理週期，不是 canonical roof；本篇不改其代表選擇。`F_(m-1)` 的不變性來自 g_m 只讀前 m 個符號，不是全算子有限秩的聲明。

## 2. 已實讀的一手 KL 輸入

來源為 G. Keller and C. Liverani, *Stability of the Spectrum for Transfer Operators*, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze (4), 28(1) (1999), 141–152，[原刊全文][kl]。

本次實際讀取原刊 141、142、144、145 頁，以及 149–150 頁的 Corollary 1 證明。浏览器正文抽取先前漏掉展示公式；主線以公開 PDF 的常規閱讀渲染提供圖像，本篇寫者另逐頁查看圖像，沒有把空白截圖或題錄當作公式閱讀。以下對照用原刊式號定位，不以本地 PDF 物理頁序取代印刷頁號。

### 2.1 源假設，不以「KL 可用」作替代

KL §1 的 (1) 就是 (2) 的混合范數。它要求同一 Banach 空間有弱范數 `|u|<=||u||`，並對擾動族 `P_epsilon` 有共同常數 `C_1,C_2,C_3,M>0`、`0<alpha_KL<1`、`alpha_KL<M`，使

\[
|P_\varepsilon^n u|\le C_1M^n|u|,
\tag{4}
\]
\[
\|P_\varepsilon^n u\|
\le C_2\alpha_{\rm KL}^n\|u\|+C_3M^n|u|.
\tag{5}
\]

這分別是源 (2)、(3)。源 (4) 另要求 `|zeta|>alpha_KL` 的譜點不是 residual spectrum；下文以本質譜界及 Fredholm index 為零核實其所需的「單射則滿射」性質。源 (5) 要求

\[
|||P_\varepsilon-P_0|||\le\tau(\varepsilon)\longrightarrow0,
\tag{6}
\]

其中 tau 單調、上半連續，且 epsilon>0 時 tau(epsilon)>0。沒有要求 `epsilon -> P_epsilon` 強范數連續。強單位球的弱緊性列於源 Remark 1(c)，是驗證本質譜條件的充分結構，不是可省略 (4)–(6) 的替代話術。

### 2.2 源結論、范數與秩的區別

對 `delta>0`、`alpha_KL<r<M`，令

\[
V_{\delta,r}(P_0)=
\{\zeta:|\zeta|\le r\ \text{或}\
\operatorname{dist}(\zeta,\operatorname{spec}P_0)\le\delta\},
\qquad
\vartheta=\frac{\log(r/\alpha_{\rm KL})}{\log(M/\alpha_{\rm KL})}>0.
\tag{7}
\]

原刊 Theorem 1 的 (8)、(9) 給充分小擾動及 `zeta notin V` 的強逆界

\[
\|R_\varepsilon(\zeta)u\|
\le a_r\|u\|+b_{\delta,r}|u|,
\quad R_\varepsilon(\zeta)=(\zeta I-P_\varepsilon)^{-1},
\tag{8}
\]

以及混合差界

\[
|||R_\varepsilon(\zeta)-R_0(\zeta)|||
\le\tau(\varepsilon)^\vartheta
 \left(c_{\delta,r}\|R_0(\zeta)\|
      +d_{\delta,r}\|R_0(\zeta)\|^2\right).
\tag{9}
\]

原刊 145 頁明說：常數經由共同 `M,C_1,...,C_4` 依賴算子族，其中 `C_4=C_2+C_3`；擾動門檻和 b 還依賴 tau 及原強 resolvent 的界。不能僅將 pointwise 常數改下標就宣稱 compact-s 一致。

對孤立譜點 lambda，Corollary 1 給相應小圓周的混合投影差趋零，並有同一類譜子空間上的

\[
\|u\|\le K_2|u|\quad(u\in\operatorname{ran}\Pi_\varepsilon),
\tag{10}
\]

包含 epsilon=0；足夠小圓周及擾動下秩相同。Remark 4 識別此秩為孤立有限譜簇的總代數重數。源證明從 (8) 的圍道積分及足夠小圓周得到 (10)，再結合混合投影差；**混合范數接近本身不保證秩相同**。§5 將明寫其本案用法。

## 3. 本案 KL 假設逐項核實

### 3.1 先固定有限複窗口與共同本質譜門檻

[固定空间條帶筆記][strip]給物理熵 h>0、`lambda_h=1`，並給 h 周圍一條已有的 resolvent 條帶。選其中一個閉實小區間 J，使 h 為內點且

\[
\lambda^+:=\max_{t\in J}\lambda_t<1/q.
\tag{11}
\]

這只縮小參數範圍，不改 g 或 B；存在性來自 `lambda_h=1`、q<1 和原實 RPF 主值的連續性。固定

\[
\lambda^+<M<1/q,\qquad
\alpha_{\rm KL}:=qM<1,\qquad
\mathcal W=J+i[-B_f,B_f],\quad B_f<\infty,
\]
\[
A=\max_{t\in J}|t|,\qquad S=\max_{s\in\mathcal W}|s|,
\qquad D=Gq/(1-q).
\tag{12}
\]

因 J 含 h，M>1，可為 ζ=1 的接口選 `alpha_KL<r<1`。任意有限 B_f 可以預先指定，但各常數與 cutoff 可依賴它；沒有無限頻段一致性。

原 RPF 的正特徵函數比較及其在 J 的局部連續規範給固定 `C_0>=1`，滿足

\[
A_n(t):=|\mathcal L_t^n1|\le C_0\lambda_t^n
\quad(t\in J,n\ge0).
\tag{13}
\]

這使用[低頻筆記][low] §7.1 已證的正特徵函數及倒數一致有界，不假定近似 g_m 的 RPF 常數自動一致。由 (3) 的實值誤差，每條 n 步正權有

\[
A_{n,m}(t):=|\mathcal L_t^{[m],n}1|
\le e^{|t|\epsilon_m n}A_n(t).
\tag{14}
\]

選固定 m_0>=2 使 `lambda^+ exp(A epsilon_(m_0))<=M`，則全部 `m>=m_0`、`s in W` 有

\[
A_{n,m}(t)\le C_0M^n.
\tag{15}
\]

原算子也滿足同一上界。

### 3.2 同一 LY 證明給共同強弱常數

[roof] §5 的 n 步配對分支證明只用 `[g]_beta<=G` 與實權模，因此逐式適用於 g_m；其 distortion 常數至多 D。結合 (15) 得

\[
|\mathcal L_s^{[m],n}u|\le C_0M^n|u|,
\tag{16}
\]
\[
\|\mathcal L_s^{[m],n}u\|
\le C_0(qM)^n\|u\|
 +C_0(3+2SD)M^n|u|.
\tag{17}
\]

原 L_s 有完全相同的界。故 (4)、(5) 可取
`C_1=C_2=C_0`、`C_3=C_0(3+2SD)` 與 (12) 的 M、alpha_KL。所有常數與 m、n 無關。這裡使用固定強范數，沒有暗藏 b 加權范數的等價因子。

### 3.3 混合誤差與離散 m 的合法嵌入

設 `e_m=g_m-g`。由 e_m 實值及沿實線段的指數差界，

\[
|e^{-s e_m}-1|
\le |s|\epsilon_m e^{A\epsilon_m},\qquad
\mathcal L_s^{[m]}-\mathcal L_s
=\mathcal L_s M_{e^{-s e_m}-1}.
\tag{18}
\]

每點兩個前像、`2a<=g<=10a`，遂得

\[
|||\mathcal L_s^{[m]}-\mathcal L_s|||
\le2e^{10aA}S e^{A\epsilon_{m_0}}Gq^m
\le C_{\mathcal W}q^m.
\tag{19}
\]

可將 C_W 增至正數以包括 G=0 的形式情況。源 epsilon 參數不必是幾何擾動：epsilon>0 時取最小 `m>=m_0` 使 `q^m<=epsilon`，epsilon=0 時取原算子。用 `tau(epsilon)=C_W epsilon` 即滿足源單調、上半連續及正性要求。每個離散 m 都可由 epsilon=q^m 取得；不要求插值強連續。

固定基點 `s_0 in W` 時還有

\[
|||\mathcal L_s^{[m]}-\mathcal L_{s_0}|||
\le C'_{\mathcal W}\bigl(q^m+|s-s_0|\bigr).
\tag{20}
\]

第二項由固定 g 的有限前像公式對複 s 沿線段積分得到；可取包含该線段的固定有界窗口來定常數。§5 的 compact-s 證明使用 (20)，不假定 (19) 是強范數界。

### 3.4 弱緊性、本質譜與 residual 條件

強單位球的一致有界和共同 `q^N` 模數給弱相對緊性；一致極限仍滿足原范數界，故強閉單位球在 sup 范數下緊。也可由已知 `|u-P_k u|<=q^k[u]_beta` 和有限維柱值盒直接證明全有界性。

更具體地，將 `I-P_k` 代入 g_m 的 n 步 LY，得

\[
\|\mathcal L_s^{[m],n}-\mathcal L_s^{[m],n}P_k\|
\le A_{n,m}(t)\bigl(2q^n+(3+2|s|D)q^k\bigr).
\tag{21}
\]

右側近似算子有限秩。先令 k 趋無窮，再在緊算子商中取 n 次根，與 [roof] §6 的同一證明給

\[
r_{\rm ess}(\mathcal L_s^{[m]})
\le q\lambda_{t,m}\le qM=\alpha_{\rm KL},
\qquad
\lambda_{t,m}:=\lim_{n\to\infty}A_{n,m}(t)^{1/n}.
\tag{22}
\]

這裡 lambda_(t,m) 由正權次乘性存在，並由 (14) 滿足
`lambda_(t,m)<=exp(|t|epsilon_m)lambda_t`；不把它用來重新定義本篇的算子族。原 L_s 同樣有 `r_ess<=alpha_KL`。

`|zeta|>alpha_KL` 時，`zeta I-L_s^[m]` 在 Calkin 意義下 Fredholm；外圓盤是連通的 Fredholm 區域，並連到大 ζ 的可逆點，所以 index 為零。因而在這裡若單射就必滿射，非可逆點為孤立有限代數重數特徵值，而非源 (4) 所需排除的 residual 障礙。至此 KL 全部假設已在同一固定 B 上核實。

## 4. 固定 s 的 KL 譜／投影結論

固定 `s in W`，選 `alpha_KL<r<M` 和一條位於 `|zeta|>r`、避開 `spec(L_s)` 的有限長小圍道 Gamma，其內部只包住一個孤立譜點或有限組外層孤立譜点。用源 Theorem 1、(19) 及有限段積分，得到大 m 時共同可逆性，以及

\[
\sup_{\zeta\in\Gamma}
||| (\zeta I-\mathcal L_s^{[m]})^{-1}
 -(\zeta I-\mathcal L_s)^{-1} |||
\le C_{s,\Gamma}q^{m\vartheta},
\tag{23}
\]
\[
|||\Pi_m(s)-\Pi(s)|||\le C'_{s,\Gamma}q^{m\vartheta},
\qquad
\Pi_m(s)=\frac1{2\pi i}\int_\Gamma
(\zeta I-\mathcal L_s^{[m]})^{-1}\,d\zeta.
\tag{24}
\]

其中 vartheta 由 (7) 給出。多個孤立點可以用有限條互不相交小圓周再求和。本節常數允許依賴固定 s 和圍道；本篇下一節的 compact-s 結論只宣稱定性局部一致，不將 (23) 的 pointwise 常數默認一致。

## 5. 緊複參數集的一致性與秩：定基點、縮鄰域、有限覆蓋

### 5.1 源定理的常數可用於整個小擾動集合

固定 `s_j`。考慮所有滿足 (16)、(17)、(22) 且
`|||Q-L_(s_j)|||<=C' epsilon` 的算子 Q。可在每個 epsilon 從中任選一個作源 `P_epsilon`，其 tau 取同一連續線性函數。KL 常數只依上述共同常數、固定基點的 resolvent 函數與這個 tau，不依任選的具體成員。因此其結論適用於這整個小擾動集合。

特別是 (20) 使全部 `Q=L_s^[m]` 在
`q^m+|s-s_j|<=epsilon` 時包含其中。這是定基點下的一個雙參數擾動集合，不需要將 m 和 s 排成強連續路徑。源定理中基點 resolvent 的依賴始終保留，不被「緊致性」一詞省去。

### 5.2 任意共同緊 resolvent 集

設 `Omega` 是 `(s,zeta)` 的緊集，滿足

\[
s\in\mathcal W,\qquad
|\zeta|>\alpha_{\rm KL},\qquad
\zeta\notin\operatorname{spec}(\mathcal L_s)
\quad((s,\zeta)\in\Omega).
\tag{25}
\]

選共同 `alpha_KL<r<min{M,inf_Omega|zeta|}`。在每個 `(s_j,zeta_j)`，取 `delta_j>0` 和 ζ 的小鄰域 `V_j`，使其閉包位於
`C\V_(delta_j,r)(L_(s_j))`。此時源 Theorem 1 的基點完全固定；其強 resolvent 函數在源譜排除區的有界性及相應常數由該定理保證，而在 `V_j` 上還可直接由固定基點 resolvent 的連續性取上界。

由 §5.1，選足夠小的 s 鄰域 `U_j` 及足夠大的 m，可同時使所有 `s in U_j`、`zeta in V_j` 的近似逆存在，並由 (8) 給共同強范數界。取覆蓋 Omega 的有限多個 `U_j x V_j`，再取有限多個 m 門檻及逆界的最大值，得到

\[
\sup_{(s,\zeta)\in\Omega}
\|(\zeta I-\mathcal L_s^{[m]})^{-1}\|\le C_\Omega
\quad(m\ge m_\Omega).
\tag{26}
\]

**混合收斂的量詞另證。** 先給任意精度 eps>0。在每個基點附近，(9)、(20) 及固定基點 resolvent 在 V_j 的界給

\[
|||R_m(s,\zeta)-R(s_j,\zeta)|||
\le C_j\bigl(q^m+|s-s_j|\bigr)^\vartheta,
\tag{27}
\]

其中 `R_m(s,zeta)=(zeta I-L_s^[m])^-1`、`R(s,zeta)=(zeta I-L_s)^-1`。先縮小 U_j，使 (27) 的 `|s-s_j|` 貢獻小於 eps/3。又因原 `s -> L_s` 強算子范數整，局部 Neumann／resolvent identity 在 `U_j x V_j` 給
`||R(s,zeta)-R(s_j,zeta)||<eps/3`，可再次縮小 U_j 達成。這不依賴近似算子的強收斂。

上述逐點小鄰域仍覆蓋 Omega；取有限子覆蓋，最後取共同大 m，使各 (27) 的 `q^m` 貢獻小於 eps/3。三角不等式遂給

\[
\boxed{\sup_{(s,\zeta)\in\Omega}
|||R_m(s,\zeta)-R(s,\zeta)|||\longrightarrow0.}
\tag{28}
\]

這證明定性的 compact-s 一致性。有限覆蓋可以隨 eps 變化；所以本論證不聲稱已有一個對所有精度共用的 `C_Omega q^(m vartheta)` 速率。

### 5.3 局部共同圍道與投影秩

固定 `s_0 in W`，令 lambda 為 `L_(s_0)` 的孤立譜點，`|lambda|>alpha_KL`。選 `alpha_KL<r<min{M,|lambda|}`，再取以 lambda 為中心的足夠小圓周 Gamma，使其閉盤位於 `|zeta|>r`、只包含這一個原譜點，並滿足源 Corollary 1(2) 的小半徑條件。

利用 §5.1 將所有近 s、大 m 與固定 `L_(s_0)` 比較。由本篇 (24) 的投影估計與源 Corollary 1(2)（本篇 (10)）可取共同 K_2 及混合投影差，並將鄰域和門檻取到

\[
|||\Pi_m(s)-\Pi(s_0)|||<\frac1{2K_2},\qquad
\|u\|\le K_2|u|
\quad\bigl(u\in\operatorname{ran}\Pi_m(s)
\ \text{或}\ u\in\operatorname{ran}\Pi(s_0)\bigr).
\tag{29}
\]

源 epsilon=0 包含在同一 K_2 中，故兩個子空間都受控。若 `u in ran Pi_m(s)` 且 `Pi(s_0)u=0`，則

\[
|u|=|(\Pi_m(s)-\Pi(s_0))u|
\le\frac{\|u\|}{2K_2}\le\frac12|u|,
\tag{30}
\]

因此 u=0，`Pi(s_0)` 在近似像空間上單射。反過來交換兩個投影，用同一 (29) 得 `Pi_m(s)` 在原像空間上也單射。故兩者秩相同；這是線性單射的維數比較，不是把 mixed-close 當作 strong-close。

原 `Pi(s)` 在這個小 s 鄰域強范數解析且秩局部恆定，於是

\[
\operatorname{rank}\Pi_m(s)=\operatorname{rank}\Pi(s_0)
=\operatorname{rank}\Pi(s)
\tag{31}
\]

對同一小鄰域和全部充分大 m 成立。對其任意緊子集 K，`Omega=K x Gamma` 滿足 (25)，積分 (28) 另給

\[
\boxed{\sup_{s\in K}|||\Pi_m(s)-\Pi(s)|||\longrightarrow0.}
\tag{32}
\]

式 (31) 是包含廣義特徵向量的代數秩結論，(32) 是混合范數而非強投影范數收斂。每個固定 m 的 `s -> L_s^[m]` 與原族都強范數整，故圍道不碰譜的鄰域中兩個投影族各自全純；沒有因此把 m 極限稱為強全純收斂。

## 6. 有限矩陣與有限記憶全算子的完整外層代數譜

以下固定 m>=2 和複 s；本節的精確譜等式本身不要求 s 在 (12) 的窗口內。令 k=m-1，並定義

\[
v_m(u)=\sup_{\substack{x\ne y\\N(x,y)\ge k}}
 \frac{|u(x)-u(y)|}{q^{N(x,y)}}.
\tag{33}
\]

其核恰為 F_k，且加上任何柱常數不改 v_m。它因此在商 `B/F_k` 上是范數。令 `||[u]||_quot=inf_(f in F_k)||u-f||`。立刻有 `v_m(u)<=||[u]||_quot`。

反向令 `e=u-P_k u`。同柱兩點的 P_k 值相同，所以柱內差商至多 v_m(u)，且 `|e|<=q^k v_m(u)`。跨柱兩點的首分歧 `N<=k-1`，由兩個 sup 界

\[
\frac{|e(x)-e(y)|}{q^N}
\le2q^{k-N}v_m(u)\le2qv_m(u).
\tag{34}
\]

因此 `[e]_beta<=max{1,2q}v_m(u)<=2v_m(u)`，得到

\[
\boxed{v_m(u)\le\|[u]\|_{\rm quot}\le3v_m(u).}
\tag{35}
\]

這只是原空間的輔助商；沒有更換計算原譜的空間或 beta。

令 `N(x,y)>=m-1`，配對相同長度 n 前綴 w。对 `0<=j<n`，`sigma^j(wx)` 和 `sigma^j(wy)` 至少一致於前 `N+n-j>=m` 個座標，因此 g_m 的值完全相同。全部 n 步權重遂完全相同，沒有 distortion 餘項；同時

\[
|u(wx)-u(wy)|\le v_m(u)q^{N+n}.
\tag{36}
\]

將權重模求和，得到商算子 `overline L_s^[m]` 的迭代界

\[
v_m(\mathcal L_s^{[m],n}u)
\le q^n A_{n,m}(t)v_m(u),\qquad
r(\overline{\mathcal L}_s^{[m]})\le q\lambda_{t,m},
\quad t=\operatorname{Re}s.
\tag{37}
\]

F_k 是有限維閉不變子空間，且有已固定的有界投影 P_k。用這個分裂把全算子寫成上三角區塊：左上塊是 A_m(s)，右下塊等價於商算子。`|zeta|>q lambda_(t,m)` 時右下塊的 `zeta I` 減算子可逆，故整個塊矩陣可逆當且僅當左上塊可逆。因此

\[
\boxed{
\operatorname{spec}(\mathcal L_s^{[m]})
 \cap\{|\zeta|>q\lambda_{t,m}\}
=\operatorname{spec}(A_m(s))
 \cap\{|\zeta|>q\lambda_{t,m}\}.
}
\tag{38}
\]

代數重數也完全相同。若 `(L_s^[m]-zeta I)^ell u=0`，投到商上，由商算子的 `zeta I` 減算子可逆，得到 `[u]=0`；所以整個廣義根空間落在 F_k。反向 F_k 內的廣義特徵向量本來就是全空間的廣義特徵向量。等價地，外層小圍道的全 Riesz 投影像就在 F_k，且其限制是矩陣的 Riesz 投影。

在 (12) 的參數窗口及 m>=m_0，`q lambda_(t,m)<=alpha_KL`。因此 §4–5 所比較的外層谱簇，確實由既有 A_m(s) 捕獲，包含完整代數重數。這不是由「F_k 不變」單獨推出，也沒有斷言全 `L_s^[m]` 有限秩。

## 7. 能力邊界與本輪操作

本篇把既有 sup roof 逼近接到同一原 B_beta 的外層離散譜與矩陣代數譜。它不與 [input] §8 的一般 big Hölder 反例矛盾：所證收斂范數是混合范數；強 LY 一致性與強誤差趋零是不同命題。

明確保留以下界線：

- 原算子的內部／本質譜沒有由有限矩陣完整表示；(38) 只在其明列外圓盤成立。
- compact-s 的 m cutoff 依賴有限窗口、圍道和譜排除距離；沒有一個對所有 `|Im s|` 通用的 cutoff，也沒有近似 roof 的共同 Dolgopyat 常數。
- (31) 是固定 s 的譜簇代數秩；物理參數 s 的 determinant 零點階數及全純有限區塊橋由主線另外負責，不在本篇預先宣稱。
- 沒有建立整個 finite-memory determinant 在條帶內的一致收斂、普通算子跡、核 Fredholm 身份、數值 enclosure、完整五通道總誤差或量子／散射譜身份。原非緊性結論與正式停止線不變。

ARS 的有界 argument-builder 原則用於逐项源假設匹配、區分強／混合范數、單獨證明 rank 及矩陣接口。源命題由實際原刊圖像承擔，本案各界與商譜由本文公式承擔；同模型分工核對不是外部獨立科學再現或新穎性證明。

寫前確認目標不存在；只以 apply_patch 新增本檔。寫後僅對新檔作文本／引用／雜湊核對，並比對已讀舊輸入未變。未運行科學、符號、數值、譜、軌道或字詞枚舉程式，未執行 producer、正式 checker 或稿件 build。文本檢查不認證數學正確性，亦不變更 Gate、Route 或 Stage。

## 參考與上游依賴

- [原路線圖][roadmap] §4.3–4.4：既有 common-coefficient 和 rank／projection 研究義務，不視為新的執行授權。
- [一側 roof／固定空間][roof] §4–6；[低頻 RPF 規範][low] §7.1；[有限記憶矩陣][memory] §1、§4；[原 resolvent 條帶][strip] §1–4；[roof 輸入誤差][input] §3、§8–9。
- [Keller–Liverani 原刊][kl]，§1 式 (1)–(7)、Remark 1(c)、§2 Theorem 1 式 (8)–(10)、Corollary 1、Remark 4，以及原刊 149–150 頁 Corollary 1 證明。源方法給混合 resolvent／投影穩定；本案固定窗口匹配、定基點有限覆蓋和商譜接口由本文另外給出。

[roadmap]: stage1_phase6_final_report.md
[roof]: internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[low]: internal_goal01_positive_variance_and_low_frequency_branch_20260909.md
[memory]: internal_goal01_cylinder_trace_and_finite_memory_determinants_20260909.md
[strip]: internal_goal01_fixed_space_resolvent_strip_and_simple_pressure_pole_20260909.md
[input]: internal_goal01_roof_input_error_and_resolvent_stability_20260909.md
[kl]: https://www.numdam.org/item/ASNSP_1999_4_28_1_141_0.pdf
