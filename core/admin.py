from django.contrib import admin
from .models import Profile, Goods, history, Notification
# Register your models here.


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'price_now', 'endingdate', 'type', 'id')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname')


@admin.register(history)
class historyAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'goods')
    list_filter = ('price', 'goods')


@admin.register(Notification)
class notificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'goods', 'type')
