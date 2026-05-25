class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.pointer = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.pointer == self.capacity:
            self.resize()
        self.array[self.pointer] = n
        self.pointer += 1

    def popback(self) -> int:
        if self.pointer >= 0:
            n = self.array[self.pointer-1]
            self.pointer -=1
            return n

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.pointer):
            new_arr[i]= self.array[i]
        self.array = new_arr

    def getSize(self) -> int:
        return self.pointer
    
    def getCapacity(self) -> int:
        return self.capacity