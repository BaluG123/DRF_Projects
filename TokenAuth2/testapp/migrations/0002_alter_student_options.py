# Generated by Django 3.2.3 on 2021-08-17 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-no']},
        ),
    ]
