# Paper 27 successor complete dependency lock

lock_status: AUTHOR_STOP_PENDING_INDEPENDENT_REVIEW
controlling_event: B07-E0261-P27-SUCCESSOR-DEPENDENCY-COMPLETE-CHAIN-CONTENT-HASH-AND-LOCK-AUTHORIZATION
opening_ledger_identity: bytes=1075796; LF=15221; mode=0644; nlink=1; sha256=63b76d939fbdf1d84fa2cac44439926024bf114922c30551055f1f18288147e6
profile_identity: bytes=45627; LF=816; mode=0644; nlink=1; sha256=2e608faaa05e3063352c193869b92d5a305cc3de956ad18624d457b303787bec
profile_revision_review_identity: bytes=19942; LF=353; mode=0644; nlink=1; sha256=d8f8c82c722d00dcf419e6878cbcda3b3f784ed734ebb91dc33502271ceb2893
external_effect: none

## 1. Scope and authority

This is the sole dependency-lock artifact authorized by E0261.  It freezes
the complete conservative system-input candidate closure for the exact
passed Paper 27 successor source and deterministic profile.  It is a local
control record, not a build input, scientific result, PDF, release,
submission, upload, package action, or authority to create or inspect a
certified root.

The lock has exactly 87 logical rows.  Eighty-five logical paths are regular
at hop zero.  Two logical paths are symlinks and terminate at a regular first
hop.  There are 86 distinct final regular targets because one final target is
shared by its own zero-hop logical row and one symlink row.  Every final is a
mode-0644, link-one regular file.  The maximum chain length is one symlink
edge; there is no missing path, dangling target, cycle, directory, special
file, unresolved hop, alternate path, or inferred prefix.

These rows are a conservative lock.  A certified recorder may use a strict
subset.  It may not name an external input outside this lock, and an unused
locked row need not be opened merely to manufacture usage.

## 2. Author observation procedure

Before any content read, the author freshly rebound all 87 logical paths in
strict byte order with no-follow `lstat`.  Each zero-hop regular matched the
bytes, mode, and link count frozen by E0258.  Each symlink matched its frozen
symlink lstat and raw `readlink` bytes; the reviewed pure POSIX component
algorithm reproduced its canonical hop; and a fresh no-follow lstat of that
exact hop matched E0260.

After the complete chain rebind succeeded, the 86 distinct final targets
were processed once each in exact path-byte order by the fixed
`/root/miniconda3/bin/python3` under
`PYTHONDONTWRITEBYTECODE=1`.  Each path was opened with
`O_RDONLY|O_NOFOLLOW|O_CLOEXEC`, required by `fstat` to be the expected
mode-0644 link-one regular file, read in binary chunks into SHA-256, and
checked again before close.  Device, inode, size, mode, link count,
`mtime_ns`, and `ctime_ns` were identical across the pre/post fstat pair,
and every read byte count equaled the frozen size.  No directory was listed,
no symlink was followed by pathname open, and no undeclared content was read.

The author observation census is:

- logical chain rebinds: 87;
- logical regulars: 85;
- logical symlinks/readlinks: 2;
- fresh final-target no-follow lstats for symlink chains: 2;
- distinct final content hashes: 86;
- shared-final row reproductions: 1;
- failures, drift, missing reads, short reads, or changed-during-read cases: 0;
- filesystem writes by the E0261 chain-rebind/hash process before this
  artifact: 0; the controlling append-only E0261 ledger event already
  existed before that read-only process began.

## 3. Exact raw symlink bindings

| Logical path | Logical lstat | Raw target bytes | Raw target hex | Raw target UTF-8 | Canonical final |
|---|---|---:|---|---|---|
| `/usr/share/texmf/web2c/texmf.cnf` | symlink; bytes 40; mode 0777; links 1 | 40 | `2e2e2f2e2e2f7465786c6976652f7465786d662d646973742f77656232632f7465786d662e636e66` | `../../texlive/texmf-dist/web2c/texmf.cnf` | `/usr/share/texlive/texmf-dist/web2c/texmf.cnf` |
| `/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map` | symlink; bytes 15; mode 0777; links 1 | 15 | `7064667465785f646c31342e6d6170` | `pdftex_dl14.map` | `/var/lib/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map` |

