# P30 goal01：Poisson 方程、嚴格正方差與統一低頻解析分支

日期：2026-09-09 UTC。範圍：依本輪明確授權，只新建本篇內部理論筆記，保存此前紙面推導並補緊實實參數區間的一致性證明；不修改既有檔案、鎖定輸入、程式、資料、正式稿或 Stage／Route 狀態。

固定原等邊三圓盤：半徑 `a>0`、中心間距 `d=6a`、單位歐氏速率、原逐碰撞截面和盤標記。本文只處理固定幾何、固定物理時鐘、固定 Hölder 空間上的實 RPF 結構與零頻附近的複擾動。不處理幾何變動、高頻估計或 determinant 身份。

## 0. 主結論與證據分工

令 g 是[一側正 roof 筆記][roof] §3 的保原週期代表，`L_s` 是其 §4 的固定空間轉移算子。對每個實 t，本文由實 RPF 譜隙直接證明

\[
\sigma_t^2
=\lim_{n\to\infty}\frac1n\int
  \bigl(S_n(g-\mu_t(g))\bigr)^2\,d\mu_t>0,
\tag{1}
\]

且原正特徵值 `lambda_t` 的局部解析延拓滿足

\[
\log\lambda(t+ib)
=\log\lambda_t-ib\,\mu_t(g)-\frac{b^2}{2}\sigma_t^2
 +O_t(|b|^3).
\tag{2}
\]

更精確地，任意非空緊實實區間 `I` 上存在 `delta_I>0`、`c_I>0` 及 `eta_I<1`，使所有 `t in I`、`|b|<delta_I` 同時滿足

\[
\frac{r(\mathcal L_{t+ib})}{\lambda_t}
=\frac{|\lambda(t+ib)|}{\lambda_t}
\le e^{-c_I b^2},
\qquad
\operatorname{spec}(\mathcal L_{t+ib})
 \setminus\{\lambda(t+ib)\}
 \subset\{w:|w|\le\eta_I\lambda_t\}.
\tag{3}
\]

式 (3) 中的被刪特徵值是代數重數一的特徵值；`lambda(t+ib)` 只表示從實 t 出發的局部主分支，不預設任意複參數上的全局單值標號。

證據分工如下：真實物理編碼、一側化、保週期和算子整族由 [roof] 繼承；實 RPF 正特徵對與簡單譜隙取自 [Stoyanov][stoy] 的源命題，§2 明列適用條件；滿支撐、Poisson 分解、正方差、導數及統一低頻界在本文逐步推導。兩個幾何週期由[既有幾何見證][periods] 繼承。沒有把同席推導或同伴同意當成外部獨立科學證據，也未使用 CLT 或 Livšic 逆命題作黑箱。

ARS academic-paper / argument-builder 的有限論證整理原則用於區分輸入、推導和不能升級的結論；這不是完整論文寫作／審查流水線或形式化證明器的驗證紀錄。

## 1. 固定空間、物理 roof 與兩個週期

設

\[
\Sigma^+=\{x\in\{1,2,3\}^{\mathbb N_0}:x_j\ne x_{j+1}\},
\qquad
d_\theta^+(x,y)=\theta^{\min\{j\ge0:x_j\ne y_j\}}
\quad(x\ne y),
\tag{4}
\]

並令相同序列距離為零。`sigma` 在本篇一側公式中均指一側左移。固定一次 `0<theta<1`，以及

\[
\rho=\frac3{2\sqrt6-1},\qquad
\alpha=\frac{\log\rho}{\log\theta},\qquad
\beta=\alpha/2,\qquad q=\theta^\beta=\sqrt\rho<1.
\tag{5}
\]

所有算子均作用在同一複 Banach 代數

