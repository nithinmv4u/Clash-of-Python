class Aname():
    def __init__(self,name):
        if not name:
            raise ValueError('No name found')
        self.name=name

class Student(Aname):
    def __init__(self,name,place):
        super().__init__(name)
        self.place=place
    def __str__(self):
        return f"{self.name} is at {self.place}"

class Proffesor(Aname):
    def __init__(self,name,place):
        super().__init__(name)
        self.place=place
    def __str__(self):
        return f"{self.name} is at {self.place}"

student=Student('harry','nilambur')
professor=Proffesor('porter','kozhikode')
print(student)
print(professor)