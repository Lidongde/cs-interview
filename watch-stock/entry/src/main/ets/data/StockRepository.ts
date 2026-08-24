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
