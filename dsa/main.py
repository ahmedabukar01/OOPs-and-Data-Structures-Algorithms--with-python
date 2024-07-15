# Linear search
def linear_search(list, target):
    for i in range(len(list)):
        if i == target:
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