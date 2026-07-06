JSON.stringify({url: location.href, hasRecom: document.body.innerText.includes('推荐'), hasStart: document.body.innerText.includes('开始'), bodyHead: document.body.innerText.slice(0, 800)})
