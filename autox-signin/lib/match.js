"use strict";
// 纯逻辑：关键词匹配。无 AutoX 依赖，可在 Node 与 AutoX.js(Rhino) 双端运行。

// 返回 texts 数组中第一个包含任一 keyword 的下标；找不到返回 -1。
function findFirstHit(texts, keywords) {
  for (var i = 0; i < texts.length; i++) {
    for (var j = 0; j < keywords.length; j++) {
      if (typeof texts[i] === "string" &&
          texts[i].toLowerCase().indexOf(String(keywords[j]).toLowerCase()) >= 0) {
        return i;
      }
    }
  }
  return -1;
}

// texts 中是否存在任一 keyword。
function hasAny(texts, keywords) {
  return findFirstHit(texts, keywords) >= 0;
}

module.exports = { findFirstHit: findFirstHit, hasAny: hasAny };
