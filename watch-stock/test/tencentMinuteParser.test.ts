import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseTencentMinute } from '../entry/src/main/ets/data/parse/tencentMinuteParser.ts';

const SAMPLE = '{"code":0,"msg":"","data":{"sh600519":{' +
  '"data":{"date":"20260824","data":["0930 1698.00","0931 1699.50","1000 1700.00","1500 1700.00"]},' +
  '"qt":{"sh600519":["1~贵州茅台~600519~1700.00~1680.00~1690.00~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~20.00~1.19~1710.00~1670.00"]}' +
  '}}}';

test('parse tencent minute points and meta', () => {
  const data = parseTencentMinute(SAMPLE, 'sh600519');
  assert.equal(data.points.length, 4);
  assert.equal(data.points[0].time, '0930');
  assert.equal(data.points[0].price, 1698.00);
  assert.equal(data.points[3].price, 1700.00);
  assert.equal(data.prevClose, 1680.00);
  assert.equal(data.current, 1700.00);
  assert.equal(data.date, '20260824');
});

test('empty input returns empty data', () => {
  const data = parseTencentMinute('', 'sh600519');
  assert.equal(data.points.length, 0);
  assert.equal(data.prevClose, 0);
});
