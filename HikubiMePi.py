import cv2
import numpy as np

image = cv2.imread('image.png')
scale = 0.5
image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
zeros = np.zeros(gray.shape, dtype=np.uint8)

hijau = cv2.merge([zeros, gray, zeros])
kuning = cv2.merge([zeros, gray, gray])
biru = cv2.merge([gray, zeros, zeros])
merah = cv2.merge([zeros, zeros, gray])
pink = cv2.merge([gray, zeros, gray])

combine = cv2.hconcat([hijau, kuning, biru, merah, pink])

cv2.imshow('Filter Gambar 5 Warna', combine)
cv2.waitKey(0)
cv2.destroyAllWindows()