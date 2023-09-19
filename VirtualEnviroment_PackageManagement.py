# Virtual Enviroment(Sanal Ortam) ve Package Managment(Paket Yönetimi)

# Komutları terminal kısımdan yapıp kontrollerini sağlarız

# Bilgisayardaki sanal ortamların listelenmesi için:
# conda env list komutu kullanılır.

# Sanal ortam oluşturma:
# conda create -n myenv

# Sanal ortamı aktif etme:
# conda activate myenv

# Yüklü paketlerin listelenmesi:
# conda list

# Paket yükleme:
# conda install numpy

# Aynı anda birden fazla paket yükleme:
# conda install numpy scipy pandas

# Paket silme:
# conda remove package_name

# Belrli bir versiyona göre paket yükleme:
# conda install numpy=1.20.1

# Paket yükseltme:
# conda upgrade numpy

#Tüm paketlerin yükseltilmesi:
# conda upgrade -all

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install paket_adi

# Paket yükleme versiyona göre:
# pip install pandas==1.2.1

#salaries =[1500, 3000, 6000, 8000]
#
#def new_salary(salary, rate):
#    return int(salary*rate/100 + salary)
#
#for salary in salaries:
#    if salary >= 3000:
#        print(new_salary(salary,10))
#    else:
#        print(new_salary(salary,20))

string = "abracadabra"
group = []

for index,letter in enumerate(string,1):
    if index * 2 % 2 == 0:
        group.append(letter)
print(group)