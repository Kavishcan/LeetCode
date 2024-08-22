class Solution:
    def maxNumberOfBalloons(text: str) -> int:
        h = {}
        for i in text:
            h[i] = h.get(i, 0) + 1
        
        b = {"b": 1, "a": 1, "l": 2, "o": 2, "n":1}
        max_balloons = float("inf")
        for char in b:
            if char in h:
                max_balloons = min(max_balloons, h[char] // b[char])
            else:
                return 0  
        
        return max_balloons
        
    

    print(maxNumberOfBalloons("nlaebolko"))
        


        
        