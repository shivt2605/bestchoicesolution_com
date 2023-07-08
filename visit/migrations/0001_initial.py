# Generated by Django 4.2.2 on 2023-07-08 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visit.city')),
            ],
        ),
        migrations.CreateModel(
            name='Visit_Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_for', models.CharField(max_length=500)),
                ('form_name', models.CharField(max_length=500)),
                ('full_address', models.CharField(max_length=12)),
                ('contact_person', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=12)),
                ('email_id', models.CharField(blank=True, max_length=100, null=True)),
                ('featured_image', models.ImageField(null=True, upload_to='featuredimg')),
                ('map_link', models.TextField(blank=True, null=True)),
                ('comment', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('call_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visit.call_status')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visit.industry')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visit.locality')),
                ('visit_response', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visit.visit_response')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('visit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visit.visit')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(null=True, upload_to='featuredimg')),
                ('visit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visit.visit')),
            ],
        ),
    ]