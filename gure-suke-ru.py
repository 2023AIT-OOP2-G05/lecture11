import cv2
import numpy as np

# 画像の読み込み
def guresukeru():
    image = cv2.imread('IMG_2405.jpg')

    # グレースケール変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # グレースケール画像の表示
    cv2.imshow('Gray Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 2値化
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
        
    # 2値化画像の表示
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    app = guresukeru()
    app.run()
