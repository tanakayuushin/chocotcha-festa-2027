# -*- coding: utf-8 -*-
"""チョコっちゃ‼フェスタ2027 公式サイトの8ページを生成する（作業用、リポジトリには含めない）。
文面は「HP内容修正案 v1_r3」H01〜H24 の掲載文案を正本とする。"""
import json, sys, urllib.parse, os

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
BASE = 'https://chocotcha.jp/'
NAME = 'やまぐちチョコっちゃ‼フェスタ 2027'
ORG = 'チョコっちゃフェスタ実行委員会'
MAIL = 'chocotcha.festa@gmail.com'
IG = 'https://www.instagram.com/chocotcha_festa/'
IG_NAME = '@chocotcha_festa'
GA_ID = 'G-MVPER0MPET'  # Google アナリティクス（GA4）の測定ID。空なら出力しない
UPD_ISO, UPD_JA, UPD_DOT = '2026-10-29', '2026年10月29日', '2026.10.29'
VER = '20261029d'

def ph(title, text):
    return '<div class="ph" role="note"><span class="badge prep">準備中</span><div><b>%s</b><p>%s</p></div></div>' % (title, text)

def mailto(subject):
    return 'mailto:%s?subject=%s' % (MAIL, urllib.parse.quote(subject))

NAV = [
    ('index.html', 'トップ'),
    ('enjoy.html', '楽しみ方'),
    ('booth.html', 'ブース・出店'),
    ('timetable.html', 'ステージ・出演'),
    ('access.html', 'アクセス'),
    ('faq.html', 'FAQ'),
    ('contact.html', 'お問い合わせ'),
]

ICON = {
 'visit': '<svg viewBox="0 0 32 32" fill="none" stroke="#5a2a17" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 29s-9-8.2-9-15a9 9 0 0 1 18 0c0 6.8-9 15-9 15z"/><path d="M16 18.2s-3.6-2.3-3.6-4.8a2.1 2.1 0 0 1 3.6-1.4 2.1 2.1 0 0 1 3.6 1.4c0 2.5-3.6 4.8-3.6 4.8z" fill="#e3171a" stroke="none"/></svg>',
 'shop': '<svg viewBox="0 0 32 32" fill="none" stroke="#5a2a17" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l2.2-6h17.6L27 12"/><path d="M5 12c0 2 1.6 3.2 3.7 3.2S12.4 14 12.4 12c0 2 1.6 3.2 3.6 3.2s3.6-1.2 3.6-3.2c0 2 1.6 3.2 3.7 3.2S27 14 27 12"/><path d="M7 15.5V26h18V15.5"/><path d="M13 26v-6h6v6"/></svg>',
 'stage': '<svg viewBox="0 0 32 32" fill="none" stroke="#5a2a17" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="12" y="4" width="8" height="14" rx="4"/><path d="M8 15a8 8 0 0 0 16 0"/><path d="M16 23v5M11 28h10"/></svg>',
 'help': '<svg viewBox="0 0 32 32" fill="none" stroke="#5a2a17" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="12" width="22" height="15" rx="2.5"/><path d="M3.5 12h25v-3.5h-25z"/><path d="M16 8.5V27"/><path d="M16 8.5c-2-4.5-7-5-7-2s4 2 7 2c3 0 7 1 7-2s-5-2.5-7 2z"/></svg>',
}

def head(page, title, desc, og_title=None, jsonld=None):
    url = BASE if page == 'index.html' else BASE + page
    og_title = og_title or title
    h = ['<!doctype html>', '<html lang="ja">', '<head>', '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
         '<meta name="google-site-verification" content="v2-ba0GuVYBDD38ToYUJQ4U9aWuIBL6RIpnKg5NgPIE">',
         '<title>%s</title>' % title,
         '<meta name="description" content="%s">' % desc,
         '<link rel="canonical" href="%s">' % url,
         '<meta name="theme-color" content="#e3171a">',
         '<link rel="icon" type="image/png" sizes="64x64" href="favicon.png">',
         '<link rel="icon" type="image/png" sizes="512x512" href="icon-512.png">',
         '<link rel="apple-touch-icon" href="apple-touch-icon.png">',
         '<meta property="og:type" content="website">',
         '<meta property="og:site_name" content="%s">' % NAME,
         '<meta property="og:title" content="%s">' % og_title,
         '<meta property="og:description" content="%s">' % desc,
         '<meta property="og:url" content="%s">' % url,
         '<meta property="og:image" content="%sogp.png">' % BASE,
         '<meta property="og:image:width" content="1200">',
         '<meta property="og:image:height" content="630">',
         '<meta property="og:image:alt" content="%s 2027年2月14日（日）開催予定 入場無料">' % NAME,
         '<meta property="og:locale" content="ja_JP">',
         '<meta name="twitter:card" content="summary_large_image">',
         '<meta name="twitter:title" content="%s">' % og_title,
         '<meta name="twitter:description" content="%s">' % desc,
         '<meta name="twitter:image" content="%sogp.png">' % BASE]
    if GA_ID:
        h.append('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>' % GA_ID)
        h.append('<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date());gtag("config","%s",{anonymize_ip:true});</script>' % GA_ID)
    if jsonld:
        h.append('<script type="application/ld+json">\n%s\n</script>' % json.dumps(jsonld, ensure_ascii=False, indent=2))
    h += ['<link rel="preconnect" href="https://fonts.googleapis.com">',
          '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
          '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Dela+Gothic+One&family=Zen+Maru+Gothic:wght@500;700;900&display=swap">',
          '<link rel="stylesheet" href="style.css?v=%s">' % VER,
          '</head>']
    return '\n'.join(h)

def header(page):
    links = []
    for href, label in NAV:
        cur = ' class="on" aria-current="page"' if href == page else ''
        links.append('      <a href="%s"%s>%s</a>' % (href, cur, label))
    cta_cur = ' aria-current="page"' if page == 'join.html' else ''
    links.append('      <a href="join.html" class="cta"%s>申込み</a>' % cta_cur)
    return '''<body data-page="%s">
<a class="skip" href="#main">本文へ移動</a>

<header class="site-head" id="head">
  <div class="in">
    <a class="brand" href="index.html" aria-label="%s トップへ"><img src="logo-wide-t-sm.png" alt="%s" width="480" height="160"></a>
    <button class="menu-btn" type="button" aria-controls="gnav" aria-expanded="false"><span></span><span></span><span></span><b class="sr">メニュー</b></button>
    <nav class="gnav" id="gnav" aria-label="サイト内">
%s
    </nav>
  </div>
</header>

<div class="status" role="note" aria-label="開催状況">
  <div class="in">
    <span class="st"><span class="badge">開催予定</span>2027年2月14日（日）</span>
    <span class="tx">開催に向けて準備中です。<span class="pc">正式な開催情報は、決まり次第このサイトでお知らせします。</span></span>
    <span class="upd">最終更新 <time datetime="%s">%s</time></span>
  </div>
</div>
''' % (page.replace('.html', ''), NAME, NAME, '\n'.join(links), UPD_ISO, UPD_JA)

