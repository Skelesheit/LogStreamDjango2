# Generated by Django 5.1.3 on 2024-11-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='picture',
            field=models.ImageField(upload_to='news_images/'),
        ),
    ]
