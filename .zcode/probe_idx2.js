(() => {
  const card = document.querySelector('.exercise-card');
  let vue = card.__vue__;  // ExercisesCard
  // CatalogPlatform 监听了 singleTagPaper，处理者在它的父组件
  // 在 Vue 2 中，父组件通过 _events 处理子组件 emit
  const catalog = card.__vue__.$parent;  // CatalogPlatform
  // catalog.$parent 才是监听者
  const parent = catalog.$parent;
  const result = {
    parentName: parent.$options.name || parent.$options._componentTag || 'anon',
    parentMethods: Object.keys(parent.$options.methods || {}),
    parentData: Object.keys(parent.$data || {}),
  };
  // 检查 parent 上 singleTagPaper 的处理
  // Vue 中 @singleTagPaper="xxx" 会在 parent.$options._parentListeners 或 parent 的 methods
  // 直接看 parent 的 methods 中相关
  const ms = parent.$options.methods || {};
  for (const m of Object.keys(ms)) {
    if (/single|paper|practice|start|tag/i.test(m)) {
      result[m] = ms[m].toString().slice(0, 800);
    }
  }
  // 也检查 startPractice
  if (ms.startPractice) result.startPractice_full = ms.startPractice.toString();
  if (ms.fetchTagData) result.fetchTagData_full = ms.fetchTagData.toString().slice(0, 800);
  return JSON.stringify(result, null, 2);
})()
