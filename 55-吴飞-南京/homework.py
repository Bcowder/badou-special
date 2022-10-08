import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('husky.jpg', 1)
# 颜色转换-接口
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 颜色转换-非接口 Gray = R*0.299 + G*0.587 + B*0.114
img2 = (img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.299).astype(np.uint8)
# 二值化
img3 = np.where(img1 >= 124, 255, 0).astype(np.uint8)

plt.subplot(221), plt.imshow(img1, cmap='gray')
plt.subplot(222), plt.imshow(img2, cmap='gray')
plt.subplot(223), plt.imshow(img3, cmap='gray')
plt.show()

# cv2.imshow('img', img)
# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.waitKey()
# cv2.destroyAllWindows()