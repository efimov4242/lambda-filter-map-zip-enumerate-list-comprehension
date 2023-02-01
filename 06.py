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