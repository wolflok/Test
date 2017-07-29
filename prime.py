#!/usr/bin/env python3

def checkprime(target,denom):
	limit=target
	#print ("limit is ", limit)
	while denom <= limit:
		if target % denom ==0:
			#print (number, " is not prime")
			return False
		denom=denom+1
		limit=target//denom
	#print ("limit is ", limit)
	#print ("denom is ", denom)
	return True
		

#primeList = []
#for i in range(2,100):
#	if checkprime(i) == True:
#		primeList.append(i)


#flag=True
#number=101
#denom=2
#limit=number
#while denom < limit:
#	if (number % denom) ==0:
#		print (number, " is not prime")
#		flag=False
#		break
#	denom=denom+1
#	limit=limit//denom
#
#if flag == True:
#	print (number , "  is prime")


