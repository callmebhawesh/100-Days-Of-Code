# Generated by Django 4.1.dev20220125165312 on 2022-01-25 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_field',
            new_name='choice_text',
        ),
    ]
