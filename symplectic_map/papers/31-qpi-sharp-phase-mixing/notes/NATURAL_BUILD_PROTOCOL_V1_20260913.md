# Paper31：首次完整自然构建前置协议 V1

日期：2026-09-13 UTC。本件在第一次编译前冻结；此刻无 P31 PDF 或 build 根。
采用 [制作锁](PUBLICATION_LOCK_V1_20260913.md) 的简单同源双根协议，不能代替各项实际验收。

## 1. 冻结输入

- 完整源：`paper/v2/`，12件2454行／108337 bytes，身份由 [SOURCE_V2_20260913.sha256](SOURCE_V2_20260913.sha256) 唯一固定；清单 SHA `9f61d249df26d8997690be71d2d24f5d0f3727e07c4159bc4a78aa66a91cd89f`。
- 源前置门：[完整源处置](COMPLETE_SOURCE_DISPOSITION_V2_20260913.md)，结合首次 FULL actual V1 与真实 M1 successor 续查 PASS；源不得在构建期间编辑。
- 两锁：source V1 SHA `b056a664863e41cf778225118ea719a3e43b4a78c451d302703f423c931dd584`；publication V1 SHA `65cd1504f15890bbba0d9b9221062303f2daf17640d161f62e8841514f4e4a5c`。
- 引用：原六项 CITATION_RECORDS V1 SHA `85be5a08f81484538fce6190d79901726a288a09060fb83dc528766732dd7947` 加 lift supplement SHA `680f1016a6caa1b220591e41507b31c4637415202057f700b0adb5d8a024c6cb`；共7项实际 bib。
- 工具／14件顶层依赖：[BUILD_TOOLCHAIN_INVENTORY_V1_20260913.md](BUILD_TOOLCHAIN_INVENTORY_V1_20260913.md)，102行／7484 bytes，SHA `d705e5cf18670c497291f1fc94e8b4b8c2c99c8968b9adc359e2db7c9cbf4e9b`；主控 FULL 读回。实际传递输入在首次 `.fls` 留存后记录。
- 执行脚本：[build_natural_v1.sh](../scripts/build_natural_v1.sh)，62行／2597 bytes，SHA `e2fc648804d39c61a0dd5d6f43f8692d1685a1da5bce8894faed89faefb7e116`。主控 FULL 读回；`bash -n` 通过，尚未生产执行。

## 2. 精确执行与保留

项目绝对根为 `/root/autodl-tmp/symplectic_map/papers/31-qpi-sharp-phase-mixing`。
第一根 `build/natural-20260913-r0/work`；第二根 `build/natural-20260913-r1/work`。
脚本执行前拒绝已经存在的目标根，先校核完整源清单，再复制12源到新 work；不带入旧辅助文件。

固定环境：`SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C TEXINPUTS=.: BIBINPUTS=.: BSTINPUTS=.:`。
固定引擎 `/usr/bin/pdflatex`，实际 `/usr/bin/pdftex`；固定现存格式
`/var/lib/texmf/web2c/pdftex/pdflatex.fmt`，SHA `5e3d04e4b504653152b7fbbe415f78de3d353795a3c3d9ceb68e39bb3c0cf8f0`。
选项为 `-fmt=/var/lib/texmf/web2c/pdftex/pdflatex.fmt -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex`。
次序为该 pdfLaTeX 命令、`/usr/bin/bibtex main`、同一 pdfLaTeX 命令、同一 pdfLaTeX 命令。
从项目根执行：`bash scripts/build_natural_v1.sh r0`；第二根满足下一节前提后才执行 `bash scripts/build_natural_v1.sh r1`。

每一遍保留精确命令、stdout/stderr、退出码以及当时存在的 main.log/aux/out/fls/blg/bbl/pdf 快照。
失败即停止，保留 work 和 logs，不清理、不覆盖、不自动循环。后续额外收敛遍次仅限真实未收敛且先记录原因。
四遍成功后再次核源清单，保留 recorder 的全部绝对输入路径及实际 SHA、pdfinfo/pdffonts、完整 layout text 和最终 PDF SHA。
这些只表明工具实际完成；完整依赖分析、警告处置和 PDF 验收另记，不由脚本末句授 PASS。

## 3. 自然页窗、第二根与验收

第一根成功后，以 `LastBodyPage` 实际 aux 页号、逐页文本以及真实正文末页／参考文献首页图相互核验。
硬窗为22–30正文页；参考文献另页，不将完整必要证明移到附录，不用缩字、改边距或装饰填页。
第一完整构建成功且该窗实际通过，才允许第二 absent 根按同一完整源、格式和脚本执行。
两根 PDF 要 `cmp` 字节相同且 SHA 相同，并核记录的实际依赖身份；只看起来相同不够。
全部实际日志须无未处置错误、缺字体/字形、缺引用或不收敛，溢出逐项定位并做实际页面核验。
主控全页阅读后，fresh 非作者完成 actual 稿件/全部页PDF审查，再由另席独立终局完整性审查。
真实制作错误可按锁作最小 successor；本协议不授权反复试排择页数、改变科学合同或迁移 P30 的40页例外。
尚无任何页数实测，第二根和后续验收不预授。仅本地效力；不安装、不联网补隐藏依赖、不提交或发布。
