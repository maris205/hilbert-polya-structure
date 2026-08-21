# C85 source audit

| source | SHA-256 | role |
|---|---|---|
| C75 evidence | `8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98` | twenty actual point-set subgroups, named coordinates, ambient lift |
| C75 manifest | `7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb` | frozen C75 byte binding |
| C76 evidence | `42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94` | closure-fibre counts and effective label action |
| C76 manifest | `55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5` | frozen C76 byte binding |
| C80 evidence | `8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5` | complete `20 x 65536` threshold atlas |
| C80 manifest | `a674116ab6f8f9478130219cc525478525f10f2e42f515e71418a3066e2b229c` | frozen C80 byte binding |

Both producer and checker read and SHA-256-bind all six byte strings before
using their contents.  The producer rebuilds point-set closure and groups the
C80 vectors.  The independent checker instead enumerates the twenty subgroups
from the 54-point group law, derives all target-minimal support antichains, and
recomputes every threshold entry.

C75's lifted ambient group has order `11520`; C76's effective action on the
sixteen labels has order `1920`.  C85 records both and never substitutes one
for the other.  Neither action order is used as a proxy for the actual
point-set subgroup-inclusion relation.
