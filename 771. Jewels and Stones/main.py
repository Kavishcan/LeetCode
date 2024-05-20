class Solution(object):
    # O(m * n)
    def numJewelsInStones1(self, jewels, stones):

        count = 0
        for stone in stones:
            print(stone)
            if stone in jewels:
                count += 1
        return count

    # Time: O(m + n)
    # Space: O(n)
    def numJewelsInStones2(self, jewels, stones):
        s = set(jewels)
        count = 0

        for stone in stones:
            if stone in s:
                count += 1

        return count
