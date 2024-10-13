import random
import time


# Я считаю, что лучший вариант - это встроенная функция sorted
# В-первых: данная функция написана на С и использует оптимизированный алгоритм,
# что позволяет выигрывать по скорости у базовых алгоритмов сортировки
# Во-вторых: данная функция сохраняет порядок элементов с одинаковым значением, что может быть важно.
# Также для сравнения я привел базовый алгоритм сортировки вставкой для сравнения быстродействия
# Ниже приведенны тесты по сортировке 10000 элементов с оценкой временных затрат.


def fastest_sort(N: list):
    """Сортировка встроенной функцией"""
    return sorted(N)


def insert_sort(N: list):  # O(N*N)
    """Сортировка вставкой с временной переменной"""
    for i in range(len(N)):
        j = i - 1
        temp = N[i]
        while N[j] > temp and j >= 0:
            N[j + 1] = N[j]
            j -= 1
        N[j + 1] = temp
    return N


def sort_test(func, test_list: list):  # O(N*N)
    chk = sorted(test_list)
    s = time.time()
    result = func(test_list)
    f = time.time()
    print(f'Тестирование "{func.__doc__}" успешно пройдено. Время, затраченное на сортировку: {(f-s)*1000} миллисекунд'
          if chk == result else f'Тестирование "{func.__doc__}" провалено. ')


if __name__ == '__main__':
    sort_test(insert_sort, [random.randint(0, 999) for _ in range(10000)])
    sort_test(insert_sort, [i for i in range(1000)])
    sort_test(fastest_sort, [random.randint(0, 999) for _ in range(10000)])
    sort_test(fastest_sort, [i for i in range(1000)])
