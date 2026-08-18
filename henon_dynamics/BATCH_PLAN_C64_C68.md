# Adaptive batch HCS-C64 through HCS-C68

Status: **C64 prefreeze complete; C65 target selected from C64; C66--C68
contingent and unselected**.

This is a five-paper adaptive round.  Each successor is selected only after
the predecessor's exact theorem or certified obstruction is available.  A
candidate must pass a fresh source/novelty audit, a theorem-sized exact pilot,
implementation and independent replay gates, manuscript audit, commit, and
push.  A failed central identity kills that candidate; it is not replaced by a
smaller claim.

## C64 (completed prefreeze)

The exact 16-type table-of-marks map for the C63 subgroup support is injective:
the mark matrix has rank 16 and determinant (2^{23}3^3).  The C63
four-versus-four character relation has nonzero mark image.

Project: `henon_mu3_yukawa_burnside_marks/`.

## C65 (selected contingent target)

Use the released C64 mark matrix together with the C63 character kernel
(K=\ker_{\mathbb Z}\chi=\langle z_1,z_2,z_3\rangle).  The target is the
integral saturation defect of (m(K)): its Smith invariants are predicted to
be (2,2,8), giving

[
\operatorname{Sat}(mK)/mK\cong
\mathbb Z/2\oplus\mathbb Z/2\oplus\mathbb Z/8.
]

C65 is not authorized until the C64 release tuple is bound and the SNF pilot
is independently replayed.

## C66--C68

`UNSELECTED_CONTINGENT`: each later slot remains open until its predecessor's
released theorem or certified obstruction supplies the next concrete target.

The scope firewall for the round is `NO_BAD_EULER_OR_ROOT_NUMBER`.
