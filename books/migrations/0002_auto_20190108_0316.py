# Generated by Django 2.1.4 on 2019-01-08 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Bussiness', 'Bussiness'), ('Exam_Preparation', 'Exam_Preparation'), ('Technology', 'Technology'), ('Fiction', 'Fiction'), ('Adult', 'Adult'), ('Bed_Time', 'Bed_Time'), ('Literature', 'Literature'), ('Science', 'Science')], max_length=20),
        ),
    ]
