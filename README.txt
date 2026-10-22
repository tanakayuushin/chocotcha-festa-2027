やまぐちチョコっちゃ‼フェスタ 2027 公式サイト 一式

■ 中身
  index.html        … ページ本体
  img/              … ロゴ（透過PNG）、OGP画像（SNSでリンクを貼ったときに出る画像）、ファビコン

■ 公開前に直すところ（index.html の上のほう、<head> の中）
  1. https://example.com/ を、実際に公開するURLに置き換える（6か所）
     ・<link rel="canonical" href="…">
     ・og:url、og:image、twitter:image
     ・JSON-LD の "url" と "image"、offers の "url"
  2. 決まったら差し替える文言
     ・Instagramアカウント名、メールアドレス（「お問い合わせ」）
     ・申込み方法（「参加したい方へ」の「申込み方法は準備中です」）
     ・メインスポンサー名とロゴ（「メインスポンサー・主催」）
     ・駐車場・送迎（「会場・アクセス」）

■ 公開のしかた
  ・自分のサーバーやレンタルサーバー：このフォルダの中身をそのままアップロードする
  ・Googleサイト：HTMLをそのまま読み込む仕組みがないため、各セクションの文章と画像をGoogleサイトのエディタに貼り直す必要がある
    （Googleサイトで作る場合は、img/ogp.png をヘッダー画像に、文章はこのページから写す）
  ・GitHub Pages、Netlify、Cloudflare Pages など無料のホスティングでもそのまま動く

■ Google検索・SNSでの見え方
  ・タイトルと説明文は <title> と <meta name="description"> で設定済み
  ・SNSでリンクを貼ったときの画像は img/ogp.png（1200×630）
  ・Googleのイベント表示（リッチリザルト）用の JSON-LD を入れてある。公開後に
    Google Search Console の「URL検査」とリッチリザルトテストで確認する