The first canonical final is also the zero-hop final for logical path
`/usr/share/texlive/texmf-dist/web2c/texmf.cnf`.  Its one independently
bound content identity is reproduced in both logical rows.  The raw symlink
bytes remain distinct chain evidence and may never be replaced by the
canonical spelling during a future rebind.

## 4. Frozen row stream

The following fenced block is the exact lock row stream.  A zero-hop chain is
written as its sole logical path.  A one-hop chain is written as
`logical=>canonical-final`.  Paths and chains contain no tab, CR, LF, or
NUL.  Rows are sorted by exact logical path bytes.

```text
/etc/texmf/web2c/texmf.cnf	/etc/texmf/web2c/texmf.cnf	/etc/texmf/web2c/texmf.cnf	475	0644	1	3443c7e22fbb4585732473f7e95d3cbf3e8657100f9117e711e2af5b0db85a40
/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst	/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst	/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst	20613	0644	1	19f2cf88686b86aaa8e65d5f0313a92499815761e04b42e84ea2c3dc3685ada9
/usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map	/usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map	/usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map	3524	0644	1	d9693993efdc7d0b9ab3df777589995d43e24eeae95f12b6a230a19caadeaa42
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm	1004	0644	1	373172fe340e4aede5129b89d65f576bfb1fe6932bd55c38f60bcaa84f3d1188
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm	988	0644	1	3f56ab22f7fc6a015813976c6c6cc2fd55736bbaec4958a4562e10719fa18062
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm	916	0644	1	3b54bde5cb0e0bd071eea7bc702ed3a1a284f786779ef8e75b06eba4104bb9f2
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm	924	0644	1	c800d1dfd533040219fcc06d52e0e00c2a20fb9b0039fe9f58ccec53fd003a9f
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm	928	0644	1	719d100c110fa1cfae9ad0b63e6c21753f4980f925fa516c1a04961e206f69d5
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm	908	0644	1	d9f5f519ec718e9dbccb8527c1f5d3b4a008dfb946377f97f71611b385d3d010
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm	940	0644	1	9e0909a297a3097e50960158d324006ddd5302db665400fa1fdf966df14e1a17
/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm	940	0644	1	361b5530a4b410c6274e9330c11e993843c62e394323aeaa6e0aee61e8042444
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx10.tfm	1328	0644	1	ae296e8e41b2b0f73e9a17fdc42c743b9ddcc58d23c30acaa3411206f7824780
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx12.tfm	1324	0644	1	0eb2f13840155007c2d3c59b074322a3aa7358b9643aa314f3146468ae7f0806
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx5.tfm	1332	0644	1	a746151d8e3a521965bbfae2666e1528374a514375daa7d620e9b89ebbbfb0ae
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx6.tfm	1344	0644	1	38ded79d7cce07fa28921f37f6b88e67bd86951a3e5af709c219d63454786ce1
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx7.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx7.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx7.tfm	1336	0644	1	e7b284f0ee98b7773be9b57ca652b4bb14391370509a424b5b62b06b5cae86e4
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmbx8.tfm	1332	0644	1	6dab44c885b7cbf567771d9cfa565f3df34d0e8124132b9b6f9fdc496a1c2eda
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmex10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmex10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmex10.tfm	992	0644	1	0890bccea1dd4d27f001ac30e86c63af35bc803e0557c35aafb1903c8d208e92
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi10.tfm	1528	0644	1	e442c5487f84df70218ff37f775c87060856f5b6e04c011b6cadbbadfcf46645
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi12.tfm	1524	0644	1	79563547084d85388e6909888f9fa7f5cad33bdda44ca6b25b362e1d301db539
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi6.tfm	1512	0644	1	ab6ecb4aaba9ca1b4259b1d1f64309a785bbaeb09183fd79a066b7764a448a28
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm	1520	0644	1	65af8c1e162a952cab8e93c834fcf43ce09b508e6c16e512ebb673cd850b0d41
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr10.tfm	1296	0644	1	87f2d8981927644cbecaf3d639e96e348ea4e7be49d8804468bd8ba9ff3f5244
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr12.tfm	1288	0644	1	1ce8af37ed38e93940829d3540e494eaaddc5201758d036b9074467e70a738dc
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr17.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr17.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr17.tfm	1292	0644	1	86b6e8a52aae6ad1655e32099e12bd2904b158aba4c8afb74143266d2d9cd18f
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr6.tfm	1300	0644	1	106afa9172f0c00e58b9f5cbc72b302a18aaeeaddf50caca145af9cc0b81afd2
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmr8.tfm	1292	0644	1	4c5ae243ac0aa254e7ec7f0602cc2a4351e5011ff0cb6dc150a5f6de19585de6
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss10.tfm	1316	0644	1	431472f34665b6243a32936215f2e17d1f124cdf8513e86e2bedc4c3de3f980b
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmss8.tfm	1296	0644	1	25650d37e11bee41e03dc4757a1b6f1a64f27a53c664aa618d1a8ded54d96ed5
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy10.tfm	1124	0644	1	0ca13d421ac7133271aed7c935099ecf3d1d08ac9e15f81acb34a16564ab8a46
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy6.tfm	1116	0644	1	137eb9f38f661c66309614066a7b5d63d8969d33aba0c9efee9f844a4ce65b50
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy8.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmsy8.tfm	1120	0644	1	84c37f07ca360c41ad0a0fba7387d279d72457c69bdae03653208c683d8de6bc
/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmti10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmti10.tfm	/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmti10.tfm	1480	0644	1	46a66e937f809c4fbe317947b583a14b408aca41ecb835eca3be46391190432a
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb	34811	0644	1	ca41102968b817bf6e8b22fd6de205ca23bf5088218511cce0c8129e1577cb70
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb	32080	0644	1	c838238f31d86a9f198873dfaf501601a4fc966845b9c59e7dc251c4e85d1f1f
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb	32166	0644	1	fe99cd3dcadd182a24b86e593e56d2e900c992311218c43779f858ed6e1c3b31
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb	30251	0644	1	791b31aa1db8608d0144b3a40fc0fe53383a60f6b00d0e8fd9f06ac4a11df8cb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb	36299	0644	1	e3661061e8aa474d6de5ffa916edceb0e3d8b998862018c147f0357fce00bcd7
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb	37166	0644	1	c31dbaffb861162eadf3a7210bdf271b0dda577841aed4c0572069b0d52662b6
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb	36281	0644	1	5b293a581ddb937b02559c3ce1a60184cc434295533204a2cd3864a6ad8a1f53
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb	35469	0644	1	f396f52d9ed3498c15aa7e694baef74c0a11119624fcd6db66dad4ac76972cb0
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb	35752	0644	1	fdcede8794018df5f2b58f0905fb20a2b418ed8f67b73ee12445855dfbe5b1be
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb	32722	0644	1	9b58bfa828b9553b7c8331cf26c45443b836f8aab62e820b40a5b65c8531dd42
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb	32362	0644	1	465827b4702e12f7deea159c8084753ffc27998963de516e490bd7bd5bed41dd
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb	32734	0644	1	9fe20cb9ef24a0f4c74d38a65d4eee5cff3165f3b8600407ceba396aeb2b7617
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb	32762	0644	1	b37e8671820b0753c6e233eaa3230c6ab9cff04e6c4baee312d60ae261e5aba1
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb	32726	0644	1	8150cbfac5cfe53040327df171c3059f10730b32cabf2504b01713d639a11feb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb	24457	0644	1	c9071fd676395df32520c3d906f2829898ea735f66c40a40578dec3c0ac51738
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb	24420	0644	1	7f5744c7caf27c407888cadae84be6cd7c05f34cf2c5df385b8f69fa349a3feb
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb	32569	0644	1	62ee8cef552017551cd3e026a483e700730103eceaad959c87b7730017f59cff
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb	32587	0644	1	73eed8a83a07d8ef04d240da22bce1fd3646074f46179e3677f4f42a542f20b6
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb	32716	0644	1	583b65bd1857bffc2ab184fcb4aad4e70e12eb05c9ca9f1c58c9a00a86c8bccf
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb	32626	0644	1	2313392f0f4cd974d9da5fb54a52feae126059759edc04a4e47e33ea6027418b
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb	37944	0644	1	b6f162e1549a649c7e9b2edfb77306f60e1b0da74547f33cba39ff6ba0bdd473
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb	30273	0644	1	778a2aaea4bf9d19ce2a7342864fa2696c07770c86d36a62e2ef799ad0724b05
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb	/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb	34694	0644	1	d2121de7e7c14490a2d352e3b62e62882d6c300235464bfa577e6055696e6e62
/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii	/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii	/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii	71627	0644	1	5dd3675b88c7b61d3703e6bf35ed75623acc6b163dff7b1477b485cee8ad71cb
/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty	/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty	/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty	12594	0644	1	8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty	/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty	/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty	5949	0644	1	dab8b0e621267acfd89736cf97bdcc02647c545c0719c4997be8a7d1bf98f9c3
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty	/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty	/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty	13829	0644	1	70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd	/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd	/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd	961	0644	1	48355e960333be747dd7b4500e76fde7c3ef0b1fa9c74ec0f1438af0d3a661a4
/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd	/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd	/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd	961	0644	1	e20f21f6ed631cbe3a627d5da5fef82367732a7d51207f8df5ee7e9c77ee342e
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty	2222	0644	1	7f25c33d4010066ff2eed0286f62854867698b06d10ebad93b1b1ab96d12f936
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty	4173	0644	1	d90cfa74087e9f8678fb81bde57f809f0d4043f2674cb23b73a85958ec4a0fb6
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty	87648	0644	1	027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty	4128	0644	1	18c28b99321d0f4576cb42e2793d2654828b273700224cd9ee27047f803e99f5
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty	/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty	2444	0644	1	49426425d82407dc702c77236fdeb4b82568ebb9566b8dd849bcfbf9eb9644de
/usr/share/texlive/texmf-dist/tex/latex/base/article.cls	/usr/share/texlive/texmf-dist/tex/latex/base/article.cls	/usr/share/texlive/texmf-dist/tex/latex/base/article.cls	20144	0644	1	988fb3e599df7e5b545e4253829dab11f0c7bd7827b79d32c2aaadfb52db6f6c
/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo	/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo	/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo	8464	0644	1	efc946da03cfa55c75be27d73012ab866fcc935fd47ac4a674026bbdbdcfa9f1
/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty	/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty	/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty	6078	0644	1	3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc
/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty	/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty	/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty	51697	0644	1	a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3
/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg	/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg	/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg	1224	0644	1	feb91e48789a21e4acced98e952c77a2e2cf4a77e01bf147b59fa56a1b3f2008
/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def	/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def	/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def	19103	0644	1	62c3a2892e6acc3d94b1e8a50ecc2a11a16565ddee3f68006a84822eb5b93a5d
/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty	/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty	/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty	18399	0644	1	63cb7c6ae98653209d8f77ee842849676930fd694bc45a771309e0486c1cd9b5
/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty	/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty	/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty	7996	0644	1	da1e0ad80baeea2859059307358257c506069c91bdd29fde9e12ee957cc5db44
/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty	/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty	/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty	2671	0644	1	cdac603619a4c129511ef8a3abfbb4d2068b1bb67626cb30568baa0ceb26aea2
/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty	/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty	/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty	4009	0644	1	4af1b021af86649d926eb025a92fa4a3603f0d65893ccdb6fb756b5a16810a51
/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def	/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def	/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def	29921	0644	1	9617358386bec1691faec14fd624634525f105505a5f9573c47bd4f617ddcb5d
/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty	/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty	/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty	59397	0644	1	e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7
/usr/share/texlive/texmf-dist/tex/latex/mathtools/mhsetup.sty	/usr/share/texlive/texmf-dist/tex/latex/mathtools/mhsetup.sty	/usr/share/texlive/texmf-dist/tex/latex/mathtools/mhsetup.sty	5582	0644	1	c3ae1e23f43029fbfc271e3b1440a692e1cd924d1810430b99e4f2aa5b9ccf09
/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty	/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty	/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty	12694	0644	1	1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157
/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty	/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty	/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty	10214	0644	1	57beb2c684bafae5e22ed8ebf3873d279c68038200b1d47703f88d87cd2ea6d2
/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty	/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty	/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty	12892	0644	1	196f2a7038e1727c4088a015bf11cac88abfedc5b7ee5eca65f44ab91dbac415
/usr/share/texlive/texmf-dist/web2c/texmf.cnf	/usr/share/texlive/texmf-dist/web2c/texmf.cnf	/usr/share/texlive/texmf-dist/web2c/texmf.cnf	39432	0644	1	ced214c26baca02d79428fd1e7f3acf59e8d60436e28bc269c3fde93e1f70bab
/usr/share/texmf/web2c/texmf.cnf	/usr/share/texmf/web2c/texmf.cnf=>/usr/share/texlive/texmf-dist/web2c/texmf.cnf	/usr/share/texlive/texmf-dist/web2c/texmf.cnf	39432	0644	1	ced214c26baca02d79428fd1e7f3acf59e8d60436e28bc269c3fde93e1f70bab
/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map	/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map=>/var/lib/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map	/var/lib/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map	4123914	0644	1	f2ef4883e12f9f53a33778e8f99cc2006e1434898cbcf493784e3c46f9ed9b18
/var/lib/texmf/web2c/pdftex/pdflatex.fmt	/var/lib/texmf/web2c/pdftex/pdflatex.fmt	/var/lib/texmf/web2c/pdftex/pdflatex.fmt	1503567	0644	1	5e3d04e4b504653152b7fbbe415f78de3d353795a3c3d9ceb68e39bb3c0cf8f0
```

