(function(){
  var head=document.getElementById('head'), btn=head.querySelector('.menu-btn'), nav=document.getElementById('gnav'), dock=document.getElementById('dock');

  // スマホのメニュー開閉
  function setMenu(open){document.body.classList.toggle('menu-open',open);btn.setAttribute('aria-expanded',open?'true':'false')}
  btn.addEventListener('click',function(){setMenu(btn.getAttribute('aria-expanded')!=='true')});
  nav.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});

  // ヘッダーの線と、スマホ下部ボタンの表示
  var hero=document.getElementById('top'), heroH=hero?hero.offsetHeight*0.8:120;
  function onScroll(){
    var y=window.scrollY;
    head.classList.toggle('scrolled',y>8);
    dock.classList.toggle('show',y>heroH);
  }
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();

  // 開催日までの日数（開催日を過ぎたら出さない）
  var count=document.getElementById('count');
  if(count){
    var start=new Date('2027-02-14T00:00:00+09:00'), now=new Date();
    var days=Math.ceil((start-now)/86400000);
    if(days>0){document.getElementById('days').textContent=days;count.hidden=false}
    else if(days===0){count.textContent='本日開催！ 10:00〜20:00';count.hidden=false}
  }

  // スクロールで表示
  var items=document.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){items.forEach(function(el){el.classList.add('on')});return}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
  items.forEach(function(el){io.observe(el)});
})();
