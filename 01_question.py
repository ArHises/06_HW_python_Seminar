"""
Задача 30:  
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

"""

def fill_list(some_list):
    some_list.append(int(input("Enter 1st element: ")))
    print(some_list)
    d = int(input("Enter progretion: "))
    n = int(input("Enter length: "))
    for i in range(1, n):
        some_list.append(some_list[0] + i * d)
    
    return some_list

some_list = list()
some_list = fill_list(some_list)
print(some_list)