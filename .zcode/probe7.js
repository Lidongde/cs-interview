(() => {
  // 点击后页面是否出现新内容
  const allText = document.body.innerText;
  // 查找是否有题目相关的新元素
  const questionLike = document.querySelectorAll('[class*="question"], [class*="paper-item"], [class*="exercise-item"], [class*="test-"]');
  const info = Array.from(questionLike).slice(0, 10).map(e => ({cls: e.className, text: e.innerText.slice(0, 80)}));
  // 是否有"开始/做题/练习"按钮现在可见
  const btns = Array.from(document.querySelectorAll('button, [class*="btn"], [role="button"]')).filter(e => e.offsetParent !== null).map(e => e.innerText.trim()).filter(t => t && t.length < 25);
  // 查看 Java 卡片当前状态
  const javaCard = Array.from(document.querySelectorAll('.exercises-card-title')).find(e => e.innerText.trim() === 'Java');
  const javaParent = javaCard?.closest('[class*="card"]')?.className;
  return JSON.stringify({questionLike: info, visibleBtns: [...new Set(btns)].slice(0, 20), javaParentClass: javaParent}, null, 2);
})()
