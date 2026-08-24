# 华为手表 A 股行情 App（watch-stock）实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `watch-stock/` 下交付一个 HarmonyOS NEXT（Watch 5 / GT 5）ArkTS 应用：自选股列表实时行情、增删管理、单只分时图。

**Architecture:** 手表端直连免费行情接口（方案 A），不搭服务器。数据层分两部分：纯解析/工具函数（`.ts`，无 HarmonyOS 依赖，可在本环境 Node 24 单测）与网络/持久化层（`.ts`，用 `@kit.NetworkKit` / `@kit.ArkData`，需 DevEco 构建验证）。UI 三层页面（Index / Detail / Edit）用 ArkUI 声明式，行情源默认东方财富 UTF-8 JSON（规避腾讯接口的 GBK 解码风险，见 spec 4.1 兜底条款），分时用腾讯 JSON 接口。

**Tech Stack:** ArkTS + ArkUI（HarmonyOS NEXT API 12，target=wearable）、Preferences（本地持久化）、Canvas（分时折线）、Node 24 原生 TS 类型剥离做纯函数单测。

## Global Constraints

- 工程根目录：`watch-stock/`（相对本仓库根）。
- 非 UI 逻辑一律 `.ts` 纯文件；纯解析/工具函数**不得 import 任何 HarmonyOS kit**（`@kit.*` / `@ohos.*`），保证可用 `node --test` 在 Node 24 下单测。
- 纯文件之间对类型的引用必须用 `import type` + **无扩展名**相对路径（ArkTS 要求无扩展名，Node 类型剥离会整体擦除 `import type`，运行时不需要解析该路径）。
- 测试文件 import 被测 `.ts` 时必须带 `.ts` 扩展名（Node ESM 要求）；被测文件位于 `entry/src/main/ets/` 下，测试文件位于 `watch-stock/test/`。
- 行情源：快照默认东方财富 `https://push2.eastmoney.com/api/qt/ulist.np/get`（UTF-8 JSON）；分时用腾讯 `https://web.ifzq.gtimg.cn/appstock/app/minute/query`（UTF-8 JSON）。腾讯文本快照解析保留但不作为默认源。
- A 股配色：红涨绿跌。UP=`#F5222D`，DOWN=`#00B42A`，FLAT=`#9E9E9E`，主文字 `#FFFFFF`，次级文字 `#AAAAAA`。
- `entry/src/main/module.json5` 必须声明 `ohos.permission.INTERNET`。
- 所有 `.json5` 文件写成合法 JSON（无注释、无尾逗号），以便本环境用 `JSON.parse` 校验。
- 所有 git 提交信息用 **ASCII**（本环境 bash 启动脚本会破坏含非 ASCII 的命令行参数，中文提交信息会导致 commit 不执行）。
- 每个任务以独立 commit 结束。

---

### Task 1: HarmonyOS 工程脚手架

**Files:**
- Create: `watch-stock/.gitignore`
- Create: `watch-stock/build-profile.json5`（根）
- Create: `watch-stock/hvigorfile.ts`（根）
- Create: `watch-stock/hvigor/hvigor-config.json5`
- Create: `watch-stock/oh-package.json5`（根）
- Create: `watch-stock/AppScope/app.json5`
- Create: `watch-stock/AppScope/resources/base/element/string.json`
- Create: `watch-stock/entry/build-profile.json5`
- Create: `watch-stock/entry/hvigorfile.ts`
- Create: `watch-stock/entry/oh-package.json5`
- Create: `watch-stock/entry/obfuscation-rules.txt`
- Create: `watch-stock/entry/src/main/module.json5`
- Create: `watch-stock/entry/src/main/ets/entryability/EntryAbility.ets`
- Create: `watch-stock/entry/src/main/resources/base/element/string.json`
- Create: `watch-stock/entry/src/main/resources/base/element/color.json`
- Create: `watch-stock/entry/src/main/resources/base/profile/main_pages.json`
- Create: `watch-stock/tools/gen_icons.js`（无依赖 PNG 生成器）
- Create（由脚本生成）: `watch-stock/AppScope/resources/base/media/app_icon.png`、`watch-stock/entry/src/main/resources/base/media/icon.png`

**Interfaces:**
- Consumes: 无。
- Produces: 可被 DevEco Studio 5 直接打开的工程骨架；`pages/Index` 为启动页；`module.json5` 已声明 INTERNET 权限；后续任务的源文件放入 `entry/src/main/ets/` 对应目录。

- [ ] **Step 1: 创建目录与 `.gitignore`**

```text
watch-stock/.gitignore:
/node_modules
/oh_modules
/.hvigor
/.idea
**/build
/.cxx
/.clangd
/.clang-format
/.clang-tidy
**/.test
```

用 `mkdir -p` 创建目录树（Git Bash）：

```bash
cd /d/Workspace/Project/cs-interview && mkdir -p watch-stock/AppScope/resources/base/element watch-stock/AppScope/resources/base/media watch-stock/hvigor watch-stock/entry/src/main/ets/entryability watch-stock/entry/src/main/resources/base/element watch-stock/entry/src/main/resources/base/media watch-stock/entry/src/main/resources/base/profile watch-stock/tools watch-stock/test
```

- [ ] **Step 2: 写根级配置文件**

`watch-stock/build-profile.json5`（根）：
```json
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "compileSdkVersion": "5.0.0(12)",
        "compatibleSdkVersion": "5.0.0(12)",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "strictMode": {
            "caseSensitiveCheck": true,
            "useNormalizedOHMUrl": true
          }
        }
      }
    ],
    "buildModeSet": [
      { "name": "debug" },
      { "name": "release" }
    ]
  },
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        { "name": "default", "applyToProducts": ["default"] }
      ]
    }
  ]
}
```

`watch-stock/hvigorfile.ts`（根）：
```typescript
import { appTasks } from '@ohos/hvigor-ohos-plugin';

export default {
  system: appTasks,
  plugins: []
}
```

`watch-stock/hvigor/hvigor-config.json5`：
```json
{
  "modelVersion": "5.0.0",
  "dependencies": {},
  "execution": {
    "analyze": "normal",
    "daemon": true,
    "incremental": true
  }
}
```

`watch-stock/oh-package.json5`（根）：
```json
{
  "modelVersion": "5.0.0",
  "name": "watch_stock",
  "version": "1.0.0",
  "description": "huawei watch A-share stock quote app",
  "dependencies": {},
  "devDependencies": {
    "@ohos/hvigor-ohos-plugin": "5.0.2",
    "@ohos/hypium": "1.0.19",
    "@ohos/hamock": "1.0.0"
  }
}
```

`watch-stock/AppScope/app.json5`：
```json
{
  "app": {
    "bundleName": "com.example.watchstock",
    "vendor": "example",
    "versionCode": 1000000,
    "versionName": "1.0.0",
    "icon": "$media:app_icon",
    "label": "$string:app_name"
  }
}
```

`watch-stock/AppScope/resources/base/element/string.json`：
```json
{
  "string": [
    { "name": "app_name", "value": "股票行情" }
  ]
}
```

- [ ] **Step 3: 写 entry 模块配置文件**

`watch-stock/entry/build-profile.json5`：
```json
{
  "apiType": "stageMode",
  "buildOption": {},
  "buildOptionSet": [
    {
      "name": "release",
      "arkOptions": {
        "obfuscation": {
          "ruleOptions": {
            "enable": false,
            "files": ["./obfuscation-rules.txt"]
          }
        }
      }
    }
  ],
  "targets": [
    { "name": "default" }
  ]
}
```

`watch-stock/entry/hvigorfile.ts`：
```typescript
import { hapTasks } from '@ohos/hvigor-ohos-plugin';

export default {
  system: hapTasks,
  plugins: []
}
```

`watch-stock/entry/oh-package.json5`：
```json
{
  "name": "entry",
  "version": "1.0.0",
  "description": "watch stock entry module",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {}
}
```

`watch-stock/entry/obfuscation-rules.txt`：空文件。

