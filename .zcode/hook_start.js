(() => {
  const card = document.querySelector('.exercise-card');
  if (!card || !card.__vue__) return 'no vue';
  const indexComp = card.__vue__.$parent.$parent.$parent;
  // Hook startPractice: 包装它，记录调用和返回值
  const orig = indexComp.startPractice.bind(indexComp);
  window.__startPracticeCalls = [];
  indexComp.startPractice = function(...args) {
    window.__startPracticeCalls.push({args: JSON.stringify(args), time: Date.now()});
    // 同时 hook axios/fetch 在调用期间
    const result = orig.apply(this, args);
    if (result && typeof result.then === 'function') {
      result.then(r => window.__startPracticeCalls.push({resolved: JSON.stringify(r).slice(0, 500)}))
            .catch(e => window.__startPracticeCalls.push({error: e.message}));
    }
    return result;
  };
  // 同时检查 indexComp 上是否有 $router 或路由相关
  const hasRouter = !!indexComp.$router;
  const routes = hasRouter ? indexComp.$router.options.routes.map(r => r.path).slice(0, 30) : [];
  return JSON.stringify({hooked: true, hasRouter, routes}, null, 2);
})()
