# Generated by Django 3.1.1 on 2023-12-14 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20231214_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.course'),
        ),
    ]
