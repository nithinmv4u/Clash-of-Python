number=int(input("Enter number b/w 1 & 7: "))
if(number>=0 and number<=7):
    match number:
        case 1:print("Monday")
        case 2:print("Tuesday")
        case 3:print("Wednesday")
        case 4:print("Thursday")
        case 5:print("Friday")
        case 6:print("Saturday")
        case 7:print("Sunday")
else:print("Invalid Entry!")