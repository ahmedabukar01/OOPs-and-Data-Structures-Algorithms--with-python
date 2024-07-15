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