\[
\mathcal B=C^\beta(\Sigma^+,d_\theta^+;\mathbb C),
\qquad \|v\|_\beta=\|v\|_\infty+[v]_\beta,
\qquad
[v]_\beta=\sup_{x\ne y}
 \frac{|v(x)-v(y)|}{d_\theta^+(x,y)^\beta}.
\tag{6}
\]

[roof] §3–4 給出固定實函數 `g in B`，`2a<=g<=10a`，及固定雙向共邊界 U，使

\[
g\circ\pi=\tau-U+U\circ\sigma_{\mathbb Z},
\qquad
(\mathcal L_s v)(x)=\sum_{b\ne x_0}e^{-s g(bx)}v(bx).
\tag{7}
\]

其中 tau 是原單位速率雙向物理飛行時間，pi 忘記負座標。g 不必逐點等於 tau；(7) 保持每個閉合軌道的總物理週期。上游已在 (6) 上證明 `s -> L_s` 算子範數整解析，且

\[
\partial_s^k\mathcal L_s v=\mathcal L_s((-g)^k v).
\tag{8}
\]

令 `x^(2)=(12)^infty`、`x^(3)=(123)^infty`。由 [periods] §2、§3.4 的真實軌道及 (7)，

\[
S_2g(x^{(2)})=T_2=8a,\qquad
S_3g(x^{(3)})=T_3=(18-3\sqrt3)a,
\qquad
\frac{T_2}{2}=4a\ne(6-\sqrt3)a=\frac{T_3}{3}.
\tag{9}
\]

這裡只需要兩個不同的逐碰撞平均時間；不需要第三個 `(1213)` 週期或非零頻率相位排除。

## 2. 唯一外部動力學輸入：實 RPF 命題

使用 L. Stoyanov, *On Gibbs Measures and Spectra of Ruelle Transfer Operators*, Canadian Mathematical Bulletin 60(2) (2017), 411–421，DOI [10.4153/CMB-2016-073-2][stoy]，Theorem 2.1(i)–(iii)；[作者 arXiv 版本][stoy-preprint] 的對應標號為 Theorem 2.1(a)–(c)。對偶特徵測度關係亦明列於該文 §1 及 §3 開頭。所用內容僅為：primitive 有限轉移矩陣與實 Hölder 勢給嚴格正 Hölder 特徵函數、正對偶測度、正主特徵值，以及主特徵值代數簡單、全部餘譜嚴格縮在較小圓盤內。不使用該文額外定量常數或 essential radius 的等號。

本案矩陣 `A_ij=1` 當且僅當 `i!=j`，且 `A^2` 對角元為 2、非對角元為 1，所以 primitive 條件成立。源文的字母數參數不是本文的收縮率 q；套用時字母數為 3、源文的 Hölder 度量參數選本文 q，勢函數選 `-t g`。

范數對照也不能略去。源文使用

\[
V_q(v)=\sup_{k\ge0}\frac{\operatorname{var}_k(v)}{q^k},
\qquad
\operatorname{var}_k(v)=\sup_{x_j=y_j\;(0\le j\le k)}|v(x)-v(y)|.
\tag{10}
\]

由 (4)–(6)，`V_q(v)<=q[v]_beta`。反過來，首個不同座標 `N>=1` 時用 `var_(N-1)`，`N=0` 時用 `2||v||_infty`，得到

\[
[v]_\beta\le\max\{2\|v\|_\infty,q^{-1}V_q(v)\}.
\tag{11}
\]

故源文 `F_q` 與 (6) 是等價范數的同一空間，複化後亦然；不能只在弱的連續函數空間上引用譜隙再默認它適用於 (6)。

因此對每個固定實 t，有 `lambda_t>0`、實 `h_t in B` 嚴格正及有限正測度 `nu_t`，規範為

\[
\mathcal L_t h_t=\lambda_t h_t,\qquad
\mathcal L_t^*\nu_t=\lambda_t\nu_t,\qquad
\nu_t(h_t)=1.
\tag{12}
\]

