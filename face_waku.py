import cv2
import os
def face(inputImgPath):
    #画像読み込み
    img = cv2.imread(inputImgPath)
    #グレースケール化
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # 学習済みモデルの読み込み
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # 顔を検出する
    #lists = cascade.detectMultiScale(img_gray, minSize=(100, 100))
    faces = cascade.detectMultiScale(img, scaleFactor=1.1,minNeighbors=5, minSize=(30,30))
    #赤枠処理、表示
    if len(faces):
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
            #cv2.imshow('img', img)
            #cv2.waitKey(0)
    else:
        print('顔Nothing')

    imgName =os.path.basename(inputImgPath)
    imgName =imgName.split('.')
    filename ="../画像保存先/" +imgName[0]  + "_faceRectangle.jpg"
    #print(filename)
    cv2.imwrite(filename, img)
    print("face-waku ok")
if __name__ == "__main__":
    app = face()
    app.run()