# Generated by Django 3.2.3 on 2021-08-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='epic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
