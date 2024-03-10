def arr_max(arr):
    mx = 0
    for i in arr:
        if i > mx:
            mx = i
    
    return mx

print(arr_max([8,4,1,2,8,9,6,7]))