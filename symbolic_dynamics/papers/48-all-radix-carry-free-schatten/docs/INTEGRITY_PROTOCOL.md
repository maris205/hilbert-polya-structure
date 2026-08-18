# Paper 48 integration integrity protocol

The integration driver accepts only an absolute, real candidate root and
executes from an isolated hostile working directory with Python `-I -B`.
Every pre-existing node is checked with `lstat`; symlinks, nonregular files,
cache names, bytecode, absolute output paths, parent segments, missing files,
extra files, renamed files, and unexpected empty directories are fatal.

State A contains exactly the thirteen outputs frozen by
`EXPERIMENT_CONTRACT.json`. State B contains those files plus the acyclic
`PAPER_MANIFEST.sha256`.  The paper manifest excludes itself, the static
manifest, the PRE-OUTPUT seal, and all transient build directories.

Each run builds two complete siblings. They must agree recursively by path,
kind, mode, and file hash before installation. PRE_CERT is written before
the integrity certificate; FINAL reconstructs every producer and the full
namespace. A forced late failure exits before rename and must preserve both
target bytes and registered metadata. An identical installed target is
compared against a fresh sibling and incurs zero physical replacements.

The static manifest is acyclic: its base inventory excludes both the static
manifest and PRE-OUTPUT seal; the seal binds that base digest; the final
static manifest then records the seal but excludes itself. Candidate runs
never alter the static tree.
