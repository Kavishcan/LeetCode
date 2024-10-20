from collections import defaultdict


class Solution:
    def majorityElement(nums: list[int]) -> int:
        n = defaultdict(int)
        nums.sort()
        for i in nums:
            n[i] += 1
            print(n)
            if n[i] > len(nums) // 2:
                return i
        
    def majorityElement2(nums: list[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        max_count = -1
        ans = -1

        for key, value in counter.items():
            if value > max_count:
                max_count = value
                ans = key
        
        return ans
    
    def majorityElement3(nums: list[int]) -> int:
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
                count += 1
            elif num == ans:
                count += 1
            else:
                count -= 1
        
        return ans
        
    print(majorityElement3([3,2,3]))