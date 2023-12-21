# lecture11

## watchdogと画像処理について(高野担当)
### 動作
watchdogMain.pyを起動して、同じ階層に画像を入れます。<br>
そうするとwatchdogが反応して画像処理の各関数を実行します。<br>
処理した後の画像はその一個上の階層の「画像保存先」フォルダに保存されます。<br>

### 注意点
```
pip install watchdog
```
をお願いします。 
・watchdogMain.pyの上の階層に「画像保存先」フォルダを作って
ください。<br>
・なんか画像処理のエラーみたいなのが出たらwatchdogMain.pyを
control + C で実行停止し再度実行してください。<br>
・watchdogが意味わからないところを参照し始めたら再起動したら直ります。


