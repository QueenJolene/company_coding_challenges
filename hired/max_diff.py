
def max_subarray(A):
    max_ending_here = max_so_far = -10000000000
    for i in range(len(A)):
    	summed_list = sum(A[:i+1])
        max_so_far = max(max_so_far, summed_list)
    return max_so_far

def min_subarray(A):
    min_ending_here = min_so_far = 10000000000
    for i in range(len(A)):
    	# print i
    	# print A[-1:]
    	summed_list = sum(A[-(i+1):])
    	# print A
    	# print "minimum summed_list =", summed_list
        min_so_far = min(min_so_far, summed_list)
    return min_so_far

def max_diff(A):
	max_diff = -1000000
	for i in range(1,len(A)):
		left_array=A[:i]
		right_array = A[i:]
		temp_max_diff = max_subarray(right_array) - min_subarray(left_array)
		# print "split at index ", i
		# print max_subarray(right_array)
		# print min_subarray(left_array)

		if temp_max_diff> max_diff:
			max_diff=temp_max_diff
		# print max_diff
	return max_diff

array=[3,-5,1,-2,8,-2,3,-2,1]
array2=[-1,2,3,-10,19]

# print min_subarray(array2)
# print max_subarray(array2)
print max_diff(array2)
print max_diff(array)
# print max_diff(array)
# print max_diff(array2)

