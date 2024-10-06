def insertion_sort_indexes(lst: list) -> list:
	output_lst = [1]

	for i in range(1, len(lst)):
		cur = i
		while cur > 0 and lst[cur - 1] > lst[cur]:
			lst[cur - 1], lst[cur] = lst[cur], lst[cur - 1]
			cur -= 1
		output_lst.append(cur + 1)

	return output_lst