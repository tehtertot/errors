from django.db import models
from users.models import CustomUser

class Language(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # stacks
    # technologies
    # language_errors
    class Meta:
        db_table = 'languages'
    def __repr__(self):
        return f"<Language: {self.id} - {self.name}>"
    def __str__(self):
        return f"<Language: {self.id} - {self.name}>"

class MonthlyStack(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    language = models.ForeignKey(Language, related_name="stacks", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # student_submissions
    # current_students
    class Meta:
        db_table = 'monthly_stacks'

class Technology(models.Model):
    name = models.CharField(max_length=30)
    language = models.ForeignKey(Language, related_name="technologies", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # student_submissions

    class Meta:
        db_table = 'technologies'
    def __repr__(self):
        return f"<Technology: {self.id} - {self.name}>"
    def __str__(self):
        return f"<Technology: {self.id} - {self.name}>"

class ErrorMessage(models.Model):
    message = models.CharField(max_length=50)
    display_name = models.CharField(max_length=20, null=True)
    language = models.ForeignKey(Language, related_name="language_errors", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # student_submissions
    class Meta:
        db_table = 'error_messages'
    def __repr__(self):
        return f"<Keyword: {self.message}>"
    def __str__(self):
        return f"{self.message} - {self.display_name} ({self.language.name})"

class StudentSubmission(models.Model):
    description = models.TextField(null=True)
    error_image = models.CharField(max_length=255, null=True)
    code_error_image = models.CharField(max_length=255, null=True)
    code_fixed_image = models.CharField(max_length=255, null=True)
    error = models.ForeignKey(ErrorMessage, related_name="student_submissions", on_delete=models.CASCADE)
    uploader = models.ForeignKey(CustomUser, related_name="errors_submitted", on_delete=models.SET_NULL, null=True)
    stack = models.ForeignKey(MonthlyStack, related_name="student_submissions", on_delete=models.SET_NULL, null=True)
    associated_technologies = models.ManyToManyField(Technology, related_name="student_submissions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comments
    class Meta:
        db_table = 'student_submissions'
    def __repr__(self):
        return f"<StSub Object: {self.error.message} {self.created_at}"

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(CustomUser, related_name="comments", on_delete=models.CASCADE)
    student_error = models.ForeignKey(StudentSubmission, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return f"<Comment: {self.content} for {self.associated_error}>"
    class Meta:
        db_table = 'comments'