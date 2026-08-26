# Paper build / 论文编译

The manuscript is a self-contained equation-first theory note. It uses inline bibliography entries so the 28-file release contract has no hidden bibliography dependency.

论文是自包含、公式优先的理论短文；参考文献直接写入主文件，因此 28 文件发布契约没有隐藏的 bibliography 依赖。

Deterministic final build:

```bash
export SOURCE_DATE_EPOCH=1787673600
export FORCE_SOURCE_DATE=1
export TZ=UTC
lualatex -interaction=nonstopmode -halt-on-error main.tex
lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The release retains `main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf`. The final `main.pdf` equals round 2 byte-for-byte. Build logs and font/layout checks are summarized in `COMPILE_REPORT.md`.

发布保留三轮 PDF；最终 `main.pdf` 与 round 2 逐字节相同。编译、字体和版面检查见 `COMPILE_REPORT.md`。
