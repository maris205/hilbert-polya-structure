# Cover Letter — International Journal of Applied and Computational Mathematics

Dear Editors,

I am pleased to submit the manuscript **"An Area-Preserving Hénon-Map Model for the Riemann Zeros: A Deterministic-Dynamics Approach with Quantum and Dissipative Solvers"** for consideration as a research article in the *International Journal of Applied and Computational Mathematics* (IJACM).

**What the paper does.** We ask a constructive computational question: can a single low-dimensional *deterministic* dynamical system, without hand-tuned unfolding, reproduce both the global counting function of the Riemann zeros and their local level repulsion? The study is the third step in a sequence of numerical papers. The first reported an observed symbolic correspondence between the Logistic map at its band-merging point and the prime sieve (Wang, *Research in Mathematics* 13(1), 2026). The second reported a fitted numerical correspondence between a non-autonomous quadratic map and the low-order zeros (Wang, *Mathematical and Computational Applications* **2026**, 31(5), 193, https://doi.org/10.3390/mca31050193). Because the 1D Logistic map is dissipative and cannot host a unitary spectrum, the present work lifts the programme to the 2D area-preserving Hénon map and compares its spectrum to the first 100 zeros with two numerically independent eigensolvers (a unitary Fourier solver and a Markovian dissipative solver).

**Why IJACM.** The manuscript sits squarely in the journal's scope — applied and computational mathematics, including data-driven dynamical systems and numerical spectral methods. The core contribution is a carefully caveated numerical comparison (best MAPE ≈ 2.3% / 6.5% under single-point anchoring), together with standard spectral diagnostics (NNSD, pair correlation, number variance, spectral rigidity) and an explicit claim-classification table. It is a computational/exploratory paper, not a proof paper, and we believe that framing matches IJACM's readership.

**On rigor and claims.** We are deliberately careful about epistemic status. The manuscript presents its results as *numerical observations and heuristic arguments, not proofs*, and includes an explicit table classifying every claim as established, published numerical observation, structural argument, numerical observation, heuristic, qualitative, or explicitly not claimed. We do not claim to have identified the Hilbert–Pólya operator, nor that the spectrum of our operator equals the Riemann zeros. Related language about "isomorphism" in earlier drafts has been weakened to "observed / fitted numerical correspondence." All code, data, and logs are openly available at https://github.com/maris205/riemann_henon.

**Prior consideration.** The manuscript is original and is not under consideration elsewhere. An earlier version was previously considered by *Nonlinear Differential Equations and Applications* (NoDEA) and declined on scope grounds (the work is discrete dynamical systems + numerical spectral comparison, not PDE/nonlinear analysis). The present version incorporates the earlier Frontiers/npj revisions (corrected RMT framing, claim-status table, renamed homoclinic-tangency subsection, spectral diagnostics) and the newly published MCA sister paper as an explicit predecessor.

The sole author has no competing interests. Thank you for considering this submission. I would be happy to suggest suitable referees with expertise in quantum chaos, random matrix theory, dynamical systems, and computational spectral methods upon request.

Sincerely,
Liang Wang
School of Artificial Intelligence and Automation,
Huazhong University of Science and Technology, Wuhan, P.R. China
wangliang.f@gmail.com
