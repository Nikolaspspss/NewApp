# Generated by Django 4.1.1 on 2022-09-19 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0004_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='author_post',
        ),
    ]
