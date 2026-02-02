from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import timezone, datetime, timedelta

from products.models import Product


class User(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, null=True)
    address = models.TextField(unique=True)
    image= models.ImageField(upload_to="user_images/",null=True,blank=True)
    address= models.CharField(max_length=50, null=True,blank=True)
    age= models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.username



class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='wishlist')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='wishlists')


class EmailCode(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='email_codes')
    code=models.CharField(max_length=6)
    created_at= models.DateTimeField(auto_now_add=True)
    is_activated=models.BooleanField(default=False)
    expires_at=models.DateTimeField(null=True,blank=True)


    def save(self, *args,**kwargs):
        self.expires_at=datetime.now()+timedelta(minutes=1)
        super(EmailCode, self).save(*args,**kwargs)




