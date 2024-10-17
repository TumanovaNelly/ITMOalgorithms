def insertion_sort_reversed_bin_pow(lst: list) -> None:
	for i in range(1, len(lst)):
		key = lst[i]
		left = 0
		right = i
		while left < right:
			mid = left + (right - left) // 2
			if key > lst[mid]:
				right = mid
			else:
				left = mid + 1
		
		for j in range(i, right, -1):
			lst[j] = lst[j - 1]

		lst[right] = key

def insertion_sort_reversed(lst: list) -> None:
	for i in range(1, len(lst)):
		cur = i
		while cur > 0 and lst[cur - 1] < lst[cur]:
			lst[cur - 1], lst[cur] = lst[cur], lst[cur - 1]
			cur -= 1