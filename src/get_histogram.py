import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_img(path):
    img = cv2.imread(path)
    b, g, r = img[:,:,0], img[:,:,1], img[:,:,2]
    hist_b = cv2.calcHist([b],[0],None,[256],[0,256])
    hist_g = cv2.calcHist([g],[0],None,[256],[0,256])
    hist_r = cv2.calcHist([r],[0],None,[256],[0,256])
    plt.plot(hist_r, color='r', label="r")
    plt.plot(hist_g, color='g', label="g")
    plt.plot(hist_b, color='b', label="b")
    plt.legend()
    plt.show() 
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = img2[:,:,0], img2[:,:,1], img2[:,:,2]
    hist_h = cv2.calcHist([h],[0],None,[256],[0,256])
    hist_s = cv2.calcHist([s],[0],None,[256],[0,256])
    hist_v = cv2.calcHist([v],[0],None,[256],[0,256])
    plt.plot(hist_h, color='r', label="h")
    plt.plot(hist_s, color='g', label="s")
    plt.plot(hist_v, color='b', label="v")
    plt.legend()
    plt.show()

def show_colortile(h_color,winmsg="mode color"):
    hsv = np.ones((100, 100, 3), dtype="uint8")
    hsv[:,:,0] = int( h_color )
    hsv[:,:, 1] = 255
    hsv[:,:, 2] = 255
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow(winmsg, bgr)
    cv2.waitKey(100)


def mask_modecolor(img):
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = img2[:,:, 0], img2[:,:, 1], img2[:,:, 2]
    histbin = 32
    histwid = 256/histbin
    hist_h = cv2.calcHist([h], [0], None, [histbin], [0, 256])
    maxhs = np.argsort(-hist_h.reshape(-1))
    print(maxhs)
    maxh = maxhs[0]
    plt.plot(hist_h, color='r', label="h")
    plt.show()

    show_colortile((maxh+0.5) * histwid)
    show_colortile((maxhs[1]+0.5) * histwid,"2nd")
    
    mask = (img2[:,:, 0] >= maxh * histwid) * (img2[:,:, 0] < (maxh + 1) * histwid)*1.0
    print(mask)
    cv2.imshow("mask", mask)
    cv2.imshow("orig", img)

    cv2.waitKey(0)
    

# 彩度が低い箇所をフィルタリングする
def extract_modecolor(bgrimg,histbin = 32,showcolortile=False):
    hsvimg = cv2.cvtColor(bgrimg, cv2.COLOR_BGR2HSV)
    h, s, v = hsvimg[:,:, 0], hsvimg[:,:, 1], hsvimg[:,:, 2]
    histwid = 256 / histbin
    assert isinstance(histbin, int), print("histbin must be power of 2")
    hist_h = cv2.calcHist([h], [0], None, [histbin], [0, 256])
    maxhs = np.argsort(-hist_h.reshape(-1))
    maxh = maxhs[0]
    if showcolortile:
        show_colortile((maxh + 0.5) * histwid)
    # return top 3 colors
    return [(maxhs[0] + 0.5) * histwid,(maxhs[1] + 0.5) * histwid,(maxhs[2] + 0.5) * histwid]


if __name__ == "__main__":
    img = cv2.imread("ours_m.png")
    img = cv2.imread("theirs_m.png")

    mask_modecolor(img)
    #show_img("ours_m.png")