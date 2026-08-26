# P22 Stage 4 — REV-003 author metadata validation

## 判定

**PASS（已確認事實的保存正確；REV-003 仍須維持 contribution hold）。**

stage4_rev003_author_metadata_input.json 忠實保存了原始人類事件中的作者姓名、單位與地址、電子郵件、無資助及無利益衝突資訊。JSON 沒有把電子郵件推斷為通訊作者指定，也沒有把尚未確認的 contribution 候選句提升為已確認事實。

但是，這不是 REV-003 已完成的判定：

- **Author contributions 仍未建立。** 原始事件沒有提供 contribution 或 CRediT 角色；JSON 中的 proposed_text 只能視為待作者逐字確認的候選文字。
- **Corresponding-author designation 仍未建立。** 原始事件只提供 contact email，沒有出現 “corresponding author”、星號指定、yes 或同義明確指示。

JSON 的 rev003_completion_status: WAITING_FOR_EXPLICIT_AUTHOR_CONTRIBUTION_CONFIRMATION 因而正確。不得在沒有新的人類事件時把它改成 complete。

## Provenance 與逐欄核對

- 原始事件：notes/stage4_rev003_author_event_20260825.txt
- 原始事件 SHA-256：eaac1940fcabccba6065beb59bef85566ecbd0ccf6bff3233e6abf517cd964f1
- 結構化輸入：notes/stage4_rev003_author_metadata_input.json
- 結構化輸入 SHA-256：4fecb2b01f639b8db4467c68c0b2238e0642dee6c7bb3a42fbbaffd3aaf67ba6
- JSON 內的 source_event.input_sha256 與原始事件實際雜湊完全一致。
- JSON 已通過 python3 -m json.tool 語法解析。

| 欄位 | 原始事件 | JSON 表示 | 結論 |
|---|---|---|---|
| Byline | Liang Wang | authors_in_order: [Liang Wang], status: confirmed | **PASS**；姓名與順序均未改寫。 |
| Affiliation/address | 1School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Luoyu Road 1037, 430070, Hubei, P.R. China | label 1，作者 Liang Wang，地址文字相同 | **PASS**；只合併了原始換行及補開 affiliation label 與正文的結構，沒有更正、增補或重排地址。 |
| Email | wangliang.f@gmail.com | 同一 email，status: confirmed | **PASS**；可作 contact email。 |
| Corresponding author | 未提供 | corresponding_author_status: not_explicitly_designated | **PASS**；沒有由 sole authorship 或 email 推斷通訊作者。 |
| Funding | 资助无 | status: confirmed_none；“The author received no specific funding for this work.” | **PASS**；是保守且可投稿的英語正規化。沒有虛構 funder、grant 或 funder role。 |
| Competing interests | 利益冲突 无 | status: confirmed_none；“The author declares no competing interests.” | **PASS**；語義等值，且與 funding 分開。 |
| Contributions | 未提供 | status: pending_explicit_confirmation；candidate prose in proposed_text | **HOLD**；候選句不是來源事實，不可寫入最終稿，除非作者明確批准或提供替代文字/CRediT roles。 |

## 不當推斷檢查

未發現被標成 confirmed 的不當推斷：

- 沒有把專案聯絡人、被引用作者、AI 工具或檔案作者列入 byline。
- 沒有從單作者身份推斷 Conceptualization、Formal analysis、Writing 或其他 CRediT roles。
- 沒有從 contact email 推斷 corresponding author。
- 沒有從「無資助」推斷機構支持、grant number 或 funding-acquisition role。
- 沒有把「無利益衝突」擴張成其他未詢問的法律或倫理聲明。

唯一非來源文字是 author_contributions.proposed_text。其 pending_explicit_confirmation 狀態及頂層 WAITING 狀態已將它正確隔離。任何下游 writer 或 patch builder 都必須忽略該候選文字，直到新的 explicit author event 對其逐字確認或提供替代內容。

## 安全 LaTeX 建議

以下只是一個不宣稱通訊作者身份的安全排版建議；不得把它視為已套用 patch：

    \author{Liang Wang\textsuperscript{1}\\
    \small \textsuperscript{1}School of Artificial Intelligence and Automation,\\
    \small Huazhong University of Science and Technology,\\
    \small Luoyu Road 1037, 430070, Hubei, P.R. China\\
    \small Contact email: \texttt{wangliang.f@gmail.com}}

安全邊界：

- 在作者明確回答前，不加星號、\thanks{Corresponding author: ...}、Correspondence to 或任何同義標記。
- 不增加 ORCID、學位、職稱、department 縮寫或替代郵遞地址。
- 地址內容按原始事件保留；排版換行不表示內容更正。

已確認的 declarations 可安全寫為：

    \paragraph{Funding.}
    The author received no specific funding for this work.

    \paragraph{Competing interests.}
    The author declares no competing interests.

Author contributions 目前沒有安全的最終替換文字。B0096 應維持 hold，不得把候選句直接排入稿件。工作稿若必須顯示狀態，只能使用明確非最終提示，例如：

    \paragraph{Author contributions.}
    AUTHOR TO CONFIRM: CRediT roles and final contribution wording remain
    pending explicit author approval.

此提示不是 submission-ready replacement；REV-003 只有在取得下列最小人類回答後才可完成。

## 尚需作者回答的最小欄位

1. **Contributions（必需）**：逐字批准 JSON 的 proposed_text，或提供 Liang Wang 的最終 contribution/CRediT roles 及最終英文措辭。
2. **Corresponding-author designation（目前未明確）**：回答 Liang Wang 是否應明確標為 corresponding author。若不指定，contact email 可照原樣保留，但不得加通訊作者標記。

在第 1 項收到明確人類確認前，REV-003 不得標記完成或生成涵蓋 B0096 的最終 patch。第 2 項不應由 sole authorship 或 email 自動補全。
