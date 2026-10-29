サイト生成ツール

■ build.py … 8ページのHTMLを生成する（正本）
  使い方：リポジトリ直下で  python3 tools/build.py .
  ・文面・リンク・準備中の枠・meta・JSON-LD はすべてこのファイルの中にあります。
  ・HTMLを直接編集せず、build.py を直してから生成してください（直接編集すると次の生成で消えます）。
  ・更新日は UPD_ISO / UPD_JA / UPD_DOT、CSS・JSの版は VER を変えます。

■ make_ogp.py … SNS共有画像 ogp.png（1200×630）を生成する
  使い方：リポジトリ直下で  python3 tools/make_ogp.py ogp.png
  ・tools/fonts/ に次の4ファイルが必要です（Google Fonts の配信ファイル。リポジトリには含めていません）
      Dela.ttf   = Dela Gothic One Regular
      Zen500.ttf = Zen Maru Gothic Medium
      Zen700.ttf = Zen Maru Gothic Bold
      Zen900.ttf = Zen Maru Gothic Black
    取得例：https://fonts.googleapis.com/css2?family=Dela+Gothic+One&family=Zen+Maru+Gothic:wght@500;700;900 のCSSに書かれた url(...) をダウンロード
  ・Pillow が必要です（pip install pillow）

■ 公開の流れ
  1. 作業ブランチで build.py を直して生成し、ローカルで表示確認（python3 -m http.server）
  2. 横はみ出し（PC/390px/320px）、内部リンク、JavaScript無効時の本文表示、メニューのEscape動作を確認
  3. 作業ブランチにコミット・push
  4. オーナーの承認後、main に同じファイルを取り込んでpush（GitHub Pages が自動で公開）
