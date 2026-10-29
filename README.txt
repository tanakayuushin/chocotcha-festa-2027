やまぐちチョコっちゃ‼フェスタ 2027 公式サイト

■ 公開URL
  https://chocotcha.jp/ （独自ドメイン。リポジトリ直下の CNAME で設定）
  https://tanakayuushin.github.io/chocotcha-festa-2027/ は上のURLへ転送されます。
  GitHub Pages（ブランチ main ／ フォルダ root）で公開しています。

■ ページ構成
  index.html      トップ（開催状態・目的別の入口・概要・楽しみ方・お知らせ）
  enjoy.html      当日の楽しみ方（来場を考えている方へ）
  timetable.html  ステージ・出演（出演したい方へ）
  booth.html      出店したい方へ
  join.html       出店・出演の申込み・料金（相談・正式申込み・流れ・日程）
  access.html     会場・アクセス
  faq.html        よくある質問
  contact.html    お問い合わせ・協力（主催・窓口・協賛の相談・個人情報について）
  style.css       共通のデザイン
  main.js         メニュー開閉・カウントダウン・スクロール演出
  画像            ロゴ・OGP画像・アイコンはリポジトリ直下に置いています

■ 更新するときの注意
  ・ヘッダー、開催状態の帯、フッターは全ページ共通です。変えるときは8ページすべてをそろえます。
  ・最終更新日は、開催状態の帯とフッターの両方にあります。
  ・style.css と main.js は「?v=日付」を付けて読み込んでいます。中身を変えたら全ページの日付も変えると、
    閲覧者のブラウザに古いデザインが残りにくくなります。
  ・日時・会場・料金を変えたら、各ページの description・OGP と、トップの JSON-LD もあわせて直します。
  ・「準備中」の点線の枠は、後から内容を置く場所の目印です。内容が決まったら枠ごと差し替えます。
  ・未確定の内容は「予定」「準備中」「検討中」「公開予定」の文字ラベルを付け、確定した表現にしません。
  ・用語：出店・出演（ブースを出す／ステージに出る）、来場（当日立ち寄る）、出場（大会の一般参加者を募る場合）。
    「参加」は基本的に使わない。「BINGOの参加方法」「参加型ステージ」のような使い方だけ可。
  ・内部の検討状況や交渉中の情報は書きません（このリポジトリは公開されています）。

■ 連絡先
  メール chocotcha.festa@gmail.com ／ 公式Instagram @chocotcha_festa（変更時は index・join・faq・contact と JSON-LD を直す）

■ 外部サービス
  Google Search Console：各ページ head の google-site-verification タグで所有権を確認
  Cloudflare Web Analytics：各ページ </body> 直前のスニペット（Cookie不使用）。contact.html の個人情報欄に利用の旨を記載

■ 決まったら差し替えるところ
  ・募集要項と専用申込フォームのリンク（join.html、booth.html、timetable.html）
  ・タイムテーブル、出店者、出演団体
  ・会場範囲・案内図・駐車場（access.html）
  ・個人情報の詳しい取扱い（contact.html）
