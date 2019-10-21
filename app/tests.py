from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


# Create your tests here.

class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.user = User(username = 'audrey', email = 'audreywncode@gmail.com', first_name = 'Audrey', last_name = 'Njiraini', password = 'njiraini123')
        self.user.save()
        
        self.audrey = Profile(id = 50, user = self.user, avatar = 'default.jpg', bio = 'Test 1')
        
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.audrey, Profile))
    
    
    # Testing Save Method
    def test_save_profile(self):
        self.audrey.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
        
    # Testing delete Method
    def test_delete_profile(self):
        self.audrey.save()
        self.audrey = Profile.objects.get(id = 50)
        
        self.audrey.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
        
        
    #Testing update method
    def test_update_profile(self):
        self.audrey.save()
        self.audrey = Profile.objects.filter(bio = 'Test 1').update(bio='Test 2')
        
        self.audrey = Profile.objects.get(bio='Test 2')
        self.assertEqual(self.audrey.bio, 'Test 2')
        
        
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        


class ProjectTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.user = User(username = 'audrey', email = 'audreywncode@gmail.com', first_name = 'Audrey', last_name = 'Njiraini', password = 'njiraini123')
        self.user.save()
        
        self.audrey = Profile(id = 50, user = self.user, avatar = 'default.jpg', bio = 'Test 1')
        
        self.project = Project(id = 50, title = 'Test 1', image = 'default.jpg', description = 'Testing', link = 'testing', author = self.audrey, pub_date = '2019-10-10')
        
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
    
    
    # Testing Save Method
    def test_save_project(self):
        self.project.save()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
        
        
    # Testing delete Method
    def test_delete_project(self):
        self.project.save()
        self.project = Project.objects.get(id = 50)
        
        self.project.delete()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)
        
        
    #Testing update method
    def test_update_project(self):
        self.project.save()
        self.project = Project.objects.filter(image = 'default.jpg').update(image = 'new.jpg')
        
        self.project = Project.objects.get(image = 'new.jpg')
        self.assertEqual(self.project.image, 'new.jpg')
        
        
    def tearDown(self):
        Project.objects.all().delete()
        User.objects.all().delete()
        


class ContactTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.user = User(username = 'audrey', email = 'audreywncode@gmail.com', first_name = 'Audrey', last_name = 'Njiraini', password = 'njiraini123')
        self.user.save()
        
        self.audrey = Profile(id = 50, user = self.user, avatar = 'default.jpg', bio = 'Test 1')
        self.audrey.save()
        
        self.contact = Contact(id = 50, profile = self.audrey, phone_number = 254737819013, email = 'audreywncode@gmail.com', github = 'testing')
        
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.contact, Contact))
    
    
    # Testing Save Method
    def test_save_contact(self):
        self.contact.save()
        contacts = Contact.objects.all()
        self.assertTrue(len(contacts) > 0)
        
        
    # Testing delete Method
    def test_delete_contact(self):
        self.contact.save()
        self.contact = Contact.objects.get(id = 50)
        
        self.contact.delete()
        contacts = Contact.objects.all()
        self.assertTrue(len(contacts) == 0)
        
        
    #Testing update method
    def test_update_contact(self):
        self.contact.save()
        self.contact = Contact.objects.filter(github = 'testing').update(github = 'testing 2')
        
        self.contact = Contact.objects.get(github = 'testing 2')
        self.assertEqual(self.contact.github, 'testing 2')
        
        
    def tearDown(self):
        Contact.objects.all().delete()
        User.objects.all().delete()