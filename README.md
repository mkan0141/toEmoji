# toEmoji
与えられた日本語文をそれらしい絵文字だけの文に変換するコンソールアプリケーション  
<img src="./image/sample.png" alt="demo" title="demo">

## Description
入力された日本語文を形態素解析し、意味のある単語を抽出する。  
そして、抽出された単語と絵文字と意味の一対一表を用いて類似度の最も高かった絵文字を出力して文章を生成します。

モデルも公開したいのですが容量が大きくて公開できませんでした...。対策を考えているところです。

## Install 
```txt
$ git clone https://github.com/mkan0141/toEmoji
```


モデルの作り方はこのサイトを参考にしました  
[【Python】Word2Vecの使い方](https://qiita.com/kenta1984/items/93b64768494f971edf86)

