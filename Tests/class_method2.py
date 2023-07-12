class Student():
    def __init__(self,name,place):
        self.name=name
        self.place=place

    def __str__(self):
        return f"{self.name} from {self.place}"
    
    @classmethod
    def get(cls):
        name=input('Enter name: ')
        place=input('Enter Place: ')
        return cls(name,place)

def main():
    student=Student.get()
    print(student)

main()