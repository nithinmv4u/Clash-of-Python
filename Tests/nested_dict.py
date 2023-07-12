def marks():
    mark = {}
    mark['English']=int(input("Enter English marks: "))
    mark['Chemistry']=int(input("Enter Chemistry marks: "))
    mark['Physics']=int(input("Enter Physics marks: "))
    return mark

def interests():
    interests=[]
    for _ in range(3):
        interests.append(input("Enter interest: "))
    return interests

def student_details():
    detail = {}
    # age=input("Enter age: ")
    detail['age']=int(input("Enter age: "))
    detail['place']=input("Enter place: ")
    detail['marks']=marks()
    detail['interests']=interests()
    # print(detail)
    return detail

def student_name(students):
    name=input("Enter Name: ")
    students[name]=student_details()
    # print(students)
    return students

if __name__ == '__main__':
    students={}
    while(True):
        option = int(input("1.Add Student\nPress any other key to exit..!\nSelect Option:").strip().split()[0])
        # print(option==1)
        if (option==1 or option==2) :
            match option:
                case 1:
                    students = student_name(students)
                    print(students)
        else:break