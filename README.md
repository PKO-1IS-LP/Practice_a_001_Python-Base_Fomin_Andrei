# Practice_a_001_Python-Base_Fomin_Andrei

# 🐍 Python Practice — Учебные проекты Андрея

Добро пожаловать в мой личный **сборник учебных скриптов** по Python!  
Здесь собраны небольшие программы, которые я писал в процессе изучения основ языка — от переменных до работы со строками, циклами и даже графическим интерфейсом.

---


---

## 🔰 Базовые конструкции

### 01_int.py — Ввод чисел
```python
s = 25
print(s)  # 25

s = input()  # Ввод: 42
number = int(s)
print(number)  # 42
```

### 02_range.py — Генерация последовательности
```python
for i in range(55, 99, 3):
    print(i)  # 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97
```

### 03_len.py — Длина строк и списков
```python
s = "hello"
print(len(s))  # 5

s = "Водопад"
print(len(s))  # 7

numbers = [10, 20, 30]
print(len(numbers))  # 3

numbers = [3, 6, 3, 12, 54, 87, 10]
print(len(numbers))  # 7
```

### 04_list.py — Работа со списками
```python
numbers = list(map(int, ["1", "2", "3"]))
print(numbers)  # [1, 2, 3]

spisok = list(map(float, ["0.4", "0.1", "1.64", "8.6473"]))
print(spisok)  # [0.4, 0.1, 1.64, 8.6473]

x = list("hello")
print(x)  # ['h', 'e', 'l', 'l', 'o']

spisok_1 = list("Добрый")
spisok_2 = list("день")
summa = spisok_1 + spisok_2
print(summa)  # ['Д', 'о', 'б', 'р', 'ы', 'й', 'д', 'е', 'н', 'ь']
```

### 04_list_task_01.py — Преобразование типов
```python
a = 5
b = '5'

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>

b = int(b)
print(a + b)  # 10

a = str(a)
b = str(b)
print(a + b)  # 55
```

### 04_list_task_02.py — Сложение чисел и строк
```python
a = 23
b = 34
c = 12

print(a + b + c)  # 69

a = str(a)
b = str(b)
c = str(c)
print(a + b + c)  # 233412
```

---

## 🧰 Полезные функции

### 05_map.py — Применение map()
```python
float_numbers = [1.5, 2.7, 3.9, 4.2, 5.0]
print(float_numbers)  # [1.5, 2.7, 3.9, 4.2, 5.0]
print(list(map(int, float_numbers)))  # [1, 2, 3, 4, 5]
```

### 06_split.py — Разделение строк
```python
s = "192.168.1.1"
print(s.split("."))  # ['192', '168', '1', '1']

date = "2024-12-31"
print(date.split("-"))  # ['2024', '12', '31']
```

### 07_isdigit.py — Проверка на цифры
```python
a = "23"
print(a.isdigit())  # True
print(type(a.isdigit()))  # <class 'bool'>

b = "t"
print(b.isdigit())  # False
```

### 08_isalpha.py — Проверка на буквы
```python
a = "23"
print(a.isalpha())  # False

b = "t"
print(b.isalpha())  # True
```

### 09_isupper.py — Проверка на верхний регистр
```python
a = input(str())  # Ввод: B
print(f'''Введите значение 'a':{a}''')
print(f'''Результат isupper():{a.isupper()}''')  # True
```

### 10_islower.py — Проверка на нижний регистр
```python
a = input(str())  # Ввод: b
print(f'''Введите значение 'a':{a}''')
print(f'''Результат islower():{a.islower()}''')  # True
```

### 11_append.py — Добавление в список
```python
products = ['банан', 'яблоко', 'кефир', 'клубника', 'молоко']
print(products)  # ['банан', 'яблоко', 'кефир', 'клубника', 'молоко']
products.append('шоколад')
print(products)  # ['банан', 'яблоко', 'кефир', 'клубника', 'молоко', 'шоколад']
```

---

## 🔁 Циклы и условия

### 12_break.py — Прерывание цикла
```python
for i in range(33, 506):
    if i % 127 == 0:
        break
    print(i)  # 33...125 (до первого числа, кратного 127)
```

### 12_break_task_01.py — Чётные и нечётные
```python
# Чётные числа от 1 до 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)  # 2, 4, 6, ..., 100

# Нечётные числа от 1 до 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)  # 1, 3, 5, ..., 99
```

### 13_logic_operators.py — Логические операторы
```python
x = 34
y = x > 0 and x < 45
print(y)  # True
```

### 14_operator_%.py — Оператор %
```python
for i in range(1, 31):
    if i % 2 != 0:  # нечётные числа
        print(i)  # 1, 3, 5, ..., 29
```

---

## 📌 Индексы и срезы

