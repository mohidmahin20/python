class Student:
    def __init__(self, name, cls , id):
        self.name=name
        self.cls =cls
        self.id=id

    def __repr__(self) -> str:
        return f'student name: {self.name}, class: {self.cls}, id: {self.id}'

class Teacher:
     def __init__(self, name, sub , id):
        self.name=name
        self.sub =sub
        self.id=id
     def __repr__(self) -> str:
         return f'teacher : {self.name}, subject: {self.sub}'
     
class School:
    def __init__(self,name) -> None:
        self.name= name
        self.teachers=[]
        self.students=[]
    def add_teacher(self,name,sub):
        id=len(self.teachers)+100
        teacher =Teacher(name,sub,id)
        self.teachers.append(teacher)
    def enroll(self,name,fee):
        if fee <6500:
            return 'not enough fee'
        else: 
            id = len(self.students)+1
            student=Student(name,'c',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee-6500}'
    def __repr__(self) -> str:
        print('welcome to ', self.name)
        print('-------our teachers-------')
        for teacher in self.teachers:
            print(teacher)
        print('-------our students-------')
        for student in self.students:
            print(student)
            return 'all done for now'



# alia = Student('alia torkari',9,1)
# ranbeer =Teacher('ranbir', 'algorithm',101)
# print(alia)
# print(ranbeer)
phitron = School('phitron')
phitron.enroll('alia',5200)
phitron.enroll('ranbeer',7900)
phitron.enroll('aishwarya',7100)
phitron.enroll('vaijaan',90000)

phitron.add_teacher('tom cruice','algo')
phitron.add_teacher('decap','dsa')
phitron.add_teacher('aj','database')
print(phitron)