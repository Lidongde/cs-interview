import { router } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { StockRepository } from '../data/StockRepository';
import type { StockQuote } from '../model/StockQuote';
import { Colors, quoteColor } from '../common/Colors';
import { formatPrice, formatChangePct } from '../common/Format';

const REFRESH_MS: number = 30000;

@Entry
@Component
struct Index {
  @State quotes: StockQuote[] = [];
  @State loading: boolean = false;
  @State error: string = '';
  private repo: StockRepository = StockRepository.getInstance();
  private timerId: number = -1;

  aboutToAppear(): void {
    this.repo.subscribe(() => {
      this.quotes = this.repo.getQuotes();
      this.loading = this.repo.isLoading();
      this.error = this.repo.getLastError();
    });
    const ctx = getContext(this) as common.UIAbilityContext;
    this.repo.init(ctx);
    this.timerId = setInterval(() => {
      this.repo.refresh();
    }, REFRESH_MS);
  }

  aboutToDisappear(): void {
    if (this.timerId !== -1) {
      clearInterval(this.timerId);
      this.timerId = -1;
    }
  }

  private openDetail(q: StockQuote): void {
    router.pushUrl({ url: 'pages/Detail', params: { code: q.code, name: q.name } });
  }

  build() {
    Column() {
      Row() {
        Text('自选股')
          .fontSize(18)
          .fontColor(Colors.TEXT_MAIN)
          .fontWeight(FontWeight.Bold)
        Blank()
        Button('编辑')
          .fontSize(14)
          .height(30)
          .onClick(() => {
            router.pushUrl({ url: 'pages/Edit' });
          })
      }
      .width('100%')
      .padding({ left: 14, right: 14, top: 10, bottom: 4 })

      if (this.loading && this.quotes.length === 0) {
        Column() {
          LoadingProgress().width(40).height(40)
          Text('加载中...').fontSize(12).fontColor(Colors.TEXT_SUB)
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
      } else if (this.quotes.length === 0) {
        Column() {
          Text('暂无自选股').fontSize(15).fontColor(Colors.TEXT_MAIN)
          Text('点击"编辑"添加').fontSize(12).fontColor(Colors.TEXT_SUB)
          if (this.error.length > 0) {
            Text(this.error).fontSize(11).fontColor(Colors.TEXT_SUB)
          }
        }
        .width('100%')
        .layoutWeight(1)
        .justifyContent(FlexAlign.Center)
      } else {
        List({ space: 4 }) {
          ForEach(this.quotes, (q: StockQuote) => {
            ListItem() {
              Row() {
                Column() {
                  Text(q.name)
                    .fontSize(15)
                    .fontColor(Colors.TEXT_MAIN)
                    .maxLines(1)
                  Text(q.code.toUpperCase())
                    .fontSize(10)
                    .fontColor(Colors.TEXT_SUB)
                }
                .alignItems(HorizontalAlign.Start)
                .layoutWeight(1)

                Column() {
                  Text(formatPrice(q.price))
                    .fontSize(16)
                    .fontColor(quoteColor(q))
                  Text(formatChangePct(q.changePct))
                    .fontSize(11)
                    .fontColor(quoteColor(q))
                }
                .alignItems(HorizontalAlign.End)
              }
              .width('100%')
              .padding({ left: 14, right: 14, top: 10, bottom: 10 })
            }
            .onClick(() => {
              this.openDetail(q);
            })
          }, (q: StockQuote) => q.code)
        }
        .layoutWeight(1)
        .width('100%')
      }

      if (this.error.length > 0 && this.quotes.length > 0) {
        Text(`${this.error} · 点击重试`)
          .fontSize(10)
          .fontColor(Colors.TEXT_SUB)
          .onClick(() => {
            this.repo.refresh();
          })
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#000000')
  }
}