def footer():
    return '''<footer>
  <div class="in">
    <a class="logo" href="index.html"><img src="logo-wide-t-sm.png" alt="%s トップへ" width="480" height="160" loading="lazy"></a>
    <nav aria-label="フッター">
      <a href="index.html">トップ</a><a href="enjoy.html">楽しみ方</a><a href="booth.html">ブース・出店</a><a href="timetable.html">ステージ・出演</a>
      <a href="join.html">出店・出演の申込み</a><a href="access.html">アクセス</a><a href="faq.html">FAQ</a><a href="contact.html">お問い合わせ・協力</a>
    </nav>
    <div class="cp"><span>© %s</span><span>掲載内容は予定を含みます ・ 最終更新 %s ・ <a href="contact.html#privacy">個人情報について</a></span></div>
  </div>
</footer>

<div class="dock" id="dock" aria-label="クイックリンク">
  <a class="btn ghost" href="access.html">アクセス</a>
  <a class="btn" href="join.html">申込み</a>
</div>

<script src="main.js?v=%s" defer></script>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "87a834849f22472088c174af808520de"}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
''' % (NAME, ORG, UPD_JA, VER)

def nextstep(items, title='次に見る'):
    cards = '\n'.join('      <a href="%s"><small>%s</small><b>%s</b></a>' % i for i in items)
    return '''<section class="nextstep" aria-labelledby="next-h">
  <div class="in">
    <h2 class="sub-head" id="next-h">%s</h2>
    <div class="go-list">
%s
    </div>
  </div>
</section>''' % (title, cards)

def sec_head(en, title, lead=None, tag='h2', hid=None):
    idattr = ' id="%s"' % hid if hid else ''
    p = '<p>%s</p>' % lead if lead else ''
    return '<div class="sec-head"><span class="en" aria-hidden="true">%s</span><%s%s>%s</%s>%s</div>' % (en, tag, idattr, title, tag, p)

# ---------- 料金（H05） ----------
FEES = {
 'booth':  ('通常ブースの出店料', '0', '円', ''),
 'car':    ('キッチンカーの出店料', '5,000', '円', ''),
 'stage1': ('第1ステージの通常出演料', '3,000', '円', ''),
 'stage2': ('第2ステージの通常出演料', None, '未定', '設置を検討中です'),
 'exhibit': ('非販売展示', '0', '円', '料金'),
 'plan':    ('主催企画の運営', '0', '円', '料金'),
}
FEE_NOTES = [
 '材料・仕入れなどの費用は出店者・出演者の負担が基本です。設備代等は別途相談します。',
 '非販売展示や主催企画運営に必要な実費の支援は、事前に内容を確認して個別に相談します。',
 '電源・机・椅子は、数量・仕様・費用の負担者を確認したうえで、利用できる範囲をご案内します。',
]
def fees(keys, notes=True):
    cards = []
    for k in keys:
        nm, yen, unit, d = FEES[k]
        if yen is None:
            y = '<span class="yen undecided">%s</span>' % unit
        else:
            pre = d + ' ' if d == '料金' else ''
            y = '<span class="yen">%s%s<small>%s</small></span>' % (('<small>%s</small>' % pre) if pre else '', yen, unit)
        dd = '<span class="d">%s</span>' % d if (d and d != '料金') else ''
        cards.append('<li class="fee"><span class="nm">%s</span>%s%s</li>' % (nm, y, dd))
    out = ['<p class="fee-head"><span class="badge plan">料金案</span>※現行企画の料金案です。正式募集条件は要項確定後に公開します。</p>',
           '<ul class="fees">' + ''.join(cards) + '</ul>']
    if notes:
        out.append('<ul class="bullets fee-notes">' + ''.join('<li>%s</li>' % n for n in FEE_NOTES) + '</ul>')
    return '\n'.join(out)

PAGES = {}

# =====================================================================
# トップ
# =====================================================================
jsonld = {
 '@context': 'https://schema.org', '@type': 'Festival',
 'name': NAME,
 'description': '2027年2月14日（日）開催予定。こんこんパーク（山口市湯田温泉）を中心に計画中。入場無料・出入り自由。知らなかった味やお店、チョコの楽しみ方に出会う一日を、学生・お店・地域のみなさんとつくります。',
 'startDate': '2027-02-14T10:00:00+09:00', 'endDate': '2027-02-14T20:00:00+09:00',
 'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode',
 'isAccessibleForFree': True,
 'image': [BASE + 'ogp.png'], 'url': BASE,
 'location': {'@type': 'Place', 'name': '湯田温泉 こんこんパーク',
              'address': {'@type': 'PostalAddress', 'streetAddress': '湯田温泉5-2-15', 'addressLocality': '山口市', 'addressRegion': '山口県', 'addressCountry': 'JP'}},
 'organizer': {'@type': 'Organization', 'name': ORG, 'email': MAIL, 'url': BASE, 'sameAs': [IG]},
}
idx_desc = '%s 公式サイト。2027年2月14日（日）10:00〜20:00開催予定。こんこんパーク（山口市湯田温泉）を中心に計画中。入場無料・出入り自由。来場・出店・出演・協力の案内。' % NAME
RIBBON = ['2027.2.14 SUN 開催予定', 'こんこんパークを中心に計画中', '入場無料・出入り自由', 'バレンタインって、こんなに楽しい。', '十人十色のバレンタイン', '募集要項は11月11日ごろ公開予定']
ribbon = ''.join('<span>%s</span>' % s for s in RIBBON)

