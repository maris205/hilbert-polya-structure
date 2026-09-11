# Matching package/source roles — finite next DATA request

This is a request for evidence, not evidence that this host is Debian,
Ubuntu, RPM-based or any other distribution. No package/version/architecture
selection, download, package tool or local database query has occurred.
PACKAGE_SOURCE_REQUEST.proposed.json supplies the six exact accepted binary
pins and one intentionally unfilled kpathsea terminal role. Existing matched
receipts should be reused before requesting duplicate material.

First reuse the four exact existing DATA/ELF reception documents named in
the request. The only newly proposed local identity source is the literal
/etc/os-release leaf, separately scoped: accept only its actual complete
regular bytes or lexical link text, never shell-source it or automatically
follow to /usr/lib/os-release. It is NOT a fourth entry in this three-leaf
reader and requires separate exact source/selection authority. If an existing
authenticated distributor/build receipt already identifies these bytes,
reuse that receipt instead and omit this new identity observation.

The publisher/provider is then asked for at most seven MEMBER-SCOPED
records keyed by the listed original path and SHA256, followed by the exact
matching binary archive/member, signed index/checksum provenance, distributor
source/patches, build and debug/link-map records. Local package ownership
alone does not prove binary identity. A whole distributed member matching
the captured body, tied to authenticated package/build/source records, is
adequate ordinary provenance; no formally verified compiler or system
rebuild is imposed. Package member spelling may differ under usr-merge:
such a mapping must be explicit evidence, never an automatic host follow.

Exact URLs/package basenames are intentionally null until the distributor
and member record identify them. A source-only request must not invent an
Ubuntu/glibc/ncurses release from resemblance or fetch an arbitrary upstream
tag. Stop at HOLD_MATCHING_PACKAGE_RECORD_MISSING if no matching member
record exists. No entire /var/lib/dpkg/status, rpm database, apk inventory,
`dpkg -l`, filesystem walk, sibling glob or unnamed package search is proposed.
The next collection must pin the exact artifact names/URLs and selected
members before retrieval; unresolved names are not an executable request.

The concrete source-role targets are bounded:

- Bash: matching builtin exec role (candidate source member
  builtins/exec.def) and the already identified four init/fini origins.
- Env: matching main/environment assignment/exec and diagnostic/exit path
  (candidate member src/env.c), plus its four init/fini origins. Earlier
  inherited startup stays the accepted limit, not a new environment census.
- Kpsewhich/kpathsea: matching option/help/version/exit path (candidate
  member texk/kpathsea/kpsewhich.c), kpathsea_new and only the concrete
  helpers called before the selected exits; matched package records must
  identify their actual source members. Four existing kpsewhich origins
  and only subsequently received kpathsea origins require role mapping.
- Loader/libc: matching elf/dl-load.c, elf/dl-cache.c, elf/rtld.c,
  elf/dl-init.c, elf/dl-fini.c and relevant architecture/relocation/TLS
  support; generated trusted-dirs.h supplies the actual SYSTEM_DIRS rules.
  The [comparison loader source](https://raw.githubusercontent.com/bminor/glibc/glibc-2.35/elf/dl-load.c)
  explicitly consumes that generated header, but the comparison tag is NOT
  installed correspondence. Two existing libc array origins remain exact
  mapping targets; no whole-libc behavior proof is requested.
- Tinfo and shared CRT: match its four existing origins using package
  debug/link-map or bounded DATA relocation/symbol evidence. Matching
  libgcc/crtstuff.c routines may explain frame_dummy/dtor registration only
  if the received source/build/address evidence actually makes that mapping.

For every existing origin, retain image body pin, original descriptor/slot
span, relocation/symbol mapping, exact source member/span and its relevant
configuration/locale/load/child/exit branches. The already accepted18-origin
table is reused; no six-image redecode is needed. A concrete additional
resolver or helper is a named bounded branch, not permission to inventory
all possible constructors. ENV8 remains C.UTF-8/UTC. Cache OS/default cases
can be settled by applicable matched facts or a complete finite conservative
alternative set; customary directory names or guessed kernel/CPU facts are
not substitutes. All32/96/64 ceilings remain. No help/version/build gate is
opened by returning this request.
