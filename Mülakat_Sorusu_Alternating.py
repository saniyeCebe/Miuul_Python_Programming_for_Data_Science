#Uygulama - Mülakat Sorusu
#Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak
#Before: "Hi my name is john and i am learning pyhton"
#After: "Hi mY NaMe İS JoHn aNd i aM LeArNiNg pYtHoN"


#def alternating(string):
#    new_string = ""
#    #Girilen stringin indexlerinde gez
#    for string_index in range(len(string)):#range fonksiyonu burada 0 dan string ifadenin uzunluğuna kadar olan ifadeyi belirtir.
#        #index çift ise büyük harfe çevir.
#        if string_index % 2 == 0:
#            new_string += string[string_index].upper()
#        #index tek ise küçük harfe çevir
#        else:
#            new_string += string[string_index].lower()
#    print(new_string)
#
#alternating("Hi my name is john and i am learning pyhton")

#-------------------------------------------------------------------------------------------------------------------------------

#Alternating fonksiyonunun enumerate ile yazılması

def alternating_with_enumerate(string):
    new_string = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)
alternating_with_enumerate("Hi my name is john and i am learning pyhton")




