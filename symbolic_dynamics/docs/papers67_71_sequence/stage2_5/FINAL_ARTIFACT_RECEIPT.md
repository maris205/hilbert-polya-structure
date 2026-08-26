# Stage 2.5 final artifact receipt — P67–P71

Receipt date: `2026-08-26`  
Correction round: `1 of at most 3`  
Internal content gate: **PASS_WITH_NOTES**  
Priority clearance: **NOT GRANTED**  
External release: **HOLD**

## Canonical corrected PDFs

| Paper | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| P67 | 11 | 408243 | `ed2ffeedc97cc82d006bf540468ef7bf9c1655cad3f4600fb393f8d6451fc7da` |
| P68 | 7 | 348079 | `9527da716429ba4644271086dee8eebdd5a1c201a73cb2a0a39046cc957de61a` |
| P69 | 11 | 377379 | `93462a17e92207d9dfbccc55d6ac543391c55a8950d5057a50e9a3b9996c2766` |
| P70 | 7 | 345028 | `61398af7a4ab61ea3ace029ec315721d4a855bf8f60986c84b2fdc94d9bd0142` |
| P71 | 9 | 409426 | `971b33083dc14ceb99831f94786167c1186bf9b8365557472fb2a9f493174a9e` |

Total: 45 A4 pages.  Every final log has zero undefined citations or
references, rerun advisories, multiply-defined labels, overfull/underfull
boxes, or package warnings under the registered scan.  Every listed font is
embedded and subset.

## Current package manifests

Each `SHA256SUMS` was regenerated only after the Stage-2.5 metadata seal and
then replayed with `sha256sum -c`.

| Paper | `SHA256SUMS` SHA-256 | Full replay |
|---|---|---|
| P67 | `19b455d4af341646e64192231a3e4c7575cfd6f61cf6867ce312ffc58a7f18a9` | PASS |
| P68 | `a2df9b7cb83aa8d46ef8945f91b38a74a13bc8d03a893cb5c9d09d3f2dc2ad1b` | PASS |
| P69 | `4a6e564897d5d6565bdabaa64ac540d0a9a79e3d7ec5eff9baae2e648c92f425` | PASS |
| P70 | `a3a6c57a528b4de7b4fb3a963b83429a94b8381c349d8d77769a8bf99ab3ada7` | PASS |
| P71 | `6a058a077e17acf6f68f34552887ecfb3e59e85faf57203e118596c05826a580` | PASS |

## Citation and proof-regression closure

| Paper | Verified references | Verified contexts | Ghost/dangling | Control output SHA-256 | Replay |
|---|---:|---:|---:|---|---|
| P67 | 11 | 17 | 0/0 | `a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26` | PASS, byte-identical |
| P68 | 4 | 10 | 0/0 | `918c56ef57b9c09ce27872e58a3e76667766351378e40b5d450d9cbced2a0bbf` | PASS, byte-identical |
| P69 | 7 | 12 | 0/0 | `c8a56e4e9f692fa4bb97a535b2a683f2d220489f4e94d1dd99d5d01c87ed482d` | PASS, byte-identical |
| P70 | 7 | 14 | 0/0 | `fe26d12a4fd332b87027db685563980b788fb097bd633dc974b091de0bc2f42f` | PASS, byte-identical |
| P71 | 9 | 19 | 0/0 | `4ade498585b0750acea4b487dec11b7c19b2e322f8a5ef1d4262d6c4f39f2aba` | PASS, byte-identical |
| **Total** | **38** | **72** | **0/0** | — | **5/5 PASS** |

The controls are regression evidence only, not experiments or proof premises.

## Round-1 claim/evidence identities

