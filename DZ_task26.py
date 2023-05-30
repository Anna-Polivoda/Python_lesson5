# Задача 26:  Посчитать факториал (произведение 1 до N)
# и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

n = int(input("Введите число N:"))

def fact(n):
    if n == 1:
        return 1
    return fact(n- 1)*n

print (fact(n))

def number(n):
    if n == 1:
        return 1
    return fact(n- 1)+n

print (number(n))