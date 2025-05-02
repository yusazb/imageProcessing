import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2 as cv
import mertali
import efe
import sumeyra
import burak
import yusuf
def genisleme_fonksiyonu():
    if resim_cv is not None:
        yeni_resim = yusuf.genisleme(resim_cv)
        guncelle_resim(yeni_resim)
        yusuf.goster(yeni_resim, panel, pencere)

def asinma_fonksiyonu():
    if resim_cv is not None:
        yeni_resim = yusuf.asinma(resim_cv)
        guncelle_resim(yeni_resim)
        yusuf.goster(yeni_resim, panel, pencere)

def acma_fonksiyonu():
    if resim_cv is not None:
        yeni_resim = yusuf.acma(resim_cv)
        guncelle_resim(yeni_resim)
        yusuf.goster(yeni_resim, panel, pencere)

def kapama_fonksiyonu():
    if resim_cv is not None:
        yeni_resim = yusuf.kapama(resim_cv)
        guncelle_resim(yeni_resim)
        yusuf.goster(yeni_resim, panel, pencere)

pencere = tk.Tk()
pencere.title("🔍 Görüntü İşleme Arayüzü")
pencere.geometry("1000x700")
pencere.configure(bg="#f0f0f0")

baslik = tk.Label(pencere, text="Görüntü İşleme Uygulaması", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
baslik.pack(pady=20)

frame_buttons_left = tk.Frame(pencere, bg="#f0f0f0")
frame_buttons_left.pack(side="left", padx=20, pady=20)

frame_buttons_right = tk.Frame(pencere, bg="#f0f0f0")
frame_buttons_right.pack(side="right", padx=20, pady=20)

frame_image = tk.Frame(pencere, bd=2, relief="groove", bg="#f0f0f0")
frame_image.pack(side="top", padx=20, pady=20, expand=True)

resim = None
resim_cv = None
diger_resim = None
panel = None
zoom_scale = 1.0

def diger_resmi_sec():
    global diger_resim, panel
    dosya_yolu = filedialog.askopenfilename(filetypes=[("Görüntü Dosyaları", "*.jpg;*.jpeg;*.png")])
    if dosya_yolu:
        img = cv.imread(dosya_yolu)
        diger_resim = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        print("İkinci resim başarıyla yüklendi.")

        # İkinci resmi ekranda göster
        diger_resim_pil = Image.fromarray(diger_resim)
        diger_resim_tk = ImageTk.PhotoImage(diger_resim_pil)

        if panel is None:
            panel = tk.Label(frame_image, image=diger_resim_tk)
            panel.image = diger_resim_tk
            panel.pack(padx=10, pady=10, anchor="center")  # Resmi tam ortada yerleştirmek için anchor="center"
        else:
            panel.configure(image=diger_resim_tk)
            panel.image = diger_resim_tk

def resim_sec():
    global resim, resim_cv, panel
    dosya_yolu = filedialog.askopenfilename(filetypes=[("Görüntü Dosyaları", "*.jpg;*.jpeg;*.png")])
    if dosya_yolu:
        resim_cv = cv.imread(dosya_yolu)
        resim_cv = cv.cvtColor(resim_cv, cv.COLOR_BGR2RGB)
        resim = Image.fromarray(resim_cv)
        resim_tk = ImageTk.PhotoImage(resim)

        if panel is None:
            panel = tk.Label(frame_image, image=resim_tk)
            panel.image = resim_tk
            panel.pack(padx=10, pady=10, anchor="center")  # Resmi tam ortada yerleştirmek için anchor="center"
        else:
            panel.configure(image=resim_tk)
            panel.image = resim_tk

def zoom_image(factor=1.2):
    global resim_cv, panel
    if resim_cv is not None:
        h, w = resim_cv.shape[:2]
        new_w = int(w * factor)
        new_h = int(h * factor)
        resized_image = cv.resize(resim_cv, (new_w, new_h), interpolation=cv.INTER_LINEAR)
        resized_pil = Image.fromarray(resized_image)
        resized_tk = ImageTk.PhotoImage(resized_pil)
        panel.configure(image=resized_tk)
        panel.image = resized_tk

def buton(text, command, row, col, side="left"):
    btn = tk.Button(frame_buttons_left if side == "left" else frame_buttons_right, text=text, command=command,
                    font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
    btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

def resim_kaydet():
    if resim_cv is None:
        print("Önce bir resim seçin!")
        return
    dosya_yolu = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Dosyaları", "*.png"),
                                                                                  ("JPEG Dosyaları", "*.jpg;*.jpeg")])
    if dosya_yolu:
        cv.imwrite(dosya_yolu, cv.cvtColor(resim_cv, cv.COLOR_RGB2BGR))
        print(f"Resim başarıyla kaydedildi: {dosya_yolu}")

