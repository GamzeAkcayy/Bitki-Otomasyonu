
bitkiler={}
bitki={}
ozellikler={}
guncel_bitkiler = []

def bitki_ekle():

    print("-------YENİ BİTKİ EKLE-------")
    bitkiadet=int(input("Kaç adet yeni bitki girişi yapacaksınız?"))

    def bitki_girisi():
        for i in range(bitkiadet):
            control = 1
            no = input("Bitki numarası giriniz:")
            #ilk try bloğu bitki numarasına sıfır ya da negatif değer girilirse hata yakalar
            try:
                no = int(no)
                if no <= 0:
                    raise ValueError("Sıfır ya da negatif bir sayıyı numara olarak yazamazsınız!")
            except ValueError as problem:
                print(problem)
                control=0
            if control==1:
                no=str(no)
                adi=input("Bitki adı giriniz:")
                tur=input("Bitki türü giriniz 'Ev','Dışarı':")
                su=input("Kaç günde bir sulanmalı:")
                gunes=input("Güneş toleransı nedir 'Yüksek','Orta','Düşük':")
                bitki[
                    no + " -->"+ " Bitki adı -->" + adi + " Tür-->" + tur + " Şu kadar günde sulanmalı-->" + su + " Güneş toleransı-->" + gunes]=ozellikler
                with open("20010011039.txt","a",encoding="utf-8") as file:#sözlük yapısı ile kayıt işlemi
                    for key in bitki.keys():
                        file.write(str(key) + " ")
                        for value in bitki[key].values():
                            file.write(value)
                        file.write("\n")
                print("Yeni bitki girişi yapıldı.")

    bitki_girisi()

def bitki_sil():
    print("-------BİTKİ SİL-------")
    with open("20010011039.txt","r",encoding="utf-8") as dosya:
        kontrol= None
        bitkiNo = input("Silmek istediğiniz bitkinin numarasını giriniz: ")
        for satir in dosya.readlines():
            hucre=satir.split(" ")
            key,value=hucre[0],hucre[1:]
            bitkiler[key]=value
            if bitkiNo==key:
                kontrol=True
                bitkiler.pop(key)
        if kontrol:
            with open("20010011039.txt","w",encoding="utf-8") as file:
                for key in bitkiler.keys():
                    file.write(key)
                    for i in range(len(bitkiler[key])):
                        file.write(" "+ bitkiler[key][i])
            print("Seçtiğiniz bitki silindi.")
        else:
            print("Seçtiğiniz bitki bulunamamıştır.")


def bitki_ozellikleri_guncelle():

    with open("20010011039.txt", "r", encoding="utf-8") as file:
        guncel = input("Güncellemek istediğiniz bitkinin numarasını giriniz: ")
        for satir in file.readlines():
            if satir.startswith(guncel):
                adi = input("Bitki adı giriniz: ")
                tur = input("Bitki türü giriniz: ")
                su = input("Kaç günde bir sulanmalı: ")
                gunes = input("Güneş toleransı nedir: ")
                yeni_bilgiler = f"{guncel},{adi},{tur},{su},{gunes}\n"#liste yapısı ile güncelleme işlemi
                guncel_bitkiler.append(yeni_bilgiler)
                print("Güncelleme başarı ile yapıldı!!")
                break
            else:
                print("Yanlış numara girdiniz!!")
                guncel_bitkiler.append(satir)

def bitkileri_listele():
    with open("20010011039.txt","r",encoding="utf-8") as f:
        oku=f.readlines()
        for i in oku:
            satir = i.split("\n")
            satir.pop(1)
            print(satir)

def bitki_ara():
    bitkiNo=input("Kaç numaralı bitkiyi aramak istiyorsunuz:")
    with open("20010011039.txt","r",encoding="utf-8") as d:
        satirlar=d.readlines()
        for i in satirlar:
            satir = i.split(" ")
            if satir[0] == bitkiNo:
                print(satir)
                break
            else:
                print("Aradığınız bitki numarası bulunamadı.")
                break

