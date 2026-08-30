# Paper 25 Stage 4.5 Bibliography Integrity Correction Authorization Request

Status: **AWAITING EXPLICIT AUTHOR AUTHORIZATION**. This request does not itself grant authorization, and the proposed patch has not been applied.

## Byte-bound control artifacts

- Anchored bibliography working copy: `notes/stage4_5_references_working.bib`
  - SHA-256: `24381ded0d5d9d91fc4a3ad5250e3ccd8039c96a5f9131a8a987eb56d85bb8d6`
  - Short base hash used by the patch protocol: `24381ded0d5d`
- Block manifest: `notes/stage4_5_references_working.bib.block-manifest.json`
  - SHA-256: `a2e27c0f8e165c0d5730c165fb16f57b6067edafc0dd065676bcb1617ba71acc`
- Integrity correction list: `notes/stage4_5_integrity_correction_list.json`
  - SHA-256: `f25c80eae179acd0f50d948447000f775575a0c962ea9de3627c87d6d9c217c7`
- Exact proposed patch: `notes/stage4_5_integrity_patch_round1.json`
  - SHA-256: `c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc`

## Exact authorization surface

| Correction | Target | Allowed operation | Exact effect |
|---|---|---|---|
| `IL-MINOR-1` | `B0001` (`GaspardRice1989Semiclassical`) | `replace_block` | Add a `note` identifying the published erratum, J. Chem. Phys. 91(5), 3279 (1989), DOI `10.1063/1.457672`. |
| `IL-MINOR-2` | `B0002` (`GaspardRice1989Exact`) | `replace_block` | Add a `note` identifying the published erratum, J. Chem. Phys. 91(5), 3280 (1989), DOI `10.1063/1.457670`. |
| `IL-MINOR-3` | `B0006` (`Ruelle1976`) | `replace_block` | Add the publisher-record issue metadata `number = {3}`. |
| `IL-MINOR-4` | `B0008` (`Livsic1972`) | `replace_block` | Normalize the publisher-authoritative author form to `author = {Liv\v{s}ic, A. N.}`. |

The byte-exact replacement text is solely the `new_text` value of each corresponding operation in the proposed patch whose SHA-256 is recorded above. Each operation has one matching correction ID in `roadmap_item_ids`; all four operations declare `claim_strength_changes=[]` and `collateral_authorization_ids=[]`.

## Scope and stop conditions

Authorization, if explicitly granted, is limited to the four target/operation pairs above and to the exact proposed patch bytes identified by SHA-256. It does not authorize:

- any edit to `paper/references.bib` or the manuscript during this authorization step;
- any manuscript-claim, registered-claim, scientific-result, or canonical-result change;
- any collateral edit, structural modification, or operation on another block;
- applying a regenerated patch with a different SHA-256 without a new request.

Application must stop and return for authorization if any precondition/hash fails, any validator reports an error or structural flag, or an exact target cannot be changed as specified.

## Validation already completed (no apply)

- Block manifest validation: passed for 8 blocks.
- Integrity correction list validation: passed for 4 issues.
- Proposed patch schema, base hash, target, and old-hash validation: passed for 4 operations.
- Structural-shape analysis: 4/8 blocks touched; ratio `0.5`; threshold `0.6`; `touched_ratio_exceeded=false`; `any=false`.
- Patch application: **not performed**.

## Copy-paste authorization statement

> 我确认并授权 Paper 25 Stage 4.5 bibliography integrity correction patch，revision patch SHA-256 c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc；IL-MINOR-1 authorize B0001/replace_block；IL-MINOR-2 authorize B0002/replace_block；IL-MINOR-3 authorize B0006/replace_block；IL-MINOR-4 authorize B0008/replace_block。授权仅限上述 exact patch、targets 与 operations；不授权 collateral edits、claim-strength changes、canonical results refresh、正文修改或 paper/references.bib 在本授权步骤中的直接修改。若 hash/precondition/validator 失败、出现 structural flag 或需超出 scope，停止并请示。

