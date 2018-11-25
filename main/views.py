from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

from datetime import datetime

from .models import Language, MonthlyStack, Technology, ErrorMessage, CustomUser, StudentSubmission, Comment

import sys

TODAY = datetime.today().date()

def get_current_user(username):
    return CustomUser.objects.get(username=username)

####### HOME ERRORS PAGE ##########
@login_required
def index(request):
    current_user = get_current_user(request.user)
    if not current_user.current_stack or current_user.current_stack.end_date < TODAY:
        messages.warning(request, "Please update your current stack")
        return redirect("/accounts/update")
    active_stack = current_user.current_stack
    context = {
        "active_stack": active_stack,
        "stacks": MonthlyStack.objects.filter(start_date__lte=TODAY, end_date__gte=TODAY),
        "errors": ErrorMessage.objects.filter(language=active_stack.language).order_by("message")
    }
    return render(request, 'errors/home.html', context)

@login_required
def filtered_errors(request, id):
    requested_language = MonthlyStack.objects.get(id=id).language
    context = {
        "language": requested_language,
        "errors": ErrorMessage.objects.filter(language=requested_language).order_by("message")
    }
    return render(request, 'errors/partials/filtered.html', context)

@login_required
def add_error(request):
    if request.method == "POST":
        if len(request.POST['error']) > 0:
            ErrorMessage.objects.create(message=request.POST['error'], language=Language.objects.get(id=request.POST["language"]))
    return redirect("/")

####### SINGLE ERROR PAGE ##########
@login_required
def show(request, id):
    current_stack = get_current_user(request.user).current_stack
    current_error = ErrorMessage.objects.get(id=id)
    context = { 
        'error': current_error,
        'student_submissions': StudentSubmission.objects.filter(error=current_error, stack=current_stack),
    }
    return render(request, "errors/one.html", context)    

@login_required
def add(request, id):
    if request.method == "POST":
        try:
            current_user = CustomUser.objects.get(username=request.user)
            current_error = ErrorMessage.objects.get(id=id)
            new_submission = StudentSubmission(uploader=current_user, description=request.POST["description"], error=current_error, stack=current_user.current_stack)

            ### upload and add each image
            fs = FileSystemStorage()
            if 'error' in request.FILES:
                filename = fs.save(request.FILES['error'].name, request.FILES['error'])
                new_submission.error_image = "media/" + filename
            if 'code-error' in request.FILES:
                filename = fs.save(request.FILES['code-error'].name, request.FILES['code-error'])
                new_submission.code_error_image = "media/" + filename
            if 'code-fix' in request.FILES:
                filename = fs.save(request.FILES['code-fix'].name, request.FILES['code-fix'])
                new_submission.code_fixed_image = "media/" + filename
            new_submission.save()

            count = StudentSubmission.objects.filter(error=current_error, stack=current_user.current_stack).count()
            context = {
                'new_submission': new_submission,
                'total_count': count,
            }
            new_submission_html = render(request, "errors/partials/single_error.html", context)
            return JsonResponse({'html': new_submission_html.content.decode("utf-8"), 'size': count })
        except:
            print(sys.exc_info()[0])
            return HttpResponse(status=500)
    return redirect("/")

# def test_partial(request):
#     count = StudentSubmission.objects.all().count()
#     context = {
#         'new_submission': StudentSubmission.objects.last(),
#         'total_count': count,
#     }
#     print("context")
#     return render(request, "errors/partials/single_error.html", context)

@login_required
def update_with_solution(request, id):
    if request.method == "POST":
        current_user = get_current_user(request.user)
        submission = StudentSubmission.objects.get(id=id)

        fs = FileSystemStorage()
        if 'code-fix' in request.FILES:
            filename = fs.save(request.FILES['code-fix'].name, request.FILES['code-fix'])
            submission.code_fixed_image = "media/" + filename
            submission.save()
            return JsonResponse({'imageURL': f"media/{filename}"})
    return redirect(reverse('main:show', args=(submission.error.id,)))
    return JsonResponse(status=500)

@login_required
def add_comment(request, id):
    if request.method == "POST":
        if request.POST["exp"] != "":
            response = {}
            current_user = get_current_user(request.user)
            submission = StudentSubmission.objects.get(id=id)
            comment = Comment.objects.create(content=request.POST["exp"], author=current_user, student_error = submission)
            response['username'] = current_user.username
            response['answer'] = comment.content
            response['timestamp'] = comment.created_at.strftime("%b. %d, %Y, %I:%M %p")
        return JsonResponse(response)
    return redirect("/")