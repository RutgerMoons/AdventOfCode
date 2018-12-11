

with open('input/day1') as input:
	vals = input.readlines()

total = 0
for val in vals:
	total += int(val.strip())

print(total)
