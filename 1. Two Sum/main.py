class Solution(object):
    def twoSum1(self, nums, target):
        for n in range(len(nums)):
            for m in range(len(nums)-n):
                if n != m:
                    if nums[n] + nums[m] == target:
                        return [n, m]
                    else:
                        continue

    def twoSum2(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in seen and seen[y] != i:
                return [i, seen[y]]
