import { router } from '@kit.ArkUI';
import { StockRepository } from '../data/StockRepository';
import { normalizeCode, isValidCode } from '../data/codeUtils';
import { Colors } from '../common/Colors';

const PRESET_CODES: string[] = [
  'sh600519', 'sh601318', 'sh600036', 'sh601899', 'sh600900',
  'sz000001', 'sz000858', 'sz300750', 'sz002594', 'sh688981'
];

@Entry
@Component
struct Edit {
  @State codes: string[] = [];
  @State input: string = '';
  @State tip: string = '';
  private repo: StockRepository = StockRepository.getInstance();

  aboutToAppear(): void {
    this.repo.subscribe(() => {
      this.codes = this.repo.getCodes();
    });
    this.codes = this.repo.getCodes();
  }

  private async doAdd(): Promise<void> {
    const code: string = normalizeCode(this.input);
    if (!isValidCode(code)) {
      this.tip = '格式应为 sh600519 或 6 位数字代码';
      return;
    }
    const ok: boolean = await this.repo.add(code);
    this.tip = ok ? `已添加 ${code.toUpperCase()}` : '添加失败（已存在或保存失败）';
    this.input = '';
  }

  build() {
    Column() {
      Row() {
        Text('编辑自选')
          .fontSize(16)
          .fontColor(Colors.TEXT_MAIN)
          .fontWeight(FontWeight.Bold)
        Blank()
        Button('返回')
          .fontSize(13)
          .height(28)
          .onClick(() => {
            router.back();
          })
      }
      .width('100%')
      .padding({ left: 14, right: 14, top: 10, bottom: 4 })

      Scroll() {
        Column() {
          Row() {
            TextInput({ placeholder: '输入代码，如 sh600519', text: this.input })
              .fontSize(13)
              .height(36)
              .layoutWeight(1)
              .onChange((v: string) => {
                this.input = v;
              })
            Button('添加')
              .fontSize(13)
              .height(36)
              .margin({ left: 8 })
              .onClick(() => {
                this.doAdd();
              })
          }
          .width('100%')

          if (this.tip.length > 0) {
            Text(this.tip)
              .fontSize(11)
              .fontColor(Colors.TEXT_SUB)
              .width('100%')
              .padding({ top: 4 })
          }

          Text('当前自选')
            .fontSize(12)
            .fontColor(Colors.TEXT_SUB)
            .width('100%')
            .padding({ top: 10, bottom: 2 })

          ForEach(this.codes, (c: string) => {
            Row() {
              Text(c.toUpperCase())
                .fontSize(13)
                .fontColor(Colors.TEXT_MAIN)
                .layoutWeight(1)
              Button('删除')
                .fontSize(11)
                .height(26)
                .fontColor(Colors.DOWN)
                .onClick(() => {
                  this.repo.remove(c);
                })
            }
            .width('100%')
            .padding({ top: 6, bottom: 6 })
          }, (c: string) => c)

          Text('热门添加')
            .fontSize(12)
            .fontColor(Colors.TEXT_SUB)
            .width('100%')
            .padding({ top: 10, bottom: 2 })

          ForEach(PRESET_CODES, (c: string) => {
            Row() {
              Text(c.toUpperCase())
                .fontSize(12)
                .fontColor(Colors.TEXT_MAIN)
                .layoutWeight(1)
              Button(this.codes.includes(c) ? '已添加' : '添加')
                .fontSize(11)
                .height(26)
                .enabled(!this.codes.includes(c))
                .onClick(() => {
                  this.repo.add(c);
                })
            }
            .width('100%')
            .padding({ top: 6, bottom: 6 })
          }, (c: string) => c)
        }
        .width('100%')
        .padding({ left: 14, right: 14 })
      }
      .layoutWeight(1)
      .width('100%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#000000')
  }
}
