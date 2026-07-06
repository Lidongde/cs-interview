(() => {
  // 查找弹窗/遮罩层
  const dialogs = document.querySelectorAll('.el-dialog, .el-dialog__wrapper, [class*="dialog"], [class*="modal"], [class*="mask"]');
  const info = Array.from(dialogs).filter(e => e.offsetParent !== null).map(e => ({
    tag: e.tagName,
    cls: e.className,
    text: e.innerText.slice(0, 100),
    visible: e.offsetParent !== null
  }));
  // 查找关闭按钮
  const closeBtns = document.querySelectorAll('.el-dialog__headerbtn, .close, [class*="close"], [aria-label*="close"]');
  const closeInfo = Array.from(closeBtns).slice(0, 10).map(e => ({cls: e.className, text: e.innerText.slice(0, 20)}));
  return JSON.stringify({dialogs: info, closeBtns: closeInfo}, null, 2);
})()
