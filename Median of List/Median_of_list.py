class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0:
            m = int((len(nums1)+1)/2 - 1)
            return float(nums1[m])
        else:
            m1 = int(len(nums1)/2 - 1)
            m2 = int(len(nums1)/2)
            return float(nums1[m1]+nums1[m2])/2