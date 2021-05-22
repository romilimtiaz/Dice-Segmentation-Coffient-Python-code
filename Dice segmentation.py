# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:48:28 2021

@author: Romil
"""

import numpy as np
import cv2
from keras import backend as K
gt=cv2.imread("your ground truth",0)
seg=cv2.imread("predicted image",0)
a = np.where(gt!=255, 1, gt)
a = np.where(gt==255, 0, a)
gt=a
b = np.where(seg!=255, 1, seg)
b = np.where(seg==255, 0, b)
seg=b
k=1
dice = np.sum(seg[gt==k]) *2/ (np.sum(seg) + np.sum(gt))
print(1-dice)