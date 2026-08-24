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