`watch-stock/entry/src/main/module.json5`：
```json
{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",
    "deviceTypes": ["wearable"],
    "deliveryWithInstall": true,
    "installationFree": false,
    "pages": "$profile:main_pages",
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": ["entity.system.home"],
            "actions": ["action.system.home"]
          }
        ]
      }
    ],
    "requestPermissions": [
      {
        "name": "ohos.permission.INTERNET"
      }
    ]
  }
}
```

`watch-stock/entry/src/main/resources/base/element/string.json`：
```json
{
  "string": [
    { "name": "module_desc", "value": "watch stock module" },
    { "name": "EntryAbility_desc", "value": "A-share watchlist realtime quote" },
    { "name": "EntryAbility_label", "value": "股票行情" }
  ]
}
```

`watch-stock/entry/src/main/resources/base/element/color.json`：
```json
{
  "color": [
    { "name": "start_window_background", "value": "#000000" }
  ]
}
```

`watch-stock/entry/src/main/resources/base/profile/main_pages.json`：
```json
{
  "src": ["pages/Index", "pages/Detail", "pages/Edit"]
}
```

- [ ] **Step 4: 写 EntryAbility**

`watch-stock/entry/src/main/ets/entryability/EntryAbility.ets`：
```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN: number = 0x0000;
const TAG: string = 'WatchStock';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, TAG, 'Ability onCreate');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, TAG, 'Failed to load content: %{public}s', JSON.stringify(err));
        return;
      }
    });
  }
}
```

- [ ] **Step 5: 用脚本生成占位图标 PNG**

`watch-stock/tools/gen_icons.js`（无第三方依赖，用 Node 内置 `zlib.crc32`）：
```javascript
const zlib = require('zlib');
const fs = require('fs');
const path = require('path');

function chunk(type, data) {
  const len = Buffer.alloc(4);
  len.writeUInt32BE(data.length);
  const typeBuf = Buffer.from(type, 'ascii');
  const crc = Buffer.alloc(4);
  crc.writeUInt32BE(zlib.crc32(Buffer.concat([typeBuf, data])) >>> 0);
  return Buffer.concat([len, typeBuf, data, crc]);
}

function makePng(width, height, rgb) {
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(width, 0);
  ihdr.writeUInt32BE(height, 4);
  ihdr[8] = 8;
  ihdr[9] = 2;
  const raw = Buffer.alloc(height * (1 + width * 3));
  for (let y = 0; y < height; y++) {
    raw[y * (1 + width * 3)] = 0;
    for (let x = 0; x < width; x++) {
      const off = y * (1 + width * 3) + 1 + x * 3;
      raw[off] = rgb[0];
      raw[off + 1] = rgb[1];
      raw[off + 2] = rgb[2];
    }
  }
  const idat = zlib.deflateSync(raw);
  return Buffer.concat([sig, chunk('IHDR', ihdr), chunk('IDAT', idat), chunk('IEND', Buffer.alloc(0))]);
}

const root = path.join(__dirname, '..');
const targets = [
  path.join(root, 'AppScope/resources/base/media/app_icon.png'),
  path.join(root, 'entry/src/main/resources/base/media/icon.png')
];
for (const t of targets) {
  fs.mkdirSync(path.dirname(t), { recursive: true });
  fs.writeFileSync(t, makePng(216, 216, [33, 33, 33]));
  console.log('written', t);
}
```

运行：
```bash
cd /d/Workspace/Project/cs-interview/watch-stock && node tools/gen_icons.js
```
Expected: 两行 `written ...`，无报错。

- [ ] **Step 6: 校验所有 JSON/JSON5 与 PNG 签名**

```bash
cd /d/Workspace/Project/cs-interview/watch-stock && node -e "
const fs=require('fs');
const files=['build-profile.json5','oh-package.json5','hvigor/hvigor-config.json5','AppScope/app.json5','AppScope/resources/base/element/string.json','entry/build-profile.json5','entry/oh-package.json5','entry/src/main/module.json5','entry/src/main/resources/base/element/string.json','entry/src/main/resources/base/element/color.json','entry/src/main/resources/base/profile/main_pages.json'];
for (const f of files) { JSON.parse(fs.readFileSync(f,'utf8')); console.log('OK', f); }
for (const f of ['AppScope/resources/base/media/app_icon.png','entry/src/main/resources/base/media/icon.png']) {
  const b=fs.readFileSync(f); if (!(b[0]===137&&b[1]===80&&b[2]===78&&b[3]===71)) throw new Error('bad png '+f); console.log('OK', f);
}
"
```
Expected: 每行 `OK ...`，无异常抛出。

- [ ] **Step 7: 提交**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "feat(watch-stock): scaffold harmonyos NEXT project"
```
注意：提交信息必须为 ASCII。

---

### Task 2: 数据模型与纯解析层（Node 可单测）

**Files:**
- Create: `watch-stock/entry/src/main/ets/model/StockQuote.ts`
- Create: `watch-stock/entry/src/main/ets/model/MinuteData.ts`
- Create: `watch-stock/entry/src/main/ets/data/codeUtils.ts`
- Create: `watch-stock/entry/src/main/ets/data/parse/tencentQuoteParser.ts`
- Create: `watch-stock/entry/src/main/ets/data/parse/eastmoneyQuoteParser.ts`
- Create: `watch-stock/entry/src/main/ets/data/parse/tencentMinuteParser.ts`
- Create: `watch-stock/test/tencentQuoteParser.test.ts`
- Create: `watch-stock/test/eastmoneyQuoteParser.test.ts`
- Create: `watch-stock/test/tencentMinuteParser.test.ts`
- Create: `watch-stock/test/codeUtils.test.ts`

**Interfaces:**
- Consumes: 无（纯函数，零依赖）。
- Produces（后续任务使用的精确签名）：
  - `model/StockQuote.ts`: `export interface StockQuote { code: string; name: string; price: number; prevClose: number; change: number; changePct: number; high: number; low: number }`
  - `model/MinuteData.ts`: `export interface MinutePoint { time: string; price: number }` 与 `export interface MinuteData { points: MinutePoint[]; prevClose: number; current: number; date: string }`
  - `data/codeUtils.ts`: `normalizeCode(input: string): string`、`isValidCode(code: string): boolean`、`inferPrefix(digits: string): string`
  - `data/parse/tencentQuoteParser.ts`: `parseTencentQuote(text: string): StockQuote[]`
  - `data/parse/eastmoneyQuoteParser.ts`: `toEastmoneySecId(code: string): string`、`parseEastmoneyQuote(jsonText: string, originalCodes: string[]): StockQuote[]`
  - `data/parse/tencentMinuteParser.ts`: `parseTencentMinute(jsonText: string, code: string): MinuteData`

- [ ] **Step 1: 写模型文件**

`watch-stock/entry/src/main/ets/model/StockQuote.ts`：
```typescript
export interface StockQuote {
  code: string;
  name: string;
  price: number;
  prevClose: number;
  change: number;
  changePct: number;
  high: number;
  low: number;
}
```

`watch-stock/entry/src/main/ets/model/MinuteData.ts`：
```typescript
export interface MinutePoint {
  time: string;
  price: number;
}

export interface MinuteData {
  points: MinutePoint[];
  prevClose: number;
  current: number;
  date: string;
}
```

- [ ] **Step 2: 写代码工具（纯函数）**

`watch-stock/entry/src/main/ets/data/codeUtils.ts`：
```typescript
export function inferPrefix(digits: string): string {
  if (digits.startsWith('6')) {
    return 'sh';
  }
  if (digits.startsWith('0') || digits.startsWith('3')) {
    return 'sz';
  }
  if (digits.startsWith('4') || digits.startsWith('8') || digits.startsWith('92')) {
    return 'bj';
  }
  return 'sh';
}

export function normalizeCode(input: string): string {
  let c: string = input.trim().toLowerCase().replace(/[. ]/g, '');
  if (/^(sh|sz|bj)\d{6}$/.test(c)) {
    return c;
  }
  const digits: string = c.replace(/\D/g, '');
  return `${inferPrefix(digits)}${digits}`;
}

