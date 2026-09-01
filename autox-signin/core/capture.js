"use strict";
// 截图留档（AutoX.js 环境）。

function capture(cfg, tag) {
  var dir = cfg.capture.dir;
  if (!files.exists(dir)) files.ensureDir(dir);
  var name = "signin-" + tag + "-" + Date.now() + ".png";
  var file = files.join(dir, name);
  var img = captureScreen();
  if (img) {
    images.save(img, file);
    img.recycle();
  }
  return file;
}

module.exports = { capture: capture };
