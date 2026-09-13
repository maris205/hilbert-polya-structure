# P1 Wiki 生成元数据

[P1 Wiki 首页](../README.md) · [构建脚本](../tools/build_paper_corpus.py)

`paper-manifest.json` 和 `conversion-manifest.md` 由 `tools/build_paper_corpus.py` 生成。它们记录：

- 每个逻辑论文/项目包的稳定 ID 与所属方向；
- 选择的规范 TeX、PDF、书目和辅助 Markdown 的仓库相对路径；
- 规范 TeX 的 SHA-256；
- 生成的来源卡和全文阅读副本的相对位置与状态。

这些元数据是导航和转换 provenance，不是科学 source lock 的替代物。运行以下命令可只读验证源哈希与生成页面存在性：

```bash
python3 p1_wiki/tools/build_paper_corpus.py --check
```

若源内容或所选 TeX 改变，重新运行普通构建命令会更新派生页面和 manifest；原始研究材料不由该脚本写入。
