from unittest import TestCase

students=[{'name':'Marwan','age':23,'id':60095071},{'name':'Ali','age':23,'id':60095555},
          {'name':'Ahmed','age':24,'id':60097141},{'name':'Jamal','age':21,'id':60102546}]

def AddStudent():
    counter=0
    while counter!=1:
    
        name=str(input("enter your name "))
        age=int(input("enter your age "))
        id=int(input("enter the id "))
        
        student(name,age,id)    
        students.append({'name':name,'age':age,'id':id,})
        counter=counter+1
        print(students)

    find=int(input('enter the student id to find the student '))
        
    FindStudent(find)

    delete=int(input('enter the student id to delete the student '))
    DeleteStudent(delete)

    print(students)


def FindStudent(id):
    for i in range(len(students)):
        if students[i]['id']==id:
            print("id exist")
        
def DeleteStudent(id):
   
    for i in range(len(students)):
        if students[i]['id']==id:
            del  students[i]
       
           




class student:
    def __init__(self,name,age,id):

        if type(name)!=str:
            raise TypeError("Name must be string")
        if type(age) != int:
            raise TypeError("Age must be an integer")
        if type(id) != int:
            raise TypeError("ID must be an integer")
        if age < 0:
            raise ValueError("Age must be positive")
        if id < 0:
            raise ValueError("ID must be positive")

        self.name = name
        self.age = age
        self.id = id

        def id(self):
            return self._id

        def name(self):
            return self._name

        def age(self):
            return self._age

        



class Student_Test(TestCase):
    def test_id(self):
        testStudent = student("Marwan", 22, 60095071)

        self.assertEqual(testStudent.id, 60096009)

    def test_If_ID_Is_negative(self):
        with self.assertRaises(TypeError):
            student("Marwan", 23, -1)
            
    def test_name(self):
        testStudent = student(25, 22, 60095071)

        self.assertEqual(testStudent.name, 'Marwan')

    
    def test_age(self):
        testStudent = student("Marwan", -22, 60095071)

        self.assertEqual(testStudent.age, 22)

    def test_if_Age_is_negative(self):
        with self.assertRaises(TypeError):
            student("Marwan", -1, 1)




AddStudent()