#Bu fonksiyonu yeni ekledim, bitki fiyatı hesaplamak için kullanılır.
def bitki_fiyat_hesapla():
    print("----FİYAT HESAPLA----")
    print("İstediğiniz bitkinin özelliklerini giriniz:")
    yurt_disi = input("Bitki Türkiye'de bulunuyor mu? evet:E, hayır:H")
    ev_bitkisi = input("İstediğiniz bitki ev bitkisi mi? evet:E, hayır:H")
    # ikinci try bloğu yazım yanlışını yakalar
    try:
        if yurt_disi!="E" or "H":
            raise ValueError("Yazım yanlışı yaptınız!")
        elif ev_bitkisi!="E" or "H":
            raise ValueError("Yazım yanlışı yaptınız!")
    except ValueError as yanlis:
        print(yanlis)
    if yurt_disi == "H" and ev_bitkisi == "E":
        print("İstediğiniz bitkinin yaklaşık fiyatı 2100 tl'dir.")
    elif yurt_disi == "H" and ev_bitkisi == "H":
        print("İstediğiniz bitkinin yaklaşık fiyatı 4250 tl'dir.")
    elif yurt_disi == "E" and ev_bitkisi == "H":
        print("İstediğiniz bitkinin fiyatı 530 tl'nin altında olacaktır.")
    elif yurt_disi == "E" and ev_bitkisi == "E":
        print("İstediğiniz bitkinin fiyatı 250 tl'nin altında olacaktır.")

#Bu fonsiyon da yeni eklendi. Bitki sorununa göre çözüm üretir.
def bitki_sorun_bul():
        print("-----BİTKİ SORUNUNU BULMA-----")
        ev_bitkisi = input("Ev bitkisi mi? evet:E, hayır:H")
        if ev_bitkisi == "E":
            guneste_kalma_miktari = int(input("Güneşte kalma süresini saat cinsinden giriniz:"))
            if guneste_kalma_miktari > 2:
                print("Bitkiyi doğrudan güneş görmeyecek şekilde başka bir yere alınız.")
        sulama_miktari = int(input("Günlük sulama miktarınızı mL cinsinden giriniz:"))
        bocek = input("Bitkiniz etrafında böcek gözlemlediniz mi? evet:E, hayır:H")
        leke = input("Yapraklarında lekeler veya solgunluk gözlemlediniz mi? evet:E, hayır:H")

        if sulama_miktari == 0:
            print("Lütfen bitkiyi sulayınız!!")
        elif sulama_miktari != 0 and bocek == "E":
            bocek_sayisi = input("Böcekler bitkinin her yerini sarmış durumda mı? evet:E, hayır:H")
            if bocek_sayisi == "E":
                print("Hemen mağazamıza gelip bitki ilacı alınız!!")
            else:
                print("Bir adet sigara izmariti veya aspirinli su ile böceklerden kurtulabilirsiniz.")
        elif sulama_miktari != 0 and leke == "E":
            print("Bitki için mağazamızdan vitamin temin ediniz.")
        else:
            print("Bitkinizin ilgiye ihtiyacı var :)")

def menu():
    print("-*-*-*-*-* UZAY ÇİÇEK *-*-*-*-*-")
    while True:
        giris=int(input("1-YENİ BİTKİ GİRİŞİ\n2-BİTKİ SİL\n3-BİTKİ ÖZELLİKLERİNİ GÜNCELLE\n4-BİTKİLERİ LİSTELE\n5-BİTKİ ARA\n"
                        "6-BİTKİ FİYAT HESAPLA\n7-BİTKİ SORUNU BUL\n8-PROGRAMDAN ÇIK\n"))
        if giris==1:
            bitki_ekle()
        elif giris==2:
            bitki_sil()
        elif giris==3:
            bitki_ozellikleri_guncelle()
        elif giris==4:
            bitkileri_listele()
        elif giris==5:
            bitki_ara()
        elif giris==6:
            bitki_fiyat_hesapla()
        elif giris==7:
            bitki_sorun_bul()
        else:
            print("Programdan çıkış yaptınız.")
            break
menu()
