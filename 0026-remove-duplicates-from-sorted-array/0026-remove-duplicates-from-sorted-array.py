class Solution(object):
    def removeDuplicates(self, nums):
        l = []

        for i in nums:
            if i not in l:
                l.append(i)

        nums[:len(l)] = l
        return len(l)