from random import randint


class Set:
    def __init__(self, n):
        self.n = n
        self.list = None

    def create_list(self):
        self.list = [randint(0, 500) for i in range(self.n)]

    def get_list(self):
        return self.list

    def summa(self):
        b = float(sum(self.list[1::2]))
        return b

    def show_list(self):
        print(*self.list)

    def show_summa(self):
        print(self.summa())
