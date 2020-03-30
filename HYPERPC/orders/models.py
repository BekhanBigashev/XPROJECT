from django.db import models
from products.models import Product

class Status(models.Model):
	name = models.CharField(max_length=24)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Статус'
		verbose_name_plural = 'Статусы'

class Order(models.Model):
	customer_name = models.CharField(max_length = 64, blank = True, null = True, default = None)
	customer_email = models.EmailField(max_length = 48, blank = True, null = True, default = None)
	customer_phone = models.CharField(max_length = 48, blank = True, null = True, default = None)
	comments = models.TextField()
	created = models.DateTimeField(auto_now_add = True)	
	updates = models.DateTimeField(auto_now_add = True)
	status = models.ForeignKey(Status, on_delete = models.CASCADE)

	def __str__(self):
		return '%s %s ' % (self.name, self.status.name)

	class Meta:
		verbose_name = 'заказ'
		verbose_name_plural = 'заказы'

class ProductInOrder(models.Model):
	order = models.ForeignKey(Order, blank = True, null = True, default = None, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, blank = True, null = True, default = None, on_delete = models.CASCADE)
	created = models.DateTimeField(auto_now_add = True)	
	updates = models.DateTimeField(auto_now_add = True)
	is_active = models.BooleanField(default = True)

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'