from django.db import models

class Product(models.Model):
	name = models.CharField(max_length = 64, blank = True, null = True, default = None)
	description = models.TextField(max_length = 64, blank = True, null = True, default = None)
	created = models.DateTimeField(auto_now_add = True)	
	updates = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

class ProductImage(models.Model):
	product = models.ForeignKey(Product, blank = True, null = True, default = None, on_delete = models.CASCADE)
	image = models.ImageField(upload_to='products_images/')
	is_active = models.BooleanField(default = True)
	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Фото Товара'
		verbose_name_plural = 'Фото Товаров'