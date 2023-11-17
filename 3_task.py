#  Задача
# Вывести на экран сумму всех цифр заданного числа
# дано: 123 -> вывод: 6
# дано: 337 -> вывод: 13
def info(x):
    info=0
    while x>0:
        info +=x%10
        x = x // 10
    return info
dano1=123
dano2=337
print(info(dano1))
print(info(dano2))

