#!/usr/bin/env python3
"""Build the source-bound Markdown reader corpus for ``p1_wiki``.

The builder deliberately works at the *logical package* level, not the PDF
file level.  A package receives a navigation card and, when a canonical LaTeX
manuscript can be located, one Markdown reading rendition.  The original
source files remain authoritative: this tool never changes a source package,
never deletes generated files, and records the exact input hash in the
manifest and each generated page.

Usage from the repository root::

    python3 p1_wiki/tools/build_paper_corpus.py
    python3 p1_wiki/tools/build_paper_corpus.py --check

``--check`` is read-only.  It verifies that the manifest still matches the
current source inputs and that the expected generated pages exist.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


BUILDER_VERSION = "1.8.0"
PANDOC_TO = "markdown+tex_math_dollars"

REPO_ROOT = Path(__file__).resolve().parents[2]
WIKI_ROOT = REPO_ROOT / "p1_wiki"
DIRECTIONS_ROOT = WIKI_ROOT / "directions"
META_ROOT = WIKI_ROOT / "meta"

ROUTE_LABELS = {
    "zeta_mvp0": "Zeta MVP0：自由探索与分阶段 programme",
    "logistic_dynamics": "Session 1：Logistic Dynamics（离散 vs 连续）",
    "henon_dynamics": "Session 2：Hénon Dynamics（低维 vs 高维）",
    "symplectic_map": "Session 3：Symplectic Map（Hamiltonian chaos；耗散 vs 保守）",
    "symbolic_dynamics": "Session 4：Symbolic Dynamics（符号 vs 几何）",
    "flow_systems": "Session 5：Flow Systems（经典 vs 量子）",
}

# These directories commonly contain source fragments, frozen snapshots, or
# auxiliary figures.  They may be used only if no full document is available.
DEPRIORITIZED_PARTS = {
    ".git",
    "archive",
    "backup",
    "build",
    "figures",
    "frozen",
    "history",
    "notes",
    "qa",
    "release",
    "results",
    "review",
    "reviews",
    "source_context",
    "tests",
}

PREFERRED_TEX_NAMES = (
    "stage5_finalization/manuscript.tex",
    "paper/main.tex",
    "paper/manuscript.tex",
    "manuscript/main.tex",
    "manuscript/paper/main.tex",
    "main.tex",
    "paper/paper.tex",
    "manuscript.tex",
    "paper.tex",
)

PREFERRED_PDF_NAMES = ("paper.pdf", "main.pdf", "manuscript.pdf")

# Pandoc emits image paths relative to the source TeX file.  Reader copies
# live elsewhere, so those paths must be redirected back to the immutable
# source asset rather than copied into the Wiki.  The DOI rewrite fixes a
# Pandoc representation in which a bare DOI target would otherwise look like
# a repository-local Markdown link.
IMAGE_LINK = re.compile(r"(!\[(?P<alt>.*?)\]\()(?P<target><[^>]+>|[^)\s]+)(\))", re.DOTALL)
BARE_DOI_LINK = re.compile(
    r"(\[[^\]]+\]\()(?P<doi>10\.\d{4,9}/[^)\s]+)(\))", re.IGNORECASE
)


@dataclass
class PaperRecord:
    """A source-bound logical paper/project identity."""

    id: str
    route: str
    title: str
    source_package: str
    source_role: str
    source_status: str
    canonical_tex: str | None
    canonical_pdf: str | None
    supporting_markdown: str | None
    bibliography: str | None
    source_sha256: str | None
    fulltext_status: str = "pending"
    render_method: str | None = None
    render_error: str | None = None


def repo_relative(path: Path | None) -> str | None:
    if path is None:
        return None
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_text(path: Path, limit: int = 512_000) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            return handle.read(limit)
    except OSError:
        return ""


def markdown_link(from_file: Path, target: Path, label: str) -> str:
    relative = os.path.relpath(target, from_file.parent).replace(os.sep, "/")
    # Angle brackets keep an eventual space in a historical source path valid
    # in both GitHub-flavored Markdown and Obsidian.
    return f"[{label}](<{relative}>)"


def yaml_value(value: str | None) -> str:
    return json.dumps(value if value is not None else "", ensure_ascii=False)


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "unnamed-package"


def first_heading(path: Path | None) -> str | None:
    if path is None or not path.exists():
        return None
    for line in read_text(path).splitlines():
        match = re.match(r"^\s*#\s+(.+?)\s*$", line)
        if match:
            return re.sub(r"\s+", " ", match.group(1)).strip()
    return None


def balanced_braced_argument(source: str, opening_brace: int) -> str | None:
    """Return the TeX group beginning at ``opening_brace``, without braces."""

    if opening_brace >= len(source) or source[opening_brace] != "{":
        return None
    depth = 0
    index = opening_brace
    while index < len(source):
        character = source[index]
        if character == "\\" and index + 1 < len(source):
            # Escaped literal braces do not open or close a TeX group.
            index += 2
            continue
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return source[opening_brace + 1 : index]
        index += 1
    return None


ACCENT_COMBINING_MARKS = {
    "'": "\u0301",
    "`": "\u0300",
    "^": "\u0302",
    '"': "\u0308",
    "~": "\u0303",
    "=": "\u0304",
    ".": "\u0307",
    "c": "\u0327",
    "H": "\u030b",
    "v": "\u030c",
    "u": "\u0306",
    "r": "\u030a",
    "k": "\u0328",
}


def display_title(title: str) -> str:
    """Remove TeX layout residue while retaining the source title's meaning.

    This function is used only for derived navigation metadata.  It does not
    rewrite source TeX/PDF or the Markdown body.  In particular, inline TeX
    math such as ``\\(U_c\\)`` is intentionally kept intact.
    """

    def punctuated_accent(match: re.Match[str]) -> str:
        return unicodedata.normalize("NFC", match.group("letter") + ACCENT_COMBINING_MARKS[match.group("accent")])

    def braced_accent(match: re.Match[str]) -> str:
        return unicodedata.normalize("NFC", match.group("letter") + ACCENT_COMBINING_MARKS[match.group("accent")])

    title = re.sub(
        r"\\(?P<accent>['`^\"~=\.])(?P<letter>[A-Za-z])",
        punctuated_accent,
        title,
    )
    title = re.sub(
        r"\\(?P<accent>[cHuvrk])\{(?P<letter>[A-Za-z])\}",
        braced_accent,
        title,
    )
    # TeX linebreaks may carry an optional visual spacing dimension.  The
    # dimension is not title content, so remove the whole presentation token.
    title = re.sub(
        r"\\\\(?:\s*\[[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:em|ex|pt|cm|mm|in)\])?",
        " ",
        title,
    )
    title = re.sub(r"\\(?=\s)", " ", title)
    title = re.sub(r"\\[,:;!]", "", title)
    title = re.sub(r"\s*\[[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:em|ex|pt|cm|mm|in)\]\s*", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def latex_title(path: Path | None) -> str | None:
    if path is None or not path.exists():
        return None
    source = re.sub(r"(?<!\\)%.*", "", read_text(path))
    match = re.search(r"\\title(?![a-zA-Z@])(?:\s*\[[^\]]*\])?\s*", source)
    if not match:
        return None
    title = balanced_braced_argument(source, match.end())
    if title is None:
        return None
    # Layout-only commands occur at the start of a number of manuscripts.  A
    # generic macro unwrap would preserve ``-1.5em`` and turn it into a fake
    # title, so remove these before unwrapping semantic formatting commands.
    title = re.sub(
        r"\\(?:vspace|hspace)\*?\s*(?:\[[^\]]*\]\s*)?\{(?:[^{}]|\{[^{}]*\})*\}",
        "",
        title,
    )
    title = re.sub(
        r"\\(?:smallskip|medskip|bigskip|noindent|tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge|displaystyle)\b",
        "",
        title,
    )
    title = display_title(title)
    wrapper_commands = (
        "textbf|textit|textrm|textsf|texttt|textnormal|textsc|emph|protect|"
        "ensuremath|mathrm|mathbf|mathit|mathsf|mathtt|mathcal|mathbb|"
        "operatorname|MakeUppercase|MakeLowercase|underline|mbox"
    )
    wrapper_pattern = re.compile(rf"\\(?:{wrapper_commands})\*?\s*\{{([^{{}}]*)\}}")
    previous = None
    while title != previous:
        previous = title
        title = wrapper_pattern.sub(r"\1", title)
    title = title.replace("\\&", "&").replace("\\%", "%")
    title = re.sub(r"\\\((.*?)\\\)", lambda match: f"${match.group(1).strip()}$", title)
    # A few manuscripts use a single-letter private math macro in the title.
    # Keeping the letter is more portable than emitting an undefined macro in
    # a standalone Markdown heading.
    title = re.sub(r"\\([A-Z])\b", r"\1", title)
    title = title.replace("{", "").replace("}", "")
    title = display_title(title)
    return title or None


def choose_supporting_markdown(package: Path) -> Path | None:
    candidates = (
        package / "README.md",
        package / "readme.md",
        package / "PAPER_PLAN.md",
        package / "notes" / "pipeline_state.md",
        package / "notes" / "CLAIMS_EVIDENCE_MATRIX.md",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def tex_score(package: Path, candidate: Path) -> tuple[int, int, str]:
    relative = candidate.relative_to(package).as_posix()
    lowered = relative.lower()
    source = read_text(candidate, limit=200_000)
    has_documentclass = "\\documentclass" in source
    score = 0 if has_documentclass else 100_000
    if relative in PREFERRED_TEX_NAMES:
        score -= 10_000 - PREFERRED_TEX_NAMES.index(relative)
    name = candidate.name.lower()
    if name == "main.tex":
        score -= 40
    elif name == "manuscript.tex":
        score -= 30
    elif name == "paper.tex":
        score -= 20
    if any(part.lower() in DEPRIORITIZED_PARTS for part in candidate.relative_to(package).parts[:-1]):
        score += 1_000
    return (score, len(candidate.relative_to(package).parts), lowered)


def choose_tex(package: Path) -> Path | None:
    candidates = [path for path in package.rglob("*.tex") if path.is_file()]
    if not candidates:
        return None
    candidates.sort(key=lambda path: tex_score(package, path))
    best = candidates[0]
    # Source fragments are never misrepresented as full text.  If all files
    # are fragments, leave the canonical manuscript unset and retain a card.
    if "\\documentclass" not in read_text(best, limit=200_000):
        return None
    return best


def pdf_score(package: Path, candidate: Path, tex: Path | None) -> tuple[int, int, str]:
    relative = candidate.relative_to(package).as_posix()
    score = 0
    if tex is not None and candidate.parent == tex.parent:
        score -= 100
    if candidate.name.lower() in PREFERRED_PDF_NAMES:
        score -= 50 - PREFERRED_PDF_NAMES.index(candidate.name.lower())
    if any(part.lower() in DEPRIORITIZED_PARTS for part in candidate.relative_to(package).parts[:-1]):
        score += 1_000
    return (score, len(candidate.relative_to(package).parts), relative.lower())


def choose_pdf(package: Path, tex: Path | None) -> Path | None:
    candidates = [path for path in package.rglob("*.pdf") if path.is_file()]
    if not candidates:
        return None
    candidates.sort(key=lambda path: pdf_score(package, path, tex))
    return candidates[0]


def choose_bibliography(package: Path, tex: Path | None) -> Path | None:
    candidates = [path for path in package.rglob("*.bib") if path.is_file()]
    if not candidates:
        return None
    candidates.sort(
        key=lambda path: (
            0 if tex is not None and path.parent == tex.parent else 1,
            len(path.relative_to(package).parts),
            path.as_posix(),
        )
    )
    return candidates[0]


def package_specs() -> Iterable[tuple[str, Path, str, str]]:
    """Yield route, package directory, source role, and source status."""

    zeta_root = REPO_ROOT / "zeta_mvp0"
    for package in sorted(zeta_root.glob("paper_*")):
        if package.is_dir():
            yield "zeta_mvp0", package, "native-programme-paper", "native-package"
    rh_root = zeta_root / "papers"
    for package in sorted(rh_root.glob("RH-*")):
        if package.is_dir():
            yield "zeta_mvp0", package, "imported-rh-archive", "archival-source-preserving"

    flow_root = REPO_ROOT / "flow_systems" / "papers"
    for package in sorted(flow_root.iterdir()):
        if package.is_dir():
            yield "flow_systems", package, "flow-package", "package-record"

    henon_root = REPO_ROOT / "henon_dynamics"
    for package in sorted(henon_root.glob("henon_*")):
        if package.is_dir():
            yield "henon_dynamics", package, "henon-package", "package-record"
    for batch in sorted(henon_root.glob("research_c*")):
        papers_dir = batch / "papers"
        if not papers_dir.is_dir():
            continue
        status = "preserved-in-progress" if batch.name == "research_c429_c433" else "batch-record"
        for package in sorted(papers_dir.iterdir()):
            if package.is_dir():
                yield "henon_dynamics", package, "henon-c-series-paper", status

    logistic_root = REPO_ROOT / "logistic_dynamics" / "projects"
    for package in sorted(logistic_root.iterdir()):
        if package.is_dir():
            yield "logistic_dynamics", package, "logistic-origin-project", "project-record"

    symbolic_root = REPO_ROOT / "symbolic_dynamics" / "papers"
    for package in sorted(symbolic_root.iterdir()):
        if package.is_dir() and re.match(r"^[0-9]+-", package.name):
            yield "symbolic_dynamics", package, "symbolic-paper", "package-record"

    symplectic_root = REPO_ROOT / "symplectic_map" / "papers"
    for package in sorted(symplectic_root.iterdir()):
        if package.is_dir() and package.name != "3-s_integral_clock":
            yield "symplectic_map", package, "symplectic-paper", "package-record"


def create_records() -> list[PaperRecord]:
    records: list[PaperRecord] = []
    used_ids: set[str] = set()
    for route, package, source_role, source_status in package_specs():
        tex = choose_tex(package)
        pdf = choose_pdf(package, tex)
        support = choose_supporting_markdown(package)
        bibliography = choose_bibliography(package, tex)
        # The selected TeX manuscript is the canonical reading source, so its
        # title takes priority over a supporting README or a claims matrix.
        title = latex_title(tex) or first_heading(support) or package.name.replace("_", " ")
        identifier = f"{route}--{slugify(package.name)}"
        if identifier in used_ids:
            raise RuntimeError(f"duplicate logical-paper id: {identifier}")
        used_ids.add(identifier)
        records.append(
            PaperRecord(
                id=identifier,
                route=route,
                title=title,
                source_package=repo_relative(package) or "",
                source_role=source_role,
                source_status=source_status,
                canonical_tex=repo_relative(tex),
                canonical_pdf=repo_relative(pdf),
                supporting_markdown=repo_relative(support),
                bibliography=repo_relative(bibliography),
                source_sha256=sha256(tex) if tex is not None else None,
            )
        )
    return sorted(records, key=lambda item: (item.route, item.id))


def source_path(relative: str | None) -> Path | None:
    return REPO_ROOT / relative if relative else None


def split_pandoc_front_matter(rendered: str) -> tuple[str, str]:
    if not rendered.startswith("---\n"):
        return "", rendered
    closing = rendered.find("\n---\n", 4)
    if closing == -1:
        return "", rendered
    return rendered[4:closing], rendered[closing + 5 :]


def convert_latex(tex: Path) -> tuple[str | None, str | None]:
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        return None, "pandoc is unavailable"
    command = [
        pandoc,
        "--from=latex",
        f"--to={PANDOC_TO}",
        "--standalone",
        "--atx-headers",
        "--wrap=none",
        str(tex),
    ]
    try:
        result = subprocess.run(
            command,
            cwd=tex.parent,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as error:
        return None, str(error)
    if result.returncode != 0 or len(result.stdout.strip()) < 80:
        detail = result.stderr.strip() or f"pandoc exited {result.returncode}"
        return None, detail[:1_000]
    return result.stdout, None


def convert_pdf(pdf: Path) -> tuple[str | None, str | None]:
    pdftotext = shutil.which("pdftotext")
    if pdftotext is None:
        return None, "pdftotext is unavailable"
    try:
        result = subprocess.run(
            [pdftotext, "-layout", str(pdf), "-"],
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as error:
        return None, str(error)
    if result.returncode != 0 or len(result.stdout.strip()) < 80:
        detail = result.stderr.strip() or f"pdftotext exited {result.returncode}"
        return None, detail[:1_000]
    return result.stdout, None


def locate_source_asset(tex: Path, package: Path, target: str) -> Path | None:
    """Resolve a Pandoc image target without guessing between duplicate files."""

    direct_candidates = ((tex.parent / target).resolve(), (package / target).resolve())
    for candidate in direct_candidates:
        if candidate.is_file():
            return candidate
    # A TeX ``\graphicspath`` is lost during Pandoc conversion.  For a bare
    # filename, recover an asset only when its package-level match is unique.
    basename = Path(target).name
    if not basename:
        return None
    matches = sorted({path.resolve() for path in package.rglob(basename) if path.is_file()})
    return matches[0] if len(matches) == 1 else None


def rewrite_rendered_links(rendered: str, tex: Path, package: Path, output: Path) -> str:
    """Make Pandoc-generated resource links valid from a reader-copy page.

    This is deliberately narrow: only a local image target that resolves to a
    real source file is rewritten.  It keeps all images in their source
    packages and creates a relative link from the derived page.  All other
    Pandoc output remains a faithful reading rendition.
    """

    def image_replacement(match: re.Match[str]) -> str:
        raw = match.group("target")
        target = raw[1:-1] if raw.startswith("<") and raw.endswith(">") else raw
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", target, re.IGNORECASE):
            return match.group(0)
        target = target.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0]
        source_asset = locate_source_asset(tex, package, target)
        if source_asset is None:
            return match.group(0)
        relative = os.path.relpath(source_asset, output.parent).replace(os.sep, "/")
        return f"{match.group(1)}<{relative}>{match.group(4)}"

    rendered = IMAGE_LINK.sub(image_replacement, rendered)
    return BARE_DOI_LINK.sub(
        lambda match: f"{match.group(1)}https://doi.org/{match.group('doi')}{match.group(3)}",
        rendered,
    )


def source_list(record: PaperRecord, page: Path) -> list[str]:
    links: list[str] = []
    package = source_path(record.source_package)
    if package is not None:
        links.append(markdown_link(page, package, "原始 package"))
    tex = source_path(record.canonical_tex)
    if tex is not None:
        links.append(markdown_link(page, tex, "规范 TeX"))
    pdf = source_path(record.canonical_pdf)
    if pdf is not None:
        links.append(markdown_link(page, pdf, "关联 PDF"))
    support = source_path(record.supporting_markdown)
    if support is not None:
        links.append(markdown_link(page, support, "支撑 Markdown"))
    bibliography = source_path(record.bibliography)
    if bibliography is not None:
        links.append(markdown_link(page, bibliography, "BibTeX"))
    return links


def card_text(record: PaperRecord, page: Path) -> str:
    fulltext = page.with_name("fulltext.md")
    route_index = page.parents[2] / "index.md"
    links = source_list(record, page)
    fulltext_link = markdown_link(page, fulltext, "Markdown 阅读副本")
    source_lines = "\n".join(f"- {item}" for item in links) or "- 未找到独立 source path。"
    return f"""---
