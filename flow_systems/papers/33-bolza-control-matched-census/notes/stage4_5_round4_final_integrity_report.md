# P33 · Stage 4.5 Round 4 最終完整性查核（待主線格式驗證）

結論：FAIL。四項原有作者待確認事項仍未解決，另新識別一項 B0128 的 fixture 終態文字不一致；未修改正文、參考文獻或任何暫停前檔案，也未進入 Stage 5/6。

本次為同一輪查核的受限恢復，不是重新啟動全輪。P31 越界 API 證據與其衍生判斷未作為 P33 的證據。已成功的 P33 bundle、coverage 與 evidence-row 檢查均未重跑；暫停前實際完成的執行證據另存於 recovery1_official_execution_receipt。

## 核心結果

| 查核面向 | 本輪範圍與結果 |
|---|---|
| A 文獻身分 | 22/22 筆現行書目均作新網頁查詢；20 基礎來源加 2 更正紀錄。S02 完整主要來源 metadata 存取限制保留。 |
| B 引用語境 | 全部 48 個引用使用、14 個語境及相鄰限定語重新閱讀。現稿均為限定的書目／閱讀候選用途；48 個來源段落關係仍 INCONCLUSIVE。 |
| C 資料 | 全部 43 個清單檔案現行 hash／bytes、48 個引用綁定、14 個 fixture 位元組及原有 oracle／receipt 已核對；0/7 生產義務仍未實作。 |
| D 原創性 | 44/78 段（56.41%），含全部 43 段修訂變更與每個主要章節；88 個實際配對查詢。未識別實質未歸屬重用，但混合搜尋結果不提供逐查詢排名／筆數，不能據此宣告原創性或優先權。 |
| E 主張 | 459 個精確 UTF-8 註冊單位、464 列正式 evidence rows；452 個限定範圍相符、6 個不可驗證單位、1 個輕微失真。6 個不可驗證單位歸於原有 4 項作者事項，不重複增列 issue。 |
| Coverage | 正式建立及重播成功；32 個機械候選、0 個未註冊／部分覆蓋。語義擷取完整性仍為 not_machine_detectable。 |
| E6 | 四輪共 74 個操作逐一閱讀舊／新文字及同期授權；本次語義查核未檢出未授權強度漂移。這不是確定性的「沒有漂移」證明。 |

所有 evidence rows 的 writer anchor 均缺席，正式輸出保留 anchorless、null excerpt；452 個 VERIFIED 僅表示記錄、限定範圍或設計敘述相符，不表示文獻段落、數學定理、生產程式、作者身分或科學結果已被驗證。

## 尚未解決事項

原有 IL-SERIOUS-2 至 IL-SERIOUS-5 分別涉及資助、利益衝突、作者實際貢獻／審閱，以及提供方向／承擔責任的個人行為。一般階段授權、生成的 metadata 與同名公開紀錄均不替代本人具體確認。

新增 P33-R4-FIXTURE-STATE-001：B0128 說十二個 invalid-labelled fixtures 均須是 rejected 或 not_evaluable，但實際 oracle 與既存 receipt 為 8 個 rejected、2 個 not_evaluable、2 個 bounded_incomplete。後兩個是 incomplete_coverage.json 與 unresolved_cutoff.json。原有 14/14 診斷一致數仍正確；問題只在狀態集合的文字描述，沒有科學結果變更。未套用修補。

七種 AI 失敗模式均已評估；第 6 模式因這項方法／資料敘述差異及待確認個人行為而標為 SUSPECTED，維持檢查點關閉。其餘 CLEAR 均限於現稿實際主張範圍，不是未來程式無誤保證。

依鎖定的非 SR 分派，PRISMA-trAIce 為 null，RAISE 為 principles_only；人類監督、透明度與可重現性仍有材料缺口，fit-for-purpose 為 warn。此 ARS 原則延伸的合規貢獻上限為 warn，不消除獨立完整性阻擋，也不是正式 RAISE 證據綜整合規認證。

## 交付與界線

[完整 Schema 5 候選報告](stage4_5_round4_integrity_report.json) 保留全量 evidence rows；[Schema 12 候選報告](stage4_5_round4_compliance_report.json) 交主線執行唯一最終格式驗證。正式子程序執行見 [保全回執](stage4_5_round4_recovery1_official_execution_receipt.json)，補充歷史差異、表格、實驗聲明與範圍處理見 [supplementary comparison](stage4_5_round4_supplementary_comparison.json)。

本輪查核交付不授權再次自動審查、修稿、科學執行、canonical promotion、Route 評分或發布。後續須由主線呈報具體待決事項並取得使用者方向。

