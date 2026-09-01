"use strict";
var smtp = require("./smtp.js");
var webhook = require("./webhook.js");

function notify(cfg, result) {
  if (cfg.notify.mode === "webhook") {
    webhook.notifyWebhook(cfg, result);
    return;
  }
  smtp.sendMail(cfg, result.subject, result.body, result.screenshot);
}

module.exports = { notify: notify };
