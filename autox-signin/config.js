"use strict";
// ============================================================
// 部署配置：把下方需要填写的字段改成你自己的值
// 邮箱：163 需先在网页端设置里开启 SMTP 并获取「授权码」（非登录密码）
// ============================================================
var lib = require("./lib/config.js");

var cfg = lib.defaultConfig();

cfg.schedule = { hour: 9, minute: 0 };

// 目标 App（默认快手极速版）
cfg.appName = "快手极速版";
cfg.app.packageName = "com.kuaishou.nebula";

// 若某天 UI 改版导致关键词都点不到，可填兜底坐标（手动看截图后填）
// cfg.app.fallbackTap = { x: 540, y: 1800 };

// 屏幕：manual=需要每天第一次手动解锁（推荐）；pin=脚本输入PIN
cfg.screen.unlockMode = "manual";

// 邮箱（改成你的）
cfg.email.smtpHost = "smtp.163.com";
cfg.email.port = 465;
cfg.email.useSsl = true;
cfg.email.user = "你的账号@163.com";
cfg.email.authCode = "你的SMTP授权码";
cfg.email.from = "你的账号@163.com";
cfg.email.to = ["收件邮箱@163.com"];

// 通知方式：smtp | webhook
cfg.notify.mode = "smtp";

module.exports = cfg;
