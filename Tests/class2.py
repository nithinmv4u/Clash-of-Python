class Student():
    def __init__(self,name,place):
        self.name=name
        self.place=place

    def __str__(self):
        return f"{self.name} from {self.place}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name=name

    @property #--------GETTER--------
    def place(self):
        return self._place
    @place.setter  #--------SETTER---------
    def place(self,place):
        if place not in ['nilambur','malappuram','manjeri','kozhikode']:
            raise ValueError('not in desired location')
        self._place=place


def main():
    student=get_student()
    # print(f'{student.name} from {student.place}')
    print(student)

def get_student():
    name=input('Enter name: ')
    place=input('Enter place: ')
    student=Student(name,place)
    return student

main()