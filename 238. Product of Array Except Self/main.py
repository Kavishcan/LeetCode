class Solution:
    def productExceptSelf(nums: list[int]) -> list[int]:

      n = len(nums)
      final = []

      for i in range(n):
        x = 1
        for j in range(n):
            if i != j:
               x *= nums[j]
        final.append(x)

      return final
    
    def productExceptSelf2(nums: list[int]) -> list[int]:
        left_m = 1
        right_m = 1
        n = len(nums)
        left_arr = [1] * n
        right_arr = [1] * n 

        for i in range(n):
            j = -i -1
            left_arr[i] = left_m
            right_arr[j] = right_m
            left_m *= nums[i]
            right_m *= nums[j]
    
        return [left_arr[i] * right_arr[i] for i in range(n)]
            

print(Solution.productExceptSelf2([1, 2, 3, 4]))

