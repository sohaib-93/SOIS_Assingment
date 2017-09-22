# !/usr/bin/python3
# Python Assignment
# Program 11: Implement a python code to check whether a given number is ARMSTRONG number or prime or both.


def armstrong(num):
	temp = int(num)
	sumarm = 0
	count = 0

	while(temp > 0):  #To count the number of digits.
		temp = int(temp/10)
		count += 1

	temp = num
	
	while(temp > 0):
		rem = int(temp%10)
		sumarm += (rem**count)  
		temp = int(temp/10)

	if(sumarm == num):	# To check the armstrong condition
		return 1
	else:
		return 0


def prime(num):
	flag = 1
	for i in range(2,num):
		if((num%i) == 0):  # To check if the number is prime or not
			flag = 0
			break

	if(num == 1):
		flag=0

	if(flag == 1):
		return 1
	else:
		return 0


num = int(input("Please enter the number: "))
print (num)
arm = armstrong(num)
prime = prime(num)

if((arm == 1) and (prime == 1)):
	print("The number is both prime and armstrong")
elif(prime == 1):
	print("The number is prime")
elif(arm == 1):
	print("The number is armstrong")
else:
	print("The number is neither prime nor armstrong")
