from random import randint


class CircularFIFO:
    """При создании кольцевого буфера необходимо указать размер"""
    def __init__(self, size: int):
        self.data = []
        self.size = size

    def put(self, x):
        if len(self.data) < self.size:
            self.data.append(x)
        else:
            self.data.pop(0)
            self.data.append(x)

    def get(self):
        if len(self.data) == 0:
            print('there is no elements in FIFO')
        else:
            return self.data[0]

    def get_with_del(self):
        if len(self.data) == 0:
            print('there is no elements in FIFO')
        else:
            return self.data.pop(0)

    def show(self):
        return self.data


def test_CircularFIFO():
    fifo = CircularFIFO(5)
    for _ in range(5):
        r = randint(0, 99)
        fifo.put(r)
    print(fifo.show())
    fifo.put(199)
    fifo.put(101)
    print(fifo.show())
    print(fifo.get())
    print(fifo.show())
    print(fifo.get_with_del())
    print(fifo.show())


if __name__ == '__main__':
    test_CircularFIFO()
