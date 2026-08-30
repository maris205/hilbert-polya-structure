# C247 code contract

'c247_billiard_producer.py' emits 44 orientation-separated primitive rows for
all reduced \(m/n\) with \(n\le12\), six repetition rows, and two boundary
rows.  The frozen working coordinate is \((\theta,\alpha)\), with \(\alpha\)
the signed half-chord angle defined by \(\theta'-\theta=2\alpha\);
\(p=\sin\alpha\) is auxiliary and noncanonical.

'c247_billiard_checker.py' independently rebuilds every trigonometric value,
the rigid map and clean kernel, the length/action/caustic formulas, and the
merged endpoint semantics.  'c247_billiard_sympy_crosscheck.py' supplies
symbolic and high-precision algebra; 'c247_billiard_replay.py' checks byte
identity; 'c247_billiard_mutation.py' runs 31 repaired-hash hostile attacks.
The release manifest closes 27 payload files plus itself.
