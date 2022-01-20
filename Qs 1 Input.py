#Question 1

line="Python is a case sensitive language"

#Calculating lenght of the text
length=len(line)
print("Lenght of text is= ",length)

#Reversing the order 
reverse=line[::-1]
print("Reversed order of text is= ",reverse)

#Now slicing the text
print("Sliced line of text is= ",line[10:26])

#Now replacing the words
replaced=line.replace("a case sensitive" , "object oriented")
print("Text after replacing words is= ",replaced)

#Calculating indexes of 'a'
print(line.count("a"))

#Removing spaces from text
removed_spaces=line.replace(" " , "")
print("String afterremoving spaces is= ",removed_spaces)

