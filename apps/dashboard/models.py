from django.db import models

# title, network, releasedate
class Show(models.Model):

    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    releaseDate = models.DateField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __repr__(self):
        return f'The title is: {self.title} and id: {self.id}' 




# Inside your app's models.py file
# imports
# class Blog(models.Model):
#     name = models.CharField(max_length=255)
#     desc = models.TextField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     objects = BlogManager()    # add this line!
# """
# models come with a hidden property:
#       objects = models.Manager()
# we are going to override this!
# """
# import re	# the regex module
# class BlogManager(models.Manager):
#     def basic_validator(self, postData):    
#         errors = {}
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
#             errors['email'] = ("Invalid email address!")
#         return errors
