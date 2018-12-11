with open('input/day2') as input:
	vals = list(map(lambda x: x.strip(), input.readlines()))

# part 1
counter2, counter3 = 0, 0
for val in vals:
	found2, found3 = False, False
	for char in set(val):
		count = val.count(char)
		if count == 2: found2 = True
		if count == 3: found3 = True
		if found2 and found3: break
	if found2: counter2 += 1
	if found3: counter3 += 1

print("Part 1: %d" % (counter2 * counter3))

#part 2
def differ_by_one(fst, sec):
	if len(fst) != len(sec): return False

	for i in range(len(fst)):
		if fst[i] != sec[i]:
			return fst[i+1:] == sec[i+1:], fst[:i] + fst[i+1:]
	return False, None

def find_one(vals):
	for i in range(len(vals) - 1):
		for j in range(i + 1, len(vals)):
			differ, result = differ_by_one(vals[i], vals[j])
			if differ:
				return result

print("Part 2: %s" % find_one(vals))
