from collections import defaultdict

class Solution:
    def maxNumberOfBalloons2(text: str) -> int:
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
    
    def maxNumberOfBalloons(text: str) -> int:
        counter = defaultdict(int)
        balloon = "balloon"

        for char in text:
            if char in balloon:
                counter[char] += 1
        
        if any(char not in counter for char in balloon):
            return 0
        else:
            return(min(counter["b"], counter["a"], counter["l"] // 2, counter["o"] // 2, counter["n"]))
        
    

    print(maxNumberOfBalloons("nlaebolko"))
        


        
        