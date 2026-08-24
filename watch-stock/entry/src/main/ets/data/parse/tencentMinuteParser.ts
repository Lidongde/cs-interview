import type { MinuteData, MinutePoint } from '../../model/MinuteData';

interface MinuteEntryData {
  date?: string;
  data?: string[];
}

interface MinuteEntry {
  data?: MinuteEntryData;
  qt?: Record<string, string[] | string>;
}

interface MinuteResponse {
  code?: number;
  data?: Record<string, MinuteEntry>;
}

function num(v: string): number {
  const n: number = Number(v);
  return Number.isFinite(n) ? n : 0;
}

export function parseTencentMinute(jsonText: string, code: string): MinuteData {
  const points: MinutePoint[] = [];
  let prevClose: number = 0;
  let current: number = 0;
  let date: string = '';
  if (jsonText === '') {
    return { points, prevClose, current, date };
  }
  const parsed = JSON.parse(jsonText) as MinuteResponse;
  const entry = parsed?.data?.[code];
  const raw = entry?.data?.data ?? [];
  for (const line of raw) {
    const parts: string[] = line.split(' ');
    if (parts.length >= 2) {
      const price: number = num(parts[1]);
      if (Number.isFinite(price)) {
        points.push({ time: parts[0], price: price });
      }
    }
  }
  const qtRaw: string[] | string | undefined = entry?.qt?.[code];
  let qtArr: string[] = [];
  if (Array.isArray(qtRaw)) {
    qtArr = qtRaw.length === 1 && qtRaw[0].includes('~') ? qtRaw[0].split('~') : qtRaw;
  } else if (typeof qtRaw === 'string') {
    qtArr = qtRaw.split('~');
  }
  if (qtArr.length > 4) {
    prevClose = num(qtArr[4]);
  }
  if (qtArr.length > 3) {
    current = num(qtArr[3]);
  }
  if (current === 0 && points.length > 0) {
    current = points[points.length - 1].price;
  }
  date = entry?.data?.date ?? '';
  return { points, prevClose, current, date };
}
