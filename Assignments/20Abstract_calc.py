from abc import ABC,abstractclassmethod

class Operations(ABC):

    @abstractclassmethod
    def add(self):
        pass
    @abstractclassmethod
    def sub(self):
        pass
    @abstractclassmethod
    def mul(self):
        pass
    @abstractclassmethod
    def div(self):
        pass

class Calc(Operations):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        result=self.num1+self.num2
        return result

    def sub(self):
        result=self.num1-self.num2
        return result
    
    def mul(self):
        result=self.num1*self.num2
        return result
    
    def div(self):
        result=self.num1/self.num2
        return result

def main():
    number1=int(input('Enter 1st number: '))
    number2=int(input('Enter 2nd number: '))
    choice=int(input('Enter a choice:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n'))
    calc=Calc(number1,number2)
    if(choice>=1 and choice<=4):
        match choice:
            case 1:result=calc.add()
            case 2:result=calc.sub()
            case 3:result=calc.mul()
            case 4:result=calc.div()
    else:print('Invalid Entry!')
    print('Result=', round(result,2))

main()