export function isValidCode(code: string): boolean {
  return /^(sh|sz|bj)\d{6}$/.test(code);
}
```

- [ ] **Step 3: 写三个解析器（纯函数）**

`watch-stock/entry/src/main/ets/data/parse/tencentQuoteParser.ts`（腾讯 `v_sh600519="...";` 文本，`~` 分隔；`code` 取正则捕获组 `sh600519` 原文）：
```typescript
import type { StockQuote } from '../../model/StockQuote';

export function parseTencentQuote(text: string): StockQuote[] {
  const result: StockQuote[] = [];
  if (text === '') {
    return result;
  }
  const re = /v_(\w+)="([^"]*)"/g;
  let m: RegExpExecArray | null = re.exec(text);
  while (m !== null) {
    const fields: string[] = m[2].split('~');
    if (fields.length > 34) {
      result.push({
        code: m[1],
        name: fields[1],
        price: Number(fields[3]),
        prevClose: Number(fields[4]),
        change: Number(fields[31]),
        changePct: Number(fields[32]),
        high: Number(fields[33]),
        low: Number(fields[34])
      });
    }
    m = re.exec(text);
  }
  return result;
}
```

`watch-stock/entry/src/main/ets/data/parse/eastmoneyQuoteParser.ts`（东方财富 UTF-8 JSON；用 `originalCodes` 把 `f12` 六位代码精确映射回 `sh600519` 完整代码）：
```typescript
import type { StockQuote } from '../../model/StockQuote';

export function toEastmoneySecId(code: string): string {
  const c: string = code.trim().toLowerCase();
  const digits: string = c.replace(/\D/g, '');
  if (c.startsWith('sh')) {
    return `1.${digits}`;
  }
  if (c.startsWith('bj')) {
    return `2.${digits}`;
  }
  return `0.${digits}`;
}

interface EastmoneyDiff {
  f2: string | number;
  f3: string | number;
  f4: string | number;
  f12: string;
  f14: string;
  f15: string | number;
  f16: string | number;
  f17: string | number;
  f18: string | number;
}

interface EastmoneyResponse {
  data?: {
    diff?: EastmoneyDiff[];
  };
}

function toNumber(v: string | number): number {
  const n: number = Number(v);
  return Number.isFinite(n) ? n : 0;
}

function inferMarketCode(digits: string): string {
  if (digits.startsWith('6')) {
    return `sh${digits}`;
  }
  if (digits.startsWith('0') || digits.startsWith('3')) {
    return `sz${digits}`;
  }
  if (digits.startsWith('4') || digits.startsWith('8') || digits.startsWith('92')) {
    return `bj${digits}`;
  }
  return `sh${digits}`;
}

export function parseEastmoneyQuote(jsonText: string, originalCodes: string[]): StockQuote[] {
  const result: StockQuote[] = [];
  if (jsonText === '') {
    return result;
  }
  const codeByDigits = new Map<string, string>();
  for (const c of originalCodes) {
    codeByDigits.set(c.replace(/\D/g, ''), c);
  }
  const parsed = JSON.parse(jsonText) as EastmoneyResponse;
  const diff = parsed?.data?.diff;
  if (diff === undefined) {
    return result;
  }
  for (const item of diff) {
    const digits: string = String(item.f12);
    const code: string = codeByDigits.get(digits) ?? inferMarketCode(digits);
    result.push({
      code: code,
      name: item.f14,
      price: toNumber(item.f2),
      prevClose: toNumber(item.f18),
      change: toNumber(item.f4),
      changePct: toNumber(item.f3),
      high: toNumber(item.f15),
      low: toNumber(item.f16)
    });
  }
  return result;
}
```

`watch-stock/entry/src/main/ets/data/parse/tencentMinuteParser.ts`（腾讯分时 JSON：`data[code].data.data` 为 `"HHMM price"` 数组，`data[code].qt[code]` 为行情 `~` 数组，`[3]` 现价、`[4]` 昨收）：
```typescript
import type { MinuteData, MinutePoint } from '../../model/MinuteData';

interface MinuteEntryData {
  date?: string;
  data?: string[];
}

interface MinuteEntry {
  data?: MinuteEntryData;
  qt?: Record<string, string[]>;
}

interface MinuteResponse {
  code?: number;
  data?: Record<string, MinuteEntry>;
}

function num(v: string): number {
  const n: number = Number(v);
  return Number.isFinite(n) ? n : 0;
}

export function parseTencentMinute(jsonText: string, code: string): MinuteData {
  const points: MinutePoint[] = [];
  let prevClose: number = 0;
  let current: number = 0;
  let date: string = '';
  if (jsonText === '') {
    return { points, prevClose, current, date };
  }
  const parsed = JSON.parse(jsonText) as MinuteResponse;
  const entry = parsed?.data?.[code];
  const raw = entry?.data?.data ?? [];
  for (const line of raw) {
    const parts: string[] = line.split(' ');
    if (parts.length >= 2) {
      const price: number = num(parts[1]);
      if (Number.isFinite(price)) {
        points.push({ time: parts[0], price: price });
      }
    }
  }
  const qtArr: string[] = entry?.qt?.[code] ?? [];
  if (qtArr.length > 4) {
    prevClose = num(qtArr[4]);
  }
  if (qtArr.length > 3) {
    current = num(qtArr[3]);
  }
  if (current === 0 && points.length > 0) {
    current = points[points.length - 1].price;
  }
  date = entry?.data?.date ?? '';
  return { points, prevClose, current, date };
}
```

- [ ] **Step 4: 写解析层单测（先测，先跑红）**

`watch-stock/test/codeUtils.test.ts`：
```typescript
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalizeCode, isValidCode, inferPrefix } from '../entry/src/main/ets/data/codeUtils.ts';

test('normalizeCode: full code unchanged', () => {
  assert.equal(normalizeCode('sh600519'), 'sh600519');
  assert.equal(normalizeCode('sz000001'), 'sz000001');
});

test('normalizeCode: uppercase and separators cleaned', () => {
  assert.equal(normalizeCode('SH600519'), 'sh600519');
  assert.equal(normalizeCode('  sh600519 '), 'sh600519');
  assert.equal(normalizeCode('600519.SH'), 'sh600519');
});

test('normalizeCode: bare digits infer exchange by first digit', () => {
  assert.equal(normalizeCode('600519'), 'sh600519');
  assert.equal(normalizeCode('000001'), 'sz000001');
  assert.equal(normalizeCode('300750'), 'sz300750');
  assert.equal(normalizeCode('688981'), 'sh688981');
});

test('inferPrefix: exchange rules', () => {
  assert.equal(inferPrefix('600519'), 'sh');
  assert.equal(inferPrefix('000001'), 'sz');
  assert.equal(inferPrefix('300750'), 'sz');
  assert.equal(inferPrefix('920001'), 'bj');
});

test('isValidCode: only sh/sz/bj + 6 digits', () => {
  assert.equal(isValidCode('sh600519'), true);
  assert.equal(isValidCode('sz000001'), true);
  assert.equal(isValidCode('bj920001'), true);
  assert.equal(isValidCode('600519'), false);
  assert.equal(isValidCode('sh60051'), false);
  assert.equal(isValidCode('sh6005190'), false);
  assert.equal(isValidCode('xy600519'), false);
});
```

`watch-stock/test/tencentQuoteParser.test.ts`：
```typescript
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseTencentQuote } from '../entry/src/main/ets/data/parse/tencentQuoteParser.ts';

function makeTencentLine(code: string, name: string, price: string, prev: string, open: string,
  high: string, low: string, change: string, changePct: string): string {
  const f: string[] = new Array(35).fill('');
  f[1] = name;
  f[2] = code;
  f[3] = price;
  f[4] = prev;
  f[5] = open;
  f[31] = change;
  f[32] = changePct;
  f[33] = high;
  f[34] = low;
  return `v_sh${code}="${f.join('~')}";`;
}

