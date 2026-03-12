#Ввод символа пользователем
s = input("Введите данные: ")

#Проверка на цифру и вывод в консоль
if len(s)==1 and s.isdigit():
    print("Yes")
else:
    print("No")