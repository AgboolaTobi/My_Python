from unittest import TestCase
from Class_Exercises import student_age


class Test(TestCase):
    def test_student_age_correction(self):
        self.assertTrue(student_age.students)

    # def test_student_(self):
    #     self.assertTrue(student_age.student_age())
