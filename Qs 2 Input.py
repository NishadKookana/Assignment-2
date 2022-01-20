#Question 2

text='''
Hey. name Here!
My SID is sid
I am from dept and my CGPA is cgpa'''

# Asking the user to input following details
Name=input("Enter your name= ")
SID=input("Enter your SID= ")
Dept=input("Enter your Department name= ")
CGPA=input("Enter your CGPA= ")

# Replacing texts
text=text.replace("name" , Name)
text=text.replace("sid" , SID)
text=text.replace("dept" , Dept)
text=text.replace("cgpa" , CGPA)

print(text)
