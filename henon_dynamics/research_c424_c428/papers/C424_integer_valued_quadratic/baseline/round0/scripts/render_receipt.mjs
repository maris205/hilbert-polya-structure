// Presentation-only: read stored receipt fields; never execute a map or checker.
// The caller applies stdout as tables/residual_rows.tex with apply_patch.
import fs from 'node:fs';
const receipt = JSON.parse(fs.readFileSync(new URL('../evidence/FINITE_CORE_RESULTS.json', import.meta.url), 'utf8'));
const lines = ['% Direct rendering of recorded fields; no mathematical program execution.'];
for (const row of receipt.parameters) {
  const periods = Object.entries(row.least_period_cycle_counts)
    .map(([d, count]) => count === 1 ? d : `${d}^{[${count}]}`).join(',');
  lines.push(`${row.a} & ${row.doubled_coordinate_bound} & ${row.doubled_coordinate_alphabet.length} & ${row.strict_pruning_sizes.length - 1} & ${row.periodic_points} & $${periods || '\\text{---}'}$ \\\\`);
}
process.stdout.write(lines.join('\n') + '\n');
