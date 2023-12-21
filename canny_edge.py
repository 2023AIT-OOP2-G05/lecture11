import cv2

def edge():
    gray_img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

    threshold1 = 100
    threshold2 = 200
    edge_img = cv2.Canny(gray_img, threshold1, threshold2)
    cv2.imwrite('sample_edge.jpg', edge_img)

if __name__ == "__main__":
    app = edge()
    app.run()