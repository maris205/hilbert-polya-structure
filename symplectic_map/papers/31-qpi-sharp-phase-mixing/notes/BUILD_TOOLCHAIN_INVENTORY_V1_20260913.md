# Paper31 build toolchain inventory V1

日期：2026-09-13（UTC）。状态：`STATIC_TOOLCHAIN_PRECHECK_COMPLETE / NOT_COMPILED`。
执行者：独立有界代理 `/root/p31_toolchain_inventory_v1`。
范围：只读检查当前本地工具、固定可用 locale、现存 pdfLaTeX 格式及完整 V2 源声明的顶层排版依赖；仅新增本文件。
没有运行 TeX/BibTeX 编译、安装、联网、创建 build 根、扫描旧 build 树，亦未改变任何源或锁。

## 1. 实际输入与读取范围

工作区：`/root/autodl-tmp/symplectic_map`。
以下三件文件均 FULL 读取到 EOF，并实测身份：

| 对象（项目相对路径） | 行数 / 字节 | SHA-256 |
|---|---:|---|
| `notes/PUBLICATION_LOCK_V1_20260913.md` | 72 / 6208 | `65cd1504f15890bbba0d9b9221062303f2daf17640d161f62e8841514f4e4a5c` |
| `paper/v2/main.tex` | 41 / 1277 | `fcbfe0ac6f8ad6364728e7c86981bd1eef2d912c7d125c6d710a155d50cd53fa` |
| `paper/v2/math_commands.tex` | 17 / 577 | `d69b67aa41f2692a1df7c49de52a5299d4f6dcdec8e094d27eb603dc6fa3fc15` |

`rg --files paper/v2` 实际列出 12 件源：main、math_commands、references 和 00–08 九节。
在这 12 件文件中查找 `documentclass`、`usepackage`、`RequirePackage`、`bibliographystyle` 声明；所有匹配均在 main，未发现额外声明。
这只是依赖声明检索，不将其余十件源标为 FULL 数学内容阅读；源集合冻结及完整内容验收由主控的相应记录承担。

## 2. 可执行工具的实际身份

`readlink -f /usr/bin/pdflatex` 实际返回 `/usr/bin/pdftex`。
仅运行版本查询；`--version` / `-v` 不构成稿件编译。

| 工具 / 实际文件 | 实测版本 | SHA-256 |
|---|---|---|
| pdfLaTeX 引擎 `/usr/bin/pdftex` | pdfTeX 3.141592653-2.6-1.40.22；TeX Live 2022/dev/Debian | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `/usr/bin/bibtex` | BibTeX 0.99d；TeX Live 2022/dev/Debian | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `/usr/bin/pdfinfo` | Poppler 22.02.0 | `8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e` |
| `/usr/bin/pdftotext` | Poppler 22.02.0 | `7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d` |
| `/usr/bin/pdffonts` | Poppler 22.02.0 | `257a74fde0c3c36040504ff9068ee4b896c1cc2f19a9fae5a5b3dda55637ba5e` |
| `/usr/bin/pdftoppm` | Poppler 22.02.0 | `f09bac4b4bc5e08ef9d44620fb5a4f1dd61574a8ed9fe49f48575d45e6966165` |

引擎和 BibTeX 均报告 kpathsea `6.3.4/dev`。
引擎报告编译及使用的 libpng 均为 1.6.37、zlib 均为 1.2.11，使用 xpdf 4.03。
这些是版本查询的实际输出，不宣称已穷尽动态库或排版传递依赖。

## 3. 固定环境与现存格式

`locale -a` 实际返回 `C`、`C.utf8`、`POSIX`。
`LC_ALL=C locale` 成功，所有 LC 分类均为 `C`；因此可使用 `LC_ALL=C`。
这次查询显示继承的 LANG 为 `C.UTF-8`，但 LC_ALL 优先；生产协议应明确固定 LC_ALL，不依赖继承状态。
按已读 publication lock，生产所需固定值为：

```text
SOURCE_DATE_EPOCH=0
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
```

本记录没有替主控运行生产流程或设置持久环境。
实际使用正确的引擎限定格式查询：

```text
kpsewhich -engine=pdftex -format=fmt pdflatex.fmt
/var/lib/texmf/web2c/pdftex/pdflatex.fmt
```

