class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        for i in range(1,len(nums)):
            if i == 1: # 2nd
                dp.append(max(nums[0],nums[1]))
            elif i == 2: # 3rd
                dp.append(max(nums[1],nums[0]+nums[2]))
            else:
                a = dp[i-1]
                b = max(nums[i] + dp[i-2], nums[i]+dp[i-3])
                
                dp.append(max(a,b))
        
        print(dp)
        return dp[len(nums)-1]
