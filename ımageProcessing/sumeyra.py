import numpy as np
import tk
from PIL import Image, ImageTk
import cv2 as cv

def rgb_to_grayscale_manual(resim_cv, panel):
    if resim_cv is None:
        return

    # BGR → RGB dönüşümü (cv2 BGR kullanır)
    rgb = resim_cv[:, :, ::-1].astype(np.float32)

    # Grayscale dönüşümü: Y = 0.299*R + 0.587*G + 0.114*B
    gri = (0.299 * rgb[:, :, 0] + 0.587 * rgb[:, :, 1] + 0.114 * rgb[:, :, 2]).astype(np.uint8)

    # Grayscale görüntüyü tekrar 3 kanallı yap (panelde gösterim için)
    gri_3kanal = np.stack((gri,) * 3, axis=-1)

    # Gösterim için PIL ve Tkinter dönüşümleri
    img_pil = Image.fromarray(gri_3kanal)
    img_tk = ImageTk.PhotoImage(img_pil)

    panel.configure(image=img_tk)
    panel.image = img_tk

def resmi_goster(goruntu, panel):
    # OpenCV'den gelen BGR formatındaki resmi RGB'ye çevir
    goruntu_rgb = cv.cvtColor(goruntu, cv.COLOR_BGR2RGB)

    # NumPy array'ini PIL imajına çevir
    pil_goruntu = Image.fromarray(goruntu_rgb)

    # PIL imajını tkinter'in anlayacağı formatta dönüştür
    tk_goruntu = ImageTk.PhotoImage(pil_goruntu)

    # Panel'e resmi yerleştir
    if panel is None:
        panel = tk.Label(panel.master, image=tk_goruntu)
        panel.image = tk_goruntu
        panel.pack(padx=10, pady=10)
    else:
        panel.configure(image=tk_goruntu)
        panel.image = tk_goruntu

    return panel


def histogram_germe(goruntu):
    # Gri tonlamalı görüntüye çevir
    gri_goruntu = cv.cvtColor(goruntu, cv.COLOR_BGR2GRAY)

    # Min ve max piksel değerlerini al
    min_val, max_val = np.min(gri_goruntu), np.max(gri_goruntu)

    # Histogram germe işlemi
    gerilmis_goruntu = ((gri_goruntu - min_val) * (255 / (max_val - min_val))).astype(np.uint8)

    return gerilmis_goruntu
