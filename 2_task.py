#  Задача
# Вывести на экран:
# - сумму всех элементов списка
# - среднее арифметическое всех элементов списка
# - максимальное значение списка
# - минимальное значение списка


def info(arr):
    summ=sum(arr)
    sr=sum(arr) / len(arr)
    print(f'Сумма:{sum(arr)} ')
    print(f'Среднее арифметическое: {sum(arr) / len(arr)} ')
    print(f'Минимальное значение: {min(arr)}')
    print(f'Максимальное значение: {max(arr)}')
    return summ,sr
'''
first_arr=[]
for i in range(10):
    num=int(input(f"Введите {i} элемент:"))
    first_arr.append(num)

info(first_arr)
'''


second_arr=[12,5,456,-15,64,54,-24]
info(second_arr)
rez=print(info(second_arr)[0])
rez2=print(info(second_arr)[1])
print(rez)
print(rez2)


