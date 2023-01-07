from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class CustomUser(AbstractUser):
    status = models.CharField(verbose_name=("status"), max_length = 255, blank=True, null=True,)
    mat_no = models.CharField(verbose_name=("mat_no"), max_length = 255, blank=True, null=True,)
    course_code = models.CharField(verbose_name=("course_code"), max_length = 255, blank=True, null=True,)


    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"





# LECTURER ASSIGNMENT MODEL

class Lecturer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    course_code = models.CharField(max_length=255, null= True)
    due = models.DateTimeField(blank=True)
    attachment = models.FileField(upload_to='media/files')
    date_created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(null=True)


    def __str__(self):
        return self.course_code




# STUDENT ASSIGNMENT MODELS

class Student(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    course_code = models.CharField(max_length=255, null= True)
    answer = models.TextField()
    mat_no = models.CharField(max_length=255, null= True)
    attachment = models.FileField(upload_to='media/files')
    date_created = models.DateTimeField(auto_now_add=True)
    assignment = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null = True)
    score = models.IntegerField(null=True)
    assign_title = models.CharField(max_length=255, null= True)


    def __str__(self):
        return self.name + "  ===========  " + str(self.id)