p1_kind: {yaml_value('logical-paper-card')}
route: {yaml_value(record.route)}
logical_paper_id: {yaml_value(record.id)}
source_role: {yaml_value(record.source_role)}
source_status: {yaml_value(record.source_status)}
source_package: {yaml_value(record.source_package)}
canonical_tex: {yaml_value(record.canonical_tex)}
canonical_pdf: {yaml_value(record.canonical_pdf)}
source_sha256: {yaml_value(record.source_sha256)}
fulltext_status: {yaml_value(record.fulltext_status)}
claim_scope: {yaml_value('source-bound navigation record only')}
---

# {record.title}

[← 返回路线入口]({os.path.relpath(route_index, page.parent).replace(os.sep, '/')}) · {fulltext_link}

## 使用边界

这是一个逻辑论文／项目身份卡，不是新证据、审稿结论或路线晋级。请先阅读其所属路线的
[结论与边界]({os.path.relpath(route_index.with_name('conclusions.md'), page.parent).replace(os.sep, '/')})
与[路线图]({os.path.relpath(route_index.with_name('roadmap.md'), page.parent).replace(os.sep, '/')})，再进入正文。

## 原始入口

{source_lines}

## 渲染状态

- source role：`{record.source_role}`
- source status：`{record.source_status}`
- full-text：`{record.fulltext_status}`
- input SHA-256：`{record.source_sha256 or 'not-applicable'}`

