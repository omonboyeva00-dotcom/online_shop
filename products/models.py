from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100)
    image= models.ImageField(upload_to='category_image/',null=True,blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    title=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount_price= models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    percent=models.IntegerField()
    main_image=models.ImageField(upload_to='product_images/',null=True,blank=True)
    desc=models.TextField()
    stock=models.IntegerField()

    def save(self, *args, **kwargs):
        if self.percent:
             self.discount_price=self.price-((self.price/100)*self.percent)
             super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='product_images/',null=True,blank=True)

    def __str__(self):
        return self.product.title

