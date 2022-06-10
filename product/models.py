from django.db import models
# Create your models here.

class Products(models.Model):
    class Meta:
        db_table = "product_info"

    name = models.CharField(max_length=30, null=False)
    category = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=256, null=False)
    price = models.CharField(max_length=30, null=False)
    stock = models.CharField(max_length=30, null=False)

class Category(models.Model):
    class Meta:
        db_table = "category"

    category_name = models.ForeignKey(Products, on_delete=models.CASCADE)


class OrderStatus(models.Model):
    class Meta:
        db_table = "order"

    orderplaced = models.CharField(max_length=30, null=False)
    paid = models.CharField(max_length=30, null=False)
    completed = models.CharField(max_length=30, null=False)
    sent = models.CharField(max_length=30, null=False)
    canceled = models.CharField(max_length=30, null=False)

class ProductOrder(models.Model):
    class Meta:
        db_table = "product_order"

    userorder = models.CharField(max_length=256, null=False)
    name = models.CharField(Products, on_delete=models.CASCADE)
    count = models.CharField(max_length=30, null=False)

class UserOrder(models.Model):
    class Meta:
        db_table = "user_order"

    user = models.CharField(max_length=256, null=False)
    product = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    address = models.CharField(max_length=30, null=False)
    total_price = models.CharField(max_length=30, null=False)
    discount = models.CharField(max_length=30, null=False)
    final_price = models.CharField(max_length=30, null=False)