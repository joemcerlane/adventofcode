from collections import Counter

loc_1 = []
loc_2 = []
f = open("input.txt", "r")
for i in f:
	nums = i.split()
	loc_1.append(nums[0])
	loc_2.append(nums[1])

loc_2.sort()
loc_1.sort()

total_diff = 0

for i in range(len(loc_1)):
	total_diff += abs(int(loc_1[i]) - int(loc_2[i]))

##problem 1 answer
print(total_diff)


sim_score = 0
hm = Counter(loc_2)
for i in range(len(loc_1)):
	sim_score += int(loc_1[i]) * int(hm.get(loc_1[i], 0))

##problem 2 answer
print(sim_score)