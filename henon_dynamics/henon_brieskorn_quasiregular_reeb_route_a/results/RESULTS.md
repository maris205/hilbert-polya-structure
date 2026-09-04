# Exact results

## Canonical evidence

- File SHA-256:
  `3d000cca57cbc26bcb262b75e87fc7cafa6826b79a5e61d287cd9d62b71b5f84`
- Inner payload SHA-256:
  `93cab889afc686ff09c758a0ec29106453909f9a6872b94a08a4b6ba46c77353`
- Bytes: 3,787,774
- Global fixed-time ledger SHA-256:
  `25a48cc23c1cd7a6003f9dd44f0caaee44205fa65f8da56c20b759d776a3df35`

## Verified scale

| object | exact count |
|---|---:|
| coprime odd pairs (3\le p<q\le101) | 1,003 |
| fixed-time cells | 5,469,178 |
| orbit-type rows | 4,012 |
| transverse-rotation rows | 3,009 |
| nondegenerate CZ cells | 103,749 |
| Seifert/index rows | 1,003 |

The first pair is ((3,5)), with principal period (30) and class counts
((22,4,2,1,1)) for empty, (01), (02), (12), and principal. The final
pair is ((99,101)), with period (19,998) and counts
((19,798,100,98,1,1)).

Exactly one invariant row is positive: ((p,q)=(3,5)), where
(mu_{\rm RS}=2). No row has zero orbifold Euler characteristic or zero
principal RS index.

## Section commitments

- pair rows:
  `83c53a0927c50767f7b9d8ff56bc31b60d9f67fb3f34ade0c5205f907fb451d7`
- orbit-type rows:
  `2a82a76664cbe0969894f2ac064f467ab804358b4dd88705c8d96924971ecfab`
- rotation rows:
  `c075f3bad368343b6c31cc5e6ee23f48a9d580673f0cb1a133865a873c5e87c9`
- invariant rows:
  `3196e529d17d61fe6e0e48cbf4154a55f9d90b56a5cb95897e145a4286fadb32`

The finite ledger audits implementation and boundary branches only. The
uniform contact-dynamical statements are proved analytically.
