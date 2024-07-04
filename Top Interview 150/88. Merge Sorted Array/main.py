class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = m + n
        nums_merged = nums_merged = [0] * total
        i = 0
        j = 0
        for k in range(total):
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                nums_merged[k] = nums1[i]
                i += 1
                continue
            elif n != 0:
                nums_merged[k] = nums2[j]
                j += 1
                continue
        for k in range(total):
            nums1[k] = nums_merged[k]
