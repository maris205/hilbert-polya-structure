# CS13 声明账本

Scope ID: `ASFS-DISCOVERY-20260919-CS13`。

State: `COMPLETE; NO FACTORIZED-SPECTRUM FIT GAIN; FINE-GRID CHAIN FAILS`。
计算前卡保持FROZEN历史状态，本账本及[结果卡](result-card.md)为当前结果。

| ID | 声明 | 证据类别与边界 | 状态 |
| --- | --- | --- | --- |
| C13-01 | 有限区间Q闭稠定，J=Q*Q自伴正且Dirichlet下核为零 | [正文§3](paper.md)局部推导；不由数值残差证明 | ESTABLISHED LOCAL FORM |
| C13-02 | J_V=J_M+Var(a)q⁴ | 同参数闭二次型展开；不推导重标后拟合次序 | ESTABLISHED LOCAL IDENTITY |
| C13-03 | M/V均不识别路径排列 | 只依赖均值/方差；128点是统计求积后检 | ESTABLISHED LIMITATION |
| C13-04 | Gram单元最高12次；7点Gauss精确算术积分，先集总再Dirichlet给dI | 离散定义/多项式次数推导；不是浮点区间证书 | ESTABLISHED LOCAL FORM |
| C13-05 | 常b离散全谱为冻结解析式 | 正弦向量代入；两常漂移控制误差<4.6e−15；另四小控制均通过 | FINITE CONTROL PASS |
| C13-06 | 因子化形式相对历史标尺改善训练及固定320模拟合 | M/V J>5；主V训练M7.799171%、细格320 M8.468578%劣于历史标尺 | NOT ESTABLISHED; STOP PROMOTION |
| C13-07 | 方差项带来同参数有限效果 | V相对VAROFF full320 M降低.010589828个百分点，但末20点反向；M赢家恰同theta，不构成独立统计重复 | FINITE MIXED EFFECT; NO CHRONOLOGY |
| C13-08 | 源低阶jet具有有限作用 | SOURCEOFF保留正则尾，full320 M变为20.874623%；非素数编码消融 | FINITE SENSITIVITY ONLY |
| C13-09 | 无限连续谱收敛、内生算术/自然量子化、假目标区分 | 本轮有限网格和原已知目标不足 | OPEN / NOT ESTABLISHED |
| C13-10 | A0/A1/A2、T0–T3或正式Route信用 | 非经典候选，roof/primitive/算术迹缺失 | NOT EVALUATED; B NOT INVOKED |
| C13-11 | 整条细网格链通过预定2%门 | 两族2047→3071 full320 G约2.438%失败，最后段约.854%通过；主V时间/箱宽通过不能补齐 | NOT ESTABLISHED; CHAIN FAILS |
| C13-12 | 保存证据与指标一致 | 149谱NPZ/21含态、60拟合窗/56比较窗、全部SHA首次审计exit0；无新求谱 | ANALYZED, NOT RERUN VERIFIED |

决定：保留形式、实现与消融证据；stop本卡拟合优势推广并fork。
不追加参数搜索或把局部否定推广成全族不可能；[计算前卡](candidate-card.md)保持不动。
