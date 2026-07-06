(() => {
  // 直接调用 startPractice 并捕获
  const card = document.querySelector('.exercise-card');
  if (!card || !card.__vue__) return 'no vue card';
  const indexComp = card.__vue__.$parent.$parent.$parent;
  try {
    const r = indexComp.startPractice(570);
    return 'called, result type: ' + typeof r + ', is promise: ' + (r && typeof r.then === 'function');
  } catch(e) {
    return 'error: ' + e.message + ' | stack: ' + e.stack.slice(0, 300);
  }
})()
