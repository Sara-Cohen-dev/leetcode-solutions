class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low=1
        high=max(quantities)
        while low<high:
            mid=(high+low)//2
            if(self.canBe(n,quantities,mid)):
                high=mid
            else: low=mid+1
        
        return low

    def canBe(self, n: int, quantities: List[int],x:int) -> bool:
        sumArr=0
        for i in quantities:
          sumArr+=(i + x - 1) // x
        return sumArr<=n 
         
        