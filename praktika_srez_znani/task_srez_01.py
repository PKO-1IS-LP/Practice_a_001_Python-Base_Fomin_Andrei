N = int(input("Введите число: "))

if N <= 10000:
    last_number = N % 10
    print(last_number)
else:
    print("Число выходит за границу!")
