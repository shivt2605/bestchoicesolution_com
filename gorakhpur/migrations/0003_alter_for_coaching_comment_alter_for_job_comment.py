# Generated by Django 4.2.2 on 2023-07-23 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gorakhpur', '0002_alter_response_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_coaching',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='for_job',
            name='comment',
            field=models.TextField(),
        ),
    ]
