# P30 內部來源接口審查：幾何高頻定理與固定符號 Hölder 空間

記錄日期：2026-09-09 UTC。主線授權本分支唯一新增本檔，保存已完成的有界來源與假設審查；本次整理不追加搜尋、科學程序、實驗或舊稿修改。主線將另行核讀來源定理後整合。

## 1. 結論與審查範圍

**真實平面三盤已有可引用的幾何 Dolgopyat 型定理；但本次核讀不支持把它直接寫成目前整個固定符號空間 `C^beta(Sigma^+, d_theta)` 上的高頻算子範數定理。** 最近的義務是編碼、roof、函數空間及頻率範數的接口，而不是籠統宣稱平面三盤的幾何高頻理論全部未知。

保持 P30 的等邊三圓盤、中心間距 `6a`、半徑 `a>0`、單位歐氏速率及原物理時鐘。現有自然符號空間是三字母、相鄰不等的一側移位，度量為 `d_theta=theta^N`。主線給定的當前算子討論以一側正 roof `g in C^beta`、`2a<=g<=10a` 為前提，令 `q=theta^beta<1`：

\[
(L_su)(x)=\sum_{b\ne x_0}e^{-s g(bx)}u(bx).
\]

主線已區分實參數準緊性、複參數的壓力上界及抽象局部常數 roof 反例。本檔不重證、不提升這些結果，也不把該抽象反例當成原幾何 roof 的反例。

本檔使用 ARS Phase 3 synthesis 與 Devil's Advocate 的假設—證據—適用範圍分離方式。其具體影響是同時保留兩件事：既不抹去真正適用於平面開放台球的已發表結果，也不將其不同編碼、空間上的結論移植為本項目的已證算子估計。

## 2. 來源身份、版本與定位規則

本次使用三篇已發表一手研究的作者稿核讀定理內容。出版身份與實際核读版本分開記錄：

