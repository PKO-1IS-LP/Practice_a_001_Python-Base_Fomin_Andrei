N1 = int(input("Введите первое число: "))
N2 = int(input("Введите второе число: "))

result = 0

if N1 > N2:
    result = 1
    print(result)

elif N1 < N2:
    result = 2
    print(result)

elif N1 == N2:
    result = 0
    print(result)