# CS12 冻结与执行证据

Scope ID: `ASFS-DISCOVERY-20260919-CS12`。

Status: `COMPLETE; NO DELAY-KERNEL FIT GAIN; FINE-320 READOUT INVALID`。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: bounded constructive implementation, single execution and saved-output analysis
- Origin Date: 2026-09-19
- Verification Status: UNVERIFIED
- Separate Saved-output Analysis Status: ANALYZED; not an independent rerun
- Version Label: exp_result_v1

[候选卡](../candidate-card.md)、[执行卡](../execution-card.md)与
[14项输入锁](../input-locks.json)先于正式形式审查及科学计算。
锁定两卡、Hénon源定义/旧宏观代码、冷却来源、旧B比较、261停止记录和
既有目标；[新runner](../run_search.py)自包含实现，不导入旧热生成元或读出。
仅本包run-1写入科学输出；原284文件全部保留，后续审查不改其内容。

[形式审查](form-review.md)已完成，无数学阻断；主控全文读回239行。
最终SHA为`1675b710779ee376d6797d16cc2a204ed36a1d6b90829b25a6673571c337ecb4`。
它区别连续单步的非紧模谱与两步紧算子谱，确认有限控制及预算算术，
不曾预先保证数值控制通过或600秒内完成。独立[代码预审](code-review.md)
随后完成；主控全文读回888行源码及两份报告后才锁定
[实现版本](implementation-freeze.json)并启动。

## 唯一运行

[父进程实际收据](execution-receipt.json)记录命令、PID90468、退出0、
约55秒及源/输入不变。实际51对调用/45唯一成员/6缓存；6控制、90训练、
6族后检、4消融，共106前向/full SVD。零额外SVD、eigh、求根或新目标。
六项小控制通过；科学运行没有异常、修补或重跑。最高RSS396360KiB；
含库存表共284文件/300906247字节，没有触及600秒或1GiB输出限。

- [manifest](run-1/manifest.json)、[事件与30秒资源记录](run-1/events.jsonl)
- [完整机器结果](run-1/result.json)、[283项逐文件哈希库存](run-1/file-inventory.json)
- [冻结赢家身份](run-1/winners-frozen.json)、[8训练文件冻结](run-1/training-arrays-frozen.json)
- [45成员结果](run-1/unique-members.json)、[51调用记录](run-1/calls.json)
- [四窗指标/无效null](run-1/development-fit-metrics.json)、[网格与消融比较](run-1/comparisons.json)
- [逐点数据及有效标记](run-1/points.csv)、[必要发现门](run-1/finite-discovery-assessments.json)
- [冷却/自治门](run-1/cooling-versus-autonomous.json)、[外部旧B标尺](run-1/external-history-comparator.json)

库存列283项，不把库存自身纳入其哈希；总284文件不是计数矛盾。
A/D n39/n47及两个END共6正式对象失分辨，指标为null；原数组仍在。
唯一预定读出门失败原因是sigma_320/sigma_0<1e−10，不把原始CSV
中的未认证预测改当正式指标。

## 独立保存证据分析

[保存审查](saved-output-review.md)及其[只读脚本](../check_saved_outputs.py)
核对110个NPZ：90训练紧凑数组、4赢家训练完整复制、6族后检、4消融、
6控制；共20个完整C/左右态。重算能量/指标、排序与冻结次序、控制、
残差/FFT及库存，不重新复合四步C、求SVD或优化。
覆盖4480 CSV行、8有效正式对象的32拟合窗、6无效对象的24窗null；
4有效比较的16窗与10无效比较的40窗null均保留。

首次只读审计exit1：审计器误要求不同内存布局求和后的块诊断逐bit相等。
核块元素完全相同，归约差最多4.44e−16；修正为恢复原布局逐项精确核对、
读回布局另按原1e−12科学门检验后，第二次exit0、ANALYZED。
这是审计器的诊断复核修正，原科学文件和阈值均未改，不能称科学重跑。
非赢家没有保存左右态，其常数方向/符号门只能核对已存诊断；完整20套
则从保存态核对。前321态不是全矩阵重建，模型内部审查不是外部同行评议。

主控另请形式审查者只读复核正文失分辨、END近同和FFT占据解释；未见
越界，未动已冻结形式报告。Portfolio为stop本卡拟合/细格/冷却优势推广、
保留控制并fork；不以完工或审查通过冒充算术/Route进展。

[论文](../paper.md) · [声明账本](../claim-ledger.md)。