test('parse tencent quote line', () => {
  const text = makeTencentLine('600519', '贵州茅台', '1700.00', '1680.00', '1690.00', '1710.00', '1670.00', '20.00', '1.19');
  const q = parseTencentQuote(text)[0];
  assert.equal(q.code, 'sh600519');
  assert.equal(q.name, '贵州茅台');
  assert.equal(q.price, 1700.00);
  assert.equal(q.prevClose, 1680.00);
  assert.equal(q.change, 20.00);
  assert.equal(q.changePct, 1.19);
  assert.equal(q.high, 1710.00);
  assert.equal(q.low, 1670.00);
});

test('parse multiple lines', () => {
  const text = makeTencentLine('600519', '贵州茅台', '1700.00', '1680.00', '1690.00', '1710.00', '1670.00', '20.00', '1.19')
    + '\n' + makeTencentLine('000001', '平安银行', '10.50', '10.55', '10.55', '10.60', '10.40', '-0.05', '-0.47');
  const quotes = parseTencentQuote(text);
  assert.equal(quotes.length, 2);
  assert.equal(quotes[1].code, 'sz000001');
  assert.equal(quotes[1].changePct, -0.47);
});

test('empty input returns empty array', () => {
  assert.equal(parseTencentQuote('').length, 0);
});
```

`watch-stock/test/eastmoneyQuoteParser.test.ts`：
```typescript
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseEastmoneyQuote, toEastmoneySecId } from '../entry/src/main/ets/data/parse/eastmoneyQuoteParser.ts';

const SAMPLE = '{"rc":0,"data":{"total":2,"diff":[' +
  '{"f12":"600519","f14":"贵州茅台","f2":1700.0,"f3":1.19,"f4":20.0,"f15":1710.0,"f16":1670.0,"f17":1690.0,"f18":1680.0},' +
  '{"f12":"000001","f14":"平安银行","f2":10.5,"f3":-0.47,"f4":-0.05,"f15":10.6,"f16":10.4,"f17":10.55,"f18":10.55}' +
  ']}}';

test('parse eastmoney quote maps f12 back to original codes', () => {
  const quotes = parseEastmoneyQuote(SAMPLE, ['sh600519', 'sz000001']);
  assert.equal(quotes.length, 2);
  assert.equal(quotes[0].code, 'sh600519');
  assert.equal(quotes[0].name, '贵州茅台');
  assert.equal(quotes[0].price, 1700.0);
  assert.equal(quotes[0].changePct, 1.19);
  assert.equal(quotes[0].prevClose, 1680.0);
  assert.equal(quotes[1].code, 'sz000001');
  assert.equal(quotes[1].changePct, -0.47);
});

test('suspended stock with "-" values coerces to 0', () => {
  const text = '{"data":{"diff":[{"f12":"600000","f14":"浦发银行","f2":"-","f3":"-","f4":"-","f15":"-","f16":"-","f17":"-","f18":10.0}]}}';
  const quotes = parseEastmoneyQuote(text, ['sh600000']);
  assert.equal(quotes.length, 1);
  assert.equal(quotes[0].price, 0);
  assert.equal(quotes[0].prevClose, 10.0);
});

test('empty or empty-diff input returns empty array', () => {
  assert.equal(parseEastmoneyQuote('', ['sh600519']).length, 0);
  assert.equal(parseEastmoneyQuote('{"data":{}}', ['sh600519']).length, 0);
});

test('toEastmoneySecId mapping', () => {
  assert.equal(toEastmoneySecId('sh600519'), '1.600519');
  assert.equal(toEastmoneySecId('sz000001'), '0.000001');
  assert.equal(toEastmoneySecId('bj920001'), '2.920001');
});
```

`watch-stock/test/tencentMinuteParser.test.ts`：
```typescript
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseTencentMinute } from '../entry/src/main/ets/data/parse/tencentMinuteParser.ts';

const SAMPLE = '{"code":0,"msg":"","data":{"sh600519":{' +
  '"data":{"date":"20260824","data":["0930 1698.00","0931 1699.50","1000 1700.00","1500 1700.00"]},' +
  '"qt":{"sh600519":["1~贵州茅台~600519~1700.00~1680.00~1690.00~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~x~20.00~1.19~1710.00~1670.00"]}' +
  '}}}';

test('parse tencent minute points and meta', () => {
  const data = parseTencentMinute(SAMPLE, 'sh600519');
  assert.equal(data.points.length, 4);
  assert.equal(data.points[0].time, '0930');
  assert.equal(data.points[0].price, 1698.00);
  assert.equal(data.points[3].price, 1700.00);
  assert.equal(data.prevClose, 1680.00);
  assert.equal(data.current, 1700.00);
  assert.equal(data.date, '20260824');
});

test('empty input returns empty data', () => {
  const data = parseTencentMinute('', 'sh600519');
  assert.equal(data.points.length, 0);
  assert.equal(data.prevClose, 0);
});
```

- [ ] **Step 5: 运行单测，确认全绿**

```bash
cd /d/Workspace/Project/cs-interview/watch-stock && node --test test/codeUtils.test.ts test/tencentQuoteParser.test.ts test/eastmoneyQuoteParser.test.ts test/tencentMinuteParser.test.ts
```
Expected: `tests 14`, `pass 14`, `fail 0`（codeUtils 5 + tencentQuote 3 + eastmoney 4 + minute 2）。

- [ ] **Step 6: 提交**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "feat(watch-stock): pure model and quote/minute parsers with node tests"
```

---

### Task 3: 通用工具（配色规则 + 格式化，Node 可单测）

**Files:**
- Create: `watch-stock/entry/src/main/ets/common/Colors.ts`
- Create: `watch-stock/entry/src/main/ets/common/Format.ts`
- Create: `watch-stock/test/colorsFormat.test.ts`

**Interfaces:**
- Consumes: `model/StockQuote.ts` 的 `StockQuote`（`import type`）。
- Produces（后续任务使用的精确签名）：
  - `common/Colors.ts`: `export const Colors = { UP: '#F5222D', DOWN: '#00B42A', FLAT: '#9E9E9E', TEXT_MAIN: '#FFFFFF', TEXT_SUB: '#AAAAAA' }`（`Record<string, string>` 常量对象）+ `export function quoteColor(quote: StockQuote): string`（返回十六进制颜色串）
  - `common/Format.ts`: `formatPrice(price: number): string`、`formatChangePct(pct: number): string`、`formatChange(change: number): string`

- [ ] **Step 1: 写 Colors（含配色函数，纯函数）**

`watch-stock/entry/src/main/ets/common/Colors.ts`：
```typescript
import type { StockQuote } from '../model/StockQuote';

export const Colors: Record<string, string> = {
  UP: '#F5222D',
  DOWN: '#00B42A',
  FLAT: '#9E9E9E',
  TEXT_MAIN: '#FFFFFF',
  TEXT_SUB: '#AAAAAA'
};

export function quoteColor(quote: StockQuote): string {
  if (quote.changePct > 0) {
    return Colors.UP;
  }
  if (quote.changePct < 0) {
    return Colors.DOWN;
  }
  return Colors.FLAT;
}
```

- [ ] **Step 2: 写 Format（纯函数）**

`watch-stock/entry/src/main/ets/common/Format.ts`：
```typescript
export function formatPrice(price: number): string {
  if (!Number.isFinite(price) || price <= 0) {
    return '--';
  }
  return price.toFixed(2);
}

export function formatChangePct(pct: number): string {
  if (!Number.isFinite(pct)) {
    return '--';
  }
  const sign: string = pct > 0 ? '+' : '';
  return `${sign}${pct.toFixed(2)}%`;
}

export function formatChange(change: number): string {
  if (!Number.isFinite(change)) {
    return '--';
  }
  const sign: string = change > 0 ? '+' : '';
  return `${sign}${change.toFixed(2)}`;
}
```

- [ ] **Step 3: 写单测**

