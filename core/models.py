from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()

    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Internship(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):

    APPLICATION_TYPE = (
        ('Job', 'Job'),
        ('Internship', 'Internship'),
    )

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    mobile = models.CharField(max_length=15)

    qualification = models.CharField(max_length=200)

    skills = models.TextField()

    resume = models.FileField(
        upload_to='resumes/'
    )

    application_type = models.CharField(
        max_length=20,
        choices=APPLICATION_TYPE
    )

    applied_for = models.CharField(
        max_length=200
    )

    status = models.CharField(
        max_length=30,
        default='Pending'
    )

    applied_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name
    

class Contact(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class Quote(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    company = models.CharField(
        max_length=150,
        blank=True
    )

    service = models.CharField(max_length=100)

    budget = models.CharField(max_length=100)

    timeline = models.CharField(max_length=100)

    project_details = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name
    
    
class SiteStats(models.Model):

    projects_completed = models.IntegerField(default=150)

    happy_clients = models.IntegerField(default=100)

    team_members = models.IntegerField(default=10)

    years_experience = models.IntegerField(default=5)

    def __str__(self):
        return "Website Statistics"
    

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(default=5)
    review = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name