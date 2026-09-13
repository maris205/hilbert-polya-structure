# Symplectic-map Git同步范围（2026-09-13）

本件只记录Git副本，不修改生产研究目录或既有科学／产物验收。

- 生产目录：`/root/autodl-tmp/symplectic_map`。
- Git副本：`/root/autodl-tmp/hilbert-polya-structure-sync/symplectic_map`。
- 远端：`git@github.com:maris205/hilbert-polya-structure.git`，分支`main`。
- 原副本在`af1e97cc7`（2026-08-15，Batch02关闭）；同步前已读取远端并快进到`38f4fc652`。其间322个提交没有修改本子目录。
- 本次补齐Papers12–31及Batch03–07的源、论文PDF、图件、证明／审查／锁／失败记录、验收和必要小型制作证据；Papers1–11及旧资料按同源文件保留。
- 仅在本仓库的`symplectic_map/`下纳入变更；不把其他研究流混入本次提交，不删除只在Git副本存在的历史文件。

## 排除的本地内容

不复制或提交根及嵌套`.git`元数据、`auth.json`、根`id.txt`、`.env`类文件、私钥文件、Python／测试／notebook缓存、虚拟环境及明确的根目录临时文件。
P28以下两份大型依赖归档保留在生产目录，不纳入Git：

- `notes/dependency-capture-20260905/capsule.tar`（2237605376 bytes）。
- `notes/dependency-capture2-20260905/capsule.tar`（320194560 bytes）。

P28三个`build-capsule*`下各`r*`的`usr/、etc/、root/、var/、dev/、lib、lib64`是运行环境副本，同样排除。
它们的源、控制程序、小型输入／输出清单、失败与审查记录以及工作产物保留；这不是承诺仅靠Git克隆即可完整恢复原hermetic运行环境。
`build/`中的实际接受PDF和验收绑定证据明确选入，不能因通用Git ignore而漏掉。本次未重编译，也未改冻结源或PDF字节。

## 已知交付边界

Batch07最终入口仍为[统一总处置](research-batch07/BATCH07_FINAL_CROSS_PAPER_DISPOSITION_V1_20260913.md)。P27须连同[书目勘误](../papers/27-positive-newton-translation-reciprocity/notes/BIBLIOGRAPHIC_ERRATA_V1_20260913.md)阅读；冻结PDF中原字母不变。
历史报告中的绝对生产路径、缺读文献、FAIL及依赖哈希不重写；文件纳入Git不新增科学PASS、远端验收或跨机器复现保证。
本次执行本地提交；push须由用户明确授权。后续push若获批准，应另报告实际远端结果，而非修改本件的执行历史。
