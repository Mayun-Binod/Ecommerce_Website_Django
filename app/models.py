from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICES=(
    ("Koshi", "Koshi Province"),
    ("Madhesh", "Madhesh Province"),
    ("Bagemati", "Bagmati Province"),
    ("Gandaki", "Gandaki Province"),
    ("Lumbini", "Lumbini Province"),
    ("Karnali", "Karnali Province"),
    ("Sudurpashchim", "Sudurpashchim Province"),
)
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES=(
    ('MB','Mobile'),
    ('LP','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom War'),
)

class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=200)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=5)
    product_image=models.ImageField(upload_to="productimage")

    def __str__(self):
        return str(self.id)



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
STATUS_CHOICES=(
    ('Accept','Accepted'),
    ('Pack','Packed'),
    ('on the way','On The Way'),
    ('Deliver','Delivered'),
    ('cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATE_CHOICES,default='pending')