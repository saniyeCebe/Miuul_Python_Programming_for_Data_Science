#ANALYSİS OF CORRELATİON(KOLERASYON ANALİZİ)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = pd.read_csv("datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
print(df.head())

#Elimize bir veri seti geldiğinde bu ısıya dayalı veri setinde korolasyona bakmak ve bu veri setinde yüksek korolasyon değişkenlerden bazılarını dışarıya çıkarabilmektedir.

num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

corr = df[num_cols].corr() #Korelasyon hesaplamak için

#Korelasyon değişkenlerin birbiri ile ilişkisini ifade eden istatiksel bir ölçümdür. -1 ile +1 arasında değerler alır. -1'e ya da +1'e yaklaştıkça ilişkinin şiddeti kuvvetlenir
#Eğer iki değişeknin arasındaki ilişki pozitif ise buna pozitif korelasyon denir ve birinin değeri artıkça diğerinin de değeri artar.
#İki değişken arasındaki ilişki negatifse buna negatif korelasyon denir ve bir değişken artarken diğer değişkenin değerleri azalır.
#Dalayısıyla 0 civarındaki bir korolasyon değeri korelasyon olmadığı anlamına gelir
#Genelede korelasyonu yüksek olan değişkenlerin biribiri ile çalışmamasını tercih edilir. Çünkü ikisi de aynı şeyi ifade etmekte olduğunu gösterir.

#Isı haritası ile korolasyonun görselleştirimesi yapıldı
sns.set(rc={'figure.figsize':(12,12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

########## Yüksek korelasyonlu değişkenlerin silinmesi ##############

cor_matrix = df.corr().abs() #negatif ya da pozitif korelasyon fark etmeksizin mutlak değerlerini alınıyor.

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
#Yüksek korelasyon değerlerini silip daha düzgün bir matris oluşturmak için
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>0.90)]
cor_matrix[drop_list]
df.drop(drop_list, axis=1)

#Bu işlemi fonksiyonlaştıralım
def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plot
        sns.set(rc={'figure.figsize': (15,15)})
        sns.heatmap(corr,cmap="RdBu")
        plt.show()

    return drop_list

high_correlated_cols(df)
drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)



