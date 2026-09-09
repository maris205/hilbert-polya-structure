# ROUND4 算術返回：唯一凍結問題 AS4-S

2026-09-08 UTC（工具時鐘）。AI-assisted 作者選題；在本輪任何非平凡推導或
數學程序之前凍結。唯一寫入範圍為本目錄，無論結果如何均不自行准入。
至多兩題不是配額：本輪先只選一題。

## 1. 精確物件、全參數和全定義域

參數是所有 Salem 數 $\beta$：$\beta>1$ 為實代數整數，其最小
多項式不可約，共軛為 $\beta,\beta^{-1}$ 及其餘位於單位圓的
非實共軛；次数為任意偶數 $d\geq4$。不固定次数四、不只取某一
Pisot 極限族，也不把 $\beta$ 換成某個選取的冪。

固定標準 greedy 映射

$$
T_\beta:[0,1)\longrightarrow[0,1),\qquad
T_\beta(x)=\beta x-\lfloor\beta x\rfloor.
$$

研究輸入為全部 $x\in\mathbb Q(\beta)\cap[0,1)$，含 $x=0$、
有理和非有理輸入、全部分母。恰在分支邊界時仍使用通常 floor，
不改為 quasi-greedy、lazy、balanced 或任選有限 digit alphabet。

## 2. 原生時鐘、可觀測量及算術承載

一個 $T_\beta$ iterate 是一 tick。實際 digit 為
$a_n=\lfloor\beta T_\beta^{n-1}(x)\rfloor$，不改屋頂函數或索引。
可觀測量是軌道是否最終週期，及週期時的精確最小 preperiod、period。
完整問題要求一個對每個精確代數輸入均終止的必要充分判定，或一個
完整的全输入分類定理，並給出相應週期資料；只列出週期者不是閉合。

算術是原生數域、代數整數格點及 Galois 共軛，不是預置的目標素数。
本題沒有已建立的 rational-prime owner、$\log p$ 時鐘或精確 prime
trace weight。也不假設普通 all-input Hilbert-space trace、Fredholm
determinant 或目標 zeta 已有定义；週期分類本身是本次完整問題。

## 3. 擬攻定理及預先固定的決定性檢查

擬攻定理是上述全 Salem／全數域輸入的有效最終週期分類。
第一個實際機制是 Minkowski 共軛空間中的格點截留：保留精確
digit 決策與全部共軛，檢查是否存在由 $(\beta,x)$ 可算、並經證明
終會進入的有限格點區域。若不能截留，須給出對所有剩餘軌道均
完備的有限負證書；長前綴不重複不能作為非週期證明。

便宜檢查先做三項：

1. 確認標準共軛有界性等價於有限軌道的論證已由哪些來源擁有。
2. 推出實際 greedy digits 對單位圓共軛的精確強迫迴圈；判明
   Pisot 的收縮幾何級數界是否真的延伸到 Salem。
3. 對本輪擬用的 uniform quadratic Lyapunov 截留檢查全部分支，
   尤其零 digit 的固定原點；若此局部檢查失敗，只淘汰這一證明機制，
   不把它當作 Salem 全題不可能性。

沒有計畫做 degree／trace／迭代長度表或 GPU pilot。手推若不能
證明完整量詞，輸出精確缺口並停止，不縮為 $x=1$ 或特殊参數層。

## 4. 最近所有權與替換邊界

已讀局部碰撞：同批 AS424-I/D/B、AS2-G/B 的凍結和缺口；
AS3-H 關閉交接；Hénon C397 Salem toral fluctuation 的 registry
條目，以及 C379–C383 對 generic beta／multinacci 候選的拒絕紀錄。
另只讀 symbolic P44–P48 已存在來源表中 Flatto–Lagarias–Poonen
的 beta periodic/zeta 所有權條目，未推進或改寫 symbolic 研究。
本題是非線性 greedy 全代數輸入的返回判定，不是 C397 的線性
環面自同構，也不重寫 generic beta zeta；但這一区分不自動構成
獨立實質增量。

主要外部源候選是 Schmidt 的 Pisot／Salem 週期性工作、Boyd 的
Salem 展開研究、以及 Hare–Orovec 2025 的特定 Salem 極限族。
實際讀取版本與命題範圍另記 SOURCE_AUDIT，不把摘要當作正文證明。
若所餘只是經典有界狀態等價、Pisot 特例、任選 alphabet 週期表示、
只處理 $1$ 的展開或沒有控制單位圓狀態的猜想，處置為來源所有權
或未閉合，不能進入完整合同審查。

第二題不因本題失敗自動啟動。舊 Heisenberg 已完整且
`CLOSED_ADDENDUM_ONLY`；AS2-G 的全 $N$ 與 AS2-B 的全输入缺口保持，
本文件不重證它們、不把它們判成不可能。

## 5. 任務邊界

使用 henon-route-a-batch、idea-creator、research-lit、proof-writer；
ARS-Codex 僅作主張已定後的來源適用核查。沒有第二研究 pipeline、
外部模型、稿件上傳、TeX／PDF、正式評價、Git 寫入或新 C 編號。
來源的 source dynamics 結論不推出目標 Euler factors、root numbers、
automorphy、zero/divisor 對應或 Hilbert–Pólya 實現。
`NO_BAD_EULER_OR_ROOT_NUMBER`。
