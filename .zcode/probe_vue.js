(() => {
  // 查找所有 .exercise-card 上的事件绑定和 vue 实例
  const card = document.querySelector('.exercise-card');
  if (!card) return 'no card';
  // 查看 vue 实例
  const vueKeys = Object.keys(card).filter(k => k.startsWith('__vue') || k.startsWith('_vei'));
  // 查找 onclick 相关
  const attrs = Array.from(card.attributes).map(a => a.name + '=' + a.value);
  // 找到 vue 组件
  let vue = card.__vue__;
  let compInfo = 'none';
  if (vue) {
    compInfo = JSON.stringify({
      name: vue.$options.name || vue.$options._componentTag,
      methods: Object.keys(vue.$options.methods || {}),
      data: Object.keys(vue.$data || {}),
      props: Object.keys(vue.$props || {}),
    });
  }
  return JSON.stringify({vueKeys, attrs, compInfo}, null, 2);
})()