没有规范主稿的项目仍保留本卡，以免计划、控制或历史项目被伪装为已完成论文。
"""


def fulltext_text(
    record: PaperRecord,
    page: Path,
    rendered: str | None,
    method: str | None,
    tex: Path | None,
    package: Path | None,
) -> str:
    card = page.with_name("index.md")
    source_links = source_list(record, page)
    source_lines = "\n".join(f"- {item}" for item in source_links) or "- 未找到独立 source path。"
    heading = f"# {record.title}\n\n[← 返回论文卡]({os.path.relpath(card, page.parent).replace(os.sep, '/')})\n"
    front_matter = f"""---
p1_kind: {yaml_value('derived-fulltext-reading-copy')}
route: {yaml_value(record.route)}
logical_paper_id: {yaml_value(record.id)}
canonical_tex: {yaml_value(record.canonical_tex)}
canonical_pdf: {yaml_value(record.canonical_pdf)}
source_sha256: {yaml_value(record.source_sha256)}
render_method: {yaml_value(method)}
render_status: {yaml_value(record.fulltext_status)}
---

"""
    notice = """## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

""" + source_lines + "\n"
    if rendered is None:
        error = record.render_error or "未找到可转换的规范主稿。"
        return front_matter + heading + notice + f"""
## 全文状态

