# ANALYSİS OF TARGET VARİABLES(HEDEF DEĞİŞKEN ANALİZİ)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')

for col in df.columns: #değişkenlerde gezmemezi sağlar
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def cat_summary(dataframe, col_name, plot=False): #İçerisine giren veriyi özetlemek için yazılan fonksiyondur
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#########################################################################")

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

#Elimizdeki hedef değişkeni (bu örnekte survived değişkeni) kategorik değişkenler ve sayısal değişkenler cinsinden analiz etmekdir.

print(df.head())

df["survived"].value_counts()
cat_summary(df, "survived")

#Hedef değişkenin Kategorik değişkenler ile analizi

print(df.groupby("sex")["survived"].mean()) #İki değişkeni bir arada değerlendiriliyor
# Hedef değişkene göre gruplama işlemi yapıldığında analiz konusunda yardımcı olmaktadır. Bu örnekte survived değişkenin cinsiyete göre değişip değişmediğini değerlendirme yapmaktadır.

def target_summry_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEA": dataframe.groupby(categorical_col)[target].mean()})) #dataframe'i groupby'a categorical_col göre al. Ardından target değişkeninin ortalamasını al

target_summry_with_cat(df, "survived", "pclass")

for col in cat_cols: #Bu döngüde bütün kategorik değişkenlerle bağımlı değişken analize sokulmuş oldu
    target_summry_with_cat(df, "survived", col)

#HEDEF DEĞİŞKENİN SAYISAL DEĞİŞKENLER İLE ANALİZİ

print(df.groupby("survived")["age"].mean()) #Bu sefer de groupyda numerik değişkeni koyup diğerine numeric değişkeni yerleştirirsek
#df.groupby("survived").agg({"age": "mean"}) Yukarıdaki ile aynı çıktıyı vericektir.

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col:"mean"}), end="\n\n\n")
target_summary_with_num(df, "survived", "age")

for col in num_cols:
    target_summary_with_num(df, "survived", col)

