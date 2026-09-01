"use strict";
const { test } = require("node:test");
const assert = require("node:assert");
const ec = require("../lib/emailContent.js");

test("nowString 格式", function () {
  const s = ec.nowString(new Date(2026, 7, 31, 9, 5, 3)); // 2026-08-31 09:05:03
  assert.strictEqual(s, "2026-08-31 09:05:03");
});

test("buildSubject 含 App 名与状态", function () {
  const cfg = { appName: "快手极速版", app: { packageName: "x" } };
  const s = ec.buildSubject(cfg, "ok");
  assert.ok(s.indexOf("【签到】") === 0);
  assert.ok(s.indexOf("快手极速版") > 0);
  assert.ok(s.indexOf("签到成功") > 0);
});

test("buildBody 为 HTML 且含状态与时间", function () {
  const cfg = { appName: "快手极速版", app: { packageName: "x" } };
  const result = { status: "already", time: "2026-08-31 09:00:01", attempts: 0, message: "已签到" };
  const html = ec.buildBody(cfg, result);
  assert.ok(html.indexOf("<h2>") >= 0);
  assert.ok(html.indexOf("今日已签到") >= 0);
  assert.ok(html.indexOf("2026-08-31 09:00:01") >= 0);
});
