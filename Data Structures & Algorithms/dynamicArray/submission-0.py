class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.lst = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.lst[i]

    def set(self, i: int, n: int) -> None:
        self.lst[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.lst[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        
        return self.lst[self.length]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_lst = [0] * self.capacity

        for i in range(self.length):
            new_lst[i] = self.lst[i]
        self.lst = new_lst

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
