# Test report

The release gate regenerates evidence, runs the strict independent checker, separate SymPy reconstruction, two-path replay, and hostile mutations.  It then validates the exact 27-file payload ledger and rebuilds each of three revision rounds twice in fresh directories, using two LuaLaTeX passes per build.  Every settled log must have no LaTeX/package warning, overfull or underfull box, undefined reference, missing character, or rerun request.  Every font row must be embedded and subset, and PDF text/page contracts must hold.

Expected executable signatures are `4613 assertions`, `371 symbolic checks`, and `43/43` rejected hostile mutations.  Final hashes and page/font counts are written only after the archive is built and are frozen in `COMPILE_REPORT.md` and the release manifest.
