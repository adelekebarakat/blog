# Generated by Django 4.0.6 on 2023-11-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]