该格式实测为 1503567 字节，SHA-256 为
`5e3d04e4b504653152b7fbbe415f78de3d353795a3c3d9ceb68e39bb3c0cf8f0`。
格式已经存在，无需生成新格式。
不带 `-engine=pdftex` 的格式查找可能为空，不能据此判为缺依赖；本次判据是上面的实际成功路径及文件身份。

## 4. 顶层排版依赖

逐个使用 `kpsewhich <文件名>` 定位，再对实际返回文件执行 `sha256sum`。
下面只涵盖当前源直接声明的 14 件 cls/sty/bst；没有递归扫 texmf。
版本来自实际文件的 ProvidesClass / ProvidesPackage 字段；plainnat 取实际文件头的版本记录。

| 文件与版本 | 实际绝对路径 | SHA-256 |
|---|---|---|
| article.cls；2021/10/04 v1.4n | `/usr/share/texlive/texmf-dist/tex/latex/base/article.cls` | `988fb3e599df7e5b545e4253829dab11f0c7bd7827b79d32c2aaadfb52db6f6c` |
| lmodern.sty；2009/10/30 v1.6 | `/usr/share/texmf/tex/latex/lm/lmodern.sty` | `e1cdd137ae86b4e860f0b0bcfc4c1a90cae3ff1f9c651cb21bd86c15bb83b916` |
| fontenc.sty；2021/04/29 v2.0v | `/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty` | `d088c75e16c3c9f6b979a59571b96e5dd9e487a720bc74591580878388b82918` |
| inputenc.sty；2021/02/14 v1.3d | `/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty` | `16dffe967174f21dbd52ef849bcb74741109f3ce5bc68b881f1ce4aef3133b2a` |
| geometry.sty；2020/01/02 v5.9 | `/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty` | `d5d36ad74051ad36288242b51438e2d9a5db2bd6c063b9b5704d0931fbc9f439` |
| amsmath.sty；2021/10/15 v2.17l | `/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty` | `027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83` |
| amssymb.sty；2013/01/14 v3.01 | `/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty` | `70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986` |
| amsthm.sty；2020/05/29 v2.20.6 | `/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty` | `8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626` |
| mathtools.sty；2021/02/02 v1.28 | `/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty` | `e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7` |
| booktabs.sty；2020/01/12 v1.61803398 | `/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty` | `3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc` |
| array.sty；2021/10/04 v2.5f | `/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty` | `1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157` |
| natbib.sty；2010/09/13 8.31b | `/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty` | `d2709be806dc7d5f54daa9a16022ba1451b1322954751b98e38cfad0cc107450` |
| hyperref.sty；2021-06-07 v7.00m | `/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty` | `77e7c2421a06900f158416e090665069dd724a6e0c605cd2a1838c7d3b7944d2` |
| plainnat.bst；family 0.99b，natbst.mbs 2007/11/26 1.93 | `/usr/share/texlive/texmf-dist/bibtex/bst/natbib/plainnat.bst` | `21eefa76f1c967f5074776fcef096c0f8f2b9e42347e84b62e1dbb121dcae486` |

14 件顶层文件均存在且可读，未出现 `MISSING`。
main 实际固定 article 11pt/letter、geometry 1 inch，并含省略 PDF 日期及抑制 trailer ID 的引擎守卫；本记录未改变这些设置。

## 5. 结论与未完成事项

在此有界范围内，静态工具链预检完整，未发现缺少的顶层依赖或格式。
动态传递依赖、字体文件、配置文件及实际运行输入仍待首次真实构建的 `.fls` / 日志记录；本表不冒充其完整清单。
主控另外负责冻结完整源 manifest、精确命令及简单构建脚本，并验证两个计划新根实际 absent 后才创建。
锁定顺序保持 pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX；本记录没有执行其中任何一步。
第二空根须在第一完整构建成功且正文 22–30 页实际通过后，依相同冻结源、环境、协议构建并比较字节。
本记录不是编译成功，不是正文页窗 PASS，不是 PDF/字体/视觉验收，不是科学审查或最终接受。
没有生成 PDF，也没有预言两根 PDF 字节一致。
