# Paper28 EC supplement capture result

The confirmed one-file capture completed once with exit0 on 2026-09-05.
The script read exactly 3584 host content bytes under its 4096-byte bound,
from `/usr/share/texlive/texmf-dist/fonts/tfm/jknappen/ec/ecrm1095.tfm`.
No additional metric, package, source change, installation or build was included.

The snapshot is `dependency-ec-supplement-20260905/ecrm1095.tfm`, SHA-256
`6a3850cd71bbb2f43d98b7eb6b47f925de25626f5f4a0648c2d9d7b4b774eb2a`,
3584 bytes, 12 LF bytes; recorded mode0644. Before/after metadata records match.
Outcome SHA-256 is
`507016423515267d4ab5ab55e9e08cc2818391a4f4e00ec803b3870d75645535`.
Its decision remains `EC_METRIC_CAPTURED_AUDIT_PENDING` and its six earlier
outputs remain sealed. This document does not rewrite that execution result.

Capture review SHA-256 was
`1c5e6916b1728bff6d7db418f6936fe917f9b4454218b3c6df95f562085f6be1`.
The source trio and capture controls passed the script's closing rebind.
The source, base CAPTURE2, earlier failures and earlier controllers were not
modified by capture. The pre-execution review transparently records its initial
accidental old-path enumeration; it did not read/modify old artifact content.

Independent recording integrity is reported separately in
`EC_SUPPLEMENT_AUDIT_20260905.md` when completed. Only after that audit and the
new controller's exact-hash review may the confirmed fresh-root successor run.
Capture success is not a PDF/build or local-deliverable acceptance.
