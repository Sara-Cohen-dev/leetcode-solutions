class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
      nums.sort()
      leng=len(nums)
      result = nums[0] + nums[1] + nums[2]
      for i in range(leng-1):
        left=i+1
        right=leng-1
        while left<right:
         sum1=nums[left]+nums[right]+nums[i]
         if sum1==target:
            return sum1
         if abs(result-target)>abs(sum1-target):
            result=sum1
         if sum1<target:
            left+=1
         else: right-=1

      return result