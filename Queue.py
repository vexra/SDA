class Queue:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return str(self.data)

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        return self.data.pop(0)

    def front(self):
        return self.data[0]
    
    def rear(self):
        return self.data[-1]
    


if __name__ == "__main__":
    qq = Queue()
    print(qq)
    qq.enqueue(200)
    qq.enqueue(500)
    print(qq.front())
    print(qq.rear())
    qq.dequeue()
    print(qq.front())
    print(qq.rear())
