# 华为手表股票行情 App 设计（watch-stock）

**日期**: 2026-08-24
**状态**: 已确认，待实现

## 1. 目标与范围

### 1.1 目标
在 `cs-interview/watch-stock/` 下开发一个华为手表（HarmonyOS NEXT）应用，用于在手表屏幕上查看 A 股（沪深）股票的实时价格、涨跌，并支持自选股管理（增删）与单只股票的分时图。开发语言 ArkTS + ArkUI，目标是 Watch 5 / GT 5 等 HarmonyOS NEXT 设备。

### 1.2 范围
- **做**：
  - 自选股列表页：显示股票名称、代码、最新价、涨跌额、涨跌幅，A 股配色（红涨绿跌）
  - 自选股管理：增删自选（输入或选择股票代码），持久化保存在手表本地
  - 单只详情页：头部现价/涨跌幅 + 当日分时折线图
  - 定时刷新（30s）+ 手动刷新
- **不做（第一版）**：
  - K 线图（只做分时）
  - 表盘复杂功能（complication）快捷入口
  - 自建后端代理、推送通知、多市场（美股/港股）

### 1.3 成功标准（"跑通"的定义）
1. 工程在 DevEco Studio 5 中构建通过，无编译错误
2. App 可安装到 Watch 5 / GT 5（HarmonyOS NEXT）并正常启动
3. 列表页能看到自选股实时价格与涨跌幅，红涨绿跌配色正确
4. 可添加/删除自选股，重启 App 后自选股仍在（本地持久化）
5. 详情页能显示单只股票当日分时折线图

## 2. 已确认需求

| 决策点 | 选择 |
|--------|------|
| 市场 | A 股（沪深），红涨绿跌 |
| 目标设备 | Watch 5 / GT 5 等，HarmonyOS NEXT（API 12+） |
| 开发框架 | ArkTS + ArkUI 声明式，target=wearable |
| 数据通道 | 方案 A：手表端直连免费行情接口，不搭服务器 |
| 行情快照源 | 腾讯 `qt.gtimg.cn`（主），新浪 `hq.sinajs.cn`（备） |
| 分时数据源 | 腾讯 `web.ifzq.gtimg.cn/appstock/app/minute/query` |
| 本地持久化 | Preferences（`@ohos.data.preferences`），存自选代码列表 |
| 刷新策略 | 定时 30s + 手动刷新 |
| 功能范围 | 自选列表 + 实时价格、增删管理、单只分时图 |
| 工程位置 | `cs-interview/watch-stock/` |

## 3. 架构

### 3.1 工程形态
HarmonyOS 单工程（`AppScope` + `entry` 模块），HarmonyOS NEXT API 12+，`targets` 含 `wearable`。由 DevEco Studio 5 打开、构建、签名、装机。

### 3.2 分层结构

```
watch-stock/
├── AppScope/                          # 应用级配置（app.json5、图标）
├── entry/
│   ├── src/main/
│   │   ├── ets/
│   │   │   ├── entryability/          # EntryAbility（入口）
│   │   │   ├── pages/
│   │   │   │   ├── Index.ets          # 自选列表页（首页）
│   │   │   │   ├── Detail.ets         # 单只详情 + 分时图
│   │   │   │   └── Edit.ets           # 增删自选页
│   │   │   ├── model/
│   │   │   │   └── StockQuote.ets     # 行情模型
│   │   │   ├── data/
│   │   │   │   ├── StockApi.ets       # HTTP 请求 + 解析腾讯/新浪格式
│   │   │   │   └── StockRepository.ets# 自选清单 + 行情聚合（页面唯一入口）
│   │   │   └── common/
│   │   │       ├── Colors.ets         # A 股配色
│   │   │       └── Format.ets         # 价格/涨跌幅格式化
│   │   ├── resources/                 # 字符串、图标等资源
│   │   └── module.json5               # 声明 ohos.permission.INTERNET
│   ├── build-profile.json5
│   └── oh-package.json5
├── hvigorfile.ts
└── build-profile.json5
```

