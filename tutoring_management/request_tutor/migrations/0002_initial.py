# Generated by Django 4.0.5 on 2022-11-16 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
        ('request_tutor', '0001_initial'),
        ('index', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_to_tutor',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.student'),
        ),
        migrations.AddField(
            model_name='request_to_tutor',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.subject'),
        ),
    ]
