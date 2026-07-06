(() => {
  const card = document.querySelector('.exercise-card');
  // CatalogPlatform 是 $parent
  let vue = card.__vue__.$parent;
  const result = [];
  let depth = 0;
  while (vue && depth < 10) {
    const name = vue.$options.name || vue.$options._componentTag || 'anon';
    const methods = vue.$options.methods || {};
    const allMethods = Object.keys(methods);
    // 打印所有方法名
    result.push({depth, name, allMethods});
    // 重点看 startPractice, singleTagPaper, 以及任何含 route/push/navigate/exam/test 的
    for (const m of allMethods) {
      try {
        const src = methods[m].toString();
        if (/route|push|navigate|exam|\/test|singleTagPaper|startPractice|window\.location|href/i.test(src)) {
          result.push({depth, name, method: m, src: src.slice(0, 600)});
        }
      } catch(e) {}
    }
    vue = vue.$parent;
    depth++;
  }
  return JSON.stringify(result, null, 2);
})()
