newlist = str(input("enter the string"))

length = len(newlist)

print(length)

length_of_list = open("text.txt", "w")

length_of_list.write(str(length))
