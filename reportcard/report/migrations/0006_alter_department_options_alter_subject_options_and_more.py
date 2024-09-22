# Generated by Django 4.2.14 on 2024-09-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_rename_s_dep_card_student_department_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['Department_Name']},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['Subject_Name']},
        ),
        migrations.RenameField(
            model_name='department',
            old_name='dep_name',
            new_name='Department_Name',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='score',
            new_name='Score',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject_name',
            new_name='Subject_Name',
        ),
    ]
