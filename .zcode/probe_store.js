(() => {
  const card = document.querySelector('.exercise-card');
  let p = card.__vue__.$parent.$parent.$parent; // index
  // 查看它的 data，特别是 tagsCache, catalogTags
  const data = {
    totalCount: p.totalCount,
    tagIds: p.tagIds,
    questionType: p.questionType,
    catalogTags: typeof p.catalogTags === 'object' ? Object.keys(p.catalogTags || {}).slice(0, 5) : p.catalogTags,
    secondaryClassification: p.secondaryClassification,
    tagsCache: typeof p.tagsCache === 'object' ? Object.keys(p.tagsCache || {}).slice(0, 5) : String(p.tagsCache).slice(0, 100)
  };
  // 检查 appStore / examStore
  const appStore = p.appStore;
  const examStore = p.examStore;
  const storeInfo = {};
  if (appStore) {
    storeInfo.appStoreKeys = Object.keys(appStore.$data || appStore).slice(0, 20);
  }
  if (examStore) {
    storeInfo.examStoreKeys = Object.keys(examStore.$data || examStore).slice(0, 20);
  }
  return JSON.stringify({data, storeInfo}, null, 2);
})()
