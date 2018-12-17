#! /usr/bin/env python3

players = 478
scores = [0] * players

limit = 7124000
circle = [0, 1]
current_idx = 1
for i in range(2, limit + 1):
	if i % 71240 == 0:
		print("{}%".format(int((i * 100) / limit)))
	if i % 23 == 0:
		# add i to score
		score = i

		# add idx - 7 to score
		counter7 = (current_idx - 7) % len(circle)
		score += circle.pop(counter7)
		current_idx = counter7
		scores[i % players] += score
		continue

	append = False
	next_idx = current_idx + 2

	# current is last item
	if current_idx == (len(circle) - 1):
		next_idx = 1
	# second to last: insert at the back
	elif current_idx == (len(circle) - 2):
		append = True
	
	if append:
		circle.append(i)
		current_idx = len(circle) - 1
	else:
		circle.insert(next_idx, i)
		current_idx = next_idx

print(max(scores))
