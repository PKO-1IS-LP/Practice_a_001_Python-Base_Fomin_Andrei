N = int(input("Введите трехзначное число: "))

if 100 <= N <= 999:
    hundreds = N//100
    tens = N//10 % 10
    units = N % 10

    sum = hundreds + tens + units

    print(f'Сумма: {hundreds} + {tens} + {units} = {sum}')

else:
    print("Нужно трехзначное число!")