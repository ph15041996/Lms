# Generated by Django 2.1.4 on 2019-01-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20190111_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Bussiness', 'Bussiness'), ('Exam_Preparation', 'Exam_Preparation'), ('Bed_Time', 'Bed_Time'), ('Literature', 'Literature'), ('Science', 'Science'), ('Technology', 'Technology'), ('Adult', 'Adult')], max_length=20),
        ),
    ]
