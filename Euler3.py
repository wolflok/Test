#!/usr/bin/env python3

import prime

primeList = []
for i in range(1,200000):
	if prime.checkprime(i,2):
		primeList.append(i)

target=600851475143

i=1
while target > 2:
	if (target % primeList[i]) ==0:
		print (primeList[i])
		target=target/primeList[i]
	i=i+1



	