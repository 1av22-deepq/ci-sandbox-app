// src/math.js
export const add = (a, b) => a + b;

// src/math.test.js
import test from 'node:test';
import assert from 'node:assert';
import { add } from './math.js';

test('adds numbers correctly', () => {
  assert.strictEqual(add(2, 3), 5);
});