PAGES['index.html'] = (head('index.html', '%s｜2027年2月14日（日）開催予定・湯田温泉こんこんパーク' % NAME, idx_desc,
                            og_title='%s｜2.14 SUN 開催予定・入場無料' % NAME, jsonld=jsonld), 'index', '''
<main id="main">
<section class="hero" aria-labelledby="hero-h">
  <svg class="ribbon-line" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M-20 92 C 240 22, 430 122, 710 72 S 1170 12, 1460 62" stroke="#f4a7b9" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M-20 104 C 240 34, 430 134, 710 84 S 1170 24, 1460 74" stroke="#e3171a" stroke-width="1.8" fill="none" stroke-dasharray="2 10" stroke-linecap="round"/></svg>
  <div class="in">
    <div class="logowrap">
      <img class="logo" src="logo-icon-t.png" alt="%(name)s ロゴ。板チョコを抱える白狐" width="1254" height="1254" fetchpriority="high">
    </div>
    <div class="copy">
      <p class="eyebrow">%(name)s</p>
      <h1 id="hero-h">バレンタインって、<br><em>こんなに楽しい。</em></h1>
      <p class="sub">ひとりでも、友達や家族とでも。<br>知らなかった味やお店、楽しみ方に出会う一日。</p>
      <p class="tag">十人十色のバレンタイン</p>

      <div class="ticket-wrap">
        <div class="ticket" role="group" aria-label="開催予定の日時と会場">
          <div class="stub"><span class="lbl">開催予定</span><span class="free">入場無料</span></div>
          <div class="tbody">
            <div class="date"><span class="big">2.14</span><span class="dow">SUN<small>2027年・日曜日</small></span></div>
            <p class="meta">2027年2月14日（日）<b>10:00〜20:00</b><br>こんこんパークを中心に計画中（山口市湯田温泉）<br>入場無料・出入り自由</p>
          </div>
        </div>
      </div>

      <div class="btns">
        <a class="btn" href="enjoy.html">来場案内を見る <span class="arr" aria-hidden="true">→</span></a>
        <p class="count" id="count" hidden>開催予定日まで<span class="num">あと<b id="days">--</b>日</span></p>
      </div>
      <p class="note">現在、開催に向けて会場・内容を調整しています。正式な開催情報は、決まり次第このページでお知らせします。商品・有料体験には別途料金がかかります。</p>
    </div>
  </div>
</section>

<div class="ribbon-clip" aria-hidden="true"><div class="ribbon"><div class="track">%(ribbon)s%(ribbon)s</div></div></div>

<section class="purpose" aria-labelledby="purpose-h">
  <div class="in">
    %(purpose_head)s
    <div class="goals">
      <a class="goal main" href="enjoy.html"><span class="ico">%(i_visit)s</span><span class="k">楽しみ方・アクセス</span><b>来場を考えている方</b><p>当日の楽しみ方、会場とアクセス、雨の日の案内。来場は申込み不要です。</p><span class="go">来場案内へ →</span></a>
      <a class="goal" href="booth.html"><span class="ico">%(i_shop)s</span><span class="k">出店のかたち・料金・設備</span><b>出店したい方</b><p>募集する出店のかたちと出店料の案、学生団体やお店の出店のしかた。</p><span class="go">出店の案内へ →</span></a>
      <a class="goal" href="timetable.html#perform"><span class="ico">%(i_stage)s</span><span class="k">出演条件・募集の流れ</span><b>出演したい方</b><p>出演時間の基本、出演料の案、ステージ企画を運営したい団体の相談。</p><span class="go">出演の案内へ →</span></a>
      <a class="goal" href="contact.html#support"><span class="ico">%(i_help)s</span><span class="k">協賛・物品・展示・運営</span><b>協力・協賛を考えている方</b><p>協賛、物品・設備の協力、展示の提供、企画運営など、関わり方のご相談。</p><span class="go">協力の相談へ →</span></a>
    </div>
  </div>
</section>

<section class="facts" aria-labelledby="facts-h">
  <div class="in">
    <h2 class="sr" id="facts-h">開催概要</h2>
    <ul>
      <li><span class="k">日時 <span class="badge plan">予定</span></span><span class="v">2027年2月14日（日）<small>10:00〜20:00</small></span></li>
      <li><span class="k">会場 <span class="badge plan">計画中</span></span><span class="v">こんこんパークを中心に計画中<small>山口市湯田温泉5-2-15</small></span></li>
      <li><span class="k">入場</span><span class="v">無料・出入り自由<small>商品・有料体験には別途料金がかかります</small></span></li>
      <li><span class="k">主催</span><span class="v">%(org)s</span></li>
    </ul>
    <p class="fnote">会場範囲・会場内の案内図・アクセスは、確認ができた情報から順次お知らせします。</p>
  </div>
</section>

<section class="sec about" aria-labelledby="about-h">
  <div class="in">
    %(about_head)s
    <div class="concept-wrap"><div class="concept">
      <svg class="bow" viewBox="0 0 84 60" aria-hidden="true" focusable="false"><g stroke="#5a2a17" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"><path d="M40 30L28 56l7-3 4 6 4-27z" fill="#bd1619"/><path d="M44 30l12 26-7-3-4 6-4-27z" fill="#bd1619"/><path d="M42 28C30 8 6 6 10 24c3 12 20 10 32 4z" fill="#e3171a"/><path d="M42 28C54 8 78 6 74 24c-3 12-20 10-32 4z" fill="#e3171a"/><rect x="36" y="22" width="12" height="13" rx="4" fill="#bd1619"/></g><path d="M16 21c4-6 12-7 19-1M68 21c-4-6-12-7-19-1" stroke="#f4a7b9" stroke-width="2.2" fill="none" stroke-linecap="round"/></svg>
      <p class="catch">バレンタインって、<em>こんなに楽しい。</em></p>
      <p>知らなかった味やお店、思いがけないチョコの楽しみ方に出会う一日を、学生・お店・地域のみなさんとつくります。</p>
      <p>自分へのごほうび、誰かへの感謝、友達や家族と過ごす時間。ひとりでも、通りがかりでも、自分らしい「十人十色のバレンタイン」を見つけてみませんか。</p>
    </div></div>
    <div class="trio">
      <div class="card"><div class="ic" aria-hidden="true">十</div><h3>十人十色のバレンタイン</h3><p>自分へのごほうびも、誰かへの感謝も、友達や家族と過ごす時間も。それぞれの楽しみ方で過ごせる一日をめざしています。</p></div>
      <div class="card"><div class="ic" aria-hidden="true">×</div><h3>学生・お店・地域でつくる</h3><p>学生団体や地域のお店が考える「バレンタインやチョコの楽しみ方」を、商品・飾りつけ・体験などで持ち寄る場をつくります。</p></div>
      <div class="card"><div class="ic" aria-hidden="true">山</div><h3>山口とチョコの背景</h3><p>山口商工会議所は、2018年の家計調査で山口市のチョコレートなどへの支出が全国上位となったことを、地域のチョコレート企画の背景として紹介しています。私たちは、そのつながりを知り、山口のお店やチョコの新しい楽しみ方に出会う機会をつくりたいと考えています。</p></div>
    </div>
  </div>
</section>

<div class="stripe" aria-hidden="true"></div>

<section class="sec cream" aria-labelledby="ways-h">
  <div class="in">
    %(ways_head)s
    <div class="ways">
      <a class="way big" href="enjoy.html#way-1"><span class="big-no" aria-hidden="true">01</span><span class="wrap-ribbon" aria-hidden="true"></span><span class="num">01</span><h3>チョコやスイーツ、チョコに合う食事・飲み物との出会い</h3><p>出店者は決まり次第このサイトで紹介します。</p><span class="more">くわしく見る →</span></a>
      <a class="way" href="enjoy.html#way-2"><span class="num">02</span><h3>感謝を伝える贈り物や小物づくり</h3><span class="more">くわしく見る →</span></a>
      <a class="way" href="enjoy.html#way-3"><span class="num">03</span><h3>学生や地域の団体による演奏・ダンス</h3><span class="more">くわしく見る →</span></a>
      <a class="way" href="enjoy.html#way-4"><span class="num">04</span><h3>世界のバレンタインやチョコ文化を知る展示</h3><span class="more">くわしく見る →</span></a>
    </div>
    <p class="ways-note"><span class="badge tbd">検討中</span>カラオケ大会などの参加型ステージも検討中です。出店者・内容・時間は、決まり次第お知らせします。</p>
    %(ph_1)s
    <div class="btns"><a class="btn ghost" href="enjoy.html">当日の楽しみ方をくわしく見る <span class="arr" aria-hidden="true">→</span></a></div>
  </div>
</section>

<section class="sec" id="news" aria-labelledby="news-h">
  <div class="in">
    %(news_head)s
    <ul class="news">
      <li><time datetime="%(upd_iso)s">%(upd_dot)s</time><span class="badge soon">公開予定</span><p>募集要項と専用申込フォームは、2026年11月11日ごろ公開予定です。準備状況により変更する場合があります。公開後、<a class="txtlink" href="join.html">申込みのページ</a>からご案内します。</p></li>
      <li><time datetime="%(upd_iso)s">%(upd_dot)s</time><span class="badge plan">更新</span><p>サイトの内容を更新しました。出店料・出演料の案、申込みまでの流れ、お問い合わせ先を掲載しています。</p></li>
    </ul>
  </div>
</section>

<section class="sec tight cream" aria-label="会場と主催">
  <div class="in two">
    <div class="card">
      <h2 class="sub-head">会場・アクセス</h2>
      <dl>
        <dt>予定会場</dt><dd>湯田温泉 こんこんパークを中心に計画中</dd>
        <dt>住所</dt><dd>山口県山口市湯田温泉5-2-15</dd>
        <dt>最寄り駅</dt><dd>JR山口線 湯田温泉駅</dd>
      </dl>
      <div class="acts"><a class="btn ghost sm" href="access.html">アクセスを見る →</a></div>
    </div>
    <div class="card">
      <h2 class="sub-head">主催・お問い合わせ</h2>
      <dl>
        <dt>主催</dt><dd>%(org)s</dd>
        <dt>メール</dt><dd><a class="txtlink" href="mailto:%(mail)s">%(mail)s</a></dd>
        <dt>Instagram</dt><dd><a class="txtlink" href="%(ig)s" target="_blank" rel="noopener">%(ig_name)s</a></dd>
      </dl>
      <div class="acts"><a class="btn ghost sm" href="contact.html">お問い合わせ・協力 →</a></div>
    </div>
  </div>
</section>
</main>
''' % dict(ph_1=ph('出店者・出演団体の紹介','決まり次第、ここに掲載します。'), name=NAME, org=ORG, mail=MAIL, ig=IG, ig_name=IG_NAME, ribbon=ribbon, upd_iso=UPD_ISO, upd_dot=UPD_DOT,
           i_visit=ICON['visit'], i_shop=ICON['shop'], i_stage=ICON['stage'], i_help=ICON['help'],
           purpose_head=sec_head('FIND', 'あなたの目的から探す', hid='purpose-h'),
           about_head=sec_head('ABOUT', 'チョコっちゃ‼フェスタって？', hid='about-h'),
           ways_head=sec_head('ENJOY', 'こんな楽しみ方を準備しています', '想像しやすい例を4つ紹介します。内容は決まり次第、楽しみ方のページでお知らせします。', hid='ways-h'),
           news_head=sec_head('NEWS', 'お知らせ・更新情報', hid='news-h')))

