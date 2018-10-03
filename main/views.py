from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

from .models import Language, Framework, ErrorMessage, CustomUser, StudentImageUpload, Explanation

@login_required
def index(request):
    context = {
        "languages": Language.objects.all(),
        "frameworks": Framework.objects.all(),
        "errors": ErrorMessage.objects.filter(framework_id=2).order_by("message")
    }
    return render(request, 'errors/home.html', context)

@login_required
def filtered_errors(request, id):
    context = {
        "errors": ErrorMessage.objects.filter(framework_id=id).order_by("message")
    }
    return render(request, 'errors/filtered.html', context)

@login_required
def show(request, id):
    context = { 
        'error': ErrorMessage.objects.get(id=id),
    }
    return render(request, "errors/one.html", context)    

@login_required
def add(request, id):
    if request.method == "POST":
        try:
            current_user = CustomUser.objects.get(username=request.user)
            new_error = StudentImageUpload(uploader=current_user, error_type_id=id)
            # # upload and add each image
            fs = FileSystemStorage()
            if 'error' in request.FILES:
                error_filename = fs.save(request.FILES['error'].name, request.FILES['error'])
                new_error.image_error = "media/" + error_filename
            if 'code_error' in request.FILES:
                code_error_filename = fs.save(request.FILES['code_error'].name, request.FILES['code_error'])
                new_error.image_code_error = "media/" + code_error_filename
            if 'code_fix' in request.FILES:
                code_fix_filename = fs.save(request.FILES['code_fix'].name, request.FILES['code_fix'])
                new_error.image_code_fix = "media/" + code_fix_filename
            new_error.save()
            if request.POST["explanation"] != "":
                Explanation.objects.create(content=request.POST["explanation"], explainer=current_user, associated_error=new_error)
        except:
            response['status'] = 0
        #     return JsonResponse(response)
    return redirect(reverse('main:show', args=(id,)))

@login_required
def update_with_solution(request, id):
    if request.method == "POST":
        current_user = get_current_user(request)
        user_error = StudentImageUpload.objects.get(id=id)
        fs = FileSystemStorage()
        code_fix_filename = fs.save(request.FILES['code_fix'].name, request.FILES['code_fix'])
        user_error.image_code_fix = "media/" + code_fix_filename
        user_error.save()
    return redirect(reverse('main:show', args=(user_error.error_type.id,)))

@login_required
def add_explanation(request, id):
    if request.method == "POST":
        response = { 'status': False }
        if request.POST["exp"] != "":
            response['status'] = True
            current_user = get_current_user(request)
            student_error = StudentImageUpload.objects.get(id=id)
            new_exp = Explanation.objects.create(content=request.POST["exp"], explainer=current_user, associated_error=student_error)
            response['username'] = current_user.username
            response['answer'] = new_exp.content
        return JsonResponse(response)

def get_current_user(request):
    return CustomUser.objects.get(username=request.user)