主值 `lambda_t=r(L_t)` 代數簡單，且存在 `r_t<1` 使餘譜位於 `|w|<=r_t lambda_t`。連續嚴格正的 h_t 在緊空間上有正下界，故 `h_t^-1 in B`。比較常函數 1 與 h_t 的正倍數，再施加 `L_t^n`，可知 `||L_t^n 1||_infty` 被兩個固定正倍數的 `lambda_t^n` 夾住；因此此 `lambda_t` 也等於 [roof] §6 所用的實正權成長率。

下文先固定 t 並省略下標，定義

\[
\mu(v)=\nu(hv),\qquad
Pv=\lambda_t^{-1}h^{-1}\mathcal L_t(hv),\qquad
\Pi v=\mu(v)1.
\tag{13}
\]

mu 是機率測度，`P1=1`、`mu(Pv)=mu(v)`。相似變換保留代數重數及譜；`P Pi=Pi P=Pi`，且 `N=P-Pi` 的譜半徑小於 1。由譜半徑公式，任取 `kappa` 嚴格介於 `r(N)` 與 1 之間，存在有限 C，使

\[
\|P^n v\|_\beta\le C\kappa^n\|v\|_\beta
\quad(n\ge0,\ \mu(v)=0).
\tag{14}
\]

具體而言，大 n 時 `||N^n||^(1/n)<kappa`，有限個剩餘 n 吸收入 C；在均值零子空間，`P^n=N^n`（n>=1）。因此 (14) 不依賴源文另一條指數收斂公式的排版／規範。

## 3. 不變性、滿支撐與 Poisson 方程

對 `v,w in B`，有限前像和直接給

\[
P\bigl(v(w\circ\sigma)\bigr)=wPv.
\tag{15}
\]

取 v=1，再施加 mu，得 `mu(w o sigma)=mu(w)`。柱函數稠密於連續函數，故這是測度意義的移位不變性。反覆套用 (15) 得

\[
\mu\bigl(v(w\circ\sigma^k)\bigr)=\mu((P^k v)w)
\quad(k\ge0).
\tag{16}
\]

**滿支撐的直接證明。** 取任意非空長度 ell>=1 柱集 `C=[w_0 ... w_(ell-1)]`。對每個尾序列 x，三個字母中總能選一個 b 同時不同於 `w_(ell-1)` 和 `x_0`，於是 `w_0 ... w_(ell-1) b x` 是合法前像。因所有實權重及 h 嚴格正，

\[
P^{\ell+1}1_C(x)>0\quad\text{對每個 }x.
\tag{17}
\]

柱集指示函數屬於 B，左側連續；緊致性給正的最小值。由 mu 的 P 不變性，`mu(C)=mu(P^(ell+1)1_C)>0`。每個非空開集包含柱集，故 `supp(mu)=Sigma+`。這不是額外假設的 Gibbs 性質。

令

\[
m=\mu(g),\qquad f=g-m,\qquad
u=\sum_{n=1}^{\infty}P^n f.
\tag{18}
\]

由 (14)，級數在 B 中絕對收斂；f、P 皆實，故 u 實，且

\[
\mu(u)=0,\qquad (I-P)u=Pf.
\tag{19}
\]

在 `ker(mu)` 上，`I-P` 的逆為 `sum_(n>=0)P^n`，故 (19) 是該子空間的唯一解。設

\[
\psi=f+u-u\circ\sigma.
\tag{20}
\]

移位對符號距離至多放大 beta 次方距離 q^-1，故 `u o sigma in B`。利用 `P(u o sigma)=u` 和 (19)，

\[
P\psi=Pf+Pu-u=0.
\tag{21}
\]

此符號約定是後續導數計算的關鍵：此處 Poisson 級數從 n=1 開始，且 psi 是 `f+u-u o sigma`。

## 4. 方差恆等式與嚴格正性

由 (16)、(21) 與移位不變性，對 `0<=j<k` 有

