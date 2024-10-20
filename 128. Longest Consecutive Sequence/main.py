class Solution:
    def longestConsecutive(nums: list[int]) -> int:
        s = set(nums)
        longest = 0
        print(s)
        for num in s:
            if num - 1 not in s:
                next_num = num + 1 
                length = 1
                while next_num in s:
                    next_num += 1
                    length += 1
                longest = max(longest, length)
        
        return longest

    

    print(longestConsecutive([100, 4, 200, 1, 3, 2]))