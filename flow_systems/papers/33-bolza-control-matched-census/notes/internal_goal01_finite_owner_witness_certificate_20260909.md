# P33 內部理論：完整 owner 關係的有限見證界與編碼中立證書

日期：2026-09-09 UTC。Goal01 授權範圍內的紙面研究；唯一新增為本文件。不實作或執行 producer、checker、BFS、census、符號枚舉或科學實驗；不修改既有合同、回執、guard、現稿、Route 或 Stage 狀態。固定 S01 控制群、曲率負一的基底測地長度、`Lambda=21/10`、磁場鎖及外部逆元配對 owner 規則。

本文接續[軸到中心覆蓋][coverage]、[中心分離與容量][separation]及[精確有限字判定][exact]，補上先前尚以額外假設表述的完整群共軛、根與逆向 owner 關係。前半給出有限見證域；後半完成下一最小引理：不依賴特定 JSON 或 canonical bytes 的有限清單語義，以及完整消費該清單的 checker 之條件性 soundness 與 coverage。這是數學規範，不是已產生的實例證書。

## 1. 固定對象與條件

設 `Gamma < PSU(1,1)` 是同一真實曲面的離散、無撓、定向保持群，`o=0`。假設以下幾何資料已成立，本文不替另一份幾何證明預先出具認證：

1. `D` 是閉、凸、緊的真基本多邊形；translates 覆蓋雙曲平面，且不同元素的 tile 內部不交。
2. `B(o,r_in) subset int(D)`，其中 `r_in>1/2`；並且 `D subset closed B(o,3)`。
3. 真實 face-to-face 側鄰接及完整頂點 star，恰由固定八字母 `A=(g0,g1,g2,g3,g0^-1,g1^-1,g2^-1,g3^-1)` 給出。本文用右乘邊 `h -> ha`；實際編碼必須保持此約定或證明一致的轉換。
4. 每個有限字與真實矩陣作用精確綁定；`PSU` 相等、closed guard、hyperbolicity 及 `ell<=21/10` 的比較都有可靠且終止的有限判定。[精確判定筆記][exact]提供此項的紙面來源，不等於任何現有 codec 已驗證。

記

\[
r_o(g)=d(o,go),\quad C_x=\{g:r_o(g)\le x\},\quad
T=2\operatorname{arcosh}\sqrt{20000},\quad\Lambda=21/10.
\tag{1}
\]

`C_T^0` 仍只表示原 guard 的 identity-connected component。已有位移公式把此 guard 精確寫成 `abs(alpha_g)^2<=20000`；已有覆蓋證明給出

\[
T>\Lambda+9=111/10,\qquad
C_{\Lambda+6}\subset C_T^0,
\tag{2}
\]

且每個 `ell<=Lambda` 的雙曲共軛類有代表在 `C_(Lambda+6)`。本文的輔助有界字域不是改變 (1) 的 guard，也不是聲稱 `C_T=C_T^0`。

## 2. 中心分離加外半徑，才給全局正長度下界

由內切球的 translates 內部不交，不同群中心距離至少為 `2r_in>1`；故

\[
r_o(g)\ge1\qquad(g\ne1).
\tag{3}
\]

這是固定基點的中心分離，**不是**直接的 systole 下界。對雙曲元 `g`，若其軸距 `o` 為 `rho`，已有雙曲位移公式等價於

\[
\sinh\frac{r_o(g)}2
=\cosh\rho\,\sinh\frac{\ell(g)}2.
\tag{4}
\]

在 `g` 軸上選點並共軛進 `D`，所得代表 `h` 的軸距滿足 `rho_h<=3`。用 (3)–(4) 才得到

\[
\boxed{\ell(g)\ge\sigma:=
2\operatorname{arsinh}\frac{\sinh(1/2)}{\cosh3}>0.}
\tag{5}
\]

(5) 對本節條件下的所有雙曲元素成立；外半徑、軸共軛及同一群作用均不可省略。這不是 Bolza 的 strict-systole gate，也沒有將控制群結果移植到 BP。

下面給根指數所需的有理保守界，不估算實際 systole。由 `n!>=2*3^(n-2)` (`n>=2`，從 `n=4` 起嚴格)，有 `e<11/4`；因此

\[
\cosh3<\frac{(11/4)^3+1}{2}=\frac{1395}{128}<11,
\qquad \sinh(1/2)>1/2.
\tag{6}
\]

