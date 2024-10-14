def bin_add(first: list, second: list) -> list:
	if len(first) < len(second):
		first = [0] * (len(second) - len(first)) + first
	elif len(first) > len(second):
		second = [0] * (len(first) - len(second)) + second

	n = len(first)
	result = [0] * (n + 1)
	for i in range(n - 1, -1, -1):
		if not(first[i] == 0 or first[i] == 1) or not(second[i] == 0 or second[i] == 1):
			raise ValueError("Incorrect number")

		result[i + 1] += first[i] + second[i]
		if result[i + 1] > 1:
			result[i] += 1
			result[i + 1] -= 2

	return result