`watch-stock/test/colorsFormat.test.ts`：
```typescript
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { Colors, quoteColor } from '../entry/src/main/ets/common/Colors.ts';
import { formatPrice, formatChangePct, formatChange } from '../entry/src/main/ets/common/Format.ts';
import type { StockQuote } from '../entry/src/main/ets/model/StockQuote.ts';

function makeQuote(changePct: number): StockQuote {
  return {
    code: 'sh600519', name: 'x', price: 10, prevClose: 10,
    change: 0, changePct: changePct, high: 10, low: 10
  };
}

test('Colors constants', () => {
  assert.equal(Colors.UP, '#F5222D');
  assert.equal(Colors.DOWN, '#00B42A');
  assert.equal(Colors.FLAT, '#9E9E9E');
});

test('quoteColor: up red / down green / flat gray', () => {
  assert.equal(quoteColor(makeQuote(1.5)), Colors.UP);
  assert.equal(quoteColor(makeQuote(-0.5)), Colors.DOWN);
  assert.equal(quoteColor(makeQuote(0)), Colors.FLAT);
});

test('formatPrice', () => {
  assert.equal(formatPrice(1700), '1700.00');
  assert.equal(formatPrice(0), '--');
  assert.equal(formatPrice(NaN), '--');
});

test('formatChangePct', () => {
  assert.equal(formatChangePct(1.19), '+1.19%');
  assert.equal(formatChangePct(-0.47), '-0.47%');
  assert.equal(formatChangePct(0), '0.00%');
});

test('formatChange', () => {
  assert.equal(formatChange(20), '+20.00');
  assert.equal(formatChange(-5), '-5.00');
});
```

- [ ] **Step 4: 运行单测**

```bash
cd /d/Workspace/Project/cs-interview/watch-stock && node --test test/colorsFormat.test.ts
```
Expected: `pass 5`, `fail 0`（Colors 1 + quoteColor 1 + formatPrice 1 + formatChangePct 1 + formatChange 1）。注意测试里 `import type ... from '...StockQuote.ts'` 带 `.ts` 扩展名（type-only，Node 擦除后不解析）。

- [ ] **Step 5: 提交**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "feat(watch-stock): colors and formatting helpers with tests"
```

---

### Task 4: StockApi 网络层

**Files:**
- Create: `watch-stock/entry/src/main/ets/data/StockApi.ts`

**Interfaces:**
- Consumes: `model/StockQuote.ts`、`model/MinuteData.ts`（`import type`）；`data/parse/eastmoneyQuoteParser.ts` 的 `toEastmoneySecId` / `parseEastmoneyQuote`；`data/parse/tencentMinuteParser.ts` 的 `parseTencentMinute`。
- Produces:
  - `class StockApi`：`static fetchQuotes(codes: string[]): Promise<StockQuote[]>`、`static fetchMinute(code: string): Promise<MinuteData>`
- 说明：本文件 import `@kit.NetworkKit`，**不在本环境单测**（无法运行 HarmonyOS SDK），正确性通过本任务代码审查 + Task 9 的 DevEco 构建/真机验证兜底。

- [ ] **Step 1: 写 StockApi**

`watch-stock/entry/src/main/ets/data/StockApi.ts`：
```typescript
import { http } from '@kit.NetworkKit';
import type { StockQuote } from '../model/StockQuote';
import type { MinuteData } from '../model/MinuteData';
import { toEastmoneySecId, parseEastmoneyQuote } from './parse/eastmoneyQuoteParser';
import { parseTencentMinute } from './parse/tencentMinuteParser';

const TIMEOUT_MS: number = 10000;
const QUOTE_FIELDS: string = 'f2,f3,f4,f12,f14,f15,f16,f17,f18';

export class StockApi {
  static async fetchQuotes(codes: string[]): Promise<StockQuote[]> {
    if (codes.length === 0) {
      return [];
    }
    const secids: string[] = codes.map((c: string) => toEastmoneySecId(c));
    const url: string =
      `https://push2.eastmoney.com/api/qt/ulist.np/get` +
      `?secids=${secids.join(',')}&fields=${QUOTE_FIELDS}` +
      `&fltt=2&invt=2&pn=1&pz=50&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281`;
    const text: string = await StockApi.getText(url);
    return parseEastmoneyQuote(text, codes);
  }

  static async fetchMinute(code: string): Promise<MinuteData> {
    const url: string = `https://web.ifzq.gtimg.cn/appstock/app/minute/query?code=${code}`;
    const text: string = await StockApi.getText(url);
    return parseTencentMinute(text, code);
  }

  private static async getText(url: string): Promise<string> {
    const httpRequest = http.createHttp();
    try {
      const response = await httpRequest.request(url, {
        method: http.RequestMethod.GET,
        connectTimeout: TIMEOUT_MS,
        readTimeout: TIMEOUT_MS,
        header: {
          'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 Chrome/120.0 Mobile Safari/537.36'
        }
      });
      if (response.responseCode !== 200) {
        throw new Error(`HTTP ${response.responseCode}`);
      }
      return response.result as string;
    } finally {
      httpRequest.destroy();
    }
  }
}
```

- [ ] **Step 2: 代码审查（对照 Global Constraints）**

人工核对以下各项（本环境无 ArkTS 编译器，作为提交前检查）：
1. 无 `any`，全部显式类型；`response.result as string` 为 HarmonyOS 官方文档惯用写法。
2. 只在 `getText` 内使用 `@kit.NetworkKit`，解析函数全部来自 Task 2 纯解析器。
3. 超时兜底（connect/read 各 10s），非 200 抛错，`finally` 中 `destroy()`。
4. `fetchQuotes` 空列表直接返回空数组，避免请求无 secid。

- [ ] **Step 3: 提交**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "feat(watch-stock): stock api http layer for quotes and minute"
```

---

### Task 5: StockRepository（自选清单 + 持久化 + 聚合）

**Files:**
- Create: `watch-stock/entry/src/main/ets/data/StockRepository.ts`

**Interfaces:**
- Consumes: `@kit.ArkData` 的 `preferences`、`@kit.AbilityKit` 的 `common`；`data/StockApi.ts` 的 `StockApi`；`data/codeUtils.ts` 的 `normalizeCode` / `isValidCode`；`model/StockQuote.ts`（`import type`）。
- Produces（后续页面使用的精确签名）：
  - `class StockRepository`（单例 `getInstance()`）：`async init(context: common.UIAbilityContext): Promise<void>`、`getCodes(): string[]`、`getQuotes(): StockQuote[]`、`isLoading(): boolean`、`getLastError(): string`、`async refresh(): Promise<void>`、`async add(code: string): Promise<boolean>`、`async remove(code: string): Promise<void>`、`subscribe(fn: () => void): void`
- 说明：本文件 import HarmonyOS kit，**不在本环境单测**；逻辑由 Task 9 真机验证兜底。`normalizeCode` / `isValidCode` 已在 Task 2 单测覆盖。

- [ ] **Step 1: 写 StockRepository**

`watch-stock/entry/src/main/ets/data/StockRepository.ts`：
```typescript
import { preferences } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import type { StockQuote } from '../model/StockQuote';
import { StockApi } from './StockApi';
import { normalizeCode, isValidCode } from './codeUtils';

const STORE_NAME: string = 'watch_stock';
const KEY_WATCHLIST: string = 'watchlist';

export class StockRepository {
  private static instance: StockRepository = new StockRepository();

  static getInstance(): StockRepository {
    return StockRepository.instance;
  }

  private store: preferences.Preferences | undefined = undefined;
  private codes: string[] = [];
  private quotes: StockQuote[] = [];
  private loading: boolean = false;
  private lastError: string = '';
  private listeners: Array<() => void> = [];

  async init(context: common.UIAbilityContext): Promise<void> {
    this.store = await preferences.getPreferences(context, STORE_NAME);
    const raw: string = (await this.store.get(KEY_WATCHLIST, '[]')) as string;
    this.codes = this.safeParse(raw);
    await this.refresh();
  }

  private safeParse(raw: string): string[] {
    try {
      const arr = JSON.parse(raw) as string[];
      return Array.isArray(arr) ? arr.filter((c) => typeof c === 'string') : [];
    } catch (e) {
      return [];
    }
  }

  getCodes(): string[] {
    return this.codes;
  }

  getQuotes(): StockQuote[] {
    return this.quotes;
  }

  isLoading(): boolean {
    return this.loading;
  }

  getLastError(): string {
    return this.lastError;
  }

  async refresh(): Promise<void> {
    if (this.loading) {
      return;
    }
    this.loading = true;
    this.lastError = '';
    this.notify();
    try {
      const fetched: StockQuote[] = await StockApi.fetchQuotes(this.codes);
      const map = new Map<string, StockQuote>();
      for (const q of fetched) {
        map.set(q.code, q);
      }
      const ordered: StockQuote[] = [];
      for (const c of this.codes) {
        const q = map.get(c);
        if (q !== undefined) {
          ordered.push(q);
        }
      }
      this.quotes = ordered;
    } catch (e) {
      this.lastError = '行情加载失败，保留上次数据';
    } finally {
      this.loading = false;
      this.notify();
    }
  }

  async add(code: string): Promise<boolean> {
    const normalized: string = normalizeCode(code);
    if (!isValidCode(normalized)) {
      return false;
    }
    if (this.codes.includes(normalized)) {
      return false;
    }
    this.codes.push(normalized);
    await this.persist();
    await this.refresh();
    return true;
  }

  async remove(code: string): Promise<void> {
    this.codes = this.codes.filter((c: string) => c !== code);
    this.quotes = this.quotes.filter((q: StockQuote) => q.code !== code);
    await this.persist();
    this.notify();
  }

  private async persist(): Promise<void> {
    if (this.store !== undefined) {
      await this.store.put(KEY_WATCHLIST, JSON.stringify(this.codes));
      await this.store.flush();
    }
  }

  subscribe(fn: () => void): void {
    this.listeners.push(fn);
  }

  private notify(): void {
    for (const fn of this.listeners) {
      fn();
    }
  }
}
```

