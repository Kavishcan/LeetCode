class Solution:
    def summaryRanges(nums: list[int]) -> list[str]:

        if not nums:
            return []
        
        final = []
        start = 0
        end = 0
        
        for i in range(len(nums) - 1):
            if (nums[i] + 1) != nums[i + 1]:
                if start == end:
                    final.append(f"{nums[start]}")
                else:
                    final.append(f"{nums[start]}->{nums[end]}")
                start = i + 1
            end = i + 1
        
        # Handle the last range
        if start == end:
            final.append(f"{nums[start]}")
        else:
            final.append(f"{nums[start]}->{nums[end]}")
        
        return final
    

    def summaryRanges2(nums: list[int]) -> list[str]:
        if not nums:
            return []

        final = []
        start = 0

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    final.append(str(nums[start]))
                else:
                    final.append(f"{nums[start]}->{nums[i - 1]}")
                start = i

        return final

print(Solution.summaryRanges([0, 1, 2, 4, 5, 7]))