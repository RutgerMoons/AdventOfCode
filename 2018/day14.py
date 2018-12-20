#! /usr/bin/env python3

elfs = [0, 1]
nb_recipes = "919901"
extra_scores = 10
extra_safety = 5 * len(elfs)

scores = [0] * (10**8 + extra_scores + extra_safety)
scores[0] = 3
scores[1] = 7
nb_scores = 2



def step(scores, nb_scores, elfs):
	total = 0
	for elf_idx in elfs:
		total += scores[elf_idx]

	digits = []
	if total == 0:
		digits = [0]
	else:
		while total:
			digits.append(total % 10)
			total //= 10

	for d in reversed(digits):
		scores[nb_scores] = d
		nb_scores += 1

	new_elfs = []
	for elf_idx in elfs:
		new_idx = elf_idx + scores[elf_idx] + 1
		new_idx %= nb_scores
		new_elfs.append(new_idx)

	return scores, nb_scores, new_elfs


#while nb_scores < nb_recipes + extra_scores:
#	scores, nb_scores, elfs = step(scores, nb_scores, elfs)

#print(''.join(list(map(str, scores[nb_recipes:nb_recipes + extra_scores]))))

for i in range(100):
	print(i)
	for j in range(1000000):
		scores, nb_scores, elfs = step(scores, nb_scores, elfs)
	string = ''.join(list(map(str, scores)))
	if nb_recipes in string:
		print(string.index(nb_recipes))
		break

