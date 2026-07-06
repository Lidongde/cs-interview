(() => {
  const card = document.querySelector('.exercise-card');
  let vue = card.__vue__.$parent;
  const info = [];
  let depth = 0;
  while (vue && depth < 8) {
    const name = vue.$options.name || vue.$options._componentTag || 'anon';
    const methods = Object.keys(vue.$options.methods || {});
    // 找 change 事件监听（在父组件的 $options._parentListeners 或 props）
    const listeners = vue.$options._parentListeners ? Object.keys(vue.$options._parentListeners) : [];
    // 当前组件注册的事件监听
    const compListeners = vue.$listeners ? Object.keys(vue.$listeners) : [];
    // 找包含 practice/start/exam/jump/go/route/to/navigate 的方法
    const relevant = methods.filter(m => /practice|start|exam|jump|go|route|navigate|to|handle|change|click/i.test(m));
    info.push({depth, name, relevantMethods: relevant, listeners: compListeners});
    // 打印相关方法源码
    for (const m of relevant) {
      try {
        const src = vue.$options.methods[m].toString();
        if (/route|push|navigate|exam|practice|paper|test|url|href/i.test(src)) {
          info.push({depth, method: m, src: src.slice(0, 500)});
        }
      } catch(e) {}
    }
    vue = vue.$parent;
    depth++;
  }
  return JSON.stringify(info, null, 2);
})()
