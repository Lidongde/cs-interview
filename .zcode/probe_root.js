(() => {
  // 找所有带 __vue__ 的元素
  const all = document.querySelectorAll('*');
  let vueEls = [];
  for (const e of all) {
    if (e.__vue__) vueEls.push(e);
    if (vueEls.length > 5) break;
  }
  const info = vueEls.map(e => ({tag: e.tagName, id: e.id, cls: (e.className||'').slice(0,50)}));
  // 从第一个 vue 元素向上找根
  let root = vueEls[0];
  if (!root) return 'no vue elements';
  let cur = root.__vue__;
  const chain = [];
  while (cur) {
    const methods = Object.keys(cur.$options.methods || {});
    const relevant = methods.filter(m => /practice|start|single|paper|exam|route|navigate/i.test(m));
    if (relevant.length) {
      chain.push({
        name: cur.$options.name || 'anon',
        relevant,
        startSrc: cur.$options.methods.startPractice ? cur.$options.methods.startPractice.toString().slice(0, 700) : null,
        singleSrc: cur.$options.methods.singleTagPaper ? cur.$options.methods.singleTagPaper.toString().slice(0, 700) : null
      });
    }
    cur = cur.$parent;
  }
  return JSON.stringify({vueEls: info, chain}, null, 2);
})()
