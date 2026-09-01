"use strict";
// 亮屏与解锁（AutoX.js 环境）。unlockMode: none|pin|manual。

function ensureScreenOn(cfg) {
  if (cfg.screen.wakeUp && !device.isScreenOn()) {
    device.wakeUp();
    sleep(1000);
  }
  if (cfg.screen.unlockMode === "pin") {
    unlockWithPin(cfg.screen.pin);
  }
}

function unlockWithPin(pin) {
  // 华为锁屏可能出现「输入密码」或数字键盘，做兜底尝试
  var locked = text("输入密码").findOnce() || text("密码").findOnce() || id("com.android.systemui:id/key0").findOnce();
  if (!locked) return;
  swipe(device.width / 2, device.height * 0.8, device.width / 2, device.height * 0.3, 300);
  sleep(600);
  for (var i = 0; i < pin.length; i++) {
    var node = text(String(pin.charAt(i))).findOne(2000);
    if (node) { node.click(); sleep(350); }
  }
}

module.exports = { ensureScreenOn: ensureScreenOn };
