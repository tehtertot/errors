from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Language, Framework, ErrorMessage, StudentImageUpload, Explanation

class LanguageAdmin(admin.ModelAdmin):
    pass
class FrameworkAdmin(admin.ModelAdmin):
    pass
class ErrorMessageAdmin(admin.ModelAdmin):
    pass
class StudentImageUploadAdmin(admin.ModelAdmin):
    pass
class ExplanationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Language, LanguageAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(ErrorMessage, ErrorMessageAdmin)
admin.site.register(StudentImageUpload, StudentImageUploadAdmin)
admin.site.register(Explanation, ExplanationAdmin)