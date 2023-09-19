# 1. Uygulama:  Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,kelime kelime ayırınız.
#text = "The gloal is to turn data into information, and information into insight."

#text = "The gloal is to turn data into information, and information into insight."
#text.upper().replace(","," ").replace(","," ").split()

#------------------------------------------------------------------------------------------------------------------------------------------------

#2. Uygulama: Verilen listeye aşağıdaki adımları uygulayınız.
#Adım 1: Verilen listenin eleman sayısına bakınız.
#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
#Adım 4: Sekizinci indeksteki elemanı siliniz.
#Adım 5: Yeni bir eleman ekleyiniz.
#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz

#lst = ["D", "A", "T", "A", "S", "I", "C", "E", "N", "C", "E"]
#
#print(len(lst))
#print(lst[0])
#print(lst[10])
#data_list= lst[0:4]
#print(data_list)
#lst.pop(8)
#print(lst)
#lst.append("P")
#print(lst)
#lst.insert(8,"N")
#print(lst)

#-------------------------------------------------------------------------------------------------------------------------------------------------

#Uygulama 3: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
#Adım 1: Key değerlerine erişiniz.
#Adım 2: Value'lara erişiniz.
#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
#Adım 5: Antonio'yu dictionary'den siliniz

#dict = {'Cristian': ['American', 18],
#        'Daisy': ['England',12],
#        'Antonio': ['Spain',22],
#        'Dante': ['İtaly',25]}
#dict.keys()
#dict.values()
#dict.update({'Daisy': ['England',13]})
#print(dict)
#dict.update({'Ahmet': ['Turkey',24]})
#print(dict)
#dict.pop('Antonio')
#print(dict)

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Uygulama 4:Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.
#Liste elemanlarına tek tek erişmeniz gerekmektedir.
#Her bir elemanın çift veya tek olma durumunu kontrol etmekiçin % yapısını kullanabilirsiniz

#l = [2, 13, 18, 93, 22]
#
#def func(l):
#    c = []
#    t = []
#    new_list = []
#    for index, sayi in enumerate (l):
#        if index % 2 == 0:
#            c.append(sayi)
#        else:
#            t.append(sayi)
#    new_list.append(t)
#    new_list.append(c)
#    print(new_list)
#    return new_list
#
#func(l)

#------------------------------------------------------------------------------------------------------------------------

#Uygulama 5: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
#tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız

#ogrenciler = ["Ali", "Veli", "Ayşe", "Talan", "Zeynep", "Ece"]
#
#for i,ogrenci in enumerate(ogrenciler):
#    if i < 3:
#        i += 1
#        print("Mühendislik fakültesi: ",i, ". ogrenci: ",ogrenci)
#    else:
#        i -= 2
#        print("Tıp fakültesi: ", i, ". ogrenci: ", ogrenci)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Uygulama 6: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

#ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2205"]
#kredi = [3, 4, 2, 4]
#kontenjan = [30, 75, 150, 25]
#
#for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
#    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Uygulama 7: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir

kume1 = set(["data", "pyhton"])
kume2 = set(["data", "function", "cqut", "lambda", "pyhton", "miuul"])

def kume(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1, kume2)
kume(kume2, kume1)