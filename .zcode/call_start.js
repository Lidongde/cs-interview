(() => {
  // 安装 hook
  window.__apiCalls = [];
  const origFetch = window.fetch;
  window.fetch = function(...args) {
    const url = typeof args[0] === 'string' ? args[0] : (args[0] && args[0].url);
    window.__apiCalls.push({type: 'fetch', url: url ? url.slice(0, 250) : '', method: (args[1] && args[1].method) || 'GET'});
    return origFetch.apply(this, args);
  };
  const origOpen = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function(method, url) {
    window.__apiCalls.push({type: 'xhr', url: url ? url.slice(0, 250) : '', method});
    return origOpen.apply(this, arguments);
  };
  window.__urlChanges = [];
  const origPush = history.pushState;
  history.pushState = function() { window.__urlChanges.push({type:'push', url: arguments[2]}); return origPush.apply(this, arguments); };
  const origReplace = history.replaceState;
  history.replaceState = function() { window.__urlChanges.push({type:'replace', url: arguments[2]}); return origReplace.apply(this, arguments); };

  // 调用 startPractice(570)  - Java tag id
  const card = document.querySelector('.exercise-card');
  const indexComp = card.__vue__.$parent.$parent.$parent;
  try {
    indexComp.startPractice(570);
    return 'called startPractice(570)';
  } catch(e) {
    return 'error: ' + e.message;
  }
})()
