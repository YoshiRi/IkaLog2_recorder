import cv2
import numpy as np
import matplotlib.pyplot as plt

from get_histgram import *

cap = cv2.VideoCapture('../2020-11-24 21-14-00.mp4')

colors = []

while cap.isOpened():
    try:
        ret, frame = cap.read()
        modecolors = extract_modecolor(frame)
        colors.append(modecolors)
    except Exception as e:
        print(e)
        break