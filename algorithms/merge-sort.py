import math

#------------------------------------------------------------
# MERGE SORT (NOT IN PLACE!)

# def merge(lhs, rhs):
# 	len_lhs = len(lhs)
# 	len_rhs = len(rhs)
# 	len_sum = len_lhs + len_rhs
	
# 	lhs_new = list(lhs)
# 	rhs_new = list(rhs)
# 	lhs_new.append(math.inf)
# 	rhs_new.append(math.inf)

# 	merged = [None] * len_sum
# 	cursor_lhs = 0
# 	cursor_rhs = 0

# 	for i in range(len_sum):
# 		if lhs_new[cursor_lhs] <= rhs_new[cursor_rhs]:
# 			merged[i] = lhs_new[cursor_lhs]
# 			cursor_lhs += 1
# 		elif rhs_new[cursor_rhs] <= lhs_new[cursor_lhs]:
# 			merged[i] = rhs_new[cursor_rhs]
# 			cursor_rhs += 1
# 	# print("len merged:",len(merged))
# 	return merged


# def mergesort(list):
# 	if len(list) == 1:
# 		return list
# 	if len(list) == 2:
# 		if list[0] < list[1]:
# 			return list
# 		else:
# 			temp = list[1]
# 			list[1] = list[0]
# 			list[0] = temp
# 			return list
# 	q = math.floor(len(list)/2)
# 	lhs = mergesort(list[:q])
# 	rhs = mergesort(list[q:])
# 	merge1 = merge(lhs, rhs)
# 	return merge1

#------------------------------------------------------------
# MERGE SORT (MOSTLY IN PLACE!)

def merge(list1, p, q, r):
	len_lhs = q - p + 1
	len_rhs = r - q
	len_sum = len_lhs + len_rhs
	
	lhs_new = list(list1[p : q+1])
	rhs_new = list(list1[q+1:r+1])
	lhs_new.append(math.inf)
	rhs_new.append(math.inf)

	cursor_lhs = 0
	cursor_rhs = 0

	for i in range(p, r+1):
		if lhs_new[cursor_lhs] <= rhs_new[cursor_rhs]:
			list1[i] = lhs_new[cursor_lhs]
			cursor_lhs += 1
		elif rhs_new[cursor_rhs] <= lhs_new[cursor_lhs]:
			list1[i] = rhs_new[cursor_rhs]
			cursor_rhs += 1
	# print("len merged:",len(merged))


def mergesort(list1, p, r):
	if p < r:
		q = math.floor((p+r)/2)
		print(p,q,r)
		mergesort(list1, p, q)
		mergesort(list1, q+1, r)
		merge(list1, p, q, r)
	

def main():
	a = [3,6,5,1,8,6,4,8,7,6,0,3,5,77,53,3,22,4,77,9,-6,8,567,43,2,55,-48,6,7]
	mergesort(a, 0, len(a)-1)
	print(a)

main()

# a = [1,3,7,8]
# b = [5,7,9,10]

# print(merge(a,b))