### 3.3 组件职责
- **`StockApi`**：唯一负责网络与解析。提供 `fetchQuotes(codes): Promise<StockQuote[]>`（批量快照）与 `fetchMinute(code): Promise<MinutePoint[]>`（当日分时点）。内部对腾讯 `qt.gtimg.cn` / 分时接口做 GBK 解码与字段解析。
- **`StockRepository`**：页面唯一数据入口。维护内存自选列表 + Preferences 持久化；聚合多只行情；对外暴露 `getWatchlist()`、`add(code)`、`remove(code)`、`refresh()` 与订阅通知。
- **`pages/Index`**：渲染自选列表（名称/代码/最新价/涨跌幅，涨红跌绿），下拉/定时刷新，点击进详情，长按或按钮进编辑页。
- **`pages/Detail`**：拉单只分时数据，头部显示现价/涨跌/涨跌幅，主体用 Canvas 画分时折线（含昨收基准线）。
- **`pages/Edit`**：展示当前自选，支持删除（行内删除按钮）；添加方式为**手动输入股票代码**（如 `sh600519`，带格式校验：`sh`/`sz`/`bj` 前缀 + 6 位数字），并内置一份**热门 A 股预置列表**（约 10 只常用标的）做快捷添加，避免手表上纯键盘输入的低效。

### 3.4 数据流
```
启动 → Repository 读 Preferences 自选清单
     → StockApi 批量拉行情（腾讯 qt.gtimg.cn）
     → 渲染 Index 列表（红涨绿跌）

Index: 定时 30s / 手动刷新 → Repository.refresh() → 更新列表
Index → 点击 → Detail: StockApi.fetchMinute(code) → Canvas 画分时线
Index → 增删 → Edit: Repository.add/remove → 写 Preferences → 刷新列表
```

## 4. 关键接口与格式

### 4.1 腾讯行情快照
`GET https://qt.gtimg.cn/q=sh600519,sz000001`（GBK 编码）
返回 `v_sh600519="...~...~...";` 字段串，按 `~` 分隔，取：
- 名称（1）、代码（2）、现价（3）、昨收（4）、今开（5）、最高（33）、最低（34）、涨跌额（31）、涨跌幅（32）

> **编码兜底**：腾讯/新浪快照接口为 GBK 编码，若 HarmonyOS `util.TextDecoder` 不支持 GBK，则切换主数据源为东方财富 UTF-8 JSON 接口（`https://push2.eastmoney.com/api/qt/ulist.np/get?secids=1.600519,0.000001&fields=...`，无需 Referer、返回标准 JSON）。解析层做成纯函数，数据源切换只改 `StockApi` 内部实现，不影响上层。

### 4.2 腾讯分时接口
`GET https://web.ifzq.gtimg.cn/appstock/app/minute/query?code=sh600519`
返回 JSON，`data[code].data.data` 为 `[HHMM, price]` 点数组；`data[code].qt` 含现价/昨收。网络请求需带合理 UA/Referer，超时兜底。

### 4.3 数据模型
```
StockQuote {
  code: string      // sh600519
  name: string
  price: number
  prevClose: number
  change: number    // 涨跌额
  changePct: number // 涨跌幅 %
  high: number
  low: number
}
MinutePoint { time: string /* HHMM */, price: number }
```

## 5. 错误处理
- 行情拉取失败：列表页显示"加载失败"占位 + 重试按钮；不阻塞已缓存内容（保留上次数据）。
- 分时拉取失败：详情页显示错误提示，可重试。
- 请求超时（如 10s）：统一超时兜底，按失败处理。
- 无网络/网络错误：提示检查连接。
- 增删自选：本地操作不依赖网络，失败即提示（Preferences 写入异常）。

## 6. 测试

### 6.1 单元测试（解析层）
用固定样例字符串/JSON 喂给 `StockApi` 的解析函数，验证字段映射与边界（停牌、价格为 0、空数据）。可在本仓库用纯 JS/TS 逻辑做，不依赖 HarmonyOS 运行时（解析逻辑与网络层分离，解析为纯函数）。

### 6.2 手工验证（需 DevEco Studio）
- 构建通过、签名、装机到 Watch 5 / GT5
- 列表页实时价格与红涨绿跌配色
- 增删自选 + 重启后持久化
- 详情页分时折线图显示正确

> 注意：本开发环境无法安装 HarmonyOS SDK，工程骨架与源码在本仓库完成，构建/装机需在用户本机 DevEco Studio 5 上进行。

## 7. 明确不做 / 后续可做
- K 线图、表盘复杂功能、推送通知、多市场、自建代理、深色主题切换（手表默认深色）
