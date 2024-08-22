class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = {}
        for i in magazine:
            h[i] = h.get(i, 0) + 1
        for i in ransomNote:
            if i not in h or h[i] == 0:
                return False
            h[i] -= 1
        return True