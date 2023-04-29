"""
Задача 32: 
Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

"""

def find_segment(some_list, min = 5, max = 10):
    for i in range(len(some_list)):
        if some_list[i] >= min and some_list[i] <= max:
            print(i)

some_list = [1,2,3,4,5,6,7,8,9,10]
find_segment(some_list)