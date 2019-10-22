nums = [1,2,3,4,5,6,7,8,9]
nums2 = []
def is_even(num):
	
	if num %2 == 0:
		nums2.append(num)
	return nums2

for i in nums:
	is_even(i)
print(nums2)