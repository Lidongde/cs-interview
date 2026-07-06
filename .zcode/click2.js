(() => {
  // 监听路由变化
  window.__urlChanges = [];
  const origPush = history.pushState;
  history.pushState = function() {
    window.__urlChanges.push({type: 'push', url: arguments[2]});
    return origPush.apply(this, arguments);
  };
  const origReplace = history.replaceState;
  history.replaceState = function() {
    window.__urlChanges.push({type: 'replace', url: arguments[2]});
    return origReplace.apply(this, arguments);
  };
  // 找到 Java 卡片并真正模拟点击
  const cards = document.querySelectorAll('.exercise-card');
  let javaCard = null;
  for (const c of cards) {
    if (c.innerText.includes('Java')) { javaCard = c; break; }
  }
  if (!javaCard) return 'no java card';
  // 模拟真实点击事件
  javaCard.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true, view: window}));
  return 'dispatched click on: ' + javaCard.className;
})()
