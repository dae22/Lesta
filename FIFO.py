from random import randint


# При создании классов для буфера FIFO я использовал возможности стандартных списков.
# Первый класс CircularFIFO реализован с ограниченной размерностью, которая указывается при присваивании переменной.
# Второй класс ArrayFIFO реализован без ограничений размерности


class CircularFIFO:
    """При создании кольцевого буфера необходимо указать размер"""
    def __init__(self, size: int):
        self.data = []
        self.size = size

    def put(self, x):  # Добавление элемента в буфер, если количество элементов превысит доспустимое, первый элемент удаляется
        if len(self.data) < self.size:
            self.data.append(x)
        else:
            self.data.pop(0)
            self.data.append(x)

    def get(self):  # Получение первого элемента из буфера с его сохранением в буфере
        if len(self.data) == 0:
            print('there is no elements in FIFO')
        else:
            return self.data[0]

    def get_with_del(self):  # Получение первого элемента из буфера без сохранения в буфере
        if len(self.data) == 0:
            print('there is no elements in FIFO')
        else:
            return self.data.pop(0)

    def show(self):  # Функция для печати текущего буфера
        print(self.data)


class ArrayFIFO:
    def __init__(self):
        self.data = []

    def put(self, x):  # Добавление элекмента в буфер
        self.data.append(x)

    def get(self):  # Получение элемента из буфера с его сохранением в буфере
        if len(self.data) == 0:
            print('There is no elements in FIFO')
        else:
            return self.data[0]

    def get_with_del(self):  # Получение элемента из буфера без сохранения
        if len(self.data) == 0:
            print('There is no elements in FIFO')
        else:
            return self.data.pop(0)

    def show(self):  # Функция для печати текущего буфера
        print(self.data)


def test_CircularFIFO():
    fifo = CircularFIFO(5)
    for _ in range(5):
        r = randint(0, 99)
        fifo.put(r)
    fifo.show()
    fifo.put(199)
    fifo.put(101)
    fifo.show()
    print(fifo.get())
    fifo.show()
    print(fifo.get_with_del())
    fifo.show()


def test_ArrayFIFO():
    fifo = ArrayFIFO()
    for _ in range(10):
        r = randint(0, 99)
        fifo.put(r)
    fifo.show()
    fifo.put(199)
    fifo.put(101)
    fifo.show()
    print(fifo.get())
    fifo.show()
    print(fifo.get_with_del())
    fifo.show()


if __name__ == '__main__':
    test_CircularFIFO()
    print('-'*20)
    test_ArrayFIFO()
