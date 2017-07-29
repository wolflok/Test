#!/usr/bin/env python3
next_val = 2
cur_val = 1
sum = 0
while next_val < 4000000:
	if next_val % 2 == 0:
		sum = sum + next_val
	tmp = next_val
	next_val=next_val + cur_val
	cur_val=tmp

print (sum)

