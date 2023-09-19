#Gezinomi Kural Tabanlı Sınıflandırma İle Potansiyel Müşteri Getirisi Hesapla

import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format",lambda x:"%.2f" % x)
excel_dosya_adi=r"C:\Users\saniy\Desktop\gezinomi_tanıtım\miuul_gezinomi.xlsx"
df = pd.read_excel(excel_dosya_adi)
print(df.head())
print(df.shape)
print(df.info)

#Kaç unique şehir vardır? frekansları nelerdir?

print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

#Kaç unique Concept vardır?
print(df["ConceptName"].nunique())

#Hangi Concept'den kaçar tane satış gerçekleştirilmiş?
print(df["ConceptName"].value_counts())

#Şehirlere göre satışlardan toplam ne kadar kazanılmış?
print(df.groupby("SaleCityName").agg({"Price": "sum"}))

#Concept türlerine göre ne kadar kazanılmış?
print(df.groupby("ConceptName").agg({"Price": "sum"}))

#Şehirlere göre price ortalamaları nedir?
print(df.groupby("SaleCityName").agg({"Price": "mean"}))

#Conceptlere göre price ortalamalrı nedir?
print(df.groupby("ConceptName").agg({"Price": "mean"}))

#Şehir-Concept kırılımında Price ortalamalrı nedir?
print(df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"}))

###########################################################################
#satıs_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()] #Belirtilen değerlerde aralıklar oluşur
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"] #Bu aralıklara isimler verilmesi için dizi oluşturulur

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)

###################################################################################
#Şehir, Concept, [EB_Score,Sezon,CInday] kırılımlarında ücret ortalamalarını ve frekanslarına bakınız.

#Şehir-Concept-EB _Score kırılımlarında ücret ortalamaları
print(df.groupby(by=["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]}))

#Şehir-Concept-Sezon kırılımlarında ücret ortalamaları
print(df.groupby(by=["SaleCityName", "ConceptName", "Sezon"]).agg({"Price": ["mean", "count"]}))

#Şehir-Concept-CInday kırılımlarında ücret ortalamaları
print(df.groupby(by=["SaleCityName", "ConceptName", "CInday"]).agg({"Price": ["mean", "count"]}))

#####################################################################################
#Cıty-Concept-Season kırınımlarının çıktısını price göre sıralayanız

#Önceki sorudaki çıktıyı daha iyi görebilmke için sot_values methodunu azalan olacak şekilde PRİCE'a uygulayınız.
#Çıktıyı agg_Df olarak kaydediniz

agg_df = df.groupby(by=["SaleCityName", "ConceptName", "Season"]).agg({"Price": ["mean", "count"]})
print(agg_df.head(20))

#####################################################################################
#İndexte yer alan isimleri değişken ismine çeviriniz.

#Bu isimleri değişken isimlerine çeviriniz.

agg_df.reset_index(inplace=True)
print(agg_df.head())
#####################################################################################
#Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz

#sales_leve_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Season"]].agg(lambda x:"_".join(x).upper(), axis=1)
print(agg_df)
#####################################################################################
#Personaları segmentelere ayırınız

#PRİCE'a göre segmentelere ayrınız
#Segmentleri "segment" isimlendirmesi ile agg_df ekleyiniz
#segmenteleri betimleyiniz

agg_df["SEGMENT"] = pd.qcut(agg_df["Prıce"], 4, labels=["D", "C", "B", "A"])
print(agg_df.head())
print(agg_df.groupby("SEGMENT").agg({"Price": ["mean", "count", "sum"]}))

#####################################################################################
#Oluşan son df'i PRICE değişkenine göre sıralayınız
#"ANTALYA_HERŞEY_DAHİL_HİGH" hangi segmenttedir ve ne kadar ücret belirtmektedir bulunuz

agg_df.sort_values(by="Price")

new_user="ANTALYA_HERŞEY_DAHİL_HİGH"
agg_df[agg_df["sales_level_based"] == new_user]
