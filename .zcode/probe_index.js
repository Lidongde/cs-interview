(() => {
  const card = document.querySelector('.exercise-card');
  // index 在 depth 2: $parent.$parent
  let vue = card.__vue__.$parent.$parent;
  const methods = vue.$options.methods;
  const result = {};
  // startPractice
  result.startPractice = methods.startPractice ? methods.startPractice.toString() : 'NONE';
  // fetchTagData
  result.fetchTagData = methods.fetchTagData ? methods.fetchTagData.toString() : 'NONE';
  // onQueryChange
  result.onQueryChange = methods.onQueryChange ? methods.onQueryChange.toString().slice(0, 400) : 'NONE';
  // 查看 index 上注册的 listeners (来自模板的 @singleTagPaper 等)
  // 检查 CatalogPlatform 组件实例上的 $listeners
  const catalog = card.__vue__.$parent;
  result.catalogListeners = Object.keys(catalog.$listeners || {});
  // 检查 index 组件的 $data
  result.indexData = Object.keys(vue.$data || {});
  result.indexCurrentSwitch = vue.currentSwitch;
  return JSON.stringify(result, null, 2);
})()