def esikleme():
    if resim_cv is not None:
        mertali.adaptif_esikleme_uygula(resim_cv, panel)

def sobel():
    if resim_cv is not None:
        mertali.sobel_elle(resim_cv, panel)

def guncelle_resim(yeni_resim):
    global resim_cv
    resim_cv = yeni_resim


def median_blur():
    if resim_cv is not None:
        # Median Blur işlemi uygula
        yeni_resim = yusuf.median_blur(resim_cv, kernel_size=3)

        # Yeni resmi göster
        guncelle_resim(yeni_resim)
        yusuf.goster(yeni_resim, panel, pencere)


# Buton yerleşiminde her şeyin simetrik olmasını sağlayacak şekilde düzenleme yapalım.

buton("Görüntü Seç", resim_sec, 0, 0, side="left")
buton("Zoom In", lambda: zoom_image(1.2), 1, 0, side="left")
buton("Zoom Out", lambda: zoom_image(0.8), 2, 0, side="left")
buton("Görüntüyü Kaydet", resim_kaydet, 3, 0, side="left")
buton("Eşikleme", lambda: mertali.adaptif_esikleme_uygula(resim_cv, panel), 4, 0, side="left")

# Sağ tarafta işlemleri simetrik olarak düzenliyoruz
buton("Gri Dönüşüm", lambda: efe.resmi_goster(efe.gri_donusum(resim_cv), panel), 5, 0, side="left")
buton("Binary Dönüşüm", lambda: efe.binresmi_goster(efe.binary_donusum(resim_cv), panel), 6, 0, side="left")
buton("90 Döndür", lambda: guncelle_resim(efe.donme_ve_goster(resim_cv, panel)), 7, 0, side="left")
buton("Sobel Elle", lambda: mertali.sobel_elle(resim_cv, panel), 8, 0, side="left")
buton("Gürültü Ekle (Salt&Pepper)", lambda: mertali.resmi_goster(mertali.salt_pepper_gurultu_ekle(resim_cv), panel), 4, 0, side="right")
buton("Mean Filtre", lambda: mertali.resmi_goster(mertali.mean_filtre(resim_cv), panel), 5, 0, side="right")
buton("Median Filtre", lambda: mertali.resmi_goster(mertali.median_filtre(resim_cv), panel), 6, 0, side="right")
buton("RGB - Grayscale", lambda: sumeyra.rgb_to_grayscale_manual(resim_cv, panel), 7, 0, side="right")
buton("Histogram Germe", lambda: sumeyra.resmi_goster(sumeyra.histogram_germe(resim_cv), panel), 8, 0, side="right")
buton("Parlaklık Arttır", lambda: burak.resmi_goster(burak.parlaklik_arttir(resim_cv), panel), 9, 0, side="right")
buton("Resim Ekle", lambda: burak.resmi_goster(burak.resim_ekle(resim_cv, diger_resim), panel), 10, 0, side="right")
buton("Resim Çıkar", lambda: burak.resmi_goster(burak.resim_cikar(resim_cv, diger_resim), panel), 3, 0, side="right")
buton("Resim Çarp", lambda: burak.resmi_goster(burak.resim_carp(resim_cv, diger_resim), panel), 2, 0, side="right")
buton("Gauss Konvolüsyon", lambda: burak.resmi_goster(burak.resmi_gaussla(resim_cv), panel), 1, 0)
buton("2. Resmi Seç", diger_resmi_sec, 13, 0, side="right")
buton("Görüntüyü Kırp", lambda: guncelle_resim(yusuf.goruntu_kirp(resim_cv, panel, pencere)), 12, 0)
buton("Median Blur", lambda: [guncelle_resim(yusuf.median_blur(resim_cv)), yusuf.goster(resim_cv, panel, pencere)], 11, 0, side="right")
buton("Genişleme", genisleme_fonksiyonu, 12, 0)
buton("Aşınma", asinma_fonksiyonu, 12, 1)
buton("Açma", acma_fonksiyonu, 12, 2)
buton("Kapama", kapama_fonksiyonu, 12, 3)






pencere.mainloop()
