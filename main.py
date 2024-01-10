from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


@app.route("/picture", methods=["POST"])
def getPicture():

    # ボタン押下の確認メッセージ
    print("送信ボタンが押された")

    # 送られてきたキーが正しいか確認
    if "original-picture" not in request.files:
        print("キーが含まれていません")
        return "Key"
    
    file = request.files['original-picture']

    # ファイルが指定されているか確認
    if file.filename == "":
        print("ファイルが指定されていない")
        return "None"
    
    # ファイルの保存
    # (プロジェクトディレクトリ内のディレクトリ「uploads-picture/」に保存している)
    file.save("uploads-picture/" + file.filename)


# ただアップロードした画像を表示する
@app.route("/picture_list/", methods=["GET"])
def getPictureList():
    # 'uploads-picture/' ディレクトリ内のファイルのリストを取得
    picture_files = os.listdir("uploads-picture/")

    # テンプレートに写真のリストを渡してレンダリング
    return render_template("picture_list.html", picture_files=picture_files)

#-----#

# おそらく、この間に画像処理を挟む？

#-----#
    
    # 保存が成功
    return "Success"
    # getPicture() 関数の終わり


#-----#

# ここに、画像の一覧を表示する @app.route("/") を追加？

#-----#


# Flask CORS
@app.route("/")
def index():

    print("ページが読み込まれました")

    return render_template("Image-Processing.html")

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
    #app.run(host="localhost",port=8888,debug=True)