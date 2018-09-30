# Generated by Django 2.1.1 on 2018-09-30 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='errormessage',
            name='display_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentimageupload',
            name='error_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_submissions', to='main.ErrorMessage'),
        ),
    ]