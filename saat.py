import datetime #kütüphane eklendi

tarih = datetime.datetime.now() # tarih eklendi

#print(tarih.strftime('%d.%m.%y'))
#print(tarih.strftime('%H.%M'))
#input()

print("Hoşgeldiniz! bu program her saat başı .txt dosyası olusturur.")

while True: #program döngüye sokuldu
    
    #tarih.strftime('%H')
    #artık çalışıyor
    if tarih.strftime('%H') == tarih.strftime("%H"):
        dosya = open(f"{tarih.strftime('%d.%m.%y')}-{tarih.strftime('%H.%M')}.txt","w")
        dosya.write(f'Bugün:{tarih.strftime("%d.%m.%y Saat: %H.%M")}')
        #dosya.write(f"Bugün:{tarih.strftime('%d.%m.%y')} Saat:{tarih.strftime('%H.%M')}")
        dosya.close()
        
        
        
    '''çalışmıyor                                                    
    if tarih.strftime('%M') == '00': # eğer dakika 00 ise aşağıdaki işlemler başlar 
        dosya = open(f"{tarih.strftime('%d.%m.%y')} - {tarih.strftime('%H.%M')}.txt","w") # dosya oluşturuluyor
        dosya.write(f"Bugun {tarih.strftime('%d.%m.%y')} Saat:{tarih.strftime('%H.%M')}") #dosya yazılıyor
        dosya.close() # dosya yazma işlemi kapatılıyor
        print("\ndosya oluşturuldu.") # işlem bitince ekrana yazı yazılıyor
        continue 
    '''

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
