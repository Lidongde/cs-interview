(() => {
  // 安装 fetch hook
  window.__apiCalls = [];
  const origFetch = window.fetch;
  window.fetch = function(...args) {
    const url = typeof args[0] === 'string' ? args[0] : (args[0] && args[0].url);
    const method = (args[1] && args[1].method) || 'GET';
    const body = (args[1] && args[1].body) || '';
    window.__apiCalls.push({url: url ? url.slice(0, 300) : '', method, body: typeof body === 'string' ? body.slice(0, 200) : ''});
    return origFetch.apply(this, args);
  };
  // hook XMLHttpRequest
  const origOpen = XMLHttpRequest.prototype.open;
  const origSend = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function(method, url) {
    this.__nc_method = method;
    this.__nc_url = url;
    return origOpen.apply(this, arguments);
  };
  XMLHttpRequest.prototype.send = function(body) {
    window.__apiCalls.push({url: (this.__nc_url||'').slice(0,300), method: this.__nc_method||'GET', body: typeof body === 'string' ? body.slice(0,200) : '', type: 'xhr'});
    return origSend.apply(this, arguments);
  };
  return 'hooks installed';
})()