- [ ] **Step 2: 代码审查（对照 Global Constraints 与 Task 4 接口）**

人工核对：
1. `preferences.getPreferences(context, STORE_NAME)` 返回 `Promise<Preferences>`，与 `@kit.ArkData` API 12 一致。
2. `add` 先 `persist()` 再 `refresh()`，`remove` 同步过滤数组并 `notify()`，与 `isValidCode` / `normalizeCode` 语义一致（Task 2 已测）。
3. `refresh()` 在 `loading` 时直接返回，避免并发重复请求（30s 定时 + 手动刷新重叠时安全）。
4. 失败时保留上次 `quotes`，仅更新 `lastError`，符合 spec 第 5 节"不阻塞已缓存内容"。
5. `subscribe` 简单追加监听器；同一页面重复 `aboutToAppear` 会产生重复监听（通知幂等，无副作用）——v1 接受，避免过度设计。

- [ ] **Step 3: 提交**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "feat(watch-stock): stock repository with preferences persistence"
```

---

### Task 6: Index 列表页

**Files:**
- Create: `watch-stock/entry/src/main/ets/pages/Index.ets`

**Interfaces:**
- Consumes: `StockRepository.getInstance()`（Task 5）、`common/Colors.ts` 的 `Colors` / `quoteColor`、`common/Format.ts` 的 `formatPrice` / `formatChangePct`、`model/StockQuote.ts` 的 `StockQuote`（`import type`）、`@kit.ArkUI` 的 `router`、`@kit.AbilityKit` 的 `common`。
- Produces: 启动页；点击列表项 `router.pushUrl({ url: 'pages/Detail', params: { code, name } })`；点"编辑" `router.pushUrl({ url: 'pages/Edit' })`；`@State quotes/loading/error` 展示；30s 定时刷新。
- 验证说明：本文件为 `.ets`，**本环境无法编译**，以代码审查 + Task 9 DevEco 构建/真机验证为准。

- [ ] **Step 1: 写 Index.ets**

`watch-stock/entry/src/main/ets/pages/Index.ets`：
```typescript
import { router } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { StockRepository } from '../data/StockRepository';
import type { StockQuote } from '../model/StockQuote';
import { Colors, quoteColor } from '../common/Colors';
import { formatPrice, formatChangePct } from '../common/Format';

const REFRESH_MS: number = 30000;

@Entry
@Component
struct Index {
  @State quotes: StockQuote[] = [];
  @State loading: boolean = false;
  @State error: string = '';
  private repo: StockRepository = StockRepository.getInstance();
  private timerId: number = -1;

  aboutToAppear(): void {
    this.repo.subscribe(() => {
      this.quotes = this.repo.getQuotes();
      this.loading = this.repo.isLoading();
      this.error = this.repo.getLastError();
    });
    const ctx = getContext(this) as common.UIAbilityContext;
    this.repo.init(ctx);
    this.timerId = setInterval(() => {
      this.repo.refresh();
    }, REFRESH_MS);
  }

  aboutToDisappear(): void {
    if (this.timerId !== -1) {
      clearInterval(this.timerId);
      this.timerId = -1;
    }
  }

  private openDetail(q: StockQuote): void {
    router.pushUrl({ url: 'pages/Detail', params: { code: q.code, name: q.name } });
  }

