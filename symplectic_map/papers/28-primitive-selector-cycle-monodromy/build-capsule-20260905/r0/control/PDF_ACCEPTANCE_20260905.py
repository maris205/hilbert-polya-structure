#!/root/miniconda3/bin/python3.12
"""Frozen prospective Paper28 PDF structural acceptance; never edits a PDF.

Run only in the independently bound capsule/chroot, using Python -I -S -B:
  PDF_ACCEPTANCE_20260905.py --pdf /work/main.pdf --source-dir /source \
    --bbl /work/main.bbl \
    --output-dir /work/report \
    --site-packages /root/miniconda3/lib/python3.12/site-packages

Reads the locked source trio and derived main.bbl, and the given PDF. Writes
only a previously empty report directory. --self-test is memory-only and never
imports pymupdf. Exit 0 = automated structural gates pass, not visual/proof
review or overall publication acceptance. Exit 1 = explicit findings or error.
Page rendering follows successful input/parser/object inspection. Ordinary
acceptance findings, including pagination failure, do not short-circuit it;
a fatal parser/runtime exception is recorded and may prevent later artifacts.
The parent separately checks exact source/renderer bindings, compiler logs,
auxiliary convergence, overflow, cross-root identity and independent visual
review. This validator cannot replace any of those gates.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata


SITE = "/root/miniconda3/lib/python3.12/site-packages"
TITLE = ("Primitive Newton-Selector Cycles in Permutation-Twisted Hamiltonian "
         "Shears: Normal-Fan Classification and Exact Monodromy")
TERMINAL = ("The full mathematical argument, including the sharp failures and "
            "all decoder qualifications, is contained in the main text.")
SOURCE_HASHES = {
    "main.tex": "bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e",
    "math_commands.tex": "16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5",
    "references.bib": "e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e",
}
PROVENANCE = re.compile(
    r"(?:/root/|/home/|/work/|/control/|autodl|symplectic_map|"
    r"\bPaper\s*28\b|\bBatch\s*0?7\b|primitive_selector_cycle_monodromy_v1|"
    r"\bE0\d{3}\b|\b(?:BUILD_PROFILE|PUBLICATION_LOCK|SOURCE_LOCK|"
    r"TERMINAL_BLOCKER|CAPTURE2|RECOVERY_CONTEXT)\b|"
    r"\[(?:VERIFY|TODO|TBD)\]|\b(?:localhost|127\.0\.0\.1)\b)", re.I)
UNSAFE_KEYS = frozenset({
    "JavaScript", "JS", "Launch", "EmbeddedFiles", "EF", "RichMedia",
    "RichMediaContent", "RichMediaSettings", "AA", "OpenAction", "AcroForm",
    "XFA", "Collection", "SubmitForm", "ImportData", "Sound", "Movie", "Rendition",
})
UNSAFE_ACTIONS = frozenset({
    "GoToR", "GoToE", "Launch", "Thread", "URI_UNKNOWN", "Sound", "Movie",
    "Hide", "Named", "SubmitForm", "ResetForm", "ImportData", "JavaScript",
    "SetOCGState", "Rendition", "Trans", "GoTo3DView",
})


def sha(data):
    return hashlib.sha256(data).hexdigest()


def compact(text):
    """NFKC expands typographic ligatures; whitespace/soft hyphens alone vanish.

    Real hyphens and punctuation do not vanish. Exact source-phrase matchers
    separately permit a hard hyphen plus physical line break only inside a
    known word of their locked phrase; generic comparisons never delete it.
    """
    return "".join(c for c in unicodedata.normalize("NFKC", text)
                   if not c.isspace() and c != "\u00ad")


def compact_map(pages):
    text, physical = [], []
    for page_number, page in enumerate(pages, 1):
        for original in page:
            for char in unicodedata.normalize("NFKC", original):
                if not char.isspace() and char != "\u00ad":
                    text.append(char)
                    physical.append(page_number)
    return "".join(text), physical


def terminal_boundary(pages):
    # Preserve actual line endings and add an explicit form-feed only between
    # physical pages. The final marker character retains its original page.
    text, physical = [], []
    for page_number, page in enumerate(pages, 1):
        if page_number > 1:
            text.append("\f")
            physical.append(page_number - 1)
        for original in page:
            for char in unicodedata.normalize("NFKC", original):
                if char != "\u00ad":
                    text.append(char)
                    physical.append(page_number)
    text = "".join(text)
    matches = list(marker_expression(TERMINAL).finditer(text))
    if len(matches) != 1:
        raise ValueError("terminal sentence occurrence count is " + str(len(matches)))
    start, end = matches[0].span()
    content_page = physical[end - 1]
    extra = compact("".join(c for c, p in zip(text[end:], physical[end:])
                            if p == content_page))
    matched_hyphens = [{"physical_page": physical[start + match.start()],
                        "matched_text_offset": match.start(), "sequence": match.group(0)}
                       for match in re.finditer(r"-[ \t]*(?:\r\n|[\r\n\f])\s*", text[start:end])]
    return {"start_page": physical[start], "content_pages": content_page,
            "normalized_start": len(compact(text[:start])),
            "normalized_end_exclusive": len(compact(text[:end])),
            "marker_line_end_hyphens": matched_hyphens,
            "remaining_content_on_terminal_page": extra}


def marker_expression(marker):
    """An exact marker regex with word-local, line-ending-only hyphen support.

    Every marker character and punctuation mark remains mandatory. A rendered
    extra '-' is allowed only between consecutive alphabetic characters of one
    known marker word, and only immediately before a physical newline/page
    boundary (horizontal trailing whitespace allowed). Never modify document
    text globally, never permit a hyphen at a marker word boundary, and never
    delete a genuine hyphen present in the marker itself.
    """
    normalized = unicodedata.normalize("NFKC", marker)
    tokens = [(i, char) for i, char in enumerate(normalized)
              if not char.isspace() and char != "\u00ad"]
    pieces = []
    previous = None
    for position, char in tokens:
        if previous is not None:
            previous_position, previous_char = previous
            if position == previous_position + 1 and previous_char.isalpha() and char.isalpha():
                pieces.append(r"(?:\s*|-[ \t]*(?:\r\n|[\r\n\f])\s*)")
            else:
                pieces.append(r"\s*")
        pieces.append(re.escape(char))
        previous = (position, char)
    if not pieces:
        raise ValueError("empty marker")
    return re.compile("".join(pieces))


def source_headings(source):
    values = [(1 if kind == "section" else 2, title)
              for kind, title in re.findall(
                  r"^\\(section|subsection)\{([^{}]*)\}\s*$", source, re.M)]
    if len(values) != 40 or sum(level == 1 for level, _ in values) != 8:
        raise ValueError("locked plain source heading grammar/count mismatch")
    if any("\\" in title for _, title in values):
        raise ValueError("unexpected TeX in source heading")
    return values


def bibliography_keys(bib):
    return re.findall(r"^@(?:article|misc)\{([^,]+),", bib, re.M)


def bibliography_urls(bib):
    # Captured plainnat emits DOI with bare \Url, not hyperref's linked \url.
    # The two explicit Meunier public URLs are actual linked source targets.
    # Never add a host-wide allowance or an unrequested DOI resolver rewrite.
    explicit = re.findall(r"https?://[^\s{}]+", bib)
    return sorted(set(explicit))


def bbl_keys(bbl):
    # The locked plainnat style emits one bibitem with a single [...] author
    # option followed by the key; inner braces are harmless to this grammar.
    return re.findall(r"\\bibitem\[[^\]]*\]\s*\{([^{}]+)\}", bbl, re.S)


class Name(str):
    pass


class Ref(tuple):
    pass


def decode_pdf_string(value):
    if value.startswith(b"\xfe\xff"):
        return value[2:].decode("utf-16-be", errors="strict")
    if value.startswith(b"\xff\xfe"):
        return value[2:].decode("utf-16-le", errors="strict")
    return value.decode("latin1")


def parse_pdf_object(source):
    """Parse MuPDF's complete resolved object serialization, no regex-only audit.

    Accepted grammar: dictionaries with unique name keys, arrays, escaped names,
    literal/octal/hex strings, finite PDF numbers, references, bool and null.
    Unknown tokens, duplicate keys, trailing tokens and malformed strings fail.
    This is an object grammar, not an alternative PDF file parser.
    """
    data = source.encode("latin1")
    index = 0
    ws = b"\x00\t\n\x0c\r "
    delimiters = ws + b"()<>[]{}/%"

    def skip():
        nonlocal index
        while index < len(data):
            if data[index] in ws:
                index += 1
            elif data[index] == 37:
                while index < len(data) and data[index] not in b"\r\n":
                    index += 1
            else:
                break

    def value(depth=0):
        nonlocal index
        if depth > 100:
            raise ValueError("PDF nesting limit")
        skip()
        if data[index:index + 2] == b"<<":
            index += 2
            result = {}
            while True:
                skip()
                if data[index:index + 2] == b">>":
                    index += 2
                    return result
                key = value(depth + 1)
                if not isinstance(key, Name) or key in result:
                    raise ValueError("non-name or duplicate PDF dictionary key")
                result[str(key)] = value(depth + 1)
        if index >= len(data):
            raise ValueError("unexpected PDF object end")
        char = data[index]
        index += 1
        if char == 91:
            result = []
            while True:
                skip()
                if data[index:index + 1] == b"]":
                    index += 1
                    return result
                result.append(value(depth + 1))
        if char == 47:
            start = index
            while index < len(data) and data[index] not in delimiters:
                index += 1
            token = data[start:index]
            if re.search(rb"#(?![0-9a-fA-F]{2})", token):
                raise ValueError("bad PDF name escape")
            return Name(re.sub(rb"#([0-9a-fA-F]{2})",
                               lambda m: bytes([int(m[1], 16)]), token).decode("latin1"))
        if char == 40:
            result = bytearray()
            nesting = 1
            while index < len(data):
                char = data[index]
                index += 1
                if char == 92:
                    if index >= len(data):
                        raise ValueError("truncated literal escape")
                    escaped = data[index]
                    index += 1
                    if escaped in b"01234567":
                        digits = bytes([escaped])
                        for _ in range(2):
                            if index < len(data) and data[index] in b"01234567":
                                digits += data[index:index + 1]
                                index += 1
                        result.append(int(digits, 8) & 255)
                    elif escaped in b"\r\n":
                        if escaped == 13 and data[index:index + 1] == b"\n":
                            index += 1
                    else:
                        result.append({110: 10, 114: 13, 116: 9, 98: 8, 102: 12}.get(
                            escaped, escaped))
                elif char == 40:
                    nesting += 1
                    result.append(char)
                elif char == 41:
                    nesting -= 1
                    if nesting == 0:
                        return bytes(result)
                    result.append(char)
                else:
                    result.append(char)
            raise ValueError("unclosed PDF literal")
        if char == 60:
            finish = data.find(b">", index)
            if finish < 0:
                raise ValueError("unclosed PDF hex string")
            token = re.sub(rb"\s+", b"", data[index:finish])
            index = finish + 1
            if not re.fullmatch(rb"[0-9a-fA-F]*", token):
                raise ValueError("bad PDF hex string")
            if len(token) % 2:
                token += b"0"
            return bytes.fromhex(token.decode("ascii"))
        start = index - 1
        while index < len(data) and data[index] not in delimiters:
            index += 1
        token = data[start:index]
        if token in (b"true", b"false", b"null"):
            return {b"true": True, b"false": False, b"null": None}[token]
        if not re.fullmatch(rb"[+-]?(?:\d+(?:\.\d*)?|\.\d+)", token):
            raise ValueError("unexpected PDF token " + repr(token))
        number = float(token) if b"." in token else int(token)
        saved = index
        if isinstance(number, int):
            skip()
            candidate = re.match(rb"(\d+)\s+R(?=$|[\s\[\]<>/()])", data[index:])
            if candidate:
                index += candidate.end()
                return Ref((number, int(candidate[1])))
        index = saved
        return number

    result = value()
    skip()
    if index != len(data):
        raise ValueError("trailing PDF object tokens")
    return result


def audit_object(tree, allowed_urls, findings, location="object", parent_key=""):
    if isinstance(tree, dict):
        for key in tree:
            if key in UNSAFE_KEYS:
                findings.append({"code": "unsafe_pdf_key", "where": location, "key": key})
        if tree.get("Type") in (Name("Filespec"), Name("EmbeddedFile"), Name("ObjStm")):
            findings.append({"code": "forbidden_object_type", "where": location,
                             "type": str(tree["Type"])})
        if tree.get("Type") == Name("Annot") and tree.get("Subtype") != Name("Link"):
            findings.append({"code": "non_link_annotation", "where": location})
        if "URI" in tree:
            raw = tree["URI"]
            uri = decode_pdf_string(raw) if isinstance(raw, bytes) else None
            if uri not in allowed_urls:
                findings.append({"code": "unapproved_exact_uri", "where": location, "uri": uri})
        action = tree.get("S")
        is_action = (tree.get("Type") == Name("Action") or parent_key == "A"
                     or "URI" in tree or (isinstance(action, Name) and action in UNSAFE_ACTIONS)
                     or action in (Name("GoTo"), Name("URI")))
        if is_action and action not in (Name("GoTo"), Name("URI")):
            findings.append({"code": "unsafe_action", "where": location, "action": str(action)})
        for key, value in tree.items():
            audit_object(value, allowed_urls, findings, location + "/" + key, key)
    elif isinstance(tree, list):
        for i, item in enumerate(tree):
            audit_object(item, allowed_urls, findings, location + "/" + str(i), parent_key)
    elif isinstance(tree, bytes):
        text = decode_pdf_string(tree)
        match = PROVENANCE.search(text)
        if match:
            findings.append({"code": "provenance_string", "where": location,
                             "match": match.group(0)})
    elif isinstance(tree, Name):
        match = PROVENANCE.search(tree)
        if match:
            findings.append({"code": "provenance_name", "where": location,
                             "match": match.group(0)})


def self_test():
    assert compact("o\ufb03ce \ntext") == "officetext"
    boundary = terminal_boundary(["front", TERMINAL[:50], TERMINAL[50:]])
    assert boundary["content_pages"] == 3 and boundary["start_page"] == 2
    assert boundary["remaining_content_on_terminal_page"] == ""
    split_qualifiers = TERMINAL.replace("qualifications", "quali-\nfications")
    boundary = terminal_boundary([split_qualifiers])
    assert boundary["content_pages"] == 1 and len(boundary["marker_line_end_hyphens"]) == 1
    across_pages = TERMINAL.replace("qualifications", "qualifi-\ncations").split("\n")
    boundary = terminal_boundary(across_pages)
    assert boundary["start_page"] == 1 and boundary["content_pages"] == 2
    assert boundary["marker_line_end_hyphens"][0]["physical_page"] == 1
    multiple_splits = TERMINAL.replace("mathematical", "mathe-\nmatical").replace(
        "qualifications", "quali-\r\nfica-\ntions")
    assert len(terminal_boundary([multiple_splits])["marker_line_end_hyphens"]) == 3
    assert marker_expression("hand-derived.").fullmatch("hand-\nderived.") is not None
    assert marker_expression("hand-derived.").fullmatch("handderived.") is None
    assert marker_expression("hand-derived.").fullmatch("hand-\nderived!") is None
    assert marker_expression("Normal-fan classification").fullmatch(
        "Nor-\nmal-fan classi-\nfication") is not None
    assert marker_expression("Normal-fan classification").fullmatch(
        "Normalfan classification") is None
    assert compact("quali-\nfications") == "quali-fications"
    for pages in (["missing"], [TERMINAL, TERMINAL], [TERMINAL, split_qualifiers],
                  [split_qualifiers, split_qualifiers],
                  [TERMINAL.replace("qualifications", "quali-fications")],
                  [TERMINAL.replace("qualifications", "quali- fications")],
                  [TERMINAL.replace("all decoder", "all-\ndecoder")],
                  [TERMINAL.replace("qualifications,", "quali-\nfications;")]):
        try:
            terminal_boundary(pages)
        except ValueError:
            pass
        else:
            raise AssertionError("ambiguous marker accepted")
    obj = parse_pdf_object("<< /Type /Action /S /URI /URI (https://public.test/a\\(b\\)) >>")
    assert obj["URI"] == b"https://public.test/a(b)"
    assert parse_pdf_object("[1 0 R /Go#54o <FEFF0041> (x\\053y) null true -1.5]") == [
        Ref((1, 0)), Name("GoTo"), b"\xfe\xff\x00A", b"x+y", None, True, -1.5]
    for invalid in ("<< /A 1 /A 2 >>", "(unclosed", "[1", "1 trailing", "/A#zz"):
        try:
            parse_pdf_object(invalid)
        except (ValueError, IndexError):
            pass
        else:
            raise AssertionError("malformed PDF object accepted")
    findings = []
    audit_object(parse_pdf_object("<< /A << /S /Java#53cript /JS (bad) >> >>"), [], findings)
    assert {f["code"] for f in findings} >= {"unsafe_action", "unsafe_pdf_key"}
    findings = []
    audit_object(obj, ["https://public.test/a(b)"], findings)
    assert findings == []
    findings = []
    audit_object(parse_pdf_object("<< /A << /S /URI /URI (file:///root/private) >> >>"),
                 [], findings)
    assert {f["code"] for f in findings} >= {"unapproved_exact_uri", "provenance_string"}
    assert bibliography_urls("doi = {10.1/example}\nurl={https://public.test/~author/}") == [
        "https://public.test/~author/"]
    assert bbl_keys("\\bibitem[X(2000)]{A}\n\\bibitem[Y(2001)]{B}") == ["A", "B"]
    assert "pymupdf" not in sys.modules and "fitz" not in sys.modules
    print(json.dumps({"self_test": "PASS", "fitz_imported": False, "filesystem_writes": 0},
                     sort_keys=True))
    return 0


def json_write(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, sort_keys=True)
        stream.write("\n")


def run(args):
    out = Path(args.output_dir)
    if out.is_symlink() or not out.is_dir() or any(out.iterdir()):
        raise ValueError("output-dir must be an existing empty real directory")
    report = {"schema": "paper28-pdf-acceptance-v1", "findings": [],
              "automated_status": "FAIL", "visual_review": "PENDING_INDEPENDENT_REVIEW",
              "mathematical_review": "NOT_PERFORMED", "render_dpi": 72,
              "normalization": ("NFKC; whitespace/soft-hyphen comparison; exact locked terminal, "
                                "title and heading word-only line-end hard-hyphen matching; "
                                "preserve physical terminal char map; no global dehyphenation"),
              "date_policy": "CreationDate and ModDate absent or empty",
              "producer_allowlist": ["", "pdfTeX-1.40.22"]}
    findings = report["findings"]

    def require(condition, code, **details):
        if not condition:
            findings.append({"code": code, **details})

    try:
        require(sys.flags.isolated == 1 and sys.flags.no_site == 1
                and sys.dont_write_bytecode, "python_isolation_flags")
        if args.site_packages != SITE:
            raise ValueError("site-packages must be the exact captured path")
        sys.path[:] = ["/root/miniconda3/lib/python3.12",
                       "/root/miniconda3/lib/python3.12/lib-dynload", SITE]
        source = {}
        report["source_hashes"] = {}
        for name, expected in SOURCE_HASHES.items():
            path = Path(args.source_dir) / name
            if path.is_symlink() or not path.is_file():
                raise ValueError("source is not a real regular file: " + name)
            data = path.read_bytes()
            report["source_hashes"][name] = sha(data)
            require(sha(data) == expected, "source_hash_mismatch", name=name)
            source[name] = data.decode("utf-8")
        expected_headings = source_headings(source["main.tex"])
        keys = bibliography_keys(source["references.bib"])
        allowed_urls = bibliography_urls(source["references.bib"])
        require(len(keys) == 18 and len(set(keys)) == 18, "source_bib_key_count")
        bbl_path = Path(args.bbl)
        if bbl_path.is_symlink() or not bbl_path.is_file():
            raise ValueError("derived main.bbl must be a real regular file")
        bbl = bbl_path.read_bytes()
        ordered_keys = bbl_keys(bbl.decode("utf-8"))
        require(len(ordered_keys) == 18 and set(ordered_keys) == set(keys), "bbl_key_closure")
        report["bibliography"] = {"source_keys": keys, "bbl_sha256": sha(bbl),
                                  "bbl_order": ordered_keys, "exact_uri_allowlist": allowed_urls}
        pdf = Path(args.pdf)
        if pdf.is_symlink() or not pdf.is_file():
            raise ValueError("pdf must be a real regular file")
        data = pdf.read_bytes()
        report["pdf_sha256"] = sha(data)
        report["pdf_bytes"] = len(data)
        require(data.startswith(b"%PDF-1.5"), "pdf_version_header")
        require(data.rstrip().endswith(b"%%EOF") and data.count(b"%%EOF") == 1,
                "pdf_single_terminal_eof")
        require(len(re.findall(rb"(?m)^startxref\s*$", data)) == 1, "pdf_single_revision")
        for match in PROVENANCE.finditer(data.decode("latin1")):
            findings.append({"code": "provenance_raw_bytes", "match": match.group(0)})
        import pymupdf
        report["pymupdf_module"] = pymupdf.__file__
        require(str(Path(pymupdf.__file__).parent) == SITE + "/pymupdf",
                "unexpected_parser_origin")
        doc = pymupdf.open(stream=data, filetype="pdf")
        require(doc.is_pdf and not doc.is_repaired, "not_unrepaired_pdf")
        require(not doc.is_encrypted and not doc.needs_pass, "encrypted_pdf")
        require(doc.embfile_names() == [], "embedded_files")
        require(doc.get_xml_metadata() == "", "unexpected_xml_metadata")
        report["security"] = {"is_encrypted": doc.is_encrypted, "needs_pass": doc.needs_pass,
                              "permissions": doc.permissions, "is_repaired": doc.is_repaired}
        metadata = doc.metadata
        report["metadata"] = metadata
        expected_metadata = {"title": TITLE, "author": "Anonymous", "subject": "",
                             "keywords": "", "creator": "", "creationDate": "", "modDate": ""}
        for key, expected in expected_metadata.items():
            require(metadata.get(key, "") == expected, "metadata_value", field=key,
                    expected=expected, actual=metadata.get(key))
        require(metadata.get("producer", "") in ("", "pdfTeX-1.40.22"), "metadata_producer")
        require(metadata.get("encryption") is None, "metadata_encryption")

        objects, stream_records, stream_text = [], [], []
        trailer = parse_pdf_object(doc.xref_object(-1))
        require(isinstance(trailer, dict) and "Encrypt" not in trailer, "trailer_encrypt")
        require(isinstance(trailer, dict) and trailer.get("ID") in (None, []), "trailer_id")
        objects.append("TRAILER\n" + doc.xref_object(-1))
        audit_object(trailer, allowed_urls, findings, "trailer")
        info_kind, info_ref = doc.xref_get_key(-1, "Info")
        require(info_kind == "xref", "missing_info_dictionary")
        if info_kind == "xref":
            info_xref = int(info_ref.split()[0])
            info_keys = doc.xref_get_keys(info_xref)
            allowed_info = {"Title", "Author", "Subject", "Keywords", "Creator", "Producer",
                            "CreationDate", "ModDate", "Trapped"}
            require(set(info_keys) <= allowed_info, "unexpected_info_keys", keys=info_keys)
            raw_info = {key: doc.xref_get_key(info_xref, key) for key in info_keys}
            report["raw_info"] = raw_info
            for pdf_key, value in (("Title", TITLE), ("Author", "Anonymous"), ("Subject", ""),
                                   ("Keywords", ""), ("Creator", ""), ("CreationDate", ""),
                                   ("ModDate", "")):
                allowed = (("string", value),) if value else (("string", ""), ("null", "null"))
                require(doc.xref_get_key(info_xref, pdf_key) in allowed,
                        "raw_info_value", field=pdf_key)
            require(doc.xref_get_key(info_xref, "Producer") in (("null", "null"), ("string", ""),
                    ("string", "pdfTeX-1.40.22")), "raw_info_producer")
            require(doc.xref_get_key(info_xref, "Trapped") in (("null", "null"), ("name", "/False")),
                    "unexpected_trapped_value")
        font_stream_xrefs = set()
        for xref in range(1, doc.xref_length()):
            serialized = doc.xref_object(xref, compressed=False, ascii=True)
            objects.append("XREF " + str(xref) + "\n" + serialized)
            try:
                tree = parse_pdf_object(serialized)
                audit_object(tree, allowed_urls, findings, "xref/" + str(xref))
                if isinstance(tree, dict):
                    if tree.get("Type") == Name("FontDescriptor"):
                        for field in ("FontFile", "FontFile2", "FontFile3"):
                            ref = tree.get(field)
                            if isinstance(ref, Ref):
                                font_stream_xrefs.add(ref[0])
                    require(tree.get("Subtype") != Name("Image"), "unexpected_image", xref=xref)
            except (ValueError, IndexError, UnicodeError) as exc:
                findings.append({"code": "pdf_object_grammar", "xref": xref, "error": str(exc)})
            if doc.xref_is_stream(xref):
                raw = doc.xref_stream_raw(xref)
                decoded = doc.xref_stream(xref)
                stream_records.append({"xref": xref, "raw_bytes": len(raw), "raw_sha256": sha(raw),
                                       "decoded_bytes": len(decoded), "decoded_sha256": sha(decoded)})
                for match in PROVENANCE.finditer(decoded.decode("latin1")):
                    findings.append({"code": "provenance_decoded_stream", "xref": xref,
                                     "match": match.group(0)})
                stream_text.append((xref, decoded))
        with (out / "objects.txt").open("x", encoding="utf-8", newline="\n") as stream:
            stream.write("\n\n".join(objects) + "\n")
        with (out / "decoded-streams.txt").open("x", encoding="utf-8", newline="\n") as stream:
            for xref, decoded in stream_text:
                if xref in font_stream_xrefs:
                    stream.write("XREF " + str(xref) + " FONT PROGRAM: hash/size in streams.json\n")
                else:
                    stream.write("XREF " + str(xref) + "\n" + decoded.decode("latin1") + "\n\n")
        json_write(out / "streams.json", stream_records)

        pages, full_pages, page_records, links, fonts = [], [], [], [], {}
        for number in range(doc.page_count):
            page = doc.load_page(number)
            try:
                pixmap = page.get_pixmap(dpi=72, colorspace=pymupdf.csRGB, alpha=False)
                png = pixmap.tobytes("png")
                with (out / ("page-%03d.png" % (number + 1))).open("xb") as stream:
                    stream.write(png)
                rendered = {"file": "page-%03d.png" % (number + 1), "sha256": sha(png),
                            "width": pixmap.width, "height": pixmap.height}
            except Exception as exc:
                findings.append({"code": "page_render_error", "page": number + 1, "error": repr(exc)})
                rendered = {"error": repr(exc)}
            require(page.rotation == 0 and abs(page.rect.width - 612) < 0.01
                    and abs(page.rect.height - 792) < 0.01
                    and list(page.mediabox) == [0.0, 0.0, 612.0, 792.0]
                    and list(page.cropbox) == [0.0, 0.0, 612.0, 792.0],
                    "letter_page_geometry", page=number + 1)
            extracted = page.get_text("dict", sort=True, flags=pymupdf.TEXT_PRESERVE_WHITESPACE)
            retained, all_lines, footer_lines = [], [], []
            for block in extracted["blocks"]:
                if block.get("type") != 0:
                    continue
                for line in block["lines"]:
                    line_text = "".join(span["text"] for span in line["spans"])
                    all_lines.append(line_text)
                    if line["bbox"][1] > 740 and line_text.strip() == str(number + 1):
                        footer_lines.append({"text": line_text, "bbox": list(line["bbox"])})
                    else:
                        retained.append(line_text)
            full_pages.append("\n".join(all_lines))
            text = "\n".join(retained)
            pages.append(text)
            require(len(footer_lines) == 1, "physical_page_footer", page=number + 1,
                    count=len(footer_lines))
            require(bool(compact(text)), "empty_physical_page", page=number + 1)
            require("??" not in text and "[?]" not in text, "undefined_reference_text", page=number + 1)
            match = PROVENANCE.search(text)
            require(match is None, "provenance_visible_page", page=number + 1,
                    match=match.group(0) if match else None)
            require(list(page.annots() or []) == [], "non_link_page_annotations", page=number + 1)
            require(list(page.widgets() or []) == [], "page_widgets", page=number + 1)
            for link in page.get_links():
                record = {k: (list(v) if isinstance(v, (pymupdf.Rect, pymupdf.Point)) else v)
                          for k, v in link.items()}
                record["physical_page"] = number + 1
                links.append(record)
                if link["kind"] == pymupdf.LINK_URI:
                    require(link.get("uri") in allowed_urls, "unexpected_link_uri", link=record)
                else:
                    require(link["kind"] == pymupdf.LINK_GOTO
                            and 0 <= link.get("page", -1) < doc.page_count,
                            "invalid_internal_link", link=record)
            for item in doc.get_page_fonts(number, full=True):
                xref = item[0]
                if xref not in fonts:
                    name, ext, kind, program = doc.extract_font(xref)
                    fonts[xref] = {"xref": xref, "name": name, "extension": ext, "type": kind,
                                   "bytes": len(program), "sha256": sha(program), "pages": []}
                    require(xref > 0 and bool(program) and ext not in ("", "n/a"),
                            "unembedded_font", xref=xref, name=name)
                fonts[xref]["pages"].append(number + 1)
            page_records.append({"physical_page": number + 1, "rect": list(page.rect),
                                 "footer_lines_removed_for_comparison_only": footer_lines,
                                 "text_sha256": sha(text.encode("utf-8")), "render": rendered})
        require(bool(fonts), "no_fonts")
        report["pages"] = page_records
        report["total_pages"] = doc.page_count
        with (out / "pages.txt").open("x", encoding="utf-8", newline="\n") as stream:
            stream.write("\f".join(full_pages) + "\n")
        with (out / "comparison-pages.txt").open("x", encoding="utf-8", newline="\n") as stream:
            stream.write("\f".join(pages) + "\n")
        json_write(out / "fonts.json", sorted(fonts.values(), key=lambda f: f["xref"]))
        json_write(out / "links.json", links)

        if pages:
            first_lines = [line.strip() for line in pages[0].splitlines() if line.strip()]
            abstracts = [i for i, line in enumerate(first_lines) if line == "Abstract"]
            require(len(abstracts) == 1, "abstract_heading_count")
            if len(abstracts) == 1:
                visible_header = unicodedata.normalize("NFKC", "\n".join(
                    first_lines[:abstracts[0]])).replace("\u00ad", "")
                require(marker_expression(TITLE + "\nAnonymous").fullmatch(visible_header) is not None,
                        "visible_title_author_empty_date")
        boundary = None
        try:
            boundary = terminal_boundary(pages)
            report["content_boundary"] = boundary
            require(not boundary["remaining_content_on_terminal_page"], "text_after_terminal_sentence")
            require(22 <= boundary["content_pages"] <= 30, "content_page_gate_22_30",
                    actual=boundary["content_pages"])
        except ValueError as exc:
            findings.append({"code": "terminal_boundary", "error": str(exc)})
        refs = [(p + 1, i) for p, page in enumerate(pages)
                for i, line in enumerate([v for v in page.splitlines() if v.strip()])
                if line.strip() == "References"]
        require(len(refs) == 1, "standalone_references_heading_count", actual=len(refs))
        if len(refs) == 1:
            ref_page, ref_line = refs[0]
            report["references_start_page"] = ref_page
            require(ref_line == 0, "references_not_first_content_on_fresh_page")
            if boundary is not None:
                require(ref_page == boundary["content_pages"] + 1,
                        "references_not_immediately_after_content")
            reference_text = "\n".join(pages[ref_page - 1:])
            labels = [int(v) for v in re.findall(r"(?m)^\s*\[(\d+)\](?:\s|$)", reference_text)]
            report["bibliography"]["rendered_numeric_labels"] = labels
            require(labels == list(range(1, 19)), "rendered_bibliography_labels")
            require(compact(reference_text).startswith("References[1]"), "bibliography_prefix")
            for _, heading in expected_headings:
                require(marker_expression(heading).search(unicodedata.normalize(
                    "NFKC", reference_text).replace("\u00ad", "")) is None,
                        "body_heading_after_references", heading=heading)

        toc = doc.get_toc(simple=True)
        json_write(out / "bookmarks.json", toc)
        require([(row[0], row[1]) for row in toc] == expected_headings,
                "exact_40_plain_source_bookmarks")
        require(all(1 <= row[2] <= doc.page_count for row in toc), "bookmark_target_page")
        require([row[2] for row in toc] == sorted(row[2] for row in toc), "bookmark_order")
        for level, heading, target in toc:
            require("\\" not in heading and "$" not in heading, "raw_tex_bookmark", heading=heading)
            if 1 <= target <= len(pages):
                require(marker_expression(heading).search(unicodedata.normalize(
                    "NFKC", pages[target - 1]).replace("\u00ad", "")) is not None,
                        "bookmark_heading_not_on_target_page", heading=heading, target=target)
        names = doc.resolve_names()
        json_write(out / "destinations.json", names)
        citation_names = {name[5:] for name in names if name.startswith("cite.")}
        require(citation_names == set(keys), "citation_destination_key_closure")
        for name, destination in names.items():
            require(0 <= destination.get("page", -1) < doc.page_count,
                    "unresolved_named_destination", name=name)
            require(PROVENANCE.search(name) is None, "provenance_destination", name=name)
        if len(refs) == 1:
            for key in keys:
                destination = names.get("cite." + key, {})
                require(destination.get("page", -1) + 1 >= refs[0][0],
                        "citation_destination_outside_bibliography", key=key)
        doc.close()
        require(pdf.read_bytes() == data, "pdf_changed_during_inspection")
    except Exception as exc:
        findings.append({"code": "validator_exception", "type": type(exc).__name__, "error": str(exc)})
    report["automated_status"] = "PASS" if not findings else "FAIL"
    report["finding_count"] = len(findings)
    report["artifacts"] = [path.name for path in sorted(out.iterdir())]
    json_write(out / "acceptance.json", report)
    print(json.dumps({"automated_status": report["automated_status"],
                      "finding_count": len(findings), "pdf_sha256": report.get("pdf_sha256"),
                      "content_boundary": report.get("content_boundary"),
                      "total_pages": report.get("total_pages"),
                      "visual_review": "PENDING_INDEPENDENT_REVIEW"}, sort_keys=True))
    return 0 if not findings else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--pdf")
    parser.add_argument("--source-dir")
    parser.add_argument("--bbl")
    parser.add_argument("--output-dir")
    parser.add_argument("--site-packages")
    args = parser.parse_args()
    if args.self_test:
        if any((args.pdf, args.source_dir, args.bbl, args.output_dir, args.site_packages)):
            parser.error("--self-test accepts no filesystem arguments")
        return self_test()
    if not all((args.pdf, args.source_dir, args.bbl, args.output_dir, args.site_packages)):
        parser.error("all five path arguments are required")
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
