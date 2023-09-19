#Kategorik değişken görselleştirme
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
print(df.head())

#df["sex"].value_counts().plot(kind = "bar") #Cinsiyet değişkenin erkek ve kadın dağılımını gösteren grafiktir.
#plt.show()
#--------------------------------------------------------------------------------------------------------------
#Sayısal değişken görselleştirme

#plt.hist(df["age"])
#plt.show()
#
#plt.boxplot(df["fare"])
#plt.show()

#--------------------------------------------------------------------------------------------------------------
#Matplotlıb'in özellikleri

#plot: Veriyi görselleştirmek için kullandığımız fonksiyon

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, "o")
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

#marker: işaretleyici özellikleri

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='*') #marker ile işareteleme yapılmaktadır. Uygulanabilecek markerlar 'o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h' şeklinde sıralanabilir.
plt.show()

#line: çizgi olşturma işlemlerine olanak sağlar

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed", color='r') #Linestyle argumnalarından:dashed, dotted, dashdot. Color ile çizgi rengi gireriz
plt.show()

#Multiple Lines: Birden fazla çizgiyi matplotlib katmanlaı yapısından dolayı birlikte kullanabiliriz.
x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)
plt.show()

#Labels: Etiketler
# Ana başlık ekleme
plt.title("Bu ana başlık")

#X eksenini isimlendirme
plt.xlabel("X ekseni isimlendirmesi")

#Y ekseni isimlendirmesi
plt.ylabel("Y ekseni isimlendirmesi")

#grafik arkasına ızgara koyma
plt.grid()
plt.show()

#Subplots: Birlikte birden fazla görselin gösterilmesi çalışması

#plot1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1) #1'e 2'lik bir grafik oluşturduk ve bu ilk grafikti
plt.title("1")
plt.plot(x, y)
plt.show()

#plot2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 2) #1'e 2'lik bir grafik oluşturduk ve bu ikinci grafikti
plt.title("2")
plt.plot(x, y)
plt.show()

#######################################################################################################
#Seaborn: Veri görselleştirme kütüphanesidir. Yüksek seviyeli bir  kütüphanedir. Matplotlib ile karşılaştırıldığında daha az çaba ile veri görselleştirme yapılmaktadır.
#Kategik değişken görselleştirme

df = sns.load_dataset("tips")
df.head()

print(df["sex"].value_counts())
sns.countplot(x = df["sex"], data = df)
plt.show()

#sayısal veri görselleştirme

sns.boxplot(x=df["total_bill"])
plt.show()




