# watch-stock — 华为手表 A 股行情 App

HarmonyOS NEXT（Watch 5 / GT 5，API 12+）ArkTS 应用：自选股实时行情、增删管理、单只分时图。行情数据直连免费接口（东方财富实时快照 + 腾讯分时），无需自建服务器。

## 目录

```
entry/src/main/ets/
├── entryability/EntryAbility.ets   # 入口
├── pages/
│   ├── Index.ets                   # 自选列表（30s 定时刷新）
│   ├── Detail.ets                  # 单只分时图（Canvas）
│   └── Edit.ets                    # 增删自选
├── model/                          # StockQuote / MinuteData（纯 TS）
├── data/
│   ├── StockApi.ts                 # HTTP 网络层（@kit.NetworkKit）
│   ├── StockRepository.ts          # 自选清单 + Preferences 持久化
│   ├── codeUtils.ts                # 代码规范化（纯函数）
│   └── parse/                      # 腾讯/东财解析器（纯函数）
└── common/                         # Colors / Format（纯函数）
test/                               # Node 24 纯函数单测
```

## 在 DevEco Studio 中构建与装机（一次性验证）

1. 安装 DevEco Studio 5（HarmonyOS NEXT，含 SDK API 12）。
2. `File > Open` 打开本目录（`watch-stock/`），首次打开按提示 Sync / 更新 hvigor 依赖（网络需能访问 ohpm 源）。
3. 连接 Watch 5 / GT 5（开启开发者模式 + USB 调试，或用无线调试）。
4. `File > Project Structure > Signing Configs` 勾选 *Automatically generate signature*（手表首次需登录华为账号），保存。
5. 选择 `entry` + `default`，`Run` 到手表。构建如报 SDK/签名错误，按 DevEco 提示补 SDK 或签名配置。
6. 真机验证清单（见下）。

## 真机验证清单（对应设计成功标准）

- [ ] 工程构建通过，无编译错误
- [ ] App 可安装并正常启动到"自选股"列表页
- [ ] 列表显示实时价格与涨跌幅，涨红跌绿正确
- [ ] 下拉/点击"重试"或等待 30s，价格自动刷新
- [ ] "编辑"页添加代码（如 sh600519）或点预置项，回到列表出现该股
- [ ] 删除自选后重启 App，删除的股票不再出现；添加的仍在（Preferences 持久化）
- [ ] 点击列表项进入详情，看到当日分时折线 + 昨收虚线基准

## 单元测试（本仓库内可跑）

解析层与工具函数为纯 TS，本仓库（Node 24）直接运行：

```bash
cd watch-stock
node --test test/*.test.ts
```

## 数据源与切换

- 快照：东方财富 `push2.eastmoney.com/api/qt/ulist.np/get`（UTF-8 JSON，默认）。
- 分时：腾讯 `web.ifzq.gtimg.cn/appstock/app/minute/query`（UTF-8 JSON）。
- 腾讯文本快照解析（`tencentQuoteParser.ts`）保留备用；如后续需切换，改 `StockApi.fetchQuotes` 即可。
- 免费接口仅供个人低频使用，勿做商用/高频抓取。

## 已知边界（v1 不做）

K 线、表盘复杂功能、推送通知、美股/港股、自建代理、自选股代码输入的智能补全。
