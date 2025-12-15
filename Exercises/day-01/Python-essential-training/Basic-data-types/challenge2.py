# Converting hexadecimal to decimal 

hexaset = {
    '0' : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9 ,
    "A" : 10 , "B" : 11 , "C" : 12 , "D" : 13 , "E" : 14, "F": 15
}

def result(value):
    value_str = str(value).upper() # Convertir el valor a string para comparar con las claves del diccionario
    if value_str in hexaset:
        return hexaset [value_str]
    else:
        return 'this is not valid'
         

print(result("A"))




