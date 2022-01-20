#Question 6

side_1=int(input("Enter 1st side= "))
side_2=int(input("Enter 2nd side= "))
side_3=int(input("Enter 3rd side= "))

if side_1>=side_2+side_3:
    print("No")
elif side_2>=side_1+side_3:
    print("No")
elif side_3>=side_1+side_2:
    print("No")
else:
    print("Yes")
