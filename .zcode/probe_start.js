(() => {
  const card = document.querySelector('.exercise-card');
  // depth 2 是 index 组件
  let vue = card.__vue__.$parent.$parent;
  const methods = vue.$options.methods;
  const result = {};
  // startPractice
  if (methods.startPractice) result.startPractice = methods.startPractice.toString();
  // actionCurrentTagItemChange
  if (methods.actionCurrentTagItemChange) result.actionCurrentTagItemChange = methods.actionCurrentTagItemChange.toString();
  // onQueryChange
  if (methods.onQueryChange) result.onQueryChange = methods.onQueryChange.toString();
  // singleTagPaper 监听处理 - 找 emit 的处理
  // 查找 updateUrl 方法
  if (methods.updateUrl) result.updateUrl = methods.updateUrl.toString();
  // 查找 data 中的相关字段
  result.dataKeys = Object.keys(vue.$data || {});
  // 查找 currentSwitch
  result.currentSwitch = vue.currentSwitch;
  result.userInfo = vue.userInfo;
  return JSON.stringify(result, null, 2);
})()
