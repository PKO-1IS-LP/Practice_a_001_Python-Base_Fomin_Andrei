def IsPointInSquare(x,y):
    return (y > x**2) or (-x**2 > y)

x = float(input("Введите X: "))
y = float(input("Введите Y: "))

if IsPointInSquare(x,y):
    print("Попадает")
else:
    print("Не попадает")