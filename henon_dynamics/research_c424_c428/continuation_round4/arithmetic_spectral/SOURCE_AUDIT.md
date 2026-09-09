# AS4-S 主來源與適用範圍審計

核查：2026-09-08 UTC（工具時鐘）。狀態：
`BOUNDED_PRIMARY_SOURCE_CHECK; FULL_QUESTION_UNCLOSED; NO_NEW_CONTRACT`。
本文件區分來源存在、實際正文讀取、定理適用和本輪完整主張；
不是全世界文獻的窮盡查新，也不把搜尋命中數當作新穎性證據。

## 1. 局部碰撞和檢索範圍

已讀同批 AS424-I/D/B、AS2-G/B 的凍結和 AS2-B 缺口、AS3-H 關閉
交接；並核對 `henon_dynamics/docs/obstruction_registry.md` 的 C397
Salem toral fluctuation 所有權及 `IDEA_REPORT_C379_C383.md` 的 generic
beta／multinacci 拒絕。只讀 symbolic P44–P48 既有來源表的
Flatto–Lagarias–Poonen 條目，不修改或推進該項目。不能將線性
companion 環面週期或 generic beta zeta 重新命名成獨立增量。
部分探索性 `rg` 含不存在的 glob，回傳 exit 2；有效輸出的局部
命中用於定位，沒有將它們宣稱為全庫成功審計。

本輪使用一般網頁搜尋、出版社／作者頁、arXiv 摘要及 HTML 正文。
代表性實際查詢包括：

- `Salem beta expansion eventual periodicity all Q beta Schmidt conjecture primary paper 2025 2026`
- `Salem numbers degree four periodic beta expansions Boyd theorem unit circle conjugates`
- `Salem greedy beta expansion Schmidt conjecture 2026 arxiv`
- `Salem beta transformation Q beta periodicity unit conjugates bounded orbit proof`
- `"The beta-transformation" "companion map" Maia pdf`
- `"Periodic representations in Salem bases" Vavra greedy alphabet theorem`
- `"A note on non-periodic greedy expansions in Salem base"`

搜尋頁只作定位。以下列出的正文來源才支持相應數學適用判斷。
二手彙編、百科和未讀命中未用作定理依據。沒有執行迭代程式、
下載研究 PDF、GPU 實驗、外部模型審查或稿件上傳。

## 2. 已核對來源：版本、讀取位置、可用與不可用結論

### S1. Schmidt：經典來源，但本輪未讀原正文

