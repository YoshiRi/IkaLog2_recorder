import cv2
import numpy as np


def crop_wcenter(img, rw, rh1_, rh2_):
    try:
        if len(img.shape)==3: 
            hei, wid, col = img.shape
            color = True
        else:
            hei, wid = img.shape
            color = False
    except Exception as e:
        print(e)
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
    if color:
        return img[int(rh2 * hei):int(rh1 * hei), int(cx - rw * wid):int(cx + rw * wid),:]
    else:
        return img[int(rh2 * hei):int(rh1 * hei), int(cx - rw * wid):int(cx + rw * wid)]
      
def crop_hcenter(img, rw1_, rw2_, rh):
    try:
        if len(img.shape)==3: 
            hei, wid, col = img.shape
            color = True
        else:
            hei, wid = img.shape
            color = False
    except Exception as e:
        print(e)
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
    
    if color:
        return img[int(cy - rh * hei):int(cy + rh * hei),int(rw2 * wid):int(rw1 * wid) ,:]
    else:
        return img[int(cy - rh * hei):int(cy + rh * hei),int(rw2 * wid):int(rw1 * wid)]

def crop_whrate(img, rw1_, rw2_, rh1_, rh2_):
    try:
        if len(img.shape)==3: 
            hei, wid, col = img.shape
            color = True
        else:
            hei, wid = img.shape
            color = False
    except Exception as e:
        print(e)
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
    
    if color:
        return img[int(rh2 * hei):int(rh1 * hei),int(rw2 * wid):int(rw1 * wid) ,:]
    else:
        return img[int(rh2 * hei):int(rh1 * hei),int(rw2 * wid):int(rw1 * wid)]


def drawrect(frame,bbox,color=(0,255,0)):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, color, 2, 1)
    return frame


if __name__ == "__main__":
    
    img1 = cv2.imread("ikaimg1.png")
    
    if len(img1.shape)==3: 
        hei, wid, col = img1.shape
    else:
        hei, wid = img1.shape

    #cimg = crop_wcenter(img1, 0.25, 0.12 ,0.14)
    cimg = crop_whrate(img1, 0.28, 0.457 ,0.0268, 0.1037)
    cimg = crop_whrate(img1, 0.543, 0.72 ,0.0268, 0.1037)
    
    cv2.imshow("cropped",cimg)
    key = cv2.waitKey(0)

    if key == ord('s'):
        cv2.imwrite("save.png", cimg)
        exit(0)
    elif key == ord('r'):
        try:
            while 1:
                rect = cv2.selectROI(img1, False)
                print(rect)
                print(rect[0]/wid,rect[0]/wid+rect[2]/wid,rect[1]/hei,rect[1]/hei+rect[3]/hei)
                cv2.imshow("rectimage",drawrect(img1, rect))
                key = cv2.waitKey(0)
                
                if key == ord('q'):
                    exit(0)
        except KeyboardInterrupt:
            exit(0)