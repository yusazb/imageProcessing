import numpy as np
import cv2 as cv

def resim_ekle(resim1, resim2):
    # Boyutları eşitle
    h, w = resim1.shape[:2]
    resim2 = cv.resize(resim2, (w, h))
    sonuc = cv.add(resim1, resim2)
    return sonuc

def resim_cikar(resim1, resim2):
    # Boyutları eşitle
    h, w = resim1.shape[:2]
    resim2 = cv.resize(resim2, (w, h))
    sonuc = cv.subtract(resim1, resim2)
    return sonuc

def resmi_goster(resim, panel):
    from PIL import Image, ImageTk
    import tkinter as tk

    rgb_resim = cv.cvtColor(resim, cv.COLOR_BGR2RGB) if resim.shape[2] == 3 else resim
    img_pil = Image.fromarray(rgb_resim)
    img_tk = ImageTk.PhotoImage(img_pil)

    panel.configure(image=img_tk)
    panel.image = img_tk

def resim_carp(resim1, resim2):
    if resim1 is None or resim2 is None:
        print("Resimlerden biri eksik!")
        return None

    # İki resmi aynı boyuta getir
    h, w = resim1.shape[:2]
    resim2_resized = cv.resize(resim2, (w, h))

    # Çarpma işlemi (çıkan değerler 255'i geçmesin diye normalize edilir)
    carpim = cv.multiply(resim1.astype(np.float32), resim2_resized.astype(np.float32))
    carpim = np.clip(carpim / 255, 0, 255).astype(np.uint8)

    return carpim

def parlaklik_arttir(resim, faktor=1.2):
    """
    Parlaklık arttırma fonksiyonu.
    resim: Giriş resmi.
    faktor: Parlaklık artış faktörü. 1.0 faktörü resmi değiştirmez.
    """
    if resim is None:
        print("Resim eksik!")
        return None

    # Parlaklık arttırma işlemi
    resim_float = resim.astype(np.float32)
    resim_float *= faktor
    resim_float = np.clip(resim_float, 0, 255)  # Değerlerin 255'i geçmesini engelle
    resim_yeni = resim_float.astype(np.uint8)

    return resim_yeni
def gauss_konvolusyon(resim, kernel_boyutu=5, sigma=1.0):
    kernel = cv.getGaussianKernel(kernel_boyutu, sigma)
    kernel = kernel * kernel.T
    sonuc = cv.filter2D(resim, -1, kernel)
    return sonuc

def resmi_gaussla(resim):
    gauss_resim = gauss_konvolusyon(resim)
    return gauss_resim

