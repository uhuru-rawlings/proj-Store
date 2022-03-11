from django.db import models

# Create your models here.
class Usersignup(models.Model):
    username = models.CharField(max_length=200)
    useremail = models.EmailField(max_length=200)
    phone = models.CharField(max_length=10)
    userimage = models.ImageField(upload_to = 'profiles/')
    passwords = models.CharField(max_length=300)

    class Meta:
        db_table = 'Usersignup'

    def __str__(self):
        return self.username