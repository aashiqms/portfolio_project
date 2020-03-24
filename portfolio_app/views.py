from django.shortcuts import render
from django.http import HttpResponse
from portfolio_app.models import User


def index(request):
    return render(request, 'portfolio_app/index.html')


def users_function(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users_view_key': user_list}
    return render(request, 'portfolio_app/users.html', context=user_dict)