`{record.fulltext_status}`：{error}

该 package 仍可经上面的原始入口和论文卡使用；不要把此占位页当作论文正文。
"""

    metadata, body = split_pandoc_front_matter(rendered)
    if tex is not None:
        body = rewrite_rendered_links(body, tex, package or tex.parent, page)
    metadata_section = ""
    if metadata.strip():
        metadata_section = f"""
## 转换器读取的文档元数据

```yaml
{metadata.rstrip()}
```
"""
    return front_matter + heading + notice + metadata_section + f"""
## Markdown 正文

{body.strip()}
"""


def paper_index_text(route: str, route_records: list[PaperRecord], page: Path) -> str:
    route_index = page.with_name("index.md")
    rows = []
    for record in route_records:
        card = page.parent / "papers" / record.id / "index.md"
        fulltext = card.with_name("fulltext.md")
        card_link = markdown_link(page, card, record.title.replace("|", "\\|"))
        full_link = markdown_link(page, fulltext, record.fulltext_status)
        rows.append(
            f"| `{record.id}` | {card_link} | `{record.source_role}` | `{record.source_status}` | {full_link} |"
        )
    table = "\n".join(rows)
    return f"""---
p1_kind: {yaml_value('route-paper-catalogue')}
route: {yaml_value(route)}
builder_version: {yaml_value(BUILDER_VERSION)}
---

