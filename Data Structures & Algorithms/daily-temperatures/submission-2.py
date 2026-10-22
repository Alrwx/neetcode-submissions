class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)
        
        for idx, val in enumerate(temperatures):
            while stk and val > stk[-1][0]:
                index = idx - stk[-1][1]
                ans[stk[-1][1]] = index
                stk.pop()
            stk.append((val, idx))
        
        return ans