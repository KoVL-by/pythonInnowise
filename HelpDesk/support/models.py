from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Ticket(models.Model):
    STATUS = (
        ('open', 'open'),
        ('closed', 'closed'),
        ('at_work', 'at_work')
    )
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=7, choices=STATUS, default='open')
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.ticket_id)

    class Meta:
        ordering = ["-created"]


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name
