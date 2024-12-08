"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""
from package_lab4.lab2 import task2_4, task2_3, task2_2, task2_1
from package_lab4.lab3 import task3_1, task3_2, task3_3


def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
                        choice_lab - выбранный номер лабы
    """
    choice_lab = int(input('Выберите 2 или 3 лабороторная: '))
    choice_task = int(input('Выбирите номер задания в лабороторной работе: '))

    return choice_lab, choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        if choice[0] == 2:

            #Вызов для лабораторной работы 2
            match choice[1]:

                case 1:
                    a = float(input("a = "))
                    b = float(input("b = "))
                    c = float(input("c = "))

                    task2_1(a, b, c)

                case 2:
                    x = int(input("Введите x: "))

                    print(f"isSpecial = {task2_2(x)}")

                case 3:
                    x = float(input("Введите x: "))

                    print(f"y = {task2_3(x):+6.3f}")

                case 4:
                    dw = int(input("Введите день недели: "))
                    task2_4(dw)

                case _:
                    break

        else:
            #Вызов для лабораторной работы 3
            match choice[1]:

                case 1:
                    task3_1()

                case 2:
                    x = int(input('Введите число: '))

                    task3_2(x)

                case 3:
                    Q = int(input("Введите число: "))

                    print(task3_3(Q))

                case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