| Paper | Registry SHA-256 | Coverage SHA-256 | Evidence rows SHA-256 | Claims / tuples | External / anchorless |
|---|---|---|---|---:|---:|
| P67 | `cf405439753be62b5939d64de3314dbdbe304f785262c4c8d8848ecf39bc29ea` | `cc98d3aa4d4163035f05a219f80a69f5d5c4563085ca92b31006d6db257dd63e` | `2ee12d21799c6b11084c476c7277b569a295dc5c668d2082319befb4aea34347` | 23 / 27 | 11 / 16 |
| P68 | `8b55f2d8ee474a114600f6fd19e5d439d3766ccea04b30e0b2cd28cef5b43e8e` | `5031794e104f343e2a864d0f0968e4156a7f6b8b29b5a129ad81608af6e32df2` | `f32038047107167d1fe61fd625fc054c21ebb7e7e64bccca55c62c3ba1b8536e` | 23 / 23 | 3 / 20 |
| P69 | `a183b820506a697012a6b1cbe43a4918125a57920cdf7c7ef1407cddfcc4c5ba` | `35ab0de0664e8c91ae2d238c681d9ed4d0f6e788ae768736b920a5f24f892116` | `b094e0edd17f00e221b0b507c954aabdef5813f99c2b5ce72df8d7201b96bd90` | 35 / 37 | 12 / 25 |
| P70 | `4dbfd4362e4691973411ee7a7079c2687c217cad55f930f479f38c0f230fb10b` | `a3b2aff098d232387193f46a7c9181ace54d65a1fcf9a4b2f4f4c14184eca6ab` | `1cb809cd125ffc5f6be47248dab1f23a5113d173eb9a94d53754baf40a1680fd` | 30 / 34 | 13 / 21 |
| P71 | `360becd24c4fbbb6fee3da7a8ac098aa09cd4cbc13849da742fc201c6bb5f3e9` | `fa69c1669596d957c31d49d145a13de4f044b8837ea7f8ec2d7e82891015f101` | `df1fd0702b3e631fd4afe5125ee26f1692edff1a1eb6db5c246f1639d1b34462` | 29 / 31 | 8 / 23 |
| **Total** | — | — | — | **140 / 152** | **47 / 105** |

| Paper | Evidence source-map SHA-256 | E6 findings SHA-256 | Final disposition SHA-256 |
|---|---|---|---|
| P67 | `b3329d9f580a9ba117948eecaa34f5988d2cbf0209eed074dcc02c5a9117ad68` | `9bfee5c9683555f28d67575074e3fd2bfebf26fb27fa278a7bcf60cb7c7a33e1` | `7d8d924be13ffa0cdd0aded72f0fbe35a7548460f50d1a522b39da257fa32e29` |
| P68 | `110827277b363deccdddd3afbbc372d237da883dcf776bd8181b3b1f0f2d073d` | `33f9821758978d92cafa840e310bd592df2443d8e8ce12a6671d355a7c7e8f88` | `2e3e0df6e3edaafdcfc3679e7a13ed73acd695c89c00de16c921e5c3e17a8ef7` |
| P69 | `4d56f3748b24938a6aedb85cba8e7633371141be16bed17c2aae2f3e0f941f60` | `3fc83321dc858c80faf5348e44f0120d25e3fc9a284ca186ce7ab2fc55ba0f19` | `869b8810deb9d46082773ba892d0488cd8b6099d43c9650a766e8c5fec3f7827` |
| P70 | `a2deaaf2f8819af4e6d54309c7659569cf634fd957d7fe8784d8d63346465fa2` | `d7383f574fd4e30ad6eb44e56ec95aea1b51149063451cf083cbc7bd13affa69` | `894a83176afc14769a73357ca55d76fb32b778b8e374e9689a9a702f91f4d370` |
| P71 | `c6051013848f792869a5a2985450133c807bf9d74844c89d615ea8336275c93c` | `55070272790d783bdbd3e653bcdbd5c9d89a096bd629a3712b9a408943b97683` | `79b5d7c7f32269847627ebe12478f289dc2cf98fbce7a568445f8b31d88d9cf4` |

All five coverage reports replay `PASS`.  The 140 selected claims expand to
152 schema-valid ordered tuples: 47 rows replay exact session-held external
source excerpts and 105 no-reference rows preserve the required explicit
`anchorless` state.  There are zero manuscript-self rows.  Evidence-row
validation proves provenance fidelity only; it does not certify theorem truth,
execution, novelty, or priority.  There are zero mechanical candidate gaps,
while semantic extraction completeness remains
`not_machine_detectable` rather than claimed as complete.

Each E6 artifact is schema-valid and records the prescribed
`skipped_no_revision_evidence` branch because no prior block-anchored
Revision-Evidence Bundle exists.  The skip is not evidence that semantic drift
is absent.

Historical official-review PDFs and the input hashes in `INPUT_FREEZE.md`
remain unchanged provenance snapshots.  They are not aliases of the corrected
canonical PDFs.  Package-level `BUILD.md`, `FINAL_QA.md`, state JSON, and
freshly regenerated `SHA256SUMS` identify the current artifacts.  The active
material passport is `VERIFIED` for the bounded Stage-2.5 gate, SHA-256
`097d6d3cc38d0dc8a97889ba40966bd82d422c8a4c4bc8ae0851015b85ea6f99`;
priority clearance is not granted and external release remains `HOLD`.
