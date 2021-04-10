from django.test import TestCase
from .models import StudentModels
import pytest
# Create your tests here.
class StudentTestCase(TestCase):
    def setUpClass(cls):
        print('Setup Code Activity')
        StudentModels.objects.create(studentName='Alex',Hallticket='125Jkh',Mobile='9849098490',Email='lx160cm@gmail.com',Address='Hyderabad')
        StudentModels.objects.create(studentName='Mansuri',Hallticket='160CVu7yu',Mobile='9849015452',Email='qs@qiss.com',Address='Warangal')
    def test_student(self):
        qs = StudentModels.objects.all()
        self.assertEqual(qs.count(),2)
        s1 = StudentModels.objects.get(studentName='Alex')
        s2 = StudentModels.objects.get(studentName='Mansuri')
        self.assertEqual(s1.Mobile,'9849098490')
        self.assertEqual(s2.Mobile,'9849015452')
    def test_student_1(self):
        qs = StudentModels.objects.all()
        self.assertEqual(qs.count(),2)
        s1 = StudentModels.objects.get(studentName='Alex')
        s2 = StudentModels.objects.get(studentName='Mansuri')
        self.assertEqual(s1.Mobile,'9849098490')
        self.assertEqual(s2.Mobile,'9849015452')



