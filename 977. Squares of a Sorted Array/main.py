class Solution:
    def sortedSquares(nums: list[int]) -> list[int]:
        n = len(nums)
        left, right = 0, n - 1
        result = []
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        return result
        
    def sortedSquares2(nums: list[int]) -> list[int]:
        return sorted([x*x for x in nums])