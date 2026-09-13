# Round10 · Stage 4.5 Round4：官方校验失败停止记录

状态：**PAUSED_OFFICIAL_VALIDATION_FAILURE_REQUIRES_USER_DIRECTION**。这一次完整复核尚未完成。

2026-09-06 12:18 UTC，P32 的官方 `claim_registry_coverage.py` 以退出码 2 停止。原因是我在新建审计注册表中，将 18 项 `writer_anchors` 写成对象；`claim-registry/1.0` 要求字符串数组。这是审计输出的格式错误，不是稿件或锁定材料损坏。

已保留失败输入、原始命令及完整输出；未修正、未重跑。并行完成的 476 行证据校验只说明该证据行结构和来源字节可回放，不能替代失败的注册表覆盖校验，更不代表完整审查通过。

按本轮授权的明确停止条件，P32 执行及两位相关工作代理已停止；P31 的剩余工作也在此用户检查点暂停。P29、P30、P33 已有候选报告，但整批最终 Schema5/12 与报告级检查尚未运行。P32 的 D、完整 E6 及最终报告仍未完成。

只读保护核对：Recovery1 锁定的 **1,065 个文件零变更**；15 个 `code/experiments/results` 目录均未变。原有 16 项作者待确认事项完整保留，P31/P32 的前置机构等元数据另有新发现，不视为虚假信息，也未开展个人调查。此前 P31 API 材料继续隔离，不控制本轮允许来源的结论。

完整命令、错误文本、输入摘要、保护结果及当前中间文件清单见同名 JSON。P32 的单次失败凭证位于 `papers/32-homology-cover-renormalization-uniformity/notes/stage4_5_round4_official_coverage_attempt1_failure.json`。

建议的恢复范围（**尚未获批、尚未执行**）：保留本次失败记录，以新版本修正 P32 的字符串格式及必要的下游绑定，仅重跑受影响的校验，随后完成同一次 Round4 的剩余工作；不重启全套审查、不改稿、不增加 API 权限、不清除作者事项、不进入 Stage5/6。
