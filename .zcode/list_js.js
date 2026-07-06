(() => {
  // 找到所有 performance entries 里的 JS 资源
  const entries = performance.getEntriesByType('resource');
  const jsFiles = entries.filter(e => e.name.endsWith('.js') || e.initiatorType === 'script').map(e => e.name);
  return JSON.stringify(jsFiles, null, 2);
})()
