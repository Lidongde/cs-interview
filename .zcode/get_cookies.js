(() => {
  // 导出当前所有 cookie
  const cookies = document.cookie.split(';').map(c => c.trim());
  // 也获取 document 上可见的存储
  const lsKeys = [];
  try { for (let i = 0; i < localStorage.length; i++) lsKeys.push(localStorage.key(i)); } catch(e) {}
  return JSON.stringify({
    url: location.href,
    cookieCount: cookies.length,
    cookies: cookies,
    localStorageKeys: lsKeys.slice(0, 30)
  }, null, 2);
})()
