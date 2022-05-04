# 리스트 내포
# for
nums = [i for i in range(5)]
print(nums)

nums2 = [1,2,3]
double_nums2 = [i*2 for i in nums2]
print(double_nums2)

# if 
nums3 = [i for i in range(10) if i%2 == 0]
print(nums3)

nums4 = [1,2,3,4,5]
double_nums4 = [i*2 for i in nums4 if i>=3]
print(double_nums4)
