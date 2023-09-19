# Uygulama - Mülakat Sorusu

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Key'ler orjinal değerler value'ler ise değiştirilmiş değerler.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2 #keyler sayıların kendisi, value'ler ise sayıların işleme sokulmuş hali
 #dict comprehension yapısı ile: {n: n ** 2for n in numbers if n %  == 0}

