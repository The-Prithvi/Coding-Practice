import sys

def find_missing(arr):

    min = sys.maxsize
    for i in arr:
        if i < min:
            min = i

    max = -sys.maxsize
    for i in arr:
        if i > max:
            max = i
    
    missing_nos = []
    for i in range(min, max + 1):
        if i not in arr:
            missing_nos.append(i)
    return missing_nos

print(find_missing([5,6,3,1,4,7,8,5,2]))
print(find_missing([6,3,1,4,7,8,2]))