from multiprocessing import context
from django.shortcuts import render



def login(request):
    context = dict()
    context['message'] = "welcome to solumada Académie"
    return render(request, template_name='log/login.html', context=context)

class LoginView():
    pass 



class LogoutView():
    pass