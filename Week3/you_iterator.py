class TestIters:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter=> ', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data


# Example usage of the TestIters class with a sample sequence.
ito = TestIters([1, 2, 3])

# Optional: iterate over the instance to demonstrate the iterator protocol
for item in ito:
    print(item)

