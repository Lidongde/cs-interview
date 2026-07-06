(() => {
  const title = document.title;
  const url = location.href;
  const text = document.body.innerText;
  const hasRecom = text.includes('推荐');
  const hasIntelligent = text.includes('智能');
  const recomEls = document.querySelectorAll('[class*="recommend"], [class*="Recommend"], [id*="recommend"]');
  const recomInfo = Array.from(recomEls).slice(0, 5).map(e => ({tag: e.tagName, cls: e.className, text: e.innerText.slice(0, 80)}));
  const tabs = document.querySelectorAll('[class*="tab"], [role="tab"]');
  const tabInfo = Array.from(tabs).slice(0, 15).map(e => ({cls: e.className, text: e.innerText.slice(0, 40)}));
  return JSON.stringify({title, url, hasRecom, hasIntelligent, recomInfo, tabInfo}, null, 2);
})()
