def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	if len(a) != len(b):
		return -1
	new = []
	for i in range(len(a)):
		new.append(a[i]+b[i])
	return new
	# If vectors have different lengths, return -1.
	pass