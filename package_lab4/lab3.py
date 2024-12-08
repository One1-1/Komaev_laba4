def task3_1():
    '''
    Задание:
    Дана последовательность из 20 целых чисел. Определить со скольких
    простых чисел она начинается.

    :param : None
    :return: None
    '''
    sum = 0
    for i in range(20):
        count = 0
        x = int(input("Введите число: "))
        for j in range(x):
            if x % (j + 1) == 0:
                count += 1
        if i - 1 == sum:
            if count == 2:
                sum += 1
    if sum > 0:
        sum += 1
    print(sum)


def task3_2(x):
    '''
    Задание:
    Дана последовательность целых чисел, за которой следует ноль.
    Определить чередуются ли в ней четные и нечетные числа.

    :param x: вводимое число
    :return: None
    '''
    kn = x % 2 == 0
    while x == 0:
        x = int(input())
        if (kn and x % 2 == 0) or not (kn and x % 2 == 0):
            print("Последовательность не чередуется")
            break
        else:
            kn = x % 2 == 0
        if x == 0:
            print("Последовательность чередуется")
            break


def task3_3(Q):
    '''
    Задание:
    Найти все простые числа Фибоначчи, не превышающие Q. ((a1=1, a2=1,
    ai=ai-1+ai-2). (Числа Фибоначчи определяются следующим образом: a1=
    a2=1, при i>=3 ai=ai-1+ai-2 )

    :param Q:
    :return: a1
    '''
    a1 = 1
    a2 = 1
    a3 = 0
    while Q > a2:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
    return a1
