"use strict";
// 追加写日志（AutoX.js 环境）。

function logFile(cfg) {
  var dir = files.join(cfg.capture.dir, "log");
  if (!files.exists(dir)) files.ensureDir(dir);
  var d = new Date();
  var p = function (n) { return (n < 10 ? "0" : "") + n; };
  return files.join(dir, "signin-" + d.getFullYear() + p(d.getMonth() + 1) + p(d.getDate()) + ".log");
}

function write(cfg, result) {
  var line = "[" + new Date().toISOString() + "] " + result.status + " | " +
    (result.message || "") + " | attempts=" + (result.attempts || 0) + " | " + (result.screenshot || "");
  files.append(logFile(cfg), line + "\n");
  console.log(line);
}

module.exports = { write: write, logFile: logFile };
