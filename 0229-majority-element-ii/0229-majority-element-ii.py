class Solution(object):
    def majorityElement(self, nums):
            freq = {}
            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            result = []
            for key in freq:
                if freq[key] > len(nums) // 3:
                    result.append(key)
            return result 



        