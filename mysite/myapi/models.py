from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    catch_phrase = models.CharField(max_length=60)

    def __str__(self):
        return self.username
    