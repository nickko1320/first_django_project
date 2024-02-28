# Generated by Django 5.0.2 on 2024-02-28 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('On-going', 'ongoing'), ('Done', 'Done')], default='Pending', max_length=255),
        ),
    ]
