import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseTencentQuote } from '../entry/src/main/ets/data/parse/tencentQuoteParser.ts';

function makeTencentLine(code: string, name: string, price: string, prev: string, open: string,
  high: string, low: string, change: string, changePct: string): string {
  const f: string[] = new Array(35).fill('');
  f[1] = name;
  f[2] = code;
  f[3] = price;
  f[4] = prev;
  f[5] = open;
  f[31] = change;
  f[32] = changePct;
  f[33] = high;
  f[34] = low;
  const prefix: string = code.startsWith('6') ? 'sh' : 'sz';
  return `v_${prefix}${code}="${f.join('~')}";`;
}

test('parse tencent quote line', () => {
  const text = makeTencentLine('600519', '贵州茅台', '1700.00', '1680.00', '1690.00', '1710.00', '1670.00', '20.00', '1.19');
  const q = parseTencentQuote(text)[0];
  assert.equal(q.code, 'sh600519');
  assert.equal(q.name, '贵州茅台');
  assert.equal(q.price, 1700.00);
  assert.equal(q.prevClose, 1680.00);
  assert.equal(q.change, 20.00);
  assert.equal(q.changePct, 1.19);
  assert.equal(q.high, 1710.00);
  assert.equal(q.low, 1670.00);
});

test('parse multiple lines', () => {
  const text = makeTencentLine('600519', '贵州茅台', '1700.00', '1680.00', '1690.00', '1710.00', '1670.00', '20.00', '1.19')
    + '\n' + makeTencentLine('000001', '平安银行', '10.50', '10.55', '10.55', '10.60', '10.40', '-0.05', '-0.47');
  const quotes = parseTencentQuote(text);
  assert.equal(quotes.length, 2);
  assert.equal(quotes[1].code, 'sz000001');
  assert.equal(quotes[1].changePct, -0.47);
});

test('empty input returns empty array', () => {
  assert.equal(parseTencentQuote('').length, 0);
});

test('suspended stock with "-" values yields price 0 not NaN', () => {
  const text = makeTencentLine('600519', '贵州茅台', '-', '-', '-', '-', '-', '-', '-');
  const q = parseTencentQuote(text)[0];
  assert.equal(Number.isFinite(q.price), true);
  assert.equal(q.price, 0);
  assert.equal(q.prevClose, 0);
});
