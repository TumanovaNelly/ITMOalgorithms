from utils import read, write


def insertion_sort_indexes_bin_pow(lst: list) -> list:
	output_lst = [1]

	for i in range(1, len(lst)):
		key = lst[i]
		left = 0
		right = i
		while left < right:
			mid = left + (right - left) // 2
			if key < lst[mid]:
				right = mid
			else:
				left = mid + 1
		
		for j in range(i, right, -1):
			lst[j] = lst[j - 1]

		lst[right] = key
		output_lst.append(right + 1)

	return output_lst

	
def insertion_sort_indexes(lst: list) -> list:
	output_lst = [1]

	for i in range(1, len(lst)):
		cur = i
		while cur > 0 and lst[cur - 1] > lst[cur]:
			lst[cur - 1], lst[cur] = lst[cur], lst[cur - 1]
			cur -= 1
		output_lst.append(cur + 1)

	return output_lst


def main():
	lst, = read()
	write(*insertion_sort_indexes_bin_pow(lst))
	write(*lst, to_end=True)


if __name__ == "__main__":
	main()