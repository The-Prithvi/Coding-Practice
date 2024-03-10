def remove_duplicates(arr):
    x = []

    for i in arr:
        if i not in x:
            x.append(i)
        else:
            x.append(0)
    return x

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))