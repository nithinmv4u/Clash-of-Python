mark=float(input("Enter Total mark= "))
if(mark<=100 and mark>=90):
    print("Grade A")
elif(mark>=80):
    print("Grade B")
elif(mark>=70):
    print("Grade C")
elif(mark>=60):
    print("Grade D")
elif(mark>=50):
    print("Grade E")
elif(mark<50):
    print("Failed")
else:print("Invalid entry...")