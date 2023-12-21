from flask import Flask, request, render_template, jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

@app.route('/picture')
def getPicture():
    print("画像データを取得")

# http://127.0.0.1:5000/
# Frask CORS
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    #app.run(host="localhost",port=8888,debug=True)
    app.run(debug=True)