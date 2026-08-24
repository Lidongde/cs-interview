import { test } from 'node:test';
import assert from 'node:assert/strict';
import { Colors, quoteColor } from '../entry/src/main/ets/common/Colors.ts';
import { formatPrice, formatChangePct, formatChange } from '../entry/src/main/ets/common/Format.ts';
import type { StockQuote } from '../entry/src/main/ets/model/StockQuote.ts';

function makeQuote(changePct: number): StockQuote {
  return {
    code: 'sh600519', name: 'x', price: 10, prevClose: 10,
    change: 0, changePct: changePct, high: 10, low: 10
  };
}

test('Colors constants', () => {
  assert.equal(Colors.UP, '#F5222D');
  assert.equal(Colors.DOWN, '#00B42A');
  assert.equal(Colors.FLAT, '#9E9E9E');
});

test('quoteColor: up red / down green / flat gray', () => {
  assert.equal(quoteColor(makeQuote(1.5)), Colors.UP);
  assert.equal(quoteColor(makeQuote(-0.5)), Colors.DOWN);
  assert.equal(quoteColor(makeQuote(0)), Colors.FLAT);
});

test('formatPrice', () => {
  assert.equal(formatPrice(1700), '1700.00');
  assert.equal(formatPrice(0), '--');
  assert.equal(formatPrice(NaN), '--');
});

test('formatChangePct', () => {
  assert.equal(formatChangePct(1.19), '+1.19%');
  assert.equal(formatChangePct(-0.47), '-0.47%');
  assert.equal(formatChangePct(0), '0.00%');
});

test('formatChange', () => {
  assert.equal(formatChange(20), '+20.00');
  assert.equal(formatChange(-5), '-5.00');
});
