# merges the pieces in order
def merge(left, right):
    
        # if one side is null, return the not-null side
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	# combine the two lists
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break 

	return result
    
# Recursive merge sort function
def mergesort(array):
    
        # base case if array is only 1 element
	if len(array) < 2:
		return array
	    
        # if the array can be split, do it and recurse
	mid = int(len(array)/2)
	left = mergesort(array[:mid])
	right = mergesort(array[mid:])

        # merge the pieces in order
	return merge(left, right)

# print a merge sorted array
array = [13,44,52,134,23,832,31,71,6]
print ("Unsorted Array")
print (array)
print ("Sorted Array")
print (mergesort(array))
