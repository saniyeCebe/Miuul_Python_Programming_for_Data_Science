#Bir veri setindeki değişken isimlerini değiştirmek

#import seaborn as sns
#df = sns.load_dataset("car_crashes")
#df.columns
#
#for col in df.columns:
#    print(col.upper())
#
#A = []
#
#for col in df.columns:
#    A.append(col.upper())
#
#df.columns = A

#---------------------------------------------------------------------------------------

#İsminde "INS" olan değişkenlerin başına FLAG diğerine NO_FLAG eklemek istiyoruz.

#["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]
#df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

#---------------------------------------------------------------------------------------------

# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
#Bu işlemi sadece sayılsal değerler için yapmak istiyoruz

#import seaborn as sns
#df = sns.load_dataset("car_crashes")
#df.colums
#
#num_cols = [col for col in df.colums if df[col].dtype != "0"]
#soz = {}
#agg_list = ["mean", "min", "max", "sum"]
#
#for col in num_cols:
#    soz[col] = agg_list

