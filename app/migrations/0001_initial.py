# Generated by Django 4.2.2 on 2023-07-03 07:39

import ckeditor.fields
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
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plat_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_profile', models.ImageField(upload_to='author')),
                ('name', models.CharField(max_length=100, null=True)),
                ('about_author', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('featured_image', models.ImageField(null=True, upload_to='featuredimg')),
                ('featured_video', models.CharField(max_length=300, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('full_description', ckeditor.fields.RichTextField()),
                ('price', models.IntegerField(default=0, null=True)),
                ('discount', models.IntegerField(null=True)),
                ('slug', models.SlugField(blank=True, default='', max_length=500, null=True)),
                ('status', models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT')], max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.plat_form')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categories')),
            ],
        ),
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.service')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.userservice')),
            ],
        ),
        migrations.CreateModel(
            name='Fqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questioned', models.CharField(max_length=200)),
                ('answers', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=500)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service')),
            ],
        ),
    ]
