from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Language, Technology, MonthlyStack, ErrorMessage, StudentSubmission, Comment

class LanguageAdmin(admin.ModelAdmin):
    pass
class TechnologyAdmin(admin.ModelAdmin):
    pass
class StackAdmin(admin.ModelAdmin):
    pass
class ErrorMessageAdmin(admin.ModelAdmin):
    pass
class StudentSubmissionAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Language, LanguageAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(MonthlyStack, StackAdmin)
admin.site.register(ErrorMessage, ErrorMessageAdmin)
admin.site.register(StudentSubmission, StudentSubmissionAdmin)
admin.site.register(Comment, CommentAdmin)