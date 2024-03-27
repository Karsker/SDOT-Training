def lis(arr, n):
    lis = [1]*n
    max_length = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j]+1:
                lis[i] = lis[j]+1
        for i in range(n):
            max_length = max(max_length, lis[i])
            
    return max_length
    
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    n = len(arr)
    print(lis(arr,n))