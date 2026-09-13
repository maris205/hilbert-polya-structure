# P29 B0006 局部預檢修訂提案

狀態：`PROPOSED / UNAPPLIED`。本次僅準備補丁，不代表精確補丁已獲批准、已應用，或已完成 Stage 4.5 Round 3。

使用 ARS `draft_writer_agent` 的 `revision` 角色與材料隔離規則，完整閱讀當前 `notes/stage4_prime_revision_round4.tex` 後，依 `notes/stage4_5_round3_preflight_b0006_writer_handoff.json`、`notes/stage4_5_round3_preflight_b0006_issue_list.json` 及根目錄 `BATCH_ROUND10_STAGE4_5_ROUND3_PREFLIGHT_STOP.md` 準備。本次只使用上述提供材料，沒有新增來源或以模型記憶補足證據。

| Correction ID | 來源 | 精確目標／操作 | 提議變更 | 狀態 |
| --- | --- | --- | --- | --- |
| `IL-MEDIUM-1` | 局部預檢 `P29-B0006-BILINGUAL-SCOPE` | `B0006/replace_block` | 僅將以「文獻足以界定」起首、以「完整商集。」結尾的原句，替換為 handoff 指定的精確文字；改為逐列來源用途限制、尚未完成的項目義務，以及明確不作文獻缺席判斷。 | `PROPOSED / UNAPPLIED` |

補丁頭逐字段沿用 handoff：`patch_format_version=1.1`、`authorization_context=integrity_correction`、`revision_round=5`、`base_draft_hash=8d6294051fe0`、`emitted_by=draft_writer_agent`；`issue_list_sha256=1e8c62b5059de5c1f33c5c6045239b1209906c6149a0f1f4da0a22036a1388cd`。唯一操作沿用 `old_hash=a6eadf4da416` 及 `roadmap_item_ids=[IL-MEDIUM-1]`。這是擬接續既有 round4 的修訂協議輪次 5，不是第五次完整性審計。

`new_text` 僅使用 handoff 的 `required_new_text`，不另作潤色。替換後不再以文獻整體為主語判斷其充分性或相關結果缺席；所有者法則與完整商集仍是本項目未完成的義務。B0006 其餘文字、13+9 引文用途分區、初始動力系統、時鐘、owner、字面單一素理想值域、Gate M/Q 與 Route 邊界均保留。引用維持原 `plainnat` 數字制；不新增、刪除或修改引文。

`claim_strength_changes` 與 `collateral_authorization_ids` 均為空。未建立或改寫 ClaimIntent、作者輸入、授權 sidecar、正文、修訂 bundle、預覽或任何審計輸出；未執行官方 validator、apply、build、科學實驗或 Stage 4.5。全文未被重新輸出，未聲稱局部提案解決了其他問題。

精確補丁 SHA-256、機械核對及後續獨立閱讀由主線處理。ARS 補丁協議使本次交付保持為獨立提案 sidecar；只有作者另行明確批准精確補丁並完成正式授權流程後，才可考慮應用。寫作者不作唯一獨立審查者，也不據此宣告完整性 PASS 或 Stage 5 開放。