\[
\mu((\psi\circ\sigma^j)(\psi\circ\sigma^k))
=\mu(\psi(\psi\circ\sigma^{k-j}))
=\mu((P^{k-j}\psi)\psi)=0.
\tag{22}
\]

這裡全部函數實值，故是通常的實 `L^2(mu)` 正交性。又 `mu(psi)=0`，所以

\[
\mu((S_n\psi)^2)=n\mu(\psi^2),\qquad
S_nf=S_n\psi-u+u\circ\sigma^n.
\tag{23}
\]

令 `B_n=-u+u o sigma^n`，則 `||B_n||_2<=2||u||_infty`。因此

\[
\left|\frac{\mu((S_nf)^2)}n-\mu(\psi^2)\right|
\le \frac{4\|u\|_\infty\sqrt{\mu(\psi^2)}}{\sqrt n}
 +\frac{4\|u\|_\infty^2}{n}\longrightarrow0.
\tag{24}
\]

這證明 (1) 的極限存在且

\[
\sigma_t^2=\mu(\psi^2)\ge0.
\tag{25}
\]

另令 `gamma_k=mu(f(f o sigma^k))`。由 (16)、(14)，

\[
\gamma_k=\mu(fP^k f),\qquad
|\gamma_k|\le C\kappa^k\|f\|_\infty\|f\|_\beta,
\tag{26}
\]

故協方差級數絕對可和。展開平方有限和，移位不變性直接給

\[
\frac1n\mu((S_nf)^2)
=\mu(f^2)+2\sum_{k=1}^{n-1}(1-k/n)\gamma_k.
\tag{27}
\]

由絕對可和性取極限，再用 (18)，得到

\[
\boxed{\sigma_t^2=\mu(f^2)+2\sum_{k\ge1}\gamma_k
=\mu(f^2)+2\mu(fu)=\mu(\psi^2).}
\tag{28}
\]

**嚴格正性。** 若 `sigma_t^2=0`，(25) 及 psi 的連續性、mu 的滿支撐迫使 `psi=0` 逐點成立：若某點不為零，一個非空開鄰域上 psi 的平方有正下界，與積分為零矛盾。因而

\[
g=m+u\circ\sigma-u.
\tag{29}
\]

對每個 `sigma^n x=x`，有限和相消給 `S_ng(x)=nm`。這迫使 (9) 的兩個實際物理週期同時滿足

\[
m=4a,\qquad m=(6-\sqrt3)a,
\tag{30}
\]

不可能。故每個實 t 都有 `sigma_t^2>0`。這只是由零方差推出一個已構造的逐點共邊界，然後用兩個週期反證；沒有援引 Livšic 定理的充分方向，也沒有宣稱不共調本身即給高頻估計。

## 5. 局部解析特徵值及其一、二階導數

仍固定本節的實 t、h、`lambda_t`、mu，不隨 z 重新規範。令

\[
Q_t(z)=\lambda_t^{-1}M_{h^{-1}}\mathcal L_{t+z}M_h
=P M_{e^{-zg}}.
\tag{31}
\]

由 (8) 及 Banach 代數性，這是固定 B 上的整解析族，`Q_t(0)=P`，並有

\[
Q_t'(0)=-P M_g,\qquad Q_t''(0)=P M_{g^2}.
\tag{32}
\]

取以 1 為中心、只包住 P 的簡單特徵值 1 的小正向圓周 Gamma。對小 z，resolvent 的 Neumann 級數給解析的 Riesz 投影

\[
\Pi_t(z)=\frac1{2\pi i}\int_\Gamma
(wI-Q_t(z))^{-1}\,dw,\qquad \Pi_t(0)=\Pi.
\tag{33}
\]

縮小 z 的圓盤使 `||Pi_t(z)-Pi||<1`，近投影的秩相同，故其秩為一。再縮小可使 `mu(Pi_t(z)1)` 非零，於是

