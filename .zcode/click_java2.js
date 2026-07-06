(() => {
  // 安装路由监听
  window.__urlChanges = [];
  const origPush = history.pushState;
  history.pushState = function() {
    window.__urlChanges.push({type: 'push', url: arguments[2]});
    return origPush.apply(this, arguments);
  };
  // 点击 Java 卡片
  const cards = document.querySelectorAll('.exercise-card');
  let target = null;
  for (const c of cards) {
    const v = c.__vue__;
    if (v && v.cardInfo && v.cardInfo.title === 'Java') { target = c; break; }
  }
  if (!target) return 'Java card not found. titles: ' + Array.from(cards).map(c => c.__vue__?.cardInfo?.title).filter(Boolean).join(',');
  target.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true, view: window}));
  return 'clicked Java, cardInfo: ' + JSON.stringify(target.__vue__.cardInfo);
})()
