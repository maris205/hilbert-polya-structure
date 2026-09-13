"""Bounded, byte-only ELF64 little-endian dependency metadata parser.

This module never opens a file, resolves a path, imports a parser, or starts a
process.  The caller owns all read authority and dependency resolution.  Empty
RPATH/RUNPATH components are deliberately retained for caller-side rejection.
Only ordinary ELF64 LE executable/shared-object headers are supported; extended
program-header numbering, ambiguous mappings and non-UTF-8 strings fail closed.

Run with --self-test for synthetic in-memory tests (no file or subprocess I/O).
"""


def elf_dependencies(data: bytes):
    """Return dependency metadata, None for non-ELF, or raise ValueError."""
    if not isinstance(data, bytes):
        raise ValueError("ELF input must be immutable bytes")
    if not data.startswith(b"\x7fELF"):
        return None

    def span(offset, length, label):
        if offset < 0 or length < 0 or offset > len(data) - length:
            raise ValueError("out-of-bounds " + label)
        return data[offset:offset + length]

    def uint(offset, width):
        return int.from_bytes(span(offset, width, "integer"), "little")

    def utf8(raw, label):
        try:
            return raw.decode("utf-8", "strict")
        except UnicodeDecodeError as exc:
            raise ValueError("unsupported non-UTF-8 " + label) from exc

    span(0, 64, "ELF header")
    if data[4:7] != b"\x02\x01\x01":
        raise ValueError("only ELF64 little-endian version 1 is supported")
    if uint(16, 2) not in (2, 3) or uint(18, 2) != 62 or uint(20, 4) != 1:
        raise ValueError("unsupported ELF type or header version")
    if uint(52, 2) != 64:
        raise ValueError("unsupported ELF header size")
    phoff, phentsize, phnum = uint(32, 8), uint(54, 2), uint(56, 2)
    if phnum == 65535:
        raise ValueError("extended program-header numbering is unsupported")
    if phnum and phentsize != 56:
        raise ValueError("unsupported program-header size")
    if phnum and phoff < 64:
        raise ValueError("program-header table overlaps ELF header")
    span(phoff, phnum * phentsize, "program-header table")

    loads, dynamic_segments, interpreters = [], [], []
    for index in range(phnum):
        position = phoff + index * phentsize
        kind = uint(position, 4)
        offset = uint(position + 8, 8)
        address = uint(position + 16, 8)
        filesz = uint(position + 32, 8)
        memsz = uint(position + 40, 8)
        align = uint(position + 48, 8)
        span(offset, filesz, "program segment")
        if address + memsz > (1 << 64):
            raise ValueError("program segment address wraps")
        if kind == 1:  # PT_LOAD: only file-backed bytes can contain DT_STRTAB.
            if filesz > memsz:
                raise ValueError("PT_LOAD file size exceeds memory size")
            if align not in (0, 1):
                if align & (align - 1) or (address - offset) % align:
                    raise ValueError("invalid PT_LOAD alignment")
            loads.append((address, filesz, offset))
        elif kind == 2:  # PT_DYNAMIC
            dynamic_segments.append((offset, filesz))
        elif kind == 3:  # PT_INTERP
            raw = span(offset, filesz, "interpreter")
            if not raw or raw[-1:] != b"\x00" or b"\x00" in raw[:-1]:
                raise ValueError("interpreter must have one terminal NUL")
            interpreter = utf8(raw[:-1], "interpreter")
            if not interpreter:
                raise ValueError("empty interpreter")
            interpreters.append(interpreter)
    if len(dynamic_segments) > 1 or len(interpreters) > 1:
        raise ValueError("multiple dynamic or interpreter segments")

    result = {
        "interpreter": interpreters[0] if interpreters else None,
        "needed": [],
        "rpath": [],
        "runpath": [],
    }
    if not dynamic_segments:
        return result
    dynoffset, dynsize = dynamic_segments[0]
    if not dynsize or dynsize % 16:
        raise ValueError("invalid dynamic segment size")

    singleton, needed, terminated = {}, [], False
    for position in range(dynoffset, dynoffset + dynsize, 16):
        tag, value = uint(position, 8), uint(position + 8, 8)
        if tag == 0:  # DT_NULL: following padding is not a loader input.
            terminated = True
            break
        if tag == 1:  # DT_NEEDED
            needed.append(value)
        elif tag in (5, 10, 15, 29):  # STRTAB, STRSZ, RPATH, RUNPATH
            if tag in singleton:
                raise ValueError("duplicate singleton dynamic tag")
            singleton[tag] = value
    if not terminated:
        raise ValueError("dynamic segment lacks DT_NULL")
    has_strings = bool(needed) or 15 in singleton or 29 in singleton
    if not has_strings and 5 not in singleton and 10 not in singleton:
        return result
    if 5 not in singleton or 10 not in singleton or not singleton[10]:
        raise ValueError("missing or empty dynamic string table")
    straddr, strsize = singleton[5], singleton[10]
    if straddr + strsize > (1 << 64):
        raise ValueError("dynamic string table address wraps")
    mappings = [offset + straddr - address
                for address, filesz, offset in loads
                if straddr >= address and straddr - address <= filesz
                and strsize <= filesz - (straddr - address)]
    if len(mappings) != 1:
        raise ValueError("dynamic string table has no unique file mapping")
    string_table = span(mappings[0], strsize, "dynamic string table")
    if string_table[0:1] != b"\x00" or string_table[-1:] != b"\x00":
        raise ValueError("dynamic string table lacks boundary NULs")

    def string_at(offset):
        if offset >= len(string_table):
            raise ValueError("dynamic string offset is out of bounds")
        end = string_table.find(b"\x00", offset)
        if end < 0:
            raise ValueError("unterminated dynamic string")
        return utf8(string_table[offset:end], "dynamic string")

    result["needed"] = [string_at(offset) for offset in needed]
    if any(not item for item in result["needed"]):
        raise ValueError("empty DT_NEEDED name")
    if 15 in singleton:
        result["rpath"] = string_at(singleton[15]).split(":")
    if 29 in singleton:
        result["runpath"] = string_at(singleton[29]).split(":")
    return result


