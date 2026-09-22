import test from 'node:test';
import assert from 'node:assert/strict';
import { add } from './math.js';

test('adds two numbers correctly', () => {
  assert.strictEqual(add(2, 3), 5);
  assert.strictEqual(add(-1, 1), 0);
});