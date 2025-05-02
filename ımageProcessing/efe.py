def gri_donusum(resim_cv):
    height = len(resim_cv)
    width = len(resim_cv[0])
    gri_resim = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            R, G, B = resim_cv[y][x]
            gri = int(0.299 * R + 0.587 * G + 0.114 * B)
            gri_resim[y][x] = gri

    return gri_resim
def resmi_goster(gri_resim, panel):
    height = len(gri_resim)
    width = len(gri_resim[0])

    img = tk.PhotoImage(width=width, height=height)

    for y in range(height):
        for x in range(width):
            gri = gri_resim[y][x]
            renk = f'#{gri:02x}{gri:02x}{gri:02x}'
            img.put(renk, (x, y))

    panel.configure(image=img)
    panel.image = img
def binary_donusum(resim_cv, esik_degeri=128):
    height = len(resim_cv)
    width = len(resim_cv[0])
    binary_resim = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            R, G, B = resim_cv[y][x]
            gri = int(0.299 * R + 0.587 * G + 0.114 * B)
            binary_resim[y][x] = 255 if gri >= esik_degeri else 0

    return binary_resim

import tkinter as tk

def binresmi_goster(binary_resim, panel):
    height = len(binary_resim)
    width = len(binary_resim[0])

    img = tk.PhotoImage(width=width, height=height)

    for y in range(height):
        for x in range(width):
            binary = binary_resim[y][x]
            renk = f'#{binary:02x}{binary:02x}{binary:02x}'
            img.put(renk, (x, y))

    panel.configure(image=img)
    panel.image = img
def donme_ve_goster(resim_cv, panel):
    height = len(resim_cv)
    width = len(resim_cv[0])

    yeni_resim = [[0 for _ in range(height)] for _ in range(width)]

    for y in range(height):
        for x in range(width):
            yeni_resim[x][height - y - 1] = resim_cv[y][x]

    resim_cv = yeni_resim

    img = tk.PhotoImage(width=len(resim_cv[0]), height=len(resim_cv))

    for y in range(len(resim_cv)):
        for x in range(len(resim_cv[0])):
            r, g, b = resim_cv[y][x]
            renk = f'#{r:02x}{g:02x}{b:02x}'
            img.put(renk, (x, y))

    panel.configure(image=img)
    panel.image = img

    return resim_cv  # ← önemli: güncellenmiş resmi geri döndür
