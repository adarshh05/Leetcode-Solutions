class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans= [1] * n
        current_prod= 1
        for i in range(n):
            ans[i]= current_prod
            current_prod *= nums[i]
        current_prod= 1
        for i in range(n-1, -1, -1):
            ans[i] *= current_prod
            current_prod *= nums[i]
        return ans