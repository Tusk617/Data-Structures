"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size
        pass

    def push(self, value):
        self.storage.append(value)
        self.size = len(self.storage)
        pass

    def pop(self):
        if self.size == 0:
            return None
        else:
            popStorage = self.storage.pop()
            self.size = len(self.storage)
            return popStorage
        pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addToTail(self,value):
        newNode = Node(value)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode
    def removeHead(self):
        if self.head is None and self.tail is None:
            return
        if not self.head.getNext():
            head = self.head
            self.head = None
            self.tail = None
            return head.getValue()
        val = self.head.getValue()
        self.head = self.head.getNext()
        return val
    
    def removeTail(self):
        if self.head is None:
            return
        current = self.head
        while current.getNext() and current.getNext() is not self.tail:
            current = current.getNext()
        value = self.tail.getValue()
        self.tail = current
        self.tail.setNext(None)
        return value

    def contains(self, value):
        if not self.head:
            return False
    
        current = self.head
        while current:
            if current.getValue() == value:
                return True
            current = current.getNext()
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.getValue()
        current = self.head.getNext()
        while current:
            if current.getValue() > max_value:
                max_value = current.getValue()
            current = current.getNext()
        return max_value