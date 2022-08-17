class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mArr = []
        i1 = 0
        i2 = 0
        if nums2 == []:
            mArr = nums1
        elif nums1 == []:
            mArr = nums2
        else:
            for i in range(len(nums1) + len(nums2)):
                if i1 == len(nums1):
                    mArr.append(nums2[i2])
                    i2 += 1
                elif i2 == len(nums2) or nums1[i1] < nums2[i2]:
                    mArr.append(nums1[i1])
                    i1 += 1
                else:
                    mArr.append(nums2[i2])
                    i2 += 1
        
        if len(mArr) % 2 == 1:
            return mArr[(len(mArr) - 1)//2]
        else:
            return (mArr[len(mArr)//2] + mArr[(len(mArr)//2)-1])/2