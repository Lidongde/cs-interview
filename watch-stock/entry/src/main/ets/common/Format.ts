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
