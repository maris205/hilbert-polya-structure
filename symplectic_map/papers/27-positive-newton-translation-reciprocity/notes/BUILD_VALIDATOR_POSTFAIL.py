#!/usr/bin/env python3
"""Fail-closed deterministic validator for the Paper 27 post-failure successor build."""

import fcntl
import hashlib
import math
import os
import re
import resource
import stat
import sys
import zlib


PROJECT = "/root/autodl-tmp/symplectic_map/papers/27-positive-newton-translation-reciprocity"
BUILD_PARENT = PROJECT + "/build"
EVIDENCE = BUILD_PARENT + "/postfail-d60ec6611683-evidence"
ROOT0 = BUILD_PARENT + "/postfail-d60ec6611683-r0"
ROOT1 = BUILD_PARENT + "/postfail-d60ec6611683-r1"
STAGE0 = EVIDENCE + "/r0"
STAGE1 = EVIDENCE + "/r1"
CROSS_STAGE = EVIDENCE + "/cross-root"
VALIDATOR_SOURCE = PROJECT + "/notes/BUILD_VALIDATOR_POSTFAIL.py"
VALIDATOR_COPY = EVIDENCE + "/BUILD_VALIDATOR_POSTFAIL.py"
VALIDATOR_LOCK = PROJECT + "/notes/VALIDATOR_LOCK_POSTFAIL.md"
VALIDATOR_IDENTITY_BEGIN = "BATCH07_VALIDATOR_IDENTITY_BEGIN"
VALIDATOR_IDENTITY_END = "BATCH07_VALIDATOR_IDENTITY_END"
VALIDATOR_TERMINAL = "# BATCH07_P27_BUILD_VALIDATOR_POSTFAIL_AUTHOR_STOP"
VALIDATOR_LOCK_TERMINAL = "BATCH07_P27_VALIDATOR_LOCK_POSTFAIL_AUTHOR_STOP"

PROFILE = PROJECT + "/notes/BUILD_PROFILE_POSTFAIL.md"
DEPENDENCY_LOCK = PROJECT + "/notes/DEPENDENCY_LOCK_SUCCESSOR.md"
DEPENDENCY_REVIEW = PROJECT + "/notes/INDEPENDENT_DEPENDENCY_LOCK_SUCCESSOR_REVIEW.md"
PROFILE_REVIEW = PROJECT + "/notes/INDEPENDENT_BUILD_PROFILE_POSTFAIL_REVIEW.md"
SOURCE_REVIEW = PROJECT + "/notes/INDEPENDENT_STATIC_SOURCE_SUCCESSOR_REVIEW.md"
SOURCE_MAIN = PROJECT + "/paper/main.tex"
SOURCE_COMMANDS = PROJECT + "/paper/math_commands.tex"
SOURCE_BIB = PROJECT + "/paper/references.bib"

MAX_DYNAMIC_BYTES = 64 * 1024 * 1024
MAX_OBJECT_STREAM_BYTES = 16 * 1024 * 1024
MAX_TOTAL_OBJECT_STREAM_BYTES = 32 * 1024 * 1024
MAX_CONTENT_STREAM_BYTES = 16 * 1024 * 1024
MAX_TOTAL_CONTENT_STREAM_BYTES = 64 * 1024 * 1024
MAX_TOTAL_CONTENT_TOKENS = 2_000_000
MAX_PDF_TOKENS = 2_000_000
MAX_PDF_OBJECTS = 100_000
MAX_PDF_TOKEN_BYTES = 4096
MAX_PDF_STRING_BYTES = 64 * 1024
MAX_PDF_STREAM_DICTIONARY_BYTES = 256 * 1024
KIB = 1024
MIB = 1024 * KIB
MAX_TYPE1_PROGRAM_BYTES = 16 * MIB
MAX_TYPE1_CLEAR_BYTES = MIB
MAX_TYPE1_EEXEC_BYTES = 16 * MIB
MAX_TYPE1_TAIL_BYTES = 64 * KIB
MAX_TYPE1_TOKEN_BYTES = 4096
MAX_TYPE1_STRING_BYTES = 64 * KIB
MAX_PDF_TYPE1_DECODED_BYTES = 64 * MIB
MAX_PDF_TYPE1_LEXICAL_TOKENS = 4_000_000
MAX_PDF_TYPE1_CHARSTRING_TOKENS = 2_000_000
MAX_PDF_TYPE1_CONCRETE_STEPS = 4_000_000
MAX_PDF_TYPE1_ABSTRACT_STEPS = 4_000_000
MAX_BLG_LINE_BYTES = 4096
MAX_RECORDER_LINES = 200000
MAX_RECORDER_LINE_BYTES = 16 * KIB
MAX_PDF_TEXT_LINES = 200000
MAX_PDF_TEXT_LINE_BYTES = 64 * KIB
MIN_NOFILE = 1024
MAX_NOFILE = 4096
MAX_WARNING_FRAME_BYTES = 256 * KIB
MAX_WARNING_LINES = 4096
MAX_LOG_LINE_BYTES = 4096
MAX_LOG_LINES = 200000
MAX_STAGE_TOTAL_BYTES = 128 * MIB
MAX_ROOT_TOTAL_BYTES = 96 * MIB
MAX_CROSS_TOTAL_BYTES = 4 * MIB
MAX_EVIDENCE_REGULAR_BYTES = 2 * MIB
CHUNK = 1024 * 1024
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
ACTIVE_DIRECTORY_ANCHORS = {}
ACTIVE_REGULAR_ANCHORS = {}
EXACT_VALIDATOR_ENV = {
    b"LANG": b"C",
    b"LC_ALL": b"C",
    b"PATH": b"/usr/bin:/bin",
    b"PYTHONDONTWRITEBYTECODE": b"1",
    b"PYTHONHASHSEED": b"0",
    b"PYTHONIOENCODING": b"UTF-8:strict",
    b"PYTHONNOUSERSITE": b"1",
    b"PYTHONSAFEPATH": b"1",
    b"PYTHONUTF8": b"1",
    b"TZ": b"UTC",
}

CONTROL_IDENTITIES = {
    PROFILE: (53878, 963, 0o644, 1, "f4829e21e4626b372a05e646f34d29f0ea306b653d23d6dd924d1fc54161687e"),
    DEPENDENCY_LOCK: (30145, 215, 0o644, 1, "66c96cc6b40658370cc129e3bf828bcd08a7e69f7f2462ebea084cc77ce6ed17"),
    DEPENDENCY_REVIEW: (12687, 231, 0o644, 1, "b37e361c1cb8e7340c7a2e4af5b207de40df935ced707043c63c1e0f7017df35"),
    PROFILE_REVIEW: (13492, 248, 0o644, 1, "b1bbdf96dc68ae1ee4e6ce984616c106931c5f2d462117808f8747f6496d887b"),
    SOURCE_REVIEW: (31760, 704, 0o644, 1, "7745af4b80e4e5ff35134e9279b7d2493f9b063bac0110bab115199bae3114ae"),
}

SOURCE_IDENTITIES = {
    SOURCE_MAIN: (55063, 1681, 0o644, 1, "d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e"),
    SOURCE_COMMANDS: (601, 17, 0o644, 1, "34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957"),
    SOURCE_BIB: (6610, 217, 0o644, 1, "a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5"),
}

REGULAR_TOOLS = {
    "/usr/bin/pdftex": (1802504, 0o755, 1, "01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9"),
    "/usr/bin/bibtex.original": (117128, 0o755, 1, "c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f"),
    "/usr/bin/env": (43976, 0o755, 1, "85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0"),
    "/usr/bin/bash": (1396520, 0o755, 1, "59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4"),
    "/usr/bin/mkdir": (68104, 0o755, 1, "bd2f081ac37d653181332bd27f35a6041dbf215a7957f65838a9cbec9e64928b"),
    "/usr/bin/install": (145944, 0o755, 1, "519a00d199d07da6028ec5a9800d92c562934582a2ea1793b2cbc378a85c1439"),
    "/root/miniconda3/bin/python3.12": (30626264, 0o755, 1, "9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101"),
    "/usr/bin/cmp": (43408, 0o755, 1, "b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791"),
    "/usr/bin/pdfinfo": (59928, 0o755, 1, "8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e"),
    "/usr/bin/pdftotext": (43544, 0o755, 1, "7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d"),
}

SYMLINK_TOOLS = {
    "/usr/bin/pdflatex": (6, 0o777, 1, b"pdftex", "/usr/bin/pdftex"),
    "/usr/bin/bibtex": (24, 0o777, 1, b"/etc/alternatives/bibtex", "/etc/alternatives/bibtex"),
    "/etc/alternatives/bibtex": (24, 0o777, 1, b"/usr/bin/bibtex.original", "/usr/bin/bibtex.original"),
    "/root/miniconda3/bin/python3": (10, 0o777, 1, b"python3.12", "/root/miniconda3/bin/python3.12"),
}

ROOT_CONFIG = {
    ROOT0: (STAGE0, "r0"),
    ROOT1: (STAGE1, "r1"),
}

ROOT_SOURCE_PATHS = {
    ROOT0: (
        ROOT0 + "/main.tex",
        ROOT0 + "/math_commands.tex",
        ROOT0 + "/references.bib",
    ),
    ROOT1: (
        ROOT1 + "/main.tex",
        ROOT1 + "/math_commands.tex",
        ROOT1 + "/references.bib",
    ),
}

ROOT_STATES = {
    "R020-pre": "SETUP",
    "R020-post": "TEX1",
    "R030-pre": "TEX1",
    "R030-post": "BIB",
    "R040-pre": "BIB",
    "R040-post": "TEX2",
    "R050-pre": "TEX2",
    "R050-post": "FINAL",
}

EXPECTED_KEYS = (
    "abboud_xie_2026", "bedford_kim_2008", "berger_turaev_2025",
    "bianchi_dinh_rakhimov_2024", "blanc_van_santen_2022",
    "cheng_wang_yu_1994", "dang_favre_2021", "deserti_2018",
    "el_hilany_2024", "favre_wulcan_2012", "fordy_hone_2011",
    "gomez_meiss_2004", "grigoriev_containment", "hasselblatt_propp_2007",
    "janeczko_jelonek_2008", "koch_lomeli_2014", "nisse_2026",
    "shafikov_wolf_2003", "shao_sun_2025", "takenawa_2026",
)

TITLE = "Diagonal-Translation Rigidity and Literal Phase Reciprocity in Positive Newton-Fan Hamiltonian Shears"
HEADINGS = (
    "1 Introduction", "2 Collision positioning", "3 Typed cells and main theorem",
    "4 Positive-face survival", "5 Translation, envelopes, equality, and tail",
    "6 Full spans and literal reciprocity", "7 One-step radius and complete fixture",
    "8 Boundaries and conclusion",
)
CLAUSES = (
    "Typed survival", "Translation and transience", "Equality and tail",
    "Literal word reciprocity", "One-step radius",
)
MODULE_ANCHORS = (
    "Phase data and source rows", "The grouped face Hessian",
    "Discrete pair count and equality", "Full spans and literal reciprocity",
    "Fixed rows and an explicit half-margin radius", "Matrices and complete row lists",
)
FIXTURES = ("P1", "P2", "P3", "Q1", "Q2", "Q3")
BOUNDARIES = (
    "Characteristic zero", "Positive coordinates",
    "Coordinate lower bound and strictness", "Complete row family", "First carry",
    "Literal reflected label", "Positive-support cancellation control",
)
CONCLUSION = (
    "Larger typed fan systems and perturbations of the row data would require new "
    "hypotheses and proofs; they are directions beyond the present result."
)

DEPENDENCY_ROWS_TEXT = """/etc/texmf/web2c/texmf.cnf\t/etc/texmf/web2c/texmf.cnf\t/etc/texmf/web2c/texmf.cnf\t475\t0644\t1\t3443c7e22fbb4585732473f7e95d3cbf3e8657100f9117e711e2af5b0db85a40
/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst\t/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst\t/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst\t20613\t0644\t1\t19f2cf88686b86aaa8e65d5f0313a92499815761e04b42e84ea2c3dc3685ada9
/usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map\t/usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map\t/usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map\t3524\t0644\t1\td9693993efdc7d0b9ab3df777589995d43e24eeae95f12b6a230a19caadeaa42
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm\t1004\t0644\t1\t373172fe340e4aede5129b89d65f576bfb1fe6932bd55c38f60bcaa84f3d1188
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm\t988\t0644\t1\t3f56ab22f7fc6a015813976c6c6cc2fd55736bbaec4958a4562e10719fa18062
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm\t916\t0644\t1\t3b54bde5cb0e0bd071eea7bc702ed3a1a284f786779ef8e75b06eba4104bb9f2
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm\t924\t0644\t1\tc800d1dfd533040219fcc06d52e0e00c2a20fb9b0039fe9f58ccec53fd003a9f
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm\t928\t0644\t1\t719d100c110fa1cfae9ad0b63e6c21753f4980f925fa516c1a04961e206f69d5
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm\t908\t0644\t1\td9f5f519ec718e9dbccb8527c1f5d3b4a008dfb946377f97f71611b385d3d010
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm\t940\t0644\t1\t9e0909a297a3097e50960158d324006ddd5302db665400fa1fdf966df14e1a17
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm\t940\t0644\t1\t361b5530a4b410c6274e9330c11e993843c62e394323aeaa6e0aee61e8042444
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm\t1328\t0644\t1\tae296e8e41b2b0f73e9a17fdc42c743b9ddcc58d23c30acaa3411206f7824780
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm\t1324\t0644\t1\t0eb2f13840155007c2d3c59b074322a3aa7358b9643aa314f3146468ae7f0806
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm\t1332\t0644\t1\ta746151d8e3a521965bbfae2666e1528374a514375daa7d620e9b89ebbbfb0ae
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm\t1344\t0644\t1\t38ded79d7cce07fa28921f37f6b88e67bd86951a3e5af709c219d63454786ce1
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx7.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx7.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx7.tfm\t1336\t0644\t1\te7b284f0ee98b7773be9b57ca652b4bb14391370509a424b5b62b06b5cae86e4
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm\t1332\t0644\t1\t6dab44c885b7cbf567771d9cfa565f3df34d0e8124132b9b6f9fdc496a1c2eda
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmex10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmex10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmex10.tfm\t992\t0644\t1\t0890bccea1dd4d27f001ac30e86c63af35bc803e0557c35aafb1903c8d208e92
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm\t1528\t0644\t1\te442c5487f84df70218ff37f775c87060856f5b6e04c011b6cadbbadfcf46645
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm\t1524\t0644\t1\t79563547084d85388e6909888f9fa7f5cad33bdda44ca6b25b362e1d301db539
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm\t1512\t0644\t1\tab6ecb4aaba9ca1b4259b1d1f64309a785bbaeb09183fd79a066b7764a448a28
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm\t1520\t0644\t1\t65af8c1e162a952cab8e93c834fcf43ce09b508e6c16e512ebb673cd850b0d41
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr10.tfm\t1296\t0644\t1\t87f2d8981927644cbecaf3d639e96e348ea4e7be49d8804468bd8ba9ff3f5244
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm\t1288\t0644\t1\t1ce8af37ed38e93940829d3540e494eaaddc5201758d036b9074467e70a738dc
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr17.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr17.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr17.tfm\t1292\t0644\t1\t86b6e8a52aae6ad1655e32099e12bd2904b158aba4c8afb74143266d2d9cd18f
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm\t1300\t0644\t1\t106afa9172f0c00e58b9f5cbc72b302a18aaeeaddf50caca145af9cc0b81afd2
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr8.tfm\t1292\t0644\t1\t4c5ae243ac0aa254e7ec7f0602cc2a4351e5011ff0cb6dc150a5f6de19585de6
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss10.tfm\t1316\t0644\t1\t431472f34665b6243a32936215f2e17d1f124cdf8513e86e2bedc4c3de3f980b
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss8.tfm\t1296\t0644\t1\t25650d37e11bee41e03dc4757a1b6f1a64f27a53c664aa618d1a8ded54d96ed5
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy10.tfm\t1124\t0644\t1\t0ca13d421ac7133271aed7c935099ecf3d1d08ac9e15f81acb34a16564ab8a46
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm\t1116\t0644\t1\t137eb9f38f661c66309614066a7b5d63d8969d33aba0c9efee9f844a4ce65b50
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy8.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy8.tfm\t1120\t0644\t1\t84c37f07ca360c41ad0a0fba7387d279d72457c69bdae03653208c683d8de6bc
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmti10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmti10.tfm\t/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmti10.tfm\t1480\t0644\t1\t46a66e937f809c4fbe317947b583a14b408aca41ecb835eca3be46391190432a
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb\t34811\t0644\t1\tca41102968b817bf6e8b22fd6de205ca23bf5088218511cce0c8129e1577cb70
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb\t32080\t0644\t1\tc838238f31d86a9f198873dfaf501601a4fc966845b9c59e7dc251c4e85d1f1f
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb\t32166\t0644\t1\tfe99cd3dcadd182a24b86e593e56d2e900c992311218c43779f858ed6e1c3b31
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb\t30251\t0644\t1\t791b31aa1db8608d0144b3a40fc0fe53383a60f6b00d0e8fd9f06ac4a11df8cb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb\t36299\t0644\t1\te3661061e8aa474d6de5ffa916edceb0e3d8b998862018c147f0357fce00bcd7
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb\t37166\t0644\t1\tc31dbaffb861162eadf3a7210bdf271b0dda577841aed4c0572069b0d52662b6
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb\t36281\t0644\t1\t5b293a581ddb937b02559c3ce1a60184cc434295533204a2cd3864a6ad8a1f53
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb\t35469\t0644\t1\tf396f52d9ed3498c15aa7e694baef74c0a11119624fcd6db66dad4ac76972cb0
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb\t35752\t0644\t1\tfdcede8794018df5f2b58f0905fb20a2b418ed8f67b73ee12445855dfbe5b1be
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb\t32722\t0644\t1\t9b58bfa828b9553b7c8331cf26c45443b836f8aab62e820b40a5b65c8531dd42
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb\t32362\t0644\t1\t465827b4702e12f7deea159c8084753ffc27998963de516e490bd7bd5bed41dd
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb\t32734\t0644\t1\t9fe20cb9ef24a0f4c74d38a65d4eee5cff3165f3b8600407ceba396aeb2b7617
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb\t32762\t0644\t1\tb37e8671820b0753c6e233eaa3230c6ab9cff04e6c4baee312d60ae261e5aba1
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb\t32726\t0644\t1\t8150cbfac5cfe53040327df171c3059f10730b32cabf2504b01713d639a11feb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb\t24457\t0644\t1\tc9071fd676395df32520c3d906f2829898ea735f66c40a40578dec3c0ac51738
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb\t24420\t0644\t1\t7f5744c7caf27c407888cadae84be6cd7c05f34cf2c5df385b8f69fa349a3feb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb\t32569\t0644\t1\t62ee8cef552017551cd3e026a483e700730103eceaad959c87b7730017f59cff
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb\t32587\t0644\t1\t73eed8a83a07d8ef04d240da22bce1fd3646074f46179e3677f4f42a542f20b6
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb\t32716\t0644\t1\t583b65bd1857bffc2ab184fcb4aad4e70e12eb05c9ca9f1c58c9a00a86c8bccf
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb\t32626\t0644\t1\t2313392f0f4cd974d9da5fb54a52feae126059759edc04a4e47e33ea6027418b
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb\t37944\t0644\t1\tb6f162e1549a649c7e9b2edfb77306f60e1b0da74547f33cba39ff6ba0bdd473
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb\t30273\t0644\t1\t778a2aaea4bf9d19ce2a7342864fa2696c07770c86d36a62e2ef799ad0724b05
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb\t/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb\t34694\t0644\t1\td2121de7e7c14490a2d352e3b62e62882d6c300235464bfa577e6055696e6e62
/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\t/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\t/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\t71627\t0644\t1\t5dd3675b88c7b61d3703e6bf35ed75623acc6b163dff7b1477b485cee8ad71cb
/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty\t/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty\t/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty\t12594\t0644\t1\t8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty\t5949\t0644\t1\tdab8b0e621267acfd89736cf97bdcc02647c545c0719c4997be8a7d1bf98f9c3
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\t13829\t0644\t1\t70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd\t/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd\t/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd\t961\t0644\t1\t48355e960333be747dd7b4500e76fde7c3ef0b1fa9c74ec0f1438af0d3a661a4
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd\t/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd\t/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd\t961\t0644\t1\te20f21f6ed631cbe3a627d5da5fef82367732a7d51207f8df5ee7e9c77ee342e
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty\t2222\t0644\t1\t7f25c33d4010066ff2eed0286f62854867698b06d10ebad93b1b1ab96d12f936
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty\t4173\t0644\t1\td90cfa74087e9f8678fb81bde57f809f0d4043f2674cb23b73a85958ec4a0fb6
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\t87648\t0644\t1\t027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty\t4128\t0644\t1\t18c28b99321d0f4576cb42e2793d2654828b273700224cd9ee27047f803e99f5
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\t/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\t2444\t0644\t1\t49426425d82407dc702c77236fdeb4b82568ebb9566b8dd849bcfbf9eb9644de
/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\t/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\t/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\t20144\t0644\t1\t988fb3e599df7e5b545e4253829dab11f0c7bd7827b79d32c2aaadfb52db6f6c
/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo\t/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo\t/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo\t8464\t0644\t1\tefc946da03cfa55c75be27d73012ab866fcc935fd47ac4a674026bbdbdcfa9f1
/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\t/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\t/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\t6078\t0644\t1\t3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc
/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty\t/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty\t/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty\t51697\t0644\t1\ta217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3
/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg\t/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg\t/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg\t1224\t0644\t1\tfeb91e48789a21e4acced98e952c77a2e2cf4a77e01bf147b59fa56a1b3f2008
/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def\t/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def\t/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def\t19103\t0644\t1\t62c3a2892e6acc3d94b1e8a50ecc2a11a16565ddee3f68006a84822eb5b93a5d
/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\t/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\t/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\t18399\t0644\t1\t63cb7c6ae98653209d8f77ee842849676930fd694bc45a771309e0486c1cd9b5
/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\t/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\t/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\t7996\t0644\t1\tda1e0ad80baeea2859059307358257c506069c91bdd29fde9e12ee957cc5db44
/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty\t/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty\t/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty\t2671\t0644\t1\tcdac603619a4c129511ef8a3abfbb4d2068b1bb67626cb30568baa0ceb26aea2
/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty\t/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty\t/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty\t4009\t0644\t1\t4af1b021af86649d926eb025a92fa4a3603f0d65893ccdb6fb756b5a16810a51
/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def\t/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def\t/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def\t29921\t0644\t1\t9617358386bec1691faec14fd624634525f105505a5f9573c47bd4f617ddcb5d
/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty\t/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty\t/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty\t59397\t0644\t1\te6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7
/usr/share/texlive/texmf-dist/tex/latex/mathtools/mhsetup.sty\t/usr/share/texlive/texmf-dist/tex/latex/mathtools/mhsetup.sty\t/usr/share/texlive/texmf-dist/tex/latex/mathtools/mhsetup.sty\t5582\t0644\t1\tc3ae1e23f43029fbfc271e3b1440a692e1cd924d1810430b99e4f2aa5b9ccf09
/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty\t/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty\t/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty\t12694\t0644\t1\t1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157
/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty\t/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty\t/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty\t10214\t0644\t1\t57beb2c684bafae5e22ed8ebf3873d279c68038200b1d47703f88d87cd2ea6d2
/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty\t/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty\t/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty\t12892\t0644\t1\t196f2a7038e1727c4088a015bf11cac88abfedc5b7ee5eca65f44ab91dbac415
/usr/share/texlive/texmf-dist/web2c/texmf.cnf\t/usr/share/texlive/texmf-dist/web2c/texmf.cnf\t/usr/share/texlive/texmf-dist/web2c/texmf.cnf\t39432\t0644\t1\tced214c26baca02d79428fd1e7f3acf59e8d60436e28bc269c3fde93e1f70bab
/usr/share/texmf/web2c/texmf.cnf\t/usr/share/texmf/web2c/texmf.cnf=>/usr/share/texlive/texmf-dist/web2c/texmf.cnf\t/usr/share/texlive/texmf-dist/web2c/texmf.cnf\t39432\t0644\t1\tced214c26baca02d79428fd1e7f3acf59e8d60436e28bc269c3fde93e1f70bab
/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map\t/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map=>/var/lib/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map\t/var/lib/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map\t4123914\t0644\t1\tf2ef4883e12f9f53a33778e8f99cc2006e1434898cbcf493784e3c46f9ed9b18
/var/lib/texmf/web2c/pdftex/pdflatex.fmt\t/var/lib/texmf/web2c/pdftex/pdflatex.fmt\t/var/lib/texmf/web2c/pdftex/pdflatex.fmt\t1503567\t0644\t1\t5e3d04e4b504653152b7fbbe415f78de3d353795a3c3d9ceb68e39bb3c0cf8f0
"""

DEPENDENCY_ROWS = tuple(
    (fields[0], fields[1], fields[2], int(fields[3]), int(fields[4], 8),
     int(fields[5]), fields[6])
    for fields in (line.split("\t") for line in DEPENDENCY_ROWS_TEXT[:-1].split("\n"))
)
DEPENDENCY_LOGICAL = frozenset(row[0] for row in DEPENDENCY_ROWS)
DEPENDENCY_FINAL = frozenset(row[2] for row in DEPENDENCY_ROWS)
DEPENDENCY_SYMLINKS = {
    "/usr/share/texmf/web2c/texmf.cnf": (
        40, 0o777, 1, b"../../texlive/texmf-dist/web2c/texmf.cnf",
        "/usr/share/texlive/texmf-dist/web2c/texmf.cnf",
    ),
    "/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map": (
        15, 0o777, 1, b"pdftex_dl14.map",
        "/var/lib/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map",
    ),
}


class CheckFail(Exception):
    pass


class UsageFail(Exception):
    pass


SNAPSHOT_MAP = {
    (ROOT0, "R021"): (ROOT0 + "/main.log", STAGE0 + "/R021--main.log.snapshot"),
    (ROOT0, "R022"): (ROOT0 + "/main.aux", STAGE0 + "/R022--main.aux.snapshot"),
    (ROOT0, "R023"): (ROOT0 + "/main.fls", STAGE0 + "/R023--main.fls.snapshot"),
    (ROOT0, "R031"): (ROOT0 + "/main.bbl", STAGE0 + "/R031--main.bbl.snapshot"),
    (ROOT0, "R032"): (ROOT0 + "/main.blg", STAGE0 + "/R032--main.blg.snapshot"),
    (ROOT0, "R041"): (ROOT0 + "/main.log", STAGE0 + "/R041--main.log.snapshot"),
    (ROOT0, "R042"): (ROOT0 + "/main.aux", STAGE0 + "/R042--main.aux.snapshot"),
    (ROOT0, "R043"): (ROOT0 + "/main.fls", STAGE0 + "/R043--main.fls.snapshot"),
    (ROOT0, "R051"): (ROOT0 + "/main.log", STAGE0 + "/R051--main.log.snapshot"),
    (ROOT0, "R052"): (ROOT0 + "/main.aux", STAGE0 + "/R052--main.aux.snapshot"),
    (ROOT0, "R053"): (ROOT0 + "/main.fls", STAGE0 + "/R053--main.fls.snapshot"),
    (ROOT1, "R021"): (ROOT1 + "/main.log", STAGE1 + "/R021--main.log.snapshot"),
    (ROOT1, "R022"): (ROOT1 + "/main.aux", STAGE1 + "/R022--main.aux.snapshot"),
    (ROOT1, "R023"): (ROOT1 + "/main.fls", STAGE1 + "/R023--main.fls.snapshot"),
    (ROOT1, "R031"): (ROOT1 + "/main.bbl", STAGE1 + "/R031--main.bbl.snapshot"),
    (ROOT1, "R032"): (ROOT1 + "/main.blg", STAGE1 + "/R032--main.blg.snapshot"),
    (ROOT1, "R041"): (ROOT1 + "/main.log", STAGE1 + "/R041--main.log.snapshot"),
    (ROOT1, "R042"): (ROOT1 + "/main.aux", STAGE1 + "/R042--main.aux.snapshot"),
    (ROOT1, "R043"): (ROOT1 + "/main.fls", STAGE1 + "/R043--main.fls.snapshot"),
    (ROOT1, "R051"): (ROOT1 + "/main.log", STAGE1 + "/R051--main.log.snapshot"),
    (ROOT1, "R052"): (ROOT1 + "/main.aux", STAGE1 + "/R052--main.aux.snapshot"),
    (ROOT1, "R053"): (ROOT1 + "/main.fls", STAGE1 + "/R053--main.fls.snapshot"),
}

MANIFEST_MAP = {
    (ROOT0, "R009"): ("SETUP", STAGE0 + "/R009--root.manifest"),
    (ROOT0, "R024"): ("TEX1", STAGE0 + "/R024--root.manifest"),
    (ROOT0, "R033"): ("BIB", STAGE0 + "/R033--root.manifest"),
    (ROOT0, "R044"): ("TEX2", STAGE0 + "/R044--root.manifest"),
    (ROOT0, "R054"): ("FINAL", STAGE0 + "/R054--root.manifest"),
    (ROOT1, "R009"): ("SETUP", STAGE1 + "/R009--root.manifest"),
    (ROOT1, "R024"): ("TEX1", STAGE1 + "/R024--root.manifest"),
    (ROOT1, "R033"): ("BIB", STAGE1 + "/R033--root.manifest"),
    (ROOT1, "R044"): ("TEX2", STAGE1 + "/R044--root.manifest"),
    (ROOT1, "R054"): ("FINAL", STAGE1 + "/R054--root.manifest"),
}

RECORDER_MAP = {
    (ROOT0, "R023"): STAGE0 + "/R023--main.fls.snapshot",
    (ROOT0, "R043"): STAGE0 + "/R043--main.fls.snapshot",
    (ROOT0, "R053"): STAGE0 + "/R053--main.fls.snapshot",
    (ROOT1, "R023"): STAGE1 + "/R023--main.fls.snapshot",
    (ROOT1, "R043"): STAGE1 + "/R043--main.fls.snapshot",
    (ROOT1, "R053"): STAGE1 + "/R053--main.fls.snapshot",
}

R033_LIVE_MAP = {
    ROOT0: (ROOT0 + "/main.fls", STAGE0 + "/R023--main.fls.snapshot"),
    ROOT1: (ROOT1 + "/main.fls", STAGE1 + "/R023--main.fls.snapshot"),
}

BIB_MAP = {
    ROOT0: (ROOT0 + "/main.bbl", ROOT0 + "/main.blg", STAGE0 + "/R031--main.bbl.snapshot", STAGE0 + "/R032--main.blg.snapshot"),
    ROOT1: (ROOT1 + "/main.bbl", ROOT1 + "/main.blg", STAGE1 + "/R031--main.bbl.snapshot", STAGE1 + "/R032--main.blg.snapshot"),
}

FINAL_MAP = {
    ROOT0: (
        ROOT0 + "/main.log", ROOT0 + "/main.aux", ROOT0 + "/main.bbl",
        ROOT0 + "/main.blg", ROOT0 + "/main.pdf", STAGE0 + "/R060.stdout",
        STAGE0 + "/R062.stdout",
    ),
    ROOT1: (
        ROOT1 + "/main.log", ROOT1 + "/main.aux", ROOT1 + "/main.bbl",
        ROOT1 + "/main.blg", ROOT1 + "/main.pdf", STAGE1 + "/R060.stdout",
        STAGE1 + "/R062.stdout",
    ),
}

ROOT_INIT_IDS = ("R000", "R001", "R002", "R003", "R004", "R005", "R006", "R007", "R008")
PUBLICATION_IDS = ("R020", "R030", "R040", "R050")
ROOT_VALIDATOR_IDS = (
    "A000", "R009", "V020P", "V020Q", "R021", "R022", "R023", "C023", "R024",
    "V030P", "V030Q", "R031", "R032", "B032", "L033", "R033",
    "V040P", "V040Q", "R041", "R042", "R043", "C043", "R044",
    "V050P", "V050Q", "R051", "R052", "R053", "C053", "R054",
    "F055", "F061", "F063", "F064", "F065",
)
ROOT_INSPECTION_IDS = ("R060", "R062")
ROOT_PRE_INVENTORY_IDS = ROOT_INIT_IDS + PUBLICATION_IDS + ROOT_VALIDATOR_IDS + ROOT_INSPECTION_IDS
ROOT_FINAL_IDS = ROOT_PRE_INVENTORY_IDS + ("I066",)

ROOT_VALIDATOR_MODES = {
    "A000": "ABSENT", "R009": "MANIFEST",
    "V020P": "REPLAY", "V020Q": "REPLAY",
    "R021": "SNAPSHOT", "R022": "SNAPSHOT", "R023": "SNAPSHOT",
    "C023": "RECORDER", "R024": "MANIFEST",
    "V030P": "REPLAY", "V030Q": "REPLAY",
    "R031": "SNAPSHOT", "R032": "SNAPSHOT", "B032": "BIB",
    "L033": "R033LIVE", "R033": "MANIFEST",
    "V040P": "REPLAY", "V040Q": "REPLAY",
    "R041": "SNAPSHOT", "R042": "SNAPSHOT", "R043": "SNAPSHOT",
    "C043": "RECORDER", "R044": "MANIFEST",
    "V050P": "REPLAY", "V050Q": "REPLAY",
    "R051": "SNAPSHOT", "R052": "SNAPSHOT", "R053": "SNAPSHOT",
    "C053": "RECORDER", "R054": "MANIFEST", "F055": "SOURCEFINAL",
    "F061": "PDFINFO", "F063": "PDFTEXT", "F064": "PDFRAW",
    "F065": "LOGBIB", "I066": "STAGEINV",
}
ROOT_VALIDATOR_SECOND_FIELDS = {
    "R009": "id=R009",
    "V020P": "checkpoint=R020-pre", "V020Q": "checkpoint=R020-post",
    "R021": "id=R021", "R022": "id=R022", "R023": "id=R023",
    "C023": "id=R023", "R024": "id=R024",
    "V030P": "checkpoint=R030-pre", "V030Q": "checkpoint=R030-post",
    "R031": "id=R031", "R032": "id=R032", "R033": "id=R033",
    "V040P": "checkpoint=R040-pre", "V040Q": "checkpoint=R040-post",
    "R041": "id=R041", "R042": "id=R042", "R043": "id=R043",
    "C043": "id=R043", "R044": "id=R044",
    "V050P": "checkpoint=R050-pre", "V050Q": "checkpoint=R050-post",
    "R051": "id=R051", "R052": "id=R052", "R053": "id=R053",
    "C053": "id=R053", "R054": "id=R054",
}

SNAPSHOT_BASENAMES = (
    "R021--main.log.snapshot", "R022--main.aux.snapshot", "R023--main.fls.snapshot",
    "R031--main.bbl.snapshot", "R032--main.blg.snapshot",
    "R041--main.log.snapshot", "R042--main.aux.snapshot", "R043--main.fls.snapshot",
    "R051--main.log.snapshot", "R052--main.aux.snapshot", "R053--main.fls.snapshot",
)
MANIFEST_BASENAMES = (
    "R009--root.manifest", "R024--root.manifest", "R033--root.manifest",
    "R044--root.manifest", "R054--root.manifest",
)

EVIDENCE_ROOT_IDS = ("E001", "E010", "E011", "E012")
CROSS_COMPARE_IDS = ("X001", "X002", "X003", "X004", "X005", "X006", "X007", "X008")
CROSS_PRE_INVENTORY_IDS = CROSS_COMPARE_IDS + ("X009",)
CROSS_FINAL_IDS = CROSS_PRE_INVENTORY_IDS + ("X010",)


def _receipt_basenames(ids):
    return tuple(name for ident in ids for name in (ident + ".stdout", ident + ".stderr", ident + ".status"))


ROOT_STAGE_PRE_NAMES = tuple(sorted(_receipt_basenames(ROOT_PRE_INVENTORY_IDS) + SNAPSHOT_BASENAMES + MANIFEST_BASENAMES))
ROOT_STAGE_FINAL_NAMES = tuple(sorted(_receipt_basenames(ROOT_FINAL_IDS) + SNAPSHOT_BASENAMES + MANIFEST_BASENAMES))
EVIDENCE_ROOT_NAMES = tuple(sorted(
    ("BUILD_VALIDATOR_POSTFAIL.py", "r0", "r1", "cross-root") + _receipt_basenames(EVIDENCE_ROOT_IDS)
))
CROSS_STAGE_PRE_NAMES = tuple(sorted(_receipt_basenames(CROSS_PRE_INVENTORY_IDS)))
CROSS_STAGE_FINAL_NAMES = tuple(sorted(_receipt_basenames(CROSS_FINAL_IDS)))
EVIDENCE_ROOT_AT_ABSENT = {
    ROOT0: tuple(sorted(("BUILD_VALIDATOR_POSTFAIL.py", "r0") + _receipt_basenames(("E001", "E010")))),
    ROOT1: tuple(sorted(("BUILD_VALIDATOR_POSTFAIL.py", "r0", "r1") + _receipt_basenames(("E001", "E010", "E011")))),
}
CROSS_STAGE_BEFORE_CROSS_NAMES = tuple(sorted(_receipt_basenames(CROSS_COMPARE_IDS)))
EVIDENCE_CROSS_INFLIGHT_NAMES = tuple(sorted(CROSS_STAGE_PRE_NAMES + ("X010.stdout", "X010.stderr")))
ROOT_STAGE_TIMELINE = (
    ("A000",) + ROOT_INIT_IDS +
    ("R009", "V020P", "R020", "V020Q", "R021", "R022", "R023", "C023", "R024",
     "V030P", "R030", "V030Q", "R031", "R032", "B032", "L033", "R033",
     "V040P", "R040", "V040Q", "R041", "R042", "R043", "C043", "R044",
     "V050P", "R050", "V050Q", "R051", "R052", "R053", "C053", "R054",
     "F055", "R060", "F061", "R062", "F063", "F064", "F065", "I066")
)
ROOT_STAGE_CREATED_FILES = {
    "R009": ("R009--root.manifest",),
    "R021": ("R021--main.log.snapshot",),
    "R022": ("R022--main.aux.snapshot",),
    "R023": ("R023--main.fls.snapshot",),
    "R024": ("R024--root.manifest",),
    "R031": ("R031--main.bbl.snapshot",),
    "R032": ("R032--main.blg.snapshot",),
    "R033": ("R033--root.manifest",),
    "R041": ("R041--main.log.snapshot",),
    "R042": ("R042--main.aux.snapshot",),
    "R043": ("R043--main.fls.snapshot",),
    "R044": ("R044--root.manifest",),
    "R051": ("R051--main.log.snapshot",),
    "R052": ("R052--main.aux.snapshot",),
    "R053": ("R053--main.fls.snapshot",),
    "R054": ("R054--root.manifest",),
}

MODE_ARITY = {
    "ABSENT": 2,
    "REPLAY": 2,
    "SNAPSHOT": 4,
    "MANIFEST": 3,
    "RECORDER": 3,
    "R033LIVE": 3,
    "BIB": 5,
    "LOGBIB": 7,
    "PDFINFO": 3,
    "PDFTEXT": 3,
    "PDFRAW": 2,
    "SOURCEFINAL": 1,
    "CROSS": 1,
    "STAGEINV": 2,
    "EVIDENCE": 2,
}

VALIDATOR_RESULT_FIELDS = {
    "ABSENT": ("root", "absent", "stage_empty", "dependencies"),
    "REPLAY": ("root", "checkpoint", "root_rows", "root_sha256", "dependencies"),
    "SNAPSHOT": ("root", "id", "bytes", "LF", "sha256"),
    "MANIFEST": ("root", "id", "rows", "bytes", "sha256"),
    "RECORDER": ("root", "id", "bytes", "LF", "sha256", "normalized_sha256",
                 "local_inputs", "local_outputs", "external_unique"),
    "R033LIVE": ("root", "bytes", "LF", "sha256"),
    "BIB": ("root", "items", "bbl_sha256", "blg_sha256"),
    "LOGBIB": ("root", "sentinel", "pages", "warnings", "warning_sha256",
               "disposition", "warning_bytes_hex", "log_sha256", "aux_sha256",
               "bbl_sha256", "blg_sha256", "pdf_sha256"),
    "PDFINFO": ("root", "pages", "bytes", "pdf_sha256"),
    "PDFTEXT": ("root", "pages", "reference_page", "text_sha256",
                "pre_reference_sha256"),
    "PDFRAW": ("root", "pages", "fonts", "descriptors", "font_streams",
               "streams", "bytes", "sha256"),
    "SOURCEFINAL": ("root", "source_files", "root_rows", "manifest_sha256"),
    "CROSS": ("raw_pairs", "recorder_pairs", "manifest_pairs", "projected_fields",
              "recorder_sha256", "manifest_sha256", "sentinel", "pages", "warnings",
              "aggregate_sha256"),
    "STAGEINV": ("stage", "items", "framing_bytes", "inventory_sha256",
                 "root_manifest_sha256"),
    "EVIDENCE": ("pre_X010", "root_entries", "r0_items", "r1_items",
                 "cross_items", "inventory_sha256"),
}

DECIMAL_RESULT_FIELDS = frozenset({
    "absent", "stage_empty", "root_rows", "bytes", "LF", "rows", "local_inputs",
    "local_outputs", "external_unique", "items", "sentinel", "pages", "warnings",
    "reference_page", "fonts", "descriptors", "font_streams", "streams",
    "source_files", "raw_pairs", "recorder_pairs", "manifest_pairs",
    "projected_fields", "framing_bytes", "pre_X010", "root_entries", "r0_items",
    "r1_items", "cross_items",
})

EXACT_ARGV_ROWS = frozenset(
    [("ABSENT", root, stage) for root, (stage, _) in ROOT_CONFIG.items()] +
    [("REPLAY", root, checkpoint) for root in ROOT_CONFIG for checkpoint in ROOT_STATES] +
    [("SNAPSHOT", root, ident, source, destination)
     for (root, ident), (source, destination) in SNAPSHOT_MAP.items()] +
    [("MANIFEST", root, ident, destination)
     for (root, ident), (_, destination) in MANIFEST_MAP.items()] +
    [("RECORDER", root, ident, snapshot)
     for (root, ident), snapshot in RECORDER_MAP.items()] +
    [("R033LIVE", root, live, snapshot)
     for root, (live, snapshot) in R033_LIVE_MAP.items()] +
    [("BIB", root, bbl, blg, bbl_snapshot, blg_snapshot)
     for root, (bbl, blg, bbl_snapshot, blg_snapshot) in BIB_MAP.items()] +
    [("LOGBIB", root, *FINAL_MAP[root][:6]) for root in ROOT_CONFIG] +
    [("PDFINFO", root, FINAL_MAP[root][4], FINAL_MAP[root][5]) for root in ROOT_CONFIG] +
    [("PDFTEXT", root, FINAL_MAP[root][5], FINAL_MAP[root][6]) for root in ROOT_CONFIG] +
    [("PDFRAW", root, FINAL_MAP[root][4]) for root in ROOT_CONFIG] +
    [("SOURCEFINAL", root) for root in ROOT_CONFIG] +
    [("CROSS", CROSS_STAGE)] +
    [("STAGEINV", STAGE0, "r0-pre-I066"), ("STAGEINV", STAGE1, "r1-pre-I066")] +
    [("EVIDENCE", EVIDENCE, CROSS_STAGE)]
)


ROOT_ALLOWED_NAMES = {
    "SETUP": ("main.tex", "math_commands.tex", "references.bib", "texmf-var", "texmf-config", "texmf-home", "xdg-cache", "tmp"),
    "TEX1": ("main.aux", "main.fls", "main.log", "main.pdf", "main.tex", "math_commands.tex", "references.bib", "texmf-var", "texmf-config", "texmf-home", "xdg-cache", "tmp"),
    "BIB": ("main.aux", "main.bbl", "main.blg", "main.fls", "main.log", "main.pdf", "main.tex", "math_commands.tex", "references.bib", "texmf-var", "texmf-config", "texmf-home", "xdg-cache", "tmp"),
    "TEX2": ("main.aux", "main.bbl", "main.blg", "main.fls", "main.log", "main.pdf", "main.tex", "math_commands.tex", "references.bib", "texmf-var", "texmf-config", "texmf-home", "xdg-cache", "tmp"),
    "FINAL": ("main.aux", "main.bbl", "main.blg", "main.fls", "main.log", "main.pdf", "main.tex", "math_commands.tex", "references.bib", "texmf-var", "texmf-config", "texmf-home", "xdg-cache", "tmp"),
}
CACHE_NAMES = ("texmf-var", "texmf-config", "texmf-home", "xdg-cache", "tmp")
SOURCE_BASENAME_IDENTITIES = {
    "main.tex": SOURCE_IDENTITIES[SOURCE_MAIN],
    "math_commands.tex": SOURCE_IDENTITIES[SOURCE_COMMANDS],
    "references.bib": SOURCE_IDENTITIES[SOURCE_BIB],
}


def _fail(tag):
    raise CheckFail(tag)


def _usage(tag):
    raise UsageFail(tag)


def _bounded_decimal(value, tag, maximum, positive=False):
    if isinstance(value, bytes):
        try:
            raw = value.decode("ascii", "strict")
        except UnicodeDecodeError:
            _fail(tag + "_ASCII")
    elif isinstance(value, str):
        raw = value
    else:
        _fail(tag + "_TYPE")
    grammar = r"[1-9][0-9]*" if positive else r"0|[1-9][0-9]*"
    if (len(raw) > len(str(maximum)) or re.fullmatch(grammar, raw) is None):
        _fail(tag + "_GRAMMAR")
    number = int(raw)
    if number > maximum:
        _fail(tag + "_BOUND")
    return number


def _fixed_width_decimal(value, width, tag, maximum):
    if (not isinstance(value, bytes) or len(value) != width or
            re.fullmatch(rb"[0-9]+", value) is None):
        _fail(tag + "_GRAMMAR")
    number = 0
    for byte in value:
        number = number * 10 + byte - 0x30
    if number > maximum:
        _fail(tag + "_BOUND")
    return number


def _path_bytes(path):
    try:
        raw = path.encode("ascii", "strict")
    except UnicodeEncodeError:
        _usage("NON_ASCII_PATH")
    if not path.startswith("/") or b"\x00" in raw:
        _usage("NONCANONICAL_PATH")
    return raw


def _path_parts(path):
    raw = _path_bytes(path)
    if raw == b"/" or raw.endswith(b"/") or b"//" in raw:
        _usage("NONCANONICAL_PATH")
    parts = raw.split(b"/")[1:]
    if not parts or any(part in (b"", b".", b"..") for part in parts):
        _usage("NONCANONICAL_PATH")
    return tuple(parts)


def _stat_key(st):
    return (
        st.st_dev, st.st_ino, st.st_mode, st.st_nlink, st.st_uid, st.st_gid,
        st.st_rdev, st.st_size, st.st_mtime_ns, st.st_ctime_ns,
    )


def _anchor_key(st):
    return (
        st.st_dev, st.st_ino, st.st_mode, st.st_uid, st.st_gid, st.st_rdev,
    )


def _close_fds(fds):
    for fd in reversed(fds):
        try:
            os.close(fd)
        except OSError:
            pass


def _open_parent_chain(path, tag):
    parts = _path_parts(path)
    try:
        root_fd = os.open(b"/", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC)
    except OSError:
        _fail(tag + "_ROOT_OPEN")
    fds = [root_fd]
    links = []
    try:
        for index, name in enumerate(parts[:-1]):
            try:
                before = os.stat(name, dir_fd=fds[-1], follow_symlinks=False)
            except OSError:
                _fail(tag + "_ANCHOR_%02d_STAT" % index)
            if not stat.S_ISDIR(before.st_mode):
                _fail(tag + "_ANCHOR_%02d_TYPE" % index)
            try:
                child = os.open(
                    name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                    dir_fd=fds[-1],
                )
            except OSError:
                _fail(tag + "_ANCHOR_%02d_OPEN" % index)
            try:
                inside = os.fstat(child)
            except OSError:
                os.close(child)
                _fail(tag + "_ANCHOR_%02d_FSTAT" % index)
            if _stat_key(before) != _stat_key(inside):
                os.close(child)
                _fail(tag + "_ANCHOR_%02d_STABILITY" % index)
            prefix = b"/" + b"/".join(parts[:index + 1])
            expected_anchor = ACTIVE_DIRECTORY_ANCHORS.get(prefix.decode("ascii"))
            if (expected_anchor is not None and
                    _anchor_key(inside) != expected_anchor):
                os.close(child)
                _fail(tag + "_ANCHOR_%02d_HELD_MISMATCH" % index)
            links.append((name, before))
            fds.append(child)
    except Exception:
        _close_fds(fds)
        raise
    return (tuple(fds), tuple(links), parts[-1])


def _check_parent_chain(chain, tag):
    fds, links, _ = chain
    for index in range(len(links) - 1, -1, -1):
        name, before = links[index]
        try:
            entry = os.stat(name, dir_fd=fds[index], follow_symlinks=False)
            inside = os.fstat(fds[index + 1])
        except OSError:
            _fail(tag + "_ANCHOR_%02d_POST" % index)
        if (_anchor_key(entry) != _anchor_key(inside) or
                _anchor_key(inside) != _anchor_key(before)):
            _fail(tag + "_ANCHOR_%02d_REBIND" % index)


def _close_parent_chain_unchecked(chain):
    _close_fds(chain[0])


def _close_parent_chain(chain, tag):
    try:
        _check_parent_chain(chain, tag)
    finally:
        _close_parent_chain_unchecked(chain)


def _chain_parent_fd(chain):
    return chain[0][-1]


def _stat_chain_leaf(chain, tag):
    try:
        return os.stat(chain[2], dir_fd=_chain_parent_fd(chain), follow_symlinks=False)
    except OSError:
        _fail(tag + "_STATAT")


def _lstat(path, tag):
    chain = _open_parent_chain(path, tag)
    try:
        before = _stat_chain_leaf(chain, tag)
        after = _stat_chain_leaf(chain, tag)
        if _stat_key(before) != _stat_key(after):
            _fail(tag + "_LSTAT_STABILITY")
        return before
    finally:
        _close_parent_chain(chain, tag)


def _require_absent(path, tag):
    chain = _open_parent_chain(path, tag)
    try:
        try:
            os.stat(chain[2], dir_fd=_chain_parent_fd(chain), follow_symlinks=False)
        except FileNotFoundError:
            return
        except OSError:
            _fail(tag + "_PROBE")
        _fail(tag + "_PRESENT")
    finally:
        _close_parent_chain(chain, tag)


def _require_regular_stat(st, mode, nlink, size, tag):
    if not stat.S_ISREG(st.st_mode):
        _fail(tag + "_TYPE")
    if stat.S_IMODE(st.st_mode) != mode:
        _fail(tag + "_MODE")
    if st.st_nlink != nlink:
        _fail(tag + "_NLINK")
    if size is not None and st.st_size != size:
        _fail(tag + "_SIZE")


def _regular_anchor_slot(parent_fd, name, tag):
    try:
        parent = os.fstat(parent_fd)
    except OSError:
        _fail(tag + "_PARENT_FSTAT")
    raw_name = name if isinstance(name, bytes) else name.encode("ascii")
    return parent.st_dev, parent.st_ino, raw_name


def _enforce_regular_anchor(parent_fd, name, st, tag):
    expected = ACTIVE_REGULAR_ANCHORS.get(
        _regular_anchor_slot(parent_fd, name, tag),
    )
    if expected is not None and _stat_key(st) != expected:
        _fail(tag + "_HELD_MISMATCH")


def _register_regular_anchor(parent_fd, name, st, tag):
    slot = _regular_anchor_slot(parent_fd, name, tag)
    identity = _stat_key(st)
    previous = ACTIVE_REGULAR_ANCHORS.get(slot)
    if previous is not None and previous != identity:
        _fail(tag + "_ANCHOR_CONFLICT")
    ACTIVE_REGULAR_ANCHORS[slot] = identity


def _read_regular(path, tag, size=None, mode=0o600, nlink=1, digest=None,
                  limit=MAX_DYNAMIC_BYTES, return_stat=False):
    chain = _open_parent_chain(path, tag)
    parent_fd = _chain_parent_fd(chain)
    name = chain[2]
    fd = None
    try:
        before = _stat_chain_leaf(chain, tag)
        _require_regular_stat(before, mode, nlink, size, tag)
        _enforce_regular_anchor(parent_fd, name, before, tag)
        if before.st_size > limit:
            _fail(tag + "_LIMIT")
        try:
            fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC,
                         dir_fd=parent_fd)
        except OSError:
            _fail(tag + "_OPEN")
        try:
            first = os.fstat(fd)
            if _stat_key(first) != _stat_key(before):
                _fail(tag + "_PRE_STABILITY")
            # The frozen local-regular-file contract deliberately treats a
            # short positional read as a fail-closed I/O anomaly; it is not
            # retried under a potentially changed file version.
            data = os.pread(fd, before.st_size + 1, 0)
            last = os.fstat(fd)
        except OSError:
            _fail(tag + "_READ")
        after = _stat_chain_leaf(chain, tag)
        if _stat_key(first) != _stat_key(last) or _stat_key(last) != _stat_key(after):
            _fail(tag + "_POST_STABILITY")
        if len(data) != before.st_size:
            _fail(tag + "_READ_LENGTH")
        got = hashlib.sha256(data).hexdigest()
        if digest is not None and got != digest:
            _fail(tag + "_HASH")
        result = (data, before.st_size, data.count(b"\n"), got)
        return result + (_stat_key(last),) if return_stat else result
    finally:
        if fd is not None:
            try:
                os.close(fd)
            except OSError:
                pass
        _close_parent_chain(chain, tag)


def _strict_text(data, lf, tag):
    if (data.startswith(b"\xef\xbb\xbf") or
            any(value < 0x20 and value not in (0x09, 0x0a) for value in data)):
        _fail(tag + "_ENCODING")
    if not data.endswith(b"\n") or data.endswith(b"\n\n"):
        _fail(tag + "_TERMINAL_LF")
    if data.count(b"\n") != lf:
        _fail(tag + "_LF")
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError:
        _fail(tag + "_UTF8")
    if ("\ufeff" in text or "\u0085" in text or "\u2028" in text or
            "\u2029" in text or
            any(0x7f <= ord(value) <= 0x9f for value in text)):
        _fail(tag + "_ENCODING")
    return text


def _line_byte_preflight(data, byte_limit, line_limit, line_byte_limit,
                         terminal_lf, tag):
    if len(data) > byte_limit:
        _fail(tag + "_BYTE_LIMIT")
    lf = data.count(b"\n")
    if lf > line_limit:
        _fail(tag + "_LINE_LIMIT")
    if terminal_lf and (lf == 0 or not data.endswith(b"\n")):
        _fail(tag + "_TERMINAL_LF")
    start = 0
    for _ in range(lf):
        end = data.find(b"\n", start)
        if end < start or end - start > line_byte_limit:
            _fail(tag + "_LINE_BYTES")
        start = end + 1
    if len(data) - start > line_byte_limit:
        _fail(tag + "_LINE_BYTES")
    return lf


def _lf_lines(text, expected_lf, tag):
    if (expected_lf <= 0 or not text.endswith("\n") or
            text.count("\n") != expected_lf):
        _fail(tag + "_LF_LINES")
    lines = text[:-1].split("\n")
    if len(lines) != expected_lf:
        _fail(tag + "_LF_LINES")
    return lines


def _read_bound_text(path, identity, tag, return_stat=False):
    size, lf, mode, nlink, digest = identity
    result = _read_regular(
        path, tag, size, mode, nlink, digest, size, return_stat=return_stat,
    )
    data = result[0]
    _strict_text(data, lf, tag)
    return (data, result[4]) if return_stat else data


def _check_symlink(path, expected, tag):
    size, mode, nlink, raw_target, canonical = expected
    chain = _open_parent_chain(path, tag)
    try:
        before = _stat_chain_leaf(chain, tag)
        if not stat.S_ISLNK(before.st_mode):
            _fail(tag + "_TYPE")
        if (before.st_size != size or stat.S_IMODE(before.st_mode) != mode or
                before.st_nlink != nlink):
            _fail(tag + "_IDENTITY")
        try:
            got = os.readlink(chain[2], dir_fd=_chain_parent_fd(chain))
        except OSError:
            _fail(tag + "_READLINK")
        after = _stat_chain_leaf(chain, tag)
        if _stat_key(before) != _stat_key(after):
            _fail(tag + "_STABILITY")
        if got != raw_target:
            _fail(tag + "_TARGET")
        if _canonical_hop(path, got, tag, path in DEPENDENCY_SYMLINKS) != canonical:
            _fail(tag + "_CANONICAL")
        return _stat_key(before), got
    finally:
        _close_parent_chain(chain, tag)


def _canonical_hop(logical, raw_target, tag, restrict_dependency_root):
    if b"\x00" in raw_target or b"\r" in raw_target or b"\n" in raw_target or b"\t" in raw_target:
        _fail(tag + "_TARGET_BYTES")
    try:
        target = raw_target.decode("utf-8", "strict")
    except UnicodeDecodeError:
        _fail(tag + "_TARGET_UTF8")
    if target == "":
        _fail(tag + "_TARGET_EMPTY")
    components = [] if target.startswith("/") else logical.rsplit("/", 1)[0].split("/")[1:]
    for part in target.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if not components:
                _fail(tag + "_UNDERFLOW")
            components.pop()
        else:
            components.append(part)
    result = "/" + "/".join(components)
    if restrict_dependency_root:
        roots = ("/etc/texmf/", "/usr/share/texlive/texmf-dist/", "/usr/share/texmf/", "/var/lib/texmf/")
        if sum(result.startswith(root) for root in roots) != 1:
            _fail(tag + "_ROOT")
    return result


def _open_exact_dir(path, tag, mode=0o700, nlink=None):
    chain = _open_parent_chain(path, tag)
    fd = None
    try:
        before = _stat_chain_leaf(chain, tag)
        if not stat.S_ISDIR(before.st_mode) or stat.S_IMODE(before.st_mode) != mode:
            _fail(tag + "_DIR")
        if nlink is not None and before.st_nlink != nlink:
            _fail(tag + "_NLINK")
        try:
            fd = os.open(
                chain[2], os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                dir_fd=_chain_parent_fd(chain),
            )
        except OSError:
            _fail(tag + "_OPEN")
        try:
            inside = os.fstat(fd)
        except OSError:
            _fail(tag + "_FSTAT")
        if _stat_key(before) != _stat_key(inside):
            _fail(tag + "_STABILITY")
        expected_anchor = ACTIVE_DIRECTORY_ANCHORS.get(path)
        if (expected_anchor is not None and
                _anchor_key(inside) != expected_anchor):
            _fail(tag + "_HELD_MISMATCH")
        return fd, before, chain
    except Exception:
        if fd is not None:
            try:
                os.close(fd)
            except OSError:
                pass
        try:
            _close_parent_chain(chain, tag)
        except CheckFail:
            pass
        raise


def _raw_name(name, tag):
    if not isinstance(name, str):
        _fail(tag + "_NAME_TYPE")
    try:
        return name.encode("utf-8", "surrogateescape")
    except UnicodeEncodeError:
        _fail(tag + "_NAME_ENCODING")


def _list_fd_exact(fd, expected, tag):
    wanted = frozenset(name.encode("ascii") for name in expected)
    seen = set()
    try:
        if os.lseek(fd, 0, os.SEEK_SET) != 0:
            _fail(tag + "_REWIND")
        with os.scandir(fd) as entries:
            for entry in entries:
                name = _raw_name(entry.name, tag)
                if len(name) > 255 or name not in wanted:
                    _fail(tag + "_UNKNOWN")
                if name in seen:
                    _fail(tag + "_DUPLICATE")
                seen.add(name)
    except OSError:
        _fail(tag + "_LIST")
    missing = tuple(sorted(wanted.difference(seen)))
    if missing:
        _fail(tag + "_MISSING_" + missing[0].hex())
    if seen != wanted:
        _fail(tag + "_SET")


def _close_exact_dir(fd, before, path, tag, chain, content_stable=True):
    failure = None
    try:
        inside = os.fstat(fd)
    except OSError:
        inside = None
        failure = tag + "_FSTAT_POST"
    try:
        after = _stat_chain_leaf(chain, tag)
    except CheckFail:
        after = None
        if failure is None:
            failure = tag + "_STAT_POST"
    finally:
        try:
            os.close(fd)
        except OSError:
            pass
    if failure is None:
        key = _stat_key if content_stable else _anchor_key
        if key(before) != key(inside) or key(inside) != key(after):
            failure = tag + "_POST_STABILITY"
    try:
        _close_parent_chain(chain, tag)
    except CheckFail:
        if failure is None:
            failure = tag + "_ANCHOR_POST"
    if failure is not None:
        _fail(failure)


def _list_exact_directory(path, expected, tag, mode=0o700, nlink=None):
    fd, before, chain = _open_exact_dir(path, tag, mode, nlink)
    try:
        _list_fd_exact(fd, expected, tag)
    finally:
        _close_exact_dir(fd, before, path, tag, chain)


def _check_inflight_directory(path, completed_names, ident, tag, nlink=2):
    inflight = (ident + ".stdout", ident + ".stderr")
    expected = tuple(sorted(tuple(completed_names) + inflight))
    fd, before, chain = _open_exact_dir(path, tag, 0o700, nlink)
    try:
        _list_fd_exact(fd, expected, tag)
        for index, name in enumerate(inflight):
            data, _, _ = _read_regular_at(
                fd, name, tag + "_CURRENT_%d" % index, 0o600, 1, 0,
            )
            if data != b"":
                _fail(tag + "_CURRENT_NONEMPTY_%d" % index)
    finally:
        _close_exact_dir(fd, before, path, tag, chain)


def _stat_at(fd, name, tag):
    try:
        return os.stat(name.encode("ascii"), dir_fd=fd, follow_symlinks=False)
    except OSError:
        _fail(tag + "_STATAT")


def _read_regular_at(fd, name, tag, mode=0o600, nlink=1, limit=MAX_DYNAMIC_BYTES):
    name_b = name.encode("ascii")
    before = _stat_at(fd, name, tag)
    _require_regular_stat(before, mode, nlink, None, tag)
    _enforce_regular_anchor(fd, name, before, tag)
    if before.st_size > limit:
        _fail(tag + "_LIMIT")
    try:
        child = os.open(name_b, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=fd)
    except OSError:
        _fail(tag + "_OPENAT")
    try:
        first = os.fstat(child)
        if _stat_key(first) != _stat_key(before):
            _fail(tag + "_PRE_STABILITY")
        # Same fail-closed local-regular-file premise as `_read_regular`.
        data = os.pread(child, before.st_size + 1, 0)
        last = os.fstat(child)
    except OSError:
        _fail(tag + "_READAT")
    finally:
        try:
            os.close(child)
        except OSError:
            pass
    after = _stat_at(fd, name, tag)
    if _stat_key(first) != _stat_key(last) or _stat_key(last) != _stat_key(after):
        _fail(tag + "_POST_STABILITY")
    if len(data) != before.st_size:
        _fail(tag + "_READ_LENGTH")
    return data, before, hashlib.sha256(data).hexdigest()


def _pread_identity(fd, size, limit, tag):
    if size < 0 or size > limit:
        _fail(tag + "_LIMIT")
    position = 0
    hasher = hashlib.sha256()
    lf = 0
    try:
        while position < size:
            block = os.pread(fd, min(CHUNK, size - position), position)
            if not block:
                _fail(tag + "_SHORT")
            position += len(block)
            hasher.update(block)
            lf += block.count(b"\n")
        if os.pread(fd, 1, position):
            _fail(tag + "_LONG")
    except OSError:
        _fail(tag + "_PREAD")
    return hasher.hexdigest(), lf


def _pread_digest(fd, size, limit, tag):
    return _pread_identity(fd, size, limit, tag)[0]


def _hold_regular_at(parent_fd, name, tag, mode, limit):
    before = _stat_at(parent_fd, name, tag)
    _require_regular_stat(before, mode, 1, None, tag)
    _enforce_regular_anchor(parent_fd, name, before, tag)
    if before.st_size > limit:
        _fail(tag + "_LIMIT")
    child = None
    try:
        child = os.open(
            name.encode("ascii"), os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC,
            dir_fd=parent_fd,
        )
        first = os.fstat(child)
        if _stat_key(first) != _stat_key(before):
            _fail(tag + "_PRE_STABILITY")
        digest, lf = _pread_identity(child, before.st_size, limit, tag)
        last = os.fstat(child)
        after = _stat_at(parent_fd, name, tag)
        if (_stat_key(first) != _stat_key(last) or
                _stat_key(last) != _stat_key(after)):
            _fail(tag + "_POST_STABILITY")
        _register_regular_anchor(parent_fd, name, last, tag)
        return {
            "name": name, "fd": child, "stat": _stat_key(last),
            "size": before.st_size, "digest": digest, "mode": mode,
            "limit": limit, "lf": lf,
        }
    except Exception:
        if child is not None:
            try:
                os.close(child)
            except OSError:
                pass
        raise


def _check_held_regular_at(parent_fd, record, tag):
    name = record["name"]
    fd = record["fd"]
    try:
        first = os.fstat(fd)
        path_first = _stat_at(parent_fd, name, tag + "_PATH_PRE")
        digest = _pread_digest(fd, record["size"], record["limit"], tag)
        last = os.fstat(fd)
        path_last = _stat_at(parent_fd, name, tag + "_PATH_POST")
    except OSError:
        _fail(tag + "_FD")
    if (record["stat"] != _stat_key(first) or
            _stat_key(first) != _stat_key(path_first) or
            _stat_key(path_first) != _stat_key(last) or
            _stat_key(last) != _stat_key(path_last) or
            digest != record["digest"]):
        _fail(tag + "_VERSION")


def _register_directory_anchor(path, st, tag):
    anchor = _anchor_key(st)
    previous = ACTIVE_DIRECTORY_ANCHORS.get(path)
    if previous is not None and previous != anchor:
        _fail(tag + "_ANCHOR_CONFLICT")
    ACTIVE_DIRECTORY_ANCHORS[path] = anchor


def _register_chain_directories(path, chain, tag):
    parts = _path_parts(path)
    fds = chain[0]
    for index in range(len(parts) - 1):
        try:
            st = os.fstat(fds[index + 1])
        except OSError:
            _fail(tag + "_CHAIN_FSTAT_%02d" % index)
        prefix = "/" + b"/".join(parts[:index + 1]).decode("ascii")
        _register_directory_anchor(prefix, st, tag + "_CHAIN_%02d" % index)


def _open_held_absolute(path, tag, mode, limit, size=None, digest=None):
    chain = _open_parent_chain(path, tag)
    record = None
    try:
        _register_chain_directories(path, chain, tag)
        record = _hold_regular_at(
            _chain_parent_fd(chain), chain[2].decode("ascii"), tag,
            mode, limit,
        )
        if ((size is not None and record["size"] != size) or
                (digest is not None and record["digest"] != digest)):
            _fail(tag + "_IDENTITY")
        return {"path": path, "chain": chain, "record": record}
    except Exception:
        if record is not None:
            try:
                os.close(record["fd"])
            except OSError:
                pass
        try:
            _close_parent_chain(chain, tag)
        except CheckFail:
            pass
        raise


def _check_held_absolute(held, tag):
    _check_held_regular_at(
        _chain_parent_fd(held["chain"]), held["record"], tag,
    )
    _check_parent_chain(held["chain"], tag)


def _close_held_absolute(held):
    try:
        os.close(held["record"]["fd"])
    except OSError:
        pass
    _close_parent_chain_unchecked(held["chain"])


def _check_close_held_absolute(held, tag, suppress=False):
    failure = None
    try:
        _check_held_absolute(held, tag)
    except CheckFail as exc:
        failure = exc
    _close_held_absolute(held)
    if failure is not None and not suppress:
        raise failure


def _regular_identity(path, tag, mode=0o600, limit=MAX_DYNAMIC_BYTES):
    held = _open_held_absolute(path, tag, mode, limit)
    try:
        record = held["record"]
        result = (record["size"], record["lf"], record["digest"])
        _check_held_absolute(held, tag + "_TERMINAL")
        return result
    finally:
        _close_held_absolute(held)


def _regular_identity_at(parent_fd, name, tag, mode=0o600, limit=MAX_DYNAMIC_BYTES):
    record = _hold_regular_at(parent_fd, name, tag, mode, limit)
    try:
        _check_held_regular_at(parent_fd, record, tag + "_TERMINAL")
        return record["size"], record["lf"], record["stat"], record["digest"]
    finally:
        try:
            os.close(record["fd"])
        except OSError:
            pass


def _compare_held_payloads(left, right, tag):
    if left["size"] != right["size"]:
        _fail(tag + "_SIZE")
    position = 0
    lf = 0
    try:
        while position < left["size"]:
            width = min(CHUNK, left["size"] - position)
            left_block = os.pread(left["fd"], width, position)
            right_block = os.pread(right["fd"], width, position)
            if (not left_block or len(left_block) != width or
                    left_block != right_block):
                _fail(tag + "_BYTES")
            lf += left_block.count(b"\n")
            position += width
        if os.pread(left["fd"], 1, position) or os.pread(right["fd"], 1, position):
            _fail(tag + "_LONG")
    except OSError:
        _fail(tag + "_READ")
    return lf


def _open_held_group(rows, tag):
    held = []
    try:
        for index, row in enumerate(rows):
            held.append(_open_held_absolute(
                row[0], tag + "_%02d" % index, row[1], row[2],
                size=row[3], digest=row[4],
            ))
        return held
    except Exception:
        for index, item in reversed(tuple(enumerate(held))):
            _check_close_held_absolute(
                item, tag + "_CLEAN_%02d" % index, suppress=True,
            )
        raise


def _check_held_group(held, tag):
    failure = None
    for index, item in enumerate(held):
        try:
            _check_held_absolute(item, tag + "_%02d" % index)
        except CheckFail as exc:
            if failure is None:
                failure = exc
    if failure is not None:
        raise failure


def _close_held_group(held):
    for item in reversed(held):
        _close_held_absolute(item)


def _check_close_held_group(held, tag, suppress=False):
    failure = None
    try:
        _check_held_group(held, tag)
    except CheckFail as exc:
        failure = exc
    _close_held_group(held)
    if failure is not None and not suppress:
        raise failure


def _open_held_absence(path, tag):
    chain = _open_parent_chain(path, tag)
    try:
        _register_chain_directories(path, chain, tag)
        try:
            os.stat(chain[2], dir_fd=_chain_parent_fd(chain), follow_symlinks=False)
        except FileNotFoundError:
            pass
        except OSError:
            _fail(tag + "_PROBE")
        else:
            _fail(tag + "_PRESENT")
        return {"path": path, "chain": chain}
    except Exception:
        try:
            _close_parent_chain(chain, tag)
        except CheckFail:
            pass
        raise


def _check_held_absence(held, tag):
    try:
        os.stat(
            held["chain"][2], dir_fd=_chain_parent_fd(held["chain"]),
            follow_symlinks=False,
        )
    except FileNotFoundError:
        pass
    except OSError:
        _fail(tag + "_PROBE")
    else:
        _fail(tag + "_PRESENT")
    _check_parent_chain(held["chain"], tag)


def _close_held_absence(held):
    _close_parent_chain_unchecked(held["chain"])


def _check_close_held_absence(held, tag, suppress=False):
    failure = None
    try:
        _check_held_absence(held, tag)
    except CheckFail as exc:
        failure = exc
    _close_held_absence(held)
    if failure is not None and not suppress:
        raise failure


def _stage_file_cap(name):
    if name.endswith(".status"):
        return 2
    if name.endswith(".stderr"):
        return 0
    if name in MANIFEST_BASENAMES:
        return 256 * KIB
    snapshot_caps = {
        "--main.log.snapshot": 8 * MIB,
        "--main.aux.snapshot": 4 * MIB,
        "--main.fls.snapshot": 8 * MIB,
        "--main.bbl.snapshot": 2 * MIB,
        "--main.blg.snapshot": 512 * KIB,
    }
    for suffix, limit in snapshot_caps.items():
        if name.endswith(suffix):
            return limit
    if name.endswith(".stdout"):
        ident = name[:-7]
        if ident in ROOT_INIT_IDS or ident in CROSS_COMPARE_IDS or ident in EVIDENCE_ROOT_IDS:
            return 0
        if ident in PUBLICATION_IDS:
            return 4 * MIB
        if ident == "R060":
            return 64 * KIB
        if ident == "R062":
            return 8 * MIB
        if (ident in ROOT_VALIDATOR_MODES or ident in ("X009", "X010")):
            return MIB
    _fail("STAGE_CAP_UNKNOWN_" + name.encode("ascii").hex())


def _root_file_cap(name):
    limits = {
        "main.tex": 256 * KIB,
        "math_commands.tex": 64 * KIB,
        "references.bib": 256 * KIB,
        "main.log": 8 * MIB,
        "main.aux": 4 * MIB,
        "main.fls": 8 * MIB,
        "main.pdf": 64 * MIB,
        "main.bbl": 2 * MIB,
        "main.blg": 512 * KIB,
    }
    if name not in limits:
        _fail("ROOT_CAP_UNKNOWN_" + name.encode("ascii").hex())
    return limits[name]


def _evidence_file_cap(name):
    return MIB if name == "BUILD_VALIDATOR_POSTFAIL.py" else _stage_file_cap(name)


def _root_file_mode(name):
    return 0o644 if name in SOURCE_BASENAME_IDENTITIES else 0o600


def _stage_file_mode(name):
    return 0o600


def _evidence_file_mode(name):
    return 0o500 if name == "BUILD_VALIDATOR_POSTFAIL.py" else 0o600


def _open_held_universe(path, expected_names, child_directories, mutable_names,
                        cap_function, mode_function, total_limit, tag, nlink):
    fd, before, chain = _open_exact_dir(path, tag, 0o700, nlink)
    regulars = []
    children = []
    mutable = frozenset(mutable_names)
    try:
        _register_directory_anchor(path, before, tag)
        _list_fd_exact(fd, expected_names, tag)
        total = 0
        regular_rows = []
        for index, name in enumerate(sorted(expected_names)):
            child_tag = tag + "_PREFLIGHT_%03d" % index
            st = _stat_at(fd, name, child_tag)
            if name in child_directories:
                if (not stat.S_ISDIR(st.st_mode) or stat.S_IMODE(st.st_mode) != 0o700 or
                        st.st_nlink != 2):
                    _fail(child_tag + "_DIRECTORY")
                continue
            limit = cap_function(name)
            mode = mode_function(name)
            _require_regular_stat(st, mode, 1, None, child_tag)
            if st.st_size > limit:
                _fail(child_tag + "_LIMIT")
            if name in mutable and st.st_size != 0:
                _fail(child_tag + "_MUTABLE_NONEMPTY")
            total += st.st_size
            if total > total_limit:
                _fail(tag + "_AGGREGATE_LIMIT")
            regular_rows.append((name, mode, limit))
        for index, name in enumerate(sorted(child_directories)):
            child_tag = tag + "_CHILD_%02d" % index
            child_before = _stat_at(fd, name, child_tag)
            child_fd = None
            try:
                child_fd = os.open(
                    name.encode("ascii"),
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                    dir_fd=fd,
                )
                child_inside = os.fstat(child_fd)
            except OSError:
                if child_fd is not None:
                    try:
                        os.close(child_fd)
                    except OSError:
                        pass
                _fail(child_tag + "_OPEN")
            if _stat_key(child_before) != _stat_key(child_inside):
                os.close(child_fd)
                _fail(child_tag + "_STABILITY")
            expected_child_names = child_directories[name]
            children.append({
                "name": name, "fd": child_fd, "stat": _stat_key(child_inside),
                "expected": expected_child_names,
            })
            if expected_child_names is not None:
                _list_fd_exact(child_fd, expected_child_names, child_tag)
            _register_directory_anchor(path + "/" + name, child_inside, child_tag)
        for index, (name, mode, limit) in enumerate(regular_rows):
            if name not in mutable:
                regulars.append(_hold_regular_at(
                    fd, name, tag + "_REGULAR_%03d" % index, mode, limit,
                ))
        return {
            "path": path, "fd": fd, "before": before, "chain": chain,
            "expected": tuple(expected_names), "mutable": mutable,
            "regulars": regulars, "children": children,
            "mode_function": mode_function,
        }
    except Exception:
        for record in reversed(regulars):
            try:
                os.close(record["fd"])
            except OSError:
                pass
        for child in reversed(children):
            try:
                os.close(child["fd"])
            except OSError:
                pass
        try:
            _close_exact_dir(fd, before, path, tag, chain, content_stable=False)
        except CheckFail:
            pass
        raise


def _check_held_universe(universe, tag):
    fd = universe["fd"]
    try:
        _list_fd_exact(fd, universe["expected"], tag + "_NAMES_PRE")
        for index, record in enumerate(universe["regulars"]):
            _check_held_regular_at(
                fd, record, tag + "_REGULAR_%03d" % index,
            )
        for index, child in enumerate(universe["children"]):
            child_tag = tag + "_CHILD_%02d" % index
            if child["expected"] is not None:
                _list_fd_exact(child["fd"], child["expected"], child_tag)
            inside = os.fstat(child["fd"])
            path_st = _stat_at(fd, child["name"], child_tag)
            if (child["stat"] != _stat_key(inside) or
                    _stat_key(inside) != _stat_key(path_st)):
                _fail(child_tag + "_VERSION")
        _list_fd_exact(fd, universe["expected"], tag + "_NAMES_POST")
    except (CheckFail, OSError) as exc:
        if isinstance(exc, CheckFail):
            raise
        _fail(tag + "_CHECK")
    try:
        inside = os.fstat(fd)
        after = _stat_chain_leaf(universe["chain"], tag)
    except OSError:
        _fail(tag + "_ROOT_FSTAT")
    if (_stat_key(universe["before"]) != _stat_key(inside) or
            _stat_key(inside) != _stat_key(after)):
        _fail(tag + "_ROOT_VERSION")
    _check_parent_chain(universe["chain"], tag)


def _close_held_universe(universe):
    for record in reversed(universe["regulars"]):
        try:
            os.close(record["fd"])
        except OSError:
            pass
    for child in reversed(universe["children"]):
        try:
            os.close(child["fd"])
        except OSError:
            pass
    try:
        os.close(universe["fd"])
    except OSError:
        pass
    _close_parent_chain_unchecked(universe["chain"])


def _check_close_held_universe(universe, tag, suppress=False):
    failure = None
    try:
        _check_held_universe(universe, tag)
    except CheckFail as exc:
        failure = exc
    _close_held_universe(universe)
    if failure is not None and not suppress:
        raise failure


def _open_empty_child(parent_fd, name, tag):
    before = _stat_at(parent_fd, name, tag)
    if not stat.S_ISDIR(before.st_mode) or stat.S_IMODE(before.st_mode) != 0o700 or before.st_nlink != 2:
        _fail(tag + "_DIR")
    try:
        fd = os.open(name.encode("ascii"), os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent_fd)
    except OSError:
        _fail(tag + "_OPENAT")
    try:
        if _stat_key(os.fstat(fd)) != _stat_key(before):
            _fail(tag + "_PRE_STABILITY")
        _list_fd_exact(fd, (), tag)
    except CheckFail:
        try:
            os.close(fd)
        except OSError:
            pass
        raise
    except OSError:
        try:
            os.close(fd)
        except OSError:
            pass
        _fail(tag + "_FSTAT")
    return fd, before


def _close_empty_child(parent_fd, name, fd, before, tag):
    failure = None
    try:
        _list_fd_exact(fd, (), tag + "_FINAL")
        inside = os.fstat(fd)
    except (OSError, CheckFail):
        inside = None
        failure = tag + "_FINAL_CHECK"
    try:
        after = _stat_at(parent_fd, name, tag)
    except CheckFail:
        after = None
        if failure is None:
            failure = tag + "_FINAL_STAT"
    try:
        os.close(fd)
    except OSError:
        if failure is None:
            failure = tag + "_CLOSE"
    if failure is None:
        if (before.st_nlink != 2 or inside.st_nlink != 2 or after.st_nlink != 2 or
                _stat_key(before) != _stat_key(inside) or
                _stat_key(inside) != _stat_key(after)):
            failure = tag + "_POST_STABILITY"
    if failure is not None:
        _fail(failure)


def _exclusive_write(path, data, tag):
    stage = None
    basename = None
    for candidate in (STAGE0, STAGE1):
        prefix = candidate + "/"
        if path.startswith(prefix) and "/" not in path[len(prefix):]:
            stage = candidate
            basename = path[len(prefix):]
            break
    if stage is None or basename is None or basename == "":
        _usage("WRITE_DESTINATION")
    stage_fd, stage_before, stage_chain = _open_exact_dir(stage, tag + "_PARENT", 0o700, 2)
    name_b = basename.encode("ascii")
    fd = None
    try:
        try:
            os.stat(name_b, dir_fd=stage_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        except OSError:
            _fail(tag + "_PRECHECK")
        else:
            _fail(tag + "_EXISTS")
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC
        try:
            fd = os.open(name_b, flags, 0o600, dir_fd=stage_fd)
        except OSError:
            _fail(tag + "_CREATE")
        offset = 0
        try:
            first = os.fstat(fd)
            _require_regular_stat(first, 0o600, 1, 0, tag)
            while offset < len(data):
                written = os.write(fd, data[offset:offset + CHUNK])
                if written <= 0:
                    _fail(tag + "_WRITE")
                offset += written
            os.fsync(fd)
            last = os.fstat(fd)
        except OSError:
            _fail(tag + "_WRITE")
        finally:
            try:
                os.close(fd)
            except OSError:
                pass
            fd = None
        after = _stat_at(stage_fd, basename, tag)
        _require_regular_stat(after, 0o600, 1, len(data), tag)
        if _stat_key(last) != _stat_key(after):
            _fail(tag + "_POST_STABILITY")
        _register_regular_anchor(
            stage_fd, basename, after, tag + "_CREATED_ANCHOR",
        )
        reread, reread_stat, digest = _read_regular_at(
            stage_fd, basename, tag + "_VERIFY", 0o600, 1, max(len(data), 1),
        )
        size = len(reread)
        lf = reread.count(b"\n")
        if _stat_key(reread_stat) != _stat_key(after):
            _fail(tag + "_REREAD_STABILITY")
        if digest != hashlib.sha256(data).hexdigest():
            _fail(tag + "_REREAD_HASH")
        if reread != data:
            _fail(tag + "_COMPARE")
        return size, lf, digest
    finally:
        if fd is not None:
            try:
                os.close(fd)
            except OSError:
                pass
        _close_exact_dir(
            stage_fd, stage_before, stage, tag + "_PARENT", stage_chain,
            content_stable=False,
        )


def _same_regular(left, right, tag, left_mode=0o600, right_mode=0o600,
                  limit=MAX_DYNAMIC_BYTES):
    left_held = None
    right_held = None
    try:
        left_held = _open_held_absolute(left, tag + "_L", left_mode, limit)
        right_held = _open_held_absolute(right, tag + "_R", right_mode, limit)
        left_record = left_held["record"]
        right_record = right_held["record"]
        if (left_record["size"] != right_record["size"] or
                left_record["digest"] != right_record["digest"]):
            _fail(tag + "_IDENTITY")
        lf = _compare_held_payloads(
            left_record, right_record, tag + "_INITIAL",
        )
        if lf != left_record["lf"] or lf != right_record["lf"]:
            _fail(tag + "_LF")
        _check_held_absolute(left_held, tag + "_L_REBIND")
        _check_held_absolute(right_held, tag + "_R_REBIND")
        if _compare_held_payloads(
                left_record, right_record, tag + "_TERMINAL") != lf:
            _fail(tag + "_TERMINAL_LF")
        _check_held_absolute(left_held, tag + "_L_TERMINAL")
        _check_held_absolute(right_held, tag + "_R_TERMINAL")
        return left_record["size"], lf, left_record["digest"]
    finally:
        if right_held is not None:
            _close_held_absolute(right_held)
        if left_held is not None:
            _close_held_absolute(left_held)


def _verify_controls_and_sources():
    vectors = []
    for index, path in enumerate(sorted(CONTROL_IDENTITIES)):
        _, stat_key = _read_bound_text(
            path, CONTROL_IDENTITIES[path], "CONTROL_%02d" % index,
            return_stat=True,
        )
        vectors.append((path, stat_key))
    for index, path in enumerate(sorted(SOURCE_IDENTITIES)):
        _, stat_key = _read_bound_text(
            path, SOURCE_IDENTITIES[path], "SOURCE_%02d" % index,
            return_stat=True,
        )
        vectors.append((path, stat_key))
    return tuple(vectors)


def _verify_tools():
    for index, path in enumerate(sorted(SYMLINK_TOOLS)):
        _check_symlink(path, SYMLINK_TOOLS[path], "TOOL_LINK_%02d" % index)
    for index, path in enumerate(sorted(REGULAR_TOOLS)):
        size, mode, nlink, digest = REGULAR_TOOLS[path]
        if nlink != 1:
            _fail("TOOL_REG_%02d_NLINK_CONTRACT" % index)
        got_size, _, got_digest = _regular_identity(
            path, "TOOL_REG_%02d" % index, mode, max(size, 1),
        )
        if got_size != size or got_digest != digest:
            _fail("TOOL_REG_%02d_IDENTITY" % index)


def _verify_dependencies():
    framing = DEPENDENCY_ROWS_TEXT.encode("utf-8")
    if (len(DEPENDENCY_ROWS) != 87 or len(framing) != 23408 or framing.count(b"\n") != 87 or
            hashlib.sha256(framing).hexdigest() != "2855b5fe4a859552fc581eb3c06b11c68008b8eb67351d37f2a44c57a91adf87"):
        _fail("DEPENDENCY_CONSTANT_FRAME")
    if tuple(row[0] for row in DEPENDENCY_ROWS) != tuple(sorted(row[0] for row in DEPENDENCY_ROWS)):
        _fail("DEPENDENCY_CONSTANT_ORDER")
    finals = {}
    for index, row in enumerate(DEPENDENCY_ROWS):
        logical, chain, target, size, mode, nlink, digest = row
        tag = "DEPENDENCY_CHAIN_%02d" % index
        if logical in DEPENDENCY_SYMLINKS:
            expected = DEPENDENCY_SYMLINKS[logical]
            _check_symlink(logical, expected, tag)
            if chain != logical + "=>" + expected[4] or target != expected[4]:
                _fail(tag + "_ROW")
        else:
            st = _lstat(logical, tag)
            _require_regular_stat(st, mode, nlink, size, tag)
            if chain != logical or target != logical:
                _fail(tag + "_ROW")
        identity = (size, mode, nlink, digest)
        if target in finals and finals[target] != identity:
            _fail(tag + "_SHARED_CONFLICT")
        finals[target] = identity
    if len(finals) != 86:
        _fail("DEPENDENCY_FINAL_CENSUS")
    for index, path in enumerate(sorted(finals)):
        size, mode, nlink, digest = finals[path]
        if nlink != 1:
            _fail("DEPENDENCY_FINAL_%02d_NLINK_CONTRACT" % index)
        got_size, _, got_digest = _regular_identity(
            path, "DEPENDENCY_FINAL_%02d" % index, mode, max(size, 1),
        )
        if got_size != size or got_digest != digest:
            _fail("DEPENDENCY_FINAL_%02d_IDENTITY" % index)
    return len(DEPENDENCY_ROWS), len(finals)


def _verify_root_source_copies(root):
    if root not in ROOT_CONFIG:
        _usage("ROOT")
    sources = (SOURCE_MAIN, SOURCE_COMMANDS, SOURCE_BIB)
    copies = ROOT_SOURCE_PATHS[root]
    for index, (source, copy) in enumerate(zip(sources, copies)):
        identity = SOURCE_IDENTITIES[source]
        expected = (identity[0], identity[1], 0o644, 1, identity[4])
        source_data = _read_bound_text(source, identity, "LIVE_SOURCE_%02d" % index)
        copy_data = _read_bound_text(copy, expected, "ROOT_SOURCE_%02d" % index)
        if source_data != copy_data:
            _fail("ROOT_SOURCE_COPY_%02d" % index)


def _nofile_vector(tag):
    try:
        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    except (OSError, ValueError):
        _fail(tag + "_READ")
    if (soft == resource.RLIM_INFINITY or
            not MIN_NOFILE <= soft <= MAX_NOFILE):
        _fail(tag + "_SOFT")
    return soft, hard


def _verify_launch_fd_contract(guard):
    vector = _nofile_vector("RUNTIME_NOFILE")
    allowed = {0, 1, 2, guard["stage_fd"], *guard["read_fds"],
               *guard["stage_chain"][0]}
    scan_fd = None
    try:
        try:
            scan_fd = os.open(
                b"/proc/self/fd",
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
            )
        except OSError:
            _fail("RUNTIME_FD_DIRECTORY")
        allowed.add(scan_fd)
        scans = []
        for pass_index in range(2):
            try:
                if os.lseek(scan_fd, 0, os.SEEK_SET) != 0:
                    _fail("RUNTIME_FD_REWIND_%d" % pass_index)
                names = os.listdir(scan_fd)
            except OSError:
                _fail("RUNTIME_FD_LIST_%d" % pass_index)
            live = set()
            for name in names:
                if (not isinstance(name, str) or len(name) > 10 or
                        re.fullmatch(r"0|[1-9][0-9]*", name) is None):
                    _fail("RUNTIME_FD_NAME")
                fd = _bounded_decimal(
                    name, "RUNTIME_FD_NUMBER", 2_147_483_647,
                )
                try:
                    os.fstat(fd)
                except OSError:
                    continue
                live.add(fd)
                if fd not in allowed:
                    _fail("RUNTIME_INHERITED_FD")
            if live != allowed:
                _fail("RUNTIME_FD_LIVE_SET_%d" % pass_index)
            scans.append(frozenset(live))
        if len(scans) != 2 or scans[0] != scans[1]:
            _fail("RUNTIME_FD_SCAN_STABILITY")
    finally:
        if scan_fd is not None:
            try:
                os.close(scan_fd)
            except OSError:
                _fail("RUNTIME_FD_DIRECTORY_CLOSE")
    return vector


def _verify_runtime_contract(argv):
    if dict(os.environb) != EXACT_VALIDATOR_ENV:
        _fail("RUNTIME_ENV")
    if (argv is not sys.argv or __name__ != "__main__" or __spec__ is not None or
            __package__ is not None):
        _fail("RUNTIME_DISPATCH")
    if (sys.version_info[:2] != (3, 12) or not sys.dont_write_bytecode or
            sys.flags.no_site != 1 or sys.flags.no_user_site != 1 or
            sys.flags.safe_path != 1 or sys.flags.utf8_mode != 1 or
            sys.flags.hash_randomization != 0):
        _fail("RUNTIME_FLAGS")
    interpreter = "/root/miniconda3/bin/python3"
    if (sys.executable != interpreter or __file__ != VALIDATOR_COPY or
            tuple(sys.orig_argv) != (
                interpreter, "-S", "-B", "-P", VALIDATOR_COPY, *tuple(argv[1:]),
            )):
        _fail("RUNTIME_LAUNCH")
    link_vector = _check_symlink(
        interpreter, SYMLINK_TOOLS[interpreter], "RUNTIME_INTERPRETER_LINK",
    )
    size, mode, nlink, digest = REGULAR_TOOLS["/root/miniconda3/bin/python3.12"]
    if nlink != 1:
        _fail("RUNTIME_INTERPRETER_NLINK_CONTRACT")
    target_held = _open_held_absolute(
        "/root/miniconda3/bin/python3.12", "RUNTIME_INTERPRETER_TARGET",
        mode, max(size, 1), size=size, digest=digest,
    )
    target_stat = target_held["record"]["stat"]
    proc_fd = None
    try:
        proc_fd = os.open(b"/proc/self/exe", os.O_RDONLY | os.O_CLOEXEC)
        proc_first = os.fstat(proc_fd)
        if _stat_key(proc_first) != target_stat:
            _fail("RUNTIME_IMAGE_IDENTITY")
        hasher = hashlib.sha256()
        total = 0
        while True:
            block = os.read(proc_fd, CHUNK)
            if not block:
                break
            total += len(block)
            if total > size:
                _fail("RUNTIME_IMAGE_SIZE")
            hasher.update(block)
        proc_last = os.fstat(proc_fd)
        _check_held_absolute(
            target_held, "RUNTIME_INTERPRETER_TARGET_TERMINAL",
        )
    except OSError:
        _fail("RUNTIME_IMAGE_OPEN_READ")
    finally:
        if proc_fd is not None:
            try:
                os.close(proc_fd)
            except OSError:
                pass
        _close_held_absolute(target_held)
    if (_stat_key(proc_first) != _stat_key(proc_last) or total != size or
            hasher.hexdigest() != digest):
        _fail("RUNTIME_IMAGE_BINDING")
    return (
        link_vector, target_stat, _stat_key(proc_last), digest,
        _nofile_vector("RUNTIME_NOFILE"),
    )


def _directory_row(name, st, tag, nlink=None):
    if not stat.S_ISDIR(st.st_mode) or stat.S_IMODE(st.st_mode) != 0o700:
        _fail(tag + "_DIR")
    if nlink is not None and st.st_nlink != nlink:
        _fail(tag + "_NLINK")
    return (name, "directory", "-", "-", "0700", str(st.st_nlink), "-")


def _regular_row(name, size, lf, mode, nlink, digest):
    return (
        name, "regular", str(size), str(lf),
        "%04o" % mode, str(nlink), digest,
    )


def _frame_rows(rows, tag):
    ordered = tuple(sorted(rows, key=lambda row: row[0].encode("ascii")))
    if len({row[0] for row in ordered}) != len(ordered):
        _fail(tag + "_DUPLICATE")
    try:
        return ("".join("\t".join(row) + "\n" for row in ordered)).encode("ascii")
    except UnicodeEncodeError:
        _fail(tag + "_ASCII")


def _root_frame(root, state, tag):
    if root not in ROOT_CONFIG or state not in ROOT_ALLOWED_NAMES:
        _usage("ROOT_STATE")
    expected_names = ROOT_ALLOWED_NAMES[state]
    fd, before, chain = _open_exact_dir(root, tag, 0o700, 7)
    rows = [_directory_row(".", before, tag + "_ROOT", 7)]
    cache_handles = []
    regular_cache = []
    try:
        _list_fd_exact(fd, expected_names, tag)
        for index, name in enumerate(sorted(expected_names)):
            child_tag = tag + "_%02d" % index
            if name in CACHE_NAMES:
                cache_fd, cache_before = _open_empty_child(fd, name, child_tag)
                cache_handles.append((name, cache_fd, cache_before, child_tag))
                rows.append(_directory_row(name, cache_before, child_tag, 2))
                continue
            mode = 0o644 if name in SOURCE_BASENAME_IDENTITIES else 0o600
            limit = _root_file_cap(name)
            record = _hold_regular_at(fd, name, child_tag, mode, limit)
            regular_cache.append((record, child_tag))
            if name in SOURCE_BASENAME_IDENTITIES:
                size, lf, expected_mode, nlink, expected_hash = SOURCE_BASENAME_IDENTITIES[name]
                if (record["size"], record["lf"], mode, 1,
                        record["digest"]) != (
                        size, lf, expected_mode, nlink, expected_hash):
                    _fail(child_tag + "_SOURCE_IDENTITY")
            rows.append(_regular_row(
                name, record["size"], record["lf"], mode, 1,
                record["digest"],
            ))
    finally:
        cache_failure = None
        try:
            _list_fd_exact(fd, expected_names, tag + "_FINAL")
            for record, child_tag in regular_cache:
                _check_held_regular_at(
                    fd, record, child_tag + "_FINAL_VERSION",
                )
        except CheckFail as exc:
            cache_failure = exc
        for record, _ in reversed(regular_cache):
            try:
                os.close(record["fd"])
            except OSError:
                pass
        for name, cache_fd, cache_before, child_tag in reversed(cache_handles):
            try:
                _close_empty_child(fd, name, cache_fd, cache_before, child_tag)
            except CheckFail as exc:
                if cache_failure is None:
                    cache_failure = exc
        try:
            _close_exact_dir(fd, before, root, tag, chain)
        except CheckFail as exc:
            if cache_failure is None:
                cache_failure = exc
        if cache_failure is not None:
            raise cache_failure
    frame = _frame_rows(rows, tag)
    parsed = _parse_manifest(frame, tag + "_SELF")
    if set(parsed) != {"."}.union(expected_names):
        _fail(tag + "_PARSED_SET")
    return frame, len(rows)


def _parse_manifest(data, tag):
    lf = _line_byte_preflight(
        data, 256 * KIB, 1024, 16 * KIB, True, tag + "_PREFLIGHT",
    )
    if (data.startswith(b"\n") or data.endswith(b"\n\n") or
            b"\r" in data or b"\x00" in data):
        _fail(tag + "_FRAMING")
    try:
        text = data.decode("ascii", "strict")
    except UnicodeDecodeError:
        _fail(tag + "_ASCII")
    result = {}
    previous = None
    for line in _lf_lines(text, lf, tag + "_LINES"):
        fields = line.split("\t")
        if len(fields) != 7:
            _fail(tag + "_FIELDS")
        name, kind, size, lf, mode, nlink, digest = fields
        if previous is not None and name.encode("ascii") <= previous:
            _fail(tag + "_ORDER")
        previous = name.encode("ascii")
        if name in result or kind not in ("directory", "regular"):
            _fail(tag + "_ROW")
        if kind == "directory":
            if size != "-" or lf != "-" or digest != "-" or mode != "0700" or not re.fullmatch(r"[1-9][0-9]*", nlink):
                _fail(tag + "_DIRECTORY")
        else:
            if (not re.fullmatch(r"0|[1-9][0-9]*", size) or
                    not re.fullmatch(r"0|[1-9][0-9]*", lf) or
                    not re.fullmatch(r"0600|0644", mode) or nlink != "1" or
                    not re.fullmatch(r"[0-9a-f]{64}", digest)):
                _fail(tag + "_REGULAR")
        result[name] = tuple(fields)
    return result


def _read_manifest(path, tag):
    data, _, _, _ = _read_regular(path, tag, mode=0o600, limit=256 * KIB)
    return data, _parse_manifest(data, tag)


def _check_manifest_transition(root, ident, current, tag):
    previous_ids = {"R024": "R009", "R033": "R024", "R044": "R033", "R054": "R044"}
    if ident == "R009":
        return
    previous_id = previous_ids[ident]
    previous_path = MANIFEST_MAP[(root, previous_id)][1]
    _, previous = _read_manifest(previous_path, tag + "_PREVIOUS")
    current_rows = _parse_manifest(current, tag + "_CURRENT")
    if ident == "R024":
        immutable = {".", *CACHE_NAMES, "main.tex", "math_commands.tex", "references.bib"}
        additions = {"main.aux", "main.fls", "main.log", "main.pdf"}
    elif ident == "R033":
        immutable = set(previous)
        additions = {"main.bbl", "main.blg"}
    else:
        immutable = {".", *CACHE_NAMES, "main.tex", "math_commands.tex", "references.bib", "main.bbl", "main.blg"}
        additions = set()
    if set(current_rows) != set(previous).union(additions):
        _fail(tag + "_DELTA_SET")
    for name in immutable:
        if previous.get(name) != current_rows.get(name):
            _fail(tag + "_IMMUTABLE_" + name.encode("ascii").hex())


def _verify_validator_copy():
    lock, lock_size, lock_lf, lock_hash, lock_stat = _read_regular(
        VALIDATOR_LOCK, "VALIDATOR_LOCK", mode=0o644, limit=1024 * 1024,
        return_stat=True,
    )
    _line_byte_preflight(
        lock, MIB, 10000, 64 * KIB, True, "VALIDATOR_LOCK_PREFLIGHT",
    )
    lock_text = _strict_text(lock, lock_lf, "VALIDATOR_LOCK")
    lines = _lf_lines(lock_text, lock_lf, "VALIDATOR_LOCK_LINES")
    if (not lines or lines[-1] != VALIDATOR_LOCK_TERMINAL or
            lines.count(VALIDATOR_LOCK_TERMINAL) != 1 or
            lines.count(VALIDATOR_IDENTITY_BEGIN) != 1 or
            lines.count(VALIDATOR_IDENTITY_END) != 1):
        _fail("VALIDATOR_LOCK_MARKERS")
    begin = lines.index(VALIDATOR_IDENTITY_BEGIN)
    end = lines.index(VALIDATOR_IDENTITY_END)
    if end != begin + 7:
        _fail("VALIDATOR_LOCK_IDENTITY_FRAME")
    fields = lines[begin + 1:end]
    expected_names = ("bytes", "LF", "mode", "nlink", "sha256", "terminal")
    values = {}
    for expected_name, line in zip(expected_names, fields):
        if "=" not in line:
            _fail("VALIDATOR_LOCK_IDENTITY_FIELD")
        name, value = line.split("=", 1)
        if name != expected_name:
            _fail("VALIDATOR_LOCK_IDENTITY_ORDER")
        values[name] = value
    if (not re.fullmatch(r"[1-9][0-9]*", values["bytes"]) or
            not re.fullmatch(r"[1-9][0-9]*", values["LF"]) or
            values["mode"] != "0644" or values["nlink"] != "1" or
            not re.fullmatch(r"[0-9a-f]{64}", values["sha256"]) or
            values["terminal"] != VALIDATOR_TERMINAL):
        _fail("VALIDATOR_LOCK_IDENTITY_VALUE")
    size = _bounded_decimal(
        values["bytes"], "VALIDATOR_LOCK_BYTES", MAX_DYNAMIC_BYTES,
        positive=True,
    )
    lf = _bounded_decimal(
        values["LF"], "VALIDATOR_LOCK_LF", size, positive=True,
    )
    digest = values["sha256"]
    source_identity = (size, lf, 0o644, 1, digest)
    copy_identity = (size, lf, 0o500, 1, digest)
    source, source_stat = _read_bound_text(
        VALIDATOR_SOURCE, source_identity, "VALIDATOR_SOURCE", return_stat=True,
    )
    copy, copy_stat = _read_bound_text(
        VALIDATOR_COPY, copy_identity, "VALIDATOR_COPY", return_stat=True,
    )
    _line_byte_preflight(
        source, MIB, 100000, 64 * KIB, True,
        "VALIDATOR_SOURCE_PREFLIGHT",
    )
    source_text = _strict_text(source, lf, "VALIDATOR_SOURCE_TEXT")
    source_lines = _lf_lines(source_text, lf, "VALIDATOR_SOURCE_LINES")
    if (source != copy or source_lines[-1] != VALIDATOR_TERMINAL or
            source_lines.count(VALIDATOR_TERMINAL) != 1):
        _fail("VALIDATOR_COPY_BINDING")
    return (
        (size, lf, digest),
        (lock_size, lock_lf, lock_hash, lock_stat),
        source_stat, copy_stat,
    )


def _mode_absent(args):
    root, stage = args
    if root not in ROOT_CONFIG or ROOT_CONFIG[root][0] != stage:
        _usage("ABSENT_TUPLE")
    _verify_controls_and_sources()
    _verify_tools()
    _verify_dependencies()
    _verify_validator_copy()
    parent = _lstat(BUILD_PARENT, "BUILD_PARENT")
    if not stat.S_ISDIR(parent.st_mode) or stat.S_ISLNK(parent.st_mode):
        _fail("BUILD_PARENT_TYPE")
    _list_exact_directory(EVIDENCE, EVIDENCE_ROOT_AT_ABSENT[root], "EVIDENCE_ROOT", 0o700)
    _check_inflight_directory(stage, (), "A000", "EMPTY_STAGE", 2)
    _require_absent(root, "ROOT_ABSENCE")
    return "root=" + ROOT_CONFIG[root][1] + " absent=1 stage_empty=1 dependencies=87/86"


def _mode_replay(args):
    root, checkpoint = args
    if root not in ROOT_CONFIG or checkpoint not in ROOT_STATES:
        _usage("REPLAY_TUPLE")
    _verify_controls_and_sources()
    _verify_tools()
    rows, finals = _verify_dependencies()
    _verify_validator_copy()
    _verify_root_source_copies(root)
    frame, count = _root_frame(root, ROOT_STATES[checkpoint], "REPLAY_ROOT")
    return ("root=" + ROOT_CONFIG[root][1] + " checkpoint=" + checkpoint +
            " root_rows=" + str(count) + " root_sha256=" + hashlib.sha256(frame).hexdigest() +
            " dependencies=" + str(rows) + "/" + str(finals))


def _mode_snapshot(args):
    root, ident, source, destination = args
    expected = SNAPSHOT_MAP.get((root, ident))
    if expected is None or expected != (source, destination):
        _usage("SNAPSHOT_TUPLE")
    source_limit = _root_file_cap(source.rsplit("/", 1)[1])
    destination_limit = _stage_file_cap(destination.rsplit("/", 1)[1])
    if source_limit != destination_limit:
        raise RuntimeError("snapshot cap mismatch")
    data, size, lf, digest = _read_regular(
        source, "SNAPSHOT_SOURCE", mode=0o600, limit=source_limit,
    )
    written_size, written_lf, written_hash = _exclusive_write(destination, data, "SNAPSHOT_DEST")
    if (size, lf, digest) != (written_size, written_lf, written_hash):
        _fail("SNAPSHOT_BINDING")
    rebound, rebound_size, rebound_lf, rebound_hash = _read_regular(
        source, "SNAPSHOT_SOURCE_POST", mode=0o600, limit=source_limit,
    )
    if (rebound != data or
            (rebound_size, rebound_lf, rebound_hash) != (size, lf, digest)):
        _fail("SNAPSHOT_SOURCE_POST_BINDING")
    destination_data, destination_size, destination_lf, destination_hash = _read_regular(
        destination, "SNAPSHOT_DEST_TERMINAL", mode=0o600,
        limit=destination_limit,
    )
    if (destination_data != data or
            (destination_size, destination_lf, destination_hash) != (size, lf, digest)):
        _fail("SNAPSHOT_DEST_TERMINAL_BINDING")
    return "root=" + ROOT_CONFIG[root][1] + " id=" + ident + " bytes=" + str(size) + " LF=" + str(lf) + " sha256=" + digest


def _mode_manifest(args):
    root, ident, destination = args
    expected = MANIFEST_MAP.get((root, ident))
    if expected is None or expected[1] != destination:
        _usage("MANIFEST_TUPLE")
    state = expected[0]
    frame, count = _root_frame(root, state, "MANIFEST_ROOT")
    _check_manifest_transition(root, ident, frame, "MANIFEST_TRANSITION")
    size, lf, digest = _exclusive_write(destination, frame, "MANIFEST_DEST")
    if lf != count:
        _fail("MANIFEST_ROW_CENSUS")
    terminal_frame, terminal_count = _root_frame(root, state, "MANIFEST_ROOT_TERMINAL")
    if terminal_frame != frame or terminal_count != count:
        _fail("MANIFEST_ROOT_TERMINAL_VERSION")
    terminal_destination, terminal_size, terminal_lf, terminal_hash = _read_regular(
        destination, "MANIFEST_DEST_TERMINAL", mode=0o600, limit=256 * KIB,
    )
    if (terminal_destination != frame or
            (terminal_size, terminal_lf, terminal_hash) != (size, lf, digest)):
        _fail("MANIFEST_DEST_TERMINAL_VERSION")
    _check_manifest_transition(root, ident, terminal_destination, "MANIFEST_TRANSITION_TERMINAL")
    final_destination, final_size, final_lf, final_hash = _read_regular(
        destination, "MANIFEST_DEST_FINAL", mode=0o600, limit=256 * KIB,
    )
    if (final_destination != terminal_destination or
            (final_size, final_lf, final_hash) != (terminal_size, terminal_lf, terminal_hash)):
        _fail("MANIFEST_DEST_FINAL_VERSION")
    return "root=" + ROOT_CONFIG[root][1] + " id=" + ident + " rows=" + str(count) + " bytes=" + str(size) + " sha256=" + digest


def _root_local_recorder_name(path, root):
    if path.startswith(root + "/"):
        suffix = path[len(root) + 1:]
        return suffix if "/" not in suffix and suffix != "" else None
    if path.startswith("./") and "/" not in path[2:]:
        return path[2:]
    if not path.startswith("/") and "/" not in path and path != "":
        return path
    return None


def _parse_recorder(root, ident, data, tag):
    lf = _line_byte_preflight(
        data, 8 * MIB, MAX_RECORDER_LINES, MAX_RECORDER_LINE_BYTES,
        True, tag + "_PREFLIGHT",
    )
    text = _strict_text(data, lf, tag)
    pwd_count = 0
    local_inputs = set()
    local_outputs = set()
    external_inputs = set()
    for number, line in enumerate(_lf_lines(text, lf, tag + "_LINES"), 1):
        if line.startswith("PWD "):
            if line[4:] != root:
                _fail(tag + "_PWD")
            pwd_count += 1
            continue
        if line.startswith("INPUT "):
            value = line[6:]
            local = _root_local_recorder_name(value, root)
            if local is not None:
                local_inputs.add(local)
            elif value in DEPENDENCY_LOGICAL or value in DEPENDENCY_FINAL:
                external_inputs.add(value)
            else:
                _fail(tag + "_INPUT_LINE_%d" % number)
            continue
        if line.startswith("OUTPUT "):
            value = line[7:]
            local = _root_local_recorder_name(value, root)
            if local is None:
                _fail(tag + "_OUTPUT_LINE_%d" % number)
            local_outputs.add(local)
            continue
        _fail(tag + "_GRAMMAR_LINE_%d" % number)
    if pwd_count != 1:
        _fail(tag + "_PWD_CENSUS")
    later = ident in ("R043", "R053")
    allowed_inputs = {"main.tex", "math_commands.tex", "main.aux"}
    required_inputs = {"main.tex", "math_commands.tex"}
    if later:
        allowed_inputs.add("main.bbl")
        required_inputs.update(("main.aux", "main.bbl"))
    if not required_inputs.issubset(local_inputs) or not local_inputs.issubset(allowed_inputs):
        _fail(tag + "_LOCAL_INPUT_SET")
    if local_outputs != {"main.aux", "main.fls", "main.log", "main.pdf"}:
        _fail(tag + "_LOCAL_OUTPUT_SET")
    if not external_inputs or not external_inputs.issubset(DEPENDENCY_LOGICAL.union(DEPENDENCY_FINAL)):
        _fail(tag + "_EXTERNAL_SET")
    return len(local_inputs), len(local_outputs), len(external_inputs)


def _normalized_recorder(data, root, tag):
    prefix = root.encode("ascii")
    if prefix not in data:
        _fail(tag + "_PREFIX_ABSENT")
    normalized = data.replace(prefix, b"<ROOT>")
    if root.encode("ascii") in normalized:
        _fail(tag + "_PREFIX_REMAINS")
    return normalized, hashlib.sha256(normalized).hexdigest()


def _mode_recorder(args):
    root, ident, snapshot = args
    expected = RECORDER_MAP.get((root, ident))
    if expected is None or snapshot != expected:
        _usage("RECORDER_TUPLE")
    data, size, lf, digest = _read_regular(
        snapshot, "RECORDER_SNAPSHOT", mode=0o600, limit=8 * MIB,
    )
    local_in, local_out, external = _parse_recorder(root, ident, data, "RECORDER")
    normalized_data, normalized_hash = _normalized_recorder(
        data, root, "RECORDER_NORMALIZE",
    )
    del normalized_data
    return ("root=" + ROOT_CONFIG[root][1] + " id=" + ident + " bytes=" + str(size) +
            " LF=" + str(lf) + " sha256=" + digest + " normalized_sha256=" + normalized_hash +
            " local_inputs=" + str(local_in) + " local_outputs=" + str(local_out) +
            " external_unique=" + str(external))


def _mode_r033live(args):
    root, live, snapshot = args
    if root not in R033_LIVE_MAP or R033_LIVE_MAP[root] != (live, snapshot):
        _usage("R033LIVE_TUPLE")
    size, lf, digest = _same_regular(
        live, snapshot, "R033LIVE", limit=8 * MIB,
    )
    return "root=" + ROOT_CONFIG[root][1] + " bytes=" + str(size) + " LF=" + str(lf) + " sha256=" + digest


def _active_tex_lines(text, tag):
    active = []
    for line in _lf_lines(text, text.count("\n"), tag):
        cut = len(line)
        for index, value in enumerate(line):
            if value != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        active.append(line[:cut])
    return tuple(active)


def _tex_control_words(line):
    words = []
    position = 0
    while position < len(line):
        if line[position] != "\\":
            position += 1
            continue
        position += 1
        if position >= len(line):
            words.append("")
            break
        if ("A" <= line[position] <= "Z" or "a" <= line[position] <= "z" or
                line[position] == "@"):
            start = position
            while (position < len(line) and
                   ("A" <= line[position] <= "Z" or "a" <= line[position] <= "z" or
                    line[position] == "@")):
                position += 1
            words.append(line[start:position])
        else:
            words.append(line[position])
            position += 1
    return tuple(words)


def _source_citation_keys(data, tag):
    text = _strict_text(data, data.count(b"\n"), tag)
    active_text = "\n".join(_active_tex_lines(text, tag + "_ACTIVE"))
    keys = []
    for group in re.findall(r"\\cite\{([^}]*)\}", active_text, re.DOTALL):
        for key in group.split(","):
            stripped = key.strip()
            if not re.fullmatch(r"[a-z0-9_]+", stripped):
                _fail(tag + "_KEY")
            keys.append(stripped)
    return keys


def _bib_entry_keys(data, tag):
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError:
        _fail(tag + "_UTF8")
    return re.findall(r"(?m)^@[A-Za-z]+\{([^,\s]+),", text)


def _balanced_tex_braces(line):
    depth = 0
    for index, value in enumerate(line):
        if value not in "{}":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2:
            continue
        depth += 1 if value == "{" else -1
        if depth < 0:
            return False
    return depth == 0


def _tex_brace_depth(line, initial):
    depth = initial
    for index, value in enumerate(line):
        if value not in "{}":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2:
            continue
        depth += 1 if value == "{" else -1
        if depth < 0:
            return -1
    return depth


def _tex_group_at(text, position, tag):
    while position < len(text) and text[position].isspace():
        position += 1
    if position >= len(text) or text[position] != "{":
        _fail(tag + "_OPEN")
    start = position + 1
    depth = 1
    position += 1
    while position < len(text):
        value = text[position]
        if value in "{}":
            backslashes = 0
            cursor = position - 1
            while cursor >= start and text[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                depth += 1 if value == "{" else -1
                if depth == 0:
                    return text[start:position], position + 1
                if depth < 0:
                    _fail(tag + "_DEPTH")
        position += 1
    _fail(tag + "_UNTERMINATED")


def _tex_exact_control_groups(text, control, count, tag):
    if not text.startswith(control):
        _fail(tag + "_CONTROL")
    position = len(control)
    groups = []
    for index in range(count):
        group, position = _tex_group_at(
            text, position, tag + "_GROUP_%d" % index,
        )
        groups.append(group)
    if text[position:].strip():
        _fail(tag + "_TRAILING")
    return tuple(groups)


def _aux_plain_text(text, tag):
    value = text.strip()
    if (not value or "^^" in value or any(
            character in value for character in "\\{}%\x00\r\n"
    ) or any(ord(character) < 0x20 for character in value)):
        _fail(tag + "_PLAIN_TEXT")
    return value


def _validate_aux_writefile(line, pdf_pages, tag):
    channel, payload = _tex_exact_control_groups(
        line, r"\@writefile", 2, tag + "_OUTER",
    )
    if channel not in ("toc", "lof", "lot"):
        _fail(tag + "_CHANNEL")
    if not payload.startswith(r"\contentsline"):
        _fail(tag + "_CONTENTS_CONTROL")
    position = len(r"\contentsline")
    fields = []
    for index in range(4):
        field, position = _tex_group_at(
            payload, position, tag + "_CONTENTS_%d" % index,
        )
        fields.append(field)
    if payload[position:].strip() != r"\protected@file@percent":
        _fail(tag + "_CONTENTS_TRAILING")
    kind, title, page, anchor = fields
    admitted = {
        "toc": frozenset({"section", "subsection", "subsubsection"}),
        "lof": frozenset({"figure"}),
        "lot": frozenset({"table"}),
    }
    if kind.strip() not in admitted[channel]:
        _fail(tag + "_KIND")
    page_value = page.strip()
    if (re.fullmatch(r"[1-9][0-9]{0,5}", page_value) is None or
            _bounded_decimal(
                page_value, tag + "_PAGE", pdf_pages, positive=True,
            ) > pdf_pages or anchor.strip()):
        _fail(tag + "_PAGE_OR_ANCHOR")
    if not title.startswith(r"\numberline"):
        _fail(tag + "_NUMBERLINE_CONTROL")
    number, after_number = _tex_group_at(
        title, len(r"\numberline"), tag + "_NUMBERLINE",
    )
    if re.fullmatch(r"[1-9][0-9]*(?:\.[1-9][0-9]*)*", number.strip()) is None:
        _fail(tag + "_NUMBER")
    remainder = title[after_number:].strip()
    if channel == "toc":
        _aux_plain_text(remainder, tag + "_TITLE")
    else:
        caption, caption_end = _tex_group_at(remainder, 0, tag + "_CAPTION")
        if remainder[caption_end:].strip() or not caption.startswith(r"\ignorespaces"):
            _fail(tag + "_CAPTION_GRAMMAR")
        _aux_plain_text(
            caption[len(r"\ignorespaces"):], tag + "_CAPTION_TEXT",
        )


def _validate_aux_newlabel(line, pdf_pages, tag):
    label, payload = _tex_exact_control_groups(
        line, r"\newlabel", 2, tag + "_OUTER",
    )
    if re.fullmatch(r"[A-Za-z0-9:._-]+", label) is None:
        _fail(tag + "_LABEL")
    display, page = _tex_exact_control_groups(
        payload, "", 2, tag + "_PAYLOAD",
    )
    page_value = page.strip()
    if (re.fullmatch(r"[1-9][0-9]*(?:\.[1-9][0-9]*)*", display.strip()) is None or
            re.fullmatch(r"[1-9][0-9]{0,5}", page_value) is None or
            _bounded_decimal(
                page_value, tag + "_PAGE", pdf_pages, positive=True,
            ) > pdf_pages):
        _fail(tag + "_FIELDS")


def _validate_aux_surface(aux_text, pdf_pages, tag):
    if (len(aux_text.encode("utf-8")) > 4 * MIB or
            aux_text.count("\n") > 100000):
        _fail(tag + "_SIZE")
    physical_lines = _lf_lines(
        aux_text, aux_text.count("\n"), tag + "_PHYSICAL_LINES",
    )
    if any(len(line.encode("utf-8")) > 16 * KIB for line in physical_lines):
        _fail(tag + "_PHYSICAL_LINE")
    lines = _active_tex_lines(aux_text, tag + "_ACTIVE_LINES")
    if len(lines) > 100000:
        _fail(tag + "_LINES")
    allowed = frozenset({
        "relax", "citation", "bibdata", "bibstyle", "bibcite",
        "@writefile", "contentsline", "numberline", "protected@file@percent",
        "ignorespaces", "addvspace", "newlabel", "gdef", "@abspage@last",
        "LT@entry",
    })
    forbidden = frozenset({
        "catcode", "csname", "endcsname", "let", "futurelet", "def", "edef",
        "xdef", "expandafter", "afterassignment", "input", "include", "openin",
        "openout", "read", "write", "write18", "special", "@input",
    })
    longtable_names = set()
    abspage_rows = 0
    cursor = 0
    while cursor < len(lines):
        line = lines[cursor]
        number = cursor + 1
        if len(line.encode("utf-8")) > 16 * KIB:
            _fail(tag + "_LINE_%d" % number)
        stripped = line.strip()
        if stripped == "":
            cursor += 1
            continue
        longtable_start = re.match(r"\\gdef\s+\\(LT@[ivxlcdm]+)\s*\{", stripped)
        if longtable_start is not None:
            record_lines = [line]
            record_bytes = len(line.encode("utf-8"))
            depth = _tex_brace_depth(line, 0)
            while depth > 0:
                cursor += 1
                if cursor >= len(lines) or len(record_lines) >= 4096:
                    _fail(tag + "_LONGTABLE_UNTERMINATED_%d" % number)
                continuation = lines[cursor]
                continuation_bytes = len(continuation.encode("utf-8"))
                if continuation_bytes > 16 * KIB:
                    _fail(tag + "_LONGTABLE_LINE_%d" % (cursor + 1))
                if record_bytes + 1 + continuation_bytes > 256 * KIB:
                    _fail(tag + "_LONGTABLE_SIZE_%d" % number)
                record_bytes += 1 + continuation_bytes
                record_lines.append(continuation)
                depth = _tex_brace_depth(continuation, depth)
            if depth != 0:
                _fail(tag + "_LONGTABLE_BRACES_%d" % number)
            record = "\n".join(record_lines).strip()
            if len(record.encode("utf-8")) > 256 * KIB:
                _fail(tag + "_LONGTABLE_SIZE_%d" % number)
            name = longtable_start.group(1)
            dimension = r"(?:[1-9][0-9]*(?:\.[0-9]+)?|0\.[0-9]*[1-9][0-9]*)pt"
            grammar = (
                r"\\gdef\s+\\" + re.escape(name) + r"\s*\{\s*" +
                r"(?:\\LT@entry\s*\{[1-9][0-9]*\}\s*\{" + dimension +
                r"\}\s*)+\}"
            )
            if name in longtable_names or re.fullmatch(grammar, record) is None:
                _fail(tag + "_LONGTABLE_GRAMMAR_%d" % number)
            longtable_names.add(name)
            cursor += 1
            continue
        if not _balanced_tex_braces(line):
            _fail(tag + "_LINE_%d" % number)
        words = _tex_control_words(line)
        if "^^" in line or any(word in forbidden for word in words):
            _fail(tag + "_DYNAMIC_%d" % number)
        allowed_words = all(
            word in allowed or re.fullmatch(r"LT@[ivxlcdm]+", word) is not None
            for word in words
        )
        if not allowed_words:
            _fail(tag + "_CONTROL_%d" % number)
        if re.fullmatch(r"\\relax\s*", stripped):
            cursor += 1
            continue
        if re.fullmatch(r"\\citation\{[a-z0-9_]+(?:,[a-z0-9_]+)*\}", stripped):
            cursor += 1
            continue
        if stripped in (r"\bibdata{references}", r"\bibstyle{plain}"):
            cursor += 1
            continue
        if re.fullmatch(r"\\bibcite\{[a-z0-9_]+\}\{(?:[1-9]|1[0-9]|20)\}", stripped):
            cursor += 1
            continue
        if stripped.startswith(r"\@writefile"):
            _validate_aux_writefile(
                stripped, pdf_pages, tag + "_WRITEFILE_%d" % number,
            )
            cursor += 1
            continue
        if stripped.startswith(r"\newlabel"):
            _validate_aux_newlabel(
                stripped, pdf_pages, tag + "_NEWLABEL_%d" % number,
            )
            cursor += 1
            continue
        abspage = re.fullmatch(
            r"\\gdef\s+\\@abspage@last\{([1-9][0-9]{0,5})\}", stripped,
        )
        if abspage is not None:
            if (_bounded_decimal(
                    abspage.group(1), tag + "_ABSPAGE", 100000,
                    positive=True,
            ) != pdf_pages or abspage_rows):
                _fail(tag + "_ABSPAGE_BINDING")
            abspage_rows += 1
            cursor += 1
            continue
        _fail(tag + "_GRAMMAR_%d" % number)
    if abspage_rows != 1:
        _fail(tag + "_ABSPAGE_CENSUS")


def _validate_bbl_surface(bbl_text, tag):
    if (len(bbl_text.encode("utf-8")) > 2 * MIB or
            bbl_text.count("\n") > 50000):
        _fail(tag + "_SIZE")
    physical_lines = _lf_lines(
        bbl_text, bbl_text.count("\n"), tag + "_PHYSICAL_LINES",
    )
    if any(len(line.encode("utf-8")) > 16 * KIB for line in physical_lines):
        _fail(tag + "_PHYSICAL_LINE")
    lines = _active_tex_lines(bbl_text, tag + "_ACTIVE_LINES")
    if len(lines) > 50000:
        _fail(tag + "_LINES")
    active = [(index, line.strip()) for index, line in enumerate(lines) if line.strip()]
    if (len(active) < 3 or
            re.fullmatch(r"\\begin\{thebibliography\}\{(?:10|20)\}", active[0][1]) is None or
            active[-1][1] != r"\end{thebibliography}"):
        _fail(tag + "_ENVIRONMENT")
    allowed_words = frozenset({"newblock", "em", "rm", "hbox", "mathbb"})
    allowed_symbols = frozenset({"&", "%", "_", "#", "$", "'", '"', "`", "~", "^", "=", "."})
    items = []
    content_lines = 0
    content_bytes = 0
    content_depth = 0
    newblocks = 0
    for active_index, (line_number, stripped) in enumerate(active):
        line = lines[line_number]
        encoded_line = line.encode("utf-8")
        if len(encoded_line) > 16 * KIB:
            _fail(tag + "_LINE_%d" % (line_number + 1))
        words = _tex_control_words(line)
        if "^^" in line:
            _fail(tag + "_DYNAMIC_%d" % (line_number + 1))
        if active_index == 0:
            if words != ("begin",) or content_depth:
                _fail(tag + "_BEGIN_CONTROL")
            continue
        if active_index == len(active) - 1:
            if (words != ("end",) or not items or content_lines == 0 or
                    content_depth):
                _fail(tag + "_END_CONTROL")
            continue
        item = re.fullmatch(r"\\bibitem\{([a-z0-9_]+)\}", stripped)
        if item is not None:
            if content_depth or (items and content_lines == 0):
                _fail(tag + "_EMPTY_ITEM")
            if len(items) >= 20:
                _fail(tag + "_ITEM_CENSUS")
            items.append(item.group(1))
            content_lines = 0
            content_bytes = 0
            newblocks = 0
            if words != ("bibitem",):
                _fail(tag + "_ITEM_CONTROL")
            continue
        if not items:
            _fail(tag + "_CONTENT_BEFORE_ITEM")
        if stripped.startswith(r"\bibitem") or stripped.startswith(
                r"\end{thebibliography}"):
            _fail(tag + "_RECORD_BOUNDARY")
        for word in words:
            if ((word and (word[0].isalpha() or word[0] == "@") and
                 word not in allowed_words) or
                    (not word or (not word[0].isalpha() and word not in allowed_symbols))):
                _fail(tag + "_CONTROL_%d" % (line_number + 1))
        if "newblock" in words:
            if words.count("newblock") != 1 or not stripped.startswith(r"\newblock "):
                _fail(tag + "_NEWBLOCK_GRAMMAR")
            newblocks += 1
            if newblocks > 6:
                _fail(tag + "_NEWBLOCK_CENSUS")
        content_depth = _tex_brace_depth(line, content_depth)
        if content_depth < 0:
            _fail(tag + "_BRACE_DEPTH_%d" % (line_number + 1))
        content_lines += 1
        content_bytes += len(encoded_line) + 1
        if content_lines > 4096 or content_bytes > 256 * KIB:
            _fail(tag + "_ITEM_LIMIT")
    if len(items) != 20 or len(set(items)) != 20 or tuple(sorted(items)) != EXPECTED_KEYS:
        _fail(tag + "_KEYS")
    return tuple(items)


BIBTEX_FUNCTION_COUNTER_NAMES = (
    "=", ">", "<", "+", "-", "*", ":=", "add.period$", "call.type$",
    "change.case$", "chr.to.int$", "cite$", "duplicate$", "empty$",
    "format.name$", "if$", "int.to.chr$", "int.to.str$", "missing$",
    "newline$", "num.names$", "pop$", "preamble$", "purify$", "quote$",
    "skip$", "stack$", "substring$", "swap$", "text.length$",
    "text.prefix$", "top$", "type$", "warning$", "while$", "width$", "write$",
)


def _validate_blg_surface(blg_text, tag):
    encoded = blg_text.encode("utf-8")
    if len(encoded) > 512 * KIB:
        _fail(tag + "_SIZE")
    lines = _lf_lines(
        blg_text, blg_text.count("\n"), tag + "_LINES",
    )
    if len(lines) != 9 + len(BIBTEX_FUNCTION_COUNTER_NAMES):
        _fail(tag + "_LINE_CENSUS")
    if any(len(line.encode("utf-8")) > MAX_BLG_LINE_BYTES for line in lines):
        _fail(tag + "_LINE_LIMIT")
    if (re.fullmatch(r"This is BibTeX, Version 0\.99d \(TeX Live [0-9]{4}/Debian\)", lines[0]) is None or
            lines[1] != "Capacity: max_strings=200000, hash_size=200000, hash_prime=170003" or
            lines[2] != "The top-level auxiliary file: main.aux" or
            lines[3] != "The style file: plain.bst" or
            lines[4] != "Database file #1: references.bib" or
            lines[5] != "You've used 20 entries,"):
        _fail(tag + "_HEADER")
    if re.fullmatch(r" +[1-9][0-9]{0,8} wiz_defined-function locations,", lines[6]) is None:
        _fail(tag + "_WIZ")
    if re.fullmatch(r" +[1-9][0-9]{0,8} strings with [1-9][0-9]{0,8} characters,", lines[7]) is None:
        _fail(tag + "_STRINGS")
    total_match = re.fullmatch(
        r"and the built_in function-call counts, ([1-9][0-9]{0,8}) in all, are:",
        lines[8],
    )
    if total_match is None:
        _fail(tag + "_FUNCTION_HEADER")
    total = 0
    for index, (line, name) in enumerate(zip(lines[9:], BIBTEX_FUNCTION_COUNTER_NAMES)):
        match = re.fullmatch(re.escape(name) + r" -- (0|[1-9][0-9]{0,8})", line)
        if match is None:
            _fail(tag + "_FUNCTION_%02d" % index)
        value = _bounded_decimal(
            match.group(1), tag + "_FUNCTION_%02d_COUNT" % index,
            999_999_999,
        )
        if name == "warning$" and value != 0:
            _fail(tag + "_WARNING_COUNT")
        total += value
    if total != _bounded_decimal(
            total_match.group(1), tag + "_FUNCTION_TOTAL_COUNT", 999_999_999,
    ):
        _fail(tag + "_FUNCTION_TOTAL")


def _validate_bibliography_bytes(bbl, blg, tag):
    if (len(bbl) > 2 * MIB or bbl.count(b"\n") > 50000 or
            len(blg) > 512 * KIB or blg.count(b"\n") > 1024):
        _fail(tag + "_PREFLIGHT")
    bbl_lf = _line_byte_preflight(
        bbl, 2 * MIB, 50000, 16 * KIB, True, tag + "_BBL_PREFLIGHT",
    )
    blg_lf = _line_byte_preflight(
        blg, 512 * KIB, 1024, MAX_BLG_LINE_BYTES, True,
        tag + "_BLG_PREFLIGHT",
    )
    bbl_text = _strict_text(bbl, bbl_lf, tag + "_BBL")
    blg_text = _strict_text(blg, blg_lf, tag + "_BLG")
    items = _validate_bbl_surface(bbl_text, tag + "_BBL_SURFACE")
    _validate_blg_surface(blg_text, tag + "_BLG_SURFACE")
    return items


def _validate_source_bib_sets():
    main = _read_bound_text(SOURCE_MAIN, SOURCE_IDENTITIES[SOURCE_MAIN], "CITE_SOURCE")
    bib = _read_bound_text(SOURCE_BIB, SOURCE_IDENTITIES[SOURCE_BIB], "BIB_SOURCE")
    cites = _source_citation_keys(main, "CITE_SOURCE")
    entries = _bib_entry_keys(bib, "BIB_SOURCE")
    if len(cites) != 20 or len(set(cites)) != 20 or tuple(sorted(cites)) != EXPECTED_KEYS:
        _fail("SOURCE_CITATION_SET")
    if len(entries) != 20 or len(set(entries)) != 20 or tuple(sorted(entries)) != EXPECTED_KEYS:
        _fail("SOURCE_BIB_ENTRY_SET")


def _mode_bib(args):
    root, bbl_path, blg_path, bbl_snapshot, blg_snapshot = args
    if root not in BIB_MAP or BIB_MAP[root] != (bbl_path, blg_path, bbl_snapshot, blg_snapshot):
        _usage("BIB_TUPLE")
    _validate_source_bib_sets()
    bbl, _, _, bbl_hash = _read_regular(
        bbl_path, "BIB_BBL", mode=0o600, limit=2 * MIB,
    )
    blg, _, _, blg_hash = _read_regular(
        blg_path, "BIB_BLG", mode=0o600, limit=512 * KIB,
    )
    _same_regular(
        bbl_path, bbl_snapshot, "BIB_BBL_SNAPSHOT", limit=2 * MIB,
    )
    _same_regular(
        blg_path, blg_snapshot, "BIB_BLG_SNAPSHOT", limit=512 * KIB,
    )
    items = _validate_bibliography_bytes(bbl, blg, "BIB")
    return ("root=" + ROOT_CONFIG[root][1] + " items=" + str(len(items)) +
            " bbl_sha256=" + bbl_hash + " blg_sha256=" + blg_hash)


def _receipt_paths(root, ident):
    if root not in ROOT_CONFIG:
        _usage("RECEIPT_ROOT")
    stage = ROOT_CONFIG[root][0]
    return (stage + "/" + ident + ".stdout", stage + "/" + ident + ".stderr", stage + "/" + ident + ".status")


def _parse_validator_stdout(stdout, mode, expected, tag):
    if mode not in VALIDATOR_RESULT_FIELDS:
        _fail(tag + "_MODE")
    if (not stdout.endswith(b"\n") or stdout.count(b"\n") != 1 or b"\r" in stdout or
            b"\x00" in stdout or any(value < 0x20 or value > 0x7e for value in stdout[:-1])):
        _fail(tag + "_FRAMING")
    try:
        text = stdout[:-1].decode("ascii", "strict")
    except UnicodeDecodeError:
        _fail(tag + "_ASCII")
    names = VALIDATOR_RESULT_FIELDS[mode]
    if text.count(" ") != 1 + len(names):
        _fail(tag + "_PREFIX")
    tokens = text.split(" ")
    if len(tokens) != 2 + len(names) or tokens[:2] != ["PASS", mode]:
        _fail(tag + "_PREFIX")
    values = {}
    for name, token in zip(names, tokens[2:]):
        prefix = name + "="
        if not token.startswith(prefix) or token == prefix:
            _fail(tag + "_FIELD_" + name)
        values[name] = token[len(prefix):]
    for name, value in values.items():
        if name in DECIMAL_RESULT_FIELDS:
            if not re.fullmatch(r"0|[1-9][0-9]*", value):
                _fail(tag + "_DECIMAL_" + name)
        elif name == "root":
            if value not in ("r0", "r1"):
                _fail(tag + "_ROOT")
        elif name == "stage":
            if value not in ("r0", "r1"):
                _fail(tag + "_STAGE")
        elif name == "checkpoint":
            if value not in ROOT_STATES:
                _fail(tag + "_CHECKPOINT")
        elif name == "id":
            if not re.fullmatch(r"R0(?:09|21|22|23|24|31|32|33|41|42|43|44|51|52|53|54)", value):
                _fail(tag + "_ID")
        elif name == "dependencies":
            if value != "87/86":
                _fail(tag + "_DEPENDENCIES")
        elif name == "disposition":
            if value != "benign-underfull-only":
                _fail(tag + "_DISPOSITION")
        elif name == "warning_bytes_hex":
            if value != "-" and (len(value) % 2 or re.fullmatch(r"[0-9a-f]+", value) is None):
                _fail(tag + "_WARNING_HEX")
        elif name == "recorder_sha256":
            pattern = r"R023:([0-9a-f]{64})/\1,R043:([0-9a-f]{64})/\2,R053:([0-9a-f]{64})/\3"
            if re.fullmatch(pattern, value) is None:
                _fail(tag + "_RECORDER_HASHES")
        elif name == "manifest_sha256" and mode == "CROSS":
            pattern = (r"R009:([0-9a-f]{64})/\1,R024:([0-9a-f]{64})/\2,"
                       r"R033:([0-9a-f]{64})/\3,R044:([0-9a-f]{64})/\4,"
                       r"R054:([0-9a-f]{64})/\5")
            if re.fullmatch(pattern, value) is None:
                _fail(tag + "_MANIFEST_HASHES")
        elif "sha256" in name:
            if re.fullmatch(r"[0-9a-f]{64}", value) is None:
                _fail(tag + "_HASH_" + name)
        else:
            _fail(tag + "_UNVALIDATED_" + name)
    for name, value in expected:
        if values.get(name) != value:
            _fail(tag + "_EXPECTED_" + name)
    return values


def _validate_receipt_bytes(stdout, stderr, status_data, kind, tag):
    parsed = None
    if stderr != b"" or status_data != b"0\n":
        _fail(tag + "_STATUS")
    if kind == "silent":
        if stdout != b"":
            _fail(tag + "_STDOUT")
    elif isinstance(kind, tuple) and len(kind) == 3 and kind[0] == "validator":
        parsed = _parse_validator_stdout(stdout, kind[1], kind[2], tag + "_VALIDATOR")
    elif kind in ("text", "pdfinfo"):
        if not stdout or not stdout.endswith(b"\n") or b"\r" in stdout or b"\x00" in stdout:
            _fail(tag + "_TEXT_STDOUT")
        try:
            stdout.decode("utf-8", "strict")
        except UnicodeDecodeError:
            _fail(tag + "_TEXT_UTF8")
    elif kind == "pdftext":
        if not stdout or b"\r" in stdout or b"\x00" in stdout:
            _fail(tag + "_PDFTEXT_STDOUT")
        try:
            stdout.decode("utf-8", "strict")
        except UnicodeDecodeError:
            _fail(tag + "_PDFTEXT_UTF8")
    else:
        _fail(tag + "_KIND")
    return parsed


def _read_receipt_triplet(root, ident, kind, tag):
    stdout_path, stderr_path, status_path = _receipt_paths(root, ident)
    stdout_limits = {"pdfinfo": 64 * KIB, "pdftext": 8 * MIB}
    if kind not in stdout_limits:
        _fail(tag + "_KIND_LIMIT")
    stdout, _, _, _ = _read_regular(
        stdout_path, tag + "_OUT", mode=0o600, limit=stdout_limits[kind],
    )
    stderr, _, _, _ = _read_regular(
        stderr_path, tag + "_ERR", mode=0o600, limit=0,
    )
    status_data, _, _, _ = _read_regular(
        status_path, tag + "_STATUS", mode=0o600, limit=2,
    )
    _validate_receipt_bytes(stdout, stderr, status_data, kind, tag)
    return stdout


def _parse_pdfinfo(data, pdf_size, tag):
    schema = (
        "Title", "Subject", "Keywords", "Author", "Creator", "Producer",
        "CreationDate", "ModDate", "Custom Metadata", "Metadata Stream", "Tagged",
        "UserProperties", "Suspects", "Form", "JavaScript", "Pages", "Encrypted",
        "Page size", "Page rot", "File size", "Optimized", "PDF version",
    )
    if (len(data) > 64 * KIB or not data.endswith(b"\n") or
            data.endswith(b"\n\n") or b"\r" in data or b"\x00" in data or
            data.startswith(b"\xef\xbb\xbf")):
        _fail(tag + "_FRAMING")
    fields = {}
    encoded_schema = tuple((key, (key + ":").encode("ascii")) for key in schema)
    for raw_line in data[:-1].split(b"\n"):
        if (len(raw_line) > 4096 or b"\t" in raw_line or
                any(value >= 0x80 for value in raw_line)):
            _fail(tag + "_LINE_BYTES")
        matches = tuple(
            (key, prefix) for key, prefix in encoded_schema
            if raw_line.startswith(prefix)
        )
        if len(matches) != 1:
            _fail(tag + "_LINE_KEY")
        key, prefix = matches[0]
        value_bytes = raw_line[len(prefix):]
        if any(value < 0x20 or value > 0x7e for value in value_bytes):
            _fail(tag + "_VALUE_BYTES")
        value_bytes = value_bytes.lstrip(b" ")
        if value_bytes.endswith(b" "):
            _fail(tag + "_VALUE_TRAILING_SPACE")
        value = value_bytes.decode("ascii")
        if key in fields:
            _fail(tag + "_DUPLICATE")
        fields[key] = value
    exact = {
        "Creator": "TeX", "Producer": "pdfTeX-1.40.22", "Custom Metadata": "no",
        "Metadata Stream": "no", "Tagged": "no", "UserProperties": "no", "Suspects": "no",
        "Form": "none", "JavaScript": "no", "Encrypted": "no", "Page rot": "0",
        "Optimized": "no", "PDF version": "1.5",
    }
    for key, value in exact.items():
        if fields.get(key) != value:
            _fail(tag + "_FIELD_" + key.replace(" ", "_"))
    if fields.get("CreationDate") != "D:19700101000000Z" or fields.get("ModDate") != "D:19700101000000Z":
        _fail(tag + "_DATES")
    if fields.get("Author", "") not in ("", "Anonymous"):
        _fail(tag + "_AUTHOR")
    if fields.get("Title", "") not in ("", TITLE):
        _fail(tag + "_TITLE")
    if fields.get("Subject", "") != "" or fields.get("Keywords", "") != "":
        _fail(tag + "_SUBJECT_KEYWORDS")
    if fields.get("Page size") not in ("612 x 792 pts (letter)", "612 x 792 pts"):
        _fail(tag + "_PAGE_SIZE")
    pages = _bounded_decimal(
        fields.get("Pages", ""), tag + "_PAGES", 100_000, positive=True,
    )
    file_match = re.fullmatch(r"([1-9][0-9]{0,8}) bytes", fields.get("File size", ""))
    if (file_match is None or _bounded_decimal(
            file_match.group(1), tag + "_FILE_SIZE_VALUE", 64 * MIB,
            positive=True,
    ) != pdf_size):
        _fail(tag + "_FILE_SIZE")
    required_fields = set(exact).union({
        "CreationDate", "ModDate", "Pages", "Page size", "File size",
    })
    optional_fields = {"Title", "Subject", "Keywords", "Author"}
    if not required_fields.issubset(fields) or set(fields) - required_fields - optional_fields:
        _fail(tag + "_FIELD_SET")
    if tuple(fields) != tuple(name for name in schema if name in fields):
        _fail(tag + "_FIELD_ORDER")
    return pages, fields


def _parse_log(log, pdf_size, pdf_pages, tag):
    lf = _line_byte_preflight(
        log, 8 * MIB, MAX_LOG_LINES, MAX_LOG_LINE_BYTES, True,
        tag + "_PREFLIGHT",
    )
    text = _strict_text(log, lf, tag)
    lines = _lf_lines(text, lf, tag + "_LINES")
    if any(len(line.encode("utf-8")) > MAX_LOG_LINE_BYTES for line in lines):
        _fail(tag + "_LINE_LIMIT")
    sentinel_matches = _bounded_regex_rows(
        re.compile(r"(?m)^BATCH07_REFERENCE_START_PAGE=([1-9][0-9]{0,5})$"),
        text, 1, tag + "_SENTINEL_ROWS",
    )
    output_matches = _bounded_regex_rows(
        re.compile(
            r"(?m)^Output written on main\.pdf \(([1-9][0-9]{0,5}) pages?, ([1-9][0-9]{0,8}) bytes\)\.$"
        ),
        text, 1, tag + "_OUTPUT_ROWS",
    )
    if len(sentinel_matches) != 1 or len(output_matches) != 1:
        _fail(tag + "_SENTINEL_OUTPUT")
    sentinel = _bounded_decimal(
        sentinel_matches[0].group(1), tag + "_SENTINEL", 100_000,
        positive=True,
    )
    pages = _bounded_decimal(
        output_matches[0].group(1), tag + "_OUTPUT_PAGES", 100_000,
        positive=True,
    )
    logged_bytes = _bounded_decimal(
        output_matches[0].group(2), tag + "_OUTPUT_BYTES", 64 * MIB,
        positive=True,
    )
    if pages != pdf_pages or logged_bytes != pdf_size or not (24 <= sentinel - 1 <= 28) or pages < sentinel:
        _fail(tag + "_PAGE_BINDING")
    rejected = (
        r"(?im)^!", r"(?i)error", r"(?i)undefined", r"(?i)multiply defined",
        r"(?i)missing character", r"(?i)emergency stop", r"(?i)fatal",
        r"(?i)overfull", r"(?i)rerun", r"(?i)label\(s\) may have changed",
        r"(?i)destination with the same identifier", r"(?i)token not allowed in a pdf string",
        r"(?i)font shape.*substitut", r"(?i)shell[ -]?escape", r"(?i)\\write18.*enabled",
    )
    for pattern in rejected:
        if re.search(pattern, text):
            _fail(tag + "_REJECTED_DIAGNOSTIC")
    warning_lines = []
    warning_bytes = 0
    for line in lines:
        encoded_line = line.encode("utf-8")
        if "warning" not in line.lower() and "underfull" not in line.lower():
            continue
        if "underfull" not in line.lower() or "warning" in line.lower():
            _fail(tag + "_UNCLASSIFIED_WARNING")
        if re.search(r"(?i)(?:at lines? [1-9][0-9]*|while \\output is active)", line) is None:
            _fail(tag + "_UNDERFULL_LOCUS")
        warning_bytes += len(encoded_line) + 1
        if (len(warning_lines) >= MAX_WARNING_LINES or
                warning_bytes > MAX_WARNING_FRAME_BYTES):
            _fail(tag + "_WARNING_LIMIT")
        warning_lines.append(encoded_line)
    warning_frame = b"".join(line + b"\n" for line in warning_lines)
    return (sentinel, pages, len(warning_lines), hashlib.sha256(warning_frame).hexdigest(),
            warning_frame.hex() if warning_frame else "-")


def _validate_aux_and_bbl(aux, bbl, pdf_pages, tag):
    if (len(aux) > 4 * MIB or aux.count(b"\n") > 100000 or
            len(bbl) > 2 * MIB or bbl.count(b"\n") > 50000):
        _fail(tag + "_PREFLIGHT")
    aux_lf = _line_byte_preflight(
        aux, 4 * MIB, 100000, 16 * KIB, True, tag + "_AUX_PREFLIGHT",
    )
    bbl_lf = _line_byte_preflight(
        bbl, 2 * MIB, 50000, 16 * KIB, True, tag + "_BBL_PREFLIGHT",
    )
    aux_text = _strict_text(aux, aux_lf, tag + "_AUX")
    bbl_text = _strict_text(bbl, bbl_lf, tag + "_BBL")
    _validate_aux_surface(aux_text, pdf_pages, tag + "_AUX_SURFACE")
    items = _validate_bbl_surface(bbl_text, tag + "_BBL_SURFACE")
    citations = []
    bibcites = []
    bibdata_count = 0
    bibstyle_count = 0
    for line in _active_tex_lines(aux_text, tag + "_AUX_ACTIVE"):
        stripped = line.strip()
        words = _tex_control_words(line)
        if "^^" in line or any(word in ("csname", "endcsname", "catcode", "let") for word in words):
            _fail(tag + "_AUX_DYNAMIC_CONTROL")
        citation = re.fullmatch(r"\\citation\{([a-z0-9_]+(?:,[a-z0-9_]+)*)\}", stripped)
        if "citation" in words and (words.count("citation") != 1 or citation is None):
            _fail(tag + "_CITATION_GRAMMAR")
        if citation is not None:
            for key_match in re.finditer(r"[a-z0-9_]+", citation.group(1)):
                if len(citations) >= 20:
                    _fail(tag + "_CITATION_CENSUS")
                citations.append(key_match.group(0))
        bibcite = re.fullmatch(
            r"\\bibcite\{([a-z0-9_]+)\}\{([1-9]|1[0-9]|20)\}", stripped,
        )
        if "bibcite" in words and (words.count("bibcite") != 1 or bibcite is None):
            _fail(tag + "_BIBCITE_GRAMMAR")
        if bibcite is not None:
            if len(bibcites) >= 20:
                _fail(tag + "_BIBCITE_CENSUS")
            bibcites.append((bibcite.group(1), bibcite.group(2)))
        bibdata = re.fullmatch(r"\\bibdata\{references\}", stripped)
        if "bibdata" in words and (words.count("bibdata") != 1 or bibdata is None):
            _fail(tag + "_BIBDATA_GRAMMAR")
        if bibdata is not None:
            if bibdata_count:
                _fail(tag + "_BIBDATA_CENSUS")
            bibdata_count += 1
        bibstyle = re.fullmatch(r"\\bibstyle\{plain\}", stripped)
        if "bibstyle" in words and (words.count("bibstyle") != 1 or bibstyle is None):
            _fail(tag + "_BIBSTYLE_GRAMMAR")
        if bibstyle is not None:
            if bibstyle_count:
                _fail(tag + "_BIBSTYLE_CENSUS")
            bibstyle_count += 1
    if len(citations) != 20 or len(set(citations)) != 20 or tuple(sorted(citations)) != EXPECTED_KEYS:
        _fail(tag + "_CITATIONS")
    if bibdata_count != 1 or bibstyle_count != 1:
        _fail(tag + "_AUX_BIB_BINDING")
    if len(items) != 20 or len(set(items)) != 20 or tuple(sorted(items)) != EXPECTED_KEYS:
        _fail(tag + "_ITEMS")
    if (len(bibcites) != 20 or len({key for key, _ in bibcites}) != 20 or
            len({label for _, label in bibcites}) != 20 or
            tuple(sorted(key for key, _ in bibcites)) != EXPECTED_KEYS or
            sorted(label for _, label in bibcites) != sorted(str(number) for number in range(1, 21))):
        _fail(tag + "_BIBCITES")
    labels_by_key = dict(bibcites)
    if any(labels_by_key.get(key) != str(index) for index, key in enumerate(items, 1)):
        _fail(tag + "_BIBCITE_ITEM_ORDER")


def _mode_pdfinfo(args):
    root, pdf_path, stdout_path = args
    if root not in FINAL_MAP or (pdf_path, stdout_path) != (FINAL_MAP[root][4], FINAL_MAP[root][5]):
        _usage("PDFINFO_TUPLE")
    pdf_size, _, pdf_hash = _regular_identity(
        pdf_path, "PDFINFO_PDF", mode=0o600, limit=64 * MIB,
    )
    stdout = _read_receipt_triplet(root, "R060", "pdfinfo", "PDFINFO_RECEIPT")
    if stdout_path != _receipt_paths(root, "R060")[0]:
        _usage("PDFINFO_STDOUT")
    pages, _ = _parse_pdfinfo(stdout, pdf_size, "PDFINFO_PARSE")
    return "root=" + ROOT_CONFIG[root][1] + " pages=" + str(pages) + " bytes=" + str(pdf_size) + " pdf_sha256=" + pdf_hash


def _mode_logbib(args):
    root, log_path, aux_path, bbl_path, blg_path, pdf_path, pdfinfo_path = args
    expected = FINAL_MAP.get(root)
    if expected is None or (log_path, aux_path, bbl_path, blg_path, pdf_path, pdfinfo_path) != expected[:6]:
        _usage("LOGBIB_TUPLE")
    _validate_source_bib_sets()
    log, _, _, log_hash = _read_regular(
        log_path, "LOGBIB_LOG", mode=0o600, limit=8 * MIB,
    )
    aux, _, _, aux_hash = _read_regular(
        aux_path, "LOGBIB_AUX", mode=0o600, limit=4 * MIB,
    )
    bbl, _, _, bbl_hash = _read_regular(
        bbl_path, "LOGBIB_BBL", mode=0o600, limit=2 * MIB,
    )
    blg, _, _, blg_hash = _read_regular(
        blg_path, "LOGBIB_BLG", mode=0o600, limit=512 * KIB,
    )
    pdf_size, _, pdf_hash = _regular_identity(
        pdf_path, "LOGBIB_PDF", mode=0o600, limit=64 * MIB,
    )
    if pdfinfo_path != _receipt_paths(root, "R060")[0]:
        _usage("LOGBIB_PDFINFO_STDOUT")
    pdfinfo = _read_receipt_triplet(
        root, "R060", "pdfinfo", "LOGBIB_PDFINFO_RECEIPT",
    )
    pdf_pages, _ = _parse_pdfinfo(pdfinfo, pdf_size, "LOGBIB_PDFINFO_PARSE")
    sentinel, pages, warnings, warning_hash, warning_hex = _parse_log(log, pdf_size, pdf_pages, "LOGBIB_LOG_PARSE")
    _validate_bibliography_bytes(bbl, blg, "LOGBIB_BIB")
    _validate_aux_and_bbl(aux, bbl, pdf_pages, "LOGBIB_KEYS")
    return ("root=" + ROOT_CONFIG[root][1] + " sentinel=" + str(sentinel) +
            " pages=" + str(pages) + " warnings=" + str(warnings) +
            " warning_sha256=" + warning_hash + " disposition=benign-underfull-only" +
            " warning_bytes_hex=" + warning_hex +
            " log_sha256=" + log_hash + " aux_sha256=" + aux_hash +
            " bbl_sha256=" + bbl_hash + " blg_sha256=" + blg_hash +
            " pdf_sha256=" + pdf_hash)


TEXT_REJECTION_TOKENS = (
    "BATCH07", "B07-", "SOURCE_LOCK", "PUBLICATION_LOCK", "reviewer_role",
    "candidate_id", "/root/", "/home/", "autodl-tmp", "symplectic_map",
    "localhost", "127.0.0.1", "::1",
)


def _collapse(text):
    return re.sub(r"[ \t\n\v\f]+", " ", text).strip(" \t\n\v\f")


def _parse_pdf_text(data, pdf_pages, sentinel, tag):
    _line_byte_preflight(
        data, 8 * MIB, MAX_PDF_TEXT_LINES, MAX_PDF_TEXT_LINE_BYTES,
        False, tag + "_PREFLIGHT",
    )
    if (not data or
            any(value < 0x20 and value not in (0x09, 0x0a, 0x0c)
                for value in data)):
        _fail(tag + "_BYTES")
    terminal_formfeed = data.endswith(b"\f")
    expected_formfeeds = pdf_pages if terminal_formfeed else pdf_pages - 1
    if expected_formfeeds < 0 or data.count(b"\f") != expected_formfeeds:
        _fail(tag + "_FORMFEED_CENSUS")
    try:
        decoded = data.decode("utf-8", "strict")
    except UnicodeDecodeError:
        _fail(tag + "_UTF8")
    if ("\ufffd" in decoded or "\ufeff" in decoded or
            "\u0085" in decoded or "\u2028" in decoded or
            "\u2029" in decoded or
            any(0x7f <= ord(value) <= 0x9f for value in decoded)):
        _fail(tag + "_TEXT_CONTROL")
    pages = ((decoded[:-1] if terminal_formfeed else decoded).split("\f"))
    if len(pages) != pdf_pages:
        _fail(tag + "_PAGE_CENSUS")
    reference_index = None
    for index, page in enumerate(pages, 1):
        first = next(
            (line.strip() for line in page.split("\n") if line.strip()), "",
        )
        if first == "References":
            if reference_index is not None:
                _fail(tag + "_REFERENCE_PAGE_CENSUS")
            reference_index = index
    if reference_index != sentinel:
        _fail(tag + "_REFERENCE_PAGE")
    if any(page.strip() == "" for page in pages[:sentinel - 1]):
        _fail(tag + "_BLANK_PROOF_PAGE")
    page_one = _collapse(pages[0])
    for token in (TITLE, "Anonymous", "Abstract"):
        if token not in page_one:
            _fail(tag + "_PAGE_ONE")
    pre = _collapse("\f".join(pages[:sentinel - 1]))
    cursor = -1
    for heading in HEADINGS:
        position = pre.find(heading, cursor + 1)
        if position < 0:
            _fail(tag + "_HEADING")
        cursor = position
    module_cursor = -1
    for module_anchor in MODULE_ANCHORS:
        position = pre.find(module_anchor, module_cursor + 1)
        if position < 0:
            _fail(tag + "_MODULE_ORDER")
        module_cursor = position
    for token in MODULE_ANCHORS + CLAUSES + FIXTURES + BOUNDARIES + (CONCLUSION,):
        if token not in pre:
            _fail(tag + "_CONTENT")
    suffix = "\f".join(pages[sentinel - 1:])
    for token in HEADINGS + MODULE_ANCHORS + CLAUSES + FIXTURES + BOUNDARIES + (CONCLUSION,):
        if token in suffix:
            _fail(tag + "_POST_SENTINEL_CONTENT")
    label_count = 0
    for label_match in re.finditer(r"(?m)^[ \t]*\[([0-9]+)\]", suffix):
        if (label_count >= 20 or label_match.end() >= len(suffix) or
                suffix[label_match.end()] not in " \t"):
            _fail(tag + "_REFERENCE_LABELS")
        label_count += 1
        if label_match.group(1) != str(label_count):
            _fail(tag + "_REFERENCE_LABELS")
    if label_count != 20:
        _fail(tag + "_REFERENCE_LABELS")
    for token in TEXT_REJECTION_TOKENS:
        if token in decoded:
            _fail(tag + "_PROVENANCE")
    if re.search(r"(?i)(?<![A-Za-z0-9._%+\-])[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}(?![A-Za-z0-9.\-])", decoded):
        _fail(tag + "_EMAIL")
    return len(pages), hashlib.sha256(data).hexdigest(), hashlib.sha256(pre.encode("utf-8")).hexdigest()


def _mode_pdftext(args):
    root, pdfinfo_path, text_path = args
    expected = FINAL_MAP.get(root)
    if expected is None or (pdfinfo_path, text_path) != (expected[5], expected[6]):
        _usage("PDFTEXT_TUPLE")
    pdf_size, _, _ = _regular_identity(
        expected[4], "PDFTEXT_PDF", mode=0o600, limit=64 * MIB,
    )
    pdfinfo = _read_receipt_triplet(root, "R060", "pdfinfo", "PDFTEXT_INFO_RECEIPT")
    text = _read_receipt_triplet(root, "R062", "pdftext", "PDFTEXT_TEXT_RECEIPT")
    pages, _ = _parse_pdfinfo(pdfinfo, pdf_size, "PDFTEXT_INFO_PARSE")
    log, _, _, _ = _read_regular(
        expected[0], "PDFTEXT_LOG", mode=0o600, limit=8 * MIB,
    )
    sentinel, _, _, _, _ = _parse_log(log, pdf_size, pages, "PDFTEXT_LOG_PARSE")
    del log
    text_pages, text_hash, pre_hash = _parse_pdf_text(text, pages, sentinel, "PDFTEXT_PARSE")
    if pdfinfo_path != _receipt_paths(root, "R060")[0] or text_path != _receipt_paths(root, "R062")[0]:
        _usage("PDFTEXT_RECEIPTS")
    return ("root=" + ROOT_CONFIG[root][1] + " pages=" + str(text_pages) +
            " reference_page=" + str(sentinel) + " text_sha256=" + text_hash +
            " pre_reference_sha256=" + pre_hash)


RAW_PDF_REJECTION_TOKENS = (
    b"/JavaScript", b"/JS", b"/Launch", b"/EmbeddedFile", b"/Filespec",
    b"/RichMedia", b"/SubmitForm", b"/ImportData", b"BATCH07", b"B07-",
    b"SOURCE_LOCK", b"PUBLICATION_LOCK", b"reviewer_role", b"candidate_id",
    b"/root/", b"/home/", b"autodl-tmp", b"symplectic_map", b"localhost",
    b"127.0.0.1", b"::1",
)

PDF_ACTION_NAMES = frozenset({
    b"GoTo", b"GoToR", b"GoToE", b"Launch", b"Thread", b"URI",
    b"Sound", b"Movie", b"Hide", b"Named", b"SubmitForm",
    b"ResetForm", b"ImportData", b"JavaScript", b"SetOCGState",
    b"Rendition", b"Trans", b"GoTo3DView",
})
PDF_VALUE_KEYWORDS = frozenset({b"true", b"false", b"null"})
PDF_CATALOG_KEYS = frozenset({b"Type", b"Pages"})
PDF_PAGES_REQUIRED_KEYS = frozenset({b"Type", b"Kids", b"Count"})
PDF_PAGES_OPTIONAL_KEYS = frozenset({
    b"Parent", b"Resources", b"MediaBox", b"Rotate",
})
PDF_PAGE_REQUIRED_KEYS = frozenset({b"Type", b"Parent", b"Contents"})
PDF_PAGE_OPTIONAL_KEYS = frozenset({
    b"Resources", b"MediaBox", b"Rotate",
})
PDF_INFO_KEYS = frozenset({
    b"Title", b"Author", b"Subject", b"Keywords", b"Creator",
    b"Producer", b"CreationDate", b"ModDate", b"Trapped",
    b"PTEX.Fullbanner",
})
PDF_TRADITIONAL_TRAILER_REQUIRED_KEYS = frozenset({b"Size", b"Root"})
PDF_TRADITIONAL_TRAILER_OPTIONAL_KEYS = frozenset({b"Info", b"ID"})
PDF_XREF_STREAM_REQUIRED_KEYS = frozenset({
    b"Type", b"Length", b"Size", b"W", b"Root",
})
PDF_XREF_STREAM_OPTIONAL_KEYS = frozenset({
    b"Filter", b"Index", b"Info", b"ID",
})
PDF_CONTENT_STREAM_REQUIRED_KEYS = frozenset({b"Length"})
PDF_CONTENT_STREAM_OPTIONAL_KEYS = frozenset({b"Filter"})
PDF_FONTFILE_STREAM_REQUIRED_KEYS = frozenset({
    b"Length", b"Length1", b"Length2", b"Length3",
})
PDF_FONTFILE_STREAM_OPTIONAL_KEYS = frozenset({b"Filter"})
PDF_OBJSTM_STREAM_KEYS = frozenset({
    b"Type", b"Length", b"Filter", b"N", b"First",
})
PDF_LAYOUT_BYTES = b"\x00\x09\x0a\x0c\x0d\x20"
PDF_HEADER_RE = re.compile(
    rb"\A%PDF-1\.5(?:\r\n|\n)%[\x80-\xff]{4}(?:\r\n|\n)"
)
PDF_OBJECT_HEADER_RE = re.compile(
    rb"(?m)^([1-9][0-9]{0,5})[ \t]+(0)[ \t]+obj\b",
)
PDF_FORBIDDEN_PAYLOADS = (b"/Encrypt",) + RAW_PDF_REJECTION_TOKENS


def _pdf_layout_only(data, start, end, tag):
    if not 0 <= start <= end <= len(data):
        _fail(tag + "_RANGE")
    for position in range(start, end):
        if data[position] not in PDF_LAYOUT_BYTES:
            return False
    return True


def _pdf_rstrip_layout_end(data, start, end, tag):
    if not 0 <= start <= end <= len(data):
        _fail(tag + "_RANGE")
    while end > start and data[end - 1] in PDF_LAYOUT_BYTES:
        end -= 1
    return end


def _blank_bytearray_span(view, start, end, tag):
    if (not isinstance(view, bytearray) or
            not 0 <= start <= end <= len(view)):
        _fail(tag + "_CONTRACT")
    if start == end:
        return
    block = b" " * min(CHUNK, end - start)
    block_view = memoryview(block)
    position = start
    while position < end:
        width = min(len(block), end - position)
        view[position:position + width] = block_view[:width]
        position += width
    del block_view, block


def _copy_bytearray_range(data, start, end, maximum, tag):
    if (not 0 <= start <= end <= len(data) or
            end - start > maximum):
        _fail(tag + "_RANGE")
    result = bytearray(end - start)
    source = memoryview(data)
    result[:] = source[start:end]
    del source
    return result


def _hex_nibble(value):
    if 0x30 <= value <= 0x39:
        return value - 0x30
    if 0x41 <= value <= 0x46:
        return value - 0x41 + 10
    if 0x61 <= value <= 0x66:
        return value - 0x61 + 10
    return -1


def _literal_string_payload(data, start, limit, maximum, tag):
    if (not 0 <= start < limit <= len(data) or data[start] != 0x28 or
            not isinstance(maximum, int) or maximum < 0):
        _fail(tag + "_CONTRACT")
    output = bytearray()
    position = start + 1
    depth = 1
    escaped_values = {
        0x6e: 0x0a, 0x72: 0x0d, 0x74: 0x09,
        0x62: 0x08, 0x66: 0x0c,
        0x28: 0x28, 0x29: 0x29, 0x5c: 0x5c,
    }
    while position < limit:
        value = data[position]
        if value == 0x5c:
            position += 1
            if position >= limit:
                _fail(tag + "_ESCAPE")
            escaped = data[position]
            if escaped == 0x0d:
                position += 1
                if position < limit and data[position] == 0x0a:
                    position += 1
                continue
            if escaped == 0x0a:
                position += 1
                continue
            if 0x30 <= escaped <= 0x37:
                decoded = 0
                digits = 0
                while (position < limit and digits < 3 and
                       0x30 <= data[position] <= 0x37):
                    decoded = decoded * 8 + data[position] - 0x30
                    position += 1
                    digits += 1
                if decoded > 255:
                    _fail(tag + "_OCTAL_RANGE")
                if len(output) >= maximum:
                    _fail(tag + "_LIMIT")
                output.append(decoded)
                continue
            if len(output) >= maximum:
                _fail(tag + "_LIMIT")
            output.append(escaped_values.get(escaped, escaped))
            position += 1
            continue
        if value == 0x28:
            depth += 1
            if depth > 32:
                _fail(tag + "_DEPTH")
            if len(output) >= maximum:
                _fail(tag + "_LIMIT")
            output.append(value)
            position += 1
            continue
        if value == 0x29:
            depth -= 1
            position += 1
            if depth == 0:
                return bytes(output), position
            if len(output) >= maximum:
                _fail(tag + "_LIMIT")
            output.append(value)
            continue
        if value in (0x0a, 0x0d):
            if len(output) >= maximum:
                _fail(tag + "_LIMIT")
            output.append(0x0a)
            position += 1
            if value == 0x0d and position < limit and data[position] == 0x0a:
                position += 1
            continue
        if len(output) >= maximum:
            _fail(tag + "_LIMIT")
        output.append(value)
        position += 1
    _fail(tag + "_UNTERMINATED")


def _hex_string_payload(data, start, limit, maximum, tag):
    if (not 0 <= start < limit <= len(data) or data[start] != 0x3c or
            (start + 1 < limit and data[start + 1] == 0x3c) or
            not isinstance(maximum, int) or maximum < 0):
        _fail(tag + "_CONTRACT")
    output = bytearray()
    high = None
    position = start + 1
    while position < limit:
        value = data[position]
        if value == 0x3e:
            if high is not None:
                if len(output) >= maximum:
                    _fail(tag + "_LIMIT")
                output.append(high << 4)
            return bytes(output), position + 1
        if value in PDF_LAYOUT_BYTES:
            position += 1
            continue
        nibble = _hex_nibble(value)
        if nibble < 0:
            _fail(tag + "_BYTE")
        if high is None:
            high = nibble
        else:
            if len(output) >= maximum:
                _fail(tag + "_LIMIT")
            output.append((high << 4) | nibble)
            high = None
        position += 1
    _fail(tag + "_UNTERMINATED")


def _pdf_name_payload(data, start, limit, tag):
    delimiters = b"()<>[]{}/%"
    if not 0 <= start < limit <= len(data) or data[start] != 0x2f:
        _fail(tag + "_CONTRACT")
    output = bytearray()
    position = start + 1
    while (position < limit and data[position] not in PDF_LAYOUT_BYTES and
           data[position] not in delimiters):
        value = data[position]
        if value == 0x23:
            if position + 2 >= limit:
                _fail(tag + "_ESCAPE")
            high = _hex_nibble(data[position + 1])
            low = _hex_nibble(data[position + 2])
            if high < 0 or low < 0:
                _fail(tag + "_ESCAPE")
            value = (high << 4) | low
            position += 3
        else:
            position += 1
        if len(output) >= MAX_PDF_TOKEN_BYTES:
            _fail(tag + "_LIMIT")
        output.append(value)
    if not output:
        _fail(tag + "_EMPTY")
    return bytes(output), position


def _reject_forbidden_payload(payload, tag):
    for token in PDF_FORBIDDEN_PAYLOADS:
        if token in payload:
            _fail(tag + "_FORBIDDEN")


def _reject_pdf_semantic_tokens(data, tag, start=0, stop=None):
    limit = len(data) if stop is None else stop
    if not 0 <= start <= limit <= len(data):
        _fail(tag + "_RANGE")
    for token in PDF_FORBIDDEN_PAYLOADS:
        if data.find(token, start, limit) >= 0:
            _fail(tag + "_RAW_FORBIDDEN")
    position = start
    while position < limit:
        value = data[position]
        if value == 0x25:
            position += 1
            while position < limit and data[position] not in (0x0a, 0x0d):
                position += 1
            continue
        if value == 0x28:
            payload, position = _literal_string_payload(
                data, position, limit, MAX_PDF_STRING_BYTES,
                tag + "_LITERAL",
            )
            _reject_forbidden_payload(payload, tag + "_LITERAL")
            del payload
            continue
        if value == 0x3c:
            if position + 1 < limit and data[position + 1] == 0x3c:
                position += 2
                continue
            payload, position = _hex_string_payload(
                data, position, limit, MAX_PDF_STRING_BYTES,
                tag + "_HEX",
            )
            _reject_forbidden_payload(payload, tag + "_HEX")
            del payload
            continue
        if value == 0x2f:
            payload, position = _pdf_name_payload(
                data, position, limit, tag + "_NAME",
            )
            _reject_forbidden_payload(b"/" + payload, tag + "_NAME")
            del payload
            continue
        position += 1


def _content_security_scan(data, budget, tag, start=0, stop=None):
    limit = len(data) if stop is None else stop
    if (not 0 <= start <= limit <= len(data) or
            not isinstance(budget, dict) or
            set(budget) != {"decoded_bytes", "tokens"} or
            any(not isinstance(value, int) or value < 0
                for value in budget.values())):
        _fail(tag + "_CONTRACT")
    for token in PDF_FORBIDDEN_PAYLOADS:
        if data.find(token, start, limit) >= 0:
            _fail(tag + "_RAW_FORBIDDEN")
    delimiters = b"()<>[]{}/%"
    maximum_tail = max(len(token) for token in PDF_FORBIDDEN_PAYLOADS) - 1
    containers = []
    pending_tj_hit = False
    position = start

    def take_token():
        if budget["tokens"] <= 0:
            _fail(tag + "_TOKEN_BUDGET")
        budget["tokens"] -= 1

    def consume_pending(is_tj=False):
        nonlocal pending_tj_hit
        if pending_tj_hit and is_tj:
            _fail(tag + "_TJ_FORBIDDEN")
        pending_tj_hit = False

    def add_array_string(payload):
        if not containers or containers[-1][0] != "array":
            return
        state = containers[-1]
        joined = state[1] + payload
        if any(token in joined for token in PDF_FORBIDDEN_PAYLOADS):
            state[2] = True
        state[1] = joined[-maximum_tail:] if maximum_tail else b""

    while position < limit:
        value = data[position]
        if value in PDF_LAYOUT_BYTES:
            position += 1
            continue
        if value == 0x25:
            position += 1
            while position < limit and data[position] not in (0x0a, 0x0d):
                position += 1
            continue
        take_token()
        if value == 0x28:
            consume_pending()
            payload, position = _literal_string_payload(
                data, position, limit, MAX_PDF_STRING_BYTES,
                tag + "_LITERAL",
            )
            _reject_forbidden_payload(payload, tag + "_LITERAL")
            add_array_string(payload)
            del payload
            continue
        if value == 0x3c:
            if position + 1 < limit and data[position + 1] == 0x3c:
                consume_pending()
                if len(containers) >= 64:
                    _fail(tag + "_NESTING")
                containers.append(["dict", b"", False])
                position += 2
                continue
            consume_pending()
            payload, position = _hex_string_payload(
                data, position, limit, MAX_PDF_STRING_BYTES,
                tag + "_HEX",
            )
            _reject_forbidden_payload(payload, tag + "_HEX")
            add_array_string(payload)
            del payload
            continue
        if value == 0x3e:
            consume_pending()
            if (not data.startswith(b">>", position, limit) or
                    not containers or containers[-1][0] != "dict"):
                _fail(tag + "_DICTIONARY_CLOSE")
            containers.pop()
            position += 2
            continue
        if value == 0x5b:
            consume_pending()
            if len(containers) >= 64:
                _fail(tag + "_NESTING")
            containers.append(["array", b"", False])
            position += 1
            continue
        if value == 0x5d:
            consume_pending()
            if not containers or containers[-1][0] != "array":
                _fail(tag + "_ARRAY_CLOSE")
            state = containers.pop()
            pending_tj_hit = state[2] if not containers else False
            del state
            position += 1
            continue
        if value == 0x2f:
            consume_pending()
            payload, position = _pdf_name_payload(
                data, position, limit, tag + "_NAME",
            )
            _reject_forbidden_payload(b"/" + payload, tag + "_NAME")
            del payload
            continue
        if value in b")/%":
            _fail(tag + "_DELIMITER")
        token_start = position
        while (position < limit and data[position] not in PDF_LAYOUT_BYTES and
               data[position] not in delimiters):
            position += 1
            if position - token_start > MAX_PDF_TOKEN_BYTES:
                _fail(tag + "_TOKEN_LIMIT")
        if token_start == position:
            _fail(tag + "_TOKEN")
        raw = bytes(data[token_start:position])
        if not containers and raw == b"BI":
            _fail(tag + "_INLINE_IMAGE")
        consume_pending(raw == b"TJ" and not containers)
    if containers:
        _fail(tag + "_NESTING_CLOSURE")


def _scan_pdf_raw_excluding(data, excluded, tag):
    ranges = tuple(sorted(excluded))
    cursor = 0
    eof_count = 0
    eof_position = -1
    for index in range(len(ranges) + 1):
        end = ranges[index][0] if index < len(ranges) else len(data)
        if not 0 <= cursor <= end <= len(data):
            _fail(tag + "_RANGE")
        for token in PDF_FORBIDDEN_PAYLOADS:
            if data.find(token, cursor, end) >= 0:
                _fail(tag + "_FORBIDDEN")
        position = data.find(b"%%EOF", cursor, end)
        while position >= 0:
            eof_count += 1
            eof_position = position
            if eof_count > 1:
                _fail(tag + "_EOF_CENSUS")
            position = data.find(b"%%EOF", position + 1, end)
        if index < len(ranges):
            range_start, range_end = ranges[index]
            if not end == range_start <= range_end <= len(data):
                _fail(tag + "_RANGE")
            cursor = range_end
    return eof_count, eof_position


def _pdf_hex_string_end(data, position, tag, stop=None):
    limit = len(data) if stop is None else stop
    if (not 0 <= position < limit <= len(data) or
            data[position] != 0x3c):
        _fail(tag + "_OPEN")
    start = position
    position += 1
    while position < limit and data[position] != 0x3e:
        if (data[position] not in b"\x00\x09\x0a\x0c\x0d\x20" and
                data[position] not in b"0123456789abcdefABCDEF"):
            _fail(tag + "_BYTE")
        position += 1
        if position - start > 4 * MAX_PDF_STRING_BYTES:
            _fail(tag + "_LIMIT")
    if position >= limit:
        _fail(tag + "_UNTERMINATED")
    return position + 1


def _pdf_eol_end(data, position, tag):
    if data.startswith(b"\r\n", position):
        return position + 2
    if position < len(data) and data[position] == 0x0a:
        return position + 1
    _fail(tag + "_EOL")


def _pdf_structural_view(data, tag, start=0, stop=None):
    whitespace = b"\x00\x09\x0a\x0c\x0d\x20"
    delimiters = b"()<>[]{}/%"
    limit = len(data) if stop is None else stop
    if not 0 <= start <= limit <= len(data):
        _fail(tag + "_RANGE")
    view = data if isinstance(data, bytearray) else bytearray(data)
    position = start
    while position < limit:
        value = data[position]
        if value == 0x25:
            token_start = position
            position += 1
            while position < limit and data[position] not in (0x0a, 0x0d):
                position += 1
            _blank_bytearray_span(
                view, token_start, position, tag + "_COMMENT",
            )
            continue
        if value == 0x28:
            token_start = position
            position += 1
            depth = 1
            while position < limit and depth:
                current = data[position]
                if current == 0x5c:
                    position += 1
                    if position < limit and data[position] == 0x0d:
                        position += 1
                        if position < limit and data[position] == 0x0a:
                            position += 1
                    elif position < limit:
                        position += 1
                    continue
                if current == 0x28:
                    depth += 1
                elif current == 0x29:
                    depth -= 1
                position += 1
                if position - token_start > 4 * MAX_PDF_STRING_BYTES:
                    _fail(tag + "_LITERAL_STRING_LIMIT")
            if depth:
                _fail(tag + "_LITERAL_STRING")
            _blank_bytearray_span(
                view, token_start, position, tag + "_LITERAL",
            )
            view[token_start] = 0x28
            view[position - 1] = 0x29
            continue
        if value == 0x3c:
            if position + 1 < limit and data[position + 1] == 0x3c:
                position += 2
                continue
            token_start = position
            position = _pdf_hex_string_end(
                data, position, tag + "_HEX_STRING", limit,
            )
            _blank_bytearray_span(
                view, token_start, position, tag + "_HEX",
            )
            view[token_start] = 0x28
            view[position - 1] = 0x29
            continue
        if value == 0x2f:
            position += 1
            token_start = position
            while (position < limit and data[position] not in whitespace and
                   data[position] not in delimiters):
                position += 1
            if position - token_start > MAX_PDF_TOKEN_BYTES:
                _fail(tag + "_NAME_LIMIT")
            if token_start == position:
                _fail(tag + "_EMPTY_NAME")
            if data.find(b"#", token_start, position) >= 0:
                _fail(tag + "_NAME_ESCAPE")
            continue
        position += 1
    return view


def _reject_pdf_name_escapes(data, tag):
    _pdf_structural_view(data, tag)


def _pdf_tokens(data, tag, aggregate_budget=None, start=0, stop=None):
    whitespace = b"\x00\x09\x0a\x0c\x0d\x20"
    delimiters = b"()<>[]{}/%"
    limit = len(data) if stop is None else stop
    if not 0 <= start <= limit <= len(data):
        _fail(tag + "_RANGE")
    tokens = []
    position = start
    while position < limit:
        if data[position] in whitespace:
            position += 1
            continue
        if (len(tokens) >= MAX_PDF_TOKENS or
                (aggregate_budget is not None and aggregate_budget[0] <= 0)):
            _fail(tag + "_TOKEN_LIMIT")
        if aggregate_budget is not None:
            aggregate_budget[0] -= 1
        if data.startswith(b"<<", position, limit):
            tokens.append(("dict_start", b"<<"))
            position += 2
        elif data.startswith(b">>", position, limit):
            tokens.append(("dict_end", b">>"))
            position += 2
        elif data[position] == 0x5b:
            tokens.append(("array_start", b"["))
            position += 1
        elif data[position] == 0x5d:
            tokens.append(("array_end", b"]"))
            position += 1
        elif data[position] == 0x2f:
            position += 1
            token_start = position
            while (position < limit and data[position] not in whitespace and
                   data[position] not in delimiters):
                position += 1
            if (token_start == position or
                    position - token_start > MAX_PDF_TOKEN_BYTES):
                _fail(tag + "_EMPTY_NAME")
            tokens.append(("name", bytes(data[token_start:position])))
        elif data[position] == 0x28:
            position += 1
            while position < limit and data[position] != 0x29:
                if data[position] != 0x20:
                    _fail(tag + "_STRING_PLACEHOLDER")
                position += 1
            if position >= limit:
                _fail(tag + "_STRING_PLACEHOLDER_END")
            tokens.append(("string", b"()"))
            position += 1
        elif data[position] in b"()<>/%":
            _fail(tag + "_DELIMITER")
        else:
            token_start = position
            while (position < limit and data[position] not in whitespace and
                   data[position] not in delimiters):
                position += 1
            if (token_start == position or
                    position - token_start > MAX_PDF_TOKEN_BYTES):
                _fail(tag + "_TOKEN")
            tokens.append(("atom", bytes(data[token_start:position])))
    return tuple(tokens)


def _pdf_document_keyword_census(data, tag):
    """Count structural obj/endobj atoms without materializing tokens."""
    whitespace = b"\x00\x09\x0a\x0c\x0d\x20"
    delimiters = b"()<>[]{}/%"
    position = 0
    token_count = 0
    object_count = 0
    endobject_count = 0
    while position < len(data):
        if data[position] in whitespace:
            position += 1
            continue
        token_count += 1
        if token_count > MAX_PDF_TOKENS:
            _fail(tag + "_TOKEN_LIMIT")
        if data.startswith(b"<<", position):
            position += 2
            continue
        if data.startswith(b">>", position):
            position += 2
            continue
        if data[position] in (0x5b, 0x5d):
            position += 1
            continue
        if data[position] == 0x2f:
            position += 1
            token_start = position
            while (position < len(data) and
                   data[position] not in whitespace and
                   data[position] not in delimiters):
                position += 1
            if (token_start == position or
                    position - token_start > MAX_PDF_TOKEN_BYTES):
                _fail(tag + "_EMPTY_NAME")
            continue
        if data[position] == 0x28:
            position += 1
            while position < len(data) and data[position] != 0x29:
                if data[position] != 0x20:
                    _fail(tag + "_STRING_PLACEHOLDER")
                position += 1
            if position >= len(data):
                _fail(tag + "_STRING_PLACEHOLDER_END")
            position += 1
            continue
        if data[position] in b"()<>/%":
            _fail(tag + "_DELIMITER")
        token_start = position
        while (position < len(data) and data[position] not in whitespace and
               data[position] not in delimiters):
            position += 1
        if (token_start == position or
                position - token_start > MAX_PDF_TOKEN_BYTES):
            _fail(tag + "_TOKEN")
        width = position - token_start
        if width == 3 and data.startswith(b"obj", token_start, position):
            object_count += 1
        elif (width == 6 and
              data.startswith(b"endobj", token_start, position)):
            endobject_count += 1
    return object_count, endobject_count


def _parse_pdf_value(tokens, index, depth, tag):
    if depth > 64 or index >= len(tokens):
        _fail(tag + "_VALUE")
    kind, raw = tokens[index]
    if kind == "dict_start":
        values = {}
        index += 1
        while index < len(tokens) and tokens[index][0] != "dict_end":
            if tokens[index][0] != "name":
                _fail(tag + "_DICTIONARY_KEY")
            key = tokens[index][1]
            if key in values:
                _fail(tag + "_DICTIONARY_DUPLICATE")
            value, index = _parse_pdf_value(tokens, index + 1, depth + 1, tag)
            values[key] = value
        if index >= len(tokens) or tokens[index][0] != "dict_end":
            _fail(tag + "_DICTIONARY_END")
        return ("dict", values), index + 1
    if kind == "array_start":
        values = []
        index += 1
        while index < len(tokens) and tokens[index][0] != "array_end":
            value, index = _parse_pdf_value(tokens, index, depth + 1, tag)
            values.append(value)
        if index >= len(tokens) or tokens[index][0] != "array_end":
            _fail(tag + "_ARRAY_END")
        return ("array", tuple(values)), index + 1
    if kind in ("dict_end", "array_end"):
        _fail(tag + "_UNEXPECTED_END")
    if kind == "name":
        return ("name", raw), index + 1
    if kind == "string":
        return ("string",), index + 1
    if (kind == "atom" and re.fullmatch(rb"0|[1-9][0-9]*", raw) and
            index + 2 < len(tokens) and tokens[index + 1][0] == "atom" and
            re.fullmatch(rb"0|[1-9][0-9]*", tokens[index + 1][1]) and
            tokens[index + 2] == ("atom", b"R")):
        return (
            "ref",
            _bounded_decimal(raw, tag + "_REF_OBJECT", MAX_PDF_OBJECTS),
            _bounded_decimal(
                tokens[index + 1][1], tag + "_REF_GENERATION", 65535,
            ),
        ), index + 3
    if kind == "atom" and re.fullmatch(rb"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)", raw):
        return ("number", raw), index + 1
    if kind == "atom" and raw in PDF_VALUE_KEYWORDS:
        return ("keyword", raw), index + 1
    if kind == "atom":
        _fail(tag + "_OBJECT_KEYWORD")
    _fail(tag + "_TOKEN_KIND")


def _parse_pdf_object(data, tag, aggregate_budget=None, start=0, stop=None):
    tokens = _pdf_tokens(
        data, tag + "_TOKENS", aggregate_budget, start, stop,
    )
    if not tokens:
        _fail(tag + "_EMPTY_OBJECT")
    value, index = _parse_pdf_value(tokens, 0, 0, tag)
    if index == len(tokens):
        return value, False
    if (value[0] == "dict" and tokens[index:] ==
            (("atom", b"stream"), ("atom", b"endstream"))):
        return value, True
    _fail(tag + "_TRAILING_OBJECT")


def _pdf_dictionary(value, tag):
    if value[0] != "dict":
        _fail(tag + "_DICTIONARY")
    return value[1]


def _pdf_closed_dictionary(value, required, optional, tag):
    dictionary = _pdf_dictionary(value, tag)
    allowed = required | optional
    if (len(dictionary) > len(allowed) or
            any(key not in dictionary for key in required) or
            any(key not in allowed for key in dictionary)):
        _fail(tag + "_KEY_SET")
    return dictionary


def _pdf_name_value(value, tag):
    if value is None or value[0] != "name":
        _fail(tag + "_NAME")
    return value[1]


def _pdf_ref_value(value, tag):
    if value is None or value[0] != "ref" or value[2] != 0 or value[1] <= 0:
        _fail(tag + "_REF")
    return value[1]


def _pdf_integer_value(value, tag, positive=False, maximum=MAX_DYNAMIC_BYTES):
    if (value is None or value[0] != "number" or
            re.fullmatch(rb"0|[1-9][0-9]*", value[1]) is None):
        _fail(tag + "_INTEGER")
    result = _bounded_decimal(value[1], tag, maximum, positive=positive)
    if positive and result <= 0:
        _fail(tag + "_POSITIVE")
    return result


def _pdf_ref_array_value(value, tag):
    if (value is None or value[0] != "array" or not value[1] or
            len(value[1]) > MAX_PDF_OBJECTS):
        _fail(tag + "_REF_ARRAY")
    refs = []
    seen = set()
    for item in value[1]:
        reference = _pdf_ref_value(item, tag)
        if reference in seen:
            _fail(tag + "_REF_ARRAY_DUPLICATE")
        seen.add(reference)
        refs.append(reference)
    return tuple(refs)


def _next_pdf_stream(data, start, tag):
    position = start
    last_header = None
    while position < len(data):
        value = data[position]
        if value == 0x25:
            position += 1
            while position < len(data) and data[position] not in (0x0a, 0x0d):
                position += 1
            continue
        if value == 0x28:
            string_start = position
            position += 1
            depth = 1
            while position < len(data) and depth:
                current = data[position]
                if current == 0x5c:
                    position += 1
                    if position < len(data) and data[position] == 0x0d:
                        position += 1
                        if position < len(data) and data[position] == 0x0a:
                            position += 1
                    elif position < len(data):
                        position += 1
                    continue
                if current == 0x28:
                    depth += 1
                elif current == 0x29:
                    depth -= 1
                position += 1
                if position - string_start > 4 * MAX_PDF_STRING_BYTES:
                    _fail(tag + "_LITERAL_STRING_LIMIT")
            if depth:
                _fail(tag + "_LITERAL_STRING")
            continue
        if value == 0x3c and data.startswith(b"<<", position):
            position += 2
            continue
        if value == 0x3c:
            position = _pdf_hex_string_end(data, position, tag + "_HEX_STRING")
            continue
        line_start = position == 0 or data[position - 1] == 0x0a
        if line_start:
            header = PDF_OBJECT_HEADER_RE.match(data, position, len(data))
            if header is not None:
                last_header = (
                    header.start(), header.end(),
                    header.group(1), header.group(2),
                )
                position = header.end()
                continue
        if (line_start and data.startswith(b"stream", position) and
                position + 6 < len(data) and data[position + 6] in (0x0a, 0x0d)):
            if last_header is None:
                _fail(tag + "_STREAM_HEADER")
            return last_header + (
                position,
                _pdf_eol_end(data, position + 6, tag + "_STREAM_START"),
            )
        position += 1
    return None


def _bounded_regex_rows(pattern, data, maximum, tag, start=0, stop=None):
    limit = len(data) if stop is None else stop
    if not 0 <= start <= limit <= len(data):
        _fail(tag + "_RANGE")
    rows = []
    for row in pattern.finditer(data, start, limit):
        if len(rows) >= maximum:
            _fail(tag + "_LIMIT")
        rows.append(row)
    return tuple(rows)


def _stream_spans(data, aggregate_budget, tag):
    spans = []
    seen_stream_ids = set()
    position = 0
    while True:
        located = _next_pdf_stream(data, position, tag + "_LEX")
        if located is None:
            break
        (header_start, header_end, object_raw, generation_raw,
         stream_start, payload_start) = located
        if (generation_raw != b"0" or
                stream_start - header_end > MAX_PDF_STREAM_DICTIONARY_BYTES):
            _fail(tag + "_STREAM_HEADER")
        _reject_pdf_semantic_tokens(
            data, tag + "_PREFIX_SECURITY", header_end, stream_start,
        )
        structural_prefix = _copy_bytearray_range(
            data, header_end, stream_start, MAX_PDF_STREAM_DICTIONARY_BYTES,
            tag + "_PREFIX_COPY",
        )
        _pdf_structural_view(structural_prefix, tag + "_PREFIX_NAMES")
        prefix_value, prefix_is_stream = _parse_pdf_object(
            structural_prefix, tag + "_STREAM_DICTIONARY", aggregate_budget,
        )
        del structural_prefix
        if prefix_is_stream:
            _fail(tag + "_STREAM_PREFIX")
        dictionary = _pdf_dictionary(prefix_value, tag + "_STREAM_DICTIONARY")
        length = _pdf_integer_value(
            dictionary.get(b"Length"), tag + "_STREAM_LENGTH",
        )
        start = payload_start
        end = start + length
        if end > len(data):
            _fail(tag + "_STREAM_BOUNDS")
        ending_start = _pdf_eol_end(data, end, tag + "_ENDSTREAM_PREFIX")
        ending_end = ending_start + len(b"endstream")
        if (not data.startswith(b"endstream", ending_start) or
                (ending_end < len(data) and
                 data[ending_end] not in b"\x00\x09\x0a\x0c\x0d\x20()<>[]{}/%")):
            _fail(tag + "_ENDSTREAM")
        object_number = _bounded_decimal(
            object_raw, tag + "_STREAM_OBJECT_NUMBER",
            MAX_PDF_OBJECTS, positive=True,
        )
        if object_number in seen_stream_ids:
            _fail(tag + "_DUPLICATE_STREAM_OBJECT")
        if len(spans) >= MAX_PDF_OBJECTS:
            _fail(tag + "_STREAM_OBJECT_LIMIT")
        seen_stream_ids.add(object_number)
        spans.append((
            object_number, start, end, prefix_value,
            header_start, header_end, stream_start, ending_end,
        ))
        position = ending_end
    return tuple(spans)


def _bounded_flate(data, tag, output_limit=MAX_OBJECT_STREAM_BYTES):
    if (not isinstance(output_limit, int) or
            not 0 <= output_limit <= MAX_OBJECT_STREAM_BYTES):
        _fail(tag + "_OUTPUT_LIMIT_CONTRACT")
    decoder = zlib.decompressobj()
    source = memoryview(data)
    output = bytearray()
    input_position = 0
    pending = None
    try:
        while True:
            if pending is None:
                if input_position < len(source):
                    input_end = min(input_position + CHUNK, len(source))
                    pending = source[input_position:input_end]
                    input_position = input_end
                else:
                    pending = b""
            pending_before = len(pending)
            room = output_limit - len(output)
            piece = decoder.decompress(pending, min(CHUNK, room + 1))
            tail = decoder.unconsumed_tail
            if len(piece) > room:
                _fail(tag + "_DECOMPRESS_LIMIT")
            output.extend(piece)
            if decoder.eof:
                if (decoder.unused_data or tail or
                        input_position != len(source)):
                    _fail(tag + "_DECOMPRESS_TRAILING")
                return output
            if tail:
                if len(tail) >= pending_before and not piece:
                    _fail(tag + "_DECOMPRESS_PROGRESS")
                pending = tail
            else:
                pending = None
                if pending_before == 0 and not piece:
                    _fail(tag + "_DECOMPRESS_TRUNCATED")
    except zlib.error:
        _fail(tag + "_DECOMPRESS")
    finally:
        pending = None
        source.release()


def _pdf_decimal_fields(data, expected, tag, start=0, stop=None):
    whitespace = b"\x00\x09\x0a\x0c\x0d\x20"
    limit = len(data) if stop is None else stop
    if not 0 <= start <= limit <= len(data):
        _fail(tag + "_RANGE")
    fields = []
    position = start
    while position < limit:
        while position < limit and data[position] in whitespace:
            position += 1
        if position == limit:
            break
        field_start = position
        while position < limit and 0x30 <= data[position] <= 0x39:
            position += 1
        if (field_start == position or position - field_start > 10 or
                (position < limit and data[position] not in whitespace)):
            _fail(tag + "_GRAMMAR")
        fields.append(bytes(memoryview(data)[field_start:position]))
        if len(fields) > expected:
            _fail(tag + "_COUNT")
    if len(fields) != expected:
        _fail(tag + "_COUNT")
    return tuple(fields)


def _pdf_objects(data, spans, aggregate_budget, tag):
    structural_pdf = bytearray(data)
    for row in spans:
        _blank_bytearray_span(
            structural_pdf, row[1], row[2], tag + "_STREAM_MASK",
        )
    _pdf_structural_view(structural_pdf, tag + "_NAMES")
    headers = _bounded_regex_rows(
        PDF_OBJECT_HEADER_RE, structural_pdf, MAX_PDF_OBJECTS,
        tag + "_OBJECT_HEADERS",
    )
    if any(re.fullmatch(rb"[1-9][0-9]*", header.group(1)) is None or
           header.group(2) != b"0" for header in headers):
        _fail(tag + "_OBJECT_HEADER_GRAMMAR")
    object_count, endobject_count = _pdf_document_keyword_census(
        structural_pdf, tag + "_DOCUMENT_TOKENS",
    )
    if object_count != len(headers) or endobject_count != len(headers):
        _fail(tag + "_OBJECT_KEYWORD_CENSUS")
    del object_count, endobject_count
    body_extents = {}
    parsed_objects = {}
    direct_offsets = {}
    direct_extents = {}
    endobj_re = re.compile(rb"(?m)^endobj[ \t]*(?:\r\n|\n)")
    endings = ()
    for index, header in enumerate(headers):
        stop = headers[index + 1].start() if index + 1 < len(headers) else len(structural_pdf)
        endings = _bounded_regex_rows(
            endobj_re, structural_pdf, 2, tag + "_ENDOBJ_ROWS",
            start=header.end(), stop=stop,
        )
        if len(endings) != 1:
            _fail(tag + "_ENDOBJ")
        end = endings[0].start()
        extent_end = endings[0].end()
        number = _bounded_decimal(
            header.group(1), tag + "_OBJECT_NUMBER", MAX_PDF_OBJECTS,
            positive=True,
        )
        if number in body_extents:
            _fail(tag + "_DUPLICATE_OBJECT")
        body_extents[number] = (header.end(), end)
        direct_offsets[number] = header.start()
        direct_extents[number] = (header.start(), extent_end)
    ordered_extents = sorted(direct_extents.values())
    for previous, following in zip(ordered_extents, ordered_extents[1:]):
        if (previous[1] > following[0] or not _pdf_layout_only(
                data, previous[1], following[0], tag + "_DIRECT_OBJECT_GAP")):
            _fail(tag + "_DIRECT_OBJECT_GAP")
    del headers, endings, ordered_extents, endobj_re
    span_map = {
        row[0]: (row[1], row[2], row[3]) for row in spans
    }
    stream_frames = {
        row[0]: (row[4], row[5], row[6], row[7]) for row in spans
    }
    if (set(span_map) != set(stream_frames) or
            not set(span_map).issubset(body_extents)):
        _fail(tag + "_STREAM_OBJECT_BINDING")
    for number in sorted(body_extents):
        body_start, body_end = body_extents[number]
        if number in span_map:
            (header_start, header_end, stream_start,
             endstream_end) = stream_frames[number]
            payload_start, payload_end, value = span_map[number]
            if (direct_offsets[number] != header_start or
                    body_start != header_end or
                    not body_start <= stream_start < payload_start <=
                    payload_end < endstream_end <= body_end or
                    not data.startswith(b"stream", stream_start, payload_start) or
                    not data.startswith(
                        b"endstream", endstream_end - len(b"endstream"),
                        endstream_end,
                    ) or not _pdf_layout_only(
                        data, endstream_end, body_end,
                        tag + "_STREAM_END_GAP",
                    )):
                _fail(tag + "_DIRECT_STREAM_FRAME")
        else:
            _reject_pdf_semantic_tokens(
                data, tag + "_DIRECT_SECURITY_%d" % number,
                body_start, body_end,
            )
            value, is_stream = _parse_pdf_object(
                structural_pdf, tag + "_DIRECT_OBJECT_%d" % number,
                aggregate_budget, body_start, body_end,
            )
            if is_stream:
                _fail(tag + "_DIRECT_STREAM_BINDING")
        parsed_objects[number] = value
    del body_extents, stream_frames
    total_decompressed = 0
    parsed_additions = {}
    compressed_locations = {}
    for number in sorted(parsed_objects):
        value = parsed_objects[number]
        if value[0] != "dict":
            continue
        dictionary = value[1]
        type_value = dictionary.get(b"Type")
        if type_value != ("name", b"ObjStm"):
            continue
        if dictionary.get(b"Filter") != ("name", b"FlateDecode"):
            _fail(tag + "_OBJSTM_FILTER")
        if b"DecodeParms" in dictionary or b"Extends" in dictionary or number not in span_map:
            _fail(tag + "_OBJSTM_HEADER")
        raw_start, raw_end, _ = span_map[number]
        remaining_total = MAX_TOTAL_OBJECT_STREAM_BYTES - total_decompressed
        decoded = _bounded_flate(
            memoryview(data)[raw_start:raw_end], tag + "_OBJSTM",
            min(MAX_OBJECT_STREAM_BYTES, remaining_total),
        )
        total_decompressed += len(decoded)
        if total_decompressed > MAX_TOTAL_OBJECT_STREAM_BYTES:
            _fail(tag + "_OBJSTM_TOTAL_LIMIT")
        count = _pdf_integer_value(
            dictionary.get(b"N"), tag + "_OBJSTM_N", positive=True,
            maximum=MAX_PDF_OBJECTS,
        )
        first = _pdf_integer_value(
            dictionary.get(b"First"), tag + "_OBJSTM_FIRST", positive=True,
        )
        if first > len(decoded):
            _fail(tag + "_OBJSTM_FIRST")
        header_numbers = _pdf_decimal_fields(
            decoded, 2 * count, tag + "_OBJSTM_INDEX", stop=first,
        )
        if any(re.fullmatch(rb"0|[1-9][0-9]*", value) is None
               for value in header_numbers):
            _fail(tag + "_OBJSTM_INDEX")
        pairs = [
            (
                _bounded_decimal(
                    header_numbers[2 * i], tag + "_OBJSTM_OBJECT_ID",
                    MAX_PDF_OBJECTS, positive=True,
                ),
                _bounded_decimal(
                    header_numbers[2 * i + 1], tag + "_OBJSTM_OFFSET",
                    len(decoded),
                ),
            )
            for i in range(count)
        ]
        del header_numbers
        if any(object_id <= 0 for object_id, _ in pairs):
            _fail(tag + "_OBJSTM_OBJECT_ID")
        offsets = [offset for _, offset in pairs]
        if not offsets or offsets[0] != 0 or offsets != sorted(offsets) or len(set(offsets)) != len(offsets):
            _fail(tag + "_OBJSTM_OFFSETS")
        payload_length = len(decoded) - first
        for index, (object_id, offset) in enumerate(pairs):
            end_offset = (
                offsets[index + 1]
                if index + 1 < len(offsets) else payload_length
            )
            if (offset >= end_offset or end_offset > payload_length or
                    object_id in parsed_objects or
                    object_id in parsed_additions):
                _fail(tag + "_OBJSTM_OBJECT")
            member_start = first + offset
            member_end = first + end_offset
            _reject_pdf_semantic_tokens(
                decoded, tag + "_OBJSTM_SECURITY",
                member_start, member_end,
            )
            _pdf_structural_view(
                decoded, tag + "_OBJSTM_NAMES", member_start, member_end,
            )
            object_value, is_stream = _parse_pdf_object(
                decoded, tag + "_COMPRESSED_OBJECT_%d" % object_id,
                aggregate_budget, member_start, member_end,
            )
            if is_stream:
                _fail(tag + "_COMPRESSED_STREAM")
            parsed_additions[object_id] = object_value
            compressed_locations[object_id] = (number, index)
            del member_start, member_end, object_value
        del decoded, payload_length, pairs, offsets
    parsed_objects.update(parsed_additions)
    if any(
        value[0] == "dict" and value[1].get(b"Type") == ("name", b"ObjStm")
        for value in parsed_additions.values()
    ):
        _fail(tag + "_COMPRESSED_OBJSTM")
    return (parsed_objects, span_map, structural_pdf, compressed_locations,
            direct_offsets, direct_extents)


def _pdf_exact_number(value, tag):
    if (len(value) > 64 or
            not re.fullmatch(rb"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)", value)):
        _fail(tag + "_NUMBER")
    negative = value.startswith(b"-")
    unsigned = value[1:] if value[:1] in (b"+", b"-") else value
    if b"." in unsigned:
        whole, fraction = unsigned.split(b".", 1)
    else:
        whole, fraction = unsigned, b""
    numerator = int((whole or b"0") + fraction)
    if negative:
        numerator = -numerator
    denominator = 10 ** len(fraction)
    common = math.gcd(abs(numerator), denominator)
    return numerator // common, denominator // common


def _pdf_exact_number_value(value, tag):
    if value is None or value[0] != "number":
        _fail(tag + "_NUMBER_VALUE")
    return _pdf_exact_number(value[1], tag)


def _pdf_top_name(value, key):
    if value[0] != "dict":
        return None
    item = value[1].get(key)
    return item[1] if item is not None and item[0] == "name" else None


def _collect_pdf_refs(value, counts, tag, depth=0):
    if depth > 64:
        _fail(tag + "_REF_DEPTH")
    kind = value[0]
    if kind == "ref":
        if value[1] <= 0 or value[2] != 0:
            _fail(tag + "_REFERENCE_GENERATION")
        counts[value[1]] = counts.get(value[1], 0) + 1
    elif kind == "dict":
        for item in value[1].values():
            _collect_pdf_refs(item, counts, tag, depth + 1)
    elif kind == "array":
        for item in value[1]:
            _collect_pdf_refs(item, counts, tag, depth + 1)
    elif kind == "keyword":
        if value[1] not in PDF_VALUE_KEYWORDS:
            _fail(tag + "_KEYWORD")
    elif kind not in ("name", "string", "number"):
        _fail(tag + "_VALUE_KIND")


def _pdf_resolved_name(value, objects, tag):
    seen = set()
    for _ in range(65):
        if value is None:
            return None
        if value[0] == "name":
            return value[1]
        if value[0] != "ref":
            return None
        target = _pdf_ref_value(value, tag + "_REF")
        if target in seen or target not in objects:
            _fail(tag + "_REFERENCE")
        seen.add(target)
        value = objects[target]
    _fail(tag + "_DEPTH")


def _pdf_reject_actions(value, objects, tag, depth=0):
    if depth > 64:
        _fail(tag + "_DEPTH")
    if value[0] == "dict":
        dictionary = value[1]
        if (_pdf_resolved_name(
                dictionary.get(b"Type"), objects, tag + "_TYPE",
        ) == b"Action" or _pdf_resolved_name(
                dictionary.get(b"S"), objects, tag + "_S",
        ) in PDF_ACTION_NAMES):
            _fail(tag + "_ACTIVE_ACTION")
        for item in dictionary.values():
            _pdf_reject_actions(item, objects, tag, depth + 1)
    elif value[0] == "array":
        for item in value[1]:
            _pdf_reject_actions(item, objects, tag, depth + 1)
    elif value[0] == "keyword":
        if value[1] not in PDF_VALUE_KEYWORDS:
            _fail(tag + "_KEYWORD")
    elif value[0] not in ("ref", "name", "string", "number"):
        _fail(tag + "_VALUE_KIND")


def _pdf_reachable_closure(objects, roots, tag):
    seen = set()
    queued = set(roots)
    pending = list(sorted(queued))
    while pending:
        object_id = pending.pop()
        queued.remove(object_id)
        if object_id in seen:
            continue
        if object_id not in objects:
            _fail(tag + "_MISSING")
        seen.add(object_id)
        targets = {}
        _collect_pdf_refs(
            objects[object_id], targets, tag + "_%d" % object_id,
        )
        for target in sorted(targets):
            if target not in seen and target not in queued:
                if len(seen) + len(queued) >= MAX_PDF_OBJECTS:
                    _fail(tag + "_LIMIT")
                queued.add(target)
                pending.append(target)
    return frozenset(seen)


def _pdf_validate_info(objects, info_id, stream_ids, tag):
    if info_id in stream_ids or info_id not in objects:
        _fail(tag + "_TARGET")
    dictionary = _pdf_closed_dictionary(
        objects[info_id], frozenset(), PDF_INFO_KEYS, tag,
    )
    for key, value in dictionary.items():
        if key == b"Trapped":
            if value not in (
                    ("name", b"True"), ("name", b"False"),
                    ("name", b"Unknown")):
                _fail(tag + "_TRAPPED")
        elif value[0] != "string":
            _fail(tag + "_FIELD_TYPE")


def _pdf_dictionary_extent(data, start, tag):
    if not data.startswith(b"<<", start):
        _fail(tag + "_DICTIONARY_START")
    depth = 0
    position = start
    while position < len(data):
        if data.startswith(b"<<", position):
            depth += 1
            position += 2
            continue
        if data.startswith(b">>", position):
            depth -= 1
            position += 2
            if depth == 0:
                return start, position
            if depth < 0:
                _fail(tag + "_DICTIONARY_DEPTH")
            continue
        position += 1
    _fail(tag + "_DICTIONARY_END")


def _font_dictionary_refs(value, tag):
    dictionary = _pdf_dictionary(value, tag + "_FONT_DICTIONARY")
    if not dictionary:
        _fail(tag + "_FONT_RESOURCE_EMPTY")
    return tuple(
        _pdf_ref_value(item, tag + "_FONT_RESOURCE_REF")
        for item in dictionary.values()
    )


def _resource_font_refs(value, objects, stream_ids, tag):
    dictionary = _pdf_dictionary(value, tag + "_RESOURCE_DICTIONARY")
    font_value = dictionary.get(b"Font")
    if font_value is None:
        _fail(tag + "_FONT_BINDING")
    if font_value[0] == "ref":
        target = _pdf_ref_value(font_value, tag + "_FONT_DICTIONARY_REF")
        if target not in objects or target in stream_ids:
            _fail(tag + "_FONT_DICTIONARY_REF")
        font_value = objects[target]
    elif font_value[0] != "dict":
        _fail(tag + "_FONT_BINDING")
    return _font_dictionary_refs(font_value, tag)


def _pdf_integer_array_value(value, tag, exact_length=None, even=False,
                             maximum_length=None):
    if value is None or value[0] != "array" or not value[1]:
        _fail(tag + "_INTEGER_ARRAY")
    if ((exact_length is not None and len(value[1]) != exact_length) or
            (even and len(value[1]) % 2) or
            (maximum_length is not None and len(value[1]) > maximum_length)):
        _fail(tag + "_INTEGER_ARRAY_LENGTH")
    result = tuple(
        _pdf_integer_value(item, tag + "_INTEGER") for item in value[1]
    )
    return result


def _pdf_consume_eol(data, position, end, tag):
    if position >= end:
        _fail(tag + "_EOL")
    if data.startswith(b"\r\n", position):
        return position + 2
    if data[position] == 0x0a:
        return position + 1
    _fail(tag + "_EOL")


def _pdf_xref_line(data, position, end, maximum, tag):
    if position >= end:
        _fail(tag + "_LINE")
    cursor = position
    while cursor < end and data[cursor] not in (0x0a, 0x0d):
        cursor += 1
        if cursor - position > maximum:
            _fail(tag + "_LINE_LIMIT")
    if cursor >= end:
        _fail(tag + "_LINE_EOL")
    line = data[position:cursor]
    return line, _pdf_consume_eol(data, cursor, end, tag)


def _validate_xref_entry_closure(entries, size, direct_offsets,
                                 compressed_locations, xref_id,
                                 object_zero_generation, tag):
    if object_zero_generation not in (255, 65535):
        _fail(tag + "_OBJECT_ZERO_GENERATION")
    if set(entries) != set(range(size)) or 0 not in entries:
        _fail(tag + "_ENTRY_SET")
    direct_ids = {number for number, entry in entries.items() if entry[0] == 1}
    compressed_ids = {number for number, entry in entries.items() if entry[0] == 2}
    free_ids = {number for number, entry in entries.items() if entry[0] == 0}
    if (direct_ids != set(direct_offsets) or
            compressed_ids != set(compressed_locations) or 0 not in free_ids):
        _fail(tag + "_CURRENT_SET")
    for number, (entry_type, field1, field2) in entries.items():
        if entry_type == 0:
            if (not 0 <= field1 < size or not 0 <= field2 <= 65535 or
                    number in direct_offsets or number in compressed_locations):
                _fail(tag + "_FREE_BINDING")
        elif entry_type == 1:
            if field2 != 0 or direct_offsets.get(number) != field1:
                _fail(tag + "_DIRECT_BINDING")
        elif entry_type == 2:
            if (compressed_locations.get(number) != (field1, field2) or
                    field1 not in direct_ids):
                _fail(tag + "_COMPRESSED_BINDING")
        else:
            _fail(tag + "_ENTRY_TYPE")
    if (entries[0][0] != 0 or
            entries[0][2] != object_zero_generation):
        _fail(tag + "_OBJECT_ZERO")
    seen = set()
    cursor = entries[0][1]
    while cursor != 0:
        if cursor not in free_ids or cursor in seen:
            _fail(tag + "_FREE_CHAIN")
        seen.add(cursor)
        cursor = entries[cursor][1]
    if seen != free_ids - {0}:
        _fail(tag + "_FREE_CLOSURE")
    if xref_id is not None and xref_id not in direct_ids:
        _fail(tag + "_XREF_SELF")


def _validate_traditional_xref(data, start, end, size, direct_offsets,
                               compressed_locations, tag):
    if compressed_locations:
        _fail(tag + "_COMPRESSED_UNSUPPORTED")
    entries = {}
    position = start
    previous_end = 0
    while position < end:
        header, position = _pdf_xref_line(
            data, position, end, 13, tag + "_SUBSECTION",
        )
        match = re.fullmatch(
            rb"(0|[1-9][0-9]{0,5}) ([1-9][0-9]{0,5})", header,
        )
        if match is None:
            _fail(tag + "_SUBSECTION_HEADER")
        first = _bounded_decimal(
            match.group(1), tag + "_SUBSECTION_FIRST", size,
        )
        count = _bounded_decimal(
            match.group(2), tag + "_SUBSECTION_COUNT", size, positive=True,
        )
        subsection_end = first + count
        if first < previous_end or subsection_end > size:
            _fail(tag + "_SUBSECTION_RANGE")
        previous_end = subsection_end
        for object_id in range(first, subsection_end):
            row = data[position:position + 20]
            row_match = re.fullmatch(
                rb"([0-9]{10}) ([0-9]{5}) ([nf])(?: \n|\r\n)", row,
            )
            if row_match is None or object_id in entries:
                _fail(tag + "_ENTRY_GRAMMAR")
            position += 20
            field1 = _fixed_width_decimal(
                row_match.group(1), 10, tag + "_ENTRY_FIELD1",
                max(len(data), size),
            )
            generation = _fixed_width_decimal(
                row_match.group(2), 5, tag + "_ENTRY_GENERATION", 65535,
            )
            state = row_match.group(3)
            if state == b"n":
                if (generation != 0 or object_id not in direct_offsets or
                        direct_offsets[object_id] != field1):
                    _fail(tag + "_DIRECT_BINDING")
                entries[object_id] = (1, field1, generation)
            else:
                if object_id in direct_offsets or field1 >= size or generation > 65535:
                    _fail(tag + "_FREE_BINDING")
                entries[object_id] = (0, field1, generation)
    if position != end:
        _fail(tag + "_ENTRY_CLOSURE")
    _validate_xref_entry_closure(
        entries, size, direct_offsets, compressed_locations, None,
        65535, tag + "_CURRENT",
    )
    return entries


def _xref_field(data, start, width):
    return 0 if width == 0 else int.from_bytes(data[start:start + width], "big")


def _validate_xref_stream(data, dictionary, xref_id, size, span_map,
                          direct_offsets, compressed_locations, tag):
    widths = _pdf_integer_array_value(
        dictionary.get(b"W"), tag + "_W", exact_length=3,
    )
    if (any(width > 8 for width in widths) or sum(widths) == 0 or
            widths[0] == 0 or widths[2] not in (1, 2)):
        _fail(tag + "_W_RANGE")
    index_value = dictionary.get(b"Index")
    if index_value is None:
        ranges = ((0, size),)
    else:
        index_rows = _pdf_integer_array_value(
            index_value, tag + "_INDEX", even=True,
            maximum_length=2 * size,
        )
        ranges = tuple(
            (index_rows[index], index_rows[index + 1])
            for index in range(0, len(index_rows), 2)
        )
    cursor = 0
    for first, count in ranges:
        if count <= 0 or first != cursor or first + count > size:
            _fail(tag + "_INDEX_RANGE")
        cursor = first + count
    if cursor != size:
        _fail(tag + "_INDEX_CLOSURE")
    filter_value = dictionary.get(b"Filter")
    if b"DecodeParms" in dictionary:
        _fail(tag + "_DECODE_PARMS")
    row_width = sum(widths)
    expected_payload = size * row_width
    start, end, _ = span_map[xref_id]
    payload = memoryview(data)[start:end]
    if filter_value is not None:
        if filter_value != ("name", b"FlateDecode"):
            _fail(tag + "_FILTER")
        payload = _bounded_flate(
            payload, tag + "_FLATE", expected_payload,
        )
    if len(payload) != expected_payload:
        _fail(tag + "_PAYLOAD_LENGTH")
    entries = {}
    position = 0
    for first, count in ranges:
        for object_id in range(first, first + count):
            fields = []
            for width in widths:
                fields.append(_xref_field(payload, position, width))
                position += width
            entry_type = 1 if widths[0] == 0 else fields[0]
            field1, field2 = fields[1], fields[2]
            if entry_type == 0:
                if (object_id in direct_offsets or object_id in compressed_locations or
                        field1 >= size or field2 > 65535):
                    _fail(tag + "_FREE_BINDING")
                entries[object_id] = (0, field1, field2)
            elif entry_type == 1:
                if (field2 != 0 or object_id not in direct_offsets or
                        direct_offsets[object_id] != field1):
                    _fail(tag + "_DIRECT_BINDING")
                entries[object_id] = (1, field1, field2)
            elif entry_type == 2:
                if compressed_locations.get(object_id) != (field1, field2):
                    _fail(tag + "_COMPRESSED_BINDING")
                entries[object_id] = (2, field1, field2)
            else:
                _fail(tag + "_ENTRY_TYPE")
    if position != len(payload):
        _fail(tag + "_ENTRY_CLOSURE")
    _validate_xref_entry_closure(
        entries, size, direct_offsets, compressed_locations, xref_id,
        (1 << (8 * widths[2])) - 1, tag + "_CURRENT",
    )
    return entries


def _pdf_catalog_pages(data, structural_pdf, objects, stream_ids, direct_offsets,
                       direct_extents, compressed_locations, span_map,
                       aggregate_budget, tag):
    # The frozen structural grammar admits Unix LF and CRLF, never lone CR.
    eol = rb"(?:\r\n|\n)"
    structural_start_re = re.compile(
        rb"(?m)^startxref" + eol + rb"(0|[1-9][0-9]{0,7})" + eol,
    )
    structural_rows = _bounded_regex_rows(
        structural_start_re, structural_pdf, 2, tag + "_STRUCTURAL_START_ROWS",
    )
    if len(structural_rows) != 1:
        _fail(tag + "_STARTXREF_CENSUS")
    terminal_start = structural_rows[0].start()
    terminal_re = re.compile(
        rb"startxref" + eol + rb"(0|[1-9][0-9]{0,7})" + eol +
        rb"%%EOF[\x00\x09\x0a\x0c\x0d\x20]*",
    )
    terminal_match = terminal_re.fullmatch(data, terminal_start, len(data))
    if (terminal_match is None or
            terminal_match.group(1) != structural_rows[0].group(1)):
        _fail(tag + "_TERMINAL_GRAMMAR")
    eof_marker_position = data.find(
        b"%%EOF", terminal_match.end(1), terminal_match.end(),
    )
    if eof_marker_position < 0:
        _fail(tag + "_TERMINAL_EOF")
    xref_offset = _bounded_decimal(
        terminal_match.group(1), tag + "_STARTXREF", len(data),
        positive=True,
    )
    if (xref_offset <= 0 or xref_offset >= len(data) or
            data[xref_offset] != structural_pdf[xref_offset]):
        _fail(tag + "_STARTXREF_OFFSET")
    trailer_rows = _bounded_regex_rows(
        re.compile(rb"(?m)^trailer(?=[\x00\x09\x0a\x0c\x0d\x20])"),
        structural_pdf, 2, tag + "_TRAILER_ROWS",
    )
    traditional_xref_rows = _bounded_regex_rows(
        re.compile(rb"(?m)^xref(?=\r?$)"), structural_pdf, 2,
        tag + "_TRADITIONAL_XREF_ROWS",
    )
    xref_stream_ids = set()
    for number, value in objects.items():
        if _pdf_top_name(value, b"Type") == b"XRef":
            xref_stream_ids.add(number)
            if len(xref_stream_ids) > 1:
                _fail(tag + "_XREF_STREAM_CENSUS")
    trailer_value = None
    traditional_bounds = None
    xref_id = None
    if (len(traditional_xref_rows) == 1 and
            traditional_xref_rows[0].start() == xref_offset):
        last_direct_end = max(
            (extent[1] for extent in direct_extents.values()), default=0,
        )
        if (len(trailer_rows) != 1 or xref_stream_ids or not direct_extents or
                last_direct_end > xref_offset or
                max(direct_offsets.values(), default=0) >= xref_offset or
                not _pdf_layout_only(
                    data, last_direct_end, xref_offset,
                    tag + "_TRADITIONAL_XREF_GAP",
                )):
            _fail(tag + "_TRADITIONAL_XREF_SOURCE")
        trailer = trailer_rows[0]
        if not (xref_offset < trailer.start() < terminal_start):
            _fail(tag + "_TRAILER_POSITION")
        position = trailer.end()
        while (position < len(structural_pdf) and
               structural_pdf[position] in b"\x00\x09\x0a\x0c\x0d\x20"):
            position += 1
        if not _pdf_layout_only(
                data, trailer.end(), position, tag + "_TRAILER_PREFIX"):
            _fail(tag + "_TRAILER_PREFIX")
        trailer_start, trailer_end = _pdf_dictionary_extent(
            structural_pdf, position, tag + "_TRAILER",
        )
        _reject_pdf_semantic_tokens(
            data, tag + "_TRAILER_SECURITY", trailer_start, trailer_end,
        )
        trailer_value, trailer_stream = _parse_pdf_object(
            structural_pdf, tag + "_TRAILER", aggregate_budget,
            trailer_start, trailer_end,
        )
        if (trailer_stream or
                not _pdf_layout_only(
                    data, trailer_end, terminal_start,
                    tag + "_TRAILER_TERMINAL",
                )):
            _fail(tag + "_TRAILER_TERMINAL")
        table_start = _pdf_consume_eol(
            data, traditional_xref_rows[0].end(), trailer.start(),
            tag + "_TRADITIONAL_XREF",
        )
        traditional_bounds = (table_start, trailer.start())
        source_value = trailer_value
    else:
        if trailer_rows or traditional_xref_rows or len(xref_stream_ids) != 1:
            _fail(tag + "_XREF_STREAM_SOURCE")
        xref_id = next(iter(xref_stream_ids))
        if (xref_id not in stream_ids or xref_id not in direct_offsets or
                direct_offsets[xref_id] != xref_offset or
                max(direct_offsets.values(), default=0) != xref_offset):
            _fail(tag + "_XREF_STREAM_OFFSET")
        xref_extent = direct_extents.get(xref_id)
        if (xref_extent is None or xref_extent[0] != xref_offset or
                xref_extent[1] > terminal_start or
                not _pdf_layout_only(
                    data, xref_extent[1], terminal_start,
                    tag + "_XREF_STREAM_TERMINAL_GAP",
                )):
            _fail(tag + "_XREF_STREAM_TERMINAL_GAP")
        source_value = objects[xref_id]
    if traditional_bounds is not None:
        source = _pdf_closed_dictionary(
            source_value, PDF_TRADITIONAL_TRAILER_REQUIRED_KEYS,
            PDF_TRADITIONAL_TRAILER_OPTIONAL_KEYS,
            tag + "_TRADITIONAL_TRAILER",
        )
    else:
        source = _pdf_closed_dictionary(
            source_value, PDF_XREF_STREAM_REQUIRED_KEYS,
            PDF_XREF_STREAM_OPTIONAL_KEYS, tag + "_XREF_SOURCE",
        )
    id_value = source.get(b"ID")
    if (id_value is not None and
            (id_value[0] != "array" or len(id_value[1]) != 2 or
             any(item[0] != "string" for item in id_value[1]))):
        _fail(tag + "_ID")
    size = _pdf_integer_value(
        source.get(b"Size"), tag + "_XREF_SIZE", positive=True,
        maximum=MAX_PDF_OBJECTS,
    )
    if not objects or max(objects) >= size:
        _fail(tag + "_XREF_SIZE_BOUND")
    if traditional_bounds is not None:
        _validate_traditional_xref(
            data, traditional_bounds[0], traditional_bounds[1], size,
            direct_offsets, compressed_locations, tag + "_TRADITIONAL_XREF",
        )
    else:
        _validate_xref_stream(
            data, source, xref_id, size, span_map, direct_offsets,
            compressed_locations, tag + "_XREF_STREAM",
        )
    root_id = _pdf_ref_value(source.get(b"Root"), tag + "_ROOT")
    if (root_id not in objects or root_id in stream_ids or
            _pdf_top_name(objects[root_id], b"Type") != b"Catalog"):
        _fail(tag + "_CATALOG_ROOT")
    catalogs = set()
    for number, value in objects.items():
        if _pdf_top_name(value, b"Type") == b"Catalog":
            catalogs.add(number)
            if len(catalogs) > 1:
                _fail(tag + "_CATALOG_CENSUS")
    if catalogs != {root_id}:
        _fail(tag + "_CATALOG_CENSUS")
    catalog = _pdf_closed_dictionary(
        objects[root_id], PDF_CATALOG_KEYS, frozenset(), tag + "_CATALOG",
    )
    pages_id = _pdf_ref_value(catalog.get(b"Pages"), tag + "_CATALOG_PAGES")
    if pages_id not in objects or pages_id in stream_ids:
        _fail(tag + "_PAGES_ROOT")
    info_id = None
    if b"Info" in source:
        info_id = _pdf_ref_value(source[b"Info"], tag + "_INFO")
        _pdf_validate_info(objects, info_id, stream_ids, tag + "_INFO")
    return (root_id, pages_id, source_value, info_id,
            frozenset(xref_stream_ids), eof_marker_position)


def _pdf_page_tree(objects, stream_ids, pages_root, expected_pages, tag):
    page_ids = set()
    pages_ids = set()
    for number, value in objects.items():
        object_type = _pdf_top_name(value, b"Type")
        if object_type == b"Page":
            if number in stream_ids:
                _fail(tag + "_PAGE_STREAM")
            _pdf_closed_dictionary(
                value, PDF_PAGE_REQUIRED_KEYS, PDF_PAGE_OPTIONAL_KEYS,
                tag + "_PAGE_%d" % number,
            )
            page_ids.add(number)
        if object_type == b"Pages":
            if number in stream_ids:
                _fail(tag + "_PAGES_STREAM")
            _pdf_closed_dictionary(
                value, PDF_PAGES_REQUIRED_KEYS, PDF_PAGES_OPTIONAL_KEYS,
                tag + "_PAGES_%d" % number,
            )
            pages_ids.add(number)
    if pages_root not in pages_ids:
        _fail(tag + "_PAGES_ROOT_TYPE")
    seen = set()
    reachable_pages = set()
    reachable_pages_nodes = set()
    parent_map = {}

    def walk(node, expected_parent, depth):
        if depth > 64 or node in seen or node not in objects:
            _fail(tag + "_TREE_CYCLE")
        seen.add(node)
        value = objects[node]
        if _pdf_top_name(value, b"Type") != b"Pages":
            _fail(tag + "_TREE_PAGES_TYPE")
        dictionary = _pdf_dictionary(value, tag + "_TREE_PAGES_DICTIONARY")
        reachable_pages_nodes.add(node)
        if expected_parent is None:
            if b"Parent" in dictionary:
                _fail(tag + "_ROOT_PARENT")
        else:
            parent = _pdf_ref_value(
                dictionary.get(b"Parent"), tag + "_PAGES_PARENT",
            )
            if parent != expected_parent:
                _fail(tag + "_PAGES_PARENT")
            parent_map[node] = expected_parent
        kids = _pdf_ref_array_value(
            dictionary.get(b"Kids"), tag + "_KIDS_%d" % node,
        )
        subtotal = 0
        for child in kids:
            if child in seen or child not in objects:
                _fail(tag + "_KID_DUPLICATE_OR_MISSING")
            child_value = objects[child]
            child_type = _pdf_top_name(child_value, b"Type")
            if child_type == b"Page":
                child_dictionary = _pdf_dictionary(
                    child_value, tag + "_PAGE_DICTIONARY",
                )
                if _pdf_ref_value(
                        child_dictionary.get(b"Parent"), tag + "_PAGE_PARENT_BACKREF",
                ) != node:
                    _fail(tag + "_PAGE_PARENT_BACKREF")
                seen.add(child)
                parent_map[child] = node
                reachable_pages.add(child)
                subtotal += 1
            elif child_type == b"Pages":
                subtotal += walk(child, node, depth + 1)
            else:
                _fail(tag + "_KID_TYPE")
        count = _pdf_integer_value(
            dictionary.get(b"Count"), tag + "_PAGE_COUNT", positive=True,
        )
        if count != subtotal:
            _fail(tag + "_PAGE_COUNT")
        return subtotal

    total = walk(pages_root, None, 0)
    if (total != expected_pages or reachable_pages != page_ids or
            reachable_pages_nodes != pages_ids or len(reachable_pages) != expected_pages):
        _fail(tag + "_TREE_CLOSURE")
    return tuple(sorted(reachable_pages)), parent_map


def _font_program_bytes(data, span_map, stream_id, budget, tag):
    start, end, dictionary_value = span_map[stream_id]
    dictionary = _pdf_dictionary(dictionary_value, tag + "_STREAM_DICTIONARY")
    filter_value = dictionary.get(b"Filter")
    if b"DecodeParms" in dictionary:
        _fail(tag + "_DECODE_PARMS")
    _type1_budget_take(budget, "decoded_bytes", 0, tag + "_AGGREGATE")
    remaining = budget["decoded_bytes"]
    if filter_value is None:
        if end - start > min(MAX_TYPE1_PROGRAM_BYTES, remaining):
            _fail(tag + "_PAYLOAD_LIMIT")
        payload = data[start:end]
    else:
        if filter_value != ("name", b"FlateDecode"):
            _fail(tag + "_FILTER")
        payload = _bounded_flate(
            memoryview(data)[start:end], tag + "_FLATE",
            min(MAX_TYPE1_PROGRAM_BYTES, remaining),
        )
    if not payload:
        _fail(tag + "_EMPTY")
    _type1_budget_take(
        budget, "decoded_bytes", len(payload), tag + "_AGGREGATE",
    )
    return payload, dictionary_value


def _type1_decrypt(data, seed, discard=0):
    if (not isinstance(discard, int) or
            not 0 <= discard <= len(data)):
        _fail("TYPE1_DECRYPT_CONTRACT")
    result = bytearray(len(data) - discard)
    state = seed
    output_index = 0
    for index, value in enumerate(data):
        decoded = value ^ (state >> 8)
        state = ((value + state) * 52845 + 22719) & 0xffff
        if index >= discard:
            result[output_index] = decoded
            output_index += 1
    if output_index != len(result):
        _fail("TYPE1_DECRYPT_CLOSURE")
    return result


def _type1_ascii_hex_decrypt(data, seed, discard, tag):
    digits = 0
    for value in data:
        if value in TYPE1_WS:
            continue
        if _hex_nibble(value) < 0:
            _fail(tag + "_HEX_GRAMMAR")
        digits += 1
    if digits % 2:
        _fail(tag + "_HEX_GRAMMAR")
    ciphertext_length = digits // 2
    if (not 64 <= ciphertext_length <= MAX_TYPE1_EEXEC_BYTES or
            not 0 <= discard <= ciphertext_length):
        _fail(tag + "_CIPHERTEXT")
    plain = bytearray(ciphertext_length - discard)
    state = seed
    high = None
    cipher_index = 0
    output_index = 0
    for value in data:
        if value in TYPE1_WS:
            continue
        nibble = _hex_nibble(value)
        if high is None:
            high = nibble
            continue
        cipher = (high << 4) | nibble
        high = None
        decoded = cipher ^ (state >> 8)
        state = ((cipher + state) * 52845 + 22719) & 0xffff
        if cipher_index >= discard:
            plain[output_index] = decoded
            output_index += 1
        cipher_index += 1
    if (high is not None or cipher_index != ciphertext_length or
            output_index != len(plain)):
        _fail(tag + "_HEX_CLOSURE")
    return plain


TYPE1_WS = b"\x00\x09\x0a\x0c\x0d\x20"
TYPE1_PS_DELIMITERS = b"()<>[]{}/%{}"
TYPE1_STRUCTURAL_NAMES = frozenset({
    b"FontType", b"FontName", b"Private", b"lenIV", b"Subrs",
    b"CharStrings",
})
TYPE1_FORBIDDEN_DYNAMIC_NAMES = frozenset({
    b"cvx", b"cvn", b"token", b"run",
})
TYPE1_ALLOWED_NESTED_NAMES = frozenset({
    b"string", b"currentfile", b"exch", b"readstring", b"pop",
    b"noaccess", b"def", b"put", b"systemdict", b"known", b"not",
    b"get", b"exec", b"dup", b"if", b"ifelse", b"index",
    b"setcurrentpoint", b"true", b"false", b"readonly", b"executeonly",
})
TYPE1_ALLOWED_CLEAR_NAMES = frozenset({
    b"dict", b"begin", b"end", b"dup", b"def", b"readonly",
    b"currentdict", b"currentfile", b"eexec", b"array", b"for",
    b"index", b"exch", b"put", b"copy", b"false", b"true",
    b"StandardEncoding", b"executeonly", b"noaccess", b"bind",
})
TYPE1_ALLOWED_EEXEC_NAMES = frozenset({
    b"dict", b"begin", b"end", b"dup", b"def", b"readonly",
    b"noaccess", b"put", b"array", b"index", b"executeonly",
    b"bind", b"false", b"true", b"RD", b"NP", b"ND", b"-|",
    b"|-", b"|", b"get", b"exch", b"definefont", b"pop", b"mark",
    b"currentfile", b"closefile",
})
TYPE1_ALLOWED_NESTED_EXEC_PREFIXES = (
    (("name", b"systemdict"), ("literal", b"internaldict"), ("name", b"get")),
    (("literal", b"startlock"), ("name", b"get")),
    (("literal", b"strtlck"), ("name", b"get")),
)
MAX_TYPE1_ABSTRACT_STEPS = 2_000_000
TYPE1_PRIVATE_SIMPLE_FIELDS = frozenset({
    b"BlueValues", b"OtherBlues", b"FamilyBlues", b"FamilyOtherBlues",
    b"BlueScale", b"BlueShift", b"BlueFuzz", b"StdHW", b"StdVW",
    b"StemSnapH", b"StemSnapV", b"ForceBold", b"LanguageGroup",
    b"ExpansionFactor", b"RndStemUp", b"password", b"MinFeature",
    b"lenIV", b"UniqueID",
})
TYPE1_FONTINFO_FIELDS = frozenset({
    b"version", b"Notice", b"FullName", b"FamilyName", b"Weight",
    b"ItalicAngle", b"isFixedPitch", b"UnderlinePosition",
    b"UnderlineThickness",
})


def _new_pdf_type1_budget():
    return {
        "decoded_bytes": MAX_PDF_TYPE1_DECODED_BYTES,
        "lexical_tokens": MAX_PDF_TYPE1_LEXICAL_TOKENS,
        "charstring_tokens": MAX_PDF_TYPE1_CHARSTRING_TOKENS,
        "concrete_steps": MAX_PDF_TYPE1_CONCRETE_STEPS,
        "abstract_steps": MAX_PDF_TYPE1_ABSTRACT_STEPS,
    }


def _reject_type1_semantic_tokens(data, binary_spans, tag):
    cursor = 0
    ranges = sorted((row[1], row[2]) for row in binary_spans)
    forbidden = (b"/Encrypt",) + RAW_PDF_REJECTION_TOKENS
    for start, end in ranges:
        if not cursor <= start <= end <= len(data):
            _fail(tag + "_BINARY_RANGE")
        for token in forbidden:
            if data.find(token, cursor, start) >= 0:
                _fail(tag + "_FORBIDDEN")
        cursor = end
    for token in forbidden:
        if data.find(token, cursor, len(data)) >= 0:
            _fail(tag + "_FORBIDDEN")


def _type1_budget_take(budget, key, amount, tag):
    if (not isinstance(budget, dict) or key not in budget or
            not isinstance(budget[key], int) or not isinstance(amount, int) or
            amount < 0):
        _fail(tag + "_BUDGET_CONTRACT")
    if amount > budget[key]:
        _fail(tag + "_BUDGET_" + key.upper())
    budget[key] -= amount


def _ps_integer(raw, tag):
    if (len(raw) > 11 or
            re.fullmatch(rb"-?(?:0|[1-9][0-9]*)", raw) is None):
        _fail(tag + "_INTEGER_GRAMMAR")
    value = int(raw)
    if not -2_147_483_648 <= value <= 2_147_483_647:
        _fail(tag + "_INTEGER_BOUND")
    return value


def _ps_real_name(raw):
    return len(raw) <= 64 and re.fullmatch(
        rb"-?(?:(?:0|[1-9][0-9]*)\.[0-9]+|\.[0-9]+)", raw,
    ) is not None


def _ps_validate_names(tokens, allowed, tag):
    for index, token in enumerate(tokens):
        if (token[0] == "name" and token[1] not in allowed and
                not _ps_real_name(token[1])):
            _fail(tag + "_%05d" % index)


def _ps_validate_allocations(tokens, dictionary_limit, array_limit, tag):
    for index, token in enumerate(tokens):
        if not _ps_token_is(token, "name") or token[1] not in (b"dict", b"array"):
            continue
        if index == 0 or not _ps_token_is(tokens[index - 1], "integer"):
            _fail(tag + "_OPERAND")
        limit = dictionary_limit if token[1] == b"dict" else array_limit
        lower = 1 if token[1] == b"dict" else 0
        if not lower <= tokens[index - 1][1] <= limit:
            _fail(tag + "_BOUND")


def _ps_skip_layout(data, position, tag):
    while position < len(data):
        if data[position] in TYPE1_WS:
            position += 1
            continue
        if data[position] == 0x25:
            position += 1
            while position < len(data) and data[position] not in (0x0a, 0x0d):
                position += 1
            continue
        break
    return position


def _ps_scan_type1(data, tag, allow_binary, max_tokens, max_binary_spans,
                   max_input_bytes, aggregate_budget=None):
    """Return real depth-zero PostScript tokens and length-bound binary spans."""
    if len(data) > max_input_bytes:
        _fail(tag + "_INPUT_LIMIT")
    tokens = []
    binary_spans = []
    stack = []
    nested_history = []
    position = 0
    lexical_tokens = 0
    binary_bytes = 0

    def count_token():
        nonlocal lexical_tokens
        lexical_tokens += 1
        if lexical_tokens > max_tokens:
            _fail(tag + "_TOKEN_LIMIT")
        if aggregate_budget is not None:
            _type1_budget_take(
                aggregate_budget, "lexical_tokens", 1,
                tag + "_AGGREGATE",
            )

    def emit(token):
        tokens.append(token)

    def emit_binary(row):
        nonlocal binary_bytes
        if len(binary_spans) >= max_binary_spans:
            _fail(tag + "_BINARY_SPAN_LIMIT")
        binary_bytes += row[2] - row[1]
        if binary_bytes > MAX_TYPE1_PROGRAM_BYTES:
            _fail(tag + "_BINARY_BYTES_LIMIT")
        binary_spans.append(row)

    while position < len(data):
        value = data[position]
        if value in TYPE1_WS:
            position += 1
            continue
        if value == 0x25:
            start = position
            position += 1
            while position < len(data) and data[position] not in (0x0a, 0x0d):
                position += 1
            if data.startswith(b"\r\n", position):
                position += 2
            elif position < len(data):
                position += 1
            continue
        if value == 0x28:
            start = position
            depth = 1
            position += 1
            while depth:
                if position >= len(data):
                    _fail(tag + "_STRING_UNTERMINATED")
                current = data[position]
                if current == 0x5c:
                    position += 1
                    if position >= len(data):
                        _fail(tag + "_STRING_ESCAPE")
                    if data.startswith(b"\r\n", position):
                        position += 2
                    else:
                        position += 1
                    continue
                if current == 0x28:
                    depth += 1
                    if depth > 32:
                        _fail(tag + "_STRING_DEPTH")
                elif current == 0x29:
                    depth -= 1
                position += 1
                if position - start > MAX_TYPE1_STRING_BYTES:
                    _fail(tag + "_STRING_LIMIT")
            semantic, semantic_end = _literal_string_payload(
                data, start, position, MAX_TYPE1_STRING_BYTES,
                tag + "_STRING_SEMANTIC",
            )
            if semantic_end != position:
                _fail(tag + "_STRING_SEMANTIC_CLOSURE")
            _reject_forbidden_payload(
                semantic, tag + "_STRING_SEMANTIC",
            )
            del semantic
            count_token()
            if not stack:
                emit(("opaque", b"string", start, position))
            else:
                nested_history = [("opaque", b"string")]
            continue
        if value == 0x3c and not data.startswith(b"<<", position):
            if data.startswith(b"<~", position):
                _fail(tag + "_ASCII85")
            start = position
            position += 1
            while position < len(data) and data[position] != 0x3e:
                if (data[position] not in TYPE1_WS and
                        data[position] not in b"0123456789abcdefABCDEF"):
                    _fail(tag + "_HEX_STRING_BYTE")
                position += 1
                if position - start > MAX_TYPE1_STRING_BYTES:
                    _fail(tag + "_HEX_STRING_LIMIT")
            if position >= len(data):
                _fail(tag + "_HEX_STRING_UNTERMINATED")
            position += 1
            semantic, semantic_end = _hex_string_payload(
                data, start, position, MAX_TYPE1_STRING_BYTES,
                tag + "_HEX_STRING_SEMANTIC",
            )
            if semantic_end != position:
                _fail(tag + "_HEX_STRING_SEMANTIC_CLOSURE")
            _reject_forbidden_payload(
                semantic, tag + "_HEX_STRING_SEMANTIC",
            )
            del semantic
            count_token()
            if not stack:
                emit(("opaque", b"hex-string", start, position))
            else:
                nested_history = [("opaque", b"hex-string")]
            continue
        opener = None
        closer = None
        width = 1
        if value == 0x7b:
            opener, closer = b"{", b"}"
        elif value == 0x5b:
            opener, closer = b"[", b"]"
        elif data.startswith(b"<<", position):
            opener, closer, width = b"<<", b">>", 2
        if opener is not None:
            start = position
            count_token()
            root_token_index = None
            if not stack:
                emit(("opaque", opener, start, start + width))
                root_token_index = len(tokens) - 1
                nested_history = []
            nested_history.append(("opaque", opener))
            if len(nested_history) > 64:
                del nested_history[:-64]
            stack.append((closer, root_token_index))
            if len(stack) > 32:
                _fail(tag + "_COMPOSITE_DEPTH")
            position += width
            continue
        current_closer = None
        closer_width = 1
        if value == 0x7d:
            current_closer = b"}"
        elif value == 0x5d:
            current_closer = b"]"
        elif data.startswith(b">>", position):
            current_closer, closer_width = b">>", 2
        elif value == 0x3e:
            _fail(tag + "_UNPAIRED_ANGLE")
        if current_closer is not None:
            count_token()
            if not stack or stack[-1][0] != current_closer:
                _fail(tag + "_COMPOSITE_CLOSER")
            _, root_token_index = stack.pop()
            position += closer_width
            if root_token_index is not None:
                token = tokens[root_token_index]
                tokens[root_token_index] = (
                    token[0], token[1], token[2], position,
                )
            if not stack:
                nested_history = []
            else:
                nested_history.append(("opaque", current_closer))
                if len(nested_history) > 64:
                    del nested_history[:-64]
            continue
        start = position
        literal = value == 0x2f
        if literal:
            position += 1
            if (position >= len(data) or data[position] in TYPE1_WS or
                    data[position] in TYPE1_PS_DELIMITERS):
                _fail(tag + "_LITERAL_NAME")
        while (position < len(data) and data[position] not in TYPE1_WS and
               data[position] not in TYPE1_PS_DELIMITERS):
            position += 1
            if position - start > MAX_TYPE1_TOKEN_BYTES:
                _fail(tag + "_TOKEN_BYTES_LIMIT")
        raw = bytes(memoryview(data)[start:position])
        if not raw:
            _fail(tag + "_TOKEN")
        if len(raw) > MAX_TYPE1_TOKEN_BYTES:
            _fail(tag + "_TOKEN_BYTES_LIMIT")
        count_token()
        if stack:
            if literal and raw[1:] in TYPE1_STRUCTURAL_NAMES:
                _fail(tag + "_STRUCTURAL_NAME_DEPTH")
            if literal:
                nested_token = ("literal", raw[1:])
            elif re.fullmatch(rb"-?(?:0|[1-9][0-9]*)", raw):
                nested_token = ("integer", _ps_integer(raw, tag + "_NESTED"))
            else:
                nested_token = ("name", raw)
            if nested_token == ("name", b"exec"):
                if not any(
                        len(nested_history) >= len(prefix) and
                        tuple(nested_history[-len(prefix):]) == prefix
                        for prefix in TYPE1_ALLOWED_NESTED_EXEC_PREFIXES):
                    _fail(tag + "_NESTED_EXEC_CONTEXT")
            elif nested_token[0] == "name":
                if (nested_token[1] in TYPE1_FORBIDDEN_DYNAMIC_NAMES or
                        (nested_token[1] not in TYPE1_ALLOWED_NESTED_NAMES and
                         not _ps_real_name(nested_token[1]))):
                    _fail(tag + "_NESTED_NAME")
            nested_history.append(nested_token)
            if len(nested_history) > 64:
                del nested_history[:-64]
            continue
        if literal:
            token = ("literal", raw[1:], start, position)
        elif re.fullmatch(rb"-?(?:0|[1-9][0-9]*)", raw):
            token = ("integer", _ps_integer(raw, tag + "_ROOT"), start, position)
        else:
            if raw in TYPE1_FORBIDDEN_DYNAMIC_NAMES or raw == b"exec":
                _fail(tag + "_DYNAMIC_NAME")
            token = ("name", raw, start, position)
        emit(token)
        if token[:2] in (("name", b"RD"), ("name", b"-|")):
            if not allow_binary:
                _fail(tag + "_BINARY_FORBIDDEN")
            length = None
            role = None
            if (len(tokens) >= 4 and tokens[-4][:2] == ("name", b"dup") and
                    tokens[-3][0] == "integer" and tokens[-3][1] >= 0 and
                    tokens[-2][0] == "integer" and tokens[-2][1] > 0):
                length = tokens[-2][1]
                role = b"subr"
            elif (len(tokens) >= 3 and tokens[-3][0] == "literal" and
                    tokens[-2][0] == "integer" and tokens[-2][1] > 0):
                length = tokens[-2][1]
                role = b"glyph"
            if length is None:
                _fail(tag + "_UNBOUND_BINARY_INTRODUCER")
            if data.startswith(b"\r\n", position):
                position += 2
            elif position < len(data) and data[position] in TYPE1_WS:
                position += 1
            else:
                _fail(tag + "_BINARY_SEPARATOR")
            body_start = position
            body_end = body_start + length
            if body_end > len(data):
                _fail(tag + "_BINARY_BOUND")
            emit_binary((token[2], body_start, body_end, token[1], role))
            position = body_end
    if stack:
        _fail(tag + "_COMPOSITE_UNTERMINATED")
    return tuple(tokens), tuple(binary_spans)


def _ps_token_is(token, kind, value=None):
    return (token[0] == kind and (value is None or token[1] == value))


def _ps_named_rows(tokens, kind, name, maximum, tag, start=0, stop=None):
    limit = len(tokens) if stop is None else stop
    if (not isinstance(maximum, int) or maximum < 0 or
            not 0 <= start <= limit <= len(tokens)):
        _fail(tag + "_CONTRACT")
    rows = []
    for index in range(start, limit):
        if _ps_token_is(tokens[index], kind, name):
            if len(rows) >= maximum:
                _fail(tag + "_CENSUS")
            rows.append(index)
    return tuple(rows)


def _ps_literal_rows(tokens, name, maximum, tag, start=0, stop=None):
    return _ps_named_rows(
        tokens, "literal", name, maximum, tag, start, stop,
    )


def _ps_matching_end(tokens, begin_index, tag):
    if not _ps_token_is(tokens[begin_index], "name", b"begin"):
        _fail(tag + "_BEGIN")
    depth = 1
    for index in range(begin_index + 1, len(tokens)):
        if _ps_token_is(tokens[index], "name", b"begin"):
            depth += 1
        elif _ps_token_is(tokens[index], "name", b"end"):
            depth -= 1
            if depth == 0:
                return index
        if depth > 32:
            _fail(tag + "_DEPTH")
    _fail(tag + "_END")


def _ps_number_token(token):
    return (_ps_token_is(token, "integer") or
            (_ps_token_is(token, "name") and _ps_real_name(token[1])))


def _ps_composite_tokens(data, token, opener, closer, maximum, tag):
    if (not _ps_token_is(token, "opaque", opener) or token[3] <= token[2] + 1 or
            data[token[2]:token[2] + len(opener)] != opener or
            data[token[3] - len(closer):token[3]] != closer):
        _fail(tag + "_FRAME")
    inner_start = token[2] + len(opener)
    inner_end = token[3] - len(closer)
    if inner_end - inner_start > MAX_TYPE1_STRING_BYTES:
        _fail(tag + "_SPAN_LIMIT")
    inner = data[inner_start:inner_end]
    nested, spans = _ps_scan_type1(
        inner, tag + "_TOKENS", False, maximum, 0,
        min(MAX_TYPE1_STRING_BYTES, max(1, len(inner))),
    )
    if spans or len(nested) > maximum:
        _fail(tag + "_STRUCTURE")
    return nested


def _ps_numeric_composite(data, token, opener, closer, minimum, maximum, tag):
    rows = _ps_composite_tokens(
        data, token, opener, closer, maximum, tag,
    )
    if not minimum <= len(rows) <= maximum or any(
            not _ps_number_token(row) for row in rows):
        _fail(tag + "_NUMBERS")
    return rows


def _ps_compact_composite(data, token, opener, closer, limit, tag):
    if (not _ps_token_is(token, "opaque", opener) or token[3] <= token[2] + 1 or
            data[token[2]:token[2] + len(opener)] != opener or
            data[token[3] - len(closer):token[3]] != closer):
        _fail(tag + "_FRAME")
    start = token[2]
    end = token[3]
    if end - start > MAX_TYPE1_STRING_BYTES:
        _fail(tag + "_SPAN_LIMIT")
    compact = bytearray()
    position = start
    while position < end:
        value = data[position]
        if value in TYPE1_WS:
            position += 1
            continue
        if value == 0x25:
            position += 1
            while position < end and data[position] not in (0x0a, 0x0d):
                position += 1
            continue
        if value in b"()<>":
            _fail(tag + "_STRING")
        compact.append(value)
        if len(compact) > limit:
            _fail(tag + "_LIMIT")
        position += 1
    return bytes(compact)


def _ps_definition_end(tokens, position, modifiers, tag):
    if (position < len(tokens) and _ps_token_is(tokens[position], "name") and
            tokens[position][1] in modifiers):
        position += 1
    if position >= len(tokens) or not _ps_token_is(tokens[position], "name", b"def"):
        _fail(tag + "_DEF")
    return position + 1


def _validate_type1_fontinfo(tokens, start, end, capacity, tag):
    position = start
    fields = set()
    while position < end:
        if (position + 2 >= end or
                not _ps_token_is(tokens[position], "literal") or
                tokens[position][1] not in TYPE1_FONTINFO_FIELDS or
                tokens[position][1] in fields):
            _fail(tag + "_FIELD")
        key = tokens[position][1]
        value = tokens[position + 1]
        if key in (b"version", b"Notice", b"FullName", b"FamilyName", b"Weight"):
            if not (_ps_token_is(value, "opaque", b"string") or
                    _ps_token_is(value, "literal")):
                _fail(tag + "_STRING_VALUE")
        elif key == b"isFixedPitch":
            if not (_ps_token_is(value, "name", b"false") or
                    _ps_token_is(value, "name", b"true")):
                _fail(tag + "_BOOLEAN_VALUE")
        elif not _ps_number_token(value):
            _fail(tag + "_NUMBER_VALUE")
        position = _ps_definition_end(
            tokens, position + 2, frozenset({b"readonly"}), tag + "_FIELD",
        )
        fields.add(key)
        if len(fields) > capacity:
            _fail(tag + "_CAPACITY")
    required = {
        b"version", b"FullName", b"FamilyName", b"Weight",
        b"ItalicAngle", b"isFixedPitch",
    }
    if not required.issubset(fields):
        _fail(tag + "_REQUIRED")


def _validate_type1_encoding(clear, tokens, position, tag):
    if not _ps_token_is(tokens[position], "literal", b"Encoding"):
        _fail(tag + "_DECLARATION")
    position += 1
    if (position < len(tokens) and
            _ps_token_is(tokens[position], "name", b"StandardEncoding")):
        return _ps_definition_end(tokens, position + 1, frozenset(), tag)
    if (position + 5 >= len(tokens) or
            not _ps_token_is(tokens[position], "integer", 256) or
            not _ps_token_is(tokens[position + 1], "name", b"array") or
            not _ps_token_is(tokens[position + 2], "integer", 0) or
            not _ps_token_is(tokens[position + 3], "integer", 1) or
            not _ps_token_is(tokens[position + 4], "integer", 255) or
            not _ps_token_is(tokens[position + 5], "opaque", b"{")):
        _fail(tag + "_ARRAY_PREFIX")
    if _ps_compact_composite(
            clear, tokens[position + 5], b"{", b"}", 128,
            tag + "_INITIALIZER",
    ) != b"{1indexexch/.notdefput}":
        _fail(tag + "_INITIALIZER")
    position += 6
    if position >= len(tokens) or not _ps_token_is(tokens[position], "name", b"for"):
        _fail(tag + "_FOR")
    position += 1
    codes = set()
    while position < len(tokens) and _ps_token_is(tokens[position], "name", b"dup"):
        if (position + 3 >= len(tokens) or
                not _ps_token_is(tokens[position + 1], "integer") or
                not 0 <= tokens[position + 1][1] <= 255 or
                not _ps_token_is(tokens[position + 2], "literal") or
                not _ps_token_is(tokens[position + 3], "name", b"put")):
            _fail(tag + "_ROW")
        code = tokens[position + 1][1]
        if code in codes:
            _fail(tag + "_DUPLICATE_CODE")
        codes.add(code)
        position += 4
    if not codes:
        _fail(tag + "_EMPTY")
    return _ps_definition_end(
        tokens, position, frozenset({b"readonly"}), tag,
    )


def _validate_type1_clear_skeleton(clear, tokens, tag):
    _ps_validate_names(tokens, TYPE1_ALLOWED_CLEAR_NAMES, tag + "_NAME")
    _ps_validate_allocations(tokens, 64, 4096, tag + "_ALLOCATION")
    if (len(tokens) < 12 or not _ps_token_is(tokens[0], "integer") or
            not 8 <= tokens[0][1] <= 64 or
            not _ps_token_is(tokens[1], "name", b"dict") or
            not _ps_token_is(tokens[2], "name", b"begin")):
        _fail(tag + "_MAIN_PREFIX")
    main_begin = 2
    main_end = _ps_matching_end(tokens, main_begin, tag + "_MAIN")
    if (main_end != len(tokens) - 3 or
            not _ps_token_is(tokens[main_end - 1], "name", b"currentdict") or
            not _ps_token_is(tokens[main_end + 1], "name", b"currentfile") or
            not _ps_token_is(tokens[main_end + 2], "name", b"eexec") or
            _ps_skip_layout(clear, tokens[-1][3], tag + "_EOF") != len(clear)):
        _fail(tag + "_MAIN_SUFFIX")
    position = main_begin + 1
    seen = set()
    font_name = None
    fontinfo_frame = None
    while position < main_end - 1:
        if not _ps_token_is(tokens[position], "literal"):
            _fail(tag + "_DECLARATION")
        key = tokens[position][1]
        if key in seen:
            _fail(tag + "_DUPLICATE_FIELD")
        if key == b"FontInfo":
            if (position + 4 >= main_end or
                    not _ps_token_is(tokens[position + 1], "integer") or
                    not 1 <= tokens[position + 1][1] <= 32 or
                    not _ps_token_is(tokens[position + 2], "name", b"dict") or
                    not _ps_token_is(tokens[position + 3], "name", b"dup") or
                    not _ps_token_is(tokens[position + 4], "name", b"begin")):
                _fail(tag + "_FONTINFO_PREFIX")
            info_begin = position + 4
            info_end = _ps_matching_end(tokens, info_begin, tag + "_FONTINFO")
            if (info_end + 2 >= main_end or
                    not _ps_token_is(tokens[info_end + 1], "name", b"readonly") or
                    not _ps_token_is(tokens[info_end + 2], "name", b"def")):
                _fail(tag + "_FONTINFO_SUFFIX")
            _validate_type1_fontinfo(
                tokens, info_begin + 1, info_end, tokens[position + 1][1],
                tag + "_FONTINFO",
            )
            fontinfo_frame = (info_begin, info_end)
            position = info_end + 3
        elif key == b"Encoding":
            position = _validate_type1_encoding(clear, tokens, position, tag + "_ENCODING")
        elif key == b"FontName":
            if (position + 2 >= main_end or
                    not _ps_token_is(tokens[position + 1], "literal") or
                    re.fullmatch(rb"(?:[A-Z]{6}\+)?[A-Za-z0-9_.-]{1,127}",
                                 tokens[position + 1][1]) is None or
                    not _ps_token_is(tokens[position + 2], "name", b"def")):
                _fail(tag + "_FONTNAME")
            font_name = tokens[position + 1][1]
            position += 3
        elif key in (b"PaintType", b"FontType"):
            expected = 0 if key == b"PaintType" else 1
            if (position + 2 >= main_end or
                    not _ps_token_is(tokens[position + 1], "integer", expected) or
                    not _ps_token_is(tokens[position + 2], "name", b"def")):
                _fail(tag + "_TYPE_FIELD")
            position += 3
        elif key == b"FontMatrix":
            if position + 3 >= main_end:
                _fail(tag + "_FONTMATRIX")
            values = _ps_numeric_composite(
                clear, tokens[position + 1], b"[", b"]", 6, 6,
                tag + "_FONTMATRIX",
            )
            normalized = tuple(row[1] for row in values)
            if (normalized != (b"0.001", 0, 0, b"0.001", 0, 0) or
                    not _ps_token_is(tokens[position + 2], "name", b"readonly") or
                    not _ps_token_is(tokens[position + 3], "name", b"def")):
                _fail(tag + "_FONTMATRIX")
            position += 4
        elif key == b"FontBBox":
            if position + 3 >= main_end or tokens[position + 1][1] not in (b"{", b"["):
                _fail(tag + "_FONTBBOX")
            opener = tokens[position + 1][1]
            closer = b"}" if opener == b"{" else b"]"
            values = _ps_numeric_composite(
                clear, tokens[position + 1], opener, closer, 4, 4,
                tag + "_FONTBBOX",
            )
            if (any(not _ps_token_is(row, "integer") or
                    not -1_000_000 <= row[1] <= 1_000_000 for row in values) or
                    not _ps_token_is(tokens[position + 2], "name", b"readonly") or
                    not _ps_token_is(tokens[position + 3], "name", b"def")):
                _fail(tag + "_FONTBBOX")
            position += 4
        elif key in (b"StrokeWidth", b"UniqueID", b"FSType"):
            if (position + 2 >= main_end or
                    not _ps_number_token(tokens[position + 1]) or
                    not _ps_token_is(tokens[position + 2], "name", b"def")):
                _fail(tag + "_OPTIONAL_FIELD")
            if (key in (b"UniqueID", b"FSType") and
                    not _ps_token_is(tokens[position + 1], "integer")):
                _fail(tag + "_OPTIONAL_INTEGER")
            position += 3
        else:
            _fail(tag + "_FIELD")
        seen.add(key)
    required = {
        b"FontInfo", b"FontName", b"PaintType", b"FontType",
        b"FontMatrix", b"Encoding", b"FontBBox",
    }
    if (position != main_end - 1 or not required.issubset(seen) or
            font_name is None or fontinfo_frame is None):
        _fail(tag + "_REQUIRED")
    if len(seen) + 2 > tokens[0][1]:
        _fail(tag + "_MAIN_CAPACITY")
    begin_rows = _ps_named_rows(
        tokens, "name", b"begin", 2, tag + "_BEGIN_ROWS",
    )
    end_rows = _ps_named_rows(
        tokens, "name", b"end", 2, tag + "_END_ROWS",
    )
    if (begin_rows != (main_begin, fontinfo_frame[0]) or
            end_rows != (fontinfo_frame[1], main_end)):
        _fail(tag + "_FRAME_CENSUS")
    return font_name


def _type1_code(raw, leniv, aggregate_budget, tag):
    if leniv == -1:
        code = raw
    else:
        if len(raw) <= leniv:
            _fail(tag + "_LENIV_BOUND")
        code = _type1_decrypt(raw, 4330, leniv)
    tokens = []
    position = 0
    while position < len(code):
        value = code[position]
        position += 1
        if 32 <= value <= 246:
            tokens.append(("number", value - 139))
        elif 247 <= value <= 250:
            if position >= len(code):
                _fail(tag + "_NUMBER")
            tokens.append(("number", (value - 247) * 256 + code[position] + 108))
            position += 1
        elif 251 <= value <= 254:
            if position >= len(code):
                _fail(tag + "_NUMBER")
            tokens.append(("number", -(value - 251) * 256 - code[position] - 108))
            position += 1
        elif value == 255:
            if position + 4 > len(code):
                _fail(tag + "_LONG_NUMBER")
            tokens.append(("number", int.from_bytes(
                code[position:position + 4], "big", signed=True,
            )))
            position += 4
        elif value == 12:
            if position >= len(code):
                _fail(tag + "_ESCAPE")
            escaped = code[position]
            position += 1
            if escaped not in (0, 1, 2, 6, 7, 12, 16, 17, 33):
                _fail(tag + "_ESCAPE_OPERATOR")
            tokens.append(("operator", (12, escaped)))
        elif value in (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 21, 22, 30, 31):
            tokens.append(("operator", (value,)))
        else:
            _fail(tag + "_OPERATOR")
        _type1_budget_take(
            aggregate_budget, "charstring_tokens", 1,
            tag + "_AGGREGATE",
        )
        if len(tokens) > 100000:
            _fail(tag + "_TOKEN_LIMIT")
    return tuple(tokens)


def _type1_validate_subr_lexical(tokens, subr_indices, tag):
    if not tokens or tokens[-1] != ("operator", (11,)):
        _fail(tag + "_RETURN")
    literal_depth = 0
    maximum_literal_depth = 0
    for index, token in enumerate(tokens):
        if token == ("operator", (11,)) and index != len(tokens) - 1:
            _fail(tag + "_EARLY_RETURN")
        if token in (("operator", (14,)), ("operator", (12, 6))):
            _fail(tag + "_GLYPH_TERMINAL")
        if token[0] == "number":
            literal_depth += 1
            maximum_literal_depth = max(maximum_literal_depth, literal_depth)
        else:
            if token == ("operator", (10,)) and index:
                previous = tokens[index - 1]
                if previous[0] == "number" and previous[1] not in subr_indices:
                    _fail(tag + "_STATIC_CALL_TARGET")
            if token[1] in ((1,), (3,), (4,), (5,), (6,), (7,), (8,), (9,),
                            (13,), (21,), (22,), (30,), (31,), (12, 0),
                            (12, 1), (12, 2), (12, 7), (12, 33)):
                literal_depth = 0
            elif token[1] in ((10,), (12, 17)):
                literal_depth = max(0, literal_depth - 1)
            elif token[1] == (12, 12):
                literal_depth = max(0, literal_depth - 1)
            elif token[1] == (12, 16):
                literal_depth = 0
    if maximum_literal_depth > 24:
        _fail(tag + "_STACK_LIMIT")


def _type1_numeric_ratio(value):
    if isinstance(value, int):
        return value, 1
    if (isinstance(value, tuple) and len(value) == 3 and
            value[0] == "fraction" and isinstance(value[1], int) and
            isinstance(value[2], int) and value[2] > 1):
        return value[1], value[2]
    return None


def _type1_division_value(left, right):
    right_ratio = _type1_numeric_ratio(right)
    if right_ratio is None or right_ratio[0] == 0:
        return False, None
    left_ratio = _type1_numeric_ratio(left)
    if left_ratio is None:
        return True, None
    numerator = left_ratio[0] * right_ratio[1]
    denominator = left_ratio[1] * right_ratio[0]
    if denominator < 0:
        numerator = -numerator
        denominator = -denominator
    common = math.gcd(numerator, denominator)
    numerator //= common
    denominator //= common
    if numerator.bit_length() > 256 or denominator.bit_length() > 256:
        return False, None
    if denominator == 1:
        return True, numerator
    return True, ("fraction", numerator, denominator)


def _type1_abstract_subr_outputs(program, input_depth, contracts,
                                 local_budget, aggregate_budget, tag):
    simple_arities = {
        (1,): 2, (3,): 2, (4,): 1, (5,): 2, (6,): 1, (7,): 1,
        (8,): 6, (9,): 0, (21,): 2, (22,): 1, (30,): 4, (31,): 4,
        (12, 0): 0, (12, 1): 6, (12, 2): 6, (12, 33): 2,
    }
    states = {(tuple(None for _ in range(input_depth)), ())}
    for token_index, (kind, value) in enumerate(program):
        next_states = set()
        for stack, pending in states:
            local_budget[0] -= 1
            if local_budget[0] < 0:
                _fail(tag + "_ABSTRACT_STEP_LIMIT")
            _type1_budget_take(
                aggregate_budget, "abstract_steps", 1,
                tag + "_AGGREGATE",
            )
            stack = list(stack)
            pending = list(pending)
            if kind == "number":
                if len(stack) < 24:
                    stack.append(value)
                    next_states.add((tuple(stack), tuple(pending)))
                continue
            if value in ((13,), (12, 7), (14,), (12, 6)):
                continue
            if value == (11,):
                if token_index == len(program) - 1 and not pending:
                    next_states.add((tuple(stack), tuple(pending)))
                continue
            if value in simple_arities:
                if len(stack) == simple_arities[value] and not pending:
                    next_states.add(((), ()))
                continue
            if value == (12, 12):
                if len(stack) >= 2:
                    right = stack.pop()
                    left = stack.pop()
                    safe, result = _type1_division_value(left, right)
                    if not safe:
                        continue
                    stack.append(result)
                    next_states.add((tuple(stack), tuple(pending)))
                continue
            if value == (12, 16):
                if len(stack) < 2 or pending:
                    continue
                other = stack.pop()
                count = stack.pop()
                if (not isinstance(other, int) or not isinstance(count, int) or
                        count < 0 or count > len(stack)):
                    continue
                arguments = stack[len(stack) - count:] if count else []
                if (other, count) == (3, 1):
                    results = [arguments[0]]
                elif (other, count) == (0, 3):
                    results = [None, None]
                elif (other, count) in ((1, 0), (2, 0)):
                    results = []
                else:
                    continue
                del stack[len(stack) - count:]
                next_states.add((tuple(stack), tuple(results)))
                continue
            if value == (12, 17):
                if pending and len(stack) < 24:
                    stack.append(pending.pop(0))
                    next_states.add((tuple(stack), tuple(pending)))
                continue
            if value == (10,):
                if not stack or pending:
                    continue
                target = stack.pop()
                if not isinstance(target, int):
                    continue
                for before, after in contracts.get(target, ()):
                    if before == len(stack):
                        next_states.add((tuple(None for _ in range(after)), ()))
                continue
        states = next_states
        if len(states) > 4096:
            _fail(tag + "_ABSTRACT_STATE_LIMIT")
        if not states:
            break
    return frozenset(len(stack) for stack, pending in states if not pending)


def _type1_subr_contracts(subrs, aggregate_budget, tag):
    if len(subrs) > 512:
        _fail(tag + "_SUBR_LIMIT")
    indices = frozenset(subrs)
    contracts = {index: set() for index in indices}
    local_budget = [MAX_TYPE1_ABSTRACT_STEPS]
    iteration_limit = max(2, min(4096, len(indices) * 25 + 2))
    for _ in range(iteration_limit):
        changed = False
        frozen = {index: frozenset(rows) for index, rows in contracts.items()}
        for index in sorted(indices):
            for input_depth in range(25):
                outputs = _type1_abstract_subr_outputs(
                    subrs[index], input_depth, frozen, local_budget,
                    aggregate_budget,
                    tag + "_%d" % index,
                )
                for output_depth in outputs:
                    row = (input_depth, output_depth)
                    if row not in contracts[index]:
                        contracts[index].add(row)
                        changed = True
        if not changed:
            return {index: frozenset(rows) for index, rows in contracts.items()}
    _fail(tag + "_FIXPOINT")


def _type1_execute_glyph(tokens, subrs, aggregate_budget, tag):
    simple_arities = {
        (1,): 2, (3,): 2, (4,): 1, (5,): 2, (6,): 1, (7,): 1,
        (8,): 6, (9,): 0, (13,): 2, (21,): 2, (22,): 1,
        (30,): 4, (31,): 4, (12, 0): 0, (12, 1): 6,
        (12, 2): 6, (12, 7): 4, (12, 33): 2,
    }
    state = {
        "stack": [], "widths": 0, "other_results": [], "steps": 0,
        "glyph_operator_seen": False, "reachable": set(),
    }

    def execute(program, role, active):
        for index, (kind, value) in enumerate(program):
            state["steps"] += 1
            if state["steps"] > 100000:
                _fail(tag + "_STEP_LIMIT")
            _type1_budget_take(
                aggregate_budget, "concrete_steps", 1,
                tag + "_AGGREGATE",
            )
            if kind == "number":
                state["stack"].append(value)
                if len(state["stack"]) > 24:
                    _fail(tag + "_STACK_LIMIT")
                continue
            if role == "glyph" and not state["glyph_operator_seen"]:
                if value not in ((13,), (12, 7)):
                    _fail(tag + "_WIDTH_FIRST")
                state["glyph_operator_seen"] = True
            if value in ((13,), (12, 7)):
                if role != "glyph" or state["widths"]:
                    _fail(tag + "_WIDTH_POSITION")
            if value in simple_arities:
                arity = simple_arities[value]
                if len(state["stack"]) != arity:
                    _fail(tag + "_ARITY")
                state["stack"].clear()
                if value in ((13,), (12, 7)):
                    state["widths"] += 1
                continue
            if value == (10,):
                if not state["stack"] or not isinstance(state["stack"][-1], int):
                    _fail(tag + "_CALLSUBR_OPERAND")
                target = state["stack"].pop()
                if target not in subrs or target in active or len(active) >= 16:
                    _fail(tag + "_CALLSUBR_TARGET")
                state["reachable"].add(target)
                execute(subrs[target], "subr", active + (target,))
                continue
            if value == (11,):
                if role != "subr" or index != len(program) - 1:
                    _fail(tag + "_RETURN")
                return
            if value == (14,):
                if (role != "glyph" or index != len(program) - 1 or
                        state["stack"] or state["other_results"]):
                    _fail(tag + "_ENDCHAR")
                return
            if value == (12, 6):
                if (role != "glyph" or index != len(program) - 1 or
                        len(state["stack"]) != 5 or state["other_results"]):
                    _fail(tag + "_SEAC")
                state["stack"].clear()
                return
            if value == (12, 12):
                if len(state["stack"]) < 2:
                    _fail(tag + "_DIV_ARITY")
                right = state["stack"].pop()
                left = state["stack"].pop()
                safe, result = _type1_division_value(left, right)
                if not safe:
                    _fail(tag + "_DIV_DENOMINATOR")
                state["stack"].append(result)
                continue
            if value == (12, 16):
                if len(state["stack"]) < 2:
                    _fail(tag + "_OTHERSUBR_ARITY")
                other = state["stack"].pop()
                count = state["stack"].pop()
                if (not isinstance(other, int) or not isinstance(count, int) or
                        count < 0 or count > len(state["stack"])):
                    _fail(tag + "_OTHERSUBR_OPERAND")
                arguments = state["stack"][len(state["stack"]) - count:] if count else []
                if (other, count) == (3, 1):
                    results = [arguments[0]]
                elif (other, count) == (0, 3):
                    results = [None, None]
                elif (other, count) in ((1, 0), (2, 0)):
                    results = []
                else:
                    results = None
                if results is None or state["other_results"]:
                    _fail(tag + "_OTHERSUBR_SIGNATURE")
                del state["stack"][len(state["stack"]) - count:]
                state["other_results"] = results
                continue
            if value == (12, 17):
                if not state["other_results"]:
                    _fail(tag + "_POP")
                state["stack"].append(state["other_results"].pop(0))
                if len(state["stack"]) > 24:
                    _fail(tag + "_STACK_LIMIT")
                continue
            _fail(tag + "_EXEC_OPERATOR")
        _fail(tag + "_MISSING_TERMINAL")

    execute(tokens, "glyph", ())
    if state["widths"] != 1:
        _fail(tag + "_WIDTH_CENSUS")
    return frozenset(state["reachable"])


def _type1_binary_span_map(spans, tag):
    result = {}
    for row in spans:
        if row[0] in result:
            _fail(tag + "_DUPLICATE_INTRODUCER")
        result[row[0]] = row
    return result


def _type1_entry_span(decrypted, token, length, role, span_map, used, tag):
    row = span_map.get(token[2])
    if (row is None or row[3] != token[1] or row[4] != role or
            row[2] - row[1] != length or token[2] in used):
        _fail(tag + "_BINARY_SPAN")
    used.add(token[2])
    return memoryview(decrypted)[row[1]:row[2]], row[2]


def _type1_parse_subr_entries(decrypted, tokens, position, capacity,
                               macro_roles, span_map, used, tag):
    read_name, _, put_name = macro_roles
    rows = []
    while position < len(tokens) and _ps_token_is(tokens[position], "name", b"dup"):
        if (position + 4 >= len(tokens) or
                not _ps_token_is(tokens[position + 1], "integer") or
                tokens[position + 1][1] < 0 or
                not _ps_token_is(tokens[position + 2], "integer") or
                tokens[position + 2][1] <= 0 or
                not _ps_token_is(tokens[position + 3], "name", read_name) or
                not _ps_token_is(tokens[position + 4], "name", put_name)):
            break
        index = tokens[position + 1][1]
        length = tokens[position + 2][1]
        intro = tokens[position + 3]
        suffix = tokens[position + 4]
        raw, body_end = _type1_entry_span(
            decrypted, intro, length, b"subr", span_map, used, tag,
        )
        if _ps_skip_layout(decrypted, body_end, tag + "_LAYOUT") != suffix[2]:
            _fail(tag + "_SUFFIX")
        if index >= capacity:
            _fail(tag + "_INDEX")
        rows.append((index, raw))
        if len(rows) > capacity:
            _fail(tag + "_CAPACITY")
        position += 5
    return tuple(rows), position


def _type1_parse_glyph_entries(decrypted, tokens, position, capacity,
                                macro_roles, span_map, used, tag):
    read_name, def_name, put_name = macro_roles
    forbidden_names = frozenset({
        b"end", b"dup", read_name, def_name, put_name,
        b"string", b"currentfile", b"exch", b"readstring", b"pop",
        b"noaccess", b"def", b"put",
    })
    rows = []
    while position < len(tokens):
        if _ps_token_is(tokens[position], "name", b"end"):
            return tuple(rows), position + 1
        use_put = False
        if _ps_token_is(tokens[position], "name", b"dup"):
            use_put = True
            position += 1
        if (position + 3 >= len(tokens) or
                not _ps_token_is(tokens[position], "literal") or
                not _ps_token_is(tokens[position + 1], "integer") or
                tokens[position + 1][1] <= 0 or
                not _ps_token_is(tokens[position + 2], "name", read_name) or
                not _ps_token_is(tokens[position + 3], "name",
                                 put_name if use_put else def_name)):
            _fail(tag + "_ENTRY_OR_END")
        name = tokens[position][1]
        if name in forbidden_names:
            _fail(tag + "_GLYPH_NAME_SHADOW")
        length = tokens[position + 1][1]
        intro = tokens[position + 2]
        suffix = tokens[position + 3]
        raw, body_end = _type1_entry_span(
            decrypted, intro, length, b"glyph", span_map, used, tag,
        )
        if _ps_skip_layout(decrypted, body_end, tag + "_LAYOUT") != suffix[2]:
            _fail(tag + "_SUFFIX")
        rows.append((name, raw))
        if len(rows) > capacity:
            _fail(tag + "_CAPACITY")
        position += 4
    _fail(tag + "_END_MISSING")


def _type1_macro_profile(decrypted, tokens, private_begin, prefix_end, tag):
    profiles = (
        (b"RD", b"ND", b"NP"),
        (b"-|", b"|-", b"|"),
    )
    bodies = (
        b"{stringcurrentfileexchreadstringpop}",
        b"{noaccessdef}",
        b"{noaccessput}",
    )
    matches = []
    all_macro_names = frozenset(name for profile in profiles for name in profile)
    for profile in profiles:
        definitions = {}
        valid = True
        for name, body in zip(profile, bodies):
            rows = _ps_literal_rows(
                tokens, name, 1, tag + "_" + name.hex(),
                start=private_begin + 1, stop=prefix_end,
            )
            if len(rows) != 1:
                valid = False
                break
            index = rows[0]
            if (index + 3 >= prefix_end or
                    not _ps_token_is(tokens[index + 1], "opaque", b"{") or
                    _ps_compact_composite(
                        decrypted, tokens[index + 1], b"{", b"}", 128,
                        tag + "_BODY",
                    ) != body or
                    not _ps_token_is(tokens[index + 2], "name") or
                    tokens[index + 2][1] not in (b"executeonly", b"bind") or
                    not _ps_token_is(tokens[index + 3], "name", b"def")):
                valid = False
                break
            definitions[index] = index + 4
        if valid:
            other_names = all_macro_names.difference(profile)
            other_rows = any(
                _ps_token_is(tokens[index], "literal") and
                tokens[index][1] in other_names
                for index in range(private_begin + 1, prefix_end)
            )
            if not other_rows:
                matches.append((profile, definitions))
    if len(matches) != 1:
        _fail(tag + "_PROFILE")
    return matches[0]


def _validate_type1_othersubrs(decrypted, tokens, position, tag):
    if (position + 2 >= len(tokens) or
            not _ps_token_is(tokens[position], "literal", b"OtherSubrs") or
            not _ps_token_is(tokens[position + 1], "opaque", b"[")):
        _fail(tag + "_PREFIX")
    compact = _ps_compact_composite(
        decrypted, tokens[position + 1], b"[", b"]", 1024,
        tag + "_TEMPLATE",
    )
    base = (
        b"[{}{}{}{systemdict/internaldictknownnot{pop3}"
        b"{1183615869systemdict/internaldictgetexecdup/startlockknown"
        b"{/startlockgetexec}{/strtlckgetexec}ifelse}ifelse}"
    )
    if compact not in (base + b"]", base + b"executeonly]"):
        _fail(tag + "_TEMPLATE")
    return _ps_definition_end(
        tokens, position + 2, frozenset({b"noaccess", b"executeonly"}), tag,
    )


def _validate_type1_private_field(decrypted, tokens, position, tag):
    if (position + 2 >= len(tokens) or
            not _ps_token_is(tokens[position], "literal") or
            tokens[position][1] not in TYPE1_PRIVATE_SIMPLE_FIELDS):
        _fail(tag + "_KEY")
    key = tokens[position][1]
    value = tokens[position + 1]
    if key in (b"BlueValues", b"OtherBlues", b"FamilyBlues", b"FamilyOtherBlues"):
        values = _ps_numeric_composite(
            decrypted, value, b"[", b"]", 2, 64, tag + "_BLUE_ARRAY",
        )
        if len(values) % 2:
            _fail(tag + "_BLUE_PAIRS")
    elif key in (b"StdHW", b"StdVW", b"StemSnapH", b"StemSnapV"):
        _ps_numeric_composite(
            decrypted, value, b"[", b"]", 1, 64, tag + "_STEM_ARRAY",
        )
    elif key in (b"ForceBold", b"RndStemUp"):
        if not (_ps_token_is(value, "name", b"false") or
                _ps_token_is(value, "name", b"true")):
            _fail(tag + "_BOOLEAN")
    elif key == b"MinFeature":
        values = _ps_numeric_composite(
            decrypted, value, b"{", b"}", 2, 2, tag + "_MINFEATURE",
        )
        if any(not _ps_token_is(row, "integer") for row in values):
            _fail(tag + "_MINFEATURE_INTEGER")
    elif key in (b"BlueScale", b"ExpansionFactor"):
        if not _ps_number_token(value):
            _fail(tag + "_REAL")
    elif key in (b"BlueShift", b"BlueFuzz"):
        if not _ps_token_is(value, "integer") or not 0 <= value[1] <= 1000:
            _fail(tag + "_BLUE_INTEGER")
    elif key == b"LanguageGroup":
        if not _ps_token_is(value, "integer") or value[1] not in (0, 1):
            _fail(tag + "_LANGUAGE_GROUP")
    elif key == b"password":
        if not _ps_token_is(value, "integer", 5839):
            _fail(tag + "_PASSWORD")
    elif key == b"lenIV":
        if not _ps_token_is(value, "integer") or not -1 <= value[1] <= 16:
            _fail(tag + "_LENIV")
    elif key == b"UniqueID":
        if (not _ps_token_is(value, "integer") or
                not 0 < value[1] <= 16_777_215):
            _fail(tag + "_UNIQUE_ID")
    else:
        _fail(tag + "_UNHANDLED_FIELD")
    return _ps_definition_end(
        tokens, position + 2, frozenset({b"readonly", b"noaccess"}), tag,
    )


def _validate_type1_eexec(encrypted, aggregate_budget, tag,
                          force_binary=False):
    if not 32 <= len(encrypted) <= MAX_TYPE1_EEXEC_BYTES:
        _fail(tag + "_ENCODED_LIMIT")
    ascii_hex_mode = False
    if not force_binary:
        probe = []
        for value in encrypted:
            if value not in TYPE1_WS:
                probe.append(value)
                if len(probe) == 4:
                    break
        ascii_hex_mode = (
            len(probe) == 4 and
            all(value in b"0123456789abcdefABCDEF" for value in probe)
        )
        del probe
    if ascii_hex_mode:
        decrypted = _type1_ascii_hex_decrypt(
            encrypted, 55665, 4, tag,
        )
    else:
        ciphertext = encrypted
        if not 64 <= len(ciphertext) <= MAX_TYPE1_EEXEC_BYTES:
            _fail(tag + "_CIPHERTEXT")
        decrypted = _type1_decrypt(ciphertext, 55665, 4)
        del ciphertext
    tokens, binary_spans = _ps_scan_type1(
        decrypted, tag + "_POSTSCRIPT", True, 200000, 8192,
        MAX_TYPE1_EEXEC_BYTES, aggregate_budget,
    )
    _reject_type1_semantic_tokens(
        decrypted, binary_spans, tag + "_SEMANTIC_TOKENS",
    )
    _ps_validate_names(tokens, TYPE1_ALLOWED_EEXEC_NAMES, tag + "_NAME")
    _ps_validate_allocations(tokens, 4096, 4096, tag + "_ALLOCATION")
    private_rows = _ps_literal_rows(
        tokens, b"Private", 1, tag + "_PRIVATE_ROWS",
    )
    if len(private_rows) != 1:
        _fail(tag + "_PRIVATE_DECLARATION")
    private_index = private_rows[0]
    if (private_index != 1 or private_index + 4 >= len(tokens) or
            not _ps_token_is(tokens[0], "name", b"dup") or
            not _ps_token_is(tokens[private_index + 1], "integer") or
            not 1 <= tokens[private_index + 1][1] <= 512 or
            not _ps_token_is(tokens[private_index + 2], "name", b"dict") or
            not _ps_token_is(tokens[private_index + 3], "name", b"dup") or
            not _ps_token_is(tokens[private_index + 4], "name", b"begin")):
        _fail(tag + "_PRIVATE_FRAME")
    private_capacity = tokens[private_index + 1][1]
    private_begin = private_index + 4
    private_end = _ps_matching_end(tokens, private_begin, tag + "_PRIVATE_FRAME")
    if (private_end + 14 != len(tokens) or
            not _ps_token_is(tokens[private_end + 1], "name", b"readonly") or
            not _ps_token_is(tokens[private_end + 2], "name", b"put") or
            not _ps_token_is(tokens[private_end + 3], "name", b"noaccess") or
            not _ps_token_is(tokens[private_end + 4], "name", b"put") or
            not _ps_token_is(tokens[private_end + 5], "name", b"dup") or
            not _ps_token_is(tokens[private_end + 6], "literal", b"FontName") or
            not _ps_token_is(tokens[private_end + 7], "name", b"get") or
            not _ps_token_is(tokens[private_end + 8], "name", b"exch") or
            not _ps_token_is(tokens[private_end + 9], "name", b"definefont") or
            not _ps_token_is(tokens[private_end + 10], "name", b"pop") or
            not _ps_token_is(tokens[private_end + 11], "name", b"mark") or
            not _ps_token_is(tokens[private_end + 12], "name", b"currentfile") or
            not _ps_token_is(tokens[private_end + 13], "name", b"closefile") or
            _ps_skip_layout(decrypted, tokens[-1][3], tag + "_EOF") != len(decrypted)):
        _fail(tag + "_PRIVATE_CLOSURE")
    if (_ps_literal_rows(
            tokens, b"FontName", 1, tag + "_FONTNAME_ROWS",
    ) != (private_end + 6,) or _ps_literal_rows(
            tokens, b"FontType", 0, tag + "_FONTTYPE_ROWS",
    )):
        _fail(tag + "_TERMINAL_STRUCTURAL_NAMES")
    leniv_positions = _ps_literal_rows(
        tokens, b"lenIV", 1, tag + "_LENIV_ROWS",
    )
    leniv = 4
    if leniv_positions:
        index = leniv_positions[0]
        if (not private_begin < index < private_end or
                index + 2 >= len(tokens) or
                not _ps_token_is(tokens[index + 1], "integer") or
                not _ps_token_is(tokens[index + 2], "name", b"def")):
            _fail(tag + "_LENIV_GRAMMAR")
        leniv = tokens[index + 1][1]
    if leniv < -1 or leniv > 16:
        _fail(tag + "_LENIV")
    span_map = _type1_binary_span_map(binary_spans, tag + "_SPANS")
    used = set()
    declarations = _ps_literal_rows(
        tokens, b"CharStrings", 1, tag + "_CHARSTRINGS_ROWS",
    )
    if len(declarations) != 1:
        _fail(tag + "_CHARSTRINGS_CENSUS")
    charstrings_index = declarations[0]
    if (not private_begin < charstrings_index < private_end or
            charstrings_index < 2 or charstrings_index + 4 >= len(tokens) or
            not _ps_token_is(tokens[charstrings_index - 2], "integer", 2) or
            not _ps_token_is(tokens[charstrings_index - 1], "name", b"index") or
            not _ps_token_is(tokens[charstrings_index + 1], "integer") or
            not 1 <= tokens[charstrings_index + 1][1] <= 4096 or
            not _ps_token_is(tokens[charstrings_index + 2], "name", b"dict") or
            not _ps_token_is(tokens[charstrings_index + 3], "name", b"dup") or
            not _ps_token_is(tokens[charstrings_index + 4], "name", b"begin")):
        _fail(tag + "_CHARSTRINGS_DECLARATION")
    capacity = tokens[charstrings_index + 1][1]
    charstrings_begin = charstrings_index + 4
    charstrings_end = _ps_matching_end(
        tokens, charstrings_begin, tag + "_CHARSTRINGS_FRAME",
    )
    macro_roles, macro_definitions = _type1_macro_profile(
        decrypted, tokens, private_begin, charstrings_index - 2,
        tag + "_MACROS",
    )
    raw_subrs = ()
    subr_after = None
    subr_positions = _ps_literal_rows(
        tokens, b"Subrs", 1, tag + "_SUBRS_ROWS",
    )
    if subr_positions:
        subrs_index = subr_positions[0]
        if (not private_begin < subrs_index < private_end or
                subrs_index + 2 >= len(tokens) or
                not _ps_token_is(tokens[subrs_index + 1], "integer") or
                not 0 <= tokens[subrs_index + 1][1] <= 512 or
                not _ps_token_is(tokens[subrs_index + 2], "name", b"array")):
            _fail(tag + "_SUBRS_DECLARATION")
        if max(macro_definitions.values()) > subrs_index:
            _fail(tag + "_MACRO_USE_BEFORE_DEFINITION")
        raw_subrs, subr_after = _type1_parse_subr_entries(
            decrypted, tokens, subrs_index + 3, tokens[subrs_index + 1][1],
            macro_roles, span_map, used, tag + "_SUBRS",
        )
        if (subr_after >= len(tokens) or
                not _ps_token_is(tokens[subr_after], "name") or
                tokens[subr_after][1] not in (macro_roles[1], b"def") or
                len(raw_subrs) > tokens[subrs_index + 1][1]):
            _fail(tag + "_SUBRS_CLOSURE")
    if len({index for index, _ in raw_subrs}) != len(raw_subrs):
        _fail(tag + "_SUBR_INDEX")
    begin_rows = _ps_named_rows(
        tokens, "name", b"begin", 2, tag + "_BEGIN_ROWS",
    )
    end_rows = _ps_named_rows(
        tokens, "name", b"end", 2, tag + "_END_ROWS",
    )
    if (begin_rows != (private_begin, charstrings_begin) or
            end_rows != (charstrings_end, private_end) or
            any(not private_begin < position < charstrings_begin
                for position in leniv_positions + subr_positions) or
            (subr_after is not None and subr_after >= charstrings_index)):
        _fail(tag + "_DICTIONARY_FRAME_CLOSURE")
    cursor = private_begin + 1
    simple_fields = set()
    othersubrs_seen = False
    while cursor < charstrings_index - 2:
        if cursor in macro_definitions:
            cursor = macro_definitions[cursor]
            continue
        if _ps_token_is(tokens[cursor], "literal", b"OtherSubrs"):
            if othersubrs_seen:
                _fail(tag + "_OTHERSUBRS_CENSUS")
            cursor = _validate_type1_othersubrs(
                decrypted, tokens, cursor, tag + "_OTHERSUBRS",
            )
            othersubrs_seen = True
            continue
        if _ps_token_is(tokens[cursor], "literal", b"Subrs"):
            if (not subr_positions or cursor != subr_positions[0] or
                    subr_after is None):
                _fail(tag + "_SUBRS_POSITION")
            cursor = subr_after + 1
            continue
        if (_ps_token_is(tokens[cursor], "literal") and
                tokens[cursor][1] in TYPE1_PRIVATE_SIMPLE_FIELDS):
            field = tokens[cursor][1]
            if field in simple_fields:
                _fail(tag + "_PRIVATE_FIELD_CENSUS")
            cursor = _validate_type1_private_field(
                decrypted, tokens, cursor, tag + "_PRIVATE_FIELD",
            )
            simple_fields.add(field)
            continue
        _fail(tag + "_PRIVATE_PRODUCTION")
    if cursor != charstrings_index - 2 or not othersubrs_seen:
        _fail(tag + "_PRIVATE_PRODUCTION_CLOSURE")
    private_definitions = (
        len(macro_definitions) + 1 + len(simple_fields) +
        (1 if subr_positions else 0)
    )
    if private_definitions > private_capacity:
        _fail(tag + "_PRIVATE_CAPACITY")
    rows, glyph_after = _type1_parse_glyph_entries(
        decrypted, tokens, charstrings_index + 5, capacity, macro_roles,
        span_map, used,
        tag + "_GLYPHS",
    )
    if (glyph_after != charstrings_end + 1 or
            charstrings_end + 1 != private_end):
        _fail(tag + "_CHARSTRINGS_CLOSURE")
    if used != set(span_map):
        _fail(tag + "_BINARY_SPAN_CLOSURE")
    subrs = {}
    subr_indices = frozenset(index for index, _ in raw_subrs)
    for subr_index, raw in raw_subrs:
        code = _type1_code(
            raw, leniv, aggregate_budget,
            tag + "_SUBR_%d" % subr_index,
        )
        _type1_validate_subr_lexical(
            code, subr_indices, tag + "_SUBR_%d" % subr_index,
        )
        subrs[subr_index] = code
    names = [name for name, _ in rows]
    if (not rows or len(rows) > capacity or
            len(set(names)) != len(names) or
            names.count(b".notdef") != 1):
        _fail(tag + "_GLYPH_CENSUS")
    if sum(len(raw) for _, raw in raw_subrs) + sum(
            len(raw) for _, raw in rows) > 16 * MIB:
        _fail(tag + "_CHARSTRING_BYTES")
    reachable = set()
    for index, (name, raw) in enumerate(rows):
        code = _type1_code(
            raw, leniv, aggregate_budget,
            tag + "_GLYPH_%d" % index,
        )
        reachable.update(_type1_execute_glyph(
            code, subrs, aggregate_budget,
            tag + "_GLYPH_%d" % index,
        ))
    contracts = _type1_subr_contracts(
        subrs, aggregate_budget, tag + "_SUBR_CONTRACT",
    )
    # Every stored glyph is concretely executed above, so `reachable` is the
    # recursive union of all renderable Subrs and carries the concrete call,
    # step, stack, and aggregate limits.  A Subr outside that union is inert
    # data; its deliberately narrower requirement is lexical closure plus an
    # existential stack-I/O contract, not concrete runtime admissibility.
    for subr_index in sorted(set(subrs) - reachable):
        if not contracts[subr_index]:
            _fail(
                tag + "_UNREACHABLE_SUBR_STACK_CONTRACT_%d" % subr_index,
            )


def _validate_type1_program(payload, dictionary, aggregate_budget, tag):
    if not payload or len(payload) > MAX_TYPE1_PROGRAM_BYTES:
        _fail(tag + "_PAYLOAD_LIMIT")
    lengths = tuple(
        _pdf_integer_value(dictionary.get(key), tag + "_" + key.decode("ascii"))
        for key in (b"Length1", b"Length2", b"Length3")
    )
    if (not 0 < lengths[0] <= MAX_TYPE1_CLEAR_BYTES or
            not 0 < lengths[1] <= MAX_TYPE1_EEXEC_BYTES or
            not 0 <= lengths[2] <= MAX_TYPE1_TAIL_BYTES):
        _fail(tag + "_LENGTHS")
    force_binary = payload.startswith(b"\x80\x01")
    if force_binary:
        position = 0
        segments = []
        terminated = False
        expected_types = (1, 2, 1)
        segment_limits = (
            MAX_TYPE1_CLEAR_BYTES, MAX_TYPE1_EEXEC_BYTES,
            MAX_TYPE1_TAIL_BYTES,
        )
        while position < len(payload):
            if position + 2 > len(payload) or payload[position] != 0x80:
                _fail(tag + "_PFB_MARKER")
            segment_type = payload[position + 1]
            position += 2
            if segment_type == 3:
                if position != len(payload):
                    _fail(tag + "_PFB_TRAILING")
                terminated = True
                break
            if (len(segments) >= len(expected_types) or
                    segment_type != expected_types[len(segments)] or
                    position + 4 > len(payload)):
                _fail(tag + "_PFB_TYPE")
            length = int.from_bytes(payload[position:position + 4], "little")
            position += 4
            if (length <= 0 or length > len(payload) - position or
                    length > segment_limits[len(segments)]):
                _fail(tag + "_PFB_LENGTH")
            segments.append((segment_type, position, position + length))
            position += length
        if (not terminated or not segments or
                tuple(row[0] for row in segments) not in ((1, 2), (1, 2, 1)) or
                tuple(row[2] - row[1] for row in segments) !=
                (lengths if len(segments) == 3 else lengths[:2]) or
                (len(segments) == 2 and lengths[2] != 0)):
            _fail(tag + "_PFB_SEGMENTS")
        clear = payload[segments[0][1]:segments[0][2]]
        encrypted = memoryview(payload)[segments[1][1]:segments[1][2]]
        tail = payload[segments[2][1]:segments[2][2]] if len(segments) == 3 else b""
    else:
        if sum(lengths) != len(payload):
            _fail(tag + "_PFA_LENGTH")
        clear = payload[:lengths[0]]
        encrypted = memoryview(payload)[lengths[0]:lengths[0] + lengths[1]]
        tail = payload[lengths[0] + lengths[1]:]
    if (not 0 < len(clear) <= MAX_TYPE1_CLEAR_BYTES or
            not 32 <= len(encrypted) <= MAX_TYPE1_EEXEC_BYTES or
            len(tail) > MAX_TYPE1_TAIL_BYTES):
        _fail(tag + "_SEGMENT_LIMIT")
    if (not (clear.startswith(b"%!PS-AdobeFont") or clear.startswith(b"%!FontType1")) or
            len(encrypted) < 32 or len(set(encrypted)) < 2):
        _fail(tag + "_PROGRAM")
    _reject_type1_semantic_tokens(clear, (), tag + "_CLEAR_TOKENS")
    clear_tokens, clear_spans = _ps_scan_type1(
        clear, tag + "_CLEAR_POSTSCRIPT", False, 100000, 0,
        MAX_TYPE1_CLEAR_BYTES, aggregate_budget,
    )
    if clear_spans:
        _fail(tag + "_CLEAR_STRUCTURE")
    del clear_spans
    font_name = _validate_type1_clear_skeleton(
        clear, clear_tokens, tag + "_CLEAR_GRAMMAR",
    )
    del clear_tokens, clear
    _validate_type1_eexec(
        encrypted, aggregate_budget, tag + "_EEXEC",
        force_binary=force_binary,
    )
    if tail:
        _reject_type1_semantic_tokens(tail, (), tag + "_TAIL_TOKENS")
        marker = b"cleartomark"
        if tail.count(marker) != 1:
            _fail(tag + "_TAIL_MARKER")
        before, after = tail.split(marker)
        if (not before or before[-1] not in TYPE1_WS or
                any(value not in TYPE1_WS + b"0" for value in before) or
                not 512 <= before.count(b"0") <= 2048 or
                any(value not in TYPE1_WS for value in after)):
            _fail(tag + "_TAIL_GRAMMAR")
    elif lengths[2] != 0:
        _fail(tag + "_TAIL_LENGTH")
    return font_name


def _validate_font_program(data, span_map, stream_id, font_key, font_subtype,
                           expected_font_name, aggregate_budget, tag):
    payload, dictionary_value = _font_program_bytes(
        data, span_map, stream_id, aggregate_budget, tag,
    )
    dictionary = _pdf_dictionary(dictionary_value, tag + "_STREAM_DICTIONARY")
    subtype_value = dictionary.get(b"Subtype")
    stream_subtype = None
    if subtype_value is not None:
        stream_subtype = _pdf_name_value(subtype_value, tag + "_STREAM_SUBTYPE")
    if (font_key != b"FontFile" or font_subtype != b"Type1" or
            stream_subtype is not None):
        _fail(tag + "_FROZEN_TYPE1_SCOPE")
    embedded_name = _validate_type1_program(
        payload, dictionary, aggregate_budget, tag + "_TYPE1",
    )
    if embedded_name != expected_font_name:
        _fail(tag + "_FONTNAME_BINDING")


def _raw_pdf_analysis(data, expected_pages, tag):
    header_match = PDF_HEADER_RE.match(data)
    if header_match is None:
        _fail(tag + "_HEADER")
    header_end = header_match.end()
    del header_match
    trimmed_end = _pdf_rstrip_layout_end(
        data, 0, len(data), tag + "_EOF_LAYOUT",
    )
    if (trimmed_end < len(b"%%EOF") or not data.startswith(
            b"%%EOF", trimmed_end - len(b"%%EOF"), trimmed_end)):
        _fail(tag + "_EOF")
    object_graph_budget = [MAX_PDF_TOKENS]
    spans = _stream_spans(data, object_graph_budget, tag)
    (objects, span_map, structural_pdf, compressed_locations,
     direct_offsets, direct_extents) = _pdf_objects(
        data, spans, object_graph_budget, tag,
    )
    ordered_direct_extents = sorted(direct_extents.values())
    if (not objects or not spans or not ordered_direct_extents or
            ordered_direct_extents[0][0] < header_end or
            not _pdf_layout_only(
                data, header_end, ordered_direct_extents[0][0],
                tag + "_HEADER_GAP",
            )):
        _fail(tag + "_STRUCTURE")
    stream_count = len(spans)
    del ordered_direct_extents, spans
    stream_ids = frozenset(span_map)
    for number in sorted(objects):
        _pdf_reject_actions(
            objects[number], objects, tag + "_ACTION_%d" % number,
        )
    (root_id, pages_root, source_value, info_id,
     xref_stream_ids, eof_marker_position) = _pdf_catalog_pages(
        data, structural_pdf, objects, stream_ids, direct_offsets,
        direct_extents, compressed_locations, span_map, object_graph_budget,
        tag + "_ROOT",
    )
    del structural_pdf, direct_extents, direct_offsets, object_graph_budget
    all_inbound = {}
    for number in sorted(objects):
        _collect_pdf_refs(objects[number], all_inbound, tag + "_OBJECT_REFS")
    if not xref_stream_ids:
        _collect_pdf_refs(source_value, all_inbound, tag + "_TRAILER_REFS")
    del source_value
    if any(target not in objects for target in all_inbound):
        _fail(tag + "_MISSING_REFERENCE_TARGET")
    object_stream_ids = {
        number for number, value in objects.items()
        if _pdf_top_name(value, b"Type") == b"ObjStm"
    }
    objstm_containers = {
        location[0] for location in compressed_locations.values()
    }
    semantic_roots = {root_id}
    if info_id is not None:
        semantic_roots.add(info_id)
    del root_id, info_id
    semantic_reachable = _pdf_reachable_closure(
        objects, semantic_roots, tag + "_SEMANTIC_REACHABILITY",
    )
    physical_roots = object_stream_ids | set(xref_stream_ids)
    if (objstm_containers != object_stream_ids or
            not set(compressed_locations).issubset(semantic_reachable) or
            semantic_reachable.intersection(physical_roots) or
            set(objects) != set(semantic_reachable) | physical_roots):
        _fail(tag + "_OBJECT_REACHABILITY_CLOSURE")
    del (compressed_locations, objstm_containers, semantic_roots,
         semantic_reachable, physical_roots)
    for object_stream_id in object_stream_ids:
        _pdf_closed_dictionary(
            objects[object_stream_id], PDF_OBJSTM_STREAM_KEYS, frozenset(),
            tag + "_OBJSTM_DICTIONARY_%d" % object_stream_id,
        )
    page_numbers, parent_map = _pdf_page_tree(
        objects, stream_ids, pages_root, expected_pages, tag + "_PAGE_TREE",
    )
    descriptor_ids = set()
    descriptor_streams = {}
    descriptor_names = {}
    font_ids = set()
    font_subtypes = {}
    font_descriptors = {}
    font_names = {}
    for number, value in objects.items():
        object_type = _pdf_top_name(value, b"Type")
        if object_type == b"Font":
            if number in stream_ids:
                _fail(tag + "_FONT_STREAM_OBJECT")
            dictionary = _pdf_dictionary(value, tag + "_FONT_DICTIONARY")
            font_ids.add(number)
            subtype = _pdf_name_value(
                dictionary.get(b"Subtype"), tag + "_FONT_SUBTYPE",
            )
            if subtype != b"Type1":
                _fail(tag + "_FROZEN_TYPE1_SUBTYPE")
            font_subtypes[number] = subtype
            font_names[number] = _pdf_name_value(
                dictionary.get(b"BaseFont"), tag + "_BASEFONT",
            )
            if re.fullmatch(
                    rb"(?:[A-Z]{6}\+)?[A-Za-z0-9_.-]{1,127}",
                    font_names[number],
            ) is None:
                _fail(tag + "_BASEFONT_GRAMMAR")
            if b"DescendantFonts" in dictionary:
                _fail(tag + "_LEAF_DESCENDANTS")
            font_descriptors[number] = _pdf_ref_value(
                dictionary.get(b"FontDescriptor"), tag + "_LEAF_DESCRIPTOR",
            )
        if object_type == b"FontDescriptor":
            if number in stream_ids:
                _fail(tag + "_FONT_DESCRIPTOR_STREAM")
            dictionary = _pdf_dictionary(value, tag + "_FONT_DESCRIPTOR_DICTIONARY")
            descriptor_ids.add(number)
            descriptor_names[number] = _pdf_name_value(
                dictionary.get(b"FontName"), tag + "_DESCRIPTOR_FONTNAME",
            )
            if re.fullmatch(
                    rb"(?:[A-Z]{6}\+)?[A-Za-z0-9_.-]{1,127}",
                    descriptor_names[number],
            ) is None:
                _fail(tag + "_DESCRIPTOR_FONTNAME_GRAMMAR")
            font_keys = tuple(
                key for key in (b"FontFile", b"FontFile2", b"FontFile3")
                if key in dictionary
            )
            if font_keys != (b"FontFile",):
                _fail(tag + "_FONTFILE_CENSUS")
            font_key = font_keys[0]
            stream_id = _pdf_ref_value(
                dictionary[font_key], tag + "_FONTFILE_REF",
            )
            if stream_id not in span_map or span_map[stream_id][1] <= span_map[stream_id][0]:
                _fail(tag + "_FONTFILE_STREAM")
            descriptor_streams[number] = (stream_id, font_key)
    resource_ids = set()
    content_stream_ids = set()
    expected_stream_inbound = {}
    for page_number in page_numbers:
        page_dictionary = _pdf_dictionary(
            objects[page_number], tag + "_PAGE_DICTIONARY",
        )
        chain_numbers = [page_number]
        while chain_numbers[-1] != pages_root:
            parent = parent_map.get(chain_numbers[-1])
            if parent is None or len(chain_numbers) > 64:
                _fail(tag + "_PAGE_CHAIN")
            chain_numbers.append(parent)
        chain_dictionaries = [
            _pdf_dictionary(objects[number], tag + "_PAGE_CHAIN_DICTIONARY")
            for number in chain_numbers
        ]
        chain_box_present = False
        for dictionary in chain_dictionaries:
            box_value = dictionary.get(b"MediaBox")
            if box_value is not None:
                if box_value[0] != "array" or len(box_value[1]) != 4:
                    _fail(tag + "_PAGE_MEDIABOX_ARRAY")
                chain_box_present = True
                values = tuple(
                    _pdf_exact_number_value(item, tag + "_MEDIABOX")
                    for item in box_value[1]
                )
                if values != ((0, 1), (0, 1), (612, 1), (792, 1)):
                    _fail(tag + "_MEDIABOX")
            rotate_value = dictionary.get(b"Rotate")
            if (rotate_value is not None and
                    _pdf_exact_number_value(
                        rotate_value, tag + "_ROTATION",
                    ) != (0, 1)):
                _fail(tag + "_ROTATION")
        if not chain_box_present:
            _fail(tag + "_PAGE_MEDIABOX_CHAIN")
        resource_target = None
        for dictionary in chain_dictionaries:
            if b"Resources" in dictionary:
                resource_target = _pdf_ref_value(
                    dictionary[b"Resources"], tag + "_RESOURCE_REF",
                )
                break
        if (resource_target is None or resource_target not in objects or
                resource_target in stream_ids):
            _fail(tag + "_RESOURCE_BINDING")
        resource_ids.add(resource_target)
        contents_value = page_dictionary.get(b"Contents")
        if contents_value is None:
            _fail(tag + "_CONTENTS_CENSUS")
        if contents_value[0] == "ref":
            content_refs = (_pdf_ref_value(contents_value, tag + "_CONTENTS_REF"),)
        elif contents_value[0] == "array":
            content_refs = _pdf_ref_array_value(
                contents_value, tag + "_CONTENTS_%d" % page_number,
            )
        else:
            _fail(tag + "_CONTENTS_GRAMMAR")
        # Conservative frozen acceptance condition: one logical content
        # stream per page.  This fails closed instead of attempting to scan
        # unseparated /Contents-array chunks with reset lexical state.
        if (len(content_refs) != 1 or any(
                value not in span_map or span_map[value][1] <= span_map[value][0]
                for value in content_refs
        )):
            _fail(tag + "_CONTENTS_STREAM")
        for content_ref in content_refs:
            expected_stream_inbound[content_ref] = (
                expected_stream_inbound.get(content_ref, 0) + 1
            )
        content_stream_ids.update(content_refs)
    page_count = len(page_numbers)
    del page_numbers, parent_map, pages_root
    resource_fonts = set()
    for resource_id in sorted(resource_ids):
        resource_fonts.update(_resource_font_refs(
            objects[resource_id], objects, stream_ids,
            tag + "_RESOURCE_%d" % resource_id,
        ))
    del resource_ids
    page_font_subtypes = {b"Type1"}
    if (not resource_fonts or any(font_id not in font_ids for font_id in resource_fonts) or
            any(font_subtypes[font_id] not in page_font_subtypes for font_id in resource_fonts)):
        _fail(tag + "_RESOURCE_FONT_SUBTYPE")
    reachable_fonts = set(resource_fonts)
    pending = list(sorted(reachable_fonts))
    reachable_descriptors = set()
    descriptor_font_subtypes = {}
    while pending:
        font_id = pending.pop()
        if font_id not in font_ids:
            _fail(tag + "_VISIBLE_FONT_REF")
        subtype = font_subtypes[font_id]
        if subtype != b"Type1":
            _fail(tag + "_LEAF_SUBTYPE")
        descriptor = font_descriptors.get(font_id)
        if (descriptor is None or descriptor not in descriptor_names or
                font_names[font_id] != descriptor_names[descriptor]):
            _fail(tag + "_VISIBLE_DESCRIPTOR")
        reachable_descriptors.add(descriptor)
        descriptor_font_subtypes.setdefault(descriptor, set()).add(subtype)
    if (not reachable_fonts or reachable_fonts != font_ids or
            not reachable_descriptors or reachable_descriptors != descriptor_ids or
            set(descriptor_streams) != descriptor_ids):
        _fail(tag + "_FONT_REACHABILITY")
    font_count = len(reachable_fonts)
    descriptor_count = len(descriptor_ids)
    del (font_ids, font_subtypes, font_descriptors, font_names,
         reachable_fonts, reachable_descriptors, descriptor_ids,
         resource_fonts, page_font_subtypes, pending)
    font_stream_ids = {stream_id for stream_id, _ in descriptor_streams.values()}
    font_stream_count = len(font_stream_ids)
    role_sets = (
        set(content_stream_ids), set(font_stream_ids),
        set(object_stream_ids), set(xref_stream_ids),
    )
    covered_stream_ids = set()
    for role_set in role_sets:
        if covered_stream_ids.intersection(role_set):
            _fail(tag + "_STREAM_ROLE_COLLISION")
        covered_stream_ids.update(role_set)
    if (not font_stream_ids or covered_stream_ids != set(stream_ids) or
            not object_stream_ids.issubset(stream_ids)):
        _fail(tag + "_STREAM_ROLE_CLOSURE")
    del role_sets, covered_stream_ids, object_stream_ids, xref_stream_ids
    content_budget = {
        "decoded_bytes": MAX_TOTAL_CONTENT_STREAM_BYTES,
        "tokens": MAX_TOTAL_CONTENT_TOKENS,
    }
    for content_stream_id in sorted(content_stream_ids):
        content_dictionary = _pdf_closed_dictionary(
            objects[content_stream_id], PDF_CONTENT_STREAM_REQUIRED_KEYS,
            PDF_CONTENT_STREAM_OPTIONAL_KEYS,
            tag + "_CONTENT_STREAM_%d" % content_stream_id,
        )
        if (content_dictionary.get(b"Filter") is not None and
                content_dictionary[b"Filter"] != ("name", b"FlateDecode")):
            _fail(tag + "_CONTENT_STREAM_FILTER")
        content_start, content_end, _ = span_map[content_stream_id]
        remaining = content_budget["decoded_bytes"]
        local_limit = min(MAX_CONTENT_STREAM_BYTES, remaining)
        if content_dictionary.get(b"Filter") is None:
            decoded_size = content_end - content_start
            if decoded_size > local_limit:
                _fail(tag + "_CONTENT_STREAM_LIMIT")
            _content_security_scan(
                data, content_budget,
                tag + "_CONTENT_SECURITY_%d" % content_stream_id,
                content_start, content_end,
            )
        else:
            decoded_content = _bounded_flate(
                memoryview(data)[content_start:content_end],
                tag + "_CONTENT_FLATE_%d" % content_stream_id,
                local_limit,
            )
            decoded_size = len(decoded_content)
            _content_security_scan(
                decoded_content, content_budget,
                tag + "_CONTENT_SECURITY_%d" % content_stream_id,
            )
            del decoded_content
        if decoded_size > content_budget["decoded_bytes"]:
            _fail(tag + "_CONTENT_AGGREGATE")
        content_budget["decoded_bytes"] -= decoded_size
    del content_budget, content_stream_ids
    type1_budget = _new_pdf_type1_budget()
    font_program_bindings = {}
    validated_font_streams = set()
    for descriptor in sorted(descriptor_streams):
        stream_id, font_key = descriptor_streams[descriptor]
        expected_stream_inbound[stream_id] = (
            expected_stream_inbound.get(stream_id, 0) + 1
        )
        stream_dictionary = _pdf_closed_dictionary(
            objects[stream_id], PDF_FONTFILE_STREAM_REQUIRED_KEYS,
            PDF_FONTFILE_STREAM_OPTIONAL_KEYS,
            tag + "_FONT_STREAM_DICTIONARY",
        )
        if (stream_dictionary.get(b"Filter") is not None and
                stream_dictionary[b"Filter"] != ("name", b"FlateDecode")):
            _fail(tag + "_FONT_STREAM_FILTER")
        subtypes = descriptor_font_subtypes.get(descriptor, set())
        if subtypes != {b"Type1"}:
            _fail(tag + "_FONT_STREAM_SUBTYPE_BINDING")
        binding = (font_key, b"Type1", descriptor_names[descriptor])
        previous_binding = font_program_bindings.get(stream_id)
        if previous_binding is None:
            font_program_bindings[stream_id] = binding
        elif previous_binding != binding:
            _fail(tag + "_FONT_STREAM_BINDING_CONFLICT")
        if stream_id not in validated_font_streams:
            _validate_font_program(
                data, span_map, stream_id, binding[0], binding[1],
                binding[2], type1_budget,
                tag + "_FONT_PROGRAM_%d" % descriptor,
            )
            validated_font_streams.add(stream_id)
    if validated_font_streams != font_stream_ids:
        _fail(tag + "_FONT_STREAM_VALIDATION_CLOSURE")
    del (objects, descriptor_streams, descriptor_names,
         descriptor_font_subtypes, font_program_bindings,
         validated_font_streams, type1_budget)
    if any(
            all_inbound.get(stream_id, 0) !=
            expected_stream_inbound.get(stream_id, 0)
            for stream_id in stream_ids):
        _fail(tag + "_STREAM_INBOUND_ROLE")
    del all_inbound, expected_stream_inbound, stream_ids
    font_ranges = tuple(
        (span_map[stream_id][0], span_map[stream_id][1])
        for stream_id in font_stream_ids
    )
    del span_map, font_stream_ids
    eof_count, nonfont_eof_position = _scan_pdf_raw_excluding(
        data, font_ranges, tag + "_NONFONT_RAW",
    )
    if eof_count != 1 or nonfont_eof_position != eof_marker_position:
        _fail(tag + "_NONFONT_EOF_CENSUS")
    return (page_count, font_count, descriptor_count, font_stream_count,
            stream_count)


def _mode_pdfraw(args):
    root, pdf_path = args
    expected = FINAL_MAP.get(root)
    if expected is None or pdf_path != expected[4]:
        _usage("PDFRAW_TUPLE")
    pdf, size, _, digest = _read_regular(
        pdf_path, "PDFRAW_PDF", mode=0o600, limit=64 * MIB,
    )
    pdfinfo = _read_receipt_triplet(root, "R060", "pdfinfo", "PDFRAW_INFO_RECEIPT")
    pages, _ = _parse_pdfinfo(pdfinfo, size, "PDFRAW_INFO_PARSE")
    page_objects, fonts, descriptors, streams, all_streams = _raw_pdf_analysis(pdf, pages, "PDFRAW_PARSE")
    return ("root=" + ROOT_CONFIG[root][1] + " pages=" + str(page_objects) +
            " fonts=" + str(fonts) + " descriptors=" + str(descriptors) +
            " font_streams=" + str(streams) + " streams=" + str(all_streams) +
            " bytes=" + str(size) + " sha256=" + digest)


def _mode_sourcefinal(args):
    root = args[0]
    if root not in ROOT_CONFIG:
        _usage("SOURCEFINAL_ROOT")
    _verify_controls_and_sources()
    _verify_validator_copy()
    _verify_root_source_copies(root)
    frame, rows = _root_frame(root, "FINAL", "SOURCEFINAL_ROOT")
    frozen_path = MANIFEST_MAP[(root, "R054")][1]
    frozen, _, _, frozen_hash = _read_regular(
        frozen_path, "SOURCEFINAL_MANIFEST", mode=0o600, limit=256 * KIB,
    )
    if frame != frozen:
        _fail("SOURCEFINAL_MANIFEST_REBIND")
    terminal_frame, terminal_rows = _root_frame(root, "FINAL", "SOURCEFINAL_ROOT_TERMINAL")
    terminal_frozen, _, _, terminal_hash = _read_regular(
        frozen_path, "SOURCEFINAL_MANIFEST_TERMINAL", mode=0o600,
        limit=256 * KIB,
    )
    if (terminal_frame != frame or terminal_rows != rows or terminal_frozen != frozen or
            terminal_hash != frozen_hash or terminal_frame != terminal_frozen):
        _fail("SOURCEFINAL_TERMINAL_VERSION")
    return ("root=" + ROOT_CONFIG[root][1] + " source_files=3 root_rows=" + str(rows) +
            " manifest_sha256=" + frozen_hash)


def _manifest_snapshot_id(manifest_id):
    return {"R024": "R023", "R033": "R023", "R044": "R043", "R054": "R053"}[manifest_id]


def _manifest_projection(root, manifest_id, data, rows, tag):
    snapshot_id = _manifest_snapshot_id(manifest_id)
    snapshot_path = RECORDER_MAP[(root, snapshot_id)]
    snapshot, size, lf, digest = _read_regular(
        snapshot_path, tag + "_SNAPSHOT", mode=0o600, limit=8 * MIB,
    )
    fls_row = rows.get("main.fls")
    expected_prefix = ("main.fls", "regular", str(size), str(lf), "0600", "1", digest)
    if fls_row != expected_prefix:
        _fail(tag + "_REBIND")
    normalized, normalized_hash = _normalized_recorder(snapshot, root, tag + "_NORMALIZE")
    projected_rows = []
    text = data.decode("ascii", "strict")
    for line in _lf_lines(text, data.count(b"\n"), tag + "_LINES"):
        fields = line.split("\t")
        if fields[0] == "main.fls":
            fields[6] = normalized_hash
        projected_rows.append(tuple(fields))
    projection = _frame_rows(projected_rows, tag + "_FRAME")
    return projection, hashlib.sha256(projection).hexdigest(), normalized, normalized_hash


def _compare_manifest_pair(manifest_id, tag):
    left_path = MANIFEST_MAP[(ROOT0, manifest_id)][1]
    right_path = MANIFEST_MAP[(ROOT1, manifest_id)][1]
    left_data, left_rows = _read_manifest(left_path, tag + "_L")
    right_data, right_rows = _read_manifest(right_path, tag + "_R")
    state = MANIFEST_MAP[(ROOT0, manifest_id)][0]
    expected_names = {"."}.union(ROOT_ALLOWED_NAMES[state])
    if set(left_rows) != expected_names or set(right_rows) != expected_names:
        _fail(tag + "_EXPECTED_SET")
    if set(left_rows) != set(right_rows):
        _fail(tag + "_SET")
    if manifest_id == "R009":
        if left_data != right_data:
            _fail(tag + "_RAW")
        digest = hashlib.sha256(left_data).hexdigest()
        return digest, digest, len(left_rows)
    for name in sorted(left_rows):
        if name == "main.fls":
            if left_rows[name][:6] != right_rows[name][:6]:
                _fail(tag + "_FLS_FIELDS")
        elif left_rows[name] != right_rows[name]:
            _fail(tag + "_FIELD_" + name.encode("ascii").hex())
    left_projection, left_hash, left_norm, left_norm_hash = _manifest_projection(
        ROOT0, manifest_id, left_data, left_rows, tag + "_LP")
    right_projection, right_hash, right_norm, right_norm_hash = _manifest_projection(
        ROOT1, manifest_id, right_data, right_rows, tag + "_RP")
    if (left_projection != right_projection or left_hash != right_hash or
            left_norm != right_norm or left_norm_hash != right_norm_hash):
        _fail(tag + "_PROJECTION")
    return left_hash, right_hash, len(left_rows)


def _root_final_summary(root, tag, receipt_cache=None):
    paths = FINAL_MAP[root]
    pdf_size, pdf_lf, pdf_hash = _regular_identity(
        paths[4], tag + "_PDF_IDENTITY", mode=0o600, limit=64 * MIB,
    )
    if receipt_cache is None:
        pdfinfo = _read_receipt_triplet(
            root, "R060", "pdfinfo", tag + "_INFO_RECEIPT",
        )
        info_hash = hashlib.sha256(pdfinfo).hexdigest()
        pdftext = None
        text_hash = None
    else:
        if set(receipt_cache) != {"R060.stdout", "R062.stdout"}:
            _fail(tag + "_RECEIPT_CACHE_SET")
        pdfinfo_record = receipt_cache.pop("R060.stdout")
        pdftext_record = receipt_cache.pop("R062.stdout")
        pdfinfo = pdfinfo_record[0]
        pdftext = pdftext_record[0]
        info_hash = pdfinfo_record[2]
        text_hash = pdftext_record[2]
        del pdfinfo_record, pdftext_record
        if receipt_cache:
            _fail(tag + "_RECEIPT_CACHE_REMAINDER")
    pages, fields = _parse_pdfinfo(pdfinfo, pdf_size, tag + "_INFO_PARSE")
    del pdfinfo
    log, log_size, log_lf, log_hash = _read_regular(
        paths[0], tag + "_LOG", mode=0o600, limit=8 * MIB,
    )
    sentinel, log_pages, warnings, warning_hash, warning_hex = _parse_log(log, pdf_size, pages, tag + "_LOG_PARSE")
    del log
    aux, aux_size, aux_lf, aux_hash = _read_regular(
        paths[1], tag + "_AUX", mode=0o600, limit=4 * MIB,
    )
    bbl, bbl_size, bbl_lf, bbl_hash = _read_regular(
        paths[2], tag + "_BBL", mode=0o600, limit=2 * MIB,
    )
    blg, blg_size, blg_lf, blg_hash = _read_regular(
        paths[3], tag + "_BLG", mode=0o600, limit=512 * KIB,
    )
    _validate_bibliography_bytes(bbl, blg, tag + "_BIB")
    _validate_aux_and_bbl(aux, bbl, pages, tag + "_KEYS")
    del aux, bbl, blg
    if pdftext is None:
        pdftext = _read_receipt_triplet(
            root, "R062", "pdftext", tag + "_TEXT_RECEIPT",
        )
        text_hash = hashlib.sha256(pdftext).hexdigest()
    text_pages, decoded_hash, pre_hash = _parse_pdf_text(pdftext, pages, sentinel, tag + "_TEXT_PARSE")
    del pdftext
    pdf, terminal_pdf_size, terminal_pdf_lf, terminal_pdf_hash = _read_regular(
        paths[4], tag + "_PDF_BYTES", mode=0o600, limit=64 * MIB,
    )
    if ((terminal_pdf_size, terminal_pdf_lf, terminal_pdf_hash) !=
            (pdf_size, pdf_lf, pdf_hash)):
        _fail(tag + "_PDF_IDENTITY_DRIFT")
    raw = _raw_pdf_analysis(pdf, pages, tag + "_RAW_PARSE")
    del pdf
    return (
        sentinel, log_pages, warnings, warning_hash, warning_hex, text_pages, decoded_hash, pre_hash,
        tuple(sorted(fields.items())), raw, log_hash, aux_hash, bbl_hash, blg_hash,
        pdf_hash, info_hash, text_hash,
        (
            ("main.log", "regular", str(log_size), str(log_lf), "0600", "1", log_hash),
            ("main.aux", "regular", str(aux_size), str(aux_lf), "0600", "1", aux_hash),
            ("main.bbl", "regular", str(bbl_size), str(bbl_lf), "0600", "1", bbl_hash),
            ("main.blg", "regular", str(blg_size), str(blg_lf), "0600", "1", blg_hash),
            ("main.pdf", "regular", str(pdf_size), str(pdf_lf), "0600", "1", pdf_hash),
        ),
    )


CROSS_FILE_PAIRS = (
    (ROOT0 + "/main.tex", ROOT1 + "/main.tex", 0o644),
    (ROOT0 + "/math_commands.tex", ROOT1 + "/math_commands.tex", 0o644),
    (ROOT0 + "/references.bib", ROOT1 + "/references.bib", 0o644),
    (ROOT0 + "/main.pdf", ROOT1 + "/main.pdf", 0o600),
    (ROOT0 + "/main.aux", ROOT1 + "/main.aux", 0o600),
    (ROOT0 + "/main.bbl", ROOT1 + "/main.bbl", 0o600),
    (ROOT0 + "/main.blg", ROOT1 + "/main.blg", 0o600),
    (ROOT0 + "/main.log", ROOT1 + "/main.log", 0o600),
)


def _mode_cross(args):
    if args != [CROSS_STAGE]:
        _usage("CROSS_TUPLE")
    _check_inflight_directory(
        CROSS_STAGE, CROSS_STAGE_BEFORE_CROSS_NAMES, "X009", "CROSS_STAGE", 2,
    )
    return _cross_analysis(CROSS_STAGE_BEFORE_CROSS_NAMES, "X009")


def _cross_analysis(completed_cross_names, inflight_ident):
    if ((completed_cross_names, inflight_ident) not in
            ((CROSS_STAGE_BEFORE_CROSS_NAMES, "X009"), (CROSS_STAGE_PRE_NAMES, "X010"))):
        _usage("CROSS_STAGE_NAMES")
    _list_exact_directory(STAGE0, ROOT_STAGE_FINAL_NAMES, "CROSS_STAGE0", 0o700, 2)
    _list_exact_directory(STAGE1, ROOT_STAGE_FINAL_NAMES, "CROSS_STAGE1", 0o700, 2)
    _verify_controls_and_sources()
    _verify_validator_copy()
    _verify_root_source_copies(ROOT0)
    _verify_root_source_copies(ROOT1)
    equal_hashes = []
    for index, (left, right, mode) in enumerate(CROSS_FILE_PAIRS):
        limit = _root_file_cap(left.rsplit("/", 1)[1])
        _, _, digest = _same_regular(
            left, right, "CROSS_RAW_%02d" % index, mode, mode, limit=limit,
        )
        equal_hashes.append(digest)
    recorder_hash_pairs = []
    aggregate_recorder_hashes = []
    for index, ident in enumerate(("R023", "R043", "R053")):
        left_path = RECORDER_MAP[(ROOT0, ident)]
        right_path = RECORDER_MAP[(ROOT1, ident)]
        left, _, _, _ = _read_regular(
            left_path, "CROSS_REC_L_%02d" % index, mode=0o600, limit=8 * MIB,
        )
        right, _, _, _ = _read_regular(
            right_path, "CROSS_REC_R_%02d" % index, mode=0o600, limit=8 * MIB,
        )
        _parse_recorder(ROOT0, ident, left, "CROSS_REC_PARSE_L_%02d" % index)
        _parse_recorder(ROOT1, ident, right, "CROSS_REC_PARSE_R_%02d" % index)
        left_norm, left_norm_hash = _normalized_recorder(left, ROOT0, "CROSS_REC_NORM_L_%02d" % index)
        right_norm, right_norm_hash = _normalized_recorder(right, ROOT1, "CROSS_REC_NORM_R_%02d" % index)
        if left_norm != right_norm or left_norm_hash != right_norm_hash:
            _fail("CROSS_RECORDER_%02d" % index)
        recorder_hash_pairs.append(ident + ":" + left_norm_hash + "/" + right_norm_hash)
        aggregate_recorder_hashes.extend((left_norm_hash, right_norm_hash))
        del left, right, left_norm, right_norm
    manifest_hash_pairs = []
    manifest_row_counts = []
    aggregate_manifest_hashes = []
    total_fields = 0
    for ident in ("R009", "R024", "R033", "R044", "R054"):
        left_digest, right_digest, rows = _compare_manifest_pair(ident, "CROSS_MANIFEST_" + ident)
        manifest_hash_pairs.append(ident + ":" + left_digest + "/" + right_digest)
        aggregate_manifest_hashes.extend((left_digest, right_digest))
        manifest_row_counts.append(rows)
        total_fields += rows * 7
    frame0, _ = _root_frame(ROOT0, "FINAL", "CROSS_ROOT0_FINAL")
    frame1, _ = _root_frame(ROOT1, "FINAL", "CROSS_ROOT1_FINAL")
    frozen0, _, _, _ = _read_regular(
        MANIFEST_MAP[(ROOT0, "R054")][1], "CROSS_FROZEN0", mode=0o600,
        limit=256 * KIB,
    )
    frozen1, _, _, _ = _read_regular(
        MANIFEST_MAP[(ROOT1, "R054")][1], "CROSS_FROZEN1", mode=0o600,
        limit=256 * KIB,
    )
    if frame0 != frozen0 or frame1 != frozen1:
        _fail("CROSS_FINAL_REBIND")
    summary0 = _root_final_summary(ROOT0, "CROSS_SUMMARY0")
    summary1 = _root_final_summary(ROOT1, "CROSS_SUMMARY1")
    if summary0 != summary1:
        _fail("CROSS_SUMMARY")
    compare_receipts = []
    for index, ident in enumerate(CROSS_COMPARE_IDS):
        out = CROSS_STAGE + "/" + ident + ".stdout"
        err = CROSS_STAGE + "/" + ident + ".stderr"
        status_path = CROSS_STAGE + "/" + ident + ".status"
        stdout, _, _, _ = _read_regular(
            out, "CROSS_CMP_OUT_%02d" % index, mode=0o600, limit=0,
        )
        stderr, _, _, _ = _read_regular(
            err, "CROSS_CMP_ERR_%02d" % index, mode=0o600, limit=0,
        )
        status_data, _, _, _ = _read_regular(
            status_path, "CROSS_CMP_STATUS_%02d" % index, mode=0o600, limit=2,
        )
        _validate_receipt_bytes(stdout, stderr, status_data, "silent", "CROSS_CMP_%02d" % index)
        compare_receipts.append((stdout, stderr, status_data))
    _list_exact_directory(STAGE0, ROOT_STAGE_FINAL_NAMES, "CROSS_STAGE0_TERMINAL", 0o700, 2)
    _list_exact_directory(STAGE1, ROOT_STAGE_FINAL_NAMES, "CROSS_STAGE1_TERMINAL", 0o700, 2)
    _check_inflight_directory(
        CROSS_STAGE, completed_cross_names, inflight_ident, "CROSS_STAGE_TERMINAL", 2,
    )
    for index, (left, right, mode) in enumerate(CROSS_FILE_PAIRS):
        limit = _root_file_cap(left.rsplit("/", 1)[1])
        _, _, digest = _same_regular(
            left, right, "CROSS_RAW_TERMINAL_%02d" % index, mode, mode,
            limit=limit,
        )
        if digest != equal_hashes[index]:
            _fail("CROSS_RAW_TERMINAL_VERSION_%02d" % index)
    for index, ident in enumerate(("R023", "R043", "R053")):
        left_path = RECORDER_MAP[(ROOT0, ident)]
        right_path = RECORDER_MAP[(ROOT1, ident)]
        left, _, _, _ = _read_regular(
            left_path, "CROSS_REC_TERMINAL_L_%02d" % index,
            mode=0o600, limit=8 * MIB,
        )
        right, _, _, _ = _read_regular(
            right_path, "CROSS_REC_TERMINAL_R_%02d" % index,
            mode=0o600, limit=8 * MIB,
        )
        _parse_recorder(ROOT0, ident, left, "CROSS_REC_TERMINAL_PARSE_L_%02d" % index)
        _parse_recorder(ROOT1, ident, right, "CROSS_REC_TERMINAL_PARSE_R_%02d" % index)
        left_norm, left_hash = _normalized_recorder(
            left, ROOT0, "CROSS_REC_TERMINAL_NORM_L_%02d" % index,
        )
        right_norm, right_hash = _normalized_recorder(
            right, ROOT1, "CROSS_REC_TERMINAL_NORM_R_%02d" % index,
        )
        terminal_pair = ident + ":" + left_hash + "/" + right_hash
        if left_norm != right_norm or terminal_pair != recorder_hash_pairs[index]:
            _fail("CROSS_RECORDER_TERMINAL_VERSION_%02d" % index)
        del left, right, left_norm, right_norm
    for index, ident in enumerate(("R009", "R024", "R033", "R044", "R054")):
        left_digest, right_digest, rows = _compare_manifest_pair(
            ident, "CROSS_MANIFEST_TERMINAL_" + ident,
        )
        terminal_pair = ident + ":" + left_digest + "/" + right_digest
        if terminal_pair != manifest_hash_pairs[index] or rows != manifest_row_counts[index]:
            _fail("CROSS_MANIFEST_TERMINAL_VERSION_" + ident)
    terminal_frame0, _ = _root_frame(ROOT0, "FINAL", "CROSS_ROOT0_TERMINAL")
    terminal_frame1, _ = _root_frame(ROOT1, "FINAL", "CROSS_ROOT1_TERMINAL")
    terminal_frozen0, _, _, _ = _read_regular(
        MANIFEST_MAP[(ROOT0, "R054")][1], "CROSS_FROZEN0_TERMINAL", mode=0o600,
        limit=256 * KIB,
    )
    terminal_frozen1, _, _, _ = _read_regular(
        MANIFEST_MAP[(ROOT1, "R054")][1], "CROSS_FROZEN1_TERMINAL", mode=0o600,
        limit=256 * KIB,
    )
    if (terminal_frame0 != frame0 or terminal_frame1 != frame1 or
            terminal_frozen0 != frozen0 or terminal_frozen1 != frozen1 or
            terminal_frame0 != terminal_frozen0 or terminal_frame1 != terminal_frozen1):
        _fail("CROSS_ROOT_TERMINAL_VERSION")
    if (_root_final_summary(ROOT0, "CROSS_SUMMARY0_TERMINAL") != summary0 or
            _root_final_summary(ROOT1, "CROSS_SUMMARY1_TERMINAL") != summary1):
        _fail("CROSS_SUMMARY_TERMINAL_VERSION")
    for index, ident in enumerate(CROSS_COMPARE_IDS):
        out = CROSS_STAGE + "/" + ident + ".stdout"
        err = CROSS_STAGE + "/" + ident + ".stderr"
        status_path = CROSS_STAGE + "/" + ident + ".status"
        terminal_receipt = (
            _read_regular(
                out, "CROSS_CMP_TERMINAL_OUT_%02d" % index,
                mode=0o600, limit=0,
            )[0],
            _read_regular(
                err, "CROSS_CMP_TERMINAL_ERR_%02d" % index,
                mode=0o600, limit=0,
            )[0],
            _read_regular(
                status_path, "CROSS_CMP_TERMINAL_STATUS_%02d" % index,
                mode=0o600, limit=2,
            )[0],
        )
        if terminal_receipt != compare_receipts[index]:
            _fail("CROSS_CMP_TERMINAL_VERSION_%02d" % index)
        _validate_receipt_bytes(*terminal_receipt, "silent", "CROSS_CMP_TERMINAL_%02d" % index)
    aggregate_material = equal_hashes + aggregate_recorder_hashes
    aggregate_material.extend(aggregate_manifest_hashes)
    aggregate = hashlib.sha256(("".join(aggregate_material)).encode("ascii")).hexdigest()
    return ("raw_pairs=8 recorder_pairs=3 manifest_pairs=5 projected_fields=" + str(total_fields) +
            " recorder_sha256=" + ",".join(recorder_hash_pairs) +
            " manifest_sha256=" + ",".join(manifest_hash_pairs) +
            " sentinel=" + str(summary0[0]) + " pages=" + str(summary0[1]) +
            " warnings=" + str(summary0[2]) + " aggregate_sha256=" + aggregate)


def _root_receipt_kind(ident, root_label):
    if ident in ROOT_INIT_IDS:
        return "silent"
    if ident in PUBLICATION_IDS:
        return "text"
    if ident == "R060":
        return "pdfinfo"
    if ident == "R062":
        return "pdftext"
    if ident in ROOT_VALIDATOR_MODES:
        expected = [("stage" if ident == "I066" else "root", root_label)]
        if ident in ROOT_VALIDATOR_SECOND_FIELDS:
            name, value = ROOT_VALIDATOR_SECOND_FIELDS[ident].split("=", 1)
            expected.append((name, value))
        return ("validator", ROOT_VALIDATOR_MODES[ident], tuple(expected))
    _fail("ROOT_RECEIPT_ID")


def _cached_receipt(cache, ident, kind, tag):
    try:
        stdout = cache[ident + ".stdout"][0]
        stderr = cache[ident + ".stderr"][0]
        status_data = cache[ident + ".status"][0]
    except KeyError:
        _fail(tag + "_MISSING")
    parsed = _validate_receipt_bytes(stdout, stderr, status_data, kind, tag)
    return stdout, parsed


def _expect_result(values, expected, tag):
    for name, value in expected.items():
        if values is None or values.get(name) != str(value):
            _fail(tag + "_" + name)


def _cached_file_identity(cache, name):
    data, _, digest = cache[name]
    return len(data), data.count(b"\n"), digest


def _validate_stage_bindings(cache, root, parsed, manifests, tag):
    root_label = ROOT_CONFIG[root][1]
    for ident, (data, rows, digest) in manifests.items():
        values = parsed[ident]
        _expect_result(values, {
            "root": root_label, "id": ident, "rows": len(rows),
            "bytes": len(data), "sha256": digest,
        }, tag + "_MANIFEST_" + ident)
    manifest_order = ("R009", "R024", "R033", "R044", "R054")
    for index in range(1, len(manifest_order)):
        previous_id = manifest_order[index - 1]
        current_id = manifest_order[index]
        previous = manifests[previous_id][1]
        current = manifests[current_id][1]
        if current_id == "R024":
            immutable = {".", *CACHE_NAMES, "main.tex", "math_commands.tex", "references.bib"}
            additions = {"main.aux", "main.fls", "main.log", "main.pdf"}
        elif current_id == "R033":
            immutable = set(previous)
            additions = {"main.bbl", "main.blg"}
        else:
            immutable = {".", *CACHE_NAMES, "main.tex", "math_commands.tex",
                         "references.bib", "main.bbl", "main.blg"}
            additions = set()
        if set(current) != set(previous).union(additions):
            _fail(tag + "_MANIFEST_DELTA_" + current_id)
        for name in immutable:
            if previous.get(name) != current.get(name):
                _fail(tag + "_MANIFEST_IMMUTABLE_" + current_id + "_" + name.encode("ascii").hex())
    snapshot_bindings = {
        "R021": ("R024", "main.log"), "R022": ("R024", "main.aux"),
        "R023": ("R024", "main.fls"), "R031": ("R033", "main.bbl"),
        "R032": ("R033", "main.blg"), "R041": ("R044", "main.log"),
        "R042": ("R044", "main.aux"), "R043": ("R044", "main.fls"),
        "R051": ("R054", "main.log"), "R052": ("R054", "main.aux"),
        "R053": ("R054", "main.fls"),
    }
    snapshot_names = {name[:4]: name for name in SNAPSHOT_BASENAMES}
    for ident, (manifest_id, product) in snapshot_bindings.items():
        name = snapshot_names[ident]
        size, lf, digest = _cached_file_identity(cache, name)
        values = parsed[ident]
        _expect_result(values, {
            "root": root_label, "id": ident, "bytes": size, "LF": lf,
            "sha256": digest,
        }, tag + "_SNAPSHOT_" + ident)
        manifest_row = manifests[manifest_id][1].get(product)
        expected_row = (product, "regular", str(size), str(lf), "0600", "1", digest)
        if manifest_row != expected_row:
            _fail(tag + "_SNAPSHOT_MANIFEST_" + ident)
    for ident in ("R023", "R043", "R053"):
        data = cache[snapshot_names[ident]][0]
        local_in, local_out, external = _parse_recorder(root, ident, data, tag + "_RECORDER_" + ident)
        normalized_data, normalized_hash = _normalized_recorder(
            data, root, tag + "_RECORDER_NORM_" + ident,
        )
        del normalized_data
        values = parsed["C" + ident[1:]]
        _expect_result(values, {
            "root": root_label, "id": ident, "bytes": len(data),
            "LF": data.count(b"\n"), "sha256": hashlib.sha256(data).hexdigest(),
            "normalized_sha256": normalized_hash, "local_inputs": local_in,
            "local_outputs": local_out, "external_unique": external,
        }, tag + "_RECORDER_RECEIPT_" + ident)
    bbl = cache[snapshot_names["R031"]][0]
    blg = cache[snapshot_names["R032"]][0]
    items = _validate_bibliography_bytes(bbl, blg, tag + "_BIB_SNAPSHOTS")
    _expect_result(parsed["B032"], {
        "root": root_label, "items": len(items),
        "bbl_sha256": hashlib.sha256(bbl).hexdigest(),
        "blg_sha256": hashlib.sha256(blg).hexdigest(),
    }, tag + "_BIB_RECEIPT")
    r023_size, r023_lf, r023_hash = _cached_file_identity(cache, snapshot_names["R023"])
    _expect_result(parsed["L033"], {
        "root": root_label, "bytes": r023_size, "LF": r023_lf, "sha256": r023_hash,
    }, tag + "_R033LIVE_RECEIPT")
    replay_manifests = {
        "V020P": "R009", "V020Q": "R024", "V030P": "R024", "V030Q": "R033",
        "V040P": "R033", "V040Q": "R044", "V050P": "R044", "V050Q": "R054",
    }
    for receipt_id, manifest_id in replay_manifests.items():
        manifest_data, manifest_rows, manifest_hash = manifests[manifest_id]
        _expect_result(parsed[receipt_id], {
            "root": root_label, "root_rows": len(manifest_rows),
            "root_sha256": manifest_hash, "dependencies": "87/86",
        }, tag + "_REPLAY_" + receipt_id)
    _expect_result(parsed["A000"], {
        "root": root_label, "absent": 1, "stage_empty": 1, "dependencies": "87/86",
    }, tag + "_ABSENT")
    r054_data, r054_rows, r054_hash = manifests["R054"]
    _expect_result(parsed["F055"], {
        "root": root_label, "source_files": 3, "root_rows": len(r054_rows),
        "manifest_sha256": r054_hash,
    }, tag + "_SOURCEFINAL")
    _validate_source_bib_sets()
    summary_receipts = {
        name: cache[name] for name in ("R060.stdout", "R062.stdout")
    }
    cache.clear()
    cache.update(summary_receipts)
    del summary_receipts, data, bbl, blg, manifest_data, r054_data
    summary = _root_final_summary(root, tag + "_FINAL", cache)
    for identity_row in summary[17]:
        if r054_rows.get(identity_row[0]) != identity_row:
            _fail(tag + "_R054_FINAL_IDENTITY_" + identity_row[0].encode("ascii").hex())
    pdf_row = r054_rows["main.pdf"]
    pdf_size = _bounded_decimal(
        pdf_row[2], tag + "_PDF_SIZE", 64 * MIB, positive=True,
    )
    pdf_hash = pdf_row[6]
    _expect_result(parsed["F061"], {
        "root": root_label, "pages": summary[1], "bytes": pdf_size,
        "pdf_sha256": pdf_hash,
    }, tag + "_PDFINFO")
    _expect_result(parsed["F063"], {
        "root": root_label, "pages": summary[5], "reference_page": summary[0],
        "text_sha256": summary[16], "pre_reference_sha256": summary[7],
    }, tag + "_PDFTEXT")
    raw_pages, fonts, descriptors, font_streams, streams = summary[9]
    _expect_result(parsed["F064"], {
        "root": root_label, "pages": raw_pages, "fonts": fonts,
        "descriptors": descriptors, "font_streams": font_streams,
        "streams": streams, "bytes": pdf_size, "sha256": pdf_hash,
    }, tag + "_PDFRAW")
    _expect_result(parsed["F065"], {
        "root": root_label, "sentinel": summary[0], "pages": summary[1],
        "warnings": summary[2], "warning_sha256": summary[3],
        "disposition": "benign-underfull-only", "warning_bytes_hex": summary[4],
        "log_sha256": summary[10], "aux_sha256": summary[11],
        "bbl_sha256": summary[12], "blg_sha256": summary[13],
        "pdf_sha256": summary[14],
    }, tag + "_LOGBIB")


def _inventory_stage(stage, names, ids, tag, inflight_ident=None):
    root_label = "r0" if stage == STAGE0 else "r1" if stage == STAGE1 else None
    if root_label is None:
        _usage("INVENTORY_STAGE")
    root = ROOT0 if stage == STAGE0 else ROOT1
    fd, before, chain = _open_exact_dir(stage, tag, 0o700, 2)
    inventory_rows = []
    cache = {}
    identity_cache = {}
    try:
        inflight_names = (() if inflight_ident is None else
                          (inflight_ident + ".stdout", inflight_ident + ".stderr"))
        _list_fd_exact(fd, tuple(sorted(tuple(names) + inflight_names)), tag)
        aggregate = 0
        caps = {}
        for index, name in enumerate(sorted(tuple(names) + inflight_names)):
            preflight_tag = tag + "_PREFLIGHT_%03d" % index
            st = _stat_at(fd, name, preflight_tag)
            _require_regular_stat(st, 0o600, 1, None, preflight_tag)
            cap = _stage_file_cap(name)
            if st.st_size > cap:
                _fail(preflight_tag + "_LIMIT")
            aggregate += st.st_size
            if aggregate > MAX_STAGE_TOTAL_BYTES:
                _fail(tag + "_AGGREGATE_LIMIT")
            caps[name] = cap
        for index, name in enumerate(inflight_names):
            current, _, _ = _read_regular_at(
                fd, name, tag + "_INFLIGHT_%d" % index, 0o600, 1,
                caps[name],
            )
            if current != b"":
                _fail(tag + "_INFLIGHT_NONEMPTY_%d" % index)
        for index, name in enumerate(sorted(names)):
            data, st, digest = _read_regular_at(
                fd, name, tag + "_%03d" % index, 0o600, 1, caps[name],
            )
            cache[name] = (data, st, digest)
            identity_cache[name] = (
                len(data), data.count(b"\n"), _stat_key(st), digest,
            )
            inventory_rows.append((name, "regular", str(len(data)), str(data.count(b"\n")), "0600", "1", digest))
        parsed = {}
        for ident in ids:
            _, parsed[ident] = _cached_receipt(
                cache, ident, _root_receipt_kind(ident, root_label), tag + "_" + ident,
            )
        manifests = {}
        for basename in MANIFEST_BASENAMES:
            data, _, digest = cache[basename]
            ident = basename[:4]
            manifests[ident] = (data, _parse_manifest(data, tag + "_MANIFEST_" + ident), digest)
        _validate_stage_bindings(cache, root, parsed, manifests, tag + "_BIND")
        if "I066" in ids:
            pre_rows = [row for row in inventory_rows if not row[0].startswith("I066.")]
            pre_frame = _frame_rows(pre_rows, tag + "_PRE_I066")
            _expect_result(parsed["I066"], {
                "stage": root_label, "items": len(pre_rows),
                "framing_bytes": len(pre_frame),
                "inventory_sha256": hashlib.sha256(pre_frame).hexdigest(),
                "root_manifest_sha256": manifests["R054"][2],
            }, tag + "_I066")
        for index, name in enumerate(sorted(names)):
            rebound_size, rebound_lf, rebound_stat, rebound_hash = _regular_identity_at(
                fd, name, tag + "_REBIND_%03d" % index, 0o600,
                caps[name],
            )
            original_size, original_lf, original_stat, original_hash = identity_cache[name]
            if ((rebound_size, rebound_lf, rebound_hash) !=
                    (original_size, original_lf, original_hash) or
                    rebound_stat != original_stat):
                _fail(tag + "_REBIND_MISMATCH_%03d" % index)
        _list_fd_exact(fd, tuple(sorted(tuple(names) + inflight_names)), tag + "_FINAL_NAMES")
        for index, name in enumerate(inflight_names):
            current, _, _ = _read_regular_at(
                fd, name, tag + "_INFLIGHT_FINAL_%d" % index, 0o600, 1,
                caps[name],
            )
            if current != b"":
                _fail(tag + "_INFLIGHT_FINAL_NONEMPTY_%d" % index)
    finally:
        _close_exact_dir(fd, before, stage, tag, chain)
    frame = _frame_rows(inventory_rows, tag + "_FRAME")
    return len(inventory_rows), len(frame), hashlib.sha256(frame).hexdigest()


def _mode_stageinv(args):
    stage, phase = args
    expected = {STAGE0: "r0-pre-I066", STAGE1: "r1-pre-I066"}
    if stage not in expected or phase != expected[stage]:
        _usage("STAGEINV_TUPLE")
    root = ROOT0 if stage == STAGE0 else ROOT1
    _verify_controls_and_sources()
    _verify_validator_copy()
    _verify_root_source_copies(root)
    items, size, digest = _inventory_stage(
        stage, ROOT_STAGE_PRE_NAMES, ROOT_PRE_INVENTORY_IDS, "STAGEINV", "I066",
    )
    frame, _ = _root_frame(root, "FINAL", "STAGEINV_ROOT")
    frozen, _, _, frozen_hash = _read_regular(
        MANIFEST_MAP[(root, "R054")][1], "STAGEINV_FROZEN", mode=0o600,
        limit=256 * KIB,
    )
    if frame != frozen:
        _fail("STAGEINV_ROOT_REBIND")
    terminal_frame, _ = _root_frame(root, "FINAL", "STAGEINV_ROOT_TERMINAL")
    terminal_frozen, _, _, terminal_frozen_hash = _read_regular(
        MANIFEST_MAP[(root, "R054")][1], "STAGEINV_FROZEN_TERMINAL", mode=0o600,
        limit=256 * KIB,
    )
    if (terminal_frame != frame or terminal_frozen != frozen or
            terminal_frozen_hash != frozen_hash or terminal_frame != terminal_frozen):
        _fail("STAGEINV_ROOT_TERMINAL_VERSION")
    terminal_inventory = _inventory_stage(
        stage, ROOT_STAGE_PRE_NAMES, ROOT_PRE_INVENTORY_IDS,
        "STAGEINV_TERMINAL", "I066",
    )
    if terminal_inventory != (items, size, digest):
        _fail("STAGEINV_TERMINAL_INVENTORY_VERSION")
    return ("stage=" + ROOT_CONFIG[root][1] + " items=" + str(items) + " framing_bytes=" +
            str(size) + " inventory_sha256=" + digest + " root_manifest_sha256=" + frozen_hash)


def _read_evidence_receipts(cache, ids, kind, tag):
    parsed = {}
    for ident in ids:
        selected = kind if isinstance(kind, (str, tuple)) else kind(ident)
        _, parsed[ident] = _cached_receipt(cache, ident, selected, tag + "_" + ident)
    return parsed


def _mode_evidence(args):
    evidence, cross_stage = args
    if (evidence, cross_stage) != (EVIDENCE, CROSS_STAGE):
        _usage("EVIDENCE_TUPLE")
    _verify_controls_and_sources()
    _verify_root_source_copies(ROOT0)
    _verify_root_source_copies(ROOT1)
    fd, before, evidence_chain = _open_exact_dir(EVIDENCE, "EVIDENCE_FINAL", 0o700, 5)
    rows = []
    evidence_cache = {}
    stage_stats = {}
    try:
        _list_fd_exact(fd, EVIDENCE_ROOT_NAMES, "EVIDENCE_FINAL")
        validator, st, digest = _read_regular_at(
            fd, "BUILD_VALIDATOR_POSTFAIL.py", "EVIDENCE_VALIDATOR", 0o500, 1,
            _evidence_file_cap("BUILD_VALIDATOR_POSTFAIL.py"),
        )
        evidence_cache["BUILD_VALIDATOR_POSTFAIL.py"] = (validator, st, digest)
        rows.append(("BUILD_VALIDATOR_POSTFAIL.py", "regular", str(len(validator)), str(validator.count(b"\n")), "0500", "1", digest))
        for index, name in enumerate(_receipt_basenames(EVIDENCE_ROOT_IDS)):
            data, child_st, child_hash = _read_regular_at(
                fd, name, "EVIDENCE_ROOT_FILE_%02d" % index, 0o600, 1,
                _evidence_file_cap(name),
            )
            evidence_cache[name] = (data, child_st, child_hash)
            rows.append((name, "regular", str(len(data)), str(data.count(b"\n")), "0600", "1", child_hash))
        _read_evidence_receipts(evidence_cache, EVIDENCE_ROOT_IDS, "silent", "EVIDENCE_ROOT_RECEIPT")
        for name in ("r0", "r1", "cross-root"):
            child = _stat_at(fd, name, "EVIDENCE_STAGE_" + name)
            stage_stats[name] = child
            rows.append(_directory_row(name, child, "EVIDENCE_STAGE_" + name, 2))
        for index, name in enumerate(("BUILD_VALIDATOR_POSTFAIL.py",) + _receipt_basenames(EVIDENCE_ROOT_IDS)):
            mode = 0o500 if name == "BUILD_VALIDATOR_POSTFAIL.py" else 0o600
            rebound, rebound_st, rebound_hash = _read_regular_at(
                fd, name, "EVIDENCE_ROOT_REBIND_%02d" % index, mode, 1,
                _evidence_file_cap(name),
            )
            original, original_st, original_hash = evidence_cache[name]
            if (rebound != original or rebound_hash != original_hash or
                    _stat_key(rebound_st) != _stat_key(original_st)):
                _fail("EVIDENCE_ROOT_REBIND_FILE_%02d" % index)
        for name, original in stage_stats.items():
            rebound = _stat_at(fd, name, "EVIDENCE_STAGE_REBIND_" + name)
            if _stat_key(rebound) != _stat_key(original):
                _fail("EVIDENCE_STAGE_REBIND_" + name)
    finally:
        _close_exact_dir(fd, before, EVIDENCE, "EVIDENCE_FINAL", evidence_chain)
    declared_size, declared_lf, declared_hash = _verify_validator_copy()[0]
    if (len(validator), validator.count(b"\n"), digest) != (
            declared_size, declared_lf, declared_hash):
        _fail("EVIDENCE_VALIDATOR_COPY")
    frame0, _ = _root_frame(ROOT0, "FINAL", "EVIDENCE_ROOT0_FINAL")
    frame1, _ = _root_frame(ROOT1, "FINAL", "EVIDENCE_ROOT1_FINAL")
    frozen0, _, _, _ = _read_regular(
        MANIFEST_MAP[(ROOT0, "R054")][1], "EVIDENCE_ROOT0_MANIFEST",
        mode=0o600, limit=256 * KIB,
    )
    frozen1, _, _, _ = _read_regular(
        MANIFEST_MAP[(ROOT1, "R054")][1], "EVIDENCE_ROOT1_MANIFEST",
        mode=0o600, limit=256 * KIB,
    )
    if frame0 != frozen0 or frame1 != frozen1:
        _fail("EVIDENCE_ROOT_REBIND")
    count0, bytes0, hash0 = _inventory_stage(STAGE0, ROOT_STAGE_FINAL_NAMES, ROOT_FINAL_IDS, "EVIDENCE_STAGE0")
    count1, bytes1, hash1 = _inventory_stage(STAGE1, ROOT_STAGE_FINAL_NAMES, ROOT_FINAL_IDS, "EVIDENCE_STAGE1")
    cross_fd, cross_before, cross_chain = _open_exact_dir(CROSS_STAGE, "EVIDENCE_CROSS", 0o700, 2)
    cross_rows = []
    cross_cache = {}
    try:
        _list_fd_exact(cross_fd, EVIDENCE_CROSS_INFLIGHT_NAMES, "EVIDENCE_CROSS")
        for index, name in enumerate(("X010.stdout", "X010.stderr")):
            current, _, _ = _read_regular_at(
                cross_fd, name, "EVIDENCE_CROSS_INFLIGHT_%d" % index, 0o600, 1,
                0,
            )
            if current != b"":
                _fail("EVIDENCE_CROSS_INFLIGHT_NONEMPTY_%d" % index)
        for index, name in enumerate(CROSS_STAGE_PRE_NAMES):
            data, child_st, child_hash = _read_regular_at(
                cross_fd, name, "EVIDENCE_CROSS_%03d" % index, 0o600, 1,
                _stage_file_cap(name),
            )
            cross_cache[name] = (data, child_st, child_hash)
            cross_rows.append(("cross-root/" + name, "regular", str(len(data)), str(data.count(b"\n")), "0600", "1", child_hash))
        _read_evidence_receipts(cross_cache, CROSS_COMPARE_IDS, "silent", "EVIDENCE_CMP")
        _read_evidence_receipts(cross_cache, ("X009",),
                                ("validator", "CROSS", (("raw_pairs", "8"),)),
                                "EVIDENCE_CROSS_VALIDATOR")
        cross_detail = _cross_analysis(CROSS_STAGE_PRE_NAMES, "X010")
        expected_cross_stdout = ("PASS CROSS " + cross_detail + "\n").encode("ascii")
        if cross_cache["X009.stdout"][0] != expected_cross_stdout:
            _fail("EVIDENCE_CROSS_RECEIPT_REBIND")
        for index, name in enumerate(CROSS_STAGE_PRE_NAMES):
            rebound, rebound_st, rebound_hash = _read_regular_at(
                cross_fd, name, "EVIDENCE_CROSS_REBIND_%03d" % index, 0o600, 1,
                _stage_file_cap(name),
            )
            original, original_st, original_hash = cross_cache[name]
            if (rebound != original or rebound_hash != original_hash or
                    _stat_key(rebound_st) != _stat_key(original_st)):
                _fail("EVIDENCE_CROSS_REBIND_%03d" % index)
        _list_fd_exact(cross_fd, EVIDENCE_CROSS_INFLIGHT_NAMES, "EVIDENCE_CROSS_FINAL_NAMES")
        for index, name in enumerate(("X010.stdout", "X010.stderr")):
            current, _, _ = _read_regular_at(
                cross_fd, name, "EVIDENCE_CROSS_INFLIGHT_FINAL_%d" % index, 0o600, 1,
                0,
            )
            if current != b"":
                _fail("EVIDENCE_CROSS_INFLIGHT_FINAL_NONEMPTY_%d" % index)
    finally:
        _close_exact_dir(cross_fd, cross_before, CROSS_STAGE, "EVIDENCE_CROSS", cross_chain)
    final_stage0 = _inventory_stage(
        STAGE0, ROOT_STAGE_FINAL_NAMES, ROOT_FINAL_IDS, "EVIDENCE_STAGE0_FINAL_REBIND",
    )
    final_stage1 = _inventory_stage(
        STAGE1, ROOT_STAGE_FINAL_NAMES, ROOT_FINAL_IDS, "EVIDENCE_STAGE1_FINAL_REBIND",
    )
    if final_stage0 != (count0, bytes0, hash0) or final_stage1 != (count1, bytes1, hash1):
        _fail("EVIDENCE_STAGE_FINAL_VERSION")
    final_frame0, _ = _root_frame(ROOT0, "FINAL", "EVIDENCE_ROOT0_TERMINAL")
    final_frame1, _ = _root_frame(ROOT1, "FINAL", "EVIDENCE_ROOT1_TERMINAL")
    final_frozen0, _, _, _ = _read_regular(
        MANIFEST_MAP[(ROOT0, "R054")][1], "EVIDENCE_ROOT0_MANIFEST_TERMINAL", mode=0o600,
        limit=256 * KIB,
    )
    final_frozen1, _, _, _ = _read_regular(
        MANIFEST_MAP[(ROOT1, "R054")][1], "EVIDENCE_ROOT1_MANIFEST_TERMINAL", mode=0o600,
        limit=256 * KIB,
    )
    if (final_frame0 != final_frozen0 or final_frame1 != final_frozen1 or
            final_frame0 != frame0 or final_frame1 != frame1 or
            final_frozen0 != frozen0 or final_frozen1 != frozen1):
        _fail("EVIDENCE_ROOT_TERMINAL_VERSION")
    terminal_cross_fd, terminal_cross_before, terminal_cross_chain = _open_exact_dir(
        CROSS_STAGE, "EVIDENCE_CROSS_TERMINAL", 0o700, 2,
    )
    try:
        _list_fd_exact(
            terminal_cross_fd, EVIDENCE_CROSS_INFLIGHT_NAMES, "EVIDENCE_CROSS_TERMINAL",
        )
        for index, name in enumerate(CROSS_STAGE_PRE_NAMES):
            rebound, rebound_st, rebound_hash = _read_regular_at(
                terminal_cross_fd, name, "EVIDENCE_CROSS_TERMINAL_%03d" % index, 0o600, 1,
                _stage_file_cap(name),
            )
            original, original_st, original_hash = cross_cache[name]
            if (rebound != original or rebound_hash != original_hash or
                    _stat_key(rebound_st) != _stat_key(original_st)):
                _fail("EVIDENCE_CROSS_TERMINAL_VERSION_%03d" % index)
        for index, name in enumerate(("X010.stdout", "X010.stderr")):
            current, _, _ = _read_regular_at(
                terminal_cross_fd, name, "EVIDENCE_CROSS_TERMINAL_INFLIGHT_%d" % index,
                0o600, 1, 0,
            )
            if current != b"":
                _fail("EVIDENCE_CROSS_TERMINAL_INFLIGHT_NONEMPTY_%d" % index)
    finally:
        _close_exact_dir(
            terminal_cross_fd, terminal_cross_before, CROSS_STAGE,
            "EVIDENCE_CROSS_TERMINAL", terminal_cross_chain,
        )
    terminal_evidence_fd, terminal_evidence_before, terminal_evidence_chain = _open_exact_dir(
        EVIDENCE, "EVIDENCE_ROOT_TERMINAL", 0o700, 5,
    )
    try:
        _list_fd_exact(terminal_evidence_fd, EVIDENCE_ROOT_NAMES, "EVIDENCE_ROOT_TERMINAL")
        regular_names = ("BUILD_VALIDATOR_POSTFAIL.py",) + _receipt_basenames(EVIDENCE_ROOT_IDS)
        for index, name in enumerate(regular_names):
            mode = 0o500 if name == "BUILD_VALIDATOR_POSTFAIL.py" else 0o600
            rebound, rebound_st, rebound_hash = _read_regular_at(
                terminal_evidence_fd, name, "EVIDENCE_ROOT_TERMINAL_%02d" % index, mode, 1,
                _evidence_file_cap(name),
            )
            original, original_st, original_hash = evidence_cache[name]
            if (rebound != original or rebound_hash != original_hash or
                    _stat_key(rebound_st) != _stat_key(original_st)):
                _fail("EVIDENCE_ROOT_TERMINAL_FILE_%02d" % index)
        for name, original in stage_stats.items():
            rebound = _stat_at(terminal_evidence_fd, name, "EVIDENCE_ROOT_TERMINAL_STAGE_" + name)
            if _stat_key(rebound) != _stat_key(original):
                _fail("EVIDENCE_ROOT_TERMINAL_STAGE_" + name)
    finally:
        _close_exact_dir(
            terminal_evidence_fd, terminal_evidence_before, EVIDENCE,
            "EVIDENCE_ROOT_TERMINAL", terminal_evidence_chain,
        )
    ultimate_stage0 = _inventory_stage(
        STAGE0, ROOT_STAGE_FINAL_NAMES, ROOT_FINAL_IDS, "EVIDENCE_STAGE0_ULTIMATE",
    )
    ultimate_stage1 = _inventory_stage(
        STAGE1, ROOT_STAGE_FINAL_NAMES, ROOT_FINAL_IDS, "EVIDENCE_STAGE1_ULTIMATE",
    )
    if (ultimate_stage0 != (count0, bytes0, hash0) or
            ultimate_stage1 != (count1, bytes1, hash1)):
        _fail("EVIDENCE_STAGE_ULTIMATE_VERSION")
    ultimate_cross_fd, ultimate_cross_before, ultimate_cross_chain = _open_exact_dir(
        CROSS_STAGE, "EVIDENCE_CROSS_ULTIMATE", 0o700, 2,
    )
    try:
        _list_fd_exact(
            ultimate_cross_fd, EVIDENCE_CROSS_INFLIGHT_NAMES,
            "EVIDENCE_CROSS_ULTIMATE",
        )
        for index, name in enumerate(CROSS_STAGE_PRE_NAMES):
            rebound, rebound_st, rebound_hash = _read_regular_at(
                ultimate_cross_fd, name, "EVIDENCE_CROSS_ULTIMATE_%03d" % index,
                0o600, 1, _stage_file_cap(name),
            )
            original, original_st, original_hash = cross_cache[name]
            if (rebound != original or rebound_hash != original_hash or
                    _stat_key(rebound_st) != _stat_key(original_st)):
                _fail("EVIDENCE_CROSS_ULTIMATE_VERSION_%03d" % index)
        for index, name in enumerate(("X010.stdout", "X010.stderr")):
            current, _, _ = _read_regular_at(
                ultimate_cross_fd, name,
                "EVIDENCE_CROSS_ULTIMATE_INFLIGHT_%d" % index, 0o600, 1, 0,
            )
            if current != b"":
                _fail("EVIDENCE_CROSS_ULTIMATE_INFLIGHT_NONEMPTY_%d" % index)
    finally:
        _close_exact_dir(
            ultimate_cross_fd, ultimate_cross_before, CROSS_STAGE,
            "EVIDENCE_CROSS_ULTIMATE", ultimate_cross_chain,
        )
    ultimate_evidence_fd, ultimate_evidence_before, ultimate_evidence_chain = _open_exact_dir(
        EVIDENCE, "EVIDENCE_ROOT_ULTIMATE", 0o700, 5,
    )
    try:
        _list_fd_exact(ultimate_evidence_fd, EVIDENCE_ROOT_NAMES, "EVIDENCE_ROOT_ULTIMATE")
        for index, name in enumerate(("BUILD_VALIDATOR_POSTFAIL.py",) +
                                     _receipt_basenames(EVIDENCE_ROOT_IDS)):
            mode = 0o500 if name == "BUILD_VALIDATOR_POSTFAIL.py" else 0o600
            rebound, rebound_st, rebound_hash = _read_regular_at(
                ultimate_evidence_fd, name, "EVIDENCE_ROOT_ULTIMATE_%02d" % index,
                mode, 1, _evidence_file_cap(name),
            )
            original, original_st, original_hash = evidence_cache[name]
            if (rebound != original or rebound_hash != original_hash or
                    _stat_key(rebound_st) != _stat_key(original_st)):
                _fail("EVIDENCE_ROOT_ULTIMATE_VERSION_%02d" % index)
        for name, original in stage_stats.items():
            rebound = _stat_at(
                ultimate_evidence_fd, name, "EVIDENCE_ROOT_ULTIMATE_STAGE_" + name,
            )
            if _stat_key(rebound) != _stat_key(original):
                _fail("EVIDENCE_ROOT_ULTIMATE_STAGE_" + name)
    finally:
        _close_exact_dir(
            ultimate_evidence_fd, ultimate_evidence_before, EVIDENCE,
            "EVIDENCE_ROOT_ULTIMATE", ultimate_evidence_chain,
        )
    combined = _frame_rows(rows + cross_rows + [
        ("r0-stage-inventory", "regular", str(bytes0), str(count0), "0600", "1", hash0),
        ("r1-stage-inventory", "regular", str(bytes1), str(count1), "0600", "1", hash1),
    ], "EVIDENCE_COMBINED")
    return ("pre_X010=1 root_entries=" + str(len(EVIDENCE_ROOT_NAMES)) +
            " r0_items=" + str(count0) + " r1_items=" + str(count1) +
            " cross_items=" + str(len(CROSS_STAGE_PRE_NAMES)) +
            " inventory_sha256=" + hashlib.sha256(combined).hexdigest())


MODE_HANDLERS = {
    "ABSENT": _mode_absent,
    "REPLAY": _mode_replay,
    "SNAPSHOT": _mode_snapshot,
    "MANIFEST": _mode_manifest,
    "RECORDER": _mode_recorder,
    "R033LIVE": _mode_r033live,
    "BIB": _mode_bib,
    "LOGBIB": _mode_logbib,
    "PDFINFO": _mode_pdfinfo,
    "PDFTEXT": _mode_pdftext,
    "PDFRAW": _mode_pdfraw,
    "SOURCEFINAL": _mode_sourcefinal,
    "CROSS": _mode_cross,
    "STAGEINV": _mode_stageinv,
    "EVIDENCE": _mode_evidence,
}


def _root_stage_before(ident):
    names = []
    for row_ident in ROOT_STAGE_TIMELINE:
        if row_ident == ident:
            return tuple(sorted(names)), ROOT_STAGE_CREATED_FILES.get(ident, ())
        names.extend(_receipt_basenames((row_ident,)))
        names.extend(ROOT_STAGE_CREATED_FILES.get(row_ident, ()))
    _usage("RECEIPT_GUARD_TIMELINE")


def _receipt_guard_target(mode, arguments):
    if mode == "CROSS":
        return CROSS_STAGE, "X009", CROSS_STAGE_BEFORE_CROSS_NAMES, ()
    if mode == "EVIDENCE":
        return CROSS_STAGE, "X010", CROSS_STAGE_PRE_NAMES, ()
    if mode == "STAGEINV":
        completed, created = _root_stage_before("I066")
        return arguments[0], "I066", completed, created
    root = arguments[0]
    if root not in ROOT_CONFIG:
        _usage("RECEIPT_GUARD_ROOT")
    stage = ROOT_CONFIG[root][0]
    if mode == "ABSENT":
        ident = "A000"
    elif mode == "REPLAY":
        checkpoint = arguments[1]
        ident = "V" + checkpoint[1:4] + ("P" if checkpoint.endswith("-pre") else "Q")
    elif mode in ("SNAPSHOT", "MANIFEST"):
        ident = arguments[1]
    elif mode == "RECORDER":
        ident = "C" + arguments[1][1:]
    elif mode == "R033LIVE":
        ident = "L033"
    elif mode == "BIB":
        ident = "B032"
    else:
        ident = {
            "LOGBIB": "F065", "PDFINFO": "F061", "PDFTEXT": "F063",
            "PDFRAW": "F064", "SOURCEFINAL": "F055",
        }.get(mode)
        if ident is None:
            _usage("RECEIPT_GUARD_MODE")
    completed, created = _root_stage_before(ident)
    return stage, ident, completed, created


def _require_absent_at(fd, name, tag):
    try:
        os.stat(name.encode("ascii"), dir_fd=fd, follow_symlinks=False)
    except FileNotFoundError:
        return
    except OSError:
        _fail(tag + "_PROBE")
    _fail(tag + "_PRESENT")


def _check_receipt_guard_stage(guard, tag):
    _check_parent_chain(guard["stage_chain"], tag + "_CHAIN")
    try:
        inside = os.fstat(guard["stage_fd"])
        path_st = _stat_chain_leaf(guard["stage_chain"], tag + "_PATH")
    except OSError:
        _fail(tag + "_FD")
    original = _anchor_key(guard["stage_before"])
    if original != _anchor_key(inside) or _anchor_key(inside) != _anchor_key(path_st):
        _fail(tag + "_VERSION")


def _open_receipt_guard(mode, arguments):
    stage, ident, completed, created = _receipt_guard_target(mode, arguments)
    stage_fd, stage_before, stage_chain = _open_exact_dir(
        stage, "RECEIPT_GUARD_STAGE", 0o700, 2,
    )
    read_fds = []
    try:
        _register_chain_directories(
            stage, stage_chain, "RECEIPT_GUARD_STAGE_CHAIN",
        )
        _register_directory_anchor(stage, stage_before, "RECEIPT_GUARD_STAGE")
        current_names = (ident + ".stdout", ident + ".stderr")
        _list_fd_exact(
            stage_fd, tuple(sorted(tuple(completed) + current_names)),
            "RECEIPT_GUARD_NAMES",
        )
        _require_absent_at(stage_fd, ident + ".status", "RECEIPT_GUARD_STATUS")
        path_stats = []
        process_stats = []
        for index, (name, process_fd) in enumerate(zip(current_names, (1, 2))):
            path_st = _stat_at(stage_fd, name, "RECEIPT_GUARD_PATH_%d" % index)
            _require_regular_stat(path_st, 0o600, 1, 0, "RECEIPT_GUARD_PATH_%d" % index)
            try:
                read_fd = os.open(
                    name.encode("ascii"), os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC,
                    dir_fd=stage_fd,
                )
                read_fds.append(read_fd)
                held_st = os.fstat(read_fd)
                process_st = os.fstat(process_fd)
                flags = fcntl.fcntl(process_fd, fcntl.F_GETFL)
                offset = os.lseek(process_fd, 0, os.SEEK_CUR)
            except OSError:
                _fail("RECEIPT_GUARD_FD_%d" % index)
            _require_regular_stat(process_st, 0o600, 1, 0, "RECEIPT_GUARD_PROCESS_%d" % index)
            if (_stat_key(path_st) != _stat_key(held_st) or
                    _stat_key(held_st) != _stat_key(process_st) or
                    flags & os.O_ACCMODE != os.O_WRONLY or flags & os.O_APPEND or offset != 0):
                _fail("RECEIPT_GUARD_BINDING_%d" % index)
            path_stats.append(path_st)
            process_stats.append(process_st)
        if _anchor_key(process_stats[0]) == _anchor_key(process_stats[1]):
            _fail("RECEIPT_GUARD_DISTINCT")
        return {
            "stage": stage, "ident": ident, "completed": completed,
            "created": created,
            "stage_fd": stage_fd, "stage_before": stage_before,
            "stage_chain": stage_chain, "read_fds": tuple(read_fds),
            "current_names": current_names, "checkpoint": None,
        }
    except Exception:
        for read_fd in reversed(read_fds):
            try:
                os.close(read_fd)
            except OSError:
                pass
        try:
            _close_exact_dir(
                stage_fd, stage_before, stage, "RECEIPT_GUARD_STAGE", stage_chain,
                content_stable=False,
            )
        except CheckFail:
            pass
        raise


def _receipt_guard_check(guard, expected_stdout, tag, include_created=True):
    _check_receipt_guard_stage(guard, tag + "_STAGE_PRE")
    stage_fd = guard["stage_fd"]
    completed = guard["completed"]
    current_names = guard["current_names"]
    pre_names = tuple(sorted(tuple(completed) + current_names))
    terminal_names = tuple(sorted(
        tuple(completed) + tuple(guard["created"]) + current_names,
    ))
    if include_created is None:
        try:
            _list_fd_exact(stage_fd, pre_names, tag + "_NAMES_PRE_BASE")
            include_created = False
        except CheckFail:
            _list_fd_exact(stage_fd, terminal_names, tag + "_NAMES_PRE_CREATED")
            include_created = True
    exact_names = terminal_names if include_created else pre_names
    _list_fd_exact(stage_fd, exact_names, tag + "_NAMES_PRE")
    _require_absent_at(stage_fd, guard["ident"] + ".status", tag + "_STATUS")
    expected_rows = (expected_stdout, b"")
    for index, (name, process_fd, read_fd, expected) in enumerate(
            zip(current_names, (1, 2), guard["read_fds"], expected_rows)):
        try:
            process_st = os.fstat(process_fd)
            held_st = os.fstat(read_fd)
            path_st = _stat_at(stage_fd, name, tag + "_PATH_%d" % index)
            offset = os.lseek(process_fd, 0, os.SEEK_CUR)
            data = os.pread(read_fd, len(expected) + 1, 0)
            flags = fcntl.fcntl(process_fd, fcntl.F_GETFL)
            process_post = os.fstat(process_fd)
            held_post = os.fstat(read_fd)
            path_post = _stat_at(stage_fd, name, tag + "_PATH_POST_%d" % index)
        except OSError:
            _fail(tag + "_FD_%d" % index)
        _require_regular_stat(process_st, 0o600, 1, len(expected), tag + "_PROCESS_%d" % index)
        if (_stat_key(process_st) != _stat_key(held_st) or
                _stat_key(held_st) != _stat_key(path_st) or data != expected or
                offset != len(expected) or flags & os.O_ACCMODE != os.O_WRONLY or
                flags & os.O_APPEND or
                _stat_key(path_st) != _stat_key(process_post) or
                _stat_key(process_post) != _stat_key(held_post) or
                _stat_key(held_post) != _stat_key(path_post)):
            _fail(tag + "_BINDING_%d" % index)
    _list_fd_exact(stage_fd, exact_names, tag + "_NAMES_POST")
    _require_absent_at(stage_fd, guard["ident"] + ".status", tag + "_STATUS_POST")
    _check_receipt_guard_stage(guard, tag + "_STAGE_POST")
    guard["checkpoint"] = (expected_stdout, include_created)
    return include_created


def _close_receipt_guard(guard, tag, suppress=False):
    failure = None
    if not suppress and guard.get("checkpoint") is not None:
        try:
            expected, include_created = guard["checkpoint"]
            _receipt_guard_check(
                guard, expected, tag + "_FINAL", include_created,
            )
        except CheckFail as exc:
            failure = exc.args[0] if exc.args else tag + "_FINAL"
    for read_fd in reversed(guard["read_fds"]):
        try:
            os.close(read_fd)
        except OSError:
            if failure is None:
                failure = tag + "_READ_CLOSE"
    try:
        _close_exact_dir(
            guard["stage_fd"], guard["stage_before"], guard["stage"], tag,
            guard["stage_chain"], content_stable=False,
        )
    except CheckFail:
        if failure is None:
            failure = tag + "_STAGE_CLOSE"
    if failure is not None and not suppress:
        _fail(failure)


def _identity_plan(mode):
    regulars = {}
    symlinks = {}

    def add_regular(path, mode_bits, limit, size, digest):
        row = (mode_bits, limit, size, digest)
        previous = regulars.get(path)
        if previous is not None and previous != row:
            raise RuntimeError("identity regular conflict")
        if path in symlinks:
            raise RuntimeError("identity kind conflict")
        regulars[path] = row

    def add_symlink(path, expected):
        previous = symlinks.get(path)
        if previous is not None and previous != expected:
            raise RuntimeError("identity symlink conflict")
        if path in regulars:
            raise RuntimeError("identity kind conflict")
        symlinks[path] = expected

    add_regular(VALIDATOR_LOCK, 0o644, MIB, None, None)
    add_regular(VALIDATOR_SOURCE, 0o644, MIB, None, None)
    add_regular(VALIDATOR_COPY, 0o500, MIB, None, None)
    for path in sorted(CONTROL_IDENTITIES):
        size, _, mode_bits, _, digest = CONTROL_IDENTITIES[path]
        add_regular(path, mode_bits, max(size, 1), size, digest)
    for path in sorted(SOURCE_IDENTITIES):
        size, _, mode_bits, _, digest = SOURCE_IDENTITIES[path]
        add_regular(path, mode_bits, max(size, 1), size, digest)
    runtime = "/root/miniconda3/bin/python3.12"
    size, mode_bits, _, digest = REGULAR_TOOLS[runtime]
    add_regular(runtime, mode_bits, max(size, 1), size, digest)
    interpreter = "/root/miniconda3/bin/python3"
    add_symlink(interpreter, SYMLINK_TOOLS[interpreter])
    if mode in ("ABSENT", "REPLAY"):
        for path in sorted(REGULAR_TOOLS):
            size, mode_bits, _, digest = REGULAR_TOOLS[path]
            add_regular(path, mode_bits, max(size, 1), size, digest)
        for _, _, target, size, mode_bits, _, digest in DEPENDENCY_ROWS:
            add_regular(target, mode_bits, max(size, 1), size, digest)
        for path in sorted(SYMLINK_TOOLS):
            add_symlink(path, SYMLINK_TOOLS[path])
        for path in sorted(DEPENDENCY_SYMLINKS):
            add_symlink(path, DEPENDENCY_SYMLINKS[path])
    return tuple(sorted(regulars.items())), tuple(sorted(symlinks.items()))


def _identity_parent(path):
    parts = _path_parts(path)
    parent = "/" if len(parts) == 1 else "/" + b"/".join(parts[:-1]).decode("ascii")
    return parent, parts[-1].decode("ascii")


def _hold_symlink_at(parent_fd, name, path, expected, tag):
    if not hasattr(os, "O_PATH"):
        _fail(tag + "_O_PATH")
    size, mode_bits, nlink, raw_target, canonical = expected
    before = _stat_at(parent_fd, name, tag)
    if (not stat.S_ISLNK(before.st_mode) or before.st_size != size or
            stat.S_IMODE(before.st_mode) != mode_bits or before.st_nlink != nlink):
        _fail(tag + "_IDENTITY")
    fd = None
    try:
        got = os.readlink(name.encode("ascii"), dir_fd=parent_fd)
        fd = os.open(
            name.encode("ascii"), os.O_PATH | os.O_NOFOLLOW | os.O_CLOEXEC,
            dir_fd=parent_fd,
        )
        first = os.fstat(fd)
        after = _stat_at(parent_fd, name, tag + "_POST")
    except OSError:
        if fd is not None:
            try:
                os.close(fd)
            except OSError:
                pass
        _fail(tag + "_OPEN_READ")
    if (_stat_key(before) != _stat_key(first) or
            _stat_key(first) != _stat_key(after) or got != raw_target or
            _canonical_hop(path, got, tag, path in DEPENDENCY_SYMLINKS) != canonical):
        os.close(fd)
        _fail(tag + "_VERSION")
    return {
        "path": path, "name": name, "fd": fd, "stat": _stat_key(first),
        "raw": raw_target, "canonical": canonical,
    }


def _check_held_symlink_at(parent_fd, record, tag):
    try:
        held_first = os.fstat(record["fd"])
        path_first = _stat_at(parent_fd, record["name"], tag + "_PATH_PRE")
        raw_first = os.readlink(
            record["name"].encode("ascii"), dir_fd=parent_fd,
        )
        path_middle = _stat_at(parent_fd, record["name"], tag + "_PATH_MID")
        raw_last = os.readlink(
            record["name"].encode("ascii"), dir_fd=parent_fd,
        )
        held_last = os.fstat(record["fd"])
        path_last = _stat_at(parent_fd, record["name"], tag + "_PATH_POST")
    except OSError:
        _fail(tag + "_FD")
    identity = record["stat"]
    if (identity != _stat_key(held_first) or
            _stat_key(held_first) != _stat_key(path_first) or
            _stat_key(path_first) != _stat_key(path_middle) or
            _stat_key(path_middle) != _stat_key(held_last) or
            _stat_key(held_last) != _stat_key(path_last) or
            raw_first != record["raw"] or raw_last != record["raw"] or
            _canonical_hop(
                record["path"], raw_last, tag,
                record["path"] in DEPENDENCY_SYMLINKS,
            ) != record["canonical"]):
        _fail(tag + "_VERSION")


def _open_identity_pool(mode, tag):
    regular_plan, symlink_plan = _identity_plan(mode)
    paths = tuple(path for path, _ in regular_plan + symlink_plan)
    prefixes = {"/"}
    for path in paths:
        parts = _path_parts(path)
        for count in range(1, len(parts)):
            prefixes.add("/" + b"/".join(parts[:count]).decode("ascii"))
    ordered_prefixes = tuple(sorted(
        prefixes, key=lambda value: (0 if value == "/" else value.count("/"), value),
    ))
    if len(ordered_prefixes) + len(regular_plan) + len(symlink_plan) > 512:
        raise RuntimeError("identity pool fd ceiling")
    pool = {"directories": {}, "regulars": [], "symlinks": [], "closed": False}
    try:
        root_fd = None
        try:
            root_fd = os.open(
                b"/", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
            )
            root_stat = os.fstat(root_fd)
        except OSError:
            if root_fd is not None:
                try:
                    os.close(root_fd)
                except OSError:
                    pass
            _fail(tag + "_ROOT")
        pool["directories"]["/"] = {
            "fd": root_fd, "anchor": _anchor_key(root_stat),
            "parent": None, "name": None,
        }
        for index, path in enumerate(ordered_prefixes[1:]):
            parent, name = _identity_parent(path)
            parent_fd = pool["directories"][parent]["fd"]
            child_tag = tag + "_DIR_%03d" % index
            child_fd = None
            try:
                before = os.stat(
                    name.encode("ascii"), dir_fd=parent_fd,
                    follow_symlinks=False,
                )
                if not stat.S_ISDIR(before.st_mode):
                    _fail(child_tag + "_TYPE")
                child_fd = os.open(
                    name.encode("ascii"),
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                    dir_fd=parent_fd,
                )
                inside = os.fstat(child_fd)
            except OSError:
                if child_fd is not None:
                    try:
                        os.close(child_fd)
                    except OSError:
                        pass
                _fail(child_tag + "_OPEN")
            if _stat_key(before) != _stat_key(inside):
                os.close(child_fd)
                _fail(child_tag + "_STABILITY")
            pool["directories"][path] = {
                "fd": child_fd, "anchor": _anchor_key(inside),
                "parent": parent, "name": name,
            }
            _register_directory_anchor(path, inside, child_tag)
        for index, (path, row) in enumerate(regular_plan):
            mode_bits, limit, expected_size, expected_digest = row
            parent, name = _identity_parent(path)
            record = _hold_regular_at(
                pool["directories"][parent]["fd"], name,
                tag + "_REG_%03d" % index, mode_bits, limit,
            )
            record.update({"path": path, "parent": parent})
            pool["regulars"].append(record)
            if ((expected_size is not None and record["size"] != expected_size) or
                    (expected_digest is not None and record["digest"] != expected_digest)):
                _fail(tag + "_REG_%03d_IDENTITY" % index)
        for index, (path, expected) in enumerate(symlink_plan):
            parent, name = _identity_parent(path)
            record = _hold_symlink_at(
                pool["directories"][parent]["fd"], name, path, expected,
                tag + "_LINK_%03d" % index,
            )
            record["parent"] = parent
            pool["symlinks"].append(record)
        return pool
    except Exception:
        _close_identity_pool(pool)
        raise


def _check_identity_pool(pool, tag):
    if pool is None or pool.get("closed"):
        return
    failure = None
    for index, record in enumerate(pool["regulars"]):
        try:
            _check_held_regular_at(
                pool["directories"][record["parent"]]["fd"], record,
                tag + "_REG_%03d" % index,
            )
        except CheckFail as exc:
            if failure is None:
                failure = exc
    for index, record in enumerate(pool["symlinks"]):
        try:
            _check_held_symlink_at(
                pool["directories"][record["parent"]]["fd"], record,
                tag + "_LINK_%03d" % index,
            )
        except CheckFail as exc:
            if failure is None:
                failure = exc
    ordered = sorted(
        pool["directories"],
        key=lambda value: (0 if value == "/" else value.count("/"), value),
        reverse=True,
    )
    for index, path in enumerate(ordered):
        record = pool["directories"][path]
        try:
            inside = os.fstat(record["fd"])
            if record["parent"] is None:
                valid = record["anchor"] == _anchor_key(inside)
            else:
                path_st = _stat_at(
                    pool["directories"][record["parent"]]["fd"],
                    record["name"], tag + "_DIR_%03d" % index,
                )
                valid = (record["anchor"] == _anchor_key(inside) and
                         _anchor_key(inside) == _anchor_key(path_st))
            if not valid:
                _fail(tag + "_DIR_%03d_VERSION" % index)
        except (CheckFail, OSError) as exc:
            current = exc if isinstance(exc, CheckFail) else CheckFail(
                tag + "_DIR_%03d_FD" % index,
            )
            if failure is None:
                failure = current
    if failure is not None:
        raise failure


def _close_identity_pool(pool):
    if pool is None or pool.get("closed"):
        return
    for record in reversed(pool["symlinks"]):
        try:
            os.close(record["fd"])
        except OSError:
            pass
    for record in reversed(pool["regulars"]):
        try:
            os.close(record["fd"])
        except OSError:
            pass
    ordered = sorted(
        pool["directories"],
        key=lambda value: (0 if value == "/" else value.count("/"), value),
        reverse=True,
    )
    for path in ordered:
        try:
            os.close(pool["directories"][path]["fd"])
        except OSError:
            pass
    pool["closed"] = True


def _snapshot_root_state(ident):
    result = {
        "R021": "TEX1", "R022": "TEX1", "R023": "TEX1",
        "R031": "BIB", "R032": "BIB",
        "R041": "TEX2", "R042": "TEX2", "R043": "TEX2",
        "R051": "FINAL", "R052": "FINAL", "R053": "FINAL",
    }.get(ident)
    if result is None:
        _usage("SNAPSHOT_ROOT_STATE")
    return result


def _mode_root_states(mode, arguments):
    if mode == "ABSENT":
        return ((ROOT0, "FINAL"),) if arguments[0] == ROOT1 else ()
    if mode == "REPLAY":
        return ((arguments[0], ROOT_STATES[arguments[1]]),)
    if mode == "SNAPSHOT":
        return ((arguments[0], _snapshot_root_state(arguments[1])),)
    if mode == "MANIFEST":
        return ((arguments[0], MANIFEST_MAP[(arguments[0], arguments[1])][0]),)
    if mode == "RECORDER":
        return ((arguments[0], _snapshot_root_state(arguments[1])),)
    if mode in ("R033LIVE", "BIB"):
        return ((arguments[0], "BIB"),)
    if mode in ("LOGBIB", "PDFINFO", "PDFTEXT", "PDFRAW", "SOURCEFINAL"):
        return ((arguments[0], "FINAL"),)
    if mode == "STAGEINV":
        root = ROOT0 if arguments[0] == STAGE0 else ROOT1
        return ((root, "FINAL"),)
    if mode in ("CROSS", "EVIDENCE"):
        return ((ROOT0, "FINAL"), (ROOT1, "FINAL"))
    return ()


def _open_mode_universes(mode, arguments):
    universes = []
    try:
        cache_children = {name: () for name in CACHE_NAMES}
        for index, (root, state) in enumerate(_mode_root_states(mode, arguments)):
            universes.append(_open_held_universe(
                root, ROOT_ALLOWED_NAMES[state], cache_children, (),
                _root_file_cap, _root_file_mode, MAX_ROOT_TOTAL_BYTES,
                "MODE_HOLD_ROOT_%d" % index, 7,
            ))
        if mode in ("ABSENT", "REPLAY"):
            root = arguments[0]
            children = {"r0": None}
            evidence_nlink = 3
            if root == ROOT1:
                children = {"r0": ROOT_STAGE_FINAL_NAMES, "r1": None}
                evidence_nlink = 4
            universes.append(_open_held_universe(
                EVIDENCE, EVIDENCE_ROOT_AT_ABSENT[root], children, (),
                _evidence_file_cap, _evidence_file_mode,
                MAX_EVIDENCE_REGULAR_BYTES, "MODE_HOLD_ABSENT_EVIDENCE",
                evidence_nlink,
            ))
            if root == ROOT1:
                universes.append(_open_held_universe(
                    STAGE0, ROOT_STAGE_FINAL_NAMES, {}, (),
                    _stage_file_cap, _stage_file_mode, MAX_STAGE_TOTAL_BYTES,
                    "MODE_HOLD_ABSENT_R0_STAGE", 2,
                ))
        if mode == "EVIDENCE":
            universes.append(_open_held_universe(
                EVIDENCE, EVIDENCE_ROOT_NAMES,
                {"r0": None, "r1": None, "cross-root": None}, (),
                _evidence_file_cap, _evidence_file_mode,
                MAX_EVIDENCE_REGULAR_BYTES, "MODE_HOLD_EVIDENCE", 5,
            ))
        if mode in ("CROSS", "EVIDENCE"):
            for index, stage in enumerate((STAGE0, STAGE1)):
                universes.append(_open_held_universe(
                    stage, ROOT_STAGE_FINAL_NAMES, {}, (),
                    _stage_file_cap, _stage_file_mode, MAX_STAGE_TOTAL_BYTES,
                    "MODE_HOLD_STAGE_%d" % index, 2,
                ))
        elif mode == "STAGEINV":
            current = ("I066.stdout", "I066.stderr")
            universes.append(_open_held_universe(
                arguments[0], tuple(sorted(ROOT_STAGE_PRE_NAMES + current)), {}, current,
                _stage_file_cap, _stage_file_mode, MAX_STAGE_TOTAL_BYTES,
                "MODE_HOLD_STAGEINV", 2,
            ))
        if mode == "CROSS":
            current = ("X009.stdout", "X009.stderr")
            universes.append(_open_held_universe(
                CROSS_STAGE,
                tuple(sorted(CROSS_STAGE_BEFORE_CROSS_NAMES + current)), {}, current,
                _stage_file_cap, _stage_file_mode, MAX_CROSS_TOTAL_BYTES,
                "MODE_HOLD_CROSS", 2,
            ))
        elif mode == "EVIDENCE":
            current = ("X010.stdout", "X010.stderr")
            universes.append(_open_held_universe(
                CROSS_STAGE, EVIDENCE_CROSS_INFLIGHT_NAMES, {}, current,
                _stage_file_cap, _stage_file_mode, MAX_CROSS_TOTAL_BYTES,
                "MODE_HOLD_EVIDENCE_CROSS", 2,
            ))
        return universes
    except Exception:
        for index, universe in reversed(tuple(enumerate(universes))):
            _check_close_held_universe(
                universe, "MODE_HOLD_CLEAN_%02d" % index, suppress=True,
            )
        raise


def _post_handler_hold_rows(mode, arguments):
    paths = []
    if mode == "SNAPSHOT":
        paths.append(arguments[3])
    elif mode == "MANIFEST":
        _, _, destination = arguments
        paths.append(destination)
    return tuple(
        (path, 0o600, _stage_file_cap(path.rsplit("/", 1)[1]), None, None)
        for path in paths
    )


def _pre_handler_hold_rows(mode, arguments):
    paths = []
    if mode == "MANIFEST":
        root, ident, _ = arguments
        previous_ids = {"R024": "R009", "R033": "R024", "R044": "R033", "R054": "R044"}
        if ident in previous_ids:
            paths.append(MANIFEST_MAP[(root, previous_ids[ident])][1])
    elif mode == "RECORDER":
        paths.append(arguments[2])
    elif mode == "R033LIVE":
        paths.append(arguments[2])
    elif mode == "BIB":
        paths.extend(arguments[3:5])
    elif mode == "LOGBIB":
        paths.extend(_receipt_paths(arguments[0], "R060"))
    elif mode == "PDFINFO":
        paths.extend(_receipt_paths(arguments[0], "R060"))
    elif mode == "PDFTEXT":
        paths.extend(_receipt_paths(arguments[0], "R060"))
        paths.extend(_receipt_paths(arguments[0], "R062"))
    elif mode == "PDFRAW":
        paths.extend(_receipt_paths(arguments[0], "R060"))
    elif mode == "SOURCEFINAL":
        paths.append(MANIFEST_MAP[(arguments[0], "R054")][1])
    unique_paths = tuple(dict.fromkeys(paths))
    return tuple(
        (path, 0o600, _stage_file_cap(path.rsplit("/", 1)[1]), None, None)
        for path in unique_paths
    )


def _check_mode_universes(universes, tag):
    failure = None
    for index, universe in enumerate(universes):
        try:
            _check_held_universe(universe, tag + "_%02d" % index)
        except CheckFail as exc:
            if failure is None:
                failure = exc
    if failure is not None:
        raise failure


def _close_mode_universes(universes):
    for universe in reversed(universes):
        _close_held_universe(universe)


def _check_close_mode_universes(universes, tag, suppress=False):
    failure = None
    try:
        _check_mode_universes(universes, tag)
    except CheckFail as exc:
        failure = exc
    _close_mode_universes(universes)
    if failure is not None and not suppress:
        raise failure


def _terminal_recompute(mode, arguments, detail):
    if mode == "SNAPSHOT":
        root, ident, source, destination = arguments
        source_limit = _root_file_cap(source.rsplit("/", 1)[1])
        destination_limit = _stage_file_cap(destination.rsplit("/", 1)[1])
        if source_limit != destination_limit:
            raise RuntimeError("terminal snapshot cap mismatch")
        source_data, size, lf, digest = _read_regular(
            source, "TERMINAL_SNAPSHOT_SOURCE", mode=0o600,
            limit=source_limit,
        )
        destination_data, destination_size, destination_lf, destination_hash = _read_regular(
            destination, "TERMINAL_SNAPSHOT_DEST", mode=0o600,
            limit=destination_limit,
        )
        if (source_data != destination_data or
                (size, lf, digest) != (destination_size, destination_lf, destination_hash)):
            _fail("TERMINAL_SNAPSHOT_BINDING")
        rebound = ("root=" + ROOT_CONFIG[root][1] + " id=" + ident +
                   " bytes=" + str(size) + " LF=" + str(lf) + " sha256=" + digest)
    elif mode == "MANIFEST":
        root, ident, destination = arguments
        state = MANIFEST_MAP[(root, ident)][0]
        frame, count = _root_frame(root, state, "TERMINAL_MANIFEST_ROOT")
        destination_data, size, lf, digest = _read_regular(
            destination, "TERMINAL_MANIFEST_DEST", mode=0o600,
            limit=256 * KIB,
        )
        if destination_data != frame or lf != count:
            _fail("TERMINAL_MANIFEST_BINDING")
        _check_manifest_transition(
            root, ident, destination_data, "TERMINAL_MANIFEST_TRANSITION",
        )
        final_destination, final_size, final_lf, final_hash = _read_regular(
            destination, "TERMINAL_MANIFEST_DEST_FINAL", mode=0o600,
            limit=256 * KIB,
        )
        if (final_destination != destination_data or
                (final_size, final_lf, final_hash) != (size, lf, digest)):
            _fail("TERMINAL_MANIFEST_DEST_VERSION")
        rebound = ("root=" + ROOT_CONFIG[root][1] + " id=" + ident +
                   " rows=" + str(count) + " bytes=" + str(size) + " sha256=" + digest)
    else:
        rebound = MODE_HANDLERS[mode](arguments)
    if rebound != detail:
        _fail("TERMINAL_RECOMPUTE_" + mode)


def _encode_result(prefix, detail):
    if not isinstance(detail, str) or detail == "" or "\n" in detail or "\r" in detail:
        _fail("RESULT_GRAMMAR")
    try:
        encoded = (prefix + " " + detail + "\n").encode("ascii", "strict")
    except UnicodeEncodeError:
        _fail("RESULT_ASCII")
    if len(encoded) > MAX_DYNAMIC_BYTES:
        _fail("RESULT_LIMIT")
    return encoded


def _write_stdout(encoded):
    offset = 0
    view = memoryview(encoded)
    try:
        while offset < len(view):
            written = os.write(1, view[offset:])
            if written <= 0:
                return False
            offset += written
    except OSError:
        return False
    return True


def _failure_bytes(kind, tag):
    if (not isinstance(tag, str) or tag == "" or "\n" in tag or "\r" in tag):
        return b"FAIL internal=RESULT_GRAMMAR\n"
    else:
        try:
            return ("FAIL " + kind + "=" + tag + "\n").encode("ascii", "strict")
        except UnicodeEncodeError:
            return b"FAIL internal=RESULT_ASCII\n"


def _guarded_failure(guard, encoded, tag):
    include_created = _receipt_guard_check(
        guard, b"", tag + "_PRE", include_created=None,
    )
    if not _write_stdout(encoded):
        return False
    try:
        os.fsync(1)
        os.fsync(2)
    except OSError:
        return False
    _receipt_guard_check(
        guard, encoded, tag + "_POST", include_created=include_created,
    )
    _close_receipt_guard(guard, tag + "_CLOSE")
    return True


def _check_all_holds(post_handler_hold, pre_handler_hold, absence_hold,
                     mode_universes, identity_hold, tag):
    failure = None
    checks = (
        (lambda: _check_held_group(post_handler_hold, tag + "_POST")),
        (lambda: _check_held_group(pre_handler_hold, tag + "_PRE")),
        (lambda: None if absence_hold is None else
         _check_held_absence(absence_hold, tag + "_ABSENCE")),
        (lambda: _check_mode_universes(mode_universes, tag + "_UNIVERSE")),
        (lambda: _check_identity_pool(identity_hold, tag + "_IDENTITY")),
    )
    for check in checks:
        try:
            check()
        except CheckFail as exc:
            if failure is None:
                failure = exc
    if failure is not None:
        raise failure


def _close_all_holds(post_handler_hold, pre_handler_hold, absence_hold,
                     mode_universes, identity_hold):
    _close_held_group(post_handler_hold)
    _close_held_group(pre_handler_hold)
    if absence_hold is not None:
        _close_held_absence(absence_hold)
    _close_mode_universes(mode_universes)
    _close_identity_pool(identity_hold)


def _check_close_all_holds(post_handler_hold, pre_handler_hold, absence_hold,
                           mode_universes, identity_hold, tag, suppress=False):
    failure = None
    try:
        _check_all_holds(
            post_handler_hold, pre_handler_hold, absence_hold,
            mode_universes, identity_hold, tag,
        )
    except CheckFail as exc:
        failure = exc
    _close_all_holds(
        post_handler_hold, pre_handler_hold, absence_hold,
        mode_universes, identity_hold,
    )
    if failure is not None and not suppress:
        raise failure


def main(argv):
    guard = None
    identity_hold = None
    mode_universes = []
    pre_handler_hold = []
    post_handler_hold = []
    absence_hold = None
    emitted = False
    holds_closed = False
    guard_expected = False
    try:
        if (len(MODE_ARITY) != 15 or set(MODE_ARITY) != set(MODE_HANDLERS) or
                set(MODE_ARITY) != set(VALIDATOR_RESULT_FIELDS) or
                len(EXACT_ARGV_ROWS) != 74 or ACTIVE_DIRECTORY_ANCHORS or
                ACTIVE_REGULAR_ANCHORS or len(ROOT_STAGE_TIMELINE) != 51 or
                set(ROOT_STAGE_TIMELINE) != set(ROOT_FINAL_IDS)):
            raise RuntimeError("static contract")
        if len(argv) < 2:
            _usage("MISSING_MODE")
        if argv[0] != VALIDATOR_COPY:
            _usage("VALIDATOR_ARGV0")
        mode = argv[1]
        if mode not in MODE_ARITY or mode not in MODE_HANDLERS:
            _usage("UNKNOWN_MODE")
        arguments = argv[2:]
        if len(arguments) != MODE_ARITY[mode]:
            _usage("ARITY")
        if (mode, *arguments) not in EXACT_ARGV_ROWS:
            _usage("ARGV_ROW")
        guard_expected = True
        guard = _open_receipt_guard(mode, arguments)
        _verify_launch_fd_contract(guard)
        identity_hold = _open_identity_pool(mode, "IDENTITY_HOLD")
        initial_runtime = _verify_runtime_contract(argv)
        initial_identity = _verify_validator_copy()
        initial_controls = _verify_controls_and_sources()
        mode_universes = _open_mode_universes(mode, arguments)
        if mode == "ABSENT":
            absence_hold = _open_held_absence(arguments[0], "ROOT_ABSENCE_HOLD")
        pre_handler_rows = _pre_handler_hold_rows(mode, arguments)
        if pre_handler_rows:
            pre_handler_hold = _open_held_group(
                pre_handler_rows, "PRE_HANDLER_HOLD",
            )
        detail = MODE_HANDLERS[mode](arguments)
        post_handler_rows = _post_handler_hold_rows(mode, arguments)
        if post_handler_rows:
            post_handler_hold = _open_held_group(
                post_handler_rows, "POST_HANDLER_HOLD",
            )
        terminal_runtime = _verify_runtime_contract(argv)
        if terminal_runtime != initial_runtime:
            _fail("RUNTIME_TERMINAL_VERSION")
        terminal_identity = _verify_validator_copy()
        if terminal_identity != initial_identity:
            _fail("VALIDATOR_TERMINAL_VERSION")
        terminal_controls = _verify_controls_and_sources()
        if terminal_controls != initial_controls:
            _fail("CONTROL_TERMINAL_VERSION")
        if not isinstance(detail, str) or detail == "":
            raise RuntimeError("result")
        _terminal_recompute(mode, arguments, detail)
        encoded = _encode_result("PASS " + mode, detail)
        _parse_validator_stdout(encoded, mode, (), "RESULT_SELF")
        _check_all_holds(
            post_handler_hold, pre_handler_hold, absence_hold,
            mode_universes, identity_hold, "HOLD_PRE_EMIT",
        )
        _receipt_guard_check(
            guard, b"", "RECEIPT_GUARD_PRE_EMIT", include_created=True,
        )
        if not _write_stdout(encoded):
            raise RuntimeError("stdout write")
        emitted = True
        os.fsync(1)
        os.fsync(2)
        _receipt_guard_check(
            guard, encoded, "RECEIPT_GUARD_POST_EMIT", include_created=True,
        )
        post_runtime = _verify_runtime_contract(argv)
        if post_runtime != initial_runtime:
            _fail("RUNTIME_POST_EMIT_VERSION")
        post_identity = _verify_validator_copy()
        if post_identity != initial_identity:
            _fail("VALIDATOR_POST_EMIT_VERSION")
        post_controls = _verify_controls_and_sources()
        if post_controls != initial_controls:
            _fail("CONTROL_POST_EMIT_VERSION")
        if mode in ("ABSENT", "REPLAY"):
            _verify_tools()
            _verify_dependencies()
        _check_all_holds(
            post_handler_hold, pre_handler_hold, absence_hold,
            mode_universes, identity_hold, "HOLD_POST_EMIT",
        )
        _receipt_guard_check(
            guard, encoded, "RECEIPT_GUARD_SEMANTIC_FINAL",
            include_created=True,
        )
        _check_all_holds(
            post_handler_hold, pre_handler_hold, absence_hold,
            mode_universes, identity_hold, "HOLD_AFTER_RECEIPT_FINAL",
        )
        _close_all_holds(
            post_handler_hold, pre_handler_hold, absence_hold,
            mode_universes, identity_hold,
        )
        holds_closed = True
        _close_receipt_guard(guard, "RECEIPT_GUARD_SUCCESS")
        guard = None
    except UsageFail as exc:
        tag = exc.args[0] if exc.args and isinstance(exc.args[0], str) else "USAGE"
        failure = _failure_bytes("usage", tag)
        if not holds_closed:
            _check_close_all_holds(
                post_handler_hold, pre_handler_hold, absence_hold,
                mode_universes, identity_hold, "HOLD_USAGE", suppress=True,
            )
            holds_closed = True
        if guard is not None and not emitted:
            try:
                if _guarded_failure(guard, failure, "RECEIPT_GUARD_USAGE"):
                    guard = None
            except Exception:
                pass
        elif guard is None and not emitted and not guard_expected:
            _write_stdout(failure)
        if guard is not None:
            _close_receipt_guard(guard, "RECEIPT_GUARD_FAILURE", suppress=True)
        ACTIVE_DIRECTORY_ANCHORS.clear()
        ACTIVE_REGULAR_ANCHORS.clear()
        return 2
    except CheckFail as exc:
        tag = exc.args[0] if exc.args and isinstance(exc.args[0], str) else "PREDICATE"
        failure = _failure_bytes("predicate", tag)
        if not holds_closed:
            _check_close_all_holds(
                post_handler_hold, pre_handler_hold, absence_hold,
                mode_universes, identity_hold, "HOLD_PREDICATE", suppress=True,
            )
            holds_closed = True
        if guard is not None and not emitted:
            try:
                if _guarded_failure(guard, failure, "RECEIPT_GUARD_PREDICATE"):
                    guard = None
            except Exception:
                pass
        elif guard is None and not emitted and not guard_expected:
            _write_stdout(failure)
        if guard is not None:
            _close_receipt_guard(guard, "RECEIPT_GUARD_FAILURE", suppress=True)
        ACTIVE_DIRECTORY_ANCHORS.clear()
        ACTIVE_REGULAR_ANCHORS.clear()
        return 1
    except Exception:
        failure = b"FAIL internal=CONTRACT\n"
        if not holds_closed:
            _check_close_all_holds(
                post_handler_hold, pre_handler_hold, absence_hold,
                mode_universes, identity_hold, "HOLD_INTERNAL", suppress=True,
            )
            holds_closed = True
        if guard is not None and not emitted:
            try:
                if _guarded_failure(guard, failure, "RECEIPT_GUARD_INTERNAL"):
                    guard = None
            except Exception:
                pass
        elif guard is None and not emitted and not guard_expected:
            _write_stdout(failure)
        if guard is not None:
            _close_receipt_guard(guard, "RECEIPT_GUARD_FAILURE", suppress=True)
        ACTIVE_DIRECTORY_ANCHORS.clear()
        ACTIVE_REGULAR_ANCHORS.clear()
        return 2
    ACTIVE_DIRECTORY_ANCHORS.clear()
    ACTIVE_REGULAR_ANCHORS.clear()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

# BATCH07_P27_BUILD_VALIDATOR_POSTFAIL_AUTHOR_STOP
