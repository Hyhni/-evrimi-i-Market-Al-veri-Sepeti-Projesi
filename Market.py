import os

class Market:
    def __init__(self):
        
        self.dosya_adi = "product.txt"
        if not os.path.exists(self.dosya_adi):
            open(self.dosya_adi, 'w').close()

    def __del__(self):
        print("Program sonlanıyor. Veriler kaydedildi.")

    def urunleri_listele(self):
        with open(self.dosya_adi, 'r') as dosya:
            satirlar = dosya.read().splitlines() 
            if not satirlar:
                return "Ürün bulunmamaktadır."

            sonuc = f"{'No':<5}{'Ürün Adı':<20}{'Kategori':<15}{'Fiyat':<10}{'Stok':<10}\n"
            sonuc += "-" * 60 + "\n"
            for i, satir in enumerate(satirlar):
                urun = satir.split(',')
                sonuc += f"{i+1:<5}{urun[0]:<20}{urun[1]:<15}{urun[2]:<10}{urun[3]:<10}\n"
            return sonuc

    def urun_ekle(self, ad, kategori, fiyat, stok):
        with open(self.dosya_adi, 'a') as dosya:
            dosya.write(f"{ad},{kategori},{fiyat},{stok}\n")

        return "Ürün başarıyla eklendi!"

    def urun_sil(self, secim):
        with open(self.dosya_adi, 'r') as dosya:
            satirlar = dosya.read().splitlines()

        if not satirlar:
            return "Silinecek ürün bulunmamaktadır."

        try:
            secim_numara = int(secim)
            if 0 < secim_numara <= len(satirlar):
                del satirlar[secim_numara - 1]
            else:
                return "Geçersiz ürün numarası."
        except ValueError:
            for i, satir in enumerate(satirlar):
                if secim in satir:
                    del satirlar[i]
                    break
            else:
                return "Ürün bulunamadı."

        with open(self.dosya_adi, 'w') as dosya:
            dosya.write('\n'.join(satirlar) + '\n')

        return "Ürün başarıyla silindi!"

def Menu():
    market = Market()

    while True:
        print("\n>>> MENÜ <<<")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")

        secim = input("Seçiminizi yapın (1-4): ")

        if secim == "1":
            print(market.urunleri_listele())
        elif secim == "2":
            ad = input("Ürün adı (örnek: Elma): ")
            kategori = input("Kategori (örnek: Meyve): ")
            fiyat = input("Fiyat (örnek: 10): ")
            stok = input("Stok miktarı (örnek: 50): ")
            print(market.urun_ekle(ad, kategori, fiyat, stok))
        elif secim == "3":
            secim = input("Silmek istediğiniz ürün adı veya numarasını girin: ")
            print(market.urun_sil(secim))
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-4 arasında bir seçim yapın.")

if __name__ == "__main__":
    Menu()
