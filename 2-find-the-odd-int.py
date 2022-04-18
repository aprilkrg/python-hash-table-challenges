'''
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python/606c0aead051520044f094db
2. Find the odd int 

Given an list of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.


Example 1:

Input: [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
Output: 5

Example 2:

Input: [1,1,2,-2,5,2,4,4,-1,-2,5]
Output: -1

Example 3:

Input: [10]
Output: 10
'''    

def find_it(li):
	num_dict = {}
	for num in li:
		if num in num_dict:
			num_dict[num] += 1
		else:
			num_dict[num] = 1
	# print(num_dict)
	odd_num = 0
	#  don't need to use variable here, could just return the el in the if check below
	for el in num_dict:
		# print(num_dict[el] % 2)
		if num_dict[el] % 2 != 0:
			odd_nums = el
	print(odd_nums, 'odd num out')

find_it([1,2,3,1,2,3,4])
# find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])