#Задайте переменные разных типов данных:
immutable_var = (1,2,3,"cake","string")
print(immutable_var)
#immutable_var [0] = 32 (кортеж относится к неизменяемым типам данных, кортеж не поддерживает обращение по элементам

#Изменение значений переменных:
mutable_list = [1,2,3,"slim","table","slow"]
print(mutable_list)
mutable_list[0] = 5
mutable_list[1] = 6
mutable_list[2] = 7
mutable_list[3] = "Big"
mutable_list[4] = "Baby"
mutable_list[5] = "Tape"
print(mutable_list)