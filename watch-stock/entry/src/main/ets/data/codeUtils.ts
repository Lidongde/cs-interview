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