# =====================================================================
# 楽しみ方（来場者向け）
# =====================================================================
PAGES['enjoy.html'] = (head('enjoy.html', '当日の楽しみ方｜%s' % NAME,
    '来場を考えている方へ。入場無料・出入り自由。チョコやスイーツとの出会い、贈り物づくり、演奏・ダンス、チョコ文化の展示を準備中。ステージの予定、出店者の紹介、BINGOとチョコまき、来場前の案内。'), 'enjoy', '''
<main id="main">
<section class="sec" aria-labelledby="page-h">
  <div class="in">
    %(h)s
    <div class="ways">
      <div class="way big" id="way-1"><span class="big-no" aria-hidden="true">01</span><span class="wrap-ribbon" aria-hidden="true"></span><span class="num">01</span><h3>チョコやスイーツ、チョコに合う食事・飲み物との出会い <span class="badge prep">準備中</span></h3><p>知らなかった味やお店に出会える場をめざしています。出店者は決まり次第、このページで紹介します。商品には別途料金がかかります。</p></div>
      <div class="way" id="way-2"><span class="num">02</span><h3>感謝を伝える贈り物や小物づくり <span class="badge prep">準備中</span></h3><p>自分へのごほうびや、誰かへの感謝に。</p></div>
      <div class="way" id="way-3"><span class="num">03</span><h3>学生や地域の団体による演奏・ダンス <span class="badge prep">準備中</span></h3><p>出演団体と時間は、決まり次第このページのステージの予定でお知らせします。</p></div>
      <div class="way" id="way-4"><span class="num">04</span><h3>世界のバレンタインやチョコ文化を知る展示 <span class="badge prep">準備中</span></h3></div>
    </div>
    <p class="ways-note"><span class="badge tbd">検討中</span>カラオケ大会などの参加型ステージも検討中です。出店者・内容・時間は、決まり次第お知らせします。</p>
  </div>
</section>

<div class="stripe" aria-hidden="true"></div>

<section class="sec cream" id="stage" aria-labelledby="stage-h">
  <div class="in">
    %(h_stage)s
    <div class="two">
      <div class="card">
        <h3>タイムテーブル <span class="badge prep">準備中</span></h3>
        <p>開催時間は 10:00〜20:00 の予定です。ステージの番組と時間は、出演団体と内容が決まり次第ここでお知らせします。</p>
        %(ph_tt)s
      </div>
      <div class="card">
        <h3>ステージで予定していること</h3>
        <ul class="list">
          <li><span class="badge prep">準備中</span><div><b>学生や地域の団体による演奏・ダンス</b><span class="d">出演団体を募集する予定です</span></div></li>
          <li><span class="badge tbd">検討中</span><div><b>カラオケ大会などの参加型ステージ</b><span class="d">内容は決まり次第お知らせします</span></div></li>
        </ul>
        %(ph_perf)s
      </div>
    </div>
  </div>
</section>

<section class="sec" id="shops" aria-labelledby="shops-h">
  <div class="in">
    %(h_shops)s
    %(ph_shops)s
  </div>
</section>

<section class="sec cream" aria-labelledby="bingo-h">
  <div class="in">
    %(h2)s
    <div class="two">
      <div class="card"><h3>BINGO <span class="badge prep">準備中</span></h3><p>BINGOは、お買い物と連動した企画として準備中です。参加方法・カードの受取条件・景品は、決まり次第ご案内します。</p></div>
      <div class="card"><h3>チョコまき <span class="badge prep">準備中</span></h3><p>チョコまきも準備中です。実施方法は安全を確認して決定します。</p></div>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="before-h">
  <div class="in">
    %(h3)s
    <div class="three">
      <div class="card"><h3>入場</h3><p>入場無料・出入り自由です。来場に申込みは必要ありません。</p><p>商品・有料体験には別途料金がかかります。</p></div>
      <div class="card"><h3>会場と休憩</h3><p>こんこんパークを中心に開催を計画しています。会場範囲・会場内の案内図・アクセスは、確認ができた情報から順次お知らせします。</p><p>出入りは自由です。ご来場の際は、公開する会場案内と当日の誘導に沿ってお入りください。休憩場所も確定後にご案内します。</p><div class="acts"><a class="btn ghost sm" href="access.html">会場・アクセス →</a></div></div>
      <div class="card"><h3>雨の日</h3><p>通常の雨天時も開催する方針です。天候により、場所や内容を変更・縮小・中止する場合があります。変更情報はこのHPと公式Instagramでお知らせします。</p><div class="acts"><a class="btn ghost sm" href="faq.html">よくある質問 →</a></div></div>
    </div>
  </div>
</section>
</main>
%(next)s
''' % dict(h=sec_head('ENJOY', '当日の楽しみ方', 'こんな楽しみ方を準備しています。内容・出店者・時間は、決まり次第このページでお知らせします。', tag='h1', hid='page-h'),
           h_stage=sec_head('STAGE', 'ステージの予定', hid='stage-h'),
           ph_tt=ph('タイムテーブル','出演団体と時間が決まり次第、ここに掲載します。'),
           ph_perf=ph('出演団体の紹介','決まり次第、ここに掲載します。'),
           h_shops=sec_head('SHOPS', '出店者の紹介', hid='shops-h'),
           ph_shops=ph('出店者の紹介','決まり次第、ここに掲載します。'),
           h2=sec_head('EVENT', 'BINGOとチョコまき', hid='bingo-h'),
           h3=sec_head('BEFORE YOU GO', '来場の前に', hid='before-h'),
           next=nextstep([('access.html', '地図と最寄り駅', '会場・アクセス'), ('faq.html', '入場料・雨の日など', 'よくある質問'), ('join.html', '出店・出演したい方', '出店・出演の申込み・料金')])))

