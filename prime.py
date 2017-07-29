#!/usr/bin/env python3

def checkprime(target,denom):
	flag=True
	limit=target
	#print ("limit is ", limit)
	while denom <= limit:
		if (target % denom) ==0:
			#print (number, " is not prime")
			flag=False
			break
		denom=denom+1
		limit=target//denom
	if flag==False:
		return False
	else:
		return True
		

