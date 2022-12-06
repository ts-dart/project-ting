class Queue:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return self.data

    def enqueue(self, value):
        if value is not None:
            self.data.append(value)
            return self.data

    def dequeue(self):
        if self.__len__() > 0:
            return self.data.pop(0)

    def search(self, index):
        ''' try:
            return self.data[index]
        except IndexError:
            raise IndexError '''

        if index < 0 or index > len(self.data):
            raise IndexError

        return self.data[index]