# =====================================================================
# ステージ・出演
# =====================================================================
PAGES['timetable.html'] = (head('timetable.html', 'ステージ・出演｜%s' % NAME,
    '出演したい方への案内。通常の出演時間は15分、転換は5分が基本。第1ステージの出演料の案、第2ステージは設置を検討中。主催企画の運営の相談も歓迎。'), 'timetable', '''
<main id="main">
<section class="sec" id="perform" aria-labelledby="page-h">
  <div class="in">
    %(h)s
    <div class="two">
      <div class="card">
        <h3>出演の基本</h3>
        <p>通常の出演時間は15分、転換は5分を基本に調整します。演奏・ダンスなどの活動発表に加え、来場者向けの企画を運営する団体の相談も歓迎します。</p>
      </div>
      <div class="card">
        <h3>第2ステージ <span class="badge tbd">検討中</span></h3>
        <p>第2ステージは設置を検討中です。利用施設・設備・出演料は決まり次第ご案内します。</p>
      </div>
    </div>
    <p class="note-box" style="margin-top:22px">当日のステージの予定と出演団体の紹介は、<a class="txtlink" href="enjoy.html#stage">当日の楽しみ方</a>のページでご案内します。</p>
  </div>
</section>

<div class="stripe" aria-hidden="true"></div>

<section class="sec cream" aria-labelledby="fee-h">
  <div class="in">
    %(h2)s
    %(fees)s
    <div class="apply">
      <div class="tx"><h3>出演の申込み <span class="badge soon">公開予定</span></h3><p>募集要項と専用申込フォームは2026年11月11日ごろ公開予定です。それまでは、メールまたは公式InstagramのDMで出演の相談を受け付けています。</p></div>
      <a class="btn" href="join.html">申込みの流れを見る <span class="arr" aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
</main>
%(next)s
''' % dict(h=sec_head('STAGE', 'ステージ・出演', '出演したい方への案内です。正式な募集条件は要項でお知らせします。', tag='h1', hid='page-h'),
           h2=sec_head('FEE', '出演料', hid='fee-h'),
           fees=fees(['stage1', 'stage2', 'plan']),
           next=nextstep([('join.html', '相談・申込み・料金', '出店・出演の申込み・料金'), (mailto('ステージ出演の相談'), 'メールで相談', MAIL), ('booth.html', 'ブースを出したい方', 'ブース・出店')])))

