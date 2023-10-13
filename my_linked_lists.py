class Node():
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node = None

class LinkedList():
    def __init__(self, value: int) -> None:
        self.head: Node = Node(value)
        self.tail: Node = self.head
        self.length: int = 1
    
    def append(self, value: int) -> None:
        newNode: Node = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value: int) -> None:
        newNode: Node = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self, index: int, value: int) -> None:
        if index<0:
            return

        if index==0:
            self.prepend(value)
            return
        
        if index>=self.length:
            self.append(value)
            return
        
        newNode: Node = Node(value)
        currentNode: Node = self.traverseToIndex(index-1)
        nextNode: Node = currentNode.next

        currentNode.next = newNode # append for currentNode
        newNode.next = nextNode # prepend for nextNode
    
        self.length += 1

    def remove(self, index: int) -> None:
        if self.length==1:
            return
        if index>=self.length or index<0:
            return
        if index == 0:
            self.head = self.head.next # removing current head
        else:
            currentNode: Node = self.traverseToIndex(index-1)
            unwantedNode: Node = currentNode.next
            currentNode.next = unwantedNode.next # removing unwantedNode
        self.length -= 1
    
    def traverseToIndex(self, index: int) -> Node:
        currentNode: Node = self.head
        for i in range(index):
            currentNode = currentNode.next
        return currentNode
        
    def __str__(self) -> str:
        output: str = f"Linked List (length:{self.length}):\n"
        currentNode: Node = self.head
        
        while(currentNode!=None):
            output += f"\tcurrentNode.value = {currentNode.value} \n"
            currentNode = currentNode.next

        return output      

myLinkedList1 = LinkedList(10)
myLinkedList1.append(5)
myLinkedList1.append(16)
myLinkedList1.prepend(1)

myLinkedList1.insert(2, 83)
print (myLinkedList1)
myLinkedList1.remove(0)
print (myLinkedList1)

