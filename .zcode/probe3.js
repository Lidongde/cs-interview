(() => {
  // 查找所有标签链接，看 tagId 对应关系
  const links = document.querySelectorAll('a[href*="tagId"], a[href*="intelligent"]');
  const linkInfo = Array.from(links).slice(0, 30).map(a => ({href: a.href, text: a.innerText.slice(0, 30)}));
  // 当前页面所有带 tagId 的链接
  const allLinks = document.querySelectorAll('a');
  const tagLinks = Array.from(allLinks).filter(a => /tagId=\d+/.test(a.href)).map(a => ({href: a.href, text: a.innerText.slice(0, 30)}));
  return JSON.stringify({linkInfo: linkInfo.slice(0, 10), tagLinksCount: tagLinks.length, sampleTagLinks: tagLinks.slice(0, 20)}, null, 2);
})()
