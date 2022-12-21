#KÜTÜPHANELER
import datetime #Zaman kütüphanesi
import time #Sayaç kütüphanesi

#zaman = datetime.datetime.now() seni yaramaz kod satırı :D

print("Hoşgeldiniz! bu program her saat başı .txt dosyası olusturur.")

while True: #program döngüye girdi

    zaman = datetime.datetime.now() #Zaman değişkeni şimdiki zamanın verilerini tutuyor

    #eğer dakika 00 ise aşağıdaki kodlar çalışır
    if zaman.minute == 00:
        dosya = open (f"{zaman.strftime('%d.%m.%y')}.txt","w")
        dosya.write(f'Bugün:{zaman.strftime("%d.%m.%y Saat: %H.%M")}') 
        dosya.close() #dosya ile işi bitiyor
        print("Dosya yazıldı.") #İşlem bitince ekrana yazı yazıyor
        time.sleep(59) #59 dakika bekliyor...
        continue
    
    #değilse dönmeye devam :)
    else:
        continue
