# Documentary source and reuse boundary

No reusable ELF/cache decoder was found in the current batch QA source tree.
Searches covered literal DT_NEEDED/PT_INTERP/cache magic/ELFMAG/DT_STRTAB
and binary integer-reader names in .cjs/.mjs/.txt. Three matches were old
statx failure auditors; their matching source ranges decode native statx
fields, not ELF or cache. None was imported or reused. A filename-only
docs/scripts/tools search returned only this new decoder; scripts/tools
do not exist and those lookup errors supply no positive reuse evidence.
This is a scoped search result, not a claim no decoder exists elsewhere.

Primary sources read for source semantics (upstream is not installed identity):

- [ELF header](https://gabi.xinuos.com/elf/02-eheader.html) and
  [program loading](https://gabi.xinuos.com/elf/07-pheader.html): header/class,
  program-table layout, file-backed segment description.
- [ELF dynamic linking](https://gabi.xinuos.com/elf/08-dynamic.html): dynamic
  string indices, terminating NULL and initialization-array descriptors.
- [glibc2.35 elf.h](https://raw.githubusercontent.com/bminor/glibc/glibc-2.35/elf/elf.h):
  numeric GNU audit/config/filter and generic dynamic constants. Complete
  selected tag ranges were read; no entire-header-source audit is claimed.
- [glibc2.35 dl-cache.h](https://raw.githubusercontent.com/bminor/glibc/glibc-2.35/sysdeps/generic/dl-cache.h):
 48byte new header,24byte rows, explicit endian flags, extension magic,
  section directory and hwcaps index/ISA bit layout. The proposal implements
  a conservative standalone-format subset and names unsupported cases.
- [glibc2.35 cache.c](https://raw.githubusercontent.com/bminor/glibc/glibc-2.35/elf/cache.c),
  [dl-cache.c](https://raw.githubusercontent.com/bminor/glibc/glibc-2.35/elf/dl-cache.c)
  and [ldconfig.h](https://raw.githubusercontent.com/bminor/glibc/glibc-2.35/sysdeps/generic/ldconfig.h):
  cache keys/string bases/hwcaps references and the distinction between
  literal records and loader eligibility. No installed selector or actual
  loader version is inferred from these documentary reference choices.

All implementation is new pure decoding source, not a copied observer or
upstream loader. Format constants/layout facts do not establish which
format, names, constructors or selected images the captured bodies contain.
