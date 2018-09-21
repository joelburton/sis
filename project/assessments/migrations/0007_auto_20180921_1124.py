# Generated by Django 2.1.1 on 2018-09-21 18:24

import django.core.validators
from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0006_submissionfile_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='feedback',
            field=models.TextField(blank=True, help_text='Feedback that will be shared with student.'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='grade',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='open', max_length=100, no_check_for_status=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='submissionfile',
            name='comments',
            field=models.TextField(blank=True, help_text='Comments from student.'),
        ),
    ]
