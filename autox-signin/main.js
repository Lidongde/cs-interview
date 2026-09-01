"use strict";
// 主流程：定时触发 → 亮屏解锁 → 打开App → 点击签到 → 判定 → 截图 → 通知
var cfg = require("./config.js");
var lib = require("./lib/config.js");
var emailContent = require("./lib/emailContent.js");
var unlock = require("./core/unlock.js");
var launcher = require("./core/appLauncher.js");
var locator = require("./core/locator.js");
var verifier = require("./core/verifier.js");
var capture = require("./core/capture.js");
var logger = require("./util/logger.js");
var state = require("./util/state.js");
var notify = require("./notify/notify.js");

// 清理超过 keepDays 天的旧截图
function pruneScreenshots(cfg) {
  var dir = cfg.capture.dir;
  var cutoff = Date.now() - (cfg.capture.keepDays * 86400000);
  try {
    var names = files.listDir(dir);
    for (var i = 0; i < names.length; i++) {
      var p = files.join(dir, names[i]);
      var f = new java.io.File(p);
      if (f.isFile() && f.lastModified() < cutoff) {
        files.remove(p);
      }
    }
  } catch (e) {}
}

function main() {
  var problems = lib.validateConfig(cfg);
  if (problems.length > 0) {
    console.log("配置校验失败: " + problems.join("; "));
    return;
  }
  if (!state.acquire()) {
    console.log("已有任务运行，跳过本次");
    return;
  }
  var result = {
    status: "fail", app: cfg.app.packageName,
    attempts: 0, message: "", time: emailContent.nowString(),
    screenshot: "",
  };
  try {
    unlock.ensureScreenOn(cfg);
    launcher.launchApp(cfg);
    for (var a = 0; a <= cfg.retry.times; a++) {
      if (a > 0) { sleep(cfg.retry.intervalMs); }
      result.attempts = a;
      var clicked = locator.tapSignButton(cfg);
      sleep(2000);
      var status = verifier.judge(cfg);
      result.status = status;
      result.message = clicked
        ? "已点击签到入口，判定=" + status
        : "未定位到签到入口（可能已签到或 UI 改版）";
      if (status !== "fail") break;
    }
  } catch (e) {
    result.status = "fail";
    result.message = String((e && e.message) || e);
  } finally {
    try {
      result.screenshot = capture.capture(cfg, result.status);
      pruneScreenshots(cfg);
    } catch (e) {}
    try { logger.write(cfg, result); } catch (e) { console.log("日志写入失败: " + e); }
    state.release();
  }
  result.subject = emailContent.buildSubject(cfg, result.status);
  result.body = emailContent.buildBody(cfg, result);
  try {
    notify.notify(cfg, result);
  } catch (e) {
    logger.write(cfg, { status: "notify-fail", message: String((e && e.message) || e), attempts: 0, screenshot: "" });
  }
  console.log("完成: " + result.status);
}

main();