# =====================================================================
# 出店
# =====================================================================
PAGES['booth.html'] = (head('booth.html', 'ブース・出店｜%s' % NAME,
    '出店したい方への案内。学生団体や地域のお店の出店を募集する予定です。店舗単独の出店も可能。募集する出店のかたち、出店料の案、キッチンカー。'), 'booth', '''
<main id="main">
<section class="sec" aria-labelledby="page-h">
  <div class="in">
    %(h)s
    <div class="card" style="max-width:860px;margin:0 auto">
      <h2 class="sub-head">出店のかたち <span class="badge new">募集予定</span></h2>
      <p class="lead-p">学生団体や地域のお店の出店を募集する予定です。店舗単独の出店も可能です。学生が主体となる売場では、商品の仕入れや委託販売先の相談も受け付けます。</p>
      <p class="lead-p">各団体が考える「バレンタインやチョコの楽しみ方」を、商品・飾りつけ・体験などで教えてください。</p>
    </div>
  </div>
</section>

<section class="sec cream" aria-labelledby="types-h">
  <div class="in">
    %(h2)s
    <ul class="pieces">
      <li class="piece"><span class="n" aria-hidden="true">01</span><span class="t">調理を伴う飲食販売</span><p>会場で調理して提供する飲食の販売です。</p></li>
      <li class="piece"><span class="n" aria-hidden="true">02</span><span class="t">会場で調理しない飲食販売</span><p>既存の個包装菓子を仕入れる、店舗の商品を預かって販売するなど。</p></li>
      <li class="piece"><span class="n" aria-hidden="true">03</span><span class="t">物販</span></li>
      <li class="piece"><span class="n" aria-hidden="true">04</span><span class="t">体験</span><p>体験枠では飲食販売を行いません。</p></li>
      <li class="piece"><span class="n" aria-hidden="true">05</span><span class="t">非販売展示</span><p>販売を行わない展示です。</p></li>
    </ul>
    <ul class="bullets" style="margin-top:22px">
      <li>「会場で調理しない飲食販売」は、既存の個包装菓子を仕入れる、店舗の商品を預かって販売するなどです。体験枠では飲食販売を行いません。</li>
      <li>必要な設備・保管方法・販売主体などを事前に確認します。</li>
      <li>キッチンカーは別枠です。通常出演・ステージ企画運営は<a class="txtlink" href="timetable.html#perform">出演のページ</a>でご案内します。</li>
      <li>来場者自身が食品を調理する体験は行いません。</li>
    </ul>
  </div>
</section>

<section class="sec" aria-labelledby="fee-h">
  <div class="in">
    %(h3)s
    %(fees)s
    <div class="apply">
      <div class="tx"><h3>出店の申込み <span class="badge soon">公開予定</span></h3><p>募集要項と専用申込フォームは2026年11月11日ごろ公開予定です。それまでは、メールまたは公式InstagramのDMで出店の相談を受け付けています。</p></div>
      <a class="btn" href="join.html">申込みの流れを見る <span class="arr" aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
</main>
%(next)s
''' % dict(h=sec_head('BOOTH', 'ブース・出店', '出店したい方への案内です。募集する出店のかたちと、出店料の案をご案内します。正式な募集条件は要項でお知らせします。', tag='h1', hid='page-h'),
           h2=sec_head('TYPES', '募集する出店のかたち', hid='types-h'),
           h3=sec_head('FEE', '出店料', hid='fee-h'),
           fees=fees(['booth', 'car', 'exhibit']),
           next=nextstep([('join.html', '相談・申込み・料金', '出店・出演の申込み・料金'), (mailto('出店の相談'), 'メールで相談', MAIL), ('timetable.html#perform', 'ステージに出たい方', 'ステージ・出演')])))

# =====================================================================
# 出店・出演の申込み・料金
# =====================================================================
PAGES['join.html'] = (head('join.html', '出店・出演の申込み・料金｜%s' % NAME,
    '出店・出演を考えている方への案内。募集要項と専用申込フォームは2026年11月11日ごろ公開予定。相談窓口、申込みから出店・出演の確定までの流れ、出店料・出演料の案。'), 'join', '''
<main id="main">
<section class="sec" aria-labelledby="page-h">
  <div class="in">
    %(h)s
    <div class="desks">
      <div class="desk">
        <h3>出店・出演の相談</h3>
        <p>メールまたは公式InstagramのDMへ。</p>
        <div class="acts"><a class="btn sm" href="%(m_consult)s">メールで相談する</a><a class="btn sm ghost" href="%(ig)s" target="_blank" rel="noopener">InstagramでDMを送る</a></div>
      </div>
      <div class="desk">
        <h3>正式な申込み <span class="badge soon">公開予定</span></h3>
        <p>募集要項と専用申込フォームは2026年11月11日ごろ公開予定です。準備状況により変更する場合があります。公開後、このページからご案内します。</p>
        %(ph_5)s
      </div>
      <div class="desk">
        <h3>学生向けアンケート <span class="badge no">申込みではありません</span></h3>
        <p>企画づくりのための需要調査です。回答しても出店・出演の申込みにはなりません。</p>
      </div>
    </div>
    <p class="note-box" style="margin-top:22px">申込み・お問い合わせの情報は、内容確認、連絡、当日の運営に使用します。協賛者への名簿の自動提供は行いません。詳しい取扱いは<a class="txtlink" href="contact.html#privacy">「個人情報について」</a>をご確認ください。</p>
  </div>
</section>

<div class="stripe" aria-hidden="true"></div>

<section class="sec cream" aria-labelledby="flow-h">
  <div class="in">
    %(h2)s
    <div class="flow-wrap">
      <ol class="flow">
        <li>募集要項を確認</li><li>専用フォーム送信</li><li>内容・設備の相談</li><li>出店・出演の条件の提示</li><li>合意と必要な入金確認</li><li>出店・出演の確定</li>
      </ol>
    </div>
    <p class="note-box" style="margin-top:22px"><b>フォームの送信だけでは出店・出演は確定しません。</b>主催から連絡し、条件を確認します。</p>
  </div>
</section>

<section class="sec" aria-labelledby="sched-h">
  <div class="in">
    %(h3)s
    <div class="card" style="max-width:860px;margin:0 auto">
      <ul class="list">
        <li><span class="badge soon">公開予定</span><div><b>2026年11月11日ごろ　募集要項・専用申込フォーム</b><span class="d">準備状況により変更する場合があります。公開後、このページからご案内します。</span></div></li>
        <li><span class="badge prep">準備中</span><div><b>募集開始日・締切</b><span class="d">要項確定後にお知らせします。</span></div></li>
        <li><span class="badge prep">準備中</span><div><b>選考方法</b><span class="d">募集区分ごとの選考方法は、正式募集前に要項でお知らせします。</span></div></li>
      </ul>
    </div>
  </div>
</section>

<section class="sec cream" aria-labelledby="fees-h">
  <div class="in">
    %(h4)s
    %(fees)s
  </div>
</section>
</main>
%(next)s
''' % dict(ph_5=ph('募集要項・専用申込フォーム','公開後、ここに掲載します。'), h=sec_head('JOIN', '出店・出演の申込み・料金', '出店・出演・展示・企画運営を考えている方への案内です。来場に申込みは必要ありません。', tag='h1', hid='page-h'),
           h2=sec_head('FLOW', '申込みから出店・出演の確定まで', hid='flow-h'),
           h3=sec_head('SCHEDULE', '募集の日程', hid='sched-h'),
           h4=sec_head('FEE', '出店料・出演料', hid='fees-h'),
           m_consult=mailto('出店・出演の相談'), ig=IG,
           fees=fees(['booth', 'car', 'exhibit', 'stage1', 'stage2', 'plan']),
           i_shop=ICON['shop'], i_stage=ICON['stage'], i_help=ICON['help'],
           next=nextstep([('booth.html', '出店のかたちと出店料', 'ブース・出店'), ('timetable.html#perform', '出演時間と出演料', 'ステージ・出演'), ('contact.html', '主催と窓口', 'お問い合わせ・協力')])))

