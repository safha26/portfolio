from email.policy import default
from tarfile import data_filter

from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    github_link = models.URLField(blank=True, null=True, verbose_name="GitHub link")
    live_link = models.URLField(blank=True, null=True, verbose_name="Live demo")
    technologies = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20,
    choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert')
    ], default = 'Intermediate')
    category = models.CharField(max_length=30, choices=[
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('Database', 'Database'),
        ('Tools', 'Tools'),
        ('Framework', 'Framework'),
        ('Other', 'Other')
    ], default='Other')
    def __str__(self):
        return f"{self.name}-{self.level}"

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True, null=True)
    currently_working = models.BooleanField(default = False, verbose_name="Currently working ?")

    def __str__(self):
        return f"{self.role} at {self.company}"
    class Meta:
        ordering = ['-start_date']

class Education(models.Model):
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=150)
    grade = models.CharField(max_length=20, verbose_name="Percentage / CGPA")
    start_year = models.CharField(max_length=20, blank=True, null=True, verbose_name="Start Year")
    end_year = models.CharField(max_length=10, verbose_name="End Year")

    def __str__(self):
        return f"{self.degree} - {self.school}"
    class Meta:
        ordering = ['-end_year']

class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    email = models.EmailField()
    alt_email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    about = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Personal Info"
