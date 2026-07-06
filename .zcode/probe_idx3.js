(() => {
  const card = document.querySelector('.exercise-card');
  // card -> ExercisesCard, $parent=CatalogPlatform, $parent=LoadingAnimation, $parent=index
  let vue = card.__vue__;
  // 跳过 ExercisesCard 自身
  let p = vue.$parent; // CatalogPlatform
  p = p.$parent; // LoadingAnimation
  p = p.$parent; // index
  const result = {
    name: p.$options.name || p.$options._componentTag || 'anon',
    methods: Object.keys(p.$options.methods || {}),
    data: Object.keys(p.$data || {})
  };
  const ms = p.$options.methods || {};
  if (ms.startPractice) result.startPractice = ms.startPractice.toString();
  if (ms.fetchTagData) result.fetchTagData = ms.fetchTagData.toString().slice(0, 1000);
  if (ms.singleTagPaper) result.singleTagPaper = ms.singleTagPaper.toString();
  if (ms.onQueryChange) result.onQueryChange = ms.onQueryChange.toString().slice(0, 600);
  if (ms.actionCurrentTagItemChange) result.actionCurrentTagItemChange = ms.actionCurrentTagItemChange.toString();
  return JSON.stringify(result, null, 2);
})()
