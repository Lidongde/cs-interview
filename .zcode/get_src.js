(() => {
  const card = document.querySelector('.exercise-card');
  const indexComp = card.__vue__.$parent.$parent.$parent;
  // 获取 startPractice 的完整源码
  const src = indexComp.$options.methods.startPractice.toString();
  // 获取 fetchTagData 完整源码
  const fetchSrc = indexComp.$options.methods.fetchTagData.toString();
  // onQueryChange
  const onQuery = indexComp.$options.methods.onQueryChange.toString();
  return JSON.stringify({startPractice: src, fetchTagData: fetchSrc, onQueryChange: onQuery}, null, 2);
})()
