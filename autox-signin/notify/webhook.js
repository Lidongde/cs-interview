"use strict";
// webhook 兜底：POST 到自建服务，由服务端发信。

function notifyWebhook(cfg, result) {
  http.postJson(cfg.notify.webhookUrl, {
    title: result.subject,
    status: result.status,
    message: result.message || "",
    time: result.time,
  });
}

module.exports = { notifyWebhook: notifyWebhook };
