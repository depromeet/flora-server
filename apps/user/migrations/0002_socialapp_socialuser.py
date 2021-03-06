# Generated by Django 2.1.4 on 2019-01-05 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('google', '구글')], max_length=20, verbose_name='플랫폼 종류')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('client_id', models.CharField(max_length=191, verbose_name='클라이언트 ID')),
                ('secret', models.CharField(max_length=191, verbose_name='시크릿')),
                ('key', models.CharField(blank=True, max_length=191, verbose_name='키')),
            ],
            options={
                'verbose_name': '소셜 앱',
                'verbose_name_plural': '소셜 앱들',
                'db_table': 'social_apps',
            },
        ),
        migrations.CreateModel(
            name='SocialUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='유저')),
            ],
            options={
                'verbose_name': '소셜 유저',
                'verbose_name_plural': '소셜 유저들',
                'db_table': 'social_users',
            },
        ),
    ]
