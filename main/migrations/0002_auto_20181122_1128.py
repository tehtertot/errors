# Generated by Django 2.1.1 on 2018-11-22 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsubmission',
            name='uploader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_sets_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='monthlystack',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stacks', to='main.Language'),
        ),
        migrations.AddField(
            model_name='framework',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frameworks', to='main.Language'),
        ),
        migrations.AddField(
            model_name='errormessage',
            name='framework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language_errors', to='main.Language'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='student_error',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.StudentSubmission'),
        ),
    ]