  build() {
    Column() {
      Row() {
        Text('自选股')
          .fontSize(18)
          .fontColor(Colors.TEXT_MAIN)
          .fontWeight(FontWeight.Bold)
        Blank()
        Button('编辑')
          .fontSize(14)
          .height(30)
          .onClick(() => {
            router.pushUrl({ url: 'pages/Edit' });
          })
      }
      .width('100%')
      .padding({ left: 14, right: 14, top: 10, bottom: 4 })

      if (this.loading && this.quotes.length === 0) {
        Column() {
          LoadingProgress().width(40).height(40)
          Text('加载中...').fontSize(12).fontColor(Colors.TEXT_SUB)
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
      } else if (this.quotes.length === 0) {
        Column() {
          Text('暂无自选股').fontSize(15).fontColor(Colors.TEXT_MAIN)
          Text('点击"编辑"添加').fontSize(12).fontColor(Colors.TEXT_SUB)
          if (this.error.length > 0) {
            Text(this.error).fontSize(11).fontColor(Colors.TEXT_SUB)
          }
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
      } else {
        List({ space: 4 }) {
          ForEach(this.quotes, (q: StockQuote) => {
            ListItem() {
              Row() {
                Column() {
                  Text(q.name)
                    .fontSize(15)
                    .fontColor(Colors.TEXT_MAIN)
                    .maxLines(1)
                  Text(q.code.toUpperCase())
                    .fontSize(10)
                    .fontColor(Colors.TEXT_SUB)
                }
                .alignItems(HorizontalAlign.Start)
                .layoutWeight(1)

                Column() {
                  Text(formatPrice(q.price))
                    .fontSize(16)
                    .fontColor(quoteColor(q))
                  Text(formatChangePct(q.changePct))
                    .fontSize(11)
                    .fontColor(quoteColor(q))
                }
                .alignItems(HorizontalAlign.End)
              }
              .width('100%')
              .padding({ left: 14, right: 14, top: 10, bottom: 10 })
            }
            .onClick(() => {
              this.openDetail(q);
            })
          }, (q: StockQuote) => q.code)
        }
        .layoutWeight(1)
        .width('100%')
      }

      if (this.error.length > 0 && this.quotes.length > 0) {
        Text(`${this.error} · 点击重试`)
          .fontSize(10)
          .fontColor(Colors.TEXT_SUB)
          .onClick(() => {
            this.repo.refresh();
          })
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#000000')
  }
}
```

- [ ] **Step 2: 代码审查（ArkTS 合规检查）**

人工核对：
1. `@Entry @Component struct` 语法、`@State` 装饰、`build()` 返回单个根组件。
2. `getContext(this) as common.UIAbilityContext` 为官方惯用写法；`router` / `FontWeight` / `FlexAlign` / `HorizontalAlign` / `LoadingProgress` / `Blank` 均为 ArkUI 全局声明，无需 import。
3. `ForEach` 第二个参数为 key generator `(q) => q.code`。
4. 定时器在 `aboutToDisappear` 清理，避免泄漏。
5. 空态/加载态/错误态覆盖完整（spec 5 节错误处理）。

- [ ] **Step 3: 提交**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "feat(watch-stock): watchlist index page"
```

---

### Task 7: Detail 分时图页

**Files:**
- Create: `watch-stock/entry/src/main/ets/pages/Detail.ets`

**Interfaces:**
- Consumes: `StockApi.fetchMinute(code)`（Task 4）、`model/MinuteData.ts` 的 `MinuteData` / `MinutePoint`（`import type`）、`common/Colors.ts`、`common/Format.ts`、`@kit.ArkUI` 的 `router`。
- Produces: 详情页；头部名称/代码/现价/涨跌/涨跌幅，主体 Canvas 分时折线 + 昨收虚线基准；返回按钮 `router.back()`。
- 验证说明：`.ets`，本环境无法编译，以代码审查 + Task 9 兜底。

- [ ] **Step 1: 写 Detail.ets**

`watch-stock/entry/src/main/ets/pages/Detail.ets`：
```typescript
import { router } from '@kit.ArkUI';
import { StockApi } from '../data/StockApi';
import type { MinuteData } from '../model/MinuteData';
import { Colors, quoteColor } from '../common/Colors';
import { formatPrice, formatChangePct, formatChange } from '../common/Format';

@Entry
@Component
struct Detail {
  @State code: string = '';
  @State name: string = '';
  @State minute: MinuteData | null = null;
  @State loading: boolean = false;
  @State error: string = '';
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private ctx2d: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  aboutToAppear(): void {
    const params = router.getParams() as Record<string, string>;
    this.code = params?.code ?? '';
    this.name = params?.name ?? '';
    this.loadData();
  }

  async loadData(): Promise<void> {
    this.loading = true;
    this.error = '';
    try {
      const data: MinuteData = await StockApi.fetchMinute(this.code);
      this.minute = data;
    } catch (e) {
      this.error = '分时数据加载失败，点击重试';
    } finally {
      this.loading = false;
    }
  }

  private mapY(price: number, min: number, max: number, height: number, pad: number): number {
    const range: number = max - min;
    if (range <= 0) {
      return height / 2;
    }
    return pad + (1 - (price - min) / range) * (height - pad * 2);
  }

  private drawChart(): void {
    const data = this.minute;
    if (data === null || data.points.length < 2) {
      return;
    }
    const width: number = this.ctx2d.width;
    const height: number = this.ctx2d.height;
    if (width <= 0 || height <= 0) {
      return;
    }
    const points = data.points;
    let min: number = points[0].price;
    let max: number = points[0].price;
    for (const p of points) {
      if (p.price < min) {
        min = p.price;
      }
      if (p.price > max) {
        max = p.price;
      }
    }
    if (max === min) {
      max = min + 1;
      min = min - 1;
    }
    const pad: number = 8;
    const color: string = data.current >= data.prevClose ? Colors.UP : Colors.DOWN;

    this.ctx2d.clearRect(0, 0, width, height);

    // 昨收基准虚线
    const baselineY: number = this.mapY(data.prevClose, min, max, height, pad);
    this.ctx2d.strokeStyle = '#555555';
    this.ctx2d.lineWidth = 1;
    this.ctx2d.setLineDash([4, 4]);
    this.ctx2d.beginPath();
    this.ctx2d.moveTo(0, baselineY);
    this.ctx2d.lineTo(width, baselineY);
    this.ctx2d.stroke();
    this.ctx2d.setLineDash([]);

    // 分时折线
    this.ctx2d.strokeStyle = color;
    this.ctx2d.lineWidth = 2;
    this.ctx2d.beginPath();
    for (let i = 0; i < points.length; i++) {
      const x: number = pad + (i / (points.length - 1)) * (width - pad * 2);
      const y: number = this.mapY(points[i].price, min, max, height, pad);
      if (i === 0) {
        this.ctx2d.moveTo(x, y);
      } else {
        this.ctx2d.lineTo(x, y);
      }
    }
    this.ctx2d.stroke();

    // 日期角标
    if (data.date.length > 0) {
      this.ctx2d.fillStyle = Colors.TEXT_SUB;
      this.ctx2d.font = '10px sans-serif';
      this.ctx2d.fillText(data.date, pad, height - 6);
    }
  }

  build() {
    Column() {
      Row() {
        Column() {
          Text(this.name.length > 0 ? this.name : this.code.toUpperCase())
            .fontSize(16)
            .fontColor(Colors.TEXT_MAIN)
            .fontWeight(FontWeight.Bold)
          Text(this.code.toUpperCase())
            .fontSize(10)
            .fontColor(Colors.TEXT_SUB)
        }
        .alignItems(HorizontalAlign.Start)
        .layoutWeight(1)

        Button('返回')
          .fontSize(13)
          .height(28)
          .onClick(() => {
            router.back();
          })
      }
      .width('100%')
      .padding({ left: 14, right: 14, top: 10, bottom: 4 })

      if (this.minute !== null) {
        Column() {
          Row() {
            Text(formatPrice(this.minute.current))
              .fontSize(26)
              .fontColor(quoteColor({
                code: this.code, name: this.name, price: this.minute.current,
                prevClose: this.minute.prevClose, change: this.minute.current - this.minute.prevClose,
                changePct: this.minute.prevClose > 0 ? (this.minute.current - this.minute.prevClose) / this.minute.prevClose * 100 : 0,
                high: 0, low: 0
              }))
            Blank()
            Text(`${formatChangePct(this.minute.prevClose > 0 ? (this.minute.current - this.minute.prevClose) / this.minute.prevClose * 100 : 0)} ${formatChange(this.minute.current - this.minute.prevClose)}`)
              .fontSize(12)
              .fontColor(quoteColor({
                code: this.code, name: this.name, price: this.minute.current,
                prevClose: this.minute.prevClose, change: this.minute.current - this.minute.prevClose,
                changePct: this.minute.prevClose > 0 ? (this.minute.current - this.minute.prevClose) / this.minute.prevClose * 100 : 0,
                high: 0, low: 0
              }))
          }
          .width('100%')
          .padding({ left: 14, right: 14, top: 4, bottom: 4 })

          Canvas(this.ctx2d)
            .width('100%')
            .layoutWeight(1)
            .onReady(() => {
              this.drawChart();
            })
        }
        .layoutWeight(1)
        .width('100%')
      } else if (this.loading) {
        Column() {
          LoadingProgress().width(40).height(40)
          Text('加载中...').fontSize(12).fontColor(Colors.TEXT_SUB)
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
      } else {
        Column() {
          if (this.error.length > 0) {
            Text(this.error)
              .fontSize(12)
              .fontColor(Colors.TEXT_SUB)
              .onClick(() => {
                this.loadData();
              })
          }
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#000000')
  }
}
```

- [ ] **Step 2: 代码审查**

人工核对：
1. `RenderingContextSettings` / `CanvasRenderingContext2D` 为 ArkUI 全局类，无需 import；`ctx2d` 字段初始化顺序在 `settings` 之后。
2. `quoteColor(...)` 接收临时 `StockQuote` 字面量——字面量字段需与 `StockQuote` 完全一致（code/name/price/prevClose/change/changePct/high/low），避免类型不匹配。
3. `params?.code ?? ''` 可选链与空值合并为 ArkTS 支持语法。
4. Canvas `onReady` 触发 `drawChart()`；`ctx2d.width/height` 为布局后实际像素，`clearRect` 先清屏。
5. 涨跌计算 `(current - prevClose) / prevClose * 100` 统一在 UI 层，`prevClose <= 0` 时按 0 处理避免除零。
6. 分时为空/异常时显示错误态并可点击重试。

- [ ] **Step 3: 提交**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "feat(watch-stock): detail page with canvas minute chart"
```

---

### Task 8: Edit 增删页

**Files:**
- Create: `watch-stock/entry/src/main/ets/pages/Edit.ets`

**Interfaces:**
- Consumes: `StockRepository.getInstance()`（Task 5）、`data/codeUtils.ts` 的 `normalizeCode` / `isValidCode`、`common/Colors.ts`、`@kit.ArkUI` 的 `router`。
- Produces: 编辑页；顶部输入框添加（格式校验 + 提示）、热门预置列表快捷添加、当前自选删除；返回按钮。
- 验证说明：`.ets`，本环境无法编译，以代码审查 + Task 9 兜底。

- [ ] **Step 1: 写 Edit.ets**

`watch-stock/entry/src/main/ets/pages/Edit.ets`：
```typescript
import { router } from '@kit.ArkUI';
import { StockRepository } from '../data/StockRepository';
import { normalizeCode, isValidCode } from '../data/codeUtils';
import { Colors } from '../common/Colors';

const PRESET_CODES: string[] = [
  'sh600519', 'sh601318', 'sh600036', 'sh601899', 'sh600900',
  'sz000001', 'sz000858', 'sz300750', 'sz002594', 'sh688981'
];

@Entry
@Component
struct Edit {
  @State codes: string[] = [];
  @State input: string = '';
  @State tip: string = '';
  private repo: StockRepository = StockRepository.getInstance();

  aboutToAppear(): void {
    this.repo.subscribe(() => {
      this.codes = this.repo.getCodes();
    });
    this.codes = this.repo.getCodes();
  }

  private async doAdd(): Promise<void> {
    const code: string = normalizeCode(this.input);
    if (!isValidCode(code)) {
      this.tip = '格式应为 sh600519 或 6 位数字代码';
      return;
    }
    const ok: boolean = await this.repo.add(code);
    this.tip = ok ? `已添加 ${code.toUpperCase()}` : '已在自选中或无效';
    this.input = '';
  }

  build() {
    Column() {
      Row() {
        Text('编辑自选')
          .fontSize(16)
          .fontColor(Colors.TEXT_MAIN)
          .fontWeight(FontWeight.Bold)
        Blank()
        Button('返回')
          .fontSize(13)
          .height(28)
          .onClick(() => {
            router.back();
          })
      }
      .width('100%')
      .padding({ left: 14, right: 14, top: 10, bottom: 4 })

      Scroll() {
        Column() {
          Row() {
            TextInput({ placeholder: '输入代码，如 sh600519', text: this.input })
              .fontSize(13)
              .height(36)
              .layoutWeight(1)
              .onChange((v: string) => {
                this.input = v;
              })
            Button('添加')
              .fontSize(13)
              .height(36)
              .margin({ left: 8 })
              .onClick(() => {
                this.doAdd();
              })
          }
          .width('100%')

          if (this.tip.length > 0) {
            Text(this.tip)
              .fontSize(11)
              .fontColor(Colors.TEXT_SUB)
              .width('100%')
              .padding({ top: 4 })
          }

          Text('当前自选')
            .fontSize(12)
            .fontColor(Colors.TEXT_SUB)
            .width('100%')
            .padding({ top: 10, bottom: 2 })

          ForEach(this.codes, (c: string) => {
            Row() {
              Text(c.toUpperCase())
                .fontSize(13)
                .fontColor(Colors.TEXT_MAIN)
                .layoutWeight(1)
              Button('删除')
                .fontSize(11)
                .height(26)
                .fontColor(Colors.DOWN)
                .onClick(() => {
                  this.repo.remove(c);
                })
            }
            .width('100%')
            .padding({ top: 6, bottom: 6 })
          }, (c: string) => c)

          Text('热门添加')
            .fontSize(12)
            .fontColor(Colors.TEXT_SUB)
            .width('100%')
            .padding({ top: 10, bottom: 2 })

          ForEach(PRESET_CODES, (c: string) => {
            Row() {
              Text(c.toUpperCase())
                .fontSize(12)
                .fontColor(Colors.TEXT_MAIN)
                .layoutWeight(1)
              Button(this.codes.includes(c) ? '已添加' : '添加')
                .fontSize(11)
                .height(26)
                .enabled(!this.codes.includes(c))
                .onClick(() => {
                  this.repo.add(c);
                })
            }
            .width('100%')
            .padding({ top: 6, bottom: 6 })
          }, (c: string) => c)
        }
        .width('100%')
        .padding({ left: 14, right: 14 })
      }
      .layoutWeight(1)
      .width('100%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#000000')
  }
}
```

- [ ] **Step 2: 代码审查**

人工核对：
1. `TextInput({ placeholder, text })` 构造参数与 `onChange((v: string) => void)` 回调为 ArkUI 标准用法。
2. `Button('添加')` onClick 触发 async `doAdd()`，fire-and-forget 合法。
3. 预置 10 只覆盖 sh/sz（`sh600519` 茅台、`sh601318` 平安、`sh600036` 招行、`sh601899` 紫金、`sh600900` 长江电力、`sz000001` 平安银行、`sz000858` 五粮液、`sz300750` 宁德、`sz002594` 比亚迪、`sh688981` 中芯）。
4. 单 `Scroll` 承载输入 + 当前自选 + 预置，适配手表小屏纵向滚动。
5. `enable` 对已添加项禁用，避免重复添加；`remove`/`add` 都走 Task 5 持久化。

- [ ] **Step 3: 提交**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "feat(watch-stock): edit page for add/remove watchlist"
```

---

### Task 9: README + 全量测试 + DevEco 验证清单

**Files:**
- Create: `watch-stock/README.md`
- Modify（如需要）: `docs/career-plan/2026-07-java-backend-interview-prep.md` 之外不加改；仅在 `watch-stock/` 内收尾。

**Interfaces:**
- Consumes: 前 8 个任务的产物。
- Produces: 用户可在 DevEco Studio 5 中打开、构建、签名、装机并手工验证的完整工程与操作手册。

- [ ] **Step 1: 写 README.md**

`watch-stock/README.md`：
```markdown
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
```

- [ ] **Step 2: 全量跑单元测试**

```bash
cd /d/Workspace/Project/cs-interview/watch-stock && node --test test/*.test.ts
```
Expected: 全部 `pass`，`fail 0`。同时确认测试文件确实 import 了每个解析器（有真实断言，非空壳）。

- [ ] **Step 3: 端到端自检（本环境内能做的全部验证）**

```bash
cd /d/Workspace/Project/cs-interview && node -e "
const fs=require('fs');
// 1) 所有 json5 可解析
const files=['watch-stock/build-profile.json5','watch-stock/oh-package.json5','watch-stock/hvigor/hvigor-config.json5','watch-stock/AppScope/app.json5','watch-stock/AppScope/resources/base/element/string.json','watch-stock/entry/build-profile.json5','watch-stock/entry/oh-package.json5','watch-stock/entry/src/main/module.json5','watch-stock/entry/src/main/resources/base/element/string.json','watch-stock/entry/src/main/resources/base/element/color.json','watch-stock/entry/src/main/resources/base/profile/main_pages.json'];
for (const f of files) JSON.parse(fs.readFileSync(f,'utf8'));
console.log('json5 ok:', files.length);
// 2) 三页存在且在 main_pages 中声明
const pages=JSON.parse(fs.readFileSync('watch-stock/entry/src/main/resources/base/profile/main_pages.json','utf8')).src;
for (const p of pages) { const f='watch-stock/entry/src/main/ets/'+p+'.ets'; if(!fs.existsSync(f)) throw new Error('missing page '+f); }
console.log('pages ok:', pages.join(', '));
// 3) INTERNET 权限已声明
const mod=JSON.parse(fs.readFileSync('watch-stock/entry/src/main/module.json5','utf8'));
const perms=(mod.module.requestPermissions||[]).map(x=>x.name);
if(!perms.includes('ohos.permission.INTERNET')) throw new Error('missing INTERNET permission');
console.log('internet permission ok');
"
```
Expected: `json5 ok: 11`、`pages ok: pages/Index, pages/Detail, pages/Edit`、`internet permission ok`，无异常。

- [ ] **Step 4: 提交 README 与收尾**

```bash
cd /d/Workspace/Project/cs-interview && git add watch-stock && git commit -m "docs(watch-stock): readme with deveco build and verification checklist"
```

- [ ] **Step 5: 把 DevEco 手工验证交接给用户**

在最终交付说明中明确：本环境无法编译/安装 HarmonyOS 应用，完成以上代码与单测后，**必须**由用户在 DevEco Studio 5 中执行 README 的"构建与装机"步骤，并按真机验证清单逐项确认。若构建报错，把 DevEco 的错误日志贴回，按需修复。
