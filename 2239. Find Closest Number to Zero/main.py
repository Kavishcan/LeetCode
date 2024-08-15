class Solution:
    # Time: O(n)
    # Space: O(1)
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for n in nums: 
            if abs(n) < abs(closest):
                closest = n

            
        if closest < 0 and abs(closest) in nums:
            return  abs(closest)
        else:
            return closest
            