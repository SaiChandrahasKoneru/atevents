# Generated by Django 3.2.10 on 2022-04-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atapp', '0014_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
