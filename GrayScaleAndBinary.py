import cv2
import numpy as np
import os
# 画像の読み込み
def grayScaleAndBinary(inputImgPath):
    image = cv2.imread(inputImgPath)

    # グレースケール変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # グレースケール画像の表示
    # cv2.imshow('Gray Image', gray_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 編集した画像を保存する
    imgName =os.path.basename(inputImgPath)
    imgName =imgName.split('.')
    filename ="../画像保存先/" +imgName[0]  + "_grayScale.jpg"
    #print(filename)
    cv2.imwrite(filename, gray_image)
    print("gray OK",end=" , ")

    # 2値化
    ret,binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY) #cv2.threshold は二つの出力を返す

        
    # 2値化画像の表示
    # cv2.imshow('Binary Image', binary_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    filename ="../画像保存先/" +imgName[0]  + "_binary.jpg"
    #print(filename)
    cv2.imwrite(filename, binary_image)
    print("Binary OK")

if __name__ == "__main__":
    grayScaleAndBinary("0220kenya-002.jpg")
    