Klaus Schmidt，*On periodic expansions of Pisot numbers and Salem
numbers*，Bull. London Math. Soc. 12 (1980), 269–278。核對了出版社
搜尋所示書目／摘要；直接頁面開啟失敗，故不能聲稱本輪已逐頁驗證
其 Lemma 2.3。該引理的編號與歸屬由下面 S2 的實際正文確認。
[出版社 DOI](https://doi.org/10.1112/blms/12.4.269)。

### S2. Maia：companion 與有界等價的直接所有權

Bruno Melo Maia，*The beta-transformation's companion map for Pisot
or Salem numbers and their periodic orbits*，Dynamical Systems 33(1),
1–9，DOI 10.1080/14689367.2017.1288701。本輪實際讀到的是作者於
2017-11-10 上傳的正文，內頁標記 June 26, 2017、accepted January
27, 2017；出版社搜尋列 online 2017-02-26／2018 卷期，沒有把這些
日期混稱為新版本日期。出版社 abs／full 直接存取失敗。
[作者上傳正文](https://www.researchgate.net/publication/313284713_The_beta-transformation's_companion_map_for_Pisot_or_Salem_numbers_and_their_periodic_orbits)。

實際核讀 §2 定義及 companion convention、§3 Proposition 3.1
及證明、Proposition 3.2，和 §4 Theorem 4.1 的完整證明；Theorem
4.2 只讀陳述及證明開頭。Theorem 4.1 明確給出實際 beta 軌道最終
週期、companion 軌道最終週期、係數向量有界、全部共軛有界的等價，
並將機制歸屬 Schmidt Lemma 2.3。這直接擁有本輪 Proof Steps 1–2
的框架；沒有提供所有 Salem 輸入的中心坐標界。§3 的環面因子
亦不等於 greedy 狀態本身返回。[同一正文 §§3–4](https://www.researchgate.net/publication/313284713_The_beta-transformation's_companion_map_for_Pisot_or_Salem_numbers_and_their_periodic_orbits)。

### S3. Vávra：週期表示存在不等於標準 greedy 返回

Tomáš Vávra，*Periodic representations in Salem bases*，arXiv
1812.08228，實際核读 v1（2018-12-19）。讀了 §§1–2 的表示定義、
Theorems 2.1、2.3、2.5，§3 Theorem 2.1 的完整證明及 §4 Comments
3–4。主構造可選有限 alphabet 和數字選擇器，使代數數有最終週期
表示；沒有證明選擇器等於本題的 floor。Theorem 2.5 的另一項結果
排除單位圓共軛，不能代入 Salem。本輪沒有將任選表示轉作 greedy
全輸入閉合。[v1 正文](https://arxiv.org/html/1812.08228v1)。

嘗試的 v2 HTML 未成功，因此這裡不宣稱核對了其後版本。
[版本入口](https://arxiv.org/abs/1812.08228)。

### S4. Akiyama–Hichri：原來的 base 與全輸入量詞均不可替換

Shigeki Akiyama、Hachem Hichri，*Periodic expansion of one by Salem
numbers*，arXiv 2206.06675。實際讀取 v2 HTML，頁面 header 為
2022-06-16：Introduction 的 Theorems 1–2、Lemma 3 及證明、§3
Theorem 1 的完整證明。Theorem 1 為每個 Salem 數給出正密度的
整數 $m$，使 $\beta^m$ 的 $1$ 展開最終週期；不是固定
$T_\beta$ 的全 $\mathbb Q(\beta)$ 軌道界。$T_{\beta^m}$ 也不能
與 $T_\beta^m$ 視為同一映射。[v2 正文](https://arxiv.org/html/2206.06675v2)。

### S5. Hare–Orovec：2025 特定族，不作全 Salem 外推

Kevin G. Hare、Liam Orovec，*Greedy Beta-expansions for families of Salem
numbers*，arXiv 2504.10787，實際版本為 v1
（摘要頁列 2025-04-15）。讀了 Introduction、Theorems 2.1 與 2.3
的陳述／假設及證明開頭，沒有讀完全部證明。Theorem 2.3 包含指定
Pisot 極限、reversibly greedy、cofactor 和種子展開形狀等條件，
處理特定 Salem 參數族的 $1$。不作所有參數或所有 $x$ 的依據。
[v1 正文](https://arxiv.org/html/2504.10787v1)。

HTML 渲染頁另出現 2026-08-24 字樣，與 arXiv 版本入口不一致；
本輪不因此聲稱有 2026 年新提交或最新版本驗證。
[arXiv 版本入口](https://arxiv.org/abs/2504.10787)。

### S6. Boyd：實際演算法／啟發式邊界

David W. Boyd，*On the beta expansion for Salem numbers of degree 6*。
讀了作者大學站的摘要／目錄、The Basic Algorithm、Detecting
periodicity 和 Probabilistic assumptions 三節。部分公式是無文字
替代的圖片，故未聲稱精確核對所有方程；啟發式隨機遊走不被用作
實際非週期證明。正文還將全數域的 Salem 週期性指向 Schmidt
猜想背景。[作者大學站](https://www.cecm.sfu.ca/organics/papers/boyd/betaexpansion/html/paper.html)、
[演算法](https://www.cecm.sfu.ca/organics/papers/boyd/betaexpansion/html/node6.html)、
[週期檢出](https://www.cecm.sfu.ca/organics/papers/boyd/betaexpansion/html/node8.html)、
[機率假設](https://www.cecm.sfu.ca/organics/papers/boyd/betaexpansion/html/node12.html)。

### S7–S8. 已發現但不足以作正文依據的近期來源

Eiji Miyanohara，*A note on non-periodic greedy expansions in Salem
base*，Research in Number Theory 10, Article 18 (2024)，出版社標記
2024-01-29。只讀出版社摘要；PDF 入口轉到付費／存取頁，未取得
全文。摘要的條件式複雜度主張不被改成明示非週期例，也未作本輪
證明前提。[出版社頁](https://link.springer.com/article/10.1007/s40993-024-00507-8)。

Waterloo 學位論文 *Greedy and Lazy β-expansions for PV and Salem
Numbers*，儲存庫 metadata 為 2026-04-27。只確認書目／摘要頁，
未讀正文、未据此聲稱全題已解或仍無人解。
[大學儲存庫](https://uwspace.uwaterloo.ca/items/b7fcb936-d011-4c34-b7a2-ea532401d80e)。

## 3. 與凍結主張的逐項差額

| 所需內容 | 真正已取得 | 未取得／處置 |
| --- | --- | --- |
| 標準 greedy 的精確代數 lift | S2 加本輪直接重建 | 來源已有，不能准入 |
| 週期當且僅當全部共軛有界 | S2 Theorem 4.1 完整正文 | 等價不是全輸入有界性證明 |
| 分母算術對真實週期的限制 | 本輪由 unimodularity 手推：分母保持、有限商週期整除真週期 | 經典有限商 corollary；沒有控制 carry lift |
| 全 Salem／全輸入的有效判定 | 未取得 | `NOT CURRENTLY JUSTIFIED` |
| 統一嚴格二次型截留 | 本輪完整反證此特定更強機制不可能 | 只淘汰該方法，沒有原動力全類 no-go |
| 新 prime owner／目標 trace weight | 未取得 | 不能以數域或模數替代 |

若試圖以「每個實際 greedy 軌道均有界」來完成本題，便返回經典
Schmidt／Salem 最終週期猜想的全輸入內容；這不是已找到的新閉合
機制。凍結的「完整判定／分類」允許存在非週期分支，因此邏輯上
不直接等同於「全部週期」猜想，但仍須完整且有效識別各分支。
本輪沒有做到其中任何一種完整結論。

## 4. 交接與誠信界線

只凍結並嘗試 AS4-S 一題，不為第二題配額擴搜。沿用 batch／
idea-creator 的先凍結門、research-lit 的來源粒度和 proof-writer 的
全量詞缺口分離；ARS 僅協助來源適用核查，未啟動另一研究 pipeline。
完整手推和方法失敗的限制見 [PROOF_PACKAGE.md](PROOF_PACKAGE.md)。
沒有完整候選可交非作者准入審查，現有准入數不由本分支增加。
來源結果、局部手推或陰性方法測試均不推出目標 Euler factors、
root numbers、automorphy 或 zero/divisor 對應。
`NO_BAD_EULER_OR_ROOT_NUMBER`。
