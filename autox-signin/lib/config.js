"use strict";
// 纯逻辑：默认配置与校验。无 AutoX 依赖，可在 Node 与 AutoX.js(Rhino) 双端运行。

function defaultConfig() {
  return {
    appName: "快手极速版",
    schedule: { hour: 9, minute: 0 },
    app: {
      packageName: "com.kuaishou.nebula",
      launchDelayMs: 8000,
      signKeywords: ["签到", "去签到", "立即签到", "领金币", "今日任务"],
      alreadyKeywords: ["已签到", "明日再来", "今日已签到", "明天再来"],
      successKeywords: ["签到成功", "金币+", "获得", "已到账"],
      fallbackTap: null, // 兜底坐标 {x, y}
    },
    screen: { wakeUp: true, unlockMode: "manual", pin: "" },
    email: {
      smtpHost: "smtp.163.com", port: 465, useSsl: true,
      user: "", authCode: "", from: "", to: [],
    },
    notify: { mode: "smtp", webhookUrl: "" },
    retry: { times: 2, intervalMs: 30000 },
    capture: { dir: "/sdcard/Download/signin-log", keepDays: 7 },
  };
}

// 返回问题列表；空数组表示通过。
function validateConfig(cfg) {
  var problems = [];
  if (!cfg) return ["config 为空"];
  if (!cfg.app || !cfg.app.packageName) problems.push("app.packageName 缺失");
  if (!cfg.email || !cfg.email.user || !cfg.email.authCode || !cfg.email.from) {
    problems.push("email 配置不完整（user/authCode/from）");
  }
  if (!cfg.email || !cfg.email.to || cfg.email.to.length === 0) problems.push("email.to 为空");
  if (cfg.screen && cfg.screen.unlockMode === "pin" && !cfg.screen.pin) {
    problems.push("unlockMode=pin 但未配置 pin");
  }
  return problems;
}

module.exports = { defaultConfig: defaultConfig, validateConfig: validateConfig };
