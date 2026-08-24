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
