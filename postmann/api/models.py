from django.db import models

# Create your models here.
class UsersAPI(models.Model):
    Name=models.CharField(max_length=50,unique=False)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=50,unique=False)

    def __str__(self):
        return self.Email
    class Meta:
        verbose_name="UsersAPI"
        verbose_name_plural = "UsersAPI"