\[
v(z)=\frac{\Pi_t(z)1}{\mu(\Pi_t(z)1)},\qquad
Q_t(z)v(z)=k(z)v(z),\qquad
\mu(v(z))=1,
\quad k(0)=1,\ v(0)=1.
\tag{34}
\]

例如 `k(z)=mu(Q_t(z)v(z))`，故 k 亦解析。本文記

\[
\lambda(t+z):=\lambda_t k(z)
\tag{35}
\]

為這條局部特徵值分支。

對 (34) 一次求導並在零點施加 mu，利用 `mu P=mu`、`mu(v'(0))=0`，得

\[
k'(0)=-m,\qquad
(I-P)v'(0)=-Pg+m=-Pf.
\tag{36}
\]

由 (19) 的唯一性，`v'(0)=-u`。再次求導得到

\[
Q_t''(0)1+2Q_t'(0)v'(0)+Pv''(0)
=k''(0)1+2k'(0)v'(0)+v''(0).
\tag{37}
\]

施加 mu，所有含 `mu(v')`、`mu(v'')` 的項消失，從而

\[
k''(0)=\mu(g^2)+2\mu(gu).
\tag{38}
\]

取 `log k(0)=0` 的局部對數分支，因 `mu(u)=0`，(28) 給

\[
(\log k)'(0)=-m,\qquad
(\log k)''(0)=k''(0)-k'(0)^2
=\mu(f^2)+2\mu(fu)=\sigma_t^2.
\tag{39}
\]

解析 Taylor 展開遂給 (2)。特別地，對實小 z，該分支是附近實 RPF 主值：Q_t(z) 保持實函數，而 Gamma 關於共軛對稱，所以 Pi_t(z) 亦保持實函數。由 (34)，v(z) 在一致范數中接近 1，於是 `h v(z)` 是 L_(t+z) 的嚴格正實特徵向量。其特徵方程與當地正對偶測度配對，因 `nu_(t+z)(h v(z))>0`，特徵值必等於當地 `lambda_(t+z)`。因此實函數

\[
p(t)=\log\lambda_t
\quad\text{局部實解析，}\qquad
p'(t)=-\mu_t(g),\quad p''(t)=\sigma_t^2>0.
\tag{40}
\]

這裡 p 的定義只是實主特徵值的對數；本文不另借未核對的壓力等同或行列式身份。

## 6. 固定 t 的全餘譜控制與低頻主分支占優

只知道 (2) 的特徵值展開，尚不足以把它寫成整個算子的譜半徑。以下補足這一步。

取 `r(P-Pi)<eta<1`，再取 `0<epsilon<1-eta`。設 Gamma 是 `|w-1|=epsilon`，並取 `R>||P||+2`。P 的譜除 1 外都在 `|w|<eta`，因此

\[
K=\{w:\eta\le|w|\le R,\ |w-1|\ge\epsilon\}
\tag{41}
\]

是一個全位於 resolvent 集的緊集；Gamma 亦在其中。原 resolvent 在 K 上有有限上界 M。小 z 時令 `||Q_t(z)-P||<1/(2M)` 且 `||Q_t(z)||<R`。由

\[
wI-Q_t(z)
=\bigl[I-(Q_t(z)-P)(wI-P)^{-1}\bigr](wI-P),
\tag{42}
\]

K 上的全部點仍屬 resolvent 集。外部 `|w|>=R` 亦由算子范數界排除。再用 §5 的秩一 Riesz 投影，得到

\[
\operatorname{spec}(Q_t(z))
\subset\{|w|<\eta\}\cup\{k(z)\},
\qquad |k(z)-1|<\epsilon,\quad |k(z)|>\eta.
\tag{43}
\]

因此 `r(L_(t+ib))=lambda_t |k(ib)|`。對 (2) 取實部，縮小 `delta_t>0` 使三階餘項絕對值不超過 `sigma_t^2 b^2/4`，可取