令 `z=sinh(1/2)/cosh3>1/22`。積分及單調性給

\[
\operatorname{arsinh}z
=\int_0^z\frac{dt}{\sqrt{1+t^2}}
\ge\frac{z}{\sqrt{1+z^2}}
>\frac{z}{1+z}>\frac1{23}.
\tag{7}
\]

故 `sigma>2/23>1/12`。若 `a^m=g`、`m>=2` 且 `0<ell(g)<=Lambda`，則 `a` 也是雙曲元且 `m ell(a)=ell(g)`，所以

\[
m\sigma\le\Lambda,\qquad
m<126/5,\qquad \boxed{2\le m\le25.}
\tag{8}
\]

保留 `25` 作後文清單的統一保守端點；不利用更精細取整來縮小搜索域。

## 3. 共軛子與所有根的中心界

令

\[
Q=\operatorname{arcosh}
\frac{\sinh(T/2)}{\sinh(\sigma/2)},
\qquad B=2Q+\Lambda/2.
\tag{9}
\]

其參數均明確且正；`T>1` 而 `sigma<1`，故 `arcosh` 的引數大於一。由 (4)–(5)，任何雙曲 `g in C_T` 的軸距均不超過 `Q`，不要求軸與 `D` 相交，也不要求 `g in C_T^0`。

**命題 1（完整群共軛見證界）。** 若 `g,h in C_T`、`0<ell(g),ell(h)<=Lambda`，且存在 `k in Gamma` 使 `kgk^-1=h^epsilon`、`epsilon in {+1,-1}`，則存在同樣滿足等式的 `k'`，且

