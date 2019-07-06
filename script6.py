name = str(input("Enter your name: "))
names =  name.split()
if (len(names) < 2):
    print("your name is: " +  names[0])
else:
    print("your first name is: " + names[0] +  " your last name is: " +  names[1])
