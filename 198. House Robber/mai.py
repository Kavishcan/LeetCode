class Solution:
    def rob(nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)
            print("first", first)
            print("second", second)
        
        return second        
    
    print(rob([2,7,9,3,1]))