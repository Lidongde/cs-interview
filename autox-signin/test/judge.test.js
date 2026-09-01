"use strict";
const { test } = require("node:test");
const assert = require("node:assert");
const judge = require("../lib/judge.js");

const hints = {
  success: ["签到成功", "金币+", "获得", "已到账"],
  already: ["已签到", "明日再来", "今日已签到", "明天再来"],
};

test("出现成功词 → ok", function () {
  assert.strictEqual(judge.judgeResult(["签到成功，金币+5"], hints), "ok");
});

test("同时出现成功词与已签到词 → ok（成功优先）", function () {
  assert.strictEqual(judge.judgeResult(["今日已签到", "获得1金币"], hints), "ok");
});

test("只出现已签到词 → already", function () {
  assert.strictEqual(judge.judgeResult(["您已签到，明日再来"], hints), "already");
});

test("都未出现 → fail", function () {
  assert.strictEqual(judge.judgeResult(["首页", "我的"], hints), "fail");
});

test("statusLabel 映射", function () {
  assert.strictEqual(judge.statusLabel("ok"), "签到成功");
  assert.strictEqual(judge.statusLabel("already"), "今日已签到");
  assert.strictEqual(judge.statusLabel("fail"), "签到失败");
});
