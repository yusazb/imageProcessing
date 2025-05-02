import cv2 as cv
import numpy as np
from PIL import Image, ImageTk


# Adaptif Eşikleme Fonksiyonu
def adaptif_esikleme_uygula(resim_cv, panel):
    if resim_cv is None:
        return

    pencere_boyutu = 11
    C = 15

    # Görüntüyü gri tonlamaya çeviriyoruz
    gri = cv.cvtColor(resim_cv, cv.COLOR_RGB2GRAY)
    height, width = gri.shape
    sonuc = gri.copy()  # Sonuç görüntüsünü kopyalıyoruz
    offset = pencere_boyutu // 2

    for y in range(height):
        for x in range(width):
            toplam = 0
            sayac = 0
            for dy in range(-offset, offset + 1):
                for dx in range(-offset, offset + 1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        toplam += int(gri[ny, nx])  # Taşma olmaması için int'e çevir
                        sayac += 1
            # Lokal ortalamayı hesaplıyoruz
            lokal_ortalama = toplam // sayac
            # Eşik değerini hesaplıyoruz
            esik = int(lokal_ortalama) - C
            # Eşik değerine göre piksel değeri atıyoruz
            sonuc[y, x] = 255 if gri[y, x] > esik else 0

    # Sonuç görüntüsünü RGB'ye dönüştürüp PIL formatında kaydediyoruz
    sonuc_rgb = cv.cvtColor(sonuc, cv.COLOR_GRAY2RGB)
    sonuc_pil = Image.fromarray(sonuc_rgb)  # PIL formatına dönüştür

    # Tkinter için uygun formata dönüştürüyoruz
    sonuc_tk = ImageTk.PhotoImage(sonuc_pil)

    # Paneli güncelliyoruz
    panel.configure(image=sonuc_tk)
    panel.image = sonuc_tk


# Sobel Kenar Algılama Fonksiyonu
def sobel_elle(resim_cv, panel):
    # RGB resmi griye çevir
    gri = np.dot(resim_cv[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)

    # Sobel çekirdeklerini tanımla
    Gx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

    Gy = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])

    h, w = gri.shape
    kenar = np.zeros((h - 2, w - 2), dtype=np.uint8)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            bolge = gri[i - 1:i + 2, j - 1:j + 2]
            gx = np.sum(Gx * bolge)
            gy = np.sum(Gy * bolge)
            deger = min(255, int((gx ** 2 + gy ** 2) ** 0.5))
            kenar[i - 1, j - 1] = deger

    # Tek kanalı tekrar RGB'ye çevir (panelde göstermek için)
    kenar_rgb = np.stack((kenar,) * 3, axis=-1)

    # Kenar resmini panelde göster
    kenar_pil = Image.fromarray(kenar_rgb)  # NumPy dizisinden PIL resmine dönüştür
    kenar_tk = ImageTk.PhotoImage(kenar_pil)

    # Paneli güncelliyoruz
    panel.configure(image=kenar_tk)
    panel.image = kenar_tk


# Resmi gösterme fonksiyonu
def resmi_goster(resim_cv, panel):
    if resim_cv is None:
        return

    # Resmi RGB formatına dönüştür
    resim_rgb = cv.cvtColor(resim_cv, cv.COLOR_BGR2RGB)
    resim_pil = Image.fromarray(resim_rgb)  # PIL formatına dönüştür

    # Tkinter için uygun formata dönüştürüyoruz
    resim_tk = ImageTk.PhotoImage(resim_pil)

    # Paneli güncelliyoruz
    panel.configure(image=resim_tk)
    panel.image = resim_tk

def mean_filtre(resim_cv, kernel_boyutu=3):
    pad = kernel_boyutu // 2
    resim_pad = cv.copyMakeBorder(resim_cv, pad, pad, pad, pad, cv.BORDER_REFLECT)
    sonuc = np.zeros_like(resim_cv)

    for y in range(pad, resim_pad.shape[0] - pad):
        for x in range(pad, resim_pad.shape[1] - pad):
            for c in range(3):  # RGB kanalları
                komsu = resim_pad[y-pad:y+pad+1, x-pad:x+pad+1, c]
                sonuc[y-pad, x-pad, c] = np.mean(komsu)
    return sonuc
def median_filtre(resim_cv, kernel_boyutu=3):
    pad = kernel_boyutu // 2
    resim_pad = cv.copyMakeBorder(resim_cv, pad, pad, pad, pad, cv.BORDER_REFLECT)
    sonuc = np.zeros_like(resim_cv)

    for y in range(pad, resim_pad.shape[0] - pad):
        for x in range(pad, resim_pad.shape[1] - pad):
            for c in range(3):
                komsu = resim_pad[y-pad:y+pad+1, x-pad:x+pad+1, c]
                sonuc[y-pad, x-pad, c] = np.median(komsu)
    return sonuc

def salt_pepper_gurultu_ekle(resim_cv, oran=0.02):
    gürültülü = resim_cv.copy()
    satir, sutun, kanal = gürültülü.shape
    toplam_piksel = satir * sutun

    tuz_sayi = int(toplam_piksel * oran / 2)
    karabiber_sayi = int(toplam_piksel * oran / 2)

    # Tuz (beyaz noktalar)
    for _ in range(tuz_sayi):
        y = np.random.randint(0, satir)
        x = np.random.randint(0, sutun)
        gürültülü[y, x] = [255, 255, 255]

    # Karabiber (siyah noktalar)
    for _ in range(karabiber_sayi):
        y = np.random.randint(0, satir)
        x = np.random.randint(0, sutun)
        gürültülü[y, x] = [0, 0, 0]

    return gürültülü
