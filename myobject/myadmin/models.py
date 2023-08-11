from django.db import models
from datetime import datetime

class User(models.Model):
    username = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.IntegerField(default=1)
    create_at=models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id':self.id,'username':self.username,'nickname':self.nickname,'password':
                self.password,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-&d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-&d %H:%M:%S')}

    class Meta:
        db_table = "user"
class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.IntegerField(default=1)
    create_at=models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "category"

class Product(models.Model):
    category_id = models.IntegerField()
    cover_pic = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    print = models.FloatField(max_length=10)
    status = models.IntegerField(default=1)
    create_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id': self.id, 'category_id': self.category_id, 'cover_pic': self.cover_pic, 'name': self.name,'price': self.print, 'status': self.status,
            'create_at': self.create_at.strftime('%Y-%m-&d %H:%M:%S'),
            'update_at': self.update_at.strftime('%Y-%m-&d %H:%M:%S')}

    class Meta:
        db_table = "product"
class Order(models.Model):
    user_id = models.IntegerField()
    money = models.FloatField()
    status = models.IntegerField(default=1)
    payment_status = models.IntegerField(default=1)
    create_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "orders"
class OrderDetail(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    status = models.IntegerField(default=1)

    class Meta:
        db_table = "order_detail"

class Payment(models.Model):
    order_id = models.IntegerField()
    money =models.FloatField()
    pay_type = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    create_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "payment"







