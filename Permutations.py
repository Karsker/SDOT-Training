def generate_permutations(nums, left, right):
    if left == right:
        print(nums)
    else:
        for i in range(left, right+1):
            nums[left], nums[i] = nums[i], nums[left]
        
            generate_permutations(nums, left+1, right)
            
            nums[left], nums[i] = nums[i], nums[left]

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    
    generate_permutations(nums, 0, n-1)