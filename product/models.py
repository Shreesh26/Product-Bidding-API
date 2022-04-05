from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from userProcess.models import UserDetail
# Create your models here.

class Product(models.Model):
    PRODUCT_TYPE = (
        ('acad','Acads'),
        ('daily', 'Daily Use'),
        ('bits merch', 'BITS Merch'),
        ('su', 'SU Items'),
        ('misc', 'Miscellaneous')
    )
    user=models.ForeignKey(User, on_delete=CASCADE)
    img=models.ImageField(upload_to="product", blank=False)
    name=models.CharField(max_length=20)
    product_type=models.CharField(max_length=20, choices=PRODUCT_TYPE)
    description=models.TextField()
    start_price=models.FloatField()
    is_sold=models.BooleanField()
    def __str__(self):
        return self.name

class Bid(models.Model):
    product=models.ForeignKey(Product, on_delete=CASCADE)
    bidder=models.ForeignKey(User, on_delete=CASCADE)
    bid=models.FloatField()
    def __str__(self):
        return self.product.name +"-"+self.bidder.username

class SuccessfulBid(models.Model):
    success_bid=models.OneToOneField(Bid, on_delete=CASCADE)
    def __str__(self):
        return self.success_bid.product.name+" - "+self.success_bid.product.user.username+" - "+self.success_bid.bidder.username

