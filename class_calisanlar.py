# sirkete Calisanlar sinifi ve calisanlar listesi



class Calisanlar:
    def __init__(self, isim, soyisim, maas, departman):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim, self.soyisim, self.maas, self.departman))

    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman

    def maas_yukselt(self, zam_miktari):
        self.maas += zam_miktari

class Yonetici(Calisanlar):
    def __init__(self, isim, soyisim, maas, departman, kisi_sayisi):
        super().__init__(isim, soyisim, maas, departman)
        self.kisi_sayisi = kisi_sayisi

    def bilgileri_goster(self):
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\nDepartman: {}\nKisi Sayisi: {}\n".format(self.isim, self.soyisim, self.maas, self.departman, self.kisi_sayisi))

    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari
    
    def kisi_ekle(self, kisi_sayisi):
        self.kisi_sayisi += kisi_sayisi
        
    def kisi_sil(self, kisi_sayisi):
        self.kisi_sayisi -= kisi_sayisi

yonetici = Yonetici("Cem", "Kaya", 50000, "Bilişim", 10)
yonetici.bilgileri_goster()
yonetici.zam_yap(10000)
yonetici.bilgileri_goster()

yonetici2 = Yonetici("Aysem", "Dolandirici", 70000, "Doktor", 21)
yonetici2.bilgileri_goster()
yonetici2.zam_yap(10000)
yonetici2.bilgileri_goster()



