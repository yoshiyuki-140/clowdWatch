# clowdWatch

# KITの学食の食券機前の混雑をなくすためにつくったシステム(Hackit)

## フォルダの説明
- camera  
    - ここにはデモ用に5秒ごとにwebカメラから画像を取得して'data/dest/image.jpg'に保存するプログラムが入っている
- data  
    - ここは「cameraで取得した画像」&「画像に印をつけたもの(marked.jpg)」&「Yolo3の学習モデル」が入っている.

- demo  
    - デモ用に学食で撮影した、人の多い時の画像と、人の少ない時の画像が入っている

- flaskServer  
    - 'main.py'はflaskサーバーを起動するためのコードなので.
        ```
        $ python main.py
        ```
        とすれば、localhostでサーバーが起動する.
- html
    - index.htmlがlocalhostのルート'/'におかれるhtmlファイル.

## 使い方

- data/yoloFilesへ
    - coco.names
    - yolov3.cfg
    - yolov3.weights
    を配置するhuman detection
