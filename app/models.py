from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import MaxLengthValidator,MinLengthValidator
STATE_CHOICES = (
   ("Andaman and Nicobar Islands",'Andaman and Nicobar Islands'),
   ("Andhra Pradesh",'Andhra Pradesh'),
   ("Arunachal Pradesh",'Arunachal Pradesh'),
   ("Assam",'Assam'),
   ("Bihar",'Bihar'),
   ("Chhattisgarh",'Chhattisgarh'),
   ("Chandigarh",'Chandigarh'),
   ("Dadra and Nagar Haveli",'Dadra and Nagar Haveli'),
   ("Daman and Diu",'Daman and Diu'),
   ("Delhi",'Delhi'),
   ("Goa",'Goa'),
   ("Gujarat",'Gujarat'),
   ("Haryana",'Haryana'),
   ("Himachal Pradesh",'Himachal Pradesh'),
   ("Jammu and Kashmir",'Jammu and Kashmir'),
   ("Jharkhand",'Jharkhand'),
   ("Karnataka",'Karnataka'),
   ("Kerala",'Kerala'),
   ("Ladakh",'Ladakh'),
   ("Lakshadweep",'Lakshadweep'),
   ("Madhya Pradesh",'Madhya Pradesh'),
   ("Maharashtra",'Maharashtra'),
   ("Manipur",'Manipur'),
   ("Meghalaya",'Meghalaya'),
   ("Mizoram",'Mizoram'),
   ("Nagaland",'Nagaland'),
   ("Odisha",'Odisha'),
   ("Punjab",'Punjab'),
   ("Pondicherry",'Pondicherry'),
   ("Rajasthan",'Rajasthan'),
   ("Sikkim",'Sikkim'),
   ("Tamil Nadu",'Tamil Nadu'),
   ("Telangana",'Telangana'),
   ("Tripura",'Tripura'),
   ("Uttar Pradesh",'Uttar Pradesh'),
   ("Uttarakhand",'Uttarakhand'),
   ("West Bengal",'West Bengal')
)

class Customer(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   name=models.CharField(max_length=50)
   locality=models.CharField(max_length=200)
   city=models.CharField(max_length=50)
   zipcode=models.IntegerField()
   state=models.CharField(choices=STATE_CHOICES,max_length=50)
   def __str__(self):
      return str(self.id)
   
CATEGORY_CHOICES=(
   ('Mobiles','Mobiles'),
   ('Laptops','Laptops'),
   ("Women's Top Wear","Women's Top Wear"),
   ("Women's Bottom Wear","Women's Bottom Wear"),
   ("Men's Top Wear","Men's Top Wear"),
   ("Men's Bottom Wear","Men's Bottom Wear")
)

class Product(models.Model):
   title=models.CharField(max_length=100)
   caption=models.CharField(max_length=250)
   selling_price=models.IntegerField()
   discount_price=models.IntegerField()
   description=models.TextField()
   brand=models.CharField(max_length=50)
   category=models.CharField(choices=CATEGORY_CHOICES,max_length=20)
   product_image=models.ImageField(upload_to='productImg')
   def __str__(self):
      return str(self.id)
   
class Cart(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity=models.PositiveBigIntegerField(default=1)
   def __str__(self):
      return str(self.id)

STATUS_CHOICES=(
   ('Accepted','Accepted'),
   ('Packed','Packed'),
   ('On the way','On the way'),
   ('Delivered','Delivered'),
   ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity=models.PositiveBigIntegerField(default=1)
   ordered_date=models.DateTimeField(auto_now_add=True)
   status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

   
