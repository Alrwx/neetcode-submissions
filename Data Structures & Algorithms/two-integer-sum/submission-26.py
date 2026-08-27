class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass technique
        mapp = {}

        for idx, val in enumerate(nums):
            look = target - val
            if look in mapp:
                return [mapp[look], idx] 
            mapp[val] = idx






        # two pass technique
        # mapped = {}
        
        # for i, num in enumerate(nums):
        #     if num not in mapped:
        #         mapped[num] = []
        #     mapped[num].append(i)

        # for i, num in enumerate(nums):
        #     look = target - num
        #     if look in mapped:
        #         if look == num and len(mapped[look]) == 1:
        #             continue

        #         if len(mapped[look]) < 2:
        #             return [i, mapped[look][0]]
        #         return [i, mapped[look][1]]
                

        