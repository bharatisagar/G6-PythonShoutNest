# Generated by Django 3.2.3 on 2021-06-22 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_reports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('friendId', models.ManyToManyField(db_column='userId', related_name='friendlist_id', to='app.User')),
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userlist_id', to='app.user')),
            ],
        ),
    ]
