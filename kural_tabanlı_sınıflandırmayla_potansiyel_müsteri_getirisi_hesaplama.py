#Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

#İş Problemi
#Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları(persona) oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup
#bu segmentlere göre yeni gelebilecek müşterilerin şirkete ortalama ne kadar kazandırabileceğini tahin etmek istemektedir.

#Veri setinin hikayesi
#Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
#demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
#tekilleştirilmemiştir. Diğer bir ifade ile bellirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

#Price: Müşterinin harcama tutarı
#Source: Müşterinin bağlandığı cihaz türü
#Sex: Müşterinin cinsiyeti
#Country: Müşterinin ülkesi
#Age: Müşterinin yaşı

#GÖREV1

import pandas as pd
pd.set_option("display.max_rows",None)
df = pd.read_csv("datasets/persona.csv")
print(df.head())
print(df.shape)

#Soru2: Kaç unique SOURCE vardır?Frekansları nedir?
print(df["SOURCE"].nunique())
print(df["SOURCE"].value_counts())

#Soru3:  Kaç unique PRİCE vardır?
print(df["PRİCE"].nunique())

#Soru4: Hangi PRİCE den kaçar tane satış gerçekleşmiştir?
print(df["PRİCE"].value_counts())

#Soru5: Hangi ülkeden kaçar tane satış olmuştur?
print(df["COUNTRY"].value_counts())
print(df.groupby("COUNTRY")["PRİCE"].sum())

#Soru6: Ülkelere göre satışalrdan toplam ne kadar kazanılmış?
print(df.groupby("COUNTRY")["PRİCE"].sum())
df.groupby("COUNTRY").agg({"PRICE": "sum"})

#Soru7: SOURCE türlerine göre satış sayıları nedir?
print(df["SOURCE"].value_counts())

#Soru8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby(by=["COUNTRY"]).agg({"PRICE": "mean"})

#Soru9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby(by=["SOURCE"]).agg({"PRICE": "mean"})

#Soru10: COUNTRY-SOURCE kırılımında PRICE ortalamları nedir?
df.groupby(by=["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

#GÖREV2: COUNTRY, SOURCE, SEX, AGE kırılımlarında ortalama kazançlar nedir?
df.groupby(by=["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head()

#GÖREV3: Çıktıyı PRİCE göre sıralayınız.
agg_df = df.groupby(by=["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
print(agg_df.head())

#GÖREV4: Indexte yer alan isimleri değişken ismine çeviriniz.
#Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
#Bu isimleri değişken isimlerine çeviriniz.

agg_df = agg_df.reset_index()
print(agg_df.head())

#GÖREV5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.

#Age sayısal değişkeni kategorik değişkene çeviriniz.
#Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.

agg_df["AGE"].describe()

#AGE değişkeninin nereden bölüneceğini belirtiniz:
bins = [0, 10, 23, 30, 40, agg_df["AGE"].max()]

#Bölünen noktalara karşılık isimlendirmelerin ne olacağını ifade edelim:
myLabels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]

#age'i bölelim:
agg_df["agg_cat"] = pd.cut(agg_df["AGE"], bins, labels=myLabels)
agg_df.head()

#GÖREV6: Yeni level based müşterileri tanımlıyoruz ve veri setine değişken olarak ekleme yapılıuor.

#customers_level_based adında yeni bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
#list comp ile customer_level_based değerleri oluşturulduktan sonra bu değişkenlerin tekilleştirilmesi gereekmektedir.
#Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
#Bunları gruopby'a alıp price ortalamalarını almak gerekmketedir.

# değişken isimleri:
agg_df.columns
#gözlem değerlerine nasıl erişiriz?
for row in agg_df.values:
    print(row)

#COUNTRY , SOURCE, SEX ve age_cat değişkenlerinin DEĞERLERİNİ yan yana ve alt tireyle birleştirmek
#Bunu list comprehension ile yapabiliriz.
#Yukarıdaki döngüdeki gözlem değerlerinin bize lazım alanlarını seçecek şekilde işlemi gerçekleştirelim.
[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]

#Veri setine ekleyelim:
agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
agg_df.head()

#Gereksiz değişkenleri çıkartalım:
agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))

agg_df["customers_level_based"].value_counts()
#Segmentere göre groupby yaptıktan sonra price ortalamalarını alalım ve degmentleri tekkilleştirelim.
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

#customers_level_based index'te  yer almaktadır. Bunu değişkene çevirelim.
agg_df = agg_df.reset_index()
agg_df.head()

agg_df["customers_level_based"].value_counts()
agg_df.head()

#GÖREV7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentelere ayırınız.

#PRICE'a göre segmentlere ayırın.
#segmentleri "SEGMNET" isimlendirmesi ile agg_df'e ekleyiniz.

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

#GÖREV8: Yeni gelen müşterileri sınıflandırmanız ne kadar gelir getirebileceğini tahmin ediniz.

#33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"] == new_user])

#35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "FRA_ISO_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"] == new_user])


