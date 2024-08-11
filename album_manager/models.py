from django.db import models

class Category(models.Model):
    category_name= models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=30, null=False)
    price = models.PositiveIntegerField(null=False, default=1)
    manufacturer = models.CharField(max_length=30, null=False)
    category_name = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product_name} - {self.manufacturer}"
    
class Client(models.Model):
    name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    age = models.PositiveIntegerField(null=False, default=1)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.name
    
class Purchase(models.Model):
    client = models.ForeignKey(Client, related_name='purchase', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name='purchase')
    purchase_date = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.total