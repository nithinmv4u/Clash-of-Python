class Home:
    def __init__(self):
          pass 
    def room1(self): 
        width=100 
        breadth = 100 
        print('area of room1: ',width*breadth) 
    def kitchen(self): 
        width = 1222
        breadth = 4888 
        print('area of kitchen: ',width*breadth)

class FirstHome(Home):
    def study_room(self):
        width =1000
        breadth=3000
        print('area of study room: ',width*breadth)

class SecondHome(Home):
    def work_area(self):
        width =1500
        breadth=3500
        print('area of work area: ',width*breadth)

def main():
    first_h=FirstHome()
    second_h=SecondHome()
    first_h.room1()
    first_h.kitchen()
    first_h.study_room()
    second_h.room1()
    second_h.kitchen()
    second_h.work_area()

main()