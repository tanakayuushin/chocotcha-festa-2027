やまぐちチョコっちゃ‼フェスタ 2027 公式サイト

■ 公開URL
  https://chocotcha.jp/ （独自ドメイン。リポジトリ直下の CNAME で設定）
  https://tanakayuushin.github.io/chocotcha-festa-2027/ は上のURLへ転送されます。
  GitHub Pages（ブランチ main ／ フォルダ root）で公開しています。

■ ページ構成
  index.html      トップ（開催状態・目的別の入口・概要・楽しみ方・お知らせ）
  enjoy.html      当日の楽しみ方（来場者向け：楽しみ方4例・ステージの予定・出店者の紹介・BINGO・来場前の案内）
  booth.html      ブース・出店（出店したい方へ：出店のかたち・出店料・申込み）
  timetable.html  ステージ・出演（出演したい方へ：出演の基本・第2ステージ・出演料・申込み）
  join.html       出店・出演の申込み・料金（相談・正式申込み・流れ・日程）
  access.html     会場・アクセス
  faq.html        よくある質問
  contact.html    お問い合わせ・協力（主催・窓口・協賛の相談・個人情報について）
  style.css       共通のデザイン
  main.js         メニュー開閉・カウントダウン・クリック計測
  画像            ロゴ・OGP画像・アイコンはリポジトリ直下に置いています
  ファビコン      favicon.ico（16/32/48）・favicon-96.png・favicon-192.png・icon-512.png・apple-touch-icon.png。
                  Google検索結果に出すには48の倍数の正方形が条件。元は icon-512.png（差し替えたら各サイズも作り直す）

■ 更新するときの注意
  ・ヘッダー、開催状態の帯、フッターは全ページ共通です。変えるときは8ページすべてをそろえます。
  ・最終更新日は、開催状態の帯とフッターの両方にあります。
  ・style.css と main.js は「?v=日付」を付けて読み込んでいます。中身を変えたら全ページの日付も変えると、
    閲覧者のブラウザに古いデザインが残りにくくなります。
  ・日時・会場・料金を変えたら、各ページの description・OGP と、トップの JSON-LD もあわせて直します。
  ・「準備中」の点線の枠は、後から内容を置く場所の目印です。内容が決まったら枠ごと差し替えます。
  ・押せるもの（リンク・ボタン）だけに立体の影と矢印を付けます。押せないカードは平らな枠にします。
  ・来場者向けの情報は「当日の楽しみ方」に集め、ブース・出店とステージ・出演のページは出店者・出演者向けにします。
  ・未確定の内容は「予定」「準備中」「検討中」「公開予定」の文字ラベルを付け、確定した表現にしません。
  ・用語：出店・出演（ブースを出す／ステージに出る）、来場（当日立ち寄る）、出場（大会の一般参加者を募る場合）。
    「参加」は基本的に使わない。「BINGOの参加方法」「参加型ステージ」のような使い方だけ可。
  ・内部の検討状況や交渉中の情報は書きません（このリポジトリは公開されています）。

■ 連絡先
  メール chocotcha.festa@gmail.com ／ 公式Instagram @chocotcha_festa（変更時は index・join・faq・contact と JSON-LD を直す）

■ 外部サービス
  Google Search Console：各ページ head の google-site-verification タグで所有権を確認
  Cloudflare Web Analytics：各ページ </body> 直前のスニペット（Cookie不使用）。contact.html の個人情報欄に利用の旨を記載
  Google アナリティクス（GA4）：測定ID G-MVPER0MPET。tools/build.py の GA_ID で出力。main.js がリンクのクリック
    （click_mail / click_instagram / click_map / go_apply / click_outbound）をイベントとして送る
  Bing Webmaster Tools：Search Console からインポートで登録済み（サイトマップも取り込み済み）
  GA4 と Search Console：GA4「サービス間のリンク」で連携済み（2026-10-29）
  目印付きURL（UTM）：Instagram プロフィール用 ?utm_source=instagram&utm_medium=profile&utm_campaign=festa2027
    チラシQR用 join.html?utm_source=flyer&utm_medium=qr&utm_campaign=festa2027

■ 決まったら差し替えるところ
  ・募集要項と専用申込フォームのリンク（join.html、booth.html、timetable.html）
  ・タイムテーブル、出店者、出演団体
  ・会場範囲・案内図・駐車場（access.html）
  ・個人情報の詳しい取扱い（contact.html）
