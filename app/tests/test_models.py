from django.test import TestCase
from app.models import Bucketlist
from django.contrib.auth.models import User


# Create your tests here.

class ModelTestCase(TestCase):
    """Defines the test suites for the bucket list model."""
    def setUp(self):
        """ test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.name, owner=user)
    def test_model_can_create_a_bucketlist(self):
        """ Test bucketlist model can create a bucktlist."""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count,new_count)
