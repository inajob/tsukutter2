tsukutter2
==========

web service list

みんなの作ったwebサービスの一覧を作るプロジェクトです

pull requestベースでサービスを追加していく運用です。

ページを見る
===========
http://inajob.github.io/tsukutter2/index.html


追加方法
==========
raw_dataにサービスの紹介用のテキストを追加してpull requestをください
例)
animecheck_v1.txt
```
animecheck
@ina_ani
http://animecheck.herokuapp.com/
見ているアニメを履修登録!
```
現状 サービス名_v1.txt というファイル名を期待しています
（v1は書式のバージョンです、ゆくゆく変わるかもなので）

pull requestがとりこまれた時点でページに反映されます。

todo
==========
- twitterのbotと連動
- RSSの出力
- ページのスタイルを綺麗に
