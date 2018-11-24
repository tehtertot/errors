from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomRegistrationForm
from main.models import MonthlyStack
from users.models import CustomUser
from datetime import datetime

class Registration(generic.CreateView):
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def update(request):
    if request.method == "GET":
        context = {
            'current_user': CustomUser.objects.get(username=request.user),
            'current_stacks': MonthlyStack.objects.filter(start_date__lte=datetime.today().date(), end_date__gte=datetime.today().date()),
        }
        return render(request, "users/update.html", context)
    elif request.method == "POST":
        errors = {}
        if len(request.POST['fname']) < 1:
            errors['fname'] = "Please provide a first name"
        if len(request.POST['lname']) < 1:
            errors['lname'] = "Please provide a last name"
        if not 'stack' in request.POST or request.POST['stack'] == "":
            errors['stack'] = "Please select your current stack"
        
        if errors:
            for k, e in errors.items():
                messages.error(request, e)
            return redirect("/accounts/update")
        current_user = CustomUser.objects.get(username=request.user)
        current_user.first_name = request.POST['fname']
        current_user.last_name = request.POST['lname']
        current_user.favorite_treat = request.POST['treat']
        current_user.current_stack = MonthlyStack.objects.get(id=request.POST['stack'])
        current_user.save()
        messages.success(request, "Account Updated!")
        return redirect("/accounts/update")