row_framing: logical_path<TAB>chain-with-=><TAB>target_path<TAB>bytes<TAB>mode<TAB>nlink<TAB>sha256<LF>
row_count: 87
row_framing_bytes: 23408
row_framing_lf: 87
row_framing_sha256: 2855b5fe4a859552fc581eb3c06b11c68008b8eb67351d37f2a44c57a91adf87
logical_path_order: strict ascending exact UTF-8 bytes; distinct
unique_final_target_count: 86
symlink_chain_count: 2
maximum_symlink_edges: 1

## 5. Required future rebind and review semantics

This artifact grants no runtime read authority.  A later exact-path event
must reproduce every row literally before a reviewer or builder may touch
the locked system paths.  For each rebind it must:

1. lstat the logical path without following and require the frozen type,
   lstat size, mode, and link count;
2. for each symlink, read and compare the exact raw target bytes, recompute
   the canonical hop with the reviewed component algorithm, and lstat the
   exact hop without following;
3. open only the exact final regular path with `O_NOFOLLOW`, require the
   frozen bytes/mode/link count by fstat, hash its bytes, and require the
   exact frozen SHA-256; and
4. stop on any drift before a compiler, BibTeX process, validator-dependent
   build action, or acceptance claim.

The build profile additionally requires a rebind immediately before and
after each publication command.  Every certified recorder snapshot must
contain no external input outside these logical/final identities.  The
BibTeX log may name only `plain.bst` and `references.bib`, and the sole
style row is the frozen
`/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst` row above.

A wholly fresh independent dependency-lock review is mandatory.  Any
Blocker, Major, Minor, Ambiguity, unverifiable row, incomplete rehash,
unsafe path operation, extra input, or chain mismatch requires
`FAIL_WRITE_NOTHING`; no review artifact, repair, retry, package
installation, build, PDF, release, later-paper action, network access, or
external effect is permitted.

BATCH07_P27_DEPENDENCY_LOCK_SUCCESSOR_AUTHOR_STOP
