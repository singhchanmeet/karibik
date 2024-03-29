from django.db import models
from django.utils.html import mark_safe
# Create your models here.
from django.db import models

class Enrollment(models.Model):

    programme_to_apply = models.CharField(max_length=100)
    candidate_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    alternate_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField()
    email_id = models.EmailField()
    gender = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='profile_photos/')
    tenth_percentage = models.CharField(max_length=10)
    twelfth_percentage = models.CharField(max_length=10)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.candidate_name
    
    def photograph_preview(self): #new
        return mark_safe(f'<img src = "{self.photo.url}" width = "100"/>')
