# Generated by Django 3.2.3 on 2021-08-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=64)),
                ('eage', models.IntegerField()),
                ('eaddr', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['-eno'],
            },
        ),
    ]
