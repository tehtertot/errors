from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import CustomUser, ErrorMessage

@login_required
def index(request):
    context = {
        'current_user': CustomUser.objects.get(username=request.user),
        'attr_errors': CustomUser.objects.raw("SELECT users.id, username, COUNT(*) as 'attribute_errors' FROM users_customuser AS users JOIN main_studentimageupload AS uploads ON uploads.uploader_id = users.id WHERE uploads.error_type_id = 1 group by username;")
    }
    return render(request, "leaderboard/index.html", context)