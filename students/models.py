from django.db import models

class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=30)
    section = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    admission_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"