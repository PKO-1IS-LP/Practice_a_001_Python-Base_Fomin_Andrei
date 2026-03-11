X = float(input("Введите X: "))

if X>0:
    res = X - int(X)
    first_digit = int(X*10)
    print(res)

elif X<0:
    print("Число отрицательное")
