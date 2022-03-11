from django.db import models
from signups.models import Usersignup

# Create your models here.
class Projects(models.Model):
    user = models.ForeignKey(Usersignup, on_delete = models.CASCADE)
    proj_title = models.CharField(max_length=400)
    project_link = models.CharField(max_length=400)
    project_image = models.ImageField(upload_to = 'projects/')
    project_description = models.CharField(max_length=4000)
    date_posted = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Projects'

    def __str__(self):
        return self.user

class Userbio(models.Model):
    user = models.ForeignKey(Usersignup, on_delete = models.CASCADE)
    bio = models.CharField(max_length=3000)
    date_posted = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Userbio'

    def __str__(self):
        return self.bio
class Rated(models.Model):
    post = models.ForeignKey(Projects, on_delete = models.CASCADE)
    rated_by = models.ForeignKey(Usersignup, on_delete = models.CASCADE)
    rated_count = models.IntegerField()