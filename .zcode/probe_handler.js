(() => {
  const card = document.querySelector('.exercise-card');
  const vue = card.__vue__;
  // 获取 cardClickHandler 的源码
  const handler = vue.$options.methods.cardClickHandler;
  const src = handler.toString();
  // 获取 cardInfo prop
  const cardInfo = vue.cardInfo;
  return JSON.stringify({handlerSrc: src, cardInfo}, null, 2);
})()
