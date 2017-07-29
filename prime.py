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
	return True
		

