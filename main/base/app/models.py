from django.db import models
from django.contrib.auth.models import User

class Applicant(models.Model):
    name = models.CharField(max_length=100, default='name')
    # Default value is an empty string
    firstName = models.CharField(max_length=100, default='')
    # Default value is an empty string
    lastName = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=20, choices=[
        ('option1', 'Male'),
        ('option2', 'Female'),
        ('option3', 'Prefer not to say'),
    ], default='option1')  # Default value is 'Male'
    email = models.EmailField(default='')  # Default value is an empty string
    # Default value is an empty string
    phoneNumber = models.CharField(max_length=20, default='')
    address = models.TextField(default='')  # Default value is an empty string
    # Default value is an empty string
    position = models.CharField(max_length=100, default='')
    dropdown1 = models.CharField(max_length=50, choices=[
        ('ai', 'Artificial Intelligence'),
        ('web-dev', 'Web Development'),
        ('blockchain', 'Blockchain'),
        ('testing', 'Testing'),
        ('database', 'Database'),
    ], default='ai')  # Default value is 'Artificial Intelligence'
    dropdown2 = models.CharField(max_length=50, choices=[
        ('beginner', '0-5 yrs'),
        ('intermediate', '5-10 yrs'),
        ('advanced', '10-20 yrs'),
        ('master', '20+ yrs'),
    ], blank=True, default='beginner')  # Default value is '0-5 yrs'
    dropdown3 = models.CharField(max_length=50, choices=[
        ('option1', 'Offline'),
        ('option2', 'Online'),
        ('option3', 'Hybrid'),
    ], default='option1')  # Default value is 'Offline'
    fileUpload = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
    class Meta:
        db_table = 'user'
        app_label = 'app'


class Recruiter(User):
    def __str__(self):
        return f"{self.get_full_name}"