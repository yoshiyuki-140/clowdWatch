# clowdWatch

# KITの学食の食券機前の混雑をなくすためにつくったシステム(Hackit)

# アプローチ

1. カメラから画像を入手
1. 画像から人間を検出
1. 人数を測定して
1. webに混雑状況を表示

> 2と4は凝ったよね。

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


## 今後
- このリポジトリはアーカイブということで私は放置します。
得られたアイデアから想定されるものはなかなか需要があるみたいなので、[clowdWatch-Mk2](https://github.com/yoshiyuki-140/clowdWatch-Mk2) で作るつもりです。