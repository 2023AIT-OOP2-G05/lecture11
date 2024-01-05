# lecture11
<br />

##　役割分担

| 氏名      | 学籍番号 | 役割                                       |
| --------- | -------- | ------------------------------------------ |
| 都築       |          | トップページおよびファイルのアップロード部分の作成    |
| 今井       |          | アップロード画像や処理済み画像の一覧ページの作成     |
| 伊澤       |          | 画像処理プログラムを通して処理済みの画像を別途保存する仕組みの作成 |
| 高野       |          | アップロードされる画像ファイルを保存するディレクトリを常に監視し続けるプログラムの作成 |
| 田川       |          | 画像処理                                   |
| 山口       |          | 画像処理                                   |
| 杉山       |          | 画像処理                                   |

<br />

##　使⽤するライブラリのバージョン
| ライブラリ          | バージョン  |
| ------------------ | ------------- |

<br />

## ディレクトリの構造

<br />

##　システムの動作確認方法
　　　









## watchdogと画像処理について(高野担当)
### 動作
watchdogMain.pyを起動して、同じ階層に画像を入れます。<br>
そうするとwatchdogが反応して画像処理の各関数を実行します。<br>
処理した後の画像はその一個上の階層の「画像保存先」フォルダに保存されます。<br>

### 注意点
・ `pip install watchdog`をお願いします。 <br>
・watchdogMain.pyの上の階層に「画像保存先」フォルダを作って
ください。<br>
・なんか画像処理のエラーみたいなのが出たらwatchdogMain.pyを
control + C で実行停止し再度実行してください。<br>
・watchdogが意味わからないところを参照し始めたら再起動したら直ります。


