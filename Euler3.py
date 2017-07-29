#!/usr/bin/env python3

import prime

#prime.checkprime(25,2) 
#if prime.checkprime(25,2) == True:
#	print ("true")
#else:
#	print ("false")

primeList = []
for i in range(1,200000):
	if prime.checkprime(i,2) == True:
		primeList.append(i)

#for i in range(1,len(primeList)):
#	print (primeList[i])

target=600851475143

#while target > 2:
#for i in range(1,len(primeList)):
#	if (target % primeList[i]) ==0:
#		print (i)
#		target=target/i

i=1
while target > 2:
#for i in range(1,len(primeList)):
	if (target % primeList[i]) ==0:
		print (primeList[i])
		target=target/primeList[i]
	i=i+1



	