from django.test import TestCase
from .models import *
from django.utils import timezone
from django.urls import reverse
from .views import *


# models test
class  CategoryTest(TestCase):

    def create_category(self, title="only a test", body="yes, this is only a test"):
        return  Category.objects.create(title=title, body=body, created_at=timezone.now())

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c,  Category))
        self.assertEqual(c.__unicode__(), c.title)


class  BranchTest(TestCase):

    def create_branch(self, title="only a test", body="yes, this is only a test"):
        return Branch.objects.create(title=title, body=body, created_at=timezone.now())

    def test_Branch_creation(self):
        b = self.create_branch()
        self.assertTrue(isinstance(b,  Branch))
        self.assertEqual(b.__unicode__(), b.title)

class ContactTest(TestCase):

    def create_contact(self, title="only a test", body="yes, this is only a test"):
        return  Contact.objects.create(title=title, body=body, created_at=timezone.now())

    def test_category_creation(self):
        cc = self.create_contact()
        self.assertTrue(isinstance(cc,  Contact))
        self.assertEqual(cc.__unicode__(), cc.title)

class  CourseTest(TestCase):

    def create_course(self, title="only a test", body="yes, this is only a test"):
        return  Course.objects.create(title=title, body=body, created_at=timezone.now())

    def test_Course_creation(self):
        ccc = self.create_course()
        self.assertTrue(isinstance(ccc,  Course))
        self.assertEqual(ccc.__unicode__(), ccc.title)

