#! /usr/bin/env python3

class SpreadRule:
	def __init__(self, state, outcome):
		self.state = state
		self.outcome = outcome

def string_to_plants(s):
	plants = []
	for pot in s:
		if pot == '#':
			plants.append(True)
		else:
			plants.append(False)
	return plants

def simulate_plant(plants, idx, rules, max_spread):
	for rule in rules:
		if plants[idx - max_spread: idx + max_spread + 1] == rule.state:
			return rule.outcome
	return False

def simulate_all_plants(plants, rules, max_spread):
	new_plants = plants.copy()
	for i in range(max_spread, len(plants)):
		new_plants[i] = simulate_plant(plants, i, rules, max_spread)
	return new_plants

def plant_sum(plants, offset):
	total = 0
	for i in range(len(plants)):
		if plants[i]:
			total += i - offset
	return total

with open('input/day12') as input:
	lines = list(map(lambda x: x.strip(), input.readlines()))

nb_generations = 20
max_spread = 2
plants = []
init = lines[0].strip()
nb_left = max_spread * (nb_generations + 1)
buffer_left = [False] * nb_left
buffer_right = [False] * nb_left
plants = buffer_left + string_to_plants(init) + buffer_right

rules_str = lines[1:]
rules = []
for rule in rules_str:
	sp = rule.strip().split(' => ')
	state = string_to_plants(sp[0])
	outcome = string_to_plants(sp[1])[0]
	rules.append(SpreadRule(state, outcome))

# Now do the simulation
for i in range(nb_generations):
	plants = simulate_all_plants(plants,rules,max_spread)
print(plant_sum(plants, nb_left))
