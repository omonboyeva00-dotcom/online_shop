

from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import timezone, datetime, timedelta

class CustomerUser(AbstractUser):

    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class EmailCode(models.Model):
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE, related_name='email_codes')
    code=models.CharField(max_length=6)
    created_at= models.DateTimeField(auto_now_add=True)
    is_activated=models.BooleanField(default=False)
    expires_at=models.DateTimeField(null=True,blank=True)


    def save(self, *args,**kwargs):
        self.expires_at=datetime.now()+timedelta(minutes=1)
        super(EmailCode, self).save(*args,**kwargs)




