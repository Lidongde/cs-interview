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
