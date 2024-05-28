from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

############# Login Model Here #################

class User(AbstractUser):
    is_farmer= models.BooleanField('Is farmer', default=False)
    is_expert = models.BooleanField('Is expert', default=False)
    






class FarmerQuery(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    title_of_query = models.CharField(max_length=100)
    description_of_query = models.TextField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    



class ExpertReply(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    farmerquery = models.OneToOneField(FarmerQuery, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    expert_reply = models.TextField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
