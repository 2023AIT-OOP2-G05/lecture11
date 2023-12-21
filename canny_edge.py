import cv2
import os
def edge(inputImgPath):
    gray_img = cv2.imread(inputImgPath, cv2.IMREAD_GRAYSCALE)

    threshold1 = 100
    threshold2 = 200
    edge_img = cv2.Canny(gray_img, threshold1, threshold2)

    # 編集した画像を保存する
    imgName =os.path.basename(inputImgPath)
    imgName =imgName.split('.')
    filename ="../画像保存先/" +imgName[0]  + "_cannyEdge.jpg"
    #print(filename)
    cv2.imwrite(filename, edge_img)
    print("canny_edge OK")
if __name__ == "__main__":
    edge("0220kenya-002.jpg")
    