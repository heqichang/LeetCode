class MyCircularQueue:
    __list = []
    __max = 0
    __head = -1
    __tail = -1

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__max = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.__head = 0
            self.__tail = 0
            if len(self.__list) < 1:
                self.__list.append(value)
            else:
                self.__list[0] = value
        else:
            self.__tail = (self.__tail + 1) % self.__max
            if len(self.__list) < self.__max and self.__tail >= len(self.__list):
                self.__list.append(value)
            else:
                self.__list[self.__tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            if self.__head == self.__tail:
                self.__head = -1
                self.__tail = -1
            else:
                self.__head = (self.__head + 1) % self.__max

            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if (self.isEmpty()):
            return -1
        return self.__list[self.__head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if (self.isEmpty()):
            return -1
        return self.__list[self.__tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__head == -1 and self.__tail == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.__tail + 1) % self.__max == self.__head


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(6)
param_1 = obj.enQueue(6)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
param_4 = obj.Rear()
print(param_4)

