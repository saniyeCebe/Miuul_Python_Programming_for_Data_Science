#CAPTURİNG VARİABLES AND GENERALİZİNG OPERATİONS(DEĞİŞKENLERİN YAKALANMASI VE İŞLEMLERİN GENELLEŞTİRİLMESİ)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()
df.info()

#Bir fonksiyon tanımlayıp bu fonksiyonun diğer kullanılıclar tarafından kullanılırken hangi bilgileri barındırması gerektiği konusunda çalışmalar yapılıcaktır.
#İlk yapılacak işlem veri setindeki kategorik değişkenleri listesini, numerik değişkneleri listesini ve kategorik ama kardinal değişken listesini ayrı ayrı getirmesi
#Docstring: Bir fonksiyona argüman yazma
#Docsrtring: Bir fonksiyon yazıldığında sonrasında bir başkasının da bu fonksiyonu kullanması için tanımlar yapılması gerekmektedir. Buna docstring denir.


def grab_col_names(dataframe, cat_th=10, car_th=20): #Bir değişken sayısal olsa dahi eşşiz değer sayısı 10 dan küçükse bu bir kategorik değişken olarak sayılıcaktır. Bir kategorik değişkenin eşşiz değer sayısı 20 den büyükse buna kardinal değişken olarak adlandırıcaz.
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kordinal değişkenlerin isimleirni verir.
    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kordinal değişkenler için sınıf eşik değeri

    Returns:
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kordinal değişken listesi

    Notes
    ----------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.


    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    print(cat_cols)
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int",
                                                                                              "float"]]  # Tip olarak int olan ama categorik olmasını yakalayan kod
    print(num_but_cat)
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    print(cat_but_car)
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    print(cat_cols)
    print(df[cat_cols].nunique())

    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f'Observation: {dataframe.shape[0]}')
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name, plot=False): #İçerisine giren veriyi özetlemek için yazılan fonksiyondur
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#########################################################################")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

for col in num_cols:
    num_summary(df, col, plot=True)

#cat_summry fonksiyonunu da plot özelliği ile biçimlendirilecek şekilde bir yol ele alma
df = sns.load_dataset('titanic')
df.info()
#Veri seti içerisinde bulunan bool tipteki değişkenleri bulup bunları int değere çevirmek
#Daha sonra cat_summry fonksyonunu görsel özellikte daha kolay kullanmak amaçlanmıştır.

for col in df.columns: #değişkenlerde gezmemezi sağlar
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)


###############################################################################################################################################

# ANALYSİS OF TARGET VARİABLES(HEDEF DEĞİŞKEN ANALİZİ)
