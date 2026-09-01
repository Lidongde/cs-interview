"use strict";
const { test } = require("node:test");
const assert = require("node:assert");
const match = require("../lib/match.js");

test("findFirstHit 返回首个命中关键词的下标", function () {
  assert.strictEqual(match.findFirstHit(["首页", "去签到", "我的"], ["签到"]), 1);
});

test("findFirstHit 命中第二个关键词", function () {
  assert.strictEqual(match.findFirstHit(["首页", "任务中心", "已签到"], ["签到", "任务中心"]), 1);
});

test("findFirstHit 未命中返回 -1", function () {
  assert.strictEqual(match.findFirstHit(["首页", "我的"], ["签到"]), -1);
});

test("findFirstHit 空输入", function () {
  assert.strictEqual(match.findFirstHit([], ["签到"]), -1);
  assert.strictEqual(match.findFirstHit(["a"], []), -1);
});

test("findFirstHit 大小写不敏感", function () {
  assert.strictEqual(match.findFirstHit(["Sign In"], ["sign"]), 0);
});

test("hasAny 命中与未命中", function () {
  assert.strictEqual(match.hasAny(["已签到"], ["已签到", "明日再来"]), true);
  assert.strictEqual(match.hasAny(["去玩"], ["已签到"]), false);
});
