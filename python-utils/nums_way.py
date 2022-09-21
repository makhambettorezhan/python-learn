def num_way(n, arr):
    return nums_way(n, arr, len(arr)-1)

def nums_way(n, arr, i):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif i < 0:
        return 0
    elif arr[i] > n:
        return nums_way(n, arr, i-1)
    else:
        return nums_way(n-arr[i], arr, i-1) + nums_way(n, arr, i-1)


print(num_way(6, [1,2,4,5,6,10]))


    
