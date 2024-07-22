# Linear search
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def varify(result):
    if result != None:
        print("the target is at index: ", result)
    else:
        print("the target is not in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 8)
varify(result)

# Binary Search
def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        middpoint = (first + last) // 2

        if list[middpoint] == target:
            return middpoint
        elif list[middpoint] < target:
            first = middpoint + 1
        else: 
            last = middpoint - 1
    return None


res = binary_search(numbers, 8)
varify(res)

# Recursive binary search
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint +1:], target)
            else: 
                return recursive_binary_search(list[:midpoint], target)
            

ress = recursive_binary_search(numbers, 8)
varify(ress)


# Linked List
class Node:
    """
    an object for storing a single node of a linked list.
    models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        # %s is placeholder, but there is newer method called f format and it's written like this: f"this is {name}"
        return "<Node: %s>" % self.data 
    
class Linked_list:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            current = current.next_node
            count += 1

            return count
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    # display format on the console
    def __repr__(self):
        # return string representation of the list

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("Head: %s" % current.data)
            elif current.next_node is None:
                nodes.append(f"Tail {current.data}")
            else: 
                nodes.append("%s" % current.data)

            current = current.next_node
        return '-> '.join(nodes)