\[
c_t=\sigma_t^2/4,\qquad
\frac{r(\mathcal L_{t+ib})}{\lambda_t}
\le\exp(-c_t b^2)\quad(|b|<\delta_t).
\tag{44}
\]

## 7. 緊實實參數區間上的共同圍道、餘譜圓盤與二次衰減

本節令 `I subset R` 為任意固定非空緊實區間；幾何、g、theta、beta 及 B 一律不變。以下給共同常數的逐步存在性證明，不把所有一致性壓縮成一句「由緊致性」。

### 7.1 實 RPF 投影和正特徵函數的連續規範

固定 `t_0 in I`。取以 `L_(t_0)` 的簡單正主值為中心的局部圓周，以算子整解析性構造 `E_(t_0)(s)`。它在複鄰域解析，對實近點保持實函數，且作用於 `h_(t_0)` 得到嚴格正特徵向量。上文 (40) 前的配對論證把這條實分支識別為當地唯一主值，因此局部投影就是當地的主 Riesz 投影 `E_t`。重疊實鄰域上的投影相同，故它們沿 I 拼成算子范數連續、局部實解析的 `t -> E_t` 和正函數 `t -> lambda_t`。

選定一個固定 `x_* in Sigma+`，統一規範

\[
h_t=\frac{E_t1}{(E_t1)(x_*)},\qquad h_t(x_*)=1.
\tag{45}
\]

因實 RPF 投影是正主特徵函數乘正對偶泛函，分母嚴格正。局部范數解析性使 `t -> h_t` 在 B 中連續。定義

\[
\nu_t(v)=(E_t v)(x_*),\qquad
\mu_t(v)=\nu_t(h_t v).
\tag{46}
\]

`E_t v=h_t nu_t(v)`、`nu_t(h_t)=1`，所以 (46) 給與 (13) 相同的不變機率測度；h 的改規範不改 mu 或 P。由固定點評價泛函及 B 的乘法連續性，`nu_t`、`mu_t` 在 B 的對偶范數中連續。此規範的 nu_t 無須本身是機率測度，mu_t 則始終是。

映射 `(t,x) -> h_t(x)` 在 `I x Sigma+` 上連續且嚴格正，故有統一正下界；在 Banach 代數中取逆連續，亦可由

\[
\|h_t^{-1}\|_\infty\le (\min h_t)^{-1},\qquad
[h_t^{-1}]_\beta\le [h_t]_\beta(\min h_t)^{-2}
\tag{47}
\]

直接看出統一有界性。`lambda_t` 亦有統一正下界。因此 `P_t=lambda_t^-1 M_(h_t^-1)L_t M_(h_t)`、`Pi_t=1 tensor mu_t`、`N_t=P_t-Pi_t` 全在算子范數中連續，且范數在 I 上有界。

### 7.2 用有限覆蓋把實餘譜間隙統一化

對每個 `t_0 in I`，已知 `r(N_(t_0))<1`。取一個介於兩者之間的 `kappa_(t_0)<1`。由譜半徑公式，存在正整數 `n_(t_0)` 使

\[
\|N_{t_0}^{n_{t_0}}\|<\kappa_{t_0}^{n_{t_0}}.
\tag{48}
\]

算子范數連續性使此嚴格不等式在一個實鄰域 `J_(t_0)` 中仍成立。故 `t in J_(t_0) cap I` 時

\[
r(N_t)\le\|N_t^{n_{t_0}}\|^{1/n_{t_0}}<\kappa_{t_0}.
\tag{49}
\]

取這些 J 的有限子覆蓋，令 `kappa_0` 為對應有限多個 `kappa_(t_0)` 的最大值，則 `kappa_0<1` 且 `r(N_t)<kappa_0` 對全部 I 成立。這也具體展示了此處所用譜半徑上半連續性的機制。

固定

