# Uygulama 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
#import seaborn as sns
#df = sns.load_dataset("car_crashes")
#print(df.columns)
#A = []
#for col in df.columns:
#    col = "NUM_" + col
#    A.append(col.upper())
#df.columns = A
#print(A)
#
#deneme = "Saniye"
#deneme = "Mrs. " + deneme + " Cebe" # String değişkenine + operatörüyle ekleme yapabilirsin. Cebe'den önce ve Mrs.'den sonra boşlu koymazsan Mrs.SaniyeCeb yazar
#deneme_2 ="Saniye"
#deneme_2 = "Mrs." + deneme_2 + "Cebe"
#
#print(deneme)
#print(deneme_2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Uygulama 2:  List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

#import seaborn as sns
#df = sns.load_dataset("car_crashes")
#print(df.columns)
#A = []
#
#for col in df.columns:
#    if "no" in col:
#        A.append(col.upper())
#    else:
#        col = col + "_FLAG"
#        A.append(col.upper())
#df.columns = A
#print(A)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Uygulama 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
#Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
#Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz

#import seaborn as sns
#df = sns.load_dataset("car_crashes")
#ogg_list = ["abbrev", "no_previous"]
#
#new_cols = [col for col in df.columns if col not in ogg_list]
#new_df = df[new_cols]
#print(new_df.head())

#################################################################################################################################################################################

#PANDAS ALIŞTIRMALARI
#Görev 1:Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

import pandas as pd
import numpy as np
import seaborn as sns
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

df = sns.load_dataset("titanic")
# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
print(df["sex"].value_counts())

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
print(df.nunique()) #Değişken sayısı hakkında bilgi verir.

#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
print(df["pclass"].nunique())

#Görev 5: pclass ve parch değişkenlerinin nunique değerlerinin sayısını bulunuz.
print(df[["pclass", "parch"]].nunique())

#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
print(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
print(df["embarked"].dtype)
df.info()

#Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
print(df[df["embarked"] == "C"].head(10))

#Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
print(df[df["embarked"] != "S"].head(10))

#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
print(df.loc[(df["age"] < 30) & (df["sex"] == "female")].head())

#Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
print(df.loc[(df["fare"] > 500) | (df["age"] > 70)].head())

#Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
print(df.isnull().sum())

#Görev 12: who değişkenini dataframe’den çıkarınız.
#print(df.drop("who", axis=1, inplace=True).head())

#Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
print(type(df["deck"].mode()))
print(df["deck"].mode()[0]) #Tipi seri olduğu için index değrerimizi belirtmemiz lazım
print(df["deck"].fillna(df["deck"].mode()[0], inplace=True)) #Boş alanları dolduması için fillna fonksiyonu kullanılır
print(df["deck"].isnull().sum())

#Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
print(df["age"].fillna(df["age"].median(), inplace=True))
print(df.isnull().sum())

#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
print(df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]}))

#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
#Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))

#Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df = sns.load_dataset("tips")
print(df.head())
print(df.shape)

#Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
print(df.groupby(["time"]).agg({"total_bill": ["sum", "min", "max", "mean"]}))

#Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
print(df.groupby(["time", "day"]).agg({"total_bill": ["sum", "min", "max", "mean"]}))

#Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
print(df[(df["time"] == "lunch") & (df["sex"] == "female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"], "tip" : ["sum", "min", "max", "mean"]}))

#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
print(df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean())

#Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
print(df["total_bill_tip_sum"].head())

#Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
new_df = df.sort_values("total_bill_tip_sum", ascending=False)[: 30] #ascending=False büyükten küçüğe sıralı hade gelmesini sağlar
print(new_df.shape)