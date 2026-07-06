(() => {
  const card = document.querySelector('.exercise-card');
  const indexComp = card.__vue__.$parent.$parent.$parent;
  const examStore = indexComp.examStore;
  const appStore = indexComp.appStore;
  return JSON.stringify({
    currentSwitch: examStore ? examStore.currentSwitch : 'no store',
    isLogin: appStore ? appStore.isLogin : 'no store',
    userInfo: appStore ? appStore.userInfo : 'no store',
    indexCurrentSwitch: indexComp.currentSwitch,
    zhuanxianglianxiABRes: indexComp.zhuanxianglianxiABRes
  }, null, 2);
})()