\[
\kappa_0<\eta_I<1,\qquad
0<\epsilon<(1-\eta_I)/3,\qquad
H=\sup_{t\in I}\|P_t\|,\qquad R>H+2.
\tag{50}
\]

定義共同緊集

\[
\mathcal K=\{(t,w):t\in I,\ \eta_I\le|w|\le R,
\ |w-1|\ge\epsilon\}.
\tag{51}
\]

對每個 `(t,w) in K`，`wI-P_t` 可逆。逆映射在可逆算子集上連續，因而在這個已排除全部實譜的緊集上有有限最大值

\[
M=\sup_{(t,w)\in\mathcal K}\|(wI-P_t)^{-1}\|<\infty.
\tag{52}
\]

共同圍道 `Gamma={|w-1|=epsilon}` 對每個 t 都包含在 (51) 中。

### 7.3 統一複擾動與全部餘譜留在共同圓盤

對每個實 t 定義以該 t 的規範凍結的

\[
Q_t(z)=P_tM_{e^{-zg}},\qquad G=\|g\|_\beta.
\tag{53}
\]

Banach 代數的指數級數給與 t 無關的界

\[
\|Q_t(z)-P_t\|\le H(e^{|z|G}-1),\qquad
\|Q_t(z)\|\le H e^{|z|G}.
\tag{54}
\]

因此可以選共同 `delta_0>0`，使 `|z|<delta_0` 時，第一界小於 `1/(2M)`、第二界小於 R。式 (42) 的同一 Neumann 論證對所有 t 和 (51) 同時成立，並給

\[
\|(wI-Q_t(z))^{-1}\|\le2M\quad((t,w)\in\mathcal K).
\tag{55}
\]

令 `Pi_t(z)` 為共同 Gamma 上的 Riesz 積分。由 resolvent 恆等式及 Gamma 長度 `2 pi epsilon`，

\[
\|\Pi_t(z)-\Pi_t\|
\le2\epsilon M^2\|Q_t(z)-P_t\|.
\tag{56}
\]

再統一縮小 delta_0，使右側小於 1/2。兩個投影距離小於 1 意味其有限維秩相同，故 `Pi_t(z)` 一律秩一。又 `||mu_t||_(B*)<=1`，所以

\[
|\mu_t(\Pi_t(z)1)-1|<1/2.
\tag{57}
\]

由 (34) 的相同公式，得到對 z 解析、對 `(t,z)` 聯合連續的 `v_t(z)` 和 `k_t(z)`。圍道內只有這一個代數簡單特徵值，並且

\[
|k_t(z)-1|<\epsilon,\qquad
\operatorname{spec}(Q_t(z))\setminus\{k_t(z)\}
\subset\{|w|<\eta_I\},\qquad |k_t(z)|>1-\epsilon>\eta_I.
\tag{58}
\]

譜圓盤外由 (55) 排除，`|w|>=R` 由 (54) 排除；這不是只追蹤主分支而忽略其他譜點。經 (31) 的相似變換，(58) 正是 (3) 所需的統一餘譜圓盤和主分支占優。

每個 t 的這條分支與 §5 的局部分支在零點的鄰域內相同，因為它是該簡單特徵值的唯一局部延拓。此證明不需要先指定全複平面上的 `lambda(s)`。

### 7.4 方差的連續嚴格正性與共同 Taylor 餘項

由 (40)，`sigma_t^2=p''(t)` 局部實解析，故在 I 上連續。§4 已對每個實 t 證明其嚴格正性。因此

\[
\sigma_*^2:=\min_{t\in I}\sigma_t^2>0.
\tag{59}
\]

嚴格不等式的有限覆蓋版本是：每個 `t_0` 有鄰域使 `sigma_t^2>sigma_(t_0)^2/2`；取有限子覆蓋，有限個正下界的最小值仍正。這一步不依賴任何未給出的數值下界。

