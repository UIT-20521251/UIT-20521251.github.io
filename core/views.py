from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Goods, history, Notification
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.contrib.auth import get_user


# Create your views here.


def home_view(request):
    return render(request, 'Home.html')


def Information_view(request):
    return render(request, 'Information.html')


def signup_view(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        dateofbirth = request.POST['dateofbirth']
        imagefront = request.POST['imagefront']
        imageback = request.POST['imageback']
        tinh = request.POST['tinh']
        huyen = request.POST['huyen']
        xa = request.POST['xa']
        diachi = request.POST['diachi']
        idcard = request.POST['idcard']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email đã tồn tại')
                return redirect('Signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username đã tồn tại')
                return redirect('Signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                # create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id, phonenumber=phonenumber,
                    firstname=firstname, gender=gender, lastname=lastname,
                    imageback=imageback, imagefront=imagefront, dateofbirth=dateofbirth,
                    tinh=tinh, huyen=huyen, xa=xa, diachi=diachi, idcard=idcard,
                )
                new_profile.save()
                return redirect('Signin')
        else:
            messages.info(request, 'Mật khẩu không đúng')
            return redirect('Signup')
    else:
        return render(request, 'Signup.html')


def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Auction')
        else:
            messages.info(request, 'Thông tin đăng nhập không hợp lệ')
            return redirect('Signin')
    else:
        return render(request, 'Signin.html')


@login_required(login_url='/Signin')
def logout_view(request):
    auth.logout(request)
    return render(request, 'Signin.html')


@login_required(login_url='/Signin')
def auction_view(request):
    user_object = get_user(request)
    user_profile = Profile.objects.get(user=user_object)
    goods_list = Goods.objects.all().order_by('startingdate')
    goods_list1 = Goods.objects.filter(type="Tài sản thanh lý")
    goods_list2 = Goods.objects.filter(type="Bất động sản - Quyền sử dụng đất")
    goods_list3 = Goods.objects.filter(type="Phương tiện xe cộ")
    list1_length = len(goods_list1)
    list2_length = len(goods_list2)
    list3_length = len(goods_list3)
    list4_length = len(Goods.objects.filter(type="Sưu tầm - Nghệ thuật"))
    list5_length = len(Goods.objects.filter(type="Hàng hiệu"))
    list6_length = len(Goods.objects.filter(type="Khác"))

    context = {
        'user_profile': user_profile,
        'goods_list': goods_list,
        'goods_list1': goods_list1,
        'goods_list2': goods_list2,
        'goods_list3': goods_list3,
        'list1_length': list1_length,
        'list2_length': list2_length,
        'list3_length': list3_length,
        'list4_length': list4_length,
        'list5_length': list5_length,
        'list6_length': list6_length,
        # 'history_list': history_list
    }
    goods_now = Goods.objects.filter(
        endingdate__lt=datetime.now(), status='Đang giao dịch')
    for goods in goods_now:
        new_notification = Notification.objects.create(
            user=goods.owner, goods=goods.id, price=goods.price_now, type='Đấu giá thành công')
        new_notification.save()
        new1_notification = Notification.objects.create(
            user=goods.user, goods=goods.id, price=goods.price_now, type='Bán thành công')
        new1_notification.save()
        goods = Goods.objects.update(status='Đã bán')
    return render(request, 'Auction.html', context)


@login_required(login_url='Signin')
def lienhe_view(request):
    user_object = get_user(request)
    user_profile = Profile.objects.get(user=user_object)
    if request.method == 'POST':
        user = request.user.username
        name = request.POST['name']
        type = request.POST['browser']
        price = request.POST['price']
        diachi = request.POST['diachi']
        time = request.POST['time']
        endingdate = request.POST['endingdate']
        image = request.FILES.get('image')
        bio = request.POST['bio']

        new_goods = Goods.objects.create(
            name=name, user=user, image=image, bio=bio, type=type, price=price, price_now=price, diachi=diachi, time=time, endingdate=endingdate)
        new_goods.save()
        user_model = User.objects.get(username=user)

        new_notification = Notification.objects.create(
            user=user, goods=new_goods.id, price=price, type='Đăng bán thành công')
        new_notification.save()
        new_history = history.objects.create(
            user=user, goods=new_goods.id, price=price)
        new_history.save()
        return redirect('Auction')
    else:
        return render(request, 'Lienhe.html', {'user_profile': user_profile})


@login_required(login_url='Signin')
def goods_view(request, pk):
    user_object = get_user(request)
    user_profile = Profile.objects.get(user=user_object)
    goods_profile = Goods.objects.get(id=pk)
    goods_list = Goods.objects.filter(
        type=goods_profile.type).exclude(id=goods_profile.id)
    history_list = history.objects.filter(
        goods=goods_profile.id).order_by('-price')
    context = {
        'goods_profile': goods_profile,
        'user_profile': user_profile,
        'goods_list': goods_list,
        'history_list': history_list,
    }
    if request.method == 'POST':
        price = request.POST['price']
        if int(price) > history_list[0].price:
            history_new = history.objects.create(
                goods=pk, user=request.user.username, price=price)
            history_new.save()
            goods_profile.price_now = price
            goods_profile.owner = user_object.username
            goods_profile.save()
            return render(request, 'Goods.html', context)
        else:
            return render(request, 'Goods.html', context)
    else:
        return render(request, 'Goods.html', context)


@ login_required(login_url='Signin')
def search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        types = request.POST['types']
        goods_list = Goods.objects.filter(
            type__contains=types, name__contains=searched)
        leng = len(Goods.objects.filter(
            type__contains=types, name__contains=searched))
        return render(request, 'Search.html', {'goods_list': goods_list, 'searched': searched, 'leng': leng})
    else:
        return render(request, 'Search.html')


@ login_required(login_url='Signin')
def searchtype_view(request, types):
    goods_list = Goods.objects.filter(type__icontains=types)
    return render(request, 'Search.html', {'goods_list': goods_list})


@ login_required(login_url='Signin')
def user_view(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    history_list = history.objects.filter(
        user=user_object).order_by('-datetime')
    goods_list = Goods.objects.filter(
        user=user_object).order_by('startingdate')
    notification_list = Notification.objects.filter(
        user=user_object).order_by('-time')

    context = {
        'user_profile': user_profile,
        'history_list': history_list,
        'goods_list': goods_list,
        'notification_list': notification_list
    }
    goods_now = Goods.objects.filter(
        endingdate__lt=datetime.now(), status='Đang giao dịch')
    for goods in goods_now:
        new_notification = Notification.objects.create(
            user=goods.owner, goods=goods.id, price=goods.price_now, type='Đấu giá thành công')
        new_notification.save()
        new1_notification = Notification.objects.create(
            user=goods.user, goods=goods.id, price=goods.price_now, type='Bán thành công')
        new1_notification.save()
        goods = Goods.objects.update(status='Đã bán')
    return render(request, 'User.html', context)


@ login_required(login_url='Signin')
def changepw_view(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        password3 = request.POST['password3']
        user = auth.authenticate(
            username=user_profile.user, password=password1)
        if password3 == password2:
            if user is not None:
                u = User.objects.get(username=user_profile.user)
                u.set_password(password2)
                u.save()
                return redirect('Auction')
            else:
                messages.info(request, 'Mật khẩu không đúng')
                return redirect('Changeyourpassword')
        else:
            messages.info(request, 'Mật khẩu không khớp')
            return redirect('Changeyourpassword')
    else:
        return render(request, 'Changepw.html')
