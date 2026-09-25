# 253 — 五个结构变形的构造搜索：保留原模型子族

**Scope ID:** `ASFS-DISCOVERY-20260919-CS03`。  
**Current status:** `STRUCTURAL SEARCH COMPLETE; BASELINE SUBFAMILY RETAINED`。

实际比较四次势、六次势、周期桥、四次动能和同端点冷却变形；固定
上一轮alpha读出，完成276个训练前向及两个新网格前向。最低百点MAPE
为2.271793%，但胜者lambda=0，属于原模型子族的微调，并非六次项成功。
开发101–150和冻结后151–200均略差，网格局限仍在；全部较差结果保留。

[全文](paper.md) · [不可变搜索前卡](candidate-card.md) · [执行卡](execution-card.md) ·
[输入锁](input-locks.json) · [声明账本](claim-ledger.md) · [证据](evidence/README.md)。

Portfolio: **fork后续构造，保留原模型子族的有限对照**；五族当前胜者均回到
lambda=0，本轮未找到新增结构项的训练MAPE优势，不继续无期限细调同一邻域。
Q/S非零成员较低的最大单点误差作为指标取舍保留，不据此回写预定目标。
这不是全参数域否定，不是可信A−1通过；formal UNASSIGNED，B NOT INVOKED。
