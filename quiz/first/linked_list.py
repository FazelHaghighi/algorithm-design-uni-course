class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def size(self):
        return self.length

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        node = Node(value)
        leader = self.traverse_to_index(index - 1)
        holding_pointer = leader.next
        leader.next = node
        node.next = holding_pointer
        self.length += 1

    def remove(self, index):
        if index >= self.length:
            return None
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        leader = self.traverse_to_index(index - 1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next
        self.length -= 1

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def print_list(self):
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next
        print(array)


my_linked_list = LinkedList()
my_linked_list.append(1)

if __name__ == "__main__":
    number = int(input())
    for i in range(number):
        place = input()
        if place == "begin":
            my_linked_list.prepend(i + 2)
        elif place == "end":
            my_linked_list.append(i + 2)
        elif place == "mid":
            if my_linked_list.size() % 2 == 0:
                my_linked_list.insert(my_linked_list.size() // 2, i + 2)
            else:
                my_linked_list.insert((my_linked_list.size() // 2) + 1, i + 2)

    my_linked_list.print_list()