### 15_index.py — Доступ по индексу
```python
s = 'HTTP encoding library list operations Parse yaml text hierarchy object nul'
print(s[3])   # P
print(s[20])  # g
print(s[25])  # r
print(s[0])   # H
print(s[8])   # c
print(s[35])  # r
```

### 16_srez_.py — Проверка палиндрома
```python
s = "level"

i = 0
print(s[i])                 # l
print(s[len(s) - 1 - i])    # l

i = 1
print(s[i])                 # e
print(s[len(s) - 1 - i])    # e

i = 2
print(s[i])                 # v
print(s[len(s) - 1 - i])    # v
```

### 16_srez_task_01.py — Проверка слова
```python
word = input("Ввод: ")  # Ввод: level
s = str(word)
len = len(word)
for i in range(1//2):
    if s[i] != s[-1-i]:
        print("Не он")
else:
    print("Он")  # Он
```

### 17_perebor_spiska.py — Перебор списка
```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)  # 1, 2, 3, 4, 5
```

---

## 🔧 Функции

### def_functions.py — Простая функция
```python
def greet():
    print("Привет, студент!")

greet()  # Привет, студент! (10 раз)
```

### def_min.py — Поиск минимума
```python
def min(a, b):
    return a if a < b else b

def min3(a, b, c):
    return min(min(a, b), c)

def min4(a, b, c, d):
    return min(min3(a, b, c), d)

# Ввод: 5, 2, 8
print(f"Минимум из трех чисел: {min3(5, 2, 8)}")  # 2

# Ввод: 10, 3, 7, 1
print(f"Минимум из четырех чисел: {min4(10, 3, 7, 1)}")  # 1
```

### def_task.py — Функция с параметрами
```python
def fun(name, age, city):
    print(f'''{name}, какое прекрасное имя. {age} это прекрасный возраст! {city} лучший город для карьеры''')

fun(name="Анна", age="25", city="Москва")
# Анна, какое прекрасное имя. 25 это прекрасный возраст! Москва лучший город для карьеры
```

---

## 📐 Геометрические задачи

### geo_task.py — Попадание в квадрат
```python
def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1

# Ввод: X: 0.5, Y: 0.5
if IsPointInSquare(0.5, 0.5):
    print("Попадает")  # Попадает

# Ввод: X: 2, Y: 2
if IsPointInSquare(2, 2):
    print("Попадает")
else:
    print("Не попадает")  # Не попадает
```

### geo_task_02.py — Сложная область
```python
def IsPointInSquare(x, y):
    return (x + 1)**2 + (y - 1)**2 <= 4 and -x - y <= 0 and (-2*x + y >= 2 or (-x - y >= 0 and -2*x + y <= 2))

# Ввод: X: 0, Y: 1
if IsPointInSquare(0, 1):
    print("Попадает")  # Попадает
```

### geo_task_03.py — Параболическая область
```python
def IsPointInSquare(x, y):
    return (y > x**2) or (-x**2 > y)

# Ввод: X: 0.5, Y: 0.3
if IsPointInSquare(0.5, 0.3):
    print("Попадает")  # Попадает (0.3 > 0.25)

# Ввод: X: 0.5, Y: 0.2
if IsPointInSquare(0.5, 0.2):
    print("Попадает")
else:
    print("Не попадает")  # Не попадает (0.2 < 0.25)
```

---

## 🧩 Простые задачи

### lite_task_01.py — Белочки и орешки (деление)
```python
n = int(input("Введите кол-во белочек: "))  # 5
k = int(input("Введите кол-во орешков: "))  # 17

if n > 10000 or k > 10000:
    print("Нельзя по заданию!")
else:
    res = k // n
    print(res)  # 3
```

### lite_task_02.py — Белочки и орешки (остаток)
```python
n = int(input("Введите кол-во белочек: "))  # 5
k = int(input("Введите кол-во орешков: "))  # 17

if n > 10000 or k > 10000:
    print("Нельзя по заданию!")
else:
    res = k % n
    print(res)  # 2
```

### lite_task_03.py — Последний символ
```python
s = input()  # Привет
print(s[-1])  # т
```

### task01.py — Подсчёт чётных и нечётных
```python
number = int(input("Введите число N: "))  # 10

chet_count = 0
nechet_count = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        chet_count += 1
    else:
        nechet_count += 1

print("Кол-во четных чисел: ", chet_count)    # 5
print("Кол-во нечетных чисел: ", nechet_count)  # 5
```

### task04.py — Поиск числа > 50
```python
number = int(input("Сколько чисел?: "))  # 3

f = False

for i in range(number):
    num = int(input(f'''Введите число {i+1}: '''))
    if num > 50:
        print("Больше 50: ", num)  # если ввести 75, то выведет
        f = True
        break

if not f:
    print("Не найдено: ")
```

