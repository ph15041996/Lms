# Generated by Django 2.1.4 on 2019-01-10 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20190109_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='quantity',
            new_name='number',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Bussiness', 'Bussiness'), ('Bed_Time', 'Bed_Time'), ('Technology', 'Technology'), ('Adult', 'Adult'), ('Exam_Preparation', 'Exam_Preparation'), ('Literature', 'Literature'), ('Science', 'Science')], max_length=20),
        ),
    ]
