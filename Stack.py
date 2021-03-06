class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[len(self.items)-1]

    