def _self_test():
    """All fixtures are constructed here, never read from the host."""
    def put(buffer, offset, value, width):
        buffer[offset:offset + width] = value.to_bytes(width, "little")

    def fixture():
        buffer = bytearray(768)
        buffer[:7] = b"\x7fELF\x02\x01\x01"
        put(buffer, 16, 3, 2)
        put(buffer, 18, 62, 2)
        put(buffer, 20, 1, 4)
        put(buffer, 32, 64, 8)
        put(buffer, 52, 64, 2)
        put(buffer, 54, 56, 2)
        put(buffer, 56, 3, 2)
        # LOAD maps the whole file at virtual address 0x400000.
        for position, kind, offset, address, size, align in (
            (64, 1, 0, 0x400000, len(buffer), 4096),
            (120, 2, 384, 0x400180, 112, 8),
            (176, 3, 256, 0x400100, 18, 1),
        ):
            put(buffer, position, kind, 4)
            put(buffer, position + 8, offset, 8)
            put(buffer, position + 16, address, 8)
            put(buffer, position + 32, size, 8)
            put(buffer, position + 40, size, 8)
            put(buffer, position + 48, align, 8)
        interpreter = b"/capsule/ld.so.1\x00"
        buffer[256:256 + len(interpreter)] = interpreter
        put(buffer, 176 + 32, len(interpreter), 8)
        put(buffer, 176 + 40, len(interpreter), 8)
        strings = b"\x00liba.so\x00libb.so\x00$ORIGIN/lib:/fixed\x00/one::/two\x00"
        buffer[512:512 + len(strings)] = strings
        tags = [(5, 0x400200), (10, len(strings)), (1, 1), (1, 9),
                (15, 17), (29, 36), (0, 0)]
        for index, (tag, value) in enumerate(tags):
            put(buffer, 384 + index * 16, tag, 8)
            put(buffer, 392 + index * 16, value, 8)
        return buffer

    def rejected(buffer):
        try:
            elf_dependencies(bytes(buffer))
        except ValueError:
            return
        raise AssertionError("malformed/unsupported fixture was accepted")

    assert elf_dependencies(b"") is None
    assert elf_dependencies(b"plain text") is None
    expected = {
        "interpreter": "/capsule/ld.so.1",
        "needed": ["liba.so", "libb.so"],
        "rpath": ["$ORIGIN/lib", "/fixed"],
        "runpath": ["/one", "", "/two"],
    }
    good = fixture()
    assert elf_dependencies(bytes(good)) == expected
    rejected(b"\x7fELF")
    for offset, value, width in (
        (4, 1, 1), (5, 2, 1), (18, 183, 2), (20, 2, 4), (52, 63, 2),
        (54, 55, 2), (56, 65535, 2), (32, 760, 8),
        (64 + 40, 1, 8), (64 + 48, 3, 8),
        (120 + 32, 111, 8), (120 + 8, 760, 8),
        (176 + 32, 15, 8), (392, 0x900000, 8),
        (408, 10000, 8), (424, 10000, 8),
        (480, 1, 8),  # Replace terminal DT_NULL with DT_NEEDED.
        (464, 5, 8),  # Duplicate DT_STRTAB.
    ):
        broken = fixture()
        put(broken, offset, value, width)
        rejected(broken)
    for offset, value in ((256, 0), (512, 1), (513, 255)):
        broken = fixture()
        broken[offset] = value
        rejected(broken)
    # A string table in zero-filled memory, beyond file-backed LOAD, is invalid.
    broken = fixture()
    put(broken, 64 + 32, 512, 8)
    rejected(broken)
    # A second overlapping LOAD makes the virtual-to-file mapping ambiguous.
    broken = fixture()
    broken[176:232] = broken[64:120]
    rejected(broken)
    # Multiple interpreter/dynamic segments are rejected independently.
    for begin, end in ((120, 176), (176, 232)):
        broken = fixture()
        broken[64:120] = broken[begin:end]
        rejected(broken)
    # No program headers is supported for an inert ELF metadata result.
    inert = fixture()
    put(inert, 56, 0, 2)
    assert elf_dependencies(bytes(inert)) == {
        "interpreter": None, "needed": [], "rpath": [], "runpath": []}


if __name__ == "__main__":
    # sys is a built-in module; the parser and tests import nothing from disk.
    if __import__("sys").argv[1:] != ["--self-test"]:
        raise SystemExit("usage: CAPTURE_ELF_20260905.py --self-test")
    _self_test()
