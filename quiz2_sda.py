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

    def isEmpty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
    
    def printQueue(self):
        for i in range(len(self.data)):
            print(f'{i+1}. {self.data[i]}')
    
    def clear(self):
        self.data = []
    
def printMenu():
    print('1. Add new vehicle to queue')
    print('2. Remove vehicle from queue')
    print('3. Vehicle terdepan')
    print('4. Check is queue empty')
    print('5. Length of queue')
    print('6. Exit program')

if __name__ == "__main__":
    print('>>> Welcome to Parking System ')
    qq = Queue()

    while True:
        printMenu()
        menu = int(input())

        if menu == 1:
            a = input("Input to queue: ")
            qq.enqueue(a)

        elif menu == 2:
            print(qq.dequeue(), 'Removed from queue')

        elif menu == 3:
            print('kendaraan terdepan adalah:', qq.front() )

        elif menu == 4:
            if qq.isEmpty() == True:
                print('Queue is empty')

        elif menu == 5:
            print('length of queue:', qq.size())
        
        elif menu == 6:
            print('>>> Thank you for using our program')
            print('>>> See You')
            break

        else:
            print('>>> Invalid Menu!')
            
            
            
            
            
           
##################################################################
class Nasabah:
    def __init__(self, name, prio):
        self.name = name
        self.prio = prio

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)

    def front(self):
        if self.isEmpty():
            return None
        else:
            maxVal = 0
            for i in range(len(self.queue)):
                if self.queue[i].prio > self.queue[maxVal].prio:
                    maxVal = i
            item = self.queue[maxVal]
            return item

    def size(self):
        return len(self.queue)

    def delete(self):
        if self.isEmpty():
            return None
        else:
            maxVal = 0
            for i in range(len(self.queue)):
                if self.queue[i].prio > self.queue[maxVal].prio:
                    maxVal = i
            item = self.queue[maxVal]
            del self.queue[maxVal]
            return item
        
def printMenu():
    print('1. Add new Nasabah to queue')
    print('2. Remove Nasabah from queue')
    print('3. Nasabah prioritas tertinggi')
    print('4. Check is queue empty')
    print('5. Length of queue')
    print('6. Exit program')

if __name__ == "__main__":
    print('>>> Welcome to Bank System ')
    qq = PriorityQueue()

    while True:
        printMenu()
        menu = int(input())

        if menu == 1:
            a = input("Input name: ")
            b = int(input("Input priority: "))
            c = Nasabah(a, b)
            qq.insert(c)

        elif menu == 2:
            print(qq.delete(), 'Removed from queue')

        elif menu == 3:
            print('Nasabah prioritas tertinggi adalah:', qq.front().name )

        elif menu == 4:
            if qq.isEmpty() == True:
                print('Queue is empty')

        elif menu == 5:
            print('Banyaknya nasabah:', qq.size())
        
        elif menu == 6:
            print('>>> Thank you for using our program')
            print('>>> See You')
            break

        else:
            print('>>> Invalid Menu!')
