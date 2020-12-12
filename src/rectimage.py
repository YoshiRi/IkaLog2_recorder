import cv2
import numpy as np


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
    
def crop_hcenter(img, rw1_, rw2_, rh):
    try:
        hei, wid, col = img.shape
        print(hei,wid)
    except:
        print("input should be color image!")
        return []

    cy, cx = hei / 2, wid / 2
    if rh > 0.5 or rh < 0:
        print("width rate must between 0 to 0.5!")
        return []
    
    rw1 = max(rw1_, rw2_)
    rw2 = min(rw1_, rw2_)
    
    if rw1 > 1 or rw2 < 0:
        print("height rate must between 0 to 1!")
        return []
    return img[int(cy - rh * hei):int(cy + rh * hei),int(rw2 * wid):int(rw2 * wid + rw1 * wid) ,:]


def crop_whrate(img, rw1_, rw2_, rh1_, rh2_):
    try:
        hei, wid, col = img.shape
        print(hei,wid)
    except:
        print("input should be color image!")
        return []

    cy, cx = hei / 2, wid / 2

    rh1 = max(rh1_, rh2_)
    rh2 = min(rh1_, rh2_)    
    if rh1 > 1 or rh2 < 0:
        print("height rate must between 0 to 1!")
        return []

    rw1 = max(rw1_, rw2_)
    rw2 = min(rw1_, rw2_)    
    if rw1 > 1 or rw2 < 0:
        print("height rate must between 0 to 1!")
        return []
    
    return img[int(rh2 * hei):int(rh2 * hei + rh1 * hei),int(rw2 * wid):int(rw2 * wid + rw1 * wid) ,:]



img1 = cv2.imread("ikaimg1.png")

hei, wid, _ = img1.shape
cy, cx = hei / 2, wid / 2


#cimg = crop_wcenter(img1, 0.25, 0.12 ,0.14)
cimg = crop_whrate(img1, 0.3, 0.45 ,0.02, 0.08)

cv2.imshow("cropped",cimg)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite("save.png",cimg)