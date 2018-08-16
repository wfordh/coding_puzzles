def index_sum(lst, target):
	"""
	Takes in a list of numbers and determines if any two sum to
	the target number. Returns the first instance of this occurring.
	If it does not happen, returns empty list
	:lst: list of numbers
	:target: target number
	"""


	for elem in lst:
		foo[elem] = lst.index(elem)

	for k, v in dct.items():
		if (target - k) in dct.keys():
			second_v = dct[(target-k)]
			if v != second_v:
				return [v, second_v]

	return []