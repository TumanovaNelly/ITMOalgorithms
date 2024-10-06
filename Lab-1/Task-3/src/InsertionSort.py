def insertion_sort_reversed(lst: list) -> None:
	for i in range(1, len(lst)):
		cur = i
		while cur > 0 and lst[cur - 1] < lst[cur]:
			lst[cur - 1], lst[cur] = lst[cur], lst[cur - 1]
			cur -= 1