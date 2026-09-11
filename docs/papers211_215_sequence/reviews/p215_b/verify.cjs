'use strict';
// P215 Review B verifier. SOURCE ONLY; no parse/import/run before root receipt
// and a separate runtime binding and one-use scientific grant.

function key(word) { return word.join(','); }
function equal(left, right) { return JSON.stringify(left) === JSON.stringify(right); }
function need(value, label) { if (!value) throw new Error(label); }
function compareWords(left, right) {
  for (let i = 0; i < left.length; i++) {
    if (left[i] !== right[i]) return left[i] - right[i];
  }
  return left.length - right.length;
}

function words(n, q) {
  let out = [[]];
  for (let i = 0; i < n; i++) {
    const next = [];
    for (const prefix of out) {
      for (let digit = 0; digit <= q; digit++) next.push(prefix.concat([digit]));
    }
    out = next;
  }
  return out;
}

function update(word) {
  let peak = 0;
  return word.map((value) => {
    peak = Math.max(peak, value);
    return peak - value;
  });
}

function turnWord(word) {
  let previous = 0;
  const out = [];
  for (const value of word) {
    const difference = value - previous;
    previous = value;
    const sign = difference > 0 ? 1 : difference < 0 ? -1 : 0;
    if (sign !== 0 && sign !== out[out.length - 1]) out.push(sign);
  }
  return out;
}

function floyd(start) {
  let tortoise = update(start);
  let hare = update(update(start));
  while (!equal(tortoise, hare)) {
    tortoise = update(tortoise);
    hare = update(update(hare));
  }
  let entry = 0;
  tortoise = start;
  while (!equal(tortoise, hare)) {
    tortoise = update(tortoise);
    hare = update(hare);
    entry++;
  }
  let period = 1;
  hare = update(tortoise);
  while (!equal(tortoise, hare)) {
    hare = update(hare);
    period++;
  }
  return {entry, period, recurrent: tortoise};
}

function choose(n, k) {
  if (!Number.isInteger(n) || !Number.isInteger(k) || k < 0 || n < 0 || k > n) return 0;
  k = Math.min(k, n - k);
  let out = 1;
  for (let j = 1; j <= k; j++) out = out * (n - k + j) / j;
  need(Number.isSafeInteger(out), 'safe binomial');
  return out;
}

function combinations(limit, size) {
  const out = [];
  function visit(prefix, next) {
    if (prefix.length === size) { out.push(prefix.slice()); return; }
    const remaining = size - prefix.length;
    for (let value = next; value <= limit - remaining; value++) {
      prefix.push(value);
      visit(prefix, value + 1);
      prefix.pop();
    }
  }
  visit([], 0);
  return out;
}

function signOfPermutation(permutation) {
  let inversions = 0;
  for (let i = 0; i < permutation.length; i++) {
    for (let j = i + 1; j < permutation.length; j++) {
      if (permutation[i] > permutation[j]) inversions++;
    }
  }
  return inversions % 2 ? -1 : 1;
}

function permutations(size) {
  const out = [];
  function visit(prefix, unused) {
    if (unused.length === 0) { out.push(prefix.slice()); return; }
    for (let i = 0; i < unused.length; i++) {
      visit(prefix.concat([unused[i]]), unused.slice(0, i).concat(unused.slice(i + 1)));
    }
  }
  visit([], Array.from({length: size}, (_, i) => i));
  return out;
}

function determinantCount(ceilings) {
  if (ceilings.length === 0) return 1;
  const matrix = ceilings.map((ceiling, i) =>
    ceilings.map((_, j) => choose(ceiling + 1, j - i + 1)));
  let value = 0;
  for (const permutation of permutations(ceilings.length)) {
    let product = signOfPermutation(permutation);
    for (let i = 0; i < permutation.length; i++) product *= matrix[i][permutation[i]];
    value += product;
  }
  return value;
}

function paperRecurrence(ceilings) {
  const counts = [1];
  for (let m = 1; m <= ceilings.length; m++) {
    let value = choose(ceilings[m - 1] + m, m);
    for (let i = 1; i < m; i++) {
      value -= counts[i - 1] * choose(
        ceilings[m - 1] - ceilings[i - 1] + m - i, m - i + 1);
    }
    counts.push(value);
  }
  return counts[counts.length - 1];
}

