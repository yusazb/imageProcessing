import tkinter as tk


def orantili_kirp(resim_cv):
    yukseklik, genislik, _ = resim_cv.shape
    baslangic_x = genislik // 4
    baslangic_y = yukseklik // 4
    bitis_x = genislik - baslangic_x
    bitis_y = yukseklik - baslangic_y
    kirpilmis = resim_cv[baslangic_y:bitis_y, baslangic_x:bitis_x]
    return kirpilmis

def resmi_cvden_pile(resim_cv):
    return Image.fromarray(resim_cv)

def goster(resim_cv, panel, pencere):
    img_pil = resmi_cvden_pile(resim_cv)
    img_tk = ImageTk.PhotoImage(img_pil)

    if panel is None:
        panel = tk.Label(pencere, image=img_tk)
        panel.image = img_tk
        panel.pack()
    else:
        panel.configure(image=img_tk)
        panel.image = img_tk

    return panel  # panel'i geri döndürüyoruz

def goruntu_kirp(resim_cv, panel, pencere):
    if resim_cv is not None:
        kirpilmis = orantili_kirp(resim_cv)
        goster(kirpilmis, panel, pencere)
        return kirpilmis
    else:
        print("Önce bir resim seçin.")
        return resim_cv

# Median Blur fonksiyonu
def median_blur(resim_cv, kernel_size=3):
    """
    Median blur işlemi, her pikselin etrafındaki piksellerin medyanını alır.
    kernel_size: 3x3, 5x5 vb. gibi kernel boyutunu belirtir.
    """
    # Resmin boyutlarını al
    yukseklik, genislik, kanal = resim_cv.shape

    # Yeni bir boş resim oluştur
    blur_resim = np.zeros_like(resim_cv)

    # Kernel yarıçapını hesapla
    kucuk_yaricap = kernel_size // 2

    # Görüntü üzerinde her pikseli gez
    for i in range(kucuk_yaricap, yukseklik - kucuk_yaricap):
        for j in range(kucuk_yaricap, genislik - kucuk_yaricap):
            # Komşu pikselleri al (kernel bölgesi)
            kernel = resim_cv[i-kucuk_yaricap:i+kucuk_yaricap+1, j-kucuk_yaricap:j+kucuk_yaricap+1]

            # Her kanal için medyanı hesapla ve blur_resim'e uygula
            for k in range(kanal):
                blur_resim[i, j, k] = np.median(kernel[:, :, k])

    return blur_resim
import cv2
import numpy as np
from PIL import Image, ImageTk


import cv2
import numpy as np

def asinma(img):
    if len(img.shape) == 3:
        gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gri = img

    kernel = np.ones((5, 5), np.uint8)
    sonuc = cv2.erode(gri, kernel, iterations=1)
    return sonuc

def genisleme(img):
    if len(img.shape) == 3:
        gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gri = img

    kernel = np.ones((5, 5), np.uint8)
    sonuc = cv2.dilate(gri, kernel, iterations=1)
    return sonuc

def acma(img):
    if len(img.shape) == 3:
        gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gri = img

    kernel = np.ones((5, 5), np.uint8)
    sonuc = cv2.morphologyEx(gri, cv2.MORPH_OPEN, kernel)
    return sonuc

def kapama(img):
    if len(img.shape) == 3:
        gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gri = img

    kernel = np.ones((5, 5), np.uint8)
    sonuc = cv2.morphologyEx(gri, cv2.MORPH_CLOSE, kernel)
    return sonuc
def goster(img, panel, pencere):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(img_rgb)
    imgtk = ImageTk.PhotoImage(image=im)
    panel.config(image=imgtk)
    panel.image = imgtk
    pencere.update()
