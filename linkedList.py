class Node:
    def __init__(self):
        self.next = None;
        self.data = 0;


# def printLinkedList(node):
#     currNode = node
#     while True:
#         print(currNode.data);
#         currNode = currNode.next;
#         if currNode.next is None:
#             print(currNode.data);
#             break;

class LinkedList :
    def __init__(self):
        self.head = None;
    #delete items from beginning of the list
    def deleteHead(self):
        temp = self.head;
        self.head = self.head.next;
        temp.next = None;
        temp = None;
    #delete items from end of the list
    def deleteTail(self):
        tail = self.head;
        while True:
            if tail.next.next is None :
                break;
            tail = tail.next;
        temp = tail.next;
        tail.next = None;
        temp = None;
    #delete a particular node
    def deleteNode(self,data):
        node = self.head;
        while True:
            if node.next.data == data:
                break;
            node = node.next;
        temp = node.next;
        node.next = temp.next;
        temp.next = None;
        temp = None;
                
    #sets head or enters a new node at head
    def insertHead(self,data):
        if self.head is None:
            self.head = Node()
            self.head.data = data;
        else :
            temp = self.head;
            newHead = Node();
            newHead.data = data;
            newHead.next = temp;
            self.head = newHead;
    # insert a node after the last node
    def insertTail(self,data):
        tail = self.head;
        while True:
            if tail.next is None:
                break
            tail = tail.next;
        newNode = Node();
        newNode.data = data;
        tail.next = newNode;

    # insert after a particular node
    def insertAfter(self,after,data):
        node = self.head;
        while True:
            if node.data == after:
                break;
            node = node.next;
        temp = node;
        newNode = Node();
        newNode.data = data;
        newNode.next = node.next;
        temp.next = newNode;
    #prints elements of linked list
    def print(self):
        temp = self.head;
        while True:
            if temp.next is None:
                print(temp.data);
                break;
            print(temp.data);
            temp = temp.next;
            
    


def main():
    li = LinkedList();
    li.insertHead(1);
    li.insertHead(2);
    li.insertHead(3);
    li.insertTail(4);
    li.insertTail(5);
    li.insertAfter(1,10);
    li.insertAfter(10,12);
    li.deleteHead();
    li.deleteNode(1);
    li.deleteTail();
    li.print();


if __name__ == '__main__':
    main();