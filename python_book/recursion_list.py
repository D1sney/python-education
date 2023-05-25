def rec(list, high=None, index=0):
    if index == 0:
        high = list[index]
    if list[index] > high:
        high = list[index]
    # print(high)
    if index == len(list) - 1:
        return high
    else:
        return rec(list, high, index+1)

print(rec([1,2,2,1,23,40,3,33,4,23,32]))
