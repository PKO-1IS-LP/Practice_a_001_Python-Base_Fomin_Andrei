import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(t=1.5):
    time.sleep(t)

def show_main_menu():
    clear()
    print("\n--- Главное меню ---")
    print("1. Работа в Houdini")
    print("2. Прохождение курсов по Houdini")
    print("3. Выход")

def work_houdini():
    clear()
    print("\n--- Работа в Houdini ---")
    print("1. Симуляции")
    print("2. Настройка освещения в сцене")
    print("3. Назад")

def work_houdini_simulations():
    clear()
    print("\n--- Симуляции ---")
    print("1. Симуляция огня")
    print("2. Симуляция воды")
    print("3. Назад")

def work_houdini_light():
    clear()
    print("\n--- Настройка освещения в сцене ---")
    print("1. Поставить источник света Area light")
    print("2. Создать volume для рассеивания света")
    print("3. Назад")

def cource_houdini():
    clear()
    print("\n--- Прохождение курсов по Houdini ---")
    print("1. Курс по настройкам в рендере Karma")
    print("2. Курс по симуляции огня")
    print("3. Назад")

def cource_houdini_karma():
    clear()
    print("\n--- Курс по настройкам в рендере Karma ---")
    print("1. Урок 12: Разница между CPU и GPU рендером")
    print("2. Урок 45: Настройка цветового пространства")
    print("3. Назад")

def cource_houdini_fire_simulation():
    clear()
    print("\n--- Курс по симуляции огня ---")
    print("1. Урок 7: Настройка скорости горения")
    print("2. Урок 56: Кэширование симуляции")
    print("3. Назад")

def main():
    while True:
        show_main_menu()
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            while True:
                work_houdini()
                sub = input("→ ").strip()

                if sub == "1":
                    while True:
                        work_houdini_simulations()
                        sim = input("→ ").strip()

                        if sim == "1":
                            clear()
                            print("Запуск симуляции огня...")
                            pause(2)
                        elif sim == "2":
                            clear()
                            print("Запуск симуляции воды...")
                            pause(2)
                        elif sim == "3":
                            break
                        else:
                            clear()
                            print("Неверный выбор")
                            pause(1.2)

                elif sub == "2":
                    while True:
                        work_houdini_light()
                        light = input("→ ").strip()

                        if light == "1":
                            clear()
                            print("Создание Area Light...")
                            pause(2)
                        elif light == "2":
                            clear()
                            print("Создание Volume для рассеивания...")
                            pause(2)
                        elif light == "3":
                            break
                        else:
                            clear()
                            print("Неверный выбор")
                            pause(1.2)

                elif sub == "3":
                    break
                else:
                    clear()
                    print("Неверный выбор")
                    pause(1.2)

        elif choice == "2":
            while True:
                cource_houdini()
                sub = input("→ ").strip()

                if sub == "1":
                    while True:
                        cource_houdini_karma()
                        karma = input("→ ").strip()

                        if karma == "1":
                            clear()
                            print("Изучаем разницу CPU и GPU рендера...")
                            pause(2)
                        elif karma == "2":
                            clear()
                            print("Изучаем цветовое пространство...")
                            pause(2)
                        elif karma == "3":
                            break
                        else:
                            clear()
                            print("Неверный выбор")
                            pause(1.2)

                elif sub == "2":
                    while True:
                        cource_houdini_fire_simulation()
                        fire = input("→ ").strip()

                        if fire == "1":
                            clear()
                            print("Изучаем настройку скорости горения...")
                            pause(2)
                        elif fire == "2":
                            clear()
                            print("Изучаем кэширование симуляции...")
                            pause(2)
                        elif fire == "3":
                            break
                        else:
                            clear()
                            print("Неверный выбор")
                            pause(1.2)

                elif sub == "3":
                    break
                else:
                    clear()
                    print("Неверный выбор")
                    pause(1.2)

        elif choice == "3":
            clear()
            print("До свидания, Андрей 🚀")
            pause(1.5)
            break

        else:
            clear()
            print("Неверный выбор")
            pause(1.2)

if __name__ == "__main__":
    main()