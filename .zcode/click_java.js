(() => {
  // 找到 Java 卡片并点击
  const cards = document.querySelectorAll('.exercises-card-title');
  let javaCard = null;
  for (const c of cards) {
    if (c.innerText.trim() === 'Java') { javaCard = c; break; }
  }
  if (!javaCard) return 'Java card not found';
  // 点击整个卡片
  const card = javaCard.closest('[class*="card"]') || javaCard.parentElement.parentElement;
  card.click();
  return 'clicked Java card, url: ' + location.href;
})()
