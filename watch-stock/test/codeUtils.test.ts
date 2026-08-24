import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalizeCode, isValidCode, inferPrefix } from '../entry/src/main/ets/data/codeUtils.ts';

test('normalizeCode: full code unchanged', () => {
  assert.equal(normalizeCode('sh600519'), 'sh600519');
  assert.equal(normalizeCode('sz000001'), 'sz000001');
});

test('normalizeCode: uppercase and separators cleaned', () => {
  assert.equal(normalizeCode('SH600519'), 'sh600519');
  assert.equal(normalizeCode('  sh600519 '), 'sh600519');
  assert.equal(normalizeCode('600519.SH'), 'sh600519');
});

test('normalizeCode: bare digits infer exchange by first digit', () => {
  assert.equal(normalizeCode('600519'), 'sh600519');
  assert.equal(normalizeCode('000001'), 'sz000001');
  assert.equal(normalizeCode('300750'), 'sz300750');
  assert.equal(normalizeCode('688981'), 'sh688981');
});

test('inferPrefix: exchange rules', () => {
  assert.equal(inferPrefix('600519'), 'sh');
  assert.equal(inferPrefix('000001'), 'sz');
  assert.equal(inferPrefix('300750'), 'sz');
  assert.equal(inferPrefix('920001'), 'bj');
});

test('isValidCode: only sh/sz/bj + 6 digits', () => {
  assert.equal(isValidCode('sh600519'), true);
  assert.equal(isValidCode('sz000001'), true);
  assert.equal(isValidCode('bj920001'), true);
  assert.equal(isValidCode('600519'), false);
  assert.equal(isValidCode('sh60051'), false);
  assert.equal(isValidCode('sh6005190'), false);
  assert.equal(isValidCode('xy600519'), false);
});
