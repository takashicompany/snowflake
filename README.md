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

### 3. XIAO RP2040の取り付け

キーボードの頭脳部分(MCU)としてXIAO RP2040を取り付けます。　　
取付箇所は表面奥側です。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7228.jpg?raw=true" width = "600px" />

基板のハンダ付け箇所とXIAO RP2040のハンダ付け箇所を重ねます。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7229.jpg?raw=true" width = "600px" />

1箇所ずつハンダ付けをしていきます。  
ズレないように注意しながら進めると手戻りやミスが少なくなります。
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7230.jpg?raw=true" width = "600px" />

全部で14箇所をハンダ付けします。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7232.jpg?raw=true" width = "600px" />

### 4. ファームウェアの書き込み

[KMK Firmware](https://github.com/KMKfw/kmk_firmware)を用いる場合です。  

[こちら](http://kmkfw.io/docs/Getting_Started/)のKMK Firmwareの導入手順も併せて読むと理解が深まると思います。

[こちら](https://circuitpython.org/board/seeeduino_xiao_rp2040/)から.uf2ファイルをダウンロードします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/47f0223c-b40d-4b95-8516-b403834db523" width = "600px" />

XIAO RP2040のUSB口とは反対側にある「B」と書かれたスイッチを押しながらUSBケーブルを差します。  
「RPI-RP2」という名前の外部デバイスが表示されれば成功です。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7233.jpg?raw=true" width = "600px" />

ダウンロードした.uf2を「RPI-RP2」に書き込みます。ドラッグアンドドロップかコピーペーストで書き込めます。  
書き込み完了後、「CIRCUITPY」という名前の外部デバイスが表示されれば成功です。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/1edcd0e8-89cb-49ea-af4f-ae5e574fdd37" width = "600px" />

[KMK Firmwareのソースコードのzip](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip)をダウンロードします。  
解凍後、フォルダ内の`boot.py`と`kmkフォルダ`をCIRCUITPYにドラッグアンドドロップ or コピーペーストします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/7f36a17a-5073-4edc-b0dd-3008e8e5ef75" width = "600px" />

[code.py](https://github.com/takashicompany/snowflake/blob/master/firmware/kmk/code.py)をダウンロード、またはコピーしてCIRCUITPYにドラッグアンドドロップ　or ペーストをします。  
<img src = "https://github.com/takashicompany/monokey/assets/4215759/0bfe6c1c-1bc5-4667-b853-cea94f43abf7" width = "600px" />

ピンセットなどでキースイッチ穴を通電させてキーが入力されるかを確認します。  
正しく入力されていない場合、XIAO RP2040と基板のハンダ付けか、ダイオードのハンダ付けに問題がある可能性が高いです。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7234.jpg?raw=true" width = "600px" />

### 5. スイッチプレートの加工と取り付け

Snowflake基板はニッパーで加工することでスイッチプレートとして利用することが可能です。  
キースイッチがより強固に固定される利点や厚みのあるデザインといった変化があります。  
動作に必須な項目ではありませんので、スキップしていただいても構いません。
（尚、後でスイッチプレートを取り付けたい…となるとハンダ付けを吸い取るといった作業が必要になります）

**ダイオード等を取り付けた基板では"ない"ものを使ってください！**  
つまり、無加工の基板を使います。

ニッパーでキースイッチ取付部部にある点線を切り取ります。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7242.jpg?raw=true" width = "600px" />

点線の2箇所をニッパーで切るとキースイッチ取付部分を切り離すことができます。  
もし、切り離せない場合は裏面からもニッパーで切ると切り離しやすくなります。  
切り離した際にキースイッチ取り付け部分が勢いよく飛ぶことがありますので、ご注意ください。
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7244.jpg?raw=true" width = "600px" />

キースイッチが挿せるかを確認します。  
キースイッチは基板の表側から挿します。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7245.jpg?raw=true" width = "600px" />

全ての穴にキースイッチが挿せることを確認します。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7246.jpg?raw=true" width = "600px" />

スイッチプレートと回路プレート(ダイオードの取り付けをしたプレート)の取り付けにはM2ネジとM2スペーサーを用います。
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7247.jpg?raw=true" width = "600px" />

回路プレートの表側にあるネジ穴の上にスペーサーを置いて、裏側からネジでスペーサーを固定してください。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7248.jpg?raw=true" width = "600px" />

全部で5箇所にスペーサーを取り付けます。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7250.jpg?raw=true" width = "600px" />

スイッチプレートのネジ穴と回路プレートのスペーサーのネジ穴の位置が合うように重ねてネジで固定します。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7252.jpg?raw=true" width = "600px" />

### 6. キースイッチのハンダ付け

キースイッチを取り付けます。キースイッチは基板の表側に載せます。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7238.jpg?raw=true" width = "600px" />

**スイッチプレートを取り付けていない場合**  
キースイッチを基板の表面に載せます。
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7238.jpg?raw=true" width = "600px" />

ハンダ付けは裏返して行うので、マスキングテープなどで固定すると楽に作業が進められます。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7239.jpg?raw=true" width = "600px" />

---

回路プレートの裏側からキースイッチの足が2本出ていることを確認します。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7254.jpg?raw=true" width = "600px" />

回路プレートとキースイッチの足をハンダ付けします。全部で13箇所です。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7255.jpg?raw=true" width = "600px" />

### 6. 滑り止めシールの貼り付け

底面に滑り止めとしてゴム足シールを貼ります。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7256.jpg?raw=true" width = "600px" />

取付箇所が狭い場合はゴム足シールを半分に切るなどしてください。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7257.jpg?raw=true" width = "600px" />

取付箇所の例は以下になります。  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7258.jpg?raw=true" width = "600px" />

### 7. キーキャップを取り付ける

キースイッチにキーキャップを取り付けて完成です！  
<img src = "https://github.com/takashicompany/snowflake/blob/master/images/build/IMG_7263.jpg?raw=true" width = "600px" />

### 8. 完成した後の楽しみ方

完成しましたら、ぜひSNSなどに写真を投稿頂ければと思います。
Twitterのハッシュタグは [`#SnowflakeMacroPad #自作キーボード`](https://twitter.com/search?q=%23%E8%87%AA%E4%BD%9C%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89%20%23SnowflakeMacroPad&src=typed_query) を付けていただけると幸いです。
キットを組み立てた感想や、キーボードを使った所感などをお待ちしております！

また、毎週日曜日の１9時より実施されている[#KEEP_PD](https://twitter.com/hashtag/KEEB_PD?f=live)に投稿頂くこともオススメです。  
開催の告知は[@KEEB_PD](https://twitter.com/KEEB_PD)にて行われております。

ご不明な点などございましたら、[@takashicompany](https://twitter.com/takashicompany)にメンションやDM頂ければ回答できるかと思います。

<!--
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

-->
