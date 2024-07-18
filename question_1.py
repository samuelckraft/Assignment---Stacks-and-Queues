#Task 1

class Stack:
    def __init__(self):
        self.items = []

#Task 2

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty:
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1] 

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


#Task 3
class Queue:
    def __init__(self):
        self.items = []

#Task 4

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0 
    
    def size(self):
        return len(self.items)
    

#Task 5

kitchen_orders = Stack()

customer_orders = Queue()

kitchen_orders.push('Double Hashbrowns Covered/Chunked/Country')
kitchen_orders.push('All-Star Special')

kitchen_orders.pop()
print(kitchen_orders.peek())

customer_orders.enqueue('All-Star Special')
customer_orders.enqueue('Double Hashbrowns Covered/Chunked/Country')

customer_orders.dequeue()
