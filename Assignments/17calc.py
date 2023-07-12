class Calc():
    def addition(self,a,b):
        a=a+b
        return a
    def substaction(self,a,b):
        a=a-b
        return a
    def multiply(self,a,b):
        a=a*b
        return a
    def divide(self,a,b):
        a=a/b
        return a

def main():
    number1=int(input('Enter 1st number: '))
    number2=int(input('Enter 2nd number: '))
    choice=int(input('Enter a choice:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n'))
    # calc=Calc(number1,number2)
    calc=Calc()
    if(choice>=1 and choice<=4):
        match choice:
            case 1:result=calc.addition(number1,number2)
            case 2:result=calc.substaction(number1,number2)
            case 3:result=calc.multiply(number1,number2)
            case 4:result=calc.divide(number1,number2)
    else:print('Invalid Entry!')
    print('Result=', result)

main()
