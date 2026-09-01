"use strict";
// 结果判定：收集文本后交给纯逻辑 judge。
var judgeLib = require("../lib/judge.js");
var locator = require("./locator.js");

function judge(cfg, texts) {
  var list = texts || locator.visibleTexts();
  return judgeLib.judgeResult(list, {
    success: cfg.app.successKeywords,
    already: cfg.app.alreadyKeywords,
  });
}

module.exports = { judge: judge };
