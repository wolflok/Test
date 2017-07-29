#!/usr/bin/env python3
sum=0
for i in range(1,1000):
	print ("sum starts with ",sum)
	if i % 3 == 0:
		sum = sum + i
	elif i % 5 == 0:
		sum = sum + i
print (sum)

