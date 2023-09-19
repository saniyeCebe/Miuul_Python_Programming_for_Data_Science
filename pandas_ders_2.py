# Aggregation & Grouping (Toplulaştırma ve Gruplama)
# Aggregation (Toplulaştırma): Bir veri yapısının içerisinde bulunan değerleri toplu bir biçimde temsil etmek.
# -count()
# -first()
# -last()
# -mean()
# -median()
# -min()
# -max()
# -std()
# -var()
# -sum()
# -pivot table
# Burada kullanılan fonksiyonlar toplulaştırma fonksiyonlarıdır.
# Toplulaştırma bize özet istatistikler veren fonksiyonlardır.
import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

#print(df["age"].mean()) #Veri setinde bulunan yaş ortalaması
#print(df.groupby('sex')["age"].mean()) #Cinsiyete göre yaş ortalaması yapılıyor. Burada groupby ile birlikte gruplama yapılıyor.
#print(df.groupby("sex").agg({"age": ["mean", "sum"]})) # Cinsiyete göre yaş ortalaması yapılıyor. Burada groupby ile birlikte gruplama yapılıyor.
#
# #print(df.groupby("sex").agg({"age": ["mean", "sum"], "embark_tower": 'count'}))
#
##a = df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"], "embark_tower": "count"})
##print(a)
#
#a = df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"], "survived": "mean", "sex": "count"})
#print(a)

# PİVOT TABLE
# Veri setini kırılımlar açısından değerlendirmek ve ilgilendiğimiz özet istatistiği bu kırılımlar açısından görme imkanı sağlar.
print(df.pivot_table("survived", "sex", "embarked"))

print(df.pivot_table("survived", "sex", "embarked" ,aggfunc="std")) #Değişkenlerin standart sapmaları hesaplıycak

print(df.pivot_table("survived", "sex", ["embarked" , "class"]))

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])#Cut ve qcut fonksiyonları elimizdeki sayısal değişkenleri kategorik değişkene çevirmek için kullanılır.
# Cut fonksiyonu sayısal değişkenleri hangi kategorilere bölmek istediğimizi biliyorsak kullanılır.
# qcut elimize bulunan sayısal değişkenleri tanımıyorsak ve çeyreklik değerlerine göre bölünsün isteniyorsa kullanılır.
print(df.pivot_table("survived", "sex", ["new_age","class"]))

#APPLY ve LAMBDA
#Döngülerden daha pratik satır yada sütunlarda otomatik olarak çalışan apply yapısı ve fonksiyon tanımlamadan kullan at fonksiyon olarak kullanılan lambda yapısını kullanmak oldukça pratiktir.
# Apply satır yada sütunlarda otomatik olarak fonksiyon çalıştırmayı sağlar.
#Lambda fonksiyon tanımlamada kullanılır. Kullan at fonksiyon olarak tanımlanır.

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5


(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10
df.head()

df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head() #Yukarıda yazılan döngüyü yazmadan pratik bir şekilde veri seti içerisinde dolaşmayı sağlar.

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head() #Uygulandığı datafreamdeki standartlaşma işlemi yapılsın.

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

#df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
df.head()

#Apply fonksiyonu satırlarda yada sütunlarda ki argümanları axisleyerek satır sütun ayarlaması yapılabilir. Bize fonksiyon uygulaması sağlar.


#Birleştirme (Join) işlemleri

m = np.random.randint(1, 30, size=(5,3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"]) #DataFrame oluşturmak için yazılan kod.
df2 = df1 + 99

pd.concat([df1, df2], ignore_index=True) #İki DataFrame birleştirmek istersek concat ile bu işlemi yapabiliyoruz. İgnore_index argumanı true yapılırsa index bilgisi birleştirme sırasında ayrı ayrı görünmez.

#Merge ile Birleştirme İşlemleri

df1 = pd.DataFrame({'employees': ['join', 'dennis', 'mark', 'maria'], 'group' : ['acconting', 'engineering', 'engineering', 'hr']})
df2 = pd.DataFrame({'employees': ['join', 'dennis', 'mark', 'maria'], 'start_data' : [2010, 2009, 2014, 2019]})

df3 = pd.merge(df1,df2)
pd.merge(df1, df2, on="employees") #Hangi değişkene göre birleştirme işlemi yapılacağını göstermek için on argumanı kullanılır.

#Amaç: Her çalışanın müdürünün bilgisine erişmek isteniyorsa

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'], 'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)


