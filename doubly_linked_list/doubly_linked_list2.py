"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        newNode = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        deletedNode = self.head.value
        self.length -= 1
        self.delete(self.head)
        return deletedNode
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newNode = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        deletedNode = self.tail.value
        self.length -= 1
        self.delete(self.tail)
        return deletedNode
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        currentVal = node

        if currentVal is not None:
            currentVal.next.prev = currentVal.prev
            currentVal.next = None
            currentVal.prev = self.tail
            self.head.prev = currentVal
            self.head = currentVal
        pass


        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        currentVal = node

        if currentVal.prev is None:
            currentVal.next = self.head
        elif currentVal.next is None:
            self.add_to_tail(currentVal)


        # if currentVal is not None:
        #     currentVal.next.prev = currentVal.prev
        #     currentVal.next = None
        #     currentVal.prev = self.tail
        #     self.tail.next = currentVal
        #     self.tail = currentVal


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return
        elif node is self.head:
            self.head = self.head.next
            self.delete(node)
        elif node is self.tail:
            self.tail = self.tail.prev
            self.delete(node)
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.delete(node)
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass