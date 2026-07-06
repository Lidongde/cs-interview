(() => {
  const scripts = document.querySelectorAll('script[src]');
  const srcs = Array.from(scripts).map(s => s.src).filter(s => s.includes('nowcoder.com') || s.includes('static'));
  return JSON.stringify(srcs, null, 2);
})()
