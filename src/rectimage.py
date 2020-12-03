import cv2
import numpy as np

img1 = cv2.imread("ikaimg1.png")

hei, wid, _ = img1.shape
cy, cx = hei / 2, wid / 2

def crop_wcenter(img, rw, rh1_, rh2_):
    try:
        hei, wid, col = img.shape
        print(hei,wid)
    except:
        print("input should be color image!")
        return []

    cy, cx = hei / 2, wid / 2
    if rw > 0.5 or rw < 0:
        print("width rate must between 0 to 0.5!")
        return []
    
    rh1 = max(rh1_, rh2_)
    rh2 = min(rh1_, rh2_)
    
    if rh1 > 1 or rh2 < 0:
        print("height rate must between 0 to 1!")
        return []
    return img[int(rh2 * hei):int(rh2 * hei + rh1 * hei), int(cx - rw * wid):int(cx + rw * wid),:]
    
    
cimg = crop_wcenter(img1, 0.25, 0.12 ,0.14)
cv2.imshow("cropped",cimg)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite("save.png",cimg)