"""Optional- Deviation
Given an array of integer elements and an integer d please consider all the 
sequences of d consecutive elements in the array. For each sequence we compute 
the difference between the maximum and the minimum value of the elements in that sequence 
and name it the deviation. write a function that computes the maximum value among the deviations 
of all the sequences 
considered above. D is an integer value giving the length of the sequences. 
Example: v: 6, 9, 4, 7, 4, 1; d: 3; output = 6"""

def deviation(array, d):
	max_dev = -10000000000
	for i in range(len(array)-2):
		sliced_list = sorted(array[i:i+d])
		if sliced_list[-1] > large:
		small = sliced_list[0]
		large =sliced_list.pop()
		dev = large - small
		if dev > max_dev:
			max_dev = dev
	return max_dev


print deviation([6,9,4,7,4,1], 3)
