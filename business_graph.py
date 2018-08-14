# Puzzle for a simple graph traversal using businesses as nodes
# moving from one to the other as edges. Basic function for finding
# the distinct (to, from) tuples and the count for the number of
# different edges of that type that were traversed.


bizid_to_type = {
	1: 'airport',
	2: 'taxi',
	3: 'Hotel',
	4: 'Hotel',
}

bizid_neighbors = {
	1: [2],
	2: [3, 4],
	3: [2],
	4: [2],
}


def biz_transitions(bizid_neighbors, bizid_to_type, start_bizid, max_depth):
	seen_edges = set()
	current = start_bizid
	neighbors = bizid_neighbors[current]
	edges_dict = dict()


	for i in range(max_depth):
		neighbors = bizid_neighbors[current][:]
		next_stop = neighbors.pop()
		if (current, next_stop) not in seen_edges:
			# to scale up, would this need to be while loop?
			pass
		else:
			next_stop = neighbors.pop()
		seen_edges.add((current, next_stop))
		current = next_stop

	for e in seen_edges:
		x = (bizid_to_type[e[0]], bizid_to_type[e[1]])
		if x in edges_dict:
			edges_dict[x] += 1
		else:
			edges_dict[x] = 1
	
	return edges_dict
