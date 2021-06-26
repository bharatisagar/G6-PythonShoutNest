# Generated by Django 3.2.3 on 2021-06-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_friendlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='DateOfBirth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='MobileNo',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='firstName',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='profilePic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]