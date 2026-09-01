"use strict";
// 幂等锁：防止定时任务并发执行（AutoX.js 环境）。
// 锁文件放在运行时目录下；目录由调用方传入（cfg.capture.dir），避免硬编码路径。

function lockPath(baseDir) {
  return files.join(baseDir, ".running");
}

function isRunning(baseDir) {
  return files.exists(lockPath(baseDir));
}

function acquire(baseDir) {
  var p = lockPath(baseDir);
  if (files.exists(p)) return false;
  files.ensureDir(baseDir);
  files.write(p, String(Date.now()));
  return true;
}

function release(baseDir) {
  var p = lockPath(baseDir);
  if (files.exists(p)) files.remove(p);
}

module.exports = { isRunning: isRunning, acquire: acquire, release: release };
