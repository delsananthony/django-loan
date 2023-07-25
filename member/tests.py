from django.test import TestCase
from .models import Member

class MemberCreationTest(TestCase):

    def setUp(self):

        self.member = Member.objects.create(
            firstname="John",
            lastname="Doe",
            middlename="Lee"
        )
    
    def test_created_member(self):

        self.assertEqual(self.member.firstname, "John")

    def tearDown(self):

        self.member.delete()

    