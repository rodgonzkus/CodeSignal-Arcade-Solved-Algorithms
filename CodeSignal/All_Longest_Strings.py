def solution (inputArray):
    max_str_len = 0
    new_array = list()
    for i in inputArray:
        if max_str_len < len(i):
            max_str_len = len(i)
    for j in inputArray:
        if len(j) == max_str_len:
            new_array.append(j)
    return new_array
 