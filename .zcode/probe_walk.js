(() => {
  const found = [];
  const visited = new Set();
  function walk(v, depth) {
    if (!v || visited.has(v) || depth > 12) return;
    visited.add(v);
    const methods = v.$options.methods || {};
    if (methods.startPractice || methods.singleTagPaper) {
      found.push({
        depth,
        name: v.$options.name || v.$options._componentTag || 'anon',
        hasStart: !!methods.startPractice,
        hasSingle: !!methods.singleTagPaper,
        startSrc: methods.startPractice ? methods.startPractice.toString().slice(0, 800) : null,
        singleSrc: methods.singleTagPaper ? methods.singleTagPaper.toString().slice(0, 800) : null
      });
    }
    const children = v.$children || [];
    for (const c of children) walk(c, depth + 1);
  }
  let app = document.querySelector('#app');
  let rootVue = app.__vue__;
  walk(rootVue, 0);
  return JSON.stringify(found, null, 2);
})()
