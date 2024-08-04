# Linear search
# O(1) is called linear time
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
    
    def insert(self, data, index):
        if index == 0: 
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head
        while position > 1:
            current = current.next_node # check
            position -= 1
        
        prev_node = current
        next_node = current.next_node

        prev_node.next_node = new
        new.next_node = next_node

    def remove(self, key):
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                self.head = current.next_node
                found = True
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else: 
                prev = current
                current = current.next_node
        return current
    
    def index_at(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return position

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


# Merging sort

def merge_sort(list):

    """
    Sorts a list in ascending order. returns a new sorted list
    Devide: find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in previous step.
    Combine: Merge the sorted sublists created in previous step
    """
    """
    Takes O(n log n) time
    """

    if len(list) <= 1:
        return list
        
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Takes O(log n) time
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else: 
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_merge(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_merge(list[1:])

arr = [33,23,45,3,5,6,77,88,1,32]
res = merge_sort(arr)
print("merge: ", res)
print(verify_merge(res))

# Linked List Merge sort

def linked_list_merge_sort(linked_list):
    """
    Sort Linked List in ascending order
    - Recursively devide the linked list into sublists containing a single mode
    - Repeatedly merge the sub lists to produce sorted sublist until one remains

    Return sorted Linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list


    left_half, right_half = split_linked(linked_list)
    left = linked_list_merge_sort(left_half)
    right = linked_list_merge_sort(right_half)

    return merge_linked_sort(left,right)

def split_linked(linked_list):
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half,right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.index_at(mid-1)

        left_half = linked_list
        right_half = Linked_list()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half



def merge_linked_sort(left,right):
    """
    Merges two linked lists, sorting by data in nodes.
    Returns a new merged lists
    """

    merged = Linked_list()
    # Add fake head that is discarded later
    merged.add(0)

    current = merged.head

    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either.
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail 
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on left to set loop condition on false
            left_head = left_head.next_node
        else: 
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on left is less than right, set current to left node
            if left_data < right_data: 
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to right node
            else: 
                current.next_node = right_head
                # Move right head to next node 
                right_head = right_head.next_node
            # Move current to next node
            current = current.next_node

            # Discard fake head and set first merged node as head
            head = merged.head.next_node
            merged.head = head

            return merged
        

l = Linked_list()
l.add(20)
l.add(40)
l.add(3)
l.add(1)
l.add(400)
print(linked_list_merge_sort(l))


#----------------------------------------------------------------------------------------------

# Bogo sort
import random
import sys

bogo_value = [99,3,5,2,1,77,4]
def is_sorted(bogo_value):
    for index in range(len(bogo_value) -1):
        if bogo_value[index] > bogo_value[index + 1]:
            return False
    return True

def bogo_sort(bogo_value):
    attempts = 0
    while not is_sorted(bogo_value):
        print("attempts", attempts)
        random.shuffle(bogo_value)
        attempts +=1
    return bogo_value

b_res = bogo_sort(bogo_value)
print(b_res)


# Selection Sort

s_values = [88,7,44,3,2,1]
def selection_sort(values):
    sorted_list = []
    for index in range(0, len(values)):
        index_to_move = min_value(values)
        sorted_list.append(values.pop(index_to_move))
        print("%-25s %-25s", values, sorted_list)
    return sorted_list

def min_value(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

print(selection_sort(s_values))

# recursion
def sum(numbers):
    if not numbers:
        return 0
    print("calling %s", numbers[1:])
    remainingSum = sum(numbers[1:])
    print(f" {remainingSum} this is numbers: {numbers} ")
    return numbers[0] + remainingSum
print(sum([3,65,6,4,2]))