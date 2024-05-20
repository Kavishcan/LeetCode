# this is solved using HASHSET big O(n) time complexity
class Solution:
    def containsDuplicateHashset(self, nums: list[int]) -> bool:
        h = set()
        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)

        return False

# this is solved using HASHSET big O(n) time complexity

    def containsDuplicateHashmap(self, nums: list[int]) -> bool:
        h = {}
        for num in nums:
            if num in h and h[num] >= 1:
                return True
            else:
                h[num] = h.get(num, 0)+1
        return False
