# Generated by Django 3.1.1 on 2023-12-14 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20231212_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.customuser'),
        ),
    ]
