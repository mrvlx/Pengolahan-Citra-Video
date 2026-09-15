import cv2
import numpy as np

im = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)
r = np.arange(256, dtype=np.float64) # semua kemungkinan nilai masukan

# ----------- 1. Negatif -----------
lut_negatif = (255 - r)

# ----------- 2. Logaritmik -----------
c = 255.0 / np.log(256.0) # agar r=255 dipetakan tepat ke 255
lut_log = c * np.log(1.0 + r)

# ----------- 3. Gamma -----------
def lut_gamma(gamma):
    return np.power(r / 255.0, gamma) * 255.0

def lut_stretch(r1=80, s1=20, r2=175, s2=240):
    out = np.empty(256, dtype=np.float64)
    bagian1 = r < r1
    bagian2 = (r >= r1) & (r < r2)
    bagian3 = r >= r2
    out[bagian1] = (s1 / r1) * r[bagian1]
    out[bagian2] = (s2 - s1) / (r2 - r1) * (r[bagian2] - r1) + s1
    out[bagian3] = (255 - s2) / (255 - r2) * (r[bagian3] - r2) + s2
    return out

def rapikan(lut):
    """Bulatkan setengah ke atas, potong ke 0..255, jadikan uint8."""
    return np.clip(np.floor(lut + 0.5), 0, 255).astype(np.uint8)

# Penerapan: satu pencarian tabel untuk seluruh citra
hasil_negatif = cv2.LUT(im, rapikan(lut_negatif))
hasil_log = cv2.LUT(im, rapikan(lut_log))
hasil_gamma = cv2.LUT(im, rapikan(lut_gamma(0.4)))
hasil_stretch = cv2.LUT(im, rapikan(lut_stretch()))

# Thresholding sudah disediakan OpenCV
_, hasil_biner = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)