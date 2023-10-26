from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from .forms import RegisterUserForm, UserLoginForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView




class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data()
        context['title'] = 'Fur-Store'
        return context




class UserRegistrationView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url =reverse_lazy('users:login')



#
# def register(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:login'))
#         else:
#             print(form.errors)
#     else:
#         messages.error(request, 'Please correct the errors below!')
#         form = RegisterUserForm()
#     context = {'form': form}
#     return render(request, 'register.html', context)




def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:home'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)



@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:home'))



# class UserProfileView(UpdateView):
#     model = User
#     form_class = UserProfileForm
#     template_name = 'profile.html'





@login_required
def user_profile(request):
    username = request.user.username
    email = request.user.email
    form = UserProfileForm()
    context = {
        'title': 'User-Profile',
        'form': form,
        'username' : username,
        'email': email
    }
    return render(request, 'profile.html', context)












