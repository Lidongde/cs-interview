#!/usr/bin/env node
/**
 * bilibili-search — 一键搜索 B站 视频
 *
 * 用法:
 *   node search.js <关键词> [页码]
 *
 * 示例:
 *   node search.js "宋红康 JVM"
 *   node search.js "Spring 注解驱动" 2
 *   node search.js "Redis 缓存穿透"
 *
 * 依赖: 无需额外安装，使用 Node.js 内置 https 模块
 */

const https = require('https');
const querystring = require('querystring');

const keyword = process.argv[2];
const page = parseInt(process.argv[3], 10) || 1;
const MAX_RETRIES = 3;

if (!keyword) {
  console.error('用法: node search.js <关键词> [页码]');
  console.error('示例: node search.js "宋红康 JVM"');
  process.exit(1);
}

const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36';

function apiGet(url, retries = MAX_RETRIES) {
  return new Promise((resolve, reject) => {
    const opts = {
      headers: {
        'User-Agent': UA,
        'Referer': 'https://www.bilibili.com/',
      },
      timeout: 15000,
    };
    https.get(url, opts, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        if (res.statusCode === 412 && retries > 0) {
          // Rate limited — wait and retry
          const delay = (MAX_RETRIES - retries + 1) * 2000;
          setTimeout(() => {
            apiGet(url, retries - 1).then(resolve, reject);
          }, delay);
        } else if (res.statusCode === 412) {
          reject(new Error('HTTP 412 — 请求被拦截（限流），请等待几秒后重试'));
        } else if (res.statusCode !== 200) {
          reject(new Error(`HTTP ${res.statusCode}`));
        } else {
          try {
            resolve(JSON.parse(data));
          } catch (e) {
            reject(new Error(`JSON 解析失败: ${e.message}`));
          }
        }
      });
    }).on('error', reject);
  });
}

function formatCount(n) {
  n = parseInt(n, 10);
  if (isNaN(n)) return '0';
  if (n >= 10000 && n < 100000000) return (n / 10000).toFixed(1).replace(/\.0$/, '') + '万';
  if (n >= 100000000) return (n / 100000000).toFixed(2).replace(/\.0+$/, '') + '亿';
  return String(n);
}

function stripHtml(s) {
  return s.replace(/<[^>]+>/g, '');
}

function formatDuration(d) {
  // "1087:45" or "53:39"
  if (!d) return '';
  const parts = d.split(':');
  if (parts.length === 2) return `${parts[0]}:${parts[1]}`;
  if (parts.length === 3) return `${parts[0]}h${parts[1]}m`;
  return d;
}

async function main() {
  const params = querystring.stringify({
    search_type: 'video',
    keyword,
    page,
  });

  const url = `https://api.bilibili.com/x/web-interface/search/type?${params}`;

  try {
    const data = await apiGet(url);

    if (data.code !== 0 || !data.data || !data.data.result) {
      console.log(`❌ 搜索失败: ${data.message || '未知错误'}`);
      process.exit(1);
    }

    const results = data.data.result;
    const totalResults = data.data.numResults || results.length;

    if (!results || results.length === 0) {
      console.log(`🔍 未找到 "${keyword}" 的相关视频`);
      process.exit(0);
    }

    console.log(`## 🔍 B站搜索: "${keyword}"`);
    console.log();
    console.log(`共 ${formatCount(totalResults)} 条结果，当前第 ${page} 页，显示前 ${results.length} 条`);
    console.log();
    console.log('| # | 标题 | UP主 | 播放量 | 弹幕 | 时长 | 发布日期 | 链接 |');
    console.log('|---|------|------|--------|------|------|---------|------|');

    results.forEach((v, i) => {
      const num = (page - 1) * 20 + i + 1;
      const title = stripHtml(v.title || '');
      const author = v.author || '未知';
      const play = formatCount(v.play);
      const danmaku = formatCount(v.video_review || 0);
      const dur = formatDuration(v.duration);
      const pubDate = v.pubdate ? new Date(v.pubdate * 1000).toISOString().split('T')[0] : '';
      const bvid = v.bvid || '';
      const link = bvid ? `https://www.bilibili.com/video/${bvid}` : (v.arcurl || '');

      // Truncate title if too long
      const displayTitle = title.length > 40 ? title.substring(0, 38) + '…' : title;

      console.log(`| ${num} | ${displayTitle} | ${author} | ${play} | ${danmaku} | ${dur} | ${pubDate} | [观看](${link}) |`);
    });

    console.log();
    console.log(`---`);
    console.log(`💡 提示: 查看更多结果请运行 \`node search.js "${keyword}" ${page + 1}\``);

  } catch (err) {
    console.error(`❌ 搜索出错: ${err.message}`);
    process.exit(1);
  }
}

main();