class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satislar = {}

   
    

    

       def __str__(self):
        saticilar_str = ""
        for satici, satis_tutari in self.__satislar.items():
            saticilar_str += f"{satici} - {satis_tutari}\n"
        return f"Mağaza Adı: {self.__magaza_adi}\nSaticilar ve Satis Tutarlari:\n{saticilar_str}Toplam Satis Tutarı: {self.magaza_satis_tutar()}"

def main():
    magazalar = {}

    while True:
        magaza_adi = input("Magaza Adi: ")
        satici_adi = input("Satici Adi: ")
        satici_cinsi = input("Satici Cinsi (tv, bilgisayar, beyaz esya, diger): ")
        satis_tutari = float(input("Satis Tutari: "))

        if magaza_adi not in magazalar:
            magazalar[magaza_adi] = Magaza(magaza_adi, satici_adi, satici_cinsi)
        else:
            magaza = magazalar[magaza_adi]
            magaza.set_satici_adi(satici_adi)
            magaza.set_satici_cinsi(satici_cinsi)

        magazalar[magaza_adi].satis_ekle(satis_tutari)

        devam = input("Devam etmek istiyor musunuz? (E/H): ")
        if devam.lower() != "e":
            break

    for magaza in magazalar.values():
        print(magaza)

if __name__ == "__main__":
    main()
