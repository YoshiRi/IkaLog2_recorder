# Splatoon recorder with python

# Development log

## 画像の座標切り抜き

- 残り時間，味方と敵の生存状況 `crop_wcenter(img1, 0.25, 0.02 ,0.1)`

![](src/time_our_their.png)

- ヤグラカウント: `cimg = crop_wcenter(img1, 0.25, 0.12 ,0.14)`

![](src/yagura_count.png)

- マップを開いている時左上に出るやつ：`cimg = crop_whrate(img1, 0, 0.1 ,0, 0.18)`

![](src/MapIcon.png)
