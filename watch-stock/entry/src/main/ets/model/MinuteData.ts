export interface MinutePoint {
  time: string;
  price: number;
}

export interface MinuteData {
  points: MinutePoint[];
  prevClose: number;
  current: number;
  date: string;
}
