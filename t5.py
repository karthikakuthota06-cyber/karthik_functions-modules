# Calculating factorial using loops

def factorial(a):     			# defining factorial function
	s=1
	if(a==0):
		return s
	else:
		while(a>0):
			s*=a	
			a-=1
		return s
b=int(input("Enter a number: "))    	#input from the user
c=factorial(b)				# function called
print(f"Factorial of {b} is: {c}")

"""Calculating factorial using recursion.

def factorial(a):
	s=1
	if a<0:
		print("You have entered Negative number.")
		return None
	else:
		if a==0:
			return 1
		else:
			b=a*factorial(a-1)
		return b
c=int(input("Enter a number: "))
d=factorial(c)
print(f"Factorial of {c} is {d}")  """