# {ROUTE_LABELS[route]}：论文／项目目录

[← 返回路线入口]({os.path.relpath(route_index, page.parent).replace(os.sep, '/')}) ·
[来源与转换说明](sources.md)

每一行对应一个逻辑 package identity，而不是一个 PDF、一次构建或一个审稿快照。
`full-text` 的状态仅说明阅读副本可否生成，不等于论文、证据或 Route 状态。

| ID | 论文卡 | source role | source status | full-text |
| --- | --- | --- | --- | --- |
{table}
"""


def manifest_markdown(records: list[PaperRecord], pandoc_version: str) -> str:
    route_counts: dict[str, dict[str, int]] = {}
    for record in records:
        counts = route_counts.setdefault(record.route, {"records": 0, "generated": 0, "fallback": 0, "unavailable": 0})
        counts["records"] += 1
        if record.fulltext_status == "generated-from-latex":
            counts["generated"] += 1
        elif record.fulltext_status == "pdf-text-fallback":
            counts["fallback"] += 1
        else:
            counts["unavailable"] += 1
    rows = "\n".join(
        f"| {ROUTE_LABELS[route]} | {values['records']} | {values['generated']} | {values['fallback']} | {values['unavailable']} |"
        for route, values in sorted(route_counts.items())
    )
    return f"""# P1 Wiki conversion manifest

