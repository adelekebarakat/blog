# Generated by Django 4.0.6 on 2023-12-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_blog_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_image',
            field=models.ImageField(upload_to='imgblog/'),
        ),
    ]
