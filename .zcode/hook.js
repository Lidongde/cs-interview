(() => {
  // 拦截并记录网络请求
  window.__apiCalls = [];
  const origFetch = window.fetch;
  window.fetch = function(...args) {
    const url = typeof args[0] === 'string' ? args[0] : args[0]?.url;
    window.__apiCalls.push({type: 'fetch', url: url?.slice(0, 200), method: args[1]?.method || 'GET'});
    return origFetch.apply(this, args);
  };
  const origOpen = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function(method, url) {
    window.__apiCalls.push({type: 'xhr', url: url?.slice(0, 200), method});
    return origOpen.apply(this, arguments);
  };
  return 'hooks installed';
})()
