# Snowflake

<img src = "https://github.com/takashicompany/snowflake/assets/4215759/8c320ca2-4ae5-4b9f-95d1-6aa8f5166f9e" width = "400px" />

<img src = "https://github.com/takashicompany/snowflake/assets/4215759/fc2945a7-06c2-4ed5-b09b-674e3a9eda9f" width = "400px" />



組み立て手順は[Arrows Plus](https://github.com/takashicompany/arrows_plus/) と同様です。  
キースイッチとキーキャップを13個ご用意ください。  
ファームウェアのソースコードは[こちら](https://github.com/takashicompany/snowflake/blob/master/firmware/kmk/code.py)にございます。  


## 組み立てに必要な部品

キットに含まれていないものはご自身でご用意ください。  

以下は必須の項目の説明です。
|記号|説明|
|:--|:--|
|必須|無いと動作しません。キットに含まれていないものはご自身でご用意ください。|
|推奨|無くても動作させられますが、用意すると組み立てさやメンテナンス性が向上します。初心者の方はご用意頂くのが確実です。|
|自由|使用スタイルに併せて、選択可能です。|

|部品名|個数|必須|キットに同梱|備考|
|:--|:--|:--|:--|:--|
|Snowflake 基板|1|必須|有|回路プレートとして、キースイッチやXIAO RP2040を取り付けます。|
|Snowflake 基板|1|自由|有|加工してスイッチプレートとして取り付けられます。無くても動作に支障はありません。|
|XIAO RP2040|1|必須|無|キー入力をPC等に伝達します。|
|ダイオード(SMD)|13|必須|有|キーの入力を検知するのに必要です。|
|スペーサー(M2 3.5mm)|5|自由|有|回路プレートとキースイッチプレートをネジで繋ぎます。|
|ネジ(M2 3mm)|10|自由|有|スペーサーに取り付けます。|
|キースイッチ(Cherry MX互換)|13|必須|無|押下することでキーの入力が可能です。|
|キーキャップ(Cherry MX軸 1u)|13|必須|無|キースイッチに取り付けます。|
|滑り止めシール|4|推奨|有|底面に貼り付けて押下時に滑らないようにします。|

## 組み立てに必要な道具

何を用意してよいか分からない方は、[こちら](https://shop.yushakobo.jp/products/a9900to)を購入するのが確実です。

|道具|備考|
|:--|:--|
|ハンダごて|おすすめは[HAKKO FX-600](https://www.hakko.com/japan/products/hakko_fx600.html)です。[こて台](https://www.hakko.com/japan/products/hakko_kote_board.html)もあると、より作業をスムーズに進められます。|
|ハンダ|[こちら](https://www.goot.jp/products/detail/se_06008)などを使う方が多いようです。|
|ピンセット|100均などで手に入るものでも充分利用できるかと思います。|
|ニッパー|100均などで手に入るものでも充分利用できるかと思いますが、1000円程度ものを買っても損では無いかと思います。|

## あるとさらに完成度が高くなる道具
|道具|備考|
|:--|:--|
|棒ヤスリ|基板の縁にあるバリを削るのに使います。|
|サインペン|基板の縁を塗るとより美しくなります。|
|マスキングテープ|キースイッチをハンダ付けする際に役立ちます。|

## 組み立て方

### 1. 基板の表裏を確認する

❅のマークが描かれている方が表です。

**表**
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7218.jpg?raw=true" width = "600px" />

**裏**
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7219.jpg?raw=true" width = "600px" />

### 2. ダイオードの取り付け

ダイオードを基板に取り付けます。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7720.jpg?raw=true" width = "600px" />

ダイオードは基板裏面のキースイッチ取付箇所の近くです。  
基板に描かれている`▷|`マークの縦線マークとダイオードに描かれている縦線が同じ方向になるように配置します。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7721.jpg?raw=true" width = "600px" />

予備ハンダをしてダイオードの片側と基板をハンダ付けします。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7772.jpg?raw=true" width = "600px" />

もう片方のダイオードも基板とハンダ付けします。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7223.jpg?raw=true" width = "600px" />

全部で13箇所にダイオードをハンダ付けします。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7224.jpg?raw=true" width = "600px" />

### XIAO RP2040の取り付け

キーボードの頭脳部分(MCU)としてXIAO RP2040を取り付けます。　　
取付箇所は表面奥側です。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7228.jpg?raw=true" width = "600px" />

基板のハンダ付け箇所とXIAO RP2040のハンダ付け箇所を重ねます。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7229.jpg?raw=true" width = "600px" />

1箇所ずつハンダ付けをしていきます。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7230.jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />


<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_ .jpg?raw=true" width = "600px" />

