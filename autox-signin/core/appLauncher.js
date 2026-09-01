"use strict";
// 打开目标 App（AutoX.js 环境）。

function launchApp(cfg) {
  var pkg = cfg.app.packageName;
  if (!app.isAppInstalled(pkg)) {
    throw new Error("App 未安装: " + pkg);
  }
  app.launch(pkg);
  sleep(cfg.app.launchDelayMs || 8000);
}

module.exports = { launchApp: launchApp };
