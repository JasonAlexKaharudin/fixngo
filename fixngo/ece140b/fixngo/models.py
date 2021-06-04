from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=30, default="Orphan")
    postal_code = models.IntegerField()
    is_Fixer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class s_RepairRequest(models.Model):
    Macos = 'MacOS'
    windows = 'windows'
    linux = 'linux'
    types = [
        (Macos, 'MacOS'),
        (windows, 'Windows'),
        (linux, 'Linux')
    ] 

    repair_name = models.CharField(max_length=50)
    Customer = models.ForeignKey(User, on_delete=CASCADE)
    description = models.TextField(max_length=200, blank = True)
    pub_date = models.DateTimeField('Date Created')
    is_taken = models.BooleanField(default=False, null=True)
    is_Fixed = models.BooleanField(default=False, null=True)
    review = models.CharField(max_length=50, default="None")
    operating_system = models.CharField(
        max_length=15,
        choices = types, 
        default = windows
    )
    customer_postalCode = models.IntegerField()

    def __str__(self):
        return self.repair_name
    
    class Meta:
        verbose_name = ('Software Repair Request')
        verbose_name_plural = ('Software Repair Requests')

class h_RepairRequest(models.Model):
    repair_name = models.CharField(max_length=50)
    Customer = models.ForeignKey(User, on_delete=CASCADE)
    description = models.TextField(max_length=200, blank = True)
    device = models.CharField(max_length=50)
    pub_date = models.DateTimeField('Date Created')
    is_taken = models.BooleanField(default=False, null=True)
    is_Fixed = models.BooleanField(default=False, null=True)
    review = models.CharField(max_length=50, default="None")
    customer_postalCode = models.IntegerField()

    def __str__(self):
        return self.repair_name
    
    class Meta:
        verbose_name = ('Hardware Repair Request')
        verbose_name_plural = ('Hardware Repair Requests')