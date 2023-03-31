class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.count + 1):
            yield i
            break


numbers = take_skip(2, 6)
for number in numbers:
    print(number, number)
