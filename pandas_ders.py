import pandas as pd
import seaborn as sns
print(pd.Series([1, 3, 6 ,8]))

df = sns.load_dataset("titanic")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info()) #genel bir inceleme yapılmak istendiğinde kullanılır.
print(df.columns)
print(df.index)
print(df.describe().T) #analitik açıdan elde bulunan değişkenlerin incelenmesini sağlar. T burada tranpozunu alması için yazılmıştır.
print(df.isnull().values.any()) #En az bir değer de olsa eksik bir değer var mı sorusunu sorar.
print(df.isnull().sum()) #Bir veri setinde değişkenlerde eksiklik bulunup bulunmadığını sorgulamak için kullanılır.
print(df["sex"].value_counts()) #Bir veride sınıfların kaçar tane olduğunu öğrenmek istediğimizde. Burada cinsiyet sorgulama yapılmış oldu.

#--------------------------------------------------------------------------------------

#Pandasta seçim işlemleri
print(df.index)
print(df[0:13])
print(df.drop(0, axis=0, inplace=True)) #satrlardan 0. indexi silmek istenildiğinde kullanılır. Değişikliğin kalıcı olmasını istediğimizde inplace kullanılır.

#Değişkeni indexe çevirmek
df["age"].head() #değişken seçimi
df.age.head() #değişken seçimi yapılır

df.index = df["age"] #yaş bilgisi bir değişken olarak indexe eklenmiş olur.
df.drop("age", axis=1 ,inplace=True) #değişeni sutunlardan silmek için kullanılır

#İndexi değişkene çevirmek
#1.yol
df["age"] = df.index
print(df.head)
#2.yol
df.reset_index().head()
df = df.reset_index()
df.head()
#--------------------------------------------------------------------------------------

#Değişken Üzerinde İşlemler

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
print(df.head())

print("age" in df) # "Age" değişkeni df veri seti içerisinde bulunuyor mu sorgusunu yapar

df["age"].head() #değişken seçme işlemi yapılır. Tipi pandas serisidir.
# Bir değişken seçerken sonucu seri yada datafream olarak alabiliriz. İki köşeli parantez girilirse datafream olarak deavm eder.
df[["age"]].head() #Çıktıısı artık float olur.
df.age.head()# değişken seçmek için yapılan diğer yöntem

print(df[["age", "alive"]])#İki değişken seçilmiş olur.

col_names = ["age", "adult_male", "alive"]
print(df[col_names])

df["age2"] = df["age"]**2 #var olan değişken üzerinde işlem yapılarak yeni bir değişken tanımlandı
df["age3"] = df["age"] / df["age2"]

df.drop("Age3", axis=1).head() #Silme işlemi yapılıyor. Kalıcı olarak silinmiyor. Kalıcı olarak değiştirmek istersek inplace=True yapılması gerekmektedir.

df.drop(col_names, axis=1).head() #Bir liste vererek de silme işlemini gerçekleştirebiliz.

df.loc[:, ~df.columns.str.contains("age")].head() #Belirli bir ifadeyi barındıran değişekni otomatik olarak seçmek için kullanılan ifadedir.Değildir ifadesi ~ olarak kullanılır.

#--------------------------------------------------------------------------------------

#İloc & loc
#İloc: İnteger based selection

df.iloc[0:3] #0'dan 3'e kadar seçim yapılır
df.iloc[0, 0] #0. satır 0. sütunda seçim yapılır.

#loc: label based selection

df.loc[0:3] #0'dan 3.ye kadar seçer. Yani 3. indexte dahil olur.

#--------------------------------------------------------------------------------------

#Conditional Selection (Koşullu Seçim)

df[df["age"] > 50].head() #Veri setindeki yaşı 50'den büyük olan kısımları çağırmış olduk
df[df["age"] > 50]["age"].count() #Yaşı 50'den büyük kişilerden kaç tane var sorusunun yanıtını verir.

df.loc[df["age"] > 50, "class"].head() #Yaşı 50'den büyük olan kişilerin sınıf bilgisini almak için kullanılır.
df.loc[df["age"] > 50, ["age", "class"]].head() #Yaşı 50'den büyük olan kişilerin sınıf ve yaş bilgilerini yazdırılmıştır.
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head() #Yaşı 50'den büyük ve cinsiyeti erkek olan kişilerin sınıf ve yaş bilgisi alonır.
# İki koşul girilme durumunda koşulları parantez içinde yazmak gereklidir.

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male") & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")), ["age", "class" , "embark_town"]].head()
df_new["embark_town"].value_counts()

