class Node:
    def __init__(self):
        self.next = None;
        self.data = 0;
def printLinkedList(node):
    currNode = node
    while True:
        print(currNode.data);
        currNode = currNode.next;
        if currNode.next is None:
            print(currNode.data);
            break;
class LinkedList :
    def __init__(self):
        self.head = None;
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

    def print(self):
        temp = self.head;
        while True:
            if temp.next is None:
                print(temp.data);
                break;
            print(temp.data);
            temp = temp.next;
# reversing the linked list
def rev_linkList(head):
    n_head = head;
    temp_node = None;
    while True:
        if n_head.next is None:
            break;
        if temp_node is None:
            temp_node = n_head;
            n_head = n_head.next
            temp_node.next = None;
        else:
            currNode = n_head;
            n_head = n_head.next;
            currNode.next = temp_node;
            temp_node = currNode;
    n_head.next = temp_node;
    return n_head;
        



def main():
    li = LinkedList();
    li.insertHead(1);
    li.insertTail(2);
    li.insertTail(3);
    li.insertTail(4);
    li.print();
    new_head = rev_linkList(li.head);
    print('Reveresed ------');
    printLinkedList(new_head);


if __name__ == '__main__':
    main();