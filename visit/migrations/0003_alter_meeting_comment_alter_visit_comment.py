# Generated by Django 4.2.2 on 2023-07-23 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_meeting_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='comment',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visit',
            name='comment',
            field=models.TextField(),
        ),
    ]
