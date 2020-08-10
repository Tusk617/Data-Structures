class Node:
    def __init__(self, value, next_node=None):
        #value is out current value we are interacting with
        self.value = value
        #next node references the next node in the linked list
        self.next_node = next_node

    #method to get value of node
    def get_value(self):
        return self.value
    #method to get the 'next_node'
    def get_next(self):
        return self.next_node
    #method to update the node's value
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        #check if linked list is empty
        if self.head is None and self.tail is None:
            #if both are empty, they both must share this value
            self.head = new_node
            self.tail = new_node
        #otherwise, the list has at least one node
        else:
            #update last node's 'next_node' to be the new_node
            self.tail.set_next(new_node)
            #update 'self.tail' to point to the new node we just added
            self.tail = new_node
    def remove_from_tail(self)
        # check if linkedl ist is empty
        if self.head is None and self.tail is None:
            return None

        #check if linkedl ist has only one node
        if self.head == self.tail:
            #store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val




ll = LinkedList()
ll.add_to_tail(5)

# ll = Node(5)

# ll.set_next(Node(7))
# ll.next_node.set_next(Node(18))
# ll.next_node.next_node.set_next(Node(22))