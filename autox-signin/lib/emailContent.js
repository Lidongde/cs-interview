"use strict";
// 纯逻辑：邮件标题与正文构建。
var judge = require("./judge.js");

function pad2(n) { return (n < 10 ? "0" : "") + n; }

function nowString(d) {
  d = d || new Date();
  return d.getFullYear() + "-" + pad2(d.getMonth() + 1) + "-" + pad2(d.getDate()) +
    " " + pad2(d.getHours()) + ":" + pad2(d.getMinutes()) + ":" + pad2(d.getSeconds());
}

function buildSubject(cfg, status) {
  return "【签到】" + (cfg.appName || cfg.app.packageName) + " " +
    judge.statusLabel(status) + " @ " + nowString();
}

function buildBody(cfg, result) {
  var label = judge.statusLabel(result.status);
  var rows = [
    ["目标 App", cfg.appName || cfg.app.packageName],
    ["执行时间", result.time || nowString()],
    ["结果", label],
    ["重试次数", String(result.attempts || 0)],
    ["说明", result.message || ""],
  ];
  var html = "<h2>" + label + "</h2><table border='1' cellpadding='6' cellspacing='0'>";
  for (var i = 0; i < rows.length; i++) {
    html += "<tr><td><b>" + rows[i][0] + "</b></td><td>" + rows[i][1] + "</td></tr>";
  }
  html += "</table>";
  return html;
}

module.exports = { nowString: nowString, buildSubject: buildSubject, buildBody: buildBody };
