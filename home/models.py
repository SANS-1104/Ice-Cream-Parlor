from django.db import models

# Create your models here.
class Login(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.IntegerField()
    yes = models.BooleanField(models.NullBooleanField(True))

    def __str__(self):
        return self.fname    


class Contact(models.Model):
    enquiry = models.TextField(max_length = 200)


