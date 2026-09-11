# Reviewer-source drafting correction 01

Finding P212-A-SOURCE-R1: CLOSED by the exact reviewer-text correction below.
This is a finding against my review draft, not a new paper finding; paper
P212-A-M1 remains the sole open Minor. Root identified the mistake before
source acceptance or any execution. I accept the correction and have checked
the revised inequalities and all small-n endpoints deductively.

The earlier independent proof incorrectly applied the long-barbell
construction to every k=n+1,...,2n-2: n=3,k=4 gives r=2 and n=4,k=5
gives r=3, contradicting its required r>=4. Its statement that small-n
maxima all came from short rows was also wrong at n=3. The paper's
`sections/03_period_set.tex` already handles these boundaries correctly.
I reread that complete source in actual command result 639353 before repair.

The revised independent paragraph separates theta half-periods 4,...,n+1
from long-barbell half-periods 6,...,2n-2. It proves the two branches of
c=max(1,k-n-1) only for k>=6, explains coverage at n=2,3,4 and n>=5,
and gives explicit sharp examples: barbell (1,1,1), theta (1,1,2), and
barbell (1,3,n-3), respectively. No scientific claim or paper text changes.

Before edits, `history/` received byte-preserving copies of the original
SOURCE_AND_PROOF.md, SOURCE_INPUTS.sha256 and SOURCE_READY.md (copy command
229fe9, exit 0). `PROOF_DELTA.patch` records the precise text change.
The source-stage seal is refreshed for the corrected proof and includes the
revision record, diff and preserved historical inputs. The navigation-only
current SOURCE_READY.md remains outside the source-stage seal, as before.

Unchanged: verify.py, PARAMETERS.json, paper/frozen files, source-review
finding counts, citation delta and execution status. No execution, import,
compile or syntax parsing was performed. This repair closes the reviewer
drafting defect locally; root's final source acceptance is still separate.
