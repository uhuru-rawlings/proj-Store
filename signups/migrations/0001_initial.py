# Generated by Django 3.2.12 on 2022-03-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usersignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('useremail', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('userimage', models.ImageField(upload_to='profiles/')),
                ('passwords', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Usersignup',
            },
        ),
    ]
