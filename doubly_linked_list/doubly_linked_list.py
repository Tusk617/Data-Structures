"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        # if self.next is None and self.prev is None:
        #     return
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
        # pass
        newHead = ListNode(value)
        self.length += 1
        #is the list empty?
        if self.head == None:
            self.head = newHead
            self.tail = newHead
        #else, the list is not empty so we must organize the data
        else:
            self.head.prev = newHead
            newHead.next = self.head
            self.head = newHead
            # return newHead
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # pass
        self.length -= 1
        #is the list empty?
        if self.head == None:
            return None
        #if the head and tail are the same node, then they must both be set to None
        elif self.head == self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        #else, there is more than one item in the list
        else:
            val = self.head.value
            newHead = self.head.next
            self.head = newHead
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # pass

        newTail = ListNode(value)
        self.length += 1
        #is the list empty?
        if self.head == None:
            self.head = newTail
            self.tail = newTail
        #if not empty, then there is at least one value in the list
        else:
            # oldTail = self.tail
            self.tail.next = newTail
            newTail.prev = self.tail
            self.tail = newTail
            return newTail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # pass
        self.length -= 1

        #is the lsit empty?
        if self.head == None:
            return None
        #else, there is at least one node
        elif self.head == self.tail:
            val = self.tail.value
            self.head = None
            self.tail = None
            return val
        #if there is more than one node
        else:
            val = self.tail.value
            newTail = self.tail.prev
            self.tail = newTail
            return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # pass
        print(node.value)
        if node is self.head:
            return
        elif node is self.tail:
            self.remove_from_tail()
            self.add_to_head(node.value)
        else:
            self.add_to_head(node.value)
            self.delete(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # pass

        if node is self.tail:
            return
        elif node is self.head:
            self.remove_from_head()
            self.add_to_tail(node.value)
        else:
            self.add_to_tail(node.value)
            self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        if self.head is None and self.tail is None:
            return
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # pass
        maxVal = self.head.value
        current = self.head
        if self.head is None:
            return None
        while current:
            if maxVal < current.value:
                maxVal = current.value
            current = current.next
        return maxVal