function flaggedSources(target, q) {
  const n = target.length;
  if (n === 0) return {sources: [[]], ceilings: []};
  if (target[0] !== 0) return {sources: [], ceilings: null};
  const zeros = [];
  for (let i = 0; i < n; i++) if (target[i] === 0) zeros.push(i);
  const ends = zeros.slice(1).concat([n]);
  const blockMaxima = zeros.map((start, j) =>
    Math.max(...target.slice(start, ends[j])));
  const barriers = [];
  for (const value of blockMaxima) {
    const previous = barriers.length ? barriers[barriers.length - 1] : 0;
    barriers.push(Math.max(value, previous));
  }
  const ceilings = barriers.slice().reverse().map((value) => q - value);
  const size = zeros.length;
  const sources = [];
  for (const flagged of combinations(q + size, size)) {
    if (!flagged.every((value, i) => value <= ceilings[i] + i)) continue;
    const shifted = flagged.map((value, i) => value - i);
    const heights = shifted.slice().reverse().map((value) => q - value);
    const source = [];
    for (let block = 0; block < size; block++) {
      for (let i = zeros[block]; i < ends[block]; i++) {
        source.push(heights[block] - target[i]);
      }
    }
    sources.push(source);
  }
  sources.sort(compareWords);
  return {sources, ceilings};
}

let assertions = 0;
function check(value, label) { assertions++; need(value, label); }

function main() {
  const lines = ['P215_B_FLOYD_FLAGGED_SUBSETS_V1', 'PARAM|n=0..5|q=0..4'];
  let totalStates = 0;
  let carriers = 0;
  for (let n = 0; n <= 5; n++) {
    for (let q = 0; q <= 4; q++) {
      carriers++;
      const states = words(n, q);
      const zero = Array(n).fill(0);
      const buckets = new Map(states.map((state) => [key(state), []]));
      for (const source of states) buckets.get(key(update(source))).push(source);
      let height = 0;
      const deepest = [];
      const expectedDeepestStates = [];
      for (const state of states) {
        const turns = turnWord(state);
        const cycle = floyd(state);
        check(cycle.entry === turns.length, 'Floyd clock');
        check(cycle.period === 1 && equal(cycle.recurrent, zero), 'unique zero cycle');
        let iterate = state;
        for (let step = 0; step <= turns.length; step++) {
          const expected = turns.slice(step).map((sign) => step % 2 ? -sign : sign);
          check(equal(turnWord(iterate), expected), 'complete turn-word itinerary');
          if (step < turns.length) iterate = update(iterate);
        }
        const differences = state.map((value, i) => value - (i ? state[i - 1] : 0));
        const alternating = differences.every((value) => value !== 0) &&
          differences.slice(1).every((value, i) => value * differences[i] < 0);
        const expectedDeepest = n > 0 && q > 0 ? alternating : equal(state, zero);
        if (expectedDeepest) expectedDeepestStates.push(state);
        check((cycle.entry === (n > 0 && q > 0 ? n : 0)) === expectedDeepest,
          'deepest predicate');
        if (cycle.entry > height) { height = cycle.entry; deepest.length = 0; deepest.push(state); }
        else if (cycle.entry === height) deepest.push(state);
      }
      let image = 0;
      let maximum = -1;
      const maximizers = [];
      for (const target of states) {
        const actual = buckets.get(key(target)).slice()
          .sort(compareWords);
        const flagged = flaggedSources(target, q);
        check(equal(flagged.sources, actual), 'complete flagged-subset fibre');
        for (const source of flagged.sources) check(equal(update(source), target), 'reconstructed source');
        const determinant = flagged.ceilings === null ? 0 : determinantCount(flagged.ceilings);
        const recurrence = flagged.ceilings === null ? 0 : paperRecurrence(flagged.ceilings);
        check(determinant === actual.length, 'determinant fibre count');
        check(recurrence === determinant, 'displayed recurrence equals determinant');
        check(Boolean(actual.length) === (n === 0 || target[0] === 0), 'image predicate');
        if (actual.length) image++;
        if (actual.length > maximum) {
          maximum = actual.length;
          maximizers.length = 0;
          maximizers.push(target);
        } else if (actual.length === maximum) maximizers.push(target);
      }
      check(height === (n > 0 && q > 0 ? n : 0), 'sharp height');
      check(image === (n === 0 ? 1 : (q + 1) ** (n - 1)), 'image size');
      check(maximum === choose(q + n, n), 'maximum fibre');
      check(maximizers.length === 1 && equal(maximizers[0], zero), 'unique maximizer');
      check(equal(deepest, expectedDeepestStates), 'complete deepest set');
      totalStates += states.length;
      lines.push(`CARRIER|n=${n}|q=${q}|states=${states.length}|height=${height}|image=${image}|maxfibre=${maximum}`);
    }
  }
  check(carriers === 30, 'carrier total');
  check(totalStates === 5704, 'state total');
  lines.push(`TOTAL|carriers=${carriers}|states=${totalStates}|assertions=${assertions}`);
  lines.push('PASS');
  process.stdout.write(lines.join('\n') + '\n');
}

main();
