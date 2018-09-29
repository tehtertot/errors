from django.db import models
from users.models import CustomUser

class Language(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # values: Python, JavaScript, C#, Java
    def __repr__(self):
        return f"<Language: {self.id} - {self.name}>"
    def __str__(self):
        return f"<Language: {self.id} - {self.name}>"

class Framework(models.Model):
    name = models.CharField(max_length=30)
    language = models.ForeignKey(Language, related_name="frameworks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # values: Fundamentals, Flask, Django, ASP.NET Core, Angular, Express, Mongoose, Spring Boot
    def __repr__(self):
        return f"<Framework: {self.id} - {self.name}>"
    def __str__(self):
        return f"<Framework: {self.id} - {self.name}>"

class ErrorMessage(models.Model):
    message = models.CharField(max_length=50)
    framework = models.ForeignKey(Framework, related_name="framework_errors", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Keyword: {self.message}>"
    def __str__(self):
        return f"{self.message} ({self.framework.language.name} - {self.framework.name})"

class StudentImageUpload(models.Model):
    image_error = models.CharField(max_length=255, null=True)
    image_code_error = models.CharField(max_length=255, null=True)
    image_code_fix = models.CharField(max_length=255, null=True)
    uploader = models.ForeignKey(CustomUser, related_name="image_sets_uploaded", on_delete=models.SET_NULL, null=True)
    error_type = models.ForeignKey(ErrorMessage, related_name="images", on_delete=models.SET_NULL, null=True)
    def __repr__(self):
        return f"<Upload: {self.id} for {self.error_type.message}>"

class Explanation(models.Model):
    content = models.TextField()
    explainer = models.ForeignKey(CustomUser, related_name="explanations", on_delete=models.CASCADE)
    associated_error = models.ForeignKey(StudentImageUpload, related_name="explanations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return f"<Suggestion: {self.content} for {self.associated_error}>"