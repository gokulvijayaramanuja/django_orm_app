# Generated by Django 3.1.1 on 2022-12-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20221227_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeid',
            field=models.CharField(help_text='employeeid', max_length=20, primary_key=True, serialize=False),
        ),
    ]
