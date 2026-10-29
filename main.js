(function(){
  var root=document.documentElement;
  var head=document.getElementById('head');
  var btn=head&&head.querySelector('.menu-btn');
  var nav=document.getElementById('gnav');
  var dock=document.getElementById('dock');

  // スマホのメニュー開閉（Escapeで閉じ、ボタンへフォーカスを戻す）
  if(btn&&nav){
    var setMenu=function(open){document.body.classList.toggle('menu-open',open);btn.setAttribute('aria-expanded',open?'true':'false')};
    btn.addEventListener('click',function(){setMenu(btn.getAttribute('aria-expanded')!=='true')});
    nav.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape'&&btn.getAttribute('aria-expanded')==='true'){setMenu(false);btn.focus()}
    });
  }

  // スマホ下部ボタンは、ページの最初の画面を過ぎてから出す
  if(dock){
    var onScroll=function(){dock.classList.toggle('show',window.scrollY>Math.min(520,window.innerHeight*0.7))};
    window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  }

  // どのリンクが押されたかを GA4 に送る（GA4 が入っていないときは何もしない）
  document.addEventListener('click',function(e){
    var a=e.target.closest('a[href]'); if(!a||typeof window.gtag!=='function')return;
    var h=a.getAttribute('href')||'', name='';
    if(h.indexOf('mailto:')===0)name='click_mail';
    else if(h.indexOf('instagram.com')>-1)name='click_instagram';
    else if(h.indexOf('google.com/maps')>-1)name='click_map';
    else if(/(^|\/)join\.html/.test(h))name='go_apply';
    else if(/^https?:\/\//.test(h)&&h.indexOf(location.hostname)===-1)name='click_outbound';
    if(name)gtag('event',name,{link_url:h,link_text:(a.textContent||'').trim().slice(0,60),page:location.pathname});
  });

  // 開催予定日までの日数（開催日を過ぎたら出さない）
  var count=document.getElementById('count');
  if(count){
    var start=new Date('2027-02-14T00:00:00+09:00'),now=new Date();
    var days=Math.ceil((start-now)/86400000);
    if(days>0){document.getElementById('days').textContent=days;count.hidden=false}
  }
})();
