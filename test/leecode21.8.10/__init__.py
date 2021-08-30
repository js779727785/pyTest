"""
2.2
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
"""
nums=[-3,-2,-2,0,1,1,2,2,3,3,3,4]
def fu(nums):
    j=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[j]=nums[i]
            j+=1
    return nums[:j],j,nums
print(fu(nums))