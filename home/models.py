from django.db import models

class comment(models.Model):
    comment = models.TextField()
    date = models.DateField()
    pr_name = models.TextField()
class product_details(models.Model):
    product_name=models.TextField()
    short_des=models.TextField()
    long_des=models.TextField()
    product_condition=models.TextField()
    seller_type=models.TextField()
    seller_department=models.TextField()
    borrow_amount=models.TextField()
    buy_amount=models.TextField()
    seller_comment=models.TextField()
    seller_name=models.TextField()
    seller_mail=models.TextField()
    product_img=models.TextField()
    product_views = models.IntegerField()
    interactions = models.IntegerField()
    