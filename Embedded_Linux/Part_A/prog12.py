#!/usr/bin/python3
#Python Assignment
#Program 12: Implement a python code to check to a) count total number of vowels b) individual count of vowel characters.

str1 = input("Please enter the string: ")

count = 0
counta = 0
counte = 0
counti = 0
counto = 0
countu = 0

str1 = str1.lower()

for i in str1:
	if(i == 'a'):
		counta += 1
	elif(i == 'e'):
		counte += 1
	elif(i == 'i'):  
		counti += 1
	elif(i == 'o'): 
		counto += 1
	elif(i == 'u'):
		countu += 1

count = counta+countu+counto+counti+counte

print ("The total count is",count)

print ("Number of A:", counta)
print ("Number of E:", counte)
print ("Number of I:", counti)
print ("Number of O:", counto)
print ("Number of U:", countu)
