mas = []
print("Введите элементы массива (последний элемент должен быть равен 0): ")

while True:
    num = int(input())
    if num == 0:
        break
    mas.append(num)

print("Чётные элементы: ")
for num in mas:
    if num % 2 == 0:
        print(num, end=' ')