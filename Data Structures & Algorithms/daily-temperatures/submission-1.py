class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for idx, num in enumerate(temperatures):
            if not stack:
                stack.append((num, idx))
                
            while stack and num > stack[-1][0]:
                val = stack.pop()
                ans[val[1]] = idx - val[1]

            stack.append((num, idx))
        return ans