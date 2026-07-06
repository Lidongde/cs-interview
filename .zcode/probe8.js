(() => {
  // 详细查看 Java 卡片的完整结构
  const javaCard = Array.from(document.querySelectorAll('.exercises-card-title')).find(e => e.innerText.trim() === 'Java');
  if (!javaCard) return 'not found';
  // 向上找到卡片容器
  let card = javaCard;
  for (let i = 0; i < 5; i++) {
    card = card.parentElement;
    if (!card) break;
  }
  const cardHTML = card ? card.outerHTML.slice(0, 1500) : 'no card';
  // 查找卡片内的所有可点击子元素和链接
  const cardLinks = card ? Array.from(card.querySelectorAll('a, button, [role="button"]')).map(e => ({tag: e.tagName, href: e.href || '', text: e.innerText.slice(0, 30)})) : [];
  return JSON.stringify({cardHTML, cardLinks}, null, 2);
})()