# =====================================================================
# 会場・アクセス
# =====================================================================
PAGES['access.html'] = (head('access.html', '会場・アクセス｜%s' % NAME,
    '会場・アクセス。湯田温泉 こんこんパーク（山口市湯田温泉5-2-15）を中心に開催を計画中です。会場範囲・会場内の案内図・アクセスは、確認ができた情報から順次お知らせします。'), 'access', '''
<main id="main">
<section class="sec access" aria-labelledby="page-h">
  <div class="in">
    %(h)s
    <div class="box">
      <div class="mapframe">
        <iframe title="湯田温泉 こんこんパーク周辺の地図" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q=%%E6%%B9%%AF%%E7%%94%%B0%%E6%%B8%%A9%%E6%%B3%%89%%E3%%81%%93%%E3%%82%%93%%E3%%81%%93%%E3%%82%%93%%E3%%83%%91%%E3%%83%%BC%%E3%%82%%AF&amp;z=16&amp;output=embed"></iframe>
      </div>
      <div class="info">
        <div class="card">
          <h2 class="nm">湯田温泉 こんこんパーク <span class="badge plan">予定会場</span></h2>
          <dl>
            <dt>住所</dt><dd>山口県山口市湯田温泉5-2-15</dd>
            <dt>最寄り駅</dt><dd>JR山口線 湯田温泉駅</dd>
            <dt>お車で</dt><dd>駐車場のご案内は決まり次第お知らせします。なるべく公共交通機関をご利用ください。</dd>
          </dl>
          <a class="btn sm ghost" href="https://www.google.com/maps/search/?api=1&amp;query=%%E6%%B9%%AF%%E7%%94%%B0%%E6%%B8%%A9%%E6%%B3%%89%%E3%%81%%93%%E3%%82%%93%%E3%%81%%93%%E3%%82%%93%%E3%%83%%91%%E3%%83%%BC%%E3%%82%%AF" target="_blank" rel="noopener">地図アプリで開く（Googleマップ） <span class="arr" aria-hidden="true">↗</span></a>
        </div>
        <div class="card">
          <h2 class="nm">会場の使い方</h2>
          <dl>
            <dt>入口</dt><dd>出入りは自由です。ご来場の際は、公開する会場案内と当日の誘導に沿ってお入りください。</dd>
            <dt>休憩</dt><dd>休憩場所も確定後にご案内します。</dd>
            <dt>雨の日</dt><dd>通常の雨天時も開催する方針です。天候により、場所や内容を変更・縮小・中止する場合があります。</dd>
          </dl>
        </div>
      </div>
    </div>
    %(ph_map)s
  </div>
</section>
</main>
%(next)s
''' % dict(ph_map=ph('会場内の案内図・駐車場','確認ができた情報から、ここに掲載します。'), h=sec_head('ACCESS', '会場・アクセス', 'こんこんパークを中心に開催を計画しています。会場範囲・会場内の案内図・アクセスは、確認ができた情報から順次お知らせします。', tag='h1', hid='page-h'),
           next=nextstep([('enjoy.html', '来場者向けの案内', '当日の楽しみ方'), ('faq.html', '入場料・雨の日など', 'よくある質問'), ('contact.html', '主催と窓口', 'お問い合わせ・協力')])))

# =====================================================================
# よくある質問
# =====================================================================
FAQ = [
 ('入場料はかかりますか？', ['入場は無料で、出入り自由です。商品・有料体験には別途料金がかかります。', 'BINGOは、お買い物と連動した企画として準備中です。参加方法・カードの受取条件・景品は、決まり次第ご案内します。']),
 ('子どもも楽しめますか？', ['ひとりでも、友達や家族とでも楽しめる一日をめざして準備しています。チョコまきなどの企画の参加方法は、安全を確認したうえで決まり次第お知らせします。']),
 ('雨が降ったら中止ですか？', ['通常の雨天時も開催する方針です。天候により、場所や内容を変更・縮小・中止する場合があります。変更情報はこのHPと公式Instagramでお知らせします。']),
 ('駐車場はありますか？', ['駐車場のご案内は決まり次第お知らせします。なるべく公共交通機関をご利用ください。']),
 ('支払いは何が使えますか？', ['各ブースによって異なります。決まり次第、出店者紹介とあわせて掲載します。']),
 ('お酒はありますか？', ['決まり次第お知らせします。20歳未満の方への提供はいたしません。']),
 ('学生じゃなくても出店できますか？', ['はい。学生団体や地域のお店の出店を募集する予定です。店舗単独の出店も可能です。キッチンカーは別枠でご案内します。']),
 ('出店・出演の申込みはいつからですか？', ['募集要項と専用申込フォームは2026年11月11日ごろ公開予定です。準備状況により変更する場合があります。募集開始日・締切は要項確定後にお知らせします。', 'それまでは<a class="txtlink" href="%s">メール</a>または<a class="txtlink" href="%s" target="_blank" rel="noopener">公式InstagramのDM</a>で相談を受け付けています。' % (mailto('出店・出演の相談'), IG)]),
 ('学生向けアンケートに回答すれば申込みになりますか？', ['なりません。学生向けアンケートは企画づくりのための需要調査です。出店・出演には、公開予定の専用申込フォームからの申込みが必要です。']),
 ('フォームを送れば出店・出演は確定しますか？', ['フォームの送信だけでは出店・出演は確定しません。主催から連絡し、条件を確認します。くわしくは<a class="txtlink" href="join.html#flow-h">申込みから出店・出演の確定までの流れ</a>をご覧ください。']),
 ('協力・協賛をしたいのですが。', ['協賛、物品・設備の協力、展示の提供、企画運営など、関わり方をご相談ください。<a class="txtlink" href="contact.html#support">協力・協賛のご相談</a>からご連絡いただけます。']),
]
faq_html = '\n'.join('    <details><summary>%s</summary><div class="a">%s</div></details>' % (q, ''.join('<p>%s</p>' % a for a in ans)) for q, ans in FAQ)
PAGES['faq.html'] = (head('faq.html', 'よくある質問｜%s' % NAME,
    'よくある質問。入場料、子ども連れ、雨の日、駐車場、出店・出演の申込み時期、アンケートと申込みの違い、協力・協賛の相談など。'), 'faq', '''
<main id="main">
<section class="sec faq" aria-labelledby="page-h">
  <div class="in">
    %(h)s
%(faq)s
  </div>
</section>
</main>
%(next)s
''' % dict(h=sec_head('FAQ', 'よくある質問', tag='h1', hid='page-h'), faq=faq_html,
           next=nextstep([('enjoy.html', '来場者向けの案内', '当日の楽しみ方'), ('join.html', '相談・申込み・料金', '出店・出演の申込み・料金'), ('contact.html', '主催と窓口', 'お問い合わせ・協力')])))

