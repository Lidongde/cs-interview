import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseEastmoneyQuote, toEastmoneySecId } from '../entry/src/main/ets/data/parse/eastmoneyQuoteParser.ts';

const SAMPLE = '{"rc":0,"data":{"total":2,"diff":[' +
  '{"f12":"600519","f14":"贵州茅台","f2":1700.0,"f3":1.19,"f4":20.0,"f15":1710.0,"f16":1670.0,"f17":1690.0,"f18":1680.0},' +
  '{"f12":"000001","f14":"平安银行","f2":10.5,"f3":-0.47,"f4":-0.05,"f15":10.6,"f16":10.4,"f17":10.55,"f18":10.55}' +
  ']}}';

test('parse eastmoney quote maps f12 back to original codes', () => {
  const quotes = parseEastmoneyQuote(SAMPLE, ['sh600519', 'sz000001']);
  assert.equal(quotes.length, 2);
  assert.equal(quotes[0].code, 'sh600519');
  assert.equal(quotes[0].name, '贵州茅台');
  assert.equal(quotes[0].price, 1700.0);
  assert.equal(quotes[0].changePct, 1.19);
  assert.equal(quotes[0].prevClose, 1680.0);
  assert.equal(quotes[1].code, 'sz000001');
  assert.equal(quotes[1].changePct, -0.47);
});

test('suspended stock with "-" values coerces to 0', () => {
  const text = '{"data":{"diff":[{"f12":"600000","f14":"浦发银行","f2":"-","f3":"-","f4":"-","f15":"-","f16":"-","f17":"-","f18":10.0}]}}';
  const quotes = parseEastmoneyQuote(text, ['sh600000']);
  assert.equal(quotes.length, 1);
  assert.equal(quotes[0].price, 0);
  assert.equal(quotes[0].prevClose, 10.0);
});

test('empty or empty-diff input returns empty array', () => {
  assert.equal(parseEastmoneyQuote('', ['sh600519']).length, 0);
  assert.equal(parseEastmoneyQuote('{"data":{}}', ['sh600519']).length, 0);
});

test('toEastmoneySecId mapping', () => {
  assert.equal(toEastmoneySecId('sh600519'), '1.600519');
  assert.equal(toEastmoneySecId('sz000001'), '0.000001');
  assert.equal(toEastmoneySecId('bj920001'), '2.920001');
});
