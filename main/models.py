from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Award(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    awarded_date = models.DateField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    user_name = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name
