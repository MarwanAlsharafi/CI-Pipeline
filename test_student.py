from unittest import TestCase
from student_program import AddStudent, FindStudent, DeleteStudent, student


class Student_Test(TestCase):
    def test_id(self):
        testStudent = student("Marwan", 22, 60095071)

        self.assertEqual(testStudent.id, 60095071)

    def test_If_ID_Is_negative(self):
        with self.assertRaises(ValueError):
            student("Marwan", 23, -1)

    def test_name(self):
        with self.assertRaises(ValueError):
            student(25, 23, -1)

    def test_age(self):
        testStudent = student("Marwan", 22, 60095071)

        self.assertEqual(testStudent.age, 22)

    def test_if_Age_is_negative(self):
        with self.assertRaises(ValueError):
            student("Marwan", -1, 1)
