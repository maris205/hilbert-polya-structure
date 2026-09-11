# Source-read/version timing defect and corrected acceptance

2026-09-11 UTC. This corrects GUARD_SOURCE_RECEPTION.md without overwriting
that historical receipt or the initial01 grant/run. Root's first full read
was an earlier177-line guard body. The later hash observation identified the
final body after the preparing agent's edits. Root incorrectly paired that
hash with the earlier full read and described runtime baseline metadata as
mandatory equality in the final guard. This was a root source-intake error.

After reviewer clarification root reread the complete final guard through
EOF in the same command as its SHA256:
ba089a57d8a9a96cdc185bf9a74df9681ccc716bf87dd4c6e0754a37340479c0.
The final snapshot records all per-path errors and all historical runtime
metadata differences. It checks expected path/kind/size/hash (absence errno),
requires zero pre/post errors, and requires complete fresh pre/post metadata
and content equality. Baseline metadata differences are disclosed, not
automatically fatal. All other exact fixed command/grant/input/output
controls remain as reviewed. Root now accepts this actual complete final
source under the ordinary runtime policy. No code/policy rewrite is made.

Fresh root preflight550af6 independently checked historical metadata equality
and all41 source/frozen pins before initial01; root raw receptiondf09c2
received all69 current keys and full RAW pre/post equality after it. Thus no
runtime metadata drift is observed. Nevertheless initial01 was submitted
before root had fully read the final guard body. Preserve its actual zero
exit and3004047-byte output as historical evidence with this timing defect;
do NOT use it as the canonical origin or a required strict replay.

A separately granted fresh initial02 follows this corrected complete source
acceptance. No existing grant/run is reused and no failed evidence is erased.
Subsequent canonical/strict/semantic/build gates remain mandatory. This is
a bounded source-version correction, not a hostile-runtime closure claim.
