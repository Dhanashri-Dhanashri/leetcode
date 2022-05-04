class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = defaultdict(int)

        count = 0
        for x in nums:
            comp = k - x
            if counter[comp]>0:
                counter[comp]-=1
                count+=1
            else:
                counter[x] +=1
        
        return count