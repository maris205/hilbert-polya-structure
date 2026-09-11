'use strict';
// Documentary utility only: no filesystem, subprocess, observer import or path use.
const assert = require('assert/strict');
function quote(s) {
  return JSON.stringify(s).replace(/[\u0080-\uffff]/g, c =>
    '\\u' + c.charCodeAt(0).toString(16).padStart(4, '0'));
}
function canonical(value, level = 0) {
  if (value === null) return 'null';
  if (typeof value === 'string') return quote(value);
  if (typeof value === 'boolean') return String(value);
  if (typeof value === 'bigint') return value.toString();
  if (typeof value === 'number') {
    assert(Number.isSafeInteger(value), 'only exact integer numeric data');
    return String(value);
  }
  const pad = '  '.repeat(level + 1), end = '  '.repeat(level);
  if (Array.isArray(value)) return value.length === 0 ? '[]' :
    '[\n' + value.map(v => pad + canonical(v, level + 1)).join(',\n') + '\n' + end + ']';
  assert(value && typeof value === 'object', 'JSON object');
  const keys = Object.keys(value);
  return keys.length === 0 ? '{}' : '{\n' +
    keys.map(k => pad + quote(k) + ': ' + canonical(value[k], level + 1)).join(',\n') +
    '\n' + end + '}';
}
function parseCanonical(raw) {
  assert(Buffer.isBuffer(raw), 'exact byte input');
  assert(raw.every(b => b < 128), 'observer canonical ASCII');
  const text = raw.toString('ascii');
  const counts = { integers: 0, unsafe_integers: 0, objects: 0, arrays: 0, strings: 0, booleans: 0, nulls: 0 };
  let i = 0;
  function skip() { while (i < text.length && ' \t\r\n'.includes(text[i])) i++; }
  function string() {
    const start = i++;
    while (i < text.length) {
      const c = text[i++];
      if (c === '"') { counts.strings++; return JSON.parse(text.slice(start, i)); }
      if (c === '\\') i++;
    }
    throw Error('unterminated JSON string');
  }
  function value() {
    skip();
    const c = text[i];
    if (c === '"') return string();
    if (c === '{') {
      counts.objects++; i++; skip();
      const out = {}, seen = new Set();
      if (text[i] === '}') { i++; return out; }
      while (true) {
        assert.equal(text[i], '"', 'object string key');
        const key = string(); assert(!seen.has(key), 'duplicate key'); seen.add(key);
        skip(); assert.equal(text[i++], ':'); const v = value();
        Object.defineProperty(out, key, {value:v, enumerable:true, configurable:true, writable:true});
        skip();
        const next = text[i++]; if (next === '}') return out;
        assert.equal(next, ','); skip();
      }
    }
    if (c === '[') {
      counts.arrays++; i++; skip(); const out = [];
      if (text[i] === ']') { i++; return out; }
      while (true) {
        out.push(value()); skip();
        const next = text[i++]; if (next === ']') return out;
        assert.equal(next, ','); skip();
      }
    }
    for (const [token, v, counter] of [['true',true,'booleans'],['false',false,'booleans'],['null',null,'nulls']]) {
      if (text.startsWith(token, i)) { i += token.length; counts[counter]++; return v; }
    }
    const token = /^-?(?:0|[1-9][0-9]*)/.exec(text.slice(i));
    assert(token, 'integer JSON value'); i += token[0].length; counts.integers++;
    const integer = BigInt(token[0]), bound = BigInt(Number.MAX_SAFE_INTEGER);
    if (integer < -bound || integer > bound) { counts.unsafe_integers++; return integer; }
    return Number(integer);
  }
  const parsed = value(); skip(); assert.equal(i, text.length, 'whole JSON EOF');
  assert.deepStrictEqual(Buffer.from(canonical(parsed) + '\n', 'ascii'), raw, 'whole canonical raw bytes');
  return { value: parsed, counts };
}
module.exports = { canonical, parseCanonical };
