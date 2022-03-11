from django.db import models

# Create your models here.
class Newslatter(models.Model):
    useremail = models.EmailField(max_length=200, unique=True)
    added_date = models.DateField(auto_now=True)
    
    class Meta:
        db_table = 'Newslatter'
        
    def __str__(self):
        return self.useremail