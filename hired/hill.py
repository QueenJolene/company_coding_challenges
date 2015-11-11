"""Given an array of integer elements. write a function that finds the minimum
value X that makes possible the following: generate a new array that is sorted 
in strictly ascending order by increasing or decreasing each of the elements of 
the initial array with integer values in the [0, X] range.
Example: Having the initial array [5, 4, 3, 2, 8] the minimum value for X is 3. 
Decrease the first element (5) by 3, decrease the second one (4) by 1, increase the 
third one (3) by 1, increase the forth one (2) by 3 and do nothing to the last one (8). 
In the end we obtain the array [2, 3, 4, 5, 8] which is sorted in strictly ascending order.
print the result X to the standard output (stdout)"""


def hill(array):
	sorted_array = sorted(array)
	max_diff = 0
	for index in range(len(array)-1):
		difference = array[index] - sorted_array[index]
		if difference > max_diff:
			max_diff = difference

	return max_diff

print hill([5,4,3,2,8])
