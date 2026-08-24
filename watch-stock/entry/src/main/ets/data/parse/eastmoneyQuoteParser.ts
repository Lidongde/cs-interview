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
