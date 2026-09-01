"use strict";
// 定位签到入口、关闭弹窗、收集可见文本（AutoX.js 环境）。
var match = require("../lib/match.js");

// 收集当前界面可见文本列表
function visibleTexts() {
  var out = [];
  var nodes = textMatches(/.*/).find();
  for (var i = 0; i < nodes.length; i++) {
    var t = nodes[i].text();
    if (t) out.push(String(t));
  }
  return out;
}

// 尝试关闭营销弹窗/引导浮层
function closePopups() {
  var kws = ["关闭", "跳过", "知道了", "暂不", "x", "X"];
  for (var i = 0; i < kws.length; i++) {
    var node = desc(kws[i]).findOnce() || text(kws[i]).findOnce();
    if (node && node.clickable()) {
      node.click();
      sleep(800);
    }
  }
  back();
  sleep(500);
}

// 点击签到入口；成功返回 true，失败（含坐标兜底失败）返回 false
function tapSignButton(cfg) {
  closePopups();
  var kws = cfg.app.signKeywords;
  for (var k = 0; k < kws.length; k++) {
    var node = textContains(kws[k]).findOne(2000);
    if (node) {
      node.click();
      sleep(1500);
      return true;
    }
  }
  if (cfg.app.fallbackTap) {
    click(cfg.app.fallbackTap.x, cfg.app.fallbackTap.y);
    sleep(1500);
    return true;
  }
  return false;
}

function alreadySigned(cfg) {
  return match.hasAny(visibleTexts(), cfg.app.alreadyKeywords);
}

module.exports = { visibleTexts: visibleTexts, closePopups: closePopups, tapSignButton: tapSignButton, alreadySigned: alreadySigned };
