import cv2
def izawa (inputImgPath):
    #画像の読み込み
    #TODO　画像の名前取得
    img = cv2.imread(inputImgPath)
    
    #画像処理
    rows,cols,channels = img.shape
    # 画素から青色を消したい場合は次のように処理する
    for y in range(rows):
        for x in range(cols):
            # 横x縦yの画素のカラーを取得(ここでは8bitRGB)
            b, g, r = img[y, x]
            # もし画素が白色だったな何もしない
            if (b, g, r) == (255, 255, 255):
                continue
            img[y, x] = 0, g, r

    print("OK")
    # 編集した画像を保存する
    #TODO　保存先どうするか
    cv2.imwrite('change_color.png', img)