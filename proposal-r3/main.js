(function(){
  // 案B：演出なし。メニュー開閉と、スマホ下部ボタンの表示だけを行う。
  var head=document.getElementById('head'),btn=head&&head.querySelector('.menu-btn'),nav=document.getElementById('gnav'),dock=document.getElementById('dock');
  if(btn&&nav){
    var set=function(o){document.body.classList.toggle('menu-open',o);btn.setAttribute('aria-expanded',o?'true':'false')};
    btn.addEventListener('click',function(){set(btn.getAttribute('aria-expanded')!=='true')});
    nav.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&btn.getAttribute('aria-expanded')==='true'){set(false);btn.focus()}});
  }
  if(dock){
    var f=function(){dock.classList.toggle('show',window.scrollY>Math.min(520,window.innerHeight*0.7))};
    window.addEventListener('scroll',f,{passive:true});f();
  }
})();
