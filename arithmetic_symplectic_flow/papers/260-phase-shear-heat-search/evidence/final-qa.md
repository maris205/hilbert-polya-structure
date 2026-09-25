# CS10 — 最终机械核对回执

Scope ID: `ASFS-DISCOVERY-20260919-CS10`。  
Status: `COMPLETE; LOW-WINDOW ORDER EFFECT; NO ROBUST FIT GAIN`。

本回执仅记录文档/身份/字节锁检查；不是新科学运行或数学认证。
科学run-1、两冻结卡和runner均保持原字节。保存数组独立审查已完成；
主控已完整读回形式、代码和保存证据三份报告，并完成主稿结论核对。
最终机械快照记录如下。

实际检查时间：2026-09-19 02:13:01.835496 UTC。

- 本包全部Markdown及根readme/papers registry，共14个Markdown文件、601个
  本地链接均存在，缺失0。外部方法链接未被当作本地路径。
- 24项输入SHA全部匹配；两冻结卡身份与原字节保留。
- README、paper、claim-ledger、result-card、evidence/README共5个当前记录
  均含同一Scope ID及本页Status，无执行或保存审查pending占位。
- 原候选卡/执行卡继续保留计算前FROZEN状态，结果在result-card另行附记，
  没有以最终状态回写旧合同。
- 两Python文件AST解析通过；对新文件逐个执行git diff --no-index --check
  无空白错误。限定任务路径的git diff --check也通过；不清理其他既有改动。
- execution receipt及input locks JSON可解析，runner实际SHA与原manifest一致。
- 没有启动任何新的传播、分解、求根、优化或目标生成；没有commit/push、
  外部发布、PDF或241/242恢复。

| 最终文件 | SHA-256 |
| --- | --- |
| paper.md | 14b27a849f22c7e2e3c55cb4a8f25edcec9a8a6217050c7ccf1418d662aaebc6 |
| run_search.py | 7e71e4df43739edc854ada54c196ac1cc6d0123dfbe2efdec39000cc0ff0e395 |
| check_saved_outputs.py | 91048ea42e764f5ea60e9c4e3a5d4cd6d9cc77d9567fe5a582b1d04209ffd7da |
| candidate-card.md | 77246a97a7c69e40454cb3e35cf107aaa85908c8c9675adf0294c6eb9b5166c5 |
| execution-card.md | ee4f3ee75de4f26b9c12bf1e36d269f967ca01b2a0e7b3be3873f5ebd143d41a |
| saved-output-review.md | 7bfdf8467a210f79d06675c6a61eb9897535ed1fa97ea1f502c1fecbe3fc758c |

本回执只追加以上无新链接的检查记录；不将自身纳入自引用哈希。
数学/数值结论仍以冻结合同、实际run-1与保存审查为依据。
Portfolio：保留有限低窗口顺序控制，stop稳健拟合/非自治收益推广，fork。
Same-object账本完整；A0/A1/A2/T0–T3 NOT EVALUATED，formal UNASSIGNED，
B NOT INVOKED；241/242暂停。
