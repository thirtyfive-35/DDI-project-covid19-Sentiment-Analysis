def bosluk_olmayan_satirlari_sil(girdi_dosya, cikti_dosya):
    with open(girdi_dosya, 'r', encoding='utf-8') as okuma_dosyasi:
        satirlar = okuma_dosyasi.readlines()

    yeni_satirlar = [satir for satir in satirlar if ' ' in satir]

    with open(cikti_dosya, 'w', encoding='utf-8') as yazma_dosyasi:
        yazma_dosyasi.writelines(yeni_satirlar)

# Örnek kullanım:
girdi_dosyasi = 'final1.txt'
cikti_dosyasi = 'final2.txt'

bosluk_olmayan_satirlari_sil(girdi_dosyasi, cikti_dosyasi)
