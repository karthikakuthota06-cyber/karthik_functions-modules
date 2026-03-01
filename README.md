                                                       ASSIGNMENT-3 : Functions & Modules in Python

1. Task-1 is about calculate the factorial of a number which is provided by the user using a loop or recusion.
   1. Calculating the factorial by loop, the program is in the t5.py .
   2. Calculating the factorial by recursion. The code is written below.
      
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
      print(f"Factorial of {c} is {d}")

    The output in both cases would be :
                                           Enter a number: 5
                                           Factorial of 5 is: 120
    

3. Task-2 is about calculating the square root, logaritm and sine function of a number which is taken as input fron the user using math module..
   The program is in the t6.py .
   The output would be :
                             Enter a number: 25
                             Square root: 5.0
                             Logaritm: 3.2188758248682006
                             Sine: -0.13235175009777303
   
