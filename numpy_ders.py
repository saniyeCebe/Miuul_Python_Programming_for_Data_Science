import numpy as np
np.array([1, 2, 3, 4, 5])#numpy array oluşturma
np.zeros(10, dtype=int) #istenildiği kadar 0 dan oluşan array oluşturma
np.random.randint(0, 10, size=10)#0 ile 10 arasında 10 adet int seçilerek array oluşturma
np.random.normal(10, 4, (3, 4))#Ortalaması 10 standart sapması 4 olan (3,4)'lük normal dağılımlı sayılardan bir array oluşturma

print(np.array([1, 2, 3, 4, 5]))

#İki bilinmeyenli denklem çözümü
#5*x0 + x1 =12
#x0 + 3 *X1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

print(np.linalg.solve(a,b))

#Numpy hızlıdır.
#Numpy bize vektörel düzeyden kolaylık sağlar
