from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=200)
	product_details = models.TextField()
	price = models.IntegerField()
	active = models.IntegerField(default='1')

	def __str__(self):
		return '%s (%s tk)' % (self.product_name, self.price)

class Order (models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    delivery_date = models.DateField(blank=True)
    product_id = models.ForeignKey(
    	'Product',
    	on_delete=models.CASCADE,
    	)

    table_id = models.ForeignKey(
        'Table',
        on_delete=models.CASCADE, null = True
        )
    payment_option = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    quantity = models.IntegerField()



class Table(models.Model):
    table_name = models.CharField(max_length=200)
    table_number = models.IntegerField()
    active = models.IntegerField(default=1)

    def __str__(self):
        return self.table_name

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    active = models.IntegerField(default=1)
    def __str__(self):
        return self.category_name