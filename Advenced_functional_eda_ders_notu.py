# ADVANCED FUNCTİONAL EDA (GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ)
#Hızlı bir şekilde elimize gelen verileri analiz etme olarak tanımlanabilir.

#1. Genel resim: Gelen verinin içerisinde neler olduğunu genel olarak inceleme basamağıdır.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()

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

def check_df(dataframe, head=5):
    print("################# Shape ##############")
    print(dataframe.shape)
    print("################# Types #################")
    print(dataframe.dtypes)
    print("################# Head ###############")
    print(dataframe.head(head))
    print("################# Tail ###############")
    print(dataframe.tail(head))
    print("############### NA ##################")
    print(dataframe.isnull().sum())
    print("################ Quantiles ##############")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)



print(check_df(df))



#----------------------------------------------------------------------------------------------------------

#Analysis of Categorical Variables (Kategorik Değişken Analizi)

print(df["embarked"].value_counts()) #Değişkenin sınıf değerlerinin öğrenilmesi için kullanılır.
print(df["sex"].unique()) #Değişkende kaç unique değer olduğunu sorgular
print(df["sex"].nunique()) #Değişkende kaç tane eşsiz değer olduğnu sorgular

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
print(cat_cols)

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]] #Tip olarak int olan ama categorik olmasını yakalayan kod
print(num_but_cat)

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
print(cat_but_car)

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]
print(cat_cols)

print(df[cat_cols].nunique())

#print(df["survived"].value_counts())
#print(100 * df["survived"].value_counts() / len(df))

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#########################################################################")

print(cat_summary(df, "sex"))

for col in cat_cols:
    print(cat_summary(df, col))

def cat_summary(dataframe, col_name, plot=False): #İçerisine giren veriyi özetlemek için yazılan fonksiyondur
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#########################################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

print(cat_summary(df, "sex", plot=True))

for col in cat_cols:
    if df[col].dtypes == "bool": #Bool tipte olanları pas geçti
        print("nkkdnvkndnn")
    else:
        print(cat_summary(df, col, plot=True))

print(df["adult_male"].astype(int)) #bool tipte olan değişkeni grafikte kullanılabilir hale getirmek için

for col in cat_cols:
    if df[col].dtypes == "bool": #Bool tipte olanları pas geçti
        df[col] = df[col].astype(int)
        print(cat_summary(df, col, plot=True))
    else:
        print(cat_summary(df, col, plot=True))