### task06.py — Кратность 2 и 3
```python
N = int(input("Ввод: "))  # 20

count2 = 0
count3 = 0
count23 = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        count2 += 1
    if i % 3 == 0:
        count3 += 1
    if i % 2 == 0 and i % 3 == 0:
        count23 += 1

print(f'''
      на 2: {count2}   # 10
      на 3: {count3}   # 6
      на 2 и на 3: {count23}''')  # 3
```

### task14.py — Поиск символа в строке
```python
stroka = str(input("Введите строку: "))  # hello
simvol = str(input("Введите символ: "))  # l

index = -1

for i in range(len(stroka)):
    if stroka[i] == simvol:
        index = i
        break

if index != -1:
    print("Индекс первого вхождения: ", index)  # 2
else:
    print("Не найдено")
```

### task16.py — Удаление цифр из строки
```python
stroka = str(input("Введите строку: "))  # a1b2c3

res = ""

for simvol in stroka:
    if not simvol.isdigit():
        res += simvol

print("Строка без цифр: ", res)  # abc
```

---

## 🎮 Консольные меню

### task_console_menu.py — Меню для Houdini
Многоуровневое меню с навигацией по разделам:
- Работа в Houdini (симуляции, освещение)
- Прохождение курсов (Karma, симуляция огня)

### task_console_menu_2.py — Простое меню
```python
# --- МЕНЮ ---
# 1. Белочки и орешки
# 2. Последний символ
# 3. Выход
# Выберите: 1
# Сколько белочек? 5
# Сколько орешков? 17
# Каждая белочка получит: 3
```

---

## 🖼️ Графические интерфейсы (Tkinter)

### tkinter_task_11.py — Яркое приветствие
![Яркое приветствие](https://via.placeholder.com/500x200/FFFACD/800080?text=HELLO+WORLD!)

### tkinter_task_12.py — Три блока
Три цветных блока с надписями: Красный, Синий, Зелёный.

### tkinter_task_13.py — Меню
Вертикальное меню с кнопками: Главная, Профиль, Друзья, Сообщения, Настройки.

### tkinter_task_14.py — Профиль
Профиль пользователя с именем, ником и рамкой.

### tkinter_task_15.py — Загрузка
Индикатор загрузки с полосой прогресса.

### tkinter_task_17.py — Действие
Большая зелёная кнопка "НАЧАТЬ ИГРУ".

### tkinter_task_18.py — Результат
Овал с текстом "ГОТОВО!" и подписью.

---

## 🔄 Цикл while

### while.py — Простой while
```python
i = 1
while i <= 5:
    print(i)  # 1, 2, 3, 4, 5
    i += 1

i = 1
while i <= 10:
    print(f'''Число: {i}''')  # Число: 1 ... Число: 10
    i += 1
```

### while_task_01.py — Обратный отсчёт
```python
i = -1
while i >= -20:
    print("Число ", i)  # -1, -2, ..., -20
    i -= 1
```

### while_task_02.py — Чётные и нечётные
```python
# Чётные числа от 2 до 20
i = 2
while i <= 20:
    if i % 2 == 0:
        print(i)  # 2, 4, 6, ..., 20
    i += 1

# Нечётные числа от 1 до 21
i = 1
while i <= 21:
    if i % 2 != 0:
        print(i)  # 1, 3, 5, ..., 21
    i += 1
```

### while_task_03.py — Выход по 0
```python
i = ''
while i != '0':
    i = input("Введите число: ")  # Ввод: 5, 3, 0

print("Вы ввели 0!")
```

### while_true.py — Бесконечный цикл
```python
while True:
    word = input()
    print(f'''Введите слово {word}''')
    if word == "python" or word == "Python":
        print("Стоп! Вы ввели python")
        break
```

---

## 🚀 Как запустить

1. Склонируй репозиторий:
   ```bash
   git clone https://github.com/твой-логин/python-practice.git
   cd python-practice
   ```

2. Запусти любой скрипт:
   ```bash
   python3 01_int.py
   ```

---

## 📚 Что я изучил

- ✅ Переменные и типы данных
- ✅ Ввод и вывод
- ✅ Условные операторы
- ✅ Циклы for и while
- ✅ Списки и операции с ними
- ✅ Строки и методы строк
- ✅ Функции
- ✅ Работа с файлами
- ✅ Графический интерфейс Tkinter
- ✅ Математические задачи
- ✅ Логические операторы

---

## 📝 Заметки

Все программы написаны в учебных целях.  
Код может содержать комментарии на русском языке для лучшего понимания.

---

**Автор:** Андрей Фомин  
**Дата создания:** 2024-2025  
**Количество файлов:** 45+
