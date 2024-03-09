# Method 1

def frequency(str, char):

    str = str.strip()
    count = 0

    for i in str:
        if i == char:
            count += 1
    return count


print(frequency("Prithvi", "i"))




# Method 2 (Making Dictionary)

def frequency2(str):

    dict = {}

    str = str.strip()
    count = 0

    for i in str:
        count = 0
        for j in str:     
            if i == j:
                count += 1

        dict[i] = count


    # Removing duplicate keys
        
    unique_dict = {}
    for key, value in dict.items():
        if key not in unique_dict:
            unique_dict[key] = value

    return unique_dict


print(frequency2("prithvi"))
