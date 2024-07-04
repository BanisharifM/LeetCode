class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        total = m + n - 1
        i = m - 1
        j = n - 1
        for k in range(total, -1, -1):
            if i >= 0 and (j < 0 or nums1[i] >= nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                j -= 1
