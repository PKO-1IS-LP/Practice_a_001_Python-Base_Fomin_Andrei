def IsPointInSquare(x,y):
    return (x + 1)**2 + (y-1)**2 <= 4 and -x -y <= 0 and (-2*x+y>=2 or (-x -y >= 0 and -2*x+y<=2))

x = float(input("Введите X: "))
y = float(input("Введите Y: "))

if IsPointInSquare(x,y):
    print("Попадает")
else:
    print("Не попадает")