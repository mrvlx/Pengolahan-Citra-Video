import cv2
import numpy as np

image = cv2.imread('rektorat.png')
scale = 0.2
image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
zeros = np.zeros(gray.shape, dtype=np.uint8)

biru = cv2.merge([gray, zeros, zeros])
hijau = cv2.merge([zeros, gray, zeros])
merah = cv2.merge([zeros, zeros, gray])

combine = cv2.hconcat([biru, hijau, merah])
cv2.imshow('Filter Gambar RGB', combine)
cv2.waitKey(0)
cv2.destroyAllWindows()
