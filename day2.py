with open('input/day2') as input:
	vals = input.readlines()

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

print(counter2 * counter3)

#part 2
def differ_by_one(t1, t2):
	s1, s2 = t1[0], t2[0]
	if len(s1) != len(s2): return False
	if len(s1 & s2) != len(s1) - 1:
		return False
	
	count = 0
	str1, str2 = t1[1], t2[1]
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			count += 1
	return count == 1

#vals = ['abcde', 'fghij','klmno','pqrst','fguij','axcye','wvxyz']
sets = list(map(lambda x: (set(x.strip()), x.strip()), vals))

def find_one(sets):
	for i in range(len(sets) - 1):
		for j in range(i + 1, len(sets)):
			if differ_by_one(sets[i], sets[j]):
				print ('Found one')
				badChar = list(sets[i][0] - (sets[i][0] & sets[j][0]))[0]
				print (sets[i])
				print (sets[j])
				print(badChar)
				print(sets[i][1].replace(badChar, ''))

find_one(sets)
#print(find_one(sets))