This manifest is generated by `tools/build_paper_corpus.py` version `{BUILDER_VERSION}`.
It is an identity and navigation record, not a scientific validation report.

## Source snapshot

- repository commit: `{git_head()}`
- converter: `{pandoc_version}`
- rendering rule: one logical package identity per reader page; TeX is preferred, PDF text is only a fallback.
- deletion rule: the builder never deletes derived pages.  A removed/renamed source needs an explicit maintenance review.

## Coverage

| Route | Logical records | TeX renders | PDF fallbacks | No canonical full text |
| --- | ---: | ---: | ---: | ---: |
{rows}

## Integrity boundary

Generated Markdown is a reading layer.  It does not replace canonical TeX/PDF, source data, proof objects,
review records, locked inputs, receipts, claim ledgers, or formal Route determinations.  In particular, a
successful render does not prove mathematical correctness or close an open gate.
"""


def git_head() -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            text=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except OSError:
        pass
    return "unavailable"


def pandoc_version() -> str:
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        return "unavailable"
    try:
        result = subprocess.run(
            [pandoc, "--version"],
            text=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        return result.stdout.splitlines()[0].strip() if result.returncode == 0 else "unavailable"
    except OSError:
        return "unavailable"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Pandoc's grid/table emission can leave presentation-only trailing spaces
    # and an extra terminal blank line.  A derived reading page has no semantic
    # use for either; normalizing them also keeps Git's conflict-marker and
    # whitespace checks meaningful.
    normalized = "\n".join(line.rstrip() for line in content.splitlines()).rstrip() + "\n"
    path.write_text(normalized, encoding="utf-8")


def build(records: list[PaperRecord]) -> None:
    converter = pandoc_version()
    for record in records:
        output_dir = DIRECTIONS_ROOT / record.route / "papers" / record.id
        fulltext = output_dir / "fulltext.md"
        rendered: str | None = None
        tex = source_path(record.canonical_tex)
        pdf = source_path(record.canonical_pdf)
        package = source_path(record.source_package)
        if tex is not None and tex.is_file():
            rendered, error = convert_latex(tex)
            if rendered is not None:
                record.fulltext_status = "generated-from-latex"
                record.render_method = f"pandoc --from=latex --to={PANDOC_TO}"
            else:
                record.render_error = error
        if rendered is None and pdf is not None and pdf.is_file():
            pdf_text, error = convert_pdf(pdf)
            if pdf_text is not None:
                rendered = f"## PDF 文本回退\n\n```text\n{pdf_text.rstrip()}\n```"
                record.fulltext_status = "pdf-text-fallback"
                record.render_method = "pdftotext -layout"
                record.render_error = None
            elif record.render_error is None:
                record.render_error = error
        if rendered is None:
            record.fulltext_status = "no-canonical-fulltext"
        write_text(fulltext, fulltext_text(record, fulltext, rendered, record.render_method, tex, package))
        card = output_dir / "index.md"
        write_text(card, card_text(record, card))

    for route in ROUTE_LABELS:
        route_records = [record for record in records if record.route == route]
        page = DIRECTIONS_ROOT / route / "paper-index.md"
        write_text(page, paper_index_text(route, route_records, page))

    META_ROOT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema": "p1-wiki-paper-manifest/1.0",
        "builder_version": BUILDER_VERSION,
        "repository_commit": git_head(),
        "pandoc_version": converter,
        "records": [asdict(record) for record in records],
    }
    write_text(META_ROOT / "paper-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    write_text(META_ROOT / "conversion-manifest.md", manifest_markdown(records, converter))


def check(records: list[PaperRecord]) -> int:
    manifest_path = META_ROOT / "paper-manifest.json"
    errors: list[str] = []
    if not manifest_path.is_file():
        errors.append("missing meta/paper-manifest.json")
    else:
        try:
            saved = json.loads(manifest_path.read_text(encoding="utf-8"))
            saved_records = {item["id"]: item for item in saved.get("records", [])}
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"unreadable manifest: {error}")
            saved_records = {}
        for record in records:
            saved_record = saved_records.get(record.id)
            if saved_record is None:
                errors.append(f"manifest lacks {record.id}")
                continue
            tex = source_path(record.canonical_tex)
            if tex is not None and tex.is_file() and saved_record.get("source_sha256") != sha256(tex):
                errors.append(f"source hash changed for {record.id}")
            output_dir = DIRECTIONS_ROOT / record.route / "papers" / record.id
            for filename in ("index.md", "fulltext.md"):
                if not (output_dir / filename).is_file():
                    errors.append(f"missing generated page {output_dir.relative_to(REPO_ROOT) / filename}")
            card = output_dir / "index.md"
            if card.is_file() and record.id not in card.read_text(encoding="utf-8", errors="replace"):
                errors.append(f"card identity mismatch for {record.id}")
    for route in ROUTE_LABELS:
        if not (DIRECTIONS_ROOT / route / "paper-index.md").is_file():
            errors.append(f"missing paper index for {route}")
    if errors:
        print("P1 wiki check: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"P1 wiki check: PASS ({len(records)} logical records)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify the existing corpus without writing")
    parser.add_argument("--dry-run", action="store_true", help="print planned record counts without writing")
    arguments = parser.parse_args()
    records = create_records()
    if arguments.dry_run:
        counts: dict[str, int] = {}
        for record in records:
            counts[record.route] = counts.get(record.route, 0) + 1
        print(json.dumps(counts, ensure_ascii=False, sort_keys=True))
        print(f"total={len(records)}")
        return 0
    if arguments.check:
        return check(records)
    build(records)
    print(f"P1 wiki corpus built: {len(records)} logical records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
