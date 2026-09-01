"use strict";
// 幂等锁：防止定时任务并发执行（AutoX.js 环境）。

var LOCK = "/sdcard/Download/signin-log/.running";

function isRunning() { return files.exists(LOCK); }

function acquire() {
  if (files.exists(LOCK)) return false;
  files.ensureDir("/sdcard/Download/signin-log");
  files.write(LOCK, String(Date.now()));
  return true;
}

function release() {
  if (files.exists(LOCK)) files.remove(LOCK);
}

module.exports = { isRunning: isRunning, acquire: acquire, release: release };