\[
\boxed{r_o(k')\le B.}
\tag{10}
\]

**證明。** 在兩軸上取距 `o` 最近的點 `p_g,p_h`。`kp_g` 位於 `h` 的軸。沿該軸，`h` 每次平移 `ell(h)`，所以有整數 `n` 使 `d(p_h,h^nkp_g)<=ell(h)/2`。令 `k'=h^n k`；左乘 `h^n` 不改變原共軛等式，而

\[
d(o,k'o)\le d(o,p_h)+d(p_h,k'p_g)+d(k'p_g,k'o)
\le Q+\Lambda/2+Q.
\tag{11}
\]

此處調整的是軸上的週期位置，不是假定一個任意既有共軛子已短。□

若兩軸另已認證交 `D`，直接取交點可改善為 `r_o(k')<=6+Lambda/2=141/20`。這個小界不適用於未定位的任意 guard states，後文統一採用 (9) 的 `B`。

**命題 2（完整群根見證界）。** 若 `g in C_T` 雙曲且 `a^m=g`、`m>=2`，則 `a,g` 同軸，`ell(a)=ell(g)/m`；(4) 隨正平移長度單調，故

\[
\boxed{r_o(a)\le r_o(g)\le T.}
\tag{12}
\]

雙曲元素的非零整數根必為同軸雙曲元素：由 `a` 與 `g=a^m` 交換，`a` 保留 `g` 的吸引／排斥端點，並沿該軸平移；其 `m` 次平移為 `g`。這也直接給長度關係。**(12) 只把根放進 `C_T`；沒有證明根在 `C_T^0`。** 將根搜索限於原 component 仍是不充分的。

## 4. 有限、可計算的完整字域

### 4.1 原 ball-packing 字界：保留通用版本

由 (3)，半徑 `1/2` 的中心開球兩兩不交。雙曲球面積為 `2pi(cosh r-1)`，故對任意有限中心子集比較面積得到

\[
\#C_x\le P(x):=
\frac{\cosh(x+1/2)-1}{\cosh(1/2)-1}<\infty.
\tag{13}
\]

同一上界適用於所有有限子集，因而亦證明整個 `C_x` 有限，沒有循環依賴未知的群元素數。對本文的明確可計算非負參數 `x`，選一個整數 `N(x)`，並攜帶正確的有理上包圍證書使

\[
P(x)<N(x),\qquad L(x):=N(x+3)-1.
\tag{14}
\]

不要求計算 `ceil(P(x))` 的精確值：先取得有限有理上界，再取更大的整數即可。`T,sigma,Q,B` 由正確分支上的可計算初等函數組成，正分母與分支內點已有證明，因此可逐步取得所需有理包圍。這是一個有限、可計算的紙面選界原理；本文沒有算出或執行 `N` 的實例。

若 `r_o(u)<=x`，既有完整 tile／頂點 star 論證給一條從 `1` 到 `u`、留在 `C_(x+3)` 的側鄰接路徑。刪除迴圈後，長度至多 `#C_(x+3)-1<=L(x)`，所以

\[
\boxed{r_o(u)\le x\ \Longrightarrow\ |u|_{\mathcal A}\le L(x).}
\tag{15}
\]

### 4.2 線段 tube-packing 改進與本規格採用的字界

保留 (13)–(15) 作通用的有限性／可計算性證明，但不再以其粗大球容量作本節主字清單的深度。令 `u in Gamma`，取線段 `J=[o,uo]`，長度 `x=r_o(u)`。凡 tile `hD` 與 `J` 相交，其中心 `ho` 距 `J` 至多 3；以這些中心為心的半徑 `1/2` 開球兩兩不交，且都在 `J` 的半徑 `7/2` 管狀鄰域內。

半徑 `v` 的線段管狀鄰域由 Fermi 座標長條與兩個端點半圓帽組成。雙曲面參數化 `(cosh(t)cosh(s),cosh(t)sinh(s),sinh(t))` 的 Lorentz 線元直接給 `dt^2+cosh(t)^2 ds^2`，故長條面積元為 `cosh(t) ds dt`；兩個半圓帽合成一個半徑 `v` 的球面積，因此

\[
\operatorname{Area}(\operatorname{Tube}_v J)
=2x\sinh v+2\pi(\cosh v-1).
\tag{15a}
\]

若 `M` 是所有與 `J` 相交的 tiles 數，面積比較給

\[
M\le Ax+B_0,\qquad
A=\frac{\sinh(7/2)}{\pi(\cosh(1/2)-1)},\quad
B_0=\frac{\cosh(7/2)-1}{\cosh(1/2)-1}.
\tag{15b}
\]

由 (6) 的 `e<11/4<25/9` 得 `e^(1/2)<5/3`，因而 `e^(7/2)<6655/192`。再用 `cosh(1/2)-1>1/8` 及 `pi>3`，得到直接有理上界

\[
A<\frac{6655}{144}<47,\qquad
B_0<\frac{6463}{48}<135.
\tag{15c}
\]

後一式使用 `cosh(7/2)-1<(e^(7/2)-1)/2`。完整頂點 star 保證這批與 `J` 相交的 tiles 的側鄰接圖連通，包含 `D,uD`；刪環路得字長至多 `M-1`。若 `X` 是經認證的非負整數且 `X>=x`，則 `M<47X+135`，整數取整後得

\[
\boxed{|u|_{\mathcal A}\le47X+133.}
\tag{15d}
\]

現在證明所需 `X`，不做矩陣數值 replay。指數正項和給 `e>1+1+1/2+1/6+1/24=65/24>8/3`，故 `cosh6>(8/3)^6/2=131072/729>142>sqrt(20000)`，所以 `T<12`。又
`cosh Q=sqrt(19999) cosh3/sinh(1/2)<142*11*2=3124`，而 `cosh9>(8/3)^9/2=67108864/19683>3124`。因此

\[
\boxed{T<12,\quad Q<9,\quad B<18+21/20=381/20<20.}
\tag{15e}
\]

對根用 `X=12`、對命題 1 的共軛子用 `X=20`，本規格採用固定深度

\[
\boxed{\widehat L_r=47\cdot12+133=697,\qquad
\widehat L_c=47\cdot20+133=1073.}
\tag{15f}
\]

令 `W_c` 為八字母所有長度 `0,...,1073` 的字，`W_r` 為所有長度 `0,...,697` 的字；兩者均包括空字及非約化字。同一群元素可有多個字，字清單不得因未證明的 normal form 或自訂去重而刪項。由 (8)、(10)、(12)、(15f)，完整共軛／逆配對／根問題已被壓到

\[
kgk^{-1}=h^{\pm1}\quad(k\in W_c),
\qquad a^m=g\quad(a\in W_r,\ 2\le m\le25).
\tag{16}
\]

這些輔助字與其中間前綴可離開原 guard；它們只供精確見證測試，不能混入 `C_T^0` 的 included stream。可計算性與有限性**不等於可行性**：即使採改進後深度，完整字樹仍有 `1+8+...+8^L` 個字，且未給每次代數判定的實用位元成本、記憶體或時間保證。`697`、`1073` 是存在見證的保守字長上界，不是實測深度或 census 數目。

## 5. 編碼中立的有限證書清單

以下是帶索引的數學清單，不指定 JSON 欄位、canonical bytes、排序流或 digest。任何實作可選自己的容器，但必須證明其解碼與本節清單逐項對應；重複項不得抵銷缺項，跳過或 unresolved 不得解讀為否定結果。

### A. 固定輸入與界

攜帶 §1 的同一群、基點、長度規範、八字母、乘法方向、原 guard／cutoff、外部逆元規則，以及 (5)、(8)、(9)、(15a)–(15f) 的證明。本規格主版本固定 `widehat L_r=697,widehat L_c=1073`；(14) 的 `N,L` 只保留為通用前輪界，不是主清單的額外生產資料。幾何前提是條件定理的輸入，不能由本清單自行產生 `PASS`。有限字矩陣必須重播到同一精確表示，不能只比對 hash 或小數。

### B. 原 component 的狀態與全部八邊閉包

給有限狀態表 `U`。每項帶字見證與精確矩陣，並驗證：

- 每一字與所列矩陣精確綁定；相異狀態代表相異 `PSU` 元素；恆等元恰列一次；每項滿足原 closed guard。
- 每個非恆等狀態有一個已驗證的父狀態與字母邊；父鏈有限回到恆等元，且全在 `U` 內。
- 索引集合恰為 `U times A` 的完整出邊表。每列只有一項可靠結論：乘積在 `PSU` 中精確等於某個 `U` 狀態，或精確證明乘積在原 closed guard 外。每一組索引恰消費一次。

父鏈證明可達性，完整出邊證明沒有遺漏；這兩者不同。本文不以此替代 CP 合同另外要求的 FIFO 次序與全部序列／版本綁定。

### C. 每個狀態的閉測地候選分類

對 `U` 的每項完整消費 hyperbolicity 判定；對每個雙曲狀態完整消費 `ell<=Lambda` 的精確比較。令 `H` **恰為**被判定為雙曲且在 cutoff 內的狀態。等號分支必須明確處理或引用對精確對象成立的排除證明；interval 跨界不能當成排除。這一步禁止只列「看起來短」的子集。

### D. 兩個完整有界字清單

字清單以字串地址區分，不以群元素身份區分。完整性的編碼中立規則是：根地址為空字且矩陣為恆等；每個非空地址的唯一父地址是刪除末字母所得前綴，且必列於表；每個深度小於指定 `L` 的地址恰有八個追加字母的子地址；深度 `L` 恰為葉；沒有重複地址或額外深度。每個非根矩陣從父項乘相應固定字母而來，且精確驗證。由深度歸納，這恰列出所有長度不超過 `L` 的字及其實際矩陣。

分別以 `L=1073,697` 建立 `W_c,W_r`；若共享前綴資料，仍須檢查兩個索引域的完整性。這是紙面完整字樹規則，不是在本輪建立巨大字樹。

### E. 根測試的完整乘積索引

對**每個** `(g,a,m) in H times W_r times {2,...,25}`，記錄並精確驗證布林值

\[
R(g,a,m)=[M_a^m=M_g\text{ in }PSU].
\tag{17}
\]

真值攜帶等式證明；假值攜帶不等式證明。禁止把「沒有列真值」當成已消費所有假值。定義 `P` 恰為沒有任何真根列的 `H` 元素；其他元素均列為非本原，並可指向任一真列作正見證。根候選 `a` 無須在 `U`，不能因其不在 `U` 就跳過。

在精確 `SU` lift 層，真值要求全矩陣使用同一個 `+` 或 `-` 符號；假值要求兩個整體符號皆不成立。所需判零／非零來自[指定嵌入的精確域][exact]，不是逐 entry 任選正負，也不是「超過某個小數容差」。

### F. 共軛與逆配對的完整乘積索引

對**每個** `(g,h,epsilon,k) in H times H times {+1,-1} times W_c`，記錄並精確驗證

\[
C(g,h,\epsilon,k)=[M_kM_gM_k^{-1}=M_h^{\epsilon}\text{ in }PSU].
\tag{18}
\]

真／假值使用與 E 相同的整體 `PSU` 比較規則。定義 `E_+(g,h)`、`E_-(g,h)` 分別為相應 `epsilon` 的有限析取；因此完整有向共軛及其逆配對結果都保留。定義 `g~h` 當且僅當 `E_+` 或 `E_-` 成立，不能改用等長、等跡、同調或字串相似。

### G. owner 商及輸出完整性

提供 `P` 的分割與每塊恰一個輸出代表；驗證每個 `P` 狀態恰屬一塊，且對所有 `g,h in P`，同塊**當且僅當** `g~h`。輸出表與分塊表必須一一對應，不得漏塊、重複出塊或加入 `P` 外元素。這一步只規定真實 owner 商，不發明新的 canonical owner bytes 或取代既有排序規則。

## 6. 下一最小引理：完整消費的 soundness 與 coverage

**定理（有限 owner 語義證書）。** 在 §1 前提下，若一個 checker 可靠地驗證並完整消費 §5 A–G 的每個規定索引與證明，且只在全數成立時接納，則其語義 owner 輸出與真實 `ell<=Lambda` 的本原共軛類再作外部逆元配對所得集合雙射。其根與有向／逆向共軛表亦分別具有完整群意義。此定理不假定任何特定 checker 已存在或曾運行。

### 6.1 Soundness：接受的判定和輸出不會冒充真 owner

先看狀態。字綁定保證 `U` 的每項確屬同一 `Gamma`；guard 與父鏈保證 `U subset C_T^0`。分類表保證 `H` 每項真是 cutoff 內的雙曲元，不以非雙曲字充當閉測地線。

每個真根列與真共軛列都是完整群的實際等式，故不會偽造「有根」或「等價」。對假值不能只援引單列正確：若某 `g in P` 在全群有根，(8)、(12)、(15f) 必將某個真根見證放入 E 的完整索引域，與所有根列均假矛盾。因此 `P` 每項在完整群中本原。若某兩個被放在不同塊的 `P` 元素實際共軛或逆配對，命題 1 與 (15f) 必將真見證放入 F 的完整索引域，亦矛盾。

反過來，同塊的兩項由 G、F 有真實共軛／逆配對見證。故每塊只代表一個真 owner，且不同塊不代表同一 owner；每個輸出代表屬於該塊的真本原短元素。這證明語義輸出到真 owner 集的映射良定且單射。負判定的正確性依賴已證見證界及完整字域，不能從單個不等式或「搜尋未找到」取得。

所用真實關係確為等價關係：恆等共軛給反身性，反轉共軛等式給對稱性；若 `kgk^-1=h^epsilon`、`lhl^-1=j^eta`，則 `(lk)g(lk)^-1=j^(eta epsilon)`，給傳遞性。故完整真值表確可作 owner 分割。

### 6.2 Coverage：不漏原 component、短類或全群見證

若 `C_T^0` 中有未列於 `U` 的元素，沿定義中的域內字母路徑取第一個遺漏者。前驅在 `U`，其該條出邊已由 B 完整消費；域內乘積不能合法判成 guard 外，只能指向 `U`，矛盾。結合 soundness 的包含關係，得 `U=C_T^0`。

任取真實 cutoff 內本原 owner。已有軸到中心及鄰接覆蓋 (2) 給出同 owner 的本原代表 `g in C_T^0`，故在 `U`。C 的完整分類將其放入 `H`；由其本原性及精確比較，E 不可能有真根列，故 `g in P`。G 完整消費 `P` 的分割及每塊輸出，因此該 owner 必被輸出。這證明滿射，與上節單射合成雙射。

同樣論證把每個非本原短共軛類也覆蓋到 `H`。對任一 `g in H` 的任意全群正整數冪根 `a^m=g` (`m>=2`)，(8)、(12)、(15f) 保證至少一個表示該根的字被 E 消費；對任意 `g,h in H` 的全群共軛或逆配對，命題 1 及 (15f) 保證至少一個被 F 消費的有界見證。因此根表與兩個有向關係表不只是 primitive output 的局部附屬測試。

### 6.3 本原根存在唯一，與表中最大指數一致

固定雙曲 `g` 的軸。保留該軸但交換兩端點的定向保持雙曲平面等距會在軸上作反射；共軛到上半平面的軸端點 `0,infinity` 後，它形如 `z -> -c/z` (`c>0`)，其平方為恆等。無撓性排除此情形。其餘軸穩定子在軸上作平移，且平移參數唯一決定等距；因此該穩定子嵌入 `(R,+)`。

離散群中的這些參數構成離散加法子群：若有非零參數趨零，相應同軸等距就趨向恆等，違反群離散性。非零離散實數加法子群有最小正元 `s`：正參數下確界若不取到，取相異且任意接近它的參數，其差就給非零參數趨零。任意參數除以 `s` 的餘數只能為零，故此群為 `sZ`。因此存在唯一與 `g` 同方向的本原根 `p`，使 `g=p^m`、`m>=1`。

若需要為每個非本原 `g in H` 附上本原根，可在 E 的真列加上平凡候選 `(g,1)`，取最大指數。若所取根還有根，指數相乘得到 `g` 的更大指數；(8) 保證此指數仍不超過 25，完整根表便會出現，矛盾。不同字表示同一根時須用精確 `PSU` 去重。所得根仍可能不在 `U`；本節不因附加根資料而改寫原 included stream。

## 7. 有限證書存在性、界限與後續接口

條件前提也保證某份 §5 的有限語義證書存在：`C_T^0` 有限，可給每項有限字和可達樹；所有八邊比較與候選分類終止；§4 給有限字深度；有限個精確矩陣比較分別終止；最後對已知真實有限等價關係分塊即可。這是存在性／可判定性的紙面構造，不是建議直接展開巨大字樹，更不聲稱實用。

本輪已補完的數學接口是「有限狀態覆蓋 + 有限全群見證覆蓋 -> 正確完整 owner 商」，而非只有 word equality。接下來若獲實作授權，尚須證明實際 parser、state codec、字目錄索引器、比較器及商輸出與 §5 逐項雙向綁定；任何壓縮字域、縮短界或省略負表的優化亦需要自己的完備性定理。

[CP 合同][cp-contract]仍另外要求 FIFO、規範 bytes、排序流、版本／digest 綁定、零 unresolved ledger 與獨立 replay。本文未生成這些材料，未填任何版本或 observed digest 空槽；`execution_performed=false` 不變。[BP 合同][bp-contract]仍走其獨立 strict-systole gate，本定理不更換其路線。

舊 `18533` 狀態、`depth 11`、既有 accepted digest、歷史 `PASS/PROVED` 或任何舊容量標籤，都不是本次 census／性能／checker 的證據。本文也沒有取得實際 owner 數、狀態數、記憶體或運行時間。

## 8. 方法、來源與實際動作

使用當前 ARS academic-paper 的 bounded argument-builder；將條件、直接紙面推導、清單規範、soundness、coverage 與未實作接口分開。不啟動 full pipeline、正式 reviewer 或 Route assessment。已完整讀取適用的 ARS router、academic-paper workflow、argument-builder role、`AGENTS.md`、`docs/workflow.md`，以及本文所引三份前輪筆記和 BP／CP 合同。

新公式與定理均在本文直接推導；引用前輪來源只承接其中明示的精確對象與條件性引理，沒有重訪外部來源、外部模型／API、符號程序、producer、checker、census 或實驗。唯一寫入為 `apply_patch` 新建本文件；只讀定位、讀取、檔案保全及文本結構檢查不構成群論定理的獨立科學認證。

寫後只讀文本檢查通過 24 對顯示數學分隔符、公式標籤 `(1)–(18)` 及插入的 `(15a)–(15f)`、五個引用定義與全部本地目標，以及控制字元、行末空白、衝突標記和末尾換行檢查。三份前輪筆記及 BP／CP 兩份合同的 SHA-256 均與寫前相同；保全結論只涵蓋這五個已比對舊檔，不聲稱已審計整個共享工作區。

[coverage]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_axis_to_center_coverage_and_finite_guards_20260908.md
[separation]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_inradius_separation_and_explicit_guard_capacity_20260909.md
[exact]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/internal_exact_state_identity_and_guard_decidability_20260909.md
[cp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/cp_enumeration_contract.json
[bp-contract]: /root/autodl-tmp/flow_systems/papers/33-bolza-control-matched-census/notes/stage4_prime_round5_support/bp_enumeration_contract.json
