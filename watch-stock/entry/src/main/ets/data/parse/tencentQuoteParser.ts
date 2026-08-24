import type { StockQuote } from '../../model/StockQuote';

function num(v: string): number {
  const n: number = Number(v);
  return Number.isFinite(n) ? n : 0;
}

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
        price: num(fields[3]),
        prevClose: num(fields[4]),
        change: num(fields[31]),
        changePct: num(fields[32]),
        high: num(fields[33]),
        low: num(fields[34])
      });
    }
    m = re.exec(text);
  }
  return result;
}
