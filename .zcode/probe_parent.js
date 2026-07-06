(() => {
  const card = document.querySelector('.exercise-card');
  let vue = card.__vue__.$parent;
  const chain = [];
  let depth = 0;
  while (vue && depth < 6) {
    const methods = Object.keys(vue.$options.methods || {});
    const data = Object.keys(vue.$data || {});
    const name = vue.$options.name || vue.$options._componentTag || 'anon';
    // 找包含 change / click / jump / route 的方法
    const relevantMethods = methods.filter(m => /change|click|jump|route|go|nav|practice|start|exam/i.test(m));
    chain.push({name, relevantMethods, data: data.slice(0, 15)});
    // 如果有 change 方法，打印它的源码
    if (vue.$options.methods && vue.$options.methods.change) {
      chain.push({changeSrc: vue.$options.methods.change.toString().slice(0, 800)});
    }
    vue = vue.$parent;
    depth++;
  }
  return JSON.stringify(chain, null, 2);
})()
