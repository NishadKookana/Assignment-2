#Question 4

number_1=float(input("Enter 1st number "))
number_2=float(input("Ener 2nd number "))
number_3=float(input("Enter 3rd number "))

if (number_1>number_2) and (number_1>number_3):
    print("Largest number is= ",number_1)

elif (number_2>number_1) and (number_2>number_3):
    print("Largest number is= ",number_2)

else:
    print("Largest number is= ",number_3)
