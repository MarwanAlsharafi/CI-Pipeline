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

        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        @property
        def age(self):
            return self._age

from unittest import TestCase


class Student_Test(TestCase):
    def test_id(self):
        testStudent = student("Marwan", 22, 60095071)

        self.assertEqual(testStudent.id, 1)

    def test_If_ID_Is_negative(self):
        with self.assertRaises(TypeError):
            student("Marwan", 23, -1)
            
    def test_name(self):
        testStudent = student("Marwan", 22, 60095071)

        self.assertEqual(testStudent.name, "Marwan")

    
    def test_age(self):
        testStudent = student("Marwan", 22, 60095071)

        self.assertEqual(testStudent.age, 22)

    def test_if_Age_is_negative(self):
        with self.assertRaises(TypeError):
            student("Marwan", -1, 1)

#to check if the methods works

s=Student_Test()
#s.test_name()
#s.test_id()
#s.test_age()
#s.test_if_Age_is_negative()
#s.test_If_ID_Is_negative()






