

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None


class Hash_Table:
    def __init__(self):
        self.table = []

    def emptyHashTable(self):
        for x in range(10):
            self.table.append(None)

    def hash(self, name):
        # simplest hashing function
        # return 5;

        # get each character ascii value of name and sum it
        # multiply it again to be more random
        # modulus by 10 to place it in table
        check_sum = 0
        for char in name:
            check_sum += ord(char)
            check_sum *= ord(char)
            check_sum %= 10
        return check_sum

    def insert(self, p):
        idx = self.hash(p.name)
        if self.table[idx] is None:
            self.table[idx] = p
        else:
            temp = self.table[idx].next
            self.table[idx].next = p
            p.next = temp

    def printTable(self):
        # print(self.table)
        for i in range(0, len(self.table)):
            print(f'{i}', end="->")
            if self.table[i] is None:
                print(f'---')
            else:
                temp = self.table[i]
                while True:
                    if temp.next is None:
                        print(f'{temp.name}', end="=> None\n")
                        break
                    print(f'{temp.name}', end="=>")
                    temp = temp.next

    def get_value(self, name):
        idx = self.hash(name)
        person = self.table[idx]
        while person is not None:
            if person.name == name:
                return person
            person = person.next
        return None

    def remove_value(self, name):
        idx = self.hash(name)
        prev = None
        node = self.table[idx]
        while node is not None:
            if node.name == name:
                if prev is None:
                    prev = node.next
                    node.next = None
                    node = None
                    self.table[idx] = prev
                else:
                    prev.next = node.next
                    node.next = None
                    node = None
                break
            prev = node
            node = self.table[idx].next


def main():
    h_t = Hash_Table()
    h_t.emptyHashTable()
    p1 = Person("Bob", 20)
    p2 = Person("Sue", 30)
    p3 = Person("Tim", 40)
    p4 = Person("Hakim", 35)
    p5 = Person("Dan", 27)
    p6 = Person("Tom", 80)
    p7 = Person("Trevor", 22)
    p8 = Person("Jacob", 21)
    p9 = Person("Jaden", 45)
    p10 = Person("Kanye", 65)
    h_t.insert(p1)
    h_t.insert(p2)
    h_t.insert(p3)
    h_t.insert(p4)
    h_t.insert(p5)
    h_t.insert(p6)
    h_t.insert(p7)
    h_t.insert(p8)
    h_t.insert(p9)
    h_t.insert(p10)
    h_t.printTable()

    person = h_t.get_value("Kanye")
    if person is None:
        print("Not found")
    else:
        print(
            f'Found \n Person Name : {person.name} \n Person Age : {person.age}')

    h_t.remove_value("Jaden")
    h_t.remove_value("Jacob")
    h_t.remove_value("Dan")
    h_t.remove_value("Bob")
    h_t.printTable()
    person = h_t.get_value("Jaden")
    if person is None:
        print("Not found")
    else:
        print(
            f'Found \n Person Name : {person.name} \n Person Age : {person.age}')


if __name__ == '__main__':
    main()
