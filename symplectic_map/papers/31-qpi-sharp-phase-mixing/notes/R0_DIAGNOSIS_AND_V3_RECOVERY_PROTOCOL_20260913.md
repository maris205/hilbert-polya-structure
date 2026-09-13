# Paper31：r0 实际制作诊断与 V3 新根协议

日期：2026-09-13 UTC。主控：`/root`。本件在 r2 第一次执行前冻结。
状态：`R0_BUILD_POSTPROCESS_FAILED / R0_BODY_WINDOW_PASS / V3_MINIMAL_REPAIR_FROZEN`。
保留原完整 V1/V2、源审查、制作锁、首次协议、脚本 V1、r0 全部现场；不回写失败为成功。

## 1. 第一次完整构建的实际结果

按 [前置协议 V1](NATURAL_BUILD_PROTOCOL_V1_20260913.md) 执行脚本 V1 的 r0。
三次 pdfLaTeX 和一次 BibTeX 均返回0，生成31页、528145 bytes 的真实 PDF，
SHA `fda521e298843de060c3582df46ce9541ea61d31ef7067203377f87ca1808c4f`。
脚本后处理在 `awk ... main.fls` 处退出2，尚未执行其后 pdfinfo/pdffonts/pdftotext 命令。
主控随后独立只读运行这些工具：LastBodyPage=30，结论在第30页，参考文献独占第31页；
亲看第30/31页图并核29–31页文本，确认正文30＋文献1，原22–30硬窗通过。
PDF为letter、匿名元数据、26项字体全部嵌入；这不是完整全页接受。

最终 TeX 日志无缺引用、缺字、缺字体或不收敛；有 §5:247–251 的0.75978pt overfull hbox，
及 §6:276 的两条同一数学书签 math-shift 警告。主控亲看第19页，前者不裁字但作局部文字修正；
后者显式指定纯文本书签。没有数学失败或页数失败。

## 2. 依赖记录的定位与保留

root 在精确格式目录找到以下三件，逐件 PWD 都指向 r0/work，实际输入含原格式和 main.tex，
输出含 main.log/aux/out/pdf；已复制到 r0/diagnostics，格式目录原件不删。

| 原件（/var/lib/texmf/web2c/pdftex 下） | bytes | SHA-256 |
|---|---:|---|
| pdflatex.fmt39469.fls | 52263 | `809be83ba75dbd49c05e7cc15f9b214e79b9809b780a9f5a0e5201451d4ac364` |
| pdflatex.fmt39483.fls | 52833 | `f103a65cf53805d2d7d7da6917fb7316d7103864b584b5d7a221fdf6cfd78756` |
| pdflatex.fmt39497.fls | 52833 | `f103a65cf53805d2d7d7da6917fb7316d7103864b584b5d7a221fdf6cfd78756` |

有界只读诊断代理 `/root/p31_toolchain_inventory_v1` 另核格式目录device142/overlay、work device2064/xfs；
实际 pdftex 反汇编显示先以前缀+PID+.fls 打开，再调用 rename 而不检查返回值。
据实际绝对 -fmt 前缀、跨设备事实及该逻辑，最相符的原因是 EXDEV 后临时名保留；
没有运行追踪观察 errno，故 EXDEV 明确为推定。实际三份完整记录已排除“recorder 被源设置禁用”。
不更改 pdfsuppressptexinfo，不生成新格式、不安装、不改变全局配置。

## 3. 完整源 V3 的两行制作修正

复制完整 V2 为 V3，仅改两行：§5 将 “They commute and have bounded...” 改为 “They commute, with bounded...”
以处置已观察的行溢出；§6 以 texorpdfstring 为原 T=3/16 小节提供 ASCII 书签。
全部公式、定理、证明量词、引用、主文件和版式不变；主控已读完整差分及原上下文，其余10件字节相同。
完整 V3 为12件2454行／108359 bytes，源清单 [SOURCE_V3_20260913.sha256](SOURCE_V3_20260913.sha256)
12行／1164 bytes，SHA `4e1a98c1e273b8d2e138b91952a1c1e1ce2e00ac6006521714ddaf0dbd8beae8`；实际 sha256sum -c 全通过。
既有 FULL V1＋M1 V2 actual 源审查保持；制作差分及其 PDF 影响交后续同一 fresh 内容审查核验，不重开数学票。

## 4. 新根与精确 successor 命令

新脚本 [build_natural_v2.sh](../scripts/build_natural_v2.sh) 64行／2656 bytes，
SHA `016eb9530c36ec27b3c6bc17b1988b4ddbab1bd426009e282a785efd861b297f`；bash -n 通过。
相对脚本 V1，只换完整源/清单为V3、允许 absent 根为r2/r3，增加固定
`TEXFORMATS=/var/lib/texmf/web2c/pdftex`，并把 -fmt 设为 `-fmt=pdflatex`。
只读 kpsewhich 已确认仍解析同一原格式，SHA `5e3d04e4b504653152b7fbbe415f78de3d353795a3c3d9ceb68e39bb3c0cf8f0`。
其它固定环境、全部工具/依赖、四遍次序、输出留存和验收约束沿首次协议；不升级为通用恢复框架。

从项目根执行 `bash scripts/build_natural_v2.sh r2`，工作目录为 `build/natural-20260913-r2/work`；
完整成功且正文窗真实通过后，才执行 `bash scripts/build_natural_v2.sh r3`，目录对应r3/work。
执行前两个根均须不存在，脚本拒绝覆盖。r1未执行，不能把其不存在写成通过。
两根要求完整源一致、原格式一致、实际依赖一致以及最终PDF字节同一，再作全页实际审查和另席终局完整性。
V3实际页数、日志清洁和确定性尚待新根运行；r0的页窗PASS不预授V3。
所有操作仅本地；不清旧根、不试排择版本、不改页数合同、不移证、不作数值或外部发布。
