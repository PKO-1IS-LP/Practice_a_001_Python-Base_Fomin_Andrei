N = int(input("Введите двузначное число: "))

if  10 <= N <= 99:
    first_N = N // 10
    print(first_N)
else:
    print("Число не двузначное!")
