import cv2

def line_drawing_image(img):
    # 画像のコントラストを調整
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # ガウシアンブラーを適用
    gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # エッジ検出で線画を生成
    edges = cv2.adaptiveThreshold(gray_blurred, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 7, 6)
    
    return edges

# 画像を読み込む
image_path = 'image/8.png'  # 入力画像のパスを指定
img = cv2.imread(image_path)

if img is None:
    print("画像を読み込めませんでした。")
    exit()

# 線画風の画像を生成
line_drawing = line_drawing_image(img)

# 生成した画像を表示する
cv2.imshow('Line Drawing Image', line_drawing)

# 生成した画像を保存
output_path = 'line_drawing_output.jpg'  # 出力画像のパスを指定
cv2.imwrite(output_path, line_drawing)
print(f'{output_path} を保存しました。')

# 'q'が押されたらウィンドウを閉じる
cv2.waitKey(0)
cv2.destroyAllWindows()
