# 快手极速版自动签到（AutoX.js）

华为 Mate 60 Pro（HarmonyOS 4.x）每日定点打开快手极速版签到，并把结果发邮件。

## 前置条件
- HarmonyOS 4.x（NEXT 不适用本方案）
- 安装 AutoX.js v6（自动签到社区常用，可在其官网/应用市场获取 APK）
- 163/QQ 邮箱已开启 SMTP 并取得「授权码」

## 安装步骤
1. 安装 AutoX.js，开启：无障碍服务、悬浮窗、自启动（设置→应用→AutoX.js→应用启动管理→手动管理全开）、电池优化→不允许优化。
2. 把 `autox-signin/` 整个目录放入手机存储，例如 `/sdcard/autox-signin/`。
3. 下载 `javax.mail-1.6.2.jar` 与 `javax.activation-1.2.0.jar` 两个 jar 都放入 `libs/`（activation 下载地址：`https://repo1.maven.org/maven2/com/sun/activation/javax.activation/1.2.0/javax.activation-1.2.0.jar`）。发送邮件附件依赖 activation，两个 jar 缺一不可。
4. 编辑 `config.js`，填：邮箱账号/授权码/收件人；如需脚本解锁，改 `unlockMode:"pin"` 并填 `pin`。
5. 在 AutoX.js 中导入项目并打开 `main.js`，先点运行做一次手动验证。
6. 通过 AutoX.js「定时任务」添加：每天 09:00 执行 `main.js`。
7. （可选加固）用鸿蒙「智慧生活」创建场景：每天 08:59 打开 AutoX.js，兜底触发。

## 结果判定
- 成功：邮件标题「签到成功」
- 已签到：标题「今日已签到」（视为成功，不重复点击）
- 失败：标题「签到失败」+ 截图附件，需人工处理

## 常见问题
- 找不到签到入口：看失败截图 → 在 `config.js` 里加一行 `cfg.app.signKeywords = ["签到", "去签到", ...]` 覆盖默认关键词，或填 `cfg.app.fallbackTap = { x: 540, y: 1800 }` 兜底坐标。
- 无障碍服务被回收：重新打开 AutoX.js 并确认服务开启；检查自启动与电池优化设置。
- 邮件发不出：确认 SMTP 授权码正确、收件人正确；163 端口 465/SSL。
- 邮件收到但附件/截图没到：检查 `libs/` 中同时存在 `javax.mail-1.6.2.jar` 与 `javax.activation-1.2.0.jar`（缺少 activation 会导致附件无法发送）。
- 每天重复「已签到」：属正常（当天只签一次）。
- closePopups 返回键行为：首次运行请人工盯着看一次——如果脚本总是按返回键、导致没进入签到页，说明弹窗关闭逻辑的 `back()` 影响了导航（已知行为），可调整 `locator.closePopups()` 中的关键词或注释掉最后的 `back()`。
- 通知失败无补发：邮件是唯一告警通道；若发送失败，脚本只记日志、不会补发（已知限制）。

## 测试
纯逻辑模块在本机跑：`node --test`（需 Node ≥ 18）。