由 (58)，可以對全部 t 使用 `|k-1|<epsilon<1` 中的同一對數級數，設 `ell_t(z)=Log k_t(z)`。在 `|z|<delta_0`，

\[
|\ell_t(z)|
\le\sum_{n\ge1}\frac{\epsilon^n}{n}
\le\frac{\epsilon}{1-\epsilon}=:L_*.
\tag{60}
\]

設 `r_0=delta_0/2`。Cauchy 係數估計在半徑 r_0 的圓上對每個 t 同時給 `|a_(n,t)|<=L_* r_0^-n`。因此對 `|z|<=r_0/2`，從三次項起的級數滿足

\[
\left|\ell_t(z)+\mu_t(g)z-\frac{\sigma_t^2}{2}z^2\right|
\le C_*|z|^3,
\qquad C_*:=\frac{2L_*}{r_0^3},
\tag{61}
\]

其中一、二次係數由已證的 (39) 給出。這提供共同的三階餘項常數，而非各個 t 的不相容 `O_t` 記號。

最後取

\[
\delta_I=\min\left\{\frac{r_0}{2},\frac{\sigma_*^2}{4C_*}\right\}>0,
\qquad c_I=\frac{\sigma_*^2}{4}>0.
\tag{62}
\]

對所有 `t in I`、`|b|<delta_I`，(61) 在 `z=ib` 的實部給

\[
\log|k_t(ib)|
\le-\frac{\sigma_t^2}{2}b^2+C_*|b|^3
\le-\frac{\sigma_*^2}{4}b^2=-c_I b^2.
\tag{63}
\]

結合 (58) 的主分支占優即證明 (3)。共同的低頻衰減和全部餘譜圓盤由同一 delta_I 同時保證。

## 8. 結論邊界與文本核對

本篇完成固定物理 g 在每個實 t 的 Poisson 分解、嚴格正漸近方差、局部解析主值二階展開，以及任意固定緊實 t 區間上的共同低頻常數與全部餘譜控制。常數是證明中的存在性選擇，沒有聲稱已給可計算的數值最優界。

本篇沒有證明任意高頻、所有實 t 的統一常數、幾何參數變動下的一致性、全局解析主值標號、CLT、流相關衰減速率或 determinant／量子等式；也不以本篇替代上游真實幾何編碼證明的獨立審核。

本輪只讀既有局部輸入並作紙面推導；新增本檔後只做文本、路徑及未修改輸入的雜湊核對，不執行科學程式、數值實驗、舊 producer、正式稿建置或外部模型呼叫。來源身份／命題適用性與本文推導的數學正確性分開處理，文本檢查通過不是獨立科學驗證。

## 參考與上游依賴

- [roof]：*P30 goal01：保原週期的一側正 roof 與固定 Hölder 空間轉移算子界*，2026-09-09，§1、§3–4、§6。只作已明列上游輸入；本篇不改動該檔。
- [periods]：*internal_geometric_period_witnesses_20260908.md*，§2 式 (7)、§3.4 式 (12)、§4。用來識別 (9) 的真實物理週期及不等平均值。
- L. Stoyanov，[期刊 DOI][stoy]，*On Gibbs Measures and Spectra of Ruelle Transfer Operators*, Canadian Mathematical Bulletin 60(2) (2017), 411–421；Theorem 2.1(i)–(iii)，另見 §1、§3 的對偶測度關係。[作者 arXiv 版本][stoy-preprint]，arXiv:1703.04276v1，Theorem 2.1(a)–(c)。期刊版源命題此前已核讀；本次出版社 PDF 和 DOI 即時讀取逾時，改以可讀的作者版本再次核對所用命題及范數定義；不將此次逾時誤報為期刊來源不存在。

[roof]: internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[periods]: internal_geometric_period_witnesses_20260908.md
[stoy]: https://doi.org/10.4153/CMB-2016-073-2
[stoy-preprint]: https://arxiv.org/pdf/1703.04276
