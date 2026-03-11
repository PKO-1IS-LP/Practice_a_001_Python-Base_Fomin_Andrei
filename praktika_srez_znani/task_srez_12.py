N1 = int(input("Введите первое число: "))
N2 = int(input("Введите второе число: "))
N3 = int(input("Введите третье число: "))

if N1 > N2 and N1 > N3:
    print(f"{N1} наибольшее число")

elif N2 > N1 and N2 > N3:
    print(f"{N2} наибольшее число")

else:
    print(f"{N3} наибольшее число")