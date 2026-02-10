firstnum = int(input("Enter the first number: "))
secnum = int(input("Enter the second number: "))
if firstnum*secnum < 0 :
    print((str(firstnum)) + " "+"x"+" "+(str(secnum))+" "+"="+" "+str((firstnum*secnum)))
    print("The result is negative.")
elif firstnum*secnum > 0 :
    print((str(firstnum)) + " "+"x"+" "+(str(secnum))+" "+"="+" "+str((firstnum*secnum)))
    print("The result is positive.")
else:
    print((str(firstnum)) + " "+"x"+" "+(str(secnum))+" "+"="+" "+str((firstnum*secnum)))
    print("The result is positive and negative")




