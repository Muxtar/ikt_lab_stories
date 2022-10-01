# Generated by Django 4.1 on 2022-09-17 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='category/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('subjets', models.IntegerField(choices=[(1, 'Teklif'), (2, 'Irad')])),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='stories/cover/')),
                ('back_image', models.ImageField(upload_to='stories/back/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=40)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='home.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
