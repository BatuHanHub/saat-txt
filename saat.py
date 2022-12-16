from datetime import datetime # zaman kütüp hanesi eklendi

tarih = datetime.now() # tarih eklendi
saat = datetime.now() # saat eklendi

tarih.strftime('%d.%m.%y')
saat.strftime('%H.%M')

print("Hoşgeldiniz! bu program her saat başı .txt dosyası olusturur.")

while True: #program döngüye sokuldu
    
    if saat.strftime('%M') == 00: # eğer dakika 00 ise aşağıdaki işlemler başlar
        dosya = open(f"{tarih.strftime('%d.%m.%y')} - {saat.strftime('%H.%M')}.txt","w") # dosya oluşturuluyor
        dosya.write(f"Bugun {tarih.strftime('%d.%m.%y')} Saat:{saat.strftime('%H.%M')}") #dosya yazılıyor
        dosya.close() # dosya yazma işlemi kapatılıyor
        print("\ndosya oluşturuldu.") # işlem bitince ekrana yazı yazılıyor
        continue 
    
    else:
        continue

"""
(...)

#deneme 1

baslangıc = open(f'deneme.txt',"w")
baslangıc.write(f'Bugün {tarih} Saat:{saat}')
baslangıc.close()

print("Hoşgeldiniz! bu program her saat başı .txt dosyası olusturur.")

while True: # program döngüye sokuldu

    if saat.minute == 00: # eğer saatin dakikası '00' olursa aşağıdaki işlemler yapılır
        dosya = open(f"{tarih} - {saat}.txt","w") # dosyanın başlığı "(tarih) - (saat).txt" olarak kaydedilecek # "w" yazdırma komutu
        dosya.write(f'Bugün {tarih} Saat:{saat}') # dosyanın içine "Bugün (Tarih) Saat:(saat)"
        dosya.close() # dosya yazdırma işlemi bitirildi
        print('dosya başarıyla yazdırıldı.')
        continue # döngü devam eder
        
    else: # değilse program devam edecek
        continue
"""