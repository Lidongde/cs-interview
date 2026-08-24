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
