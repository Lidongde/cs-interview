(() => {
  // 查找所有按钮和可点击元素的文字
  const clickables = document.querySelectorAll('button, a, [role="button"], [class*="btn"]');
  const texts = Array.from(clickables).map(e => e.innerText.trim()).filter(t => t && t.length < 30);
  const unique = [...new Set(texts)];
  // 查找包含"练习/开始/做题/推荐"的元素
  const practiceEls = Array.from(document.querySelectorAll('*')).filter(e => e.children.length === 0 && /练习|开始|做题|推荐|立即|进入/.test(e.innerText)).map(e => ({tag: e.tagName, cls: e.className, text: e.innerText.slice(0, 40)}));
  return JSON.stringify({buttons: unique.slice(0, 30), practiceEls: practiceEls.slice(0, 15)}, null, 2);
})()
