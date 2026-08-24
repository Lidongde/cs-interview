import { router } from '@kit.ArkUI';
import { StockApi } from '../data/StockApi';
import type { MinuteData } from '../model/MinuteData';
import { Colors, quoteColor } from '../common/Colors';
import { formatPrice, formatChangePct, formatChange } from '../common/Format';

@Entry
@Component
struct Detail {
  @State code: string = '';
  @State name: string = '';
  @State minute: MinuteData | null = null;
  @State loading: boolean = false;
  @State error: string = '';
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private ctx2d: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  aboutToAppear(): void {
    const params = router.getParams() as Record<string, string>;
    this.code = params?.code ?? '';
    this.name = params?.name ?? '';
    this.loadData();
  }

  async loadData(): Promise<void> {
    this.loading = true;
    this.error = '';
    try {
      const data: MinuteData = await StockApi.fetchMinute(this.code);
      this.minute = data;
    } catch (e) {
      this.error = '分时数据加载失败，点击重试';
    } finally {
      this.loading = false;
    }
  }

  private mapY(price: number, min: number, max: number, height: number, pad: number): number {
    const range: number = max - min;
    if (range <= 0) {
      return height / 2;
    }
    return pad + (1 - (price - min) / range) * (height - pad * 2);
  }

  private drawChart(): void {
    const data = this.minute;
    if (data === null || data.points.length < 2) {
      return;
    }
    const width: number = this.ctx2d.width;
    const height: number = this.ctx2d.height;
    if (width <= 0 || height <= 0) {
      return;
    }
    const points = data.points;
    let min: number = points[0].price;
    let max: number = points[0].price;
    for (const p of points) {
      if (p.price < min) {
        min = p.price;
      }
      if (p.price > max) {
        max = p.price;
      }
    }
    if (max === min) {
      max = min + 1;
      min = min - 1;
    }
    const pad: number = 8;
    const color: string = data.current >= data.prevClose ? Colors.UP : Colors.DOWN;

    this.ctx2d.clearRect(0, 0, width, height);

    // 昨收基准虚线
    const baselineY: number = this.mapY(data.prevClose, min, max, height, pad);
    this.ctx2d.strokeStyle = '#555555';
    this.ctx2d.lineWidth = 1;
    this.ctx2d.setLineDash([4, 4]);
    this.ctx2d.beginPath();
    this.ctx2d.moveTo(0, baselineY);
    this.ctx2d.lineTo(width, baselineY);
    this.ctx2d.stroke();
    this.ctx2d.setLineDash([]);

    // 分时折线
    this.ctx2d.strokeStyle = color;
    this.ctx2d.lineWidth = 2;
    this.ctx2d.beginPath();
    for (let i = 0; i < points.length; i++) {
      const x: number = pad + (i / (points.length - 1)) * (width - pad * 2);
      const y: number = this.mapY(points[i].price, min, max, height, pad);
      if (i === 0) {
        this.ctx2d.moveTo(x, y);
      } else {
        this.ctx2d.lineTo(x, y);
      }
    }
    this.ctx2d.stroke();

    // 日期角标
    if (data.date.length > 0) {
      this.ctx2d.fillStyle = Colors.TEXT_SUB;
      this.ctx2d.font = '10px sans-serif';
      this.ctx2d.fillText(data.date, pad, height - 6);
    }
  }

  build() {
    Column() {
      Row() {
        Column() {
          Text(this.name.length > 0 ? this.name : this.code.toUpperCase())
            .fontSize(16)
            .fontColor(Colors.TEXT_MAIN)
            .fontWeight(FontWeight.Bold)
          Text(this.code.toUpperCase())
            .fontSize(10)
            .fontColor(Colors.TEXT_SUB)
        }
        .alignItems(HorizontalAlign.Start)
        .layoutWeight(1)

        Button('返回')
          .fontSize(13)
          .height(28)
          .onClick(() => {
            router.back();
          })
      }
      .width('100%')
      .padding({ left: 14, right: 14, top: 10, bottom: 4 })

      if (this.minute !== null) {
        Column() {
          Row() {
            Text(formatPrice(this.minute.current))
              .fontSize(26)
              .fontColor(quoteColor({
                code: this.code, name: this.name, price: this.minute.current,
                prevClose: this.minute.prevClose, change: this.minute.current - this.minute.prevClose,
                changePct: this.minute.prevClose > 0 ? (this.minute.current - this.minute.prevClose) / this.minute.prevClose * 100 : 0,
                high: 0, low: 0
              }))
            Blank()
            Text(`${formatChangePct(this.minute.prevClose > 0 ? (this.minute.current - this.minute.prevClose) / this.minute.prevClose * 100 : 0)} ${formatChange(this.minute.current - this.minute.prevClose)}`)
              .fontSize(12)
              .fontColor(quoteColor({
                code: this.code, name: this.name, price: this.minute.current,
                prevClose: this.minute.prevClose, change: this.minute.current - this.minute.prevClose,
                changePct: this.minute.prevClose > 0 ? (this.minute.current - this.minute.prevClose) / this.minute.prevClose * 100 : 0,
                high: 0, low: 0
              }))
          }
          .width('100%')
          .padding({ left: 14, right: 14, top: 4, bottom: 4 })

          Canvas(this.ctx2d)
            .width('100%')
            .layoutWeight(1)
            .onReady(() => {
              this.drawChart();
            })
        }
        .layoutWeight(1)
        .width('100%')
      } else if (this.loading) {
        Column() {
          LoadingProgress().width(40).height(40)
          Text('加载中...').fontSize(12).fontColor(Colors.TEXT_SUB)
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
      } else {
        Column() {
          if (this.error.length > 0) {
            Text(this.error)
              .fontSize(12)
              .fontColor(Colors.TEXT_SUB)
              .onClick(() => {
                this.loadData();
              })
          }
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#000000')
  }
}
