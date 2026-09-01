"use strict";
// 纯逻辑：结果判定。success 优先于 already。
var match = require("./match.js");

function judgeResult(texts, hints) {
  if (match.hasAny(texts, hints.success)) return "ok";
  if (match.hasAny(texts, hints.already)) return "already";
  return "fail";
}

function statusLabel(status) {
  if (status === "ok") return "签到成功";
  if (status === "already") return "今日已签到";
  return "签到失败";
}

module.exports = { judgeResult: judgeResult, statusLabel: statusLabel };
