(() => {
  // 找到 Java 分类项并点击
  const items = document.querySelectorAll('[class*="paper-item"], [class*="category"], [class*="tag-item"]');
  const info = Array.from(items).slice(0, 5).map(e => ({cls: e.className, text: e.innerText.slice(0, 40)}));
  // 找所有包含 Java 文字的元素
  const javaEls = Array.from(document.querySelectorAll('*')).filter(e => e.children.length === 0 && e.innerText === 'Java');
  const javaInfo = javaEls.slice(0, 5).map(e => ({tag: e.tagName, cls: e.className, parent: e.parentElement?.className}));
  return JSON.stringify({items: info, javaEls: javaInfo}, null, 2);
})()