# =====================================================================
# お問い合わせ・協力
# =====================================================================
PAGES['contact.html'] = (head('contact.html', 'お問い合わせ・協力｜%s' % NAME,
    'お問い合わせ・協力の相談窓口。主催：%s。メールまたは公式InstagramのDMへ。協賛、物品・設備の協力、展示の提供、企画運営のご相談。' % ORG), 'contact', '''
<main id="main">
<section class="sec contact-top" aria-labelledby="page-h">
  <div class="in">
    %(h)s
    <div class="cts">
      <div class="ct"><span class="k">主催</span><span class="v">%(org)s</span></div>
      <div class="ct"><span class="k">代表</span><span class="v">日髙聖一朗</span></div>
      <div class="ct wide"><span class="k">お問い合わせ（メール）</span><span class="v"><a href="mailto:%(mail)s">%(mail)s</a></span><span class="d">出店・出演に関するご相談も、こちらへお寄せください。</span></div>
      <div class="ct wide"><span class="k">公式Instagram</span><span class="v"><a href="%(ig)s" target="_blank" rel="noopener">%(ig_name)s</a></span><span class="d">公式InstagramのDMでもご相談いただけます。</span></div>
    </div>
  </div>
</section>


<section class="sec cream" id="support" aria-labelledby="support-h">
  <div class="in">
    %(h2)s
    <ul class="support-ways">
      <li><svg class="sw-ic" viewBox="0 0 32 32" fill="none" stroke="#5a2a17" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M16 27s-10-6.2-10-13a5.6 5.6 0 0 1 10-3.4A5.6 5.6 0 0 1 26 14c0 6.8-10 13-10 13z" fill="#fde9ee"/></svg>協賛</li>
      <li><svg class="sw-ic" viewBox="0 0 32 32" fill="none" stroke="#5a2a17" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 10l11-5 11 5v12l-11 5-11-5z" fill="#fff4e6"/><path d="M5 10l11 5 11-5M16 15v12"/></svg>物品・設備の協力</li>
      <li><svg class="sw-ic" viewBox="0 0 32 32" fill="none" stroke="#5a2a17" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="5" y="6" width="22" height="18" rx="2" fill="#fff4e6"/><path d="M8 21l6-7 4 4 3-3 4 6"/><circle cx="21" cy="11" r="1.8"/><path d="M12 28h8"/></svg>展示の提供</li>
      <li><svg class="sw-ic" viewBox="0 0 32 32" fill="none" stroke="#5a2a17" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 28V5"/><path d="M7 6h16l-3.5 5L23 16H7" fill="#fde9ee"/></svg>企画運営</li>
    </ul>
    <div class="btns" style="justify-content:center"><a class="btn" href="%(m_support)s">協力・協賛について相談する</a></div>
    %(ph_sup)s
  </div>
</section>

<section class="sec" id="privacy" aria-labelledby="privacy-h">
  <div class="in">
    %(h3)s
    <div class="card" style="max-width:860px;margin:0 auto">
      <p class="lead-p">申込み・お問い合わせの情報は、内容確認、連絡、当日の運営に使用します。協賛者への名簿の自動提供は行いません。</p>
      <p class="lead-p">このサイトでは、閲覧状況を把握し内容を改善するために、次のアクセス解析を利用しています。いずれも個人を特定する情報は収集しません。</p>
      <ul class="bullets" style="margin-top:12px">
        <li><b>Google アナリティクス</b>（Google LLC）：閲覧したページ、押したリンク、閲覧日時、おおよその地域、端末やブラウザの種類などが Google に送信されます。Cookie を使って同じ端末からの再訪問を区別します。IPアドレスは匿名化して扱います。Google の<a class="txtlink" href="https://policies.google.com/technologies/partner-sites?hl=ja" target="_blank" rel="noopener">データ利用の説明（外部サイト）</a></li>
        <li><b>Cloudflare Web Analytics</b>（Cloudflare, Inc.）：閲覧したページ、参照元、国、端末の種類が Cloudflare に送信されます。Cookie は使いません。</li>
      </ul>
      <p class="lead-p" style="margin-top:12px">収集した情報は、閲覧数や流入元の把握、サイトの改善にのみ使用します。</p>
      <p class="lead-p">保管期間などの詳しい取扱いは、決まり次第このページでお知らせします。</p>
    </div>
  </div>
</section>
</main>
%(next)s
''' % dict(h=sec_head('CONTACT', 'お問い合わせ・協力', '来場・出店・出演・取材・協力のご相談はこちらへ。', tag='h1', hid='page-h'),
           h2=sec_head('SUPPORT', '企画を一緒につくってくださる方へ', '協賛、物品・設備の協力、展示の提供、企画運営など、関わり方をご相談ください。協力内容やご紹介の方法は、個別に確認します。', hid='support-h'),
           h3=sec_head('PRIVACY', '個人情報について', hid='privacy-h'),
           org=ORG, mail=MAIL, ig=IG, ig_name=IG_NAME, m_support=mailto('協力・協賛の相談'), ph_sup=ph('ご協力いただく皆さまの紹介','確定後、ここに掲載します。'),
           next=nextstep([('join.html', '相談・申込み・料金', '出店・出演の申込み・料金'), ('enjoy.html', '来場者向けの案内', '当日の楽しみ方'), ('faq.html', '入場料・雨の日など', 'よくある質問')])))

for page, (h, key, body) in PAGES.items():
    html = h + '\n' + header(page) + body.rstrip('\n') + '\n\n' + footer()
    with open(os.path.join(OUT, page), 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', page, len(html))
