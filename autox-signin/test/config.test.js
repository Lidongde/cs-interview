"use strict";
const { test } = require("node:test");
const assert = require("node:assert");
const config = require("../lib/config.js");

test("默认配置含快手极速版包名与关键词", function () {
  const cfg = config.defaultConfig();
  assert.strictEqual(cfg.app.packageName, "com.kuaishou.nebula");
  assert.ok(cfg.app.signKeywords.indexOf("签到") >= 0);
  assert.strictEqual(cfg.screen.unlockMode, "manual");
});

test("完整配置校验通过（空问题）", function () {
  const cfg = config.defaultConfig();
  cfg.email.user = "a@163.com";
  cfg.email.authCode = "xxx";
  cfg.email.from = "a@163.com";
  cfg.email.to = ["b@163.com"];
  assert.deepStrictEqual(config.validateConfig(cfg), []);
});

test("缺邮箱配置会报问题", function () {
  const cfg = config.defaultConfig();
  assert.ok(config.validateConfig(cfg).length > 0);
});

test("unlockMode=pin 但无 pin 报问题", function () {
  const cfg = config.defaultConfig();
  cfg.screen.unlockMode = "pin";
  assert.ok(config.validateConfig(cfg).indexOf("unlockMode=pin 但未配置 pin") >= 0);
});
