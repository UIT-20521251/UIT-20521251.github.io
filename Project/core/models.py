from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime


User = get_user_model()
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(default='1')
    bio = models.TextField(blank=True)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    imagefront = models.ImageField(
        upload_to='profile_images', default='user1.png')
    imageback = models.ImageField(
        upload_to='profile_images', default='user1.png')
    phonenumber = models.CharField(max_length=100, blank=True)
    dateofbirth = models.DateField(default='2000-10-10')
    gender = models.CharField(max_length=10, blank=True, default='Nam')
    idcard = models.IntegerField(default='00000000000000000')
    tinh = models.CharField(max_length=30, default='Tinh')
    huyen = models.CharField(max_length=30, default='Huyen')
    xa = models.CharField(max_length=30, default='xa')
    diachi = models.CharField(max_length=30, default='diachi')

    def __str__(self):
        return self.user.username


class Goods(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100, default='admin')
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='Goods_images', default='bua4.jpg')
    startingdate = models.DateTimeField(default=datetime.now)
    endingdate = models.DateTimeField(default=datetime.now)
    type = models.CharField(default='Khác', max_length=100)
    price = models.IntegerField(default='20000000')
    diachi = models.CharField(max_length=1000, default='Địa chỉ xem tài sản')
    time = models.CharField(max_length=1000, default='Thời gian xem tài sản')
    name = models.CharField(max_length=300, default='Tên tài sản')
    price_now = models.IntegerField(default='20000000')
    owner = models.CharField(max_length=100, default='Nguyễn Văn A')
    status = models.CharField(max_length=100, default='Đang giao dịch')

    def __str__(self):
        return self.user


class history(models.Model):
    goods = models.CharField(max_length=200, default='1')
    user = models.CharField(max_length=100, default='1')
    price = models.IntegerField(default='20000')
    datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user


class Notification(models.Model):
    user = models.CharField(max_length=100, default='1')
    price = models.IntegerField(default='200000')
    goods = models.CharField(default='1', max_length=200,)
    time = models.DateTimeField(default=datetime.now())
    type_choise = [
        ('Đấu giá thành công', 'Đấu giá thành công'),
        ('Đăng bán thành công', 'Đăng bán thành công'),
        ('Bán thành công', 'Bán thành công'),
        ('Đấu giá không thành công', 'Đấu giá không thành công'),
    ]
    type = models.CharField(
        max_length=100, default='Đấu giá thành công', choices=type_choise)

    def ___str__(self):
        return self.user