| 來源 | 出版身份 | 本次實讀版本及主要定位 |
| --- | --- | --- |
| Luchezar Stoyanov, *Non-integrability of open billiard flows and Dolgopyat-type estimates* | *Ergodic Theory and Dynamical Systems* **32** (2012), 295–313；DOI `10.1017/S0143385710000933`；出版社記載線上發表為 2011-04-05 | [arXiv:0911.5000v4](https://arxiv.org/pdf/0911.5000v4)，版本日期 2010-10-28；§1 的 (H)、(P)，§6 的 eventually contracting 定義、(ND)、Proposition 6.2、Theorem 6.3 |
| Luchezar Stoyanov, *Spectra of Ruelle transfer operators for Axiom A flows* | *Nonlinearity* **24** (2011), 1089–1120；DOI `10.1088/0951-7715/24/4/005` | [arXiv:0810.1126v4](https://arxiv.org/pdf/0810.1126v4)，版本日期 2010-10-22；§1.1 的 regular distortion、eventually contracting、Theorem 1.1 及其後一維情況說明；§2 的 (LNIC)、式 (2.1) |
| Vesselin Petkov and Luchezar Stoyanov, *Correlations for pairs of periodic trajectories for open billiards* | *Nonlinearity* **22** (2009), 2657–2679 | [作者網站 PDF `correl10.pdf`](https://www.math.u-bordeaux.fr/~vpetkov/publications/correl10.pdf)；Introduction 的自然編碼警告；§3.3 的 Lemma 1、Theorems 3–4、式 (3.14)–(3.16)，以及其前 Proposition 4／式 (3.13) |

出版身份另由出版社及作者所屬機構頁面核對：[第一篇出版社頁](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/nonintegrability-of-open-billiard-flows-and-dolgopyattype-estimates/105637A9A2490327EA059BA9C950ECBD)、[第二篇 UWA 書目頁](https://research-repository.uwa.edu.au/en/publications/spectra-of-ruelle-transfer-operators-for-axiom-a-flows/)、[第三篇 Bordeaux 機構書目頁](https://oskar-bordeaux.fr/handle/20.500.12278/190460)。身份頁不被用來替代定理段落。

**定位完整性邊界：** 定理內容由瀏覽器的遠端 PDF 文字提取讀取，沒有下載本地 PDF，也沒有執行本地 PDF 結構／頁碼 preflight。本檔以章節、定理、條件及公式編號為證據定位，不建立或聲稱 `locally verified page` 錨。上表的出版頁碼只屬書目身份，不表示核對了出版版相應頁面的正文。本次僅核讀所列相關段落，沒有聲稱完整讀完三篇論文或逐行驗證其全部證明。

## 3. 定理一：開放台球專用高頻結論

來源：Stoyanov (2012) 作者稿 §1、§6，**Theorem 6.3**。

### 3.1 幾何前提及其關係

§1 固定至少三個互不相交、緊緻、嚴格凸、具有 `C^2` 邊界的障礙物，並要求 no-eclipse：任意兩個障礙物的凸包不與第三個相交。定理考慮其真實開放台球流在 non-wandering set `Lambda` 上的限制。

Theorem 6.3 的額外假設為 pinching (P)：存在 `C>0`、`0<alpha<=beta`，使每個 `x in Lambda` 有與 `u,t` 無關的 `alpha_x,beta_x`，滿足

\[
C^{-1}e^{\alpha_x t}\|u\|
\le \|D\phi_t(x)u\|
\le Ce^{\beta_x t}\|u\|,
\quad u\in E^u(x),\ t>0,
\]
\[
\alpha\le\alpha_x\le\beta_x\le\beta,
\qquad 2\alpha_x-\beta_x\ge\alpha.
\]

作者在 §1 明言平面 `n=2` 的情況自動滿足 (P)。因此本項目不能把適用於高維的「障礙距離足夠大」充分條件另加成平面 `d=6a` 的必要門檻。

§6 的 Proposition 6.2 在 `x -> E^u(x)` 為 `C^1` 的前提下，建立限制於 `Lambda` 切向的 symplectic 非退化 (ND)。Theorem 6.3 的證明使用 (P) 提供該正則性，再得到 (ND)，最後援用 Theorem 6.1。故對 **Theorem 6.3 本身**，不應把 (ND) 重列為與 (P) 無關的新增輸入義務。

這裡的 (ND) 不是僅說環境 symplectic form 非退化：它在 trapped set 的局部不穩定方向與適當穩定切向間，要求具有統一下界的非零配對。一般 contact 性或兩個週期長不共格均不能自行代替此限制於 `Lambda` 的條件。

### 3.2 算子、空間、頻率及結論

§6 選擇 Markov family `R_i=[U_i,S_i]`，令 `U=union U_i`，沿穩定葉投影後定義一側返回映射；`tau_M` 是該 Markov 截面的真實返回時間。一般先用避開邊界的 `Uhat`；文中說明開放台球可選相對邊界為空的矩形，令 `Uhat=U`。

令 `f` 是 `U` 上對幾何距離 Lipschitz 的實值勢，`P_f` 由

\[
P(f-P_f\tau_M)=0
\]

決定。為避免把來源中的實部參數 `a` 與本項目圓盤半徑混淆，此處改記該參數為 `delta`。Eventually contracting 的精確型式是：對每個 `epsilon>0`，存在 `rho in (0,1)`、`delta_0>0`、`C>0`，使

\[
\bigl\|\mathcal L_{f-(P_f+\delta+ib)\tau_M}^{\,m}u
\bigr\|_{\mathrm{Lip},b}
\le C\rho^m|b|^\epsilon\|u\|_{\mathrm{Lip},b}
\]

對 `|delta|<=delta_0`、`|b|>=1/delta_0`、全部整數 `m>0` 成立，其中

\[
\|u\|_{\mathrm{Lip},b}
=\|u\|_\infty+\frac{\operatorname{Lip}(u)}{|b|}.
\]

這給幾何 Lipschitz 空間上相應算子的譜半徑不超過 `rho`。取 `f=0` 時，中心 `P_f=h_T` 是流熵所對應的壓力零點；結論不是對任意實部的同一組高頻常數。

## 4. 定理二：一般高頻定理所需的幾何內容

來源：Stoyanov (2011) 作者稿 §1.1、§2，**Theorem 1.1**。

定理要求 `C^2` Axiom A 流、`C^2` 完備 Riemann manifold 上的 basic set，並有下列三類條件：

1. **Local non-integrability (LNIC)。** §2、式 (2.1) 要求：對指定局部不穩定切向方向，可在足夠小鄰域找到兩個不同的穩定參照點，使 temporal-distance 差在一個方向錐內滿足
   \[
   |\Delta(\exp_z^u v,\pi_{\tilde y_1}(z))
    -\Delta(\exp_z^u v,\pi_{\tilde y_2}(z))|
   \ge\delta\|v\|.
   \]
   量詞包括對 `Lambda` 附近相關切向、縮小鄰域及符合方向錐的 `v` 的局部一致性；不是單一軌道上的不等式，也不是只排除精確頻率共振。
2. **Regular distortion along unstable manifolds。** 令
   \[
   B_T^u(z,r)=
   \{y\in W^u_{\epsilon_*}(z):
      d(\phi_tz,\phi_ty)\le r\text{ for }0\le t\le T\},
   \]
   其中 `epsilon_*` 固定一個足夠小的局部 unstable plaque 尺度。§1.1 要求某 `epsilon_0>0` 下：(a) 對任意 `0<delta<=epsilon<=epsilon_0`，`diam(Lambda cap B_T^u(z,epsilon))` 與較小半徑版本的直徑比，對全部 `z,T` 有一致上界；(b) 給定 `epsilon` 與任意 `rho in (0,1)`，可選 `delta<=epsilon`，使較小半徑版本的直徑對全部 `z,T` 不超過較大者的 `rho` 倍。
3. **Uniformly Lipschitz stable holonomy。** 沿局部穩定葉的 holonomy 必須一致 Lipschitz；僅有 Hölder 正則性不足以直接滿足這一前提。

其勢、算子空間及 eventually contracting 結論與 §3.2 所列幾何 Lipschitz／頻率範數型式相同。Theorem 1.1 後的一維情況說明指出：一維 unstable laminations 有 regular distortion，一維 stable laminations 的局部 holonomy 為 Lipschitz，並說明 contact 情況的 LNIC 來源。這些是可引用的定理性幾何輸入，不是本項目同步更新收縮常數的另一種寫法。

該節另提及透過 smoothing 推至幾何 Hölder 函數、配合適當頻率範數的估計。此處沒有讀到能直接識別為我們 **指定符號度量與完整 `C^beta` 空間** 的定理，所以不藉這句說明跳過編碼／空間比較。

## 5. 定理三：自然障礙物編碼的受限接口

來源：Petkov–Stoyanov (2009) 作者稿 Introduction、§3.3，**Theorem 4／式 (3.16)**，並核讀其依賴的 Lemma 1、Theorem 3／式 (3.14)、Proposition 4／式 (3.13)。

### 5.1 前提與適用類別

全文幾何前提為至少三個互不相交的嚴格凸障礙、`C^r` 邊界且 `r>=3`、no-eclipse。Theorem 4 列出 (P)、(NF)、(ND)：

- (P) 是 §3.3 所列 pinching 條件。
- (NF) 排除在每個相關局部 unstable manifold 中，以正餘維 `C^1` 子流形包含其與 `Lambda` 的全部局部交集。
- (ND) 是該篇 §3.3 所定義、限制於 `Lambda` 切向的 symplectic 非退化条件。

作者明言平面情況三條均成立。這是較早來源自身的前提清單；不應把其中 (NF) 再加到後來 Theorem 6.3 的前提，也不應默認不同版本的 (ND) 逐字相同。

核心限制是測試函數須滿足

\[
u\circ S\circ\psi^{-1}\in C_{\mathrm{Lip}}(U),
\]

其中 `S`、`psi` 是**作者構造的兩套編碼之間的映射**，`U` 使用來自物理相空間的幾何距離。定理不是以任意符號 Hölder 函數作輸入。Theorem 4 文面以實值 `u` 陳述；若另寫複值全空間版本，应明列其線性延拓及範數控制，而不是讓引用範圍悄悄變動。

### 5.2 估計型式與共調控制

以來源的自然編碼 roof 記為 `f_tilde`、附加勢為 `g_tilde`，壓力零點為 `s_0`。Theorem 4 給定有界實部窗口後，存在 `sigma_0<s_0`、`C_0>0`、`rho in (0,1)`，對

\[
s=\sigma+ib,\quad \sigma\ge\sigma_0,\quad
|\sigma|\le A,\quad |b|\ge1,\quad
n=p\lfloor\log|b|\rfloor+\ell,
\]

在來源指定的 `p,ell` 範圍內，有

\[
\left\|
  (L_{-s\tilde f+\tilde g}^{,n}u)
  \circ S\circ\psi^{-1}
\right\|_{\mathrm{Lip},b}
\le C_0\rho^{p\lfloor\log|b|\rfloor}
e^{\ell P(-\sigma\tilde f+\tilde g)}
\|u\circ S\circ\psi^{-1}\|_{\mathrm{Lip},b}.
\]

這裡 `A` 只是有界實部窗口，不是本項目鄰接矩陣或圓盤半徑。原式以 `0<=ell<=floor(log|b|)-1` 表示剩餘步數；實際高頻使用時應同時選取足夠大的 `|b|`，避免把分塊記法退化於小頻率的情形當成額外結論。

Lemma 1 與 Theorem 4 的證明另外控制共調乘子 `h_s,d_s`：在有界實部窗口，相關 sup 範數及比值受控，其 Lipschitz 常數為 `O(|b|)`。式 (3.13) 的代數關係必須連同這些頻率範數控制使用。

**直接反對意見。** Introduction 明確區分自然障礙物編碼與 Markov-family 編碼；其可用高頻估計的函數類不是某個完整 `F_theta(Sigma_A^+)`。作者亦明說，對應特徵值相同不推出兩邊迭代範數有相同估計。本檔採用的是這個適用範圍限制，不把作者對更大空間的疑慮升格成「已證不存在任何延伸定理」。

## 6. 前提—項目映射

| 項目 | 已有直接支撐或可引用來源 | 本次審查後仍需保留的邊界 |
| --- | --- | --- |
| 平面、三個 `C^infty` 正曲率圓盤、互不相交 | 固定原幾何，中心間距 `6a`、半徑 `a` | 符合上述障礙物類別，不需另加高維遠距假設 |
| No-eclipse | [双向編碼筆記](internal_biinfinite_coding_and_roof_locality_20260909.md) §1：間隔 `(3sqrt(3)-2)a>0` | 是真實幾何條件，不是由符號矩陣混合性代替 |
| 全 trapped 碰撞非擦邊 | 同筆記 §1、§3 的 `chi>=kappa_*=(2sqrt(6)-1)/6>1/2`；其上游為 [非擦邊筆記](internal_uniform_nongrazing_on_trapped_collisions_20260908.md) | 直接支撐物理局部正則性；本身不等於 LNIC 或 stable holonomy 的證明 |
| 雙向盤字與原 roof | 雙向編碼筆記 §3–§5：唯一實現、真實首次飛行、拓撲共軛、原 roof 的符號 Hölder 界 | 同步更新收縮不等於物理切向雙曲性；不把雙側結論自動當成 Markov 單側接口 |
| Hyperbolic basic set、平面 (P)、非整合性與正則性 | 上列開放台球／一般流的已核讀來源可提供定理性輸入；不是全數未知猜想 | 若採用，應正式記錄其真實 billiard 物件與項目 trapped set 的識別、選定截面和適用版本；不能標成由本項目初等收縮自行證明 |
| Markov roof `tau_M` 與逐碰撞一側 `g` | 同一物理時間來源，但目前尚未在本分支材料中識別兩套算子 | 需精確編碼／返回時間／共調關係；更换截面後不能默認一次迭代仍等於一次碰撞 |
| 整個固定 `C^beta(Sigma^+,d_theta)` | 主線已有基本算子結論；本次沒有核讀到可直接套用的全空間高頻定理 | 需證明函數空間比較、共調乘子及頻率範數控制；幾何 Lipschitz 或其拉回空間不能只更名為原 `C^beta` |

上表的「可引用來源」與「本項目已直接證明」是不同證據類別。引用已發表定理不要求將所有幾何論證重新證一遍，但要求把真正適用的物件、空間和結論對齊。

## 7. H30 的最近接口義務

1. **確定幾何算子。** 選定可引用來源使用的 Markov family、`U`、幾何距離、返回映射及真實時間 `tau_M`，說明其與固定三盤物件的關係。
2. **保留原時鐘。** 明列 `tau_M` 與目前逐碰撞一側 `g` 的編碼／累加／共調關係，不藉換截面修改物理週期，亦不混同兩種迭代步數。
3. **明列函數類。** 可先採用由 `C_Lip(U)` 拉回的幾何函數空間；如仍要求完整固定符號 `C^beta` 上的結論，另證比較或 smoothing／resolvent 接口。現有符號到物理的 Hölder 上界，不推出每個符號 Hölder 函數轉至物理座標後皆為 Lipschitz。
4. **追蹤頻率。** 頻率共調乘子及比較映射的 sup、Hölder／Lipschitz 常數須對 `b` 明列。不能只用代數共軛、逐頻等價範數或形式特徵值對應，聲稱一致的高頻迭代估計。

在同一個 `C_Lip(U)` 空間，`||.||_Lip,b` 對每個固定非零 `b` 與固定 Lipschitz 範數等價，因此不改變該固定 `b` 的譜；但等價常數依賴 `b`。例如 `|b|>=1` 時

\[
\|u\|_{\mathrm{Lip},b}\le\|u\|_{\mathrm{Lip}}
\le |b|\|u\|_{\mathrm{Lip},b}.
\]

故從上述頻率範數界直接轉回固定 Lipschitz 範數，通常要保留多項式頻率損失。這一基本比較仍只在同一 Lipschitz 空間內，並不完成到原符號 `C^beta` 的遷移。

本輪對候選 H30 的安全表述為：**「有已發表幾何來源支持的高頻候選；固定符號全空間接口待證。」** 本次既沒有證明它在當前空間成立，也沒有證明這種接口不可能建立。

不由本筆記推出核性、Hilbert 自伴性、全局 determinant 相等、量子共振等同或任何 Route／Stage 升級。非格點性與高頻抵消仍分開；抽象正 Hölder roof 定理不代替真實幾何高頻定理。

## 8. 實際檢索、讀取與保全紀錄

### 8.1 已完成的普通網頁检索

前一審查階段使用普通瀏覽搜尋，不使用書目 API 或外部模型。實際查詢字串為：

- `Stoyanov open billiards Dolgopyat estimates pinching condition Lipschitz Ruelle transfer operators`
- `Stoyanov spectrum Ruelle transfer operators open billiard non integrability condition regular distortion d obstacles`
- `"Correlations for pairs of periodic trajectories for open billiards" journal 2010`
- `"Spectra of Ruelle transfer operators for Axiom A flows" Nonlinearity 2011 1089 1120`

繼而開啟上述三份一手作者稿及相應出版身份頁，以 `Theorem 6.1`、`Theorem 1.1`、`Corollary`、`regular distortion`、`(LNIC)`、`n = 2`、`3.14`、`Lipschitz`、`boundaries` 等字串定位相關段落，並讀取其前後定義與定理。

第一篇出版社 PDF 入口重導至摘要／存取頁，因此定理正文使用公開 arXiv v4，而不是宣稱讀到受限的出版版全文。對第三篇作者 PDF 的一次頁面截圖請求逾時；本檔不把該失敗計為圖像核驗，所用定理內容來自已取得的遠端文字段落。未執行本地 PDF preflight，章節／定理定位規則見 §2。

搜尋中亦出現更早版本、研究平台摘要和其他題目；除上列實際核讀內容外，未將它們列為本檔定理支撐。本次不是窮盡文獻回顧，也沒有「不存在更新定理」或新穎性宣稱。

### 8.2 本地只讀與唯一寫入

此前以 `rg` 搜尋 P30 相關內部筆記的 pinching、Dolgopyat、nonintegrability、distortion、holonomy、Hölder／Lipschitz、譜及高頻邊界。雙向編碼與 roof locality 筆記已在本分支先前任務完整讀取；其他上游筆記的本次命中不被冒稱全篇再讀。

本次保存階段先以 `test ! -e` 確認本檔不存在，再用 `apply_patch` 唯一新增本檔。未追加新搜尋、未下載本地 PDF、未上傳私人材料、未運行科學或符號程序、軌道枚舉、數值實驗、稿件構建或正式驗證器；沒有改動旧筆記、現稿、程式、資料、授權鎖、失敗紀錄或正式狀態。

這是一份 AI 輔助、來源定位與假設範圍的內部審查記錄，不是完整證明驗證、外部獨立再現、正式 Gate 證書或出版就緒認證。
