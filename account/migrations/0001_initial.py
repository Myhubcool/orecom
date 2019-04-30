# Generated by Django 2.1.3 on 2019-02-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rtlrmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtlrname', models.CharField(max_length=25)),
                ('rtlrid', models.CharField(max_length=25)),
                ('rtlrpassword', models.CharField(max_length=25)),
                ('rtlrconfirmpassword', models.CharField(max_length=25)),
                ('rtlruseremail', models.CharField(max_length=60)),
                ('rtlrshopname', models.CharField(max_length=50)),
                ('rtlrshopid', models.CharField(max_length=40)),
                ('rtlrshoppassword', models.CharField(max_length=40)),
                ('rtlrshopconfirmpassword', models.CharField(max_length=40)),
                ('rtlrshopcity', models.CharField(max_length=30)),
                ('rtlrshopno', models.CharField(max_length=25)),
                ('rtlrshopaddress', models.CharField(max_length=80)),
                ('rtlrphoto', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='usermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('userid', models.CharField(max_length=25)),
                ('userpassword', models.CharField(max_length=25)),
                ('userconfirmpassword', models.CharField(max_length=25)),
                ('useremail', models.CharField(max_length=60)),
            ],
        ),
    ]