import cv2
import os
# 画像の読み込み
def mozaiku(inputImgPath):
    image = cv2.imread(inputImgPath)

    # Haar Cascade 分類器の読み込み
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 顔検出
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 検出された顔にモザイクを適用
    for (x, y, w, h) in faces:
        # 顔領域の切り抜き
        face_roi = image[y:y+h, x:x+w]

        # 顔領域にモザイクを適用
        face_roi = cv2.GaussianBlur(face_roi, (99, 99), 30)
        image[y:y+h, x:x+w] = face_roi

    # 結果の表示
    #cv2.imshow('Mosaic Faces', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
        
    # 編集した画像を保存する
    imgName =os.path.basename(inputImgPath)
    imgName =imgName.split('.')
    filename ="../画像保存先/" +imgName[0]  + "_faceMozaiku.jpg"
    #print(filename)
    cv2.imwrite(filename, image)
    print("faceMozaiku OK")
if __name__ == "__main__":
    mozaiku("0220kenya-002.jpg")
    