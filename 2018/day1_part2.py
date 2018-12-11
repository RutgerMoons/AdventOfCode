


def find_double(values):
	seen = set()
	freq = 0
	seen.add (0)
	while True:
		for val in values:
			freq += val
			if freq in seen:
				return freq
			seen.add(freq)

with open('input/day1') as input:
	vals = list(map(lambda x: int(x.strip()), input.readlines()))

print(find_double(vals))
