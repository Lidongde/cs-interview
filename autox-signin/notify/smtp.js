"use strict";
// SMTP 直发（AutoX.js + javax.mail）。需 libs/javax.mail.jar。

function sendMail(cfg, subject, html, attachmentPath) {
  var props = new java.util.Properties();
  props.setProperty("mail.smtp.host", cfg.email.smtpHost);
  props.setProperty("mail.smtp.port", String(cfg.email.port));
  props.setProperty("mail.smtp.auth", "true");
  props.setProperty("mail.smtp.connectiontimeout", "15000");
  props.setProperty("mail.smtp.timeout", "15000");
  props.setProperty("mail.smtp.writetimeout", "15000");
  if (cfg.email.useSsl) {
    props.setProperty("mail.smtp.ssl.enable", "true");
  }
  var session = javax.mail.Session.getInstance(props, null);
  var msg = new javax.mail.internet.MimeMessage(session);
  msg.setFrom(new javax.mail.internet.InternetAddress(cfg.email.from));
  for (var i = 0; i < cfg.email.to.length; i++) {
    msg.addRecipient(javax.mail.Message.RecipientType.TO,
      new javax.mail.internet.InternetAddress(cfg.email.to[i]));
  }
  msg.setSubject(subject);
  var mp = new javax.mail.internet.MimeMultipart();
  var body = new javax.mail.internet.MimeBodyPart();
  body.setContent(html, "text/html; charset=utf-8");
  mp.addBodyPart(body);
  if (attachmentPath && files.exists(attachmentPath)) {
    var att = new javax.mail.internet.MimeBodyPart();
    var ds = new javax.activation.FileDataSource(attachmentPath);
    att.setDataHandler(new javax.activation.DataHandler(ds));
    att.setFileName(files.getName(attachmentPath));
    mp.addBodyPart(att);
  }
  msg.setContent(mp);
  javax.mail.Transport.send(msg, cfg.email.user, cfg.email.authCode);
}

module.exports = { sendMail: sendMail };
