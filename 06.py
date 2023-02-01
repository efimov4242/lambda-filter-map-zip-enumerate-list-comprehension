# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# def is_Weekend_Day():
# 	print("Введите день недели: ")
# 	day_Number = int(input())

# 	while(day_Number <= 0 or day_Number > 7):
# 		print("Введите число от 0 до 7: ")
# 		day_Number = int(input())

# 	if day_Number > 0 and day_Number <= 5:
# 		print ("Нет")
# 	if day_Number > 5 and day_Number <= 7:
# 		print ("Да")
# is_Weekend_Day()

day_week = [i for i in range(1, 8)]
a = int(input("Введите номер дня недели: "))
if a in day_week and 0 < a < 6:
	print("Нет")
else:
	print('Да')
	
	
# # Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# # Пример:

# # - A (3,6); B (2,1) -> 5,09
# # - A (7,-5); B (1,-1) -> 7,21

# def printDistance(ax, bx, ay, by):
# 	a_catet = ax - bx
# 	b_catet = ay - by
# 	hypotenuse = a_catet * a_catet + b_catet * b_catet
# 	print(round(hypotenuse ** (0.5), 3))


a = lambda ax, bx, ay, by : ((ax - bx)**2 + (ay - by)**2)**0.5

print(round(a(1, 2, 3, 4), 3))


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# def getSumNumb(numb):
# 	sum = 0
# 	if numb == int(numb):
# 		while (0 < numb):
# 			sum += int(numb) % 10
# 			numb /= 10
# 		return int(sum)
# 	else:
# 		for char in str(numb):
# 			if char != '.':
# 				sum += int(char)
# 		return sum

# print(getSumNumb(232))

a = input()

my_list = [i for i in a]
new_list = list(filter(lambda x: (x != '.') , my_list))
new_list = list(map(int, new_list))
print(sum(new_list))


# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = 4
# lst = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# print(f'Последовательность: {lst}')
# print(f'Сумма: {round(sum(lst), 2)}')

n = 4
a = lambda x: round((1+1/x)**x, 2)
lst = [a(i) for i in range(1, n+1)]
print(f'Последовательность: {lst}')
print(f'Сумма: {round(sum(lst), 2)}')


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def get_some_list(lenght = 5, min_value = 1, max_value = 9):
# 	list = [RI(min_value, max_value) for i in range(lenght)]
# 	return list

# def get_sum_odd_elements(list):
# 	sum = 0
# 	for i in range(0, len(list), 2):
# 		sum += list[i]
# 	return sum

# new_list = get_some_list()

# print(new_list)
# print(get_sum_odd_elements(new_list))

from random import randint as RI
list = [RI(0, 20) for i in range(10) if i % 2 != 0]
print(sum(list))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 5, 6]
# new_list = []

# for i in range(len(list) - 2):
#     new_list.append(list[i] * list[len(list) - i - 1])

# print(new_list)


list1 = [2, 3, 5, 6]
new_list = [list1[i] * list1[len(list1) - i - 1] for i in range(len(list1) - 2)]
print(new_list)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.3, 3.1, 5.0, 10.025]

# right_elements = []

# for i in list:
# 	right = i - int(i)
# 	right = round(right, 2)
# 	if right > 0: right_elements.append(right)

# print(round(max(right_elements) - min(right_elements), 2))

import random

list1 = [round(random.random(), 3) for i in range(10)]

right_elements = [round(i - int(i), 2) for i in list1 if i > 0]

new_list = list(filter(lambda x: x > 0, right_elements))

print(max(new_list) - min(new_list))
