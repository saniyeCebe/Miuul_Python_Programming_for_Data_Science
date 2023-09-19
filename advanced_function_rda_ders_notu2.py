#Analysis of Numerical Variables (Sayısal Değişken Analizi)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()

print(df[["age", "fare"]].describe().T) #Özet istatistiksel bilgiler gelmiştir.
#Programatik olarak numebric veri setini seçme işlemi nasıl yapılır?

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


print(df[["age", "fare"]].describe().T)
num_cols = [col for col in df.columns if df[col].dtype in ["int", "float"]]

num_cols = [col for col in num_cols if col not in cat_cols]
print(num_cols)

def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df, "age")

#Daha fazla değişken bulunması durumunda gerçekleştireceğimiz senaryo
for col in num_cols:
    num_summary(df, col)

#yazdığımız fonksiyona bir özellik eklemesi yapalım.

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

num_summary(df, "age", plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)
    