from mycode import AddStudent,FindStudent,DeleteStudent,studentclass

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
