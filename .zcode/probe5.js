(() => {
  // 查看题目列表区域
  const questionEls = document.querySelectorAll('[class*="question"], [class*="paper"], [class*="exam-item"]');
  const info = Array.from(questionEls).slice(0, 10).map(e => ({cls: e.className, text: e.innerText.slice(0, 100)}));
  // 查看是否有"推荐"
  const hasRecom = document.body.innerText.includes('推荐');
  // 查看页面主体文本前2000字
  const main = document.querySelector('main, .main, #app, .content') || document.body;
  const bodyText = main.innerText.slice(0, 1500);
  return JSON.stringify({url: location.href, hasRecom, questionEls: info, bodyText}, null, 2);
})()
