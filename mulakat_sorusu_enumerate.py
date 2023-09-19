#Uygulama - Mülakat Sorusu
#divide_students fonksiyonu yazınız.
#Çift indexte yer alan öğrencileri bir listeye alınız.
#Tek indexte yer alan öğrencileri başka bir listeye alınız.
#Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    A = []
    B = []
    new_list = []

    for index,student in enumerate(students):
        if index % 2 == 0:
            A.append(student)
        else:
            B.append(student)
    new_list.append(A)
    new_list.append(B)
    print(new_list)
    return new_list